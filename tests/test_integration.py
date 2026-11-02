"""Workspace integration contracts; package checks use test_launcher.py."""
import json
from pathlib import Path
import re
import unittest
import os
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[3]
PAYLOAD = ROOT / "de/argvus-ai/packaging/archlinux/src"

class Integration(unittest.TestCase):
    def test_taskbar(self):
        source = (ROOT / "de/argvus-taskbar/src/usr/share/argvus/taskbar/config/argvus-taskbar.jsonc").read_text()
        source = re.sub(r'"(?:\\.|[^"\\])*"|//[^\n]*|/\*[\s\S]*?\*/', lambda match: match[0] if match[0].startswith('"') else '', source)
        config = json.loads(source)
        self.assertEqual(config["group/right-2"]["modules"].count("custom/ai"), 1)
        module = config["custom/ai"]
        self.assertIn("command -v argvus-ai", module["exec-if"])
        self.assertIn("argvus-ai status --check", module["exec-if"])
        self.assertEqual(module["exec"], "argvus-ai status")
        self.assertIn("argvus-ai menu", module["on-click"])

    def test_hyprland(self):
        source = (ROOT / "de/argvus-hyprland/src/usr/share/argvus/hyprland/config/hyprland.lua").read_text()
        module = (PAYLOAD / "usr/share/argvus/ai/hyprland.lua").read_text()
        self.assertIn('if _path_exists(_ai_module) then', source)
        self.assertIn('pcall(function()', source)
        self.assertIn('register(_argvus_bind, mod)', source)
        self.assertLess(source.index('register(_argvus_bind, mod)'), source.index('_load_user_override("bindings.lua")'))
        self.assertEqual(module.count('mod .. " + A"'), 1)
        self.assertIn('"app.ai"', module)
        self.assertIn('exec argvus-ai menu', module)
        manifest = json.loads((ROOT / "de/argvus-hyprland/src/usr/share/argvus/hyprland/keybindings.json").read_text())
        binding = [item for item in manifest["bindings"] if item["id"] == "app.ai"]
        self.assertEqual(len(binding), 1)
        self.assertEqual(binding[0]["keys"], "SUPER + A")
        for locale in ["en-US", "pt-BR"]:
            catalog = json.loads((ROOT / f"de/argvus/resources/locales/{locale}/control-center.json").read_text())
            self.assertIn(binding[0]["description_key"], catalog)
        hook = (ROOT / "de/argvus-hyprland/src/usr/share/libalpm/hooks/95-argvus-ai-hyprland.hook").read_text()
        for action in ["Install", "Upgrade", "Remove"]:
            self.assertIn("Operation = " + action, hook)
        self.assertIn("Target = usr/share/argvus/ai/hyprland.lua", hook)

    @unittest.skipUnless(shutil.which("Hyprland"), "native Hyprland validator unavailable")
    def test_native_optional_module_lifecycle(self):
        source = (ROOT / "de/argvus-hyprland/src/usr/share/argvus/hyprland/config/hyprland.lua").read_text()
        loader = source[source.index('local _ai_module ='):source.index('_load_user_override("monitors.lua")')]
        module = (PAYLOAD / "usr/share/argvus/ai/hyprland.lua").read_text()
        Path("/tmp/argvus").mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir="/tmp/argvus") as directory:
            root = Path(directory)
            (root / "ai").mkdir()
            path = root / "ai/hyprland.lua"
            fixture = root / "hyprland.lua"
            prelude = 'local _system_config = ' + json.dumps(directory) + '\nlocal mod = "SUPER"\nlocal count = 0\nlocal function _path_exists(p) local f = io.open(p); if f then f:close(); return true end return false end\nlocal function _argvus_bind(id, keys, action) assert(id == "app.ai"); assert(keys == "SUPER + A"); count = count + 1; hl.bind(keys, action) end\n'
            for state, expected in [("installed", 1), ("removed", 0), ("broken", 0)]:
                if state == "installed":
                    path.write_text(module)
                elif state == "removed":
                    path.unlink()
                else:
                    path.write_text('error("invalid optional module")')
                fixture.write_text(prelude + loader + f'\nassert(count == {expected})\n')
                result = subprocess.run(["Hyprland", "--verify-config", "--config", str(fixture)], env=dict(os.environ, XDG_RUNTIME_DIR=directory), capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, (result.stdout + result.stderr)[-2000:])

    def test_desktop_entries(self):
        for name, agent in [("opencode", "opencode"), ("openai-codex", "codex"), ("claude-code", "claude")]:
            entry = (PAYLOAD / f"usr/share/applications/argvus-{name}.desktop").read_text()
            self.assertIn(f"Exec=argvus-ai launch {agent}\n", entry)
            self.assertIn("Terminal=false\n", entry)
            self.assertIn("TryExec=argvus-ai\n", entry)

    def test_no_package_install_hook(self):
        self.assertFalse((PAYLOAD / "usr/lib/systemd").exists())
        self.assertFalse((PAYLOAD / "usr/bin/claude").exists())
        self.assertFalse((PAYLOAD / "usr/lib/argvus/ai/install-claude").exists())
        for kind in ["local", "remote"]:
            pkgbuild = (ROOT / f"de/argvus-ai/packaging/archlinux/pkgbuilds/{kind}/PKGBUILD").read_text()
            self.assertNotIn("install=", pkgbuild)

    def test_catalogs(self):
        root = PAYLOAD / "usr/share/argvus/i18n"
        en = json.loads((root / "en-US/ai.json").read_text())
        pt = json.loads((root / "pt-BR/ai.json").read_text())
        self.assertEqual(en.keys(), pt.keys())
        self.assertTrue(pt["usage"].startswith("Uso:"))
        for key in en:
            self.assertEqual(re.findall(r"\{[^}]+\}", en[key]), re.findall(r"\{[^}]+\}", pt[key]))

if __name__ == "__main__":
    unittest.main()
