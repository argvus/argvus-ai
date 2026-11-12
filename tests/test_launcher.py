"""Isolated launcher contracts: never start graphical applications or agents."""
import os
import json
import shutil
from pathlib import Path
import subprocess
import tempfile
import unittest

HELPER = Path(__file__).resolve().parents[1] / "packaging/archlinux/src/usr/bin/argvus-ai"

class Launcher(unittest.TestCase):
    def setUp(self):
        Path("/tmp/argvus").mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir="/tmp/argvus")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.env = dict(os.environ, HOME=str(self.root), PATH=str(self.root), ARGVUS_SYSTEM_CONFIG=str(self.root), LOG=str(self.root / "log"), ARGVUS_AI_CLAUDE_EXECUTABLE=str(self.root / "claude"))
        self.stub("rofi", 'if [ "$1" = "-config" ] && [ "$3" = "-e" ]; then exit 0; fi; /usr/bin/cat >/dev/null; /usr/bin/printf "%s" "${SELECTION:-}"; exit "${ROFI_STATUS:-0}"')
        self.stub("argvus", 'if [ "$1" = i18n ]; then /usr/bin/printf "%s" "${TRANSLATION:-$4}"; exit 0; fi; /usr/bin/printf "%s\\n" "$@" > "$LOG"; exit "${TERMINAL_STATUS:-0}"')

        (self.root / "jq").symlink_to(shutil.which("jq"))
        self.stub("id", 'echo "${FAKE_UID:-1000}"')
        self.stub("mise", 'printf "%s|%s\\n" "$PWD" "$*" >> "$HOME/mise-log"; case "$1" in ls) if [ -x "$HOME/claude" ]; then printf \'[{"version":"1","installed":true}]\'; else printf \'[]\'; fi ;; which) printf "%s\\n" "$HOME/claude" ;; install) exit "${INSTALL_STATUS:-0}" ;; *) exit 99 ;; esac')

    def stub(self, name, body="exit 0"):
        path = self.root / name
        path.write_text("#!/bin/sh\n" + body + "\n")
        path.chmod(0o755)

    def run_helper(self, *args):
        return subprocess.run([str(HELPER), *args], env=self.env, capture_output=True, text=True)

    def test_availability(self):
        for commands in [(), ("opencode",), ("codex",), ("claude",), ("opencode", "codex", "claude"), ("agy",), ("qwen",)]:
            with self.subTest(commands=commands):
                for name in ("opencode", "codex", "claude", "agy", "qwen"):
                    (self.root / name).unlink(missing_ok=True)
                for name in commands:
                    self.stub(name)
                result = self.run_helper("list")
                self.assertEqual(result.returncode, 0)
                self.assertEqual(result.stdout.splitlines(), list(commands))

    def test_menu_launches_each_agent(self):
        for label, command in [("OpenCode", "opencode"), ("OpenAI Codex", "codex"), ("Claude Code", "claude"), ("Google Antigravity", "agy"), ("Qwen Code", "qwen")]:
            self.stub(command)
            self.env["SELECTION"] = label
            self.assertEqual(self.run_helper("menu").returncode, 0)
            expected = ["tui-terminal", "--class", "argvus-ai", "--term", "kitty", "--profile", "ai-agents", "--title", "ARGVUS AI Agent", "--", "argvus", "tui-terminal", "--frame", "AI Agent", "footer.close"] + ([str(HELPER), "run-claude"] if command == "claude" else [str(self.root / command)])
            self.assertEqual((self.root / "log").read_text().splitlines(), expected)

    def test_agy_default_install_and_unavailable(self):
        self.assertNotEqual(self.run_helper("launch", "agy").returncode, 0)
        path = self.root / ".local/bin/agy"
        path.parent.mkdir(parents=True)
        path.write_text("#!/bin/sh\nexit 0\n")
        self.assertNotIn("agy", self.run_helper("list").stdout)
        path.chmod(0o755)
        self.assertIn("agy", self.run_helper("list").stdout)
        self.assertEqual(self.run_helper("launch", "agy").returncode, 0)
        self.assertEqual((self.root / "log").read_text().splitlines()[-1], str(path))

    def test_new_agents_first_launch_and_failure(self):
        for name, command in [("hermes", "hermes"), ("cursor", "agent"), ("kimi", "kimi")]:
            with self.subTest(agent=name):
                self.stub(command)
                result = self.run_helper("run-external", name)
                self.assertEqual(result.returncode, 0, result.stderr)
                (self.root / command).unlink()
                self.stub("mktemp", 'printf "%s" "$HOME/installer"')
                self.stub("curl", 'exit 8')
                self.stub("rm", 'exit 0')
                self.assertNotEqual(self.run_helper("run-external", name).returncode, 0)
                self.env["FAKE_UID"] = "0"
                self.assertNotEqual(self.run_helper("run-external", name).returncode, 0)
                self.env["FAKE_UID"] = "1000"

    def test_kimi_native_install_is_reused(self):
        path = self.root / ".kimi-code/bin/kimi"
        path.parent.mkdir(parents=True)
        path.write_text("#!/bin/sh\nexit 0\n")
        path.chmod(0o755)
        self.stub("curl", 'exit 99')
        self.assertIn("kimi", self.run_helper("list").stdout)
        self.assertEqual(self.run_helper("run-external", "kimi").returncode, 0)

    def test_empty_menu(self):
        (self.root / "mise").unlink()
        self.assertNotEqual(self.run_helper("menu").returncode, 0)
        self.assertFalse((self.root / "log").exists())

    def test_cancel_empty_and_rofi_failure(self):
        self.stub("opencode")
        for status, expected in [("1", 0), ("0", 0), ("2", 1)]:
            self.env["ROFI_STATUS"] = status
            self.assertEqual(self.run_helper("menu").returncode, expected)
            self.assertFalse((self.root / "log").exists())

    def test_invalid(self):
        self.assertEqual(self.run_helper("launch", "bad; touch injected").returncode, 2)
        self.assertEqual(self.run_helper("unknown").returncode, 2)

    def test_terminal_failure(self):
        self.stub("codex")
        self.env["TERMINAL_STATUS"] = "7"
        self.assertEqual(self.run_helper("launch", "codex").returncode, 1)

    def test_removed_and_nonexecutable(self):
        self.stub("claude")
        self.assertIn("claude", self.run_helper("list").stdout)
        (self.root / "claude").unlink()
        self.assertEqual(self.run_helper("run-claude").returncode, 1)
        self.stub("claude")
        (self.root / "claude").chmod(0o644)
        self.assertNotIn("claude", self.run_helper("list").stdout)



    def test_status(self):
        (self.root / "mise").unlink()
        self.assertNotEqual(self.run_helper("status", "--check").returncode, 0)
        self.assertEqual(json.loads(self.run_helper("status").stdout), {"text": ""})
        self.stub("opencode")
        self.assertEqual(self.run_helper("status", "--check").returncode, 0)
        self.assertTrue(json.loads(self.run_helper("status").stdout)["text"])

    def test_json_escaping(self):
        self.stub("opencode")
        self.env["TRANSLATION"] = 'Agents "quoted"\nsecond line\\backslash'
        result = self.run_helper("status")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)["tooltip"], self.env["TRANSLATION"])






    def test_queries_never_use_mise(self):
        self.stub("claude")
        self.env["ROFI_STATUS"] = "1"
        for args in [("list",), ("status",), ("menu",), ("launch", "claude")]:
            self.run_helper(*args)
        self.assertNotIn("install ", (self.root / "mise-log").read_text())


    def test_first_launch_install_and_path(self):
        template = self.root / "agent-template"
        template.write_text('#!/bin/sh\nprintf "%s" "$PATH" > "$LOG"\n')
        template.chmod(0o755)
        original = (self.root / "mise").read_text()
        (self.root / "mise").write_text(original.replace('install) exit "${INSTALL_STATUS:-0}"', 'install) [ "${INSTALL_STATUS:-0}" = 0 ] || exit "$INSTALL_STATUS"; /usr/bin/cp "$HOME/agent-template" "$HOME/claude"'))
        result = self.run_helper("run-claude")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(str(self.root) + "|install claude", (self.root / "mise-log").read_text())
        self.assertTrue((self.root / "log").read_text().startswith(str(self.root) + ":"))
        (self.root / "mise-log").unlink()
        self.assertEqual(self.run_helper("run-claude").returncode, 0)
        self.assertNotIn("install ", (self.root / "mise-log").read_text())

    def test_install_failure_and_root(self):
        self.env["INSTALL_STATUS"] = "8"
        self.assertEqual(self.run_helper("run-claude").returncode, 8)
        self.env["FAKE_UID"] = "0"
        self.assertEqual(self.run_helper("run-claude").returncode, 1)

    def test_uninstalled_claude_can_be_selected(self):
        self.env["SELECTION"] = "Claude Code"
        self.assertEqual(self.run_helper("menu").returncode, 0)
        self.assertIn("run-claude", (self.root / "log").read_text())
        self.assertFalse((self.root / "mise-log").exists())
        self.assertEqual(self.run_helper("status", "--check").returncode, 0)

if __name__ == "__main__":
    unittest.main()
