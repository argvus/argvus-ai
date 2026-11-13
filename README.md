# ARGVUS AI

OpenCode, Codex and Qwen Code are Pacman dependencies. Claude Code installs on first launch: select Claude Code in the Rofi agents menu or its application launcher entry. The ARGVUS terminal opens, runs `mise install claude` as the current user if necessary, resolves the installed executable, adds its directory to that process PATH and starts Claude. Later launches reuse the installed version. No agent installation runs during package installation, as root or at login. No manual command is required.

The menu offers Claude when mise is present, even before installation. `argvus-ai list` reports installed agents only; `status` reports whether the menu has an installed or installable agent. Queries/cancelled menus never download. Installation errors are displayed and may be retried by opening Claude again. No shell startup files or personal PATH configuration are modified; the augmented PATH belongs to the running Claude process and its children. Existing credentials and mise tools are preserved.

SUPER + A and the taskbar icon call argvus-ai menu; desktop entries call argvus-ai launch AGENT. Claude resolution queries mise from HOME, while the launched agent retains the caller working directory. make validate and make build produce build/dist artifacts. AI-assisted implementation requiring human review before upstream submission.

The package owns the Lua binding module usr/share/argvus/ai/hyprland.lua. Update argvus-hyprland too: its optional loader and Pacman hook activate/remove SUPER + A using native config autoreload. User overrides for app.ai remain authoritative. The Control Center catalog and both cheatsheets use the same shortcut.

Documentation: [English](docs/en/index.md) · [Português brasileiro](docs/pt-br/index.md).

Agents run in a centered floating Kitty window titled `ARGVUS AI Agent`, with an ARGVUS frame and a localized **Ctrl + E** close hint. Closing the frame terminates its child agent.

The dedicated `ai-agents` Kitty profile hides tabs and disables inherited tab, split and fullscreen shortcuts. It keeps clipboard shortcuts and writes its own runtime configuration under the ARGVUS cache.

Google Antigravity CLI (`agy`) is installed separately using the [official instructions](https://antigravity.google/docs/getting-started?tab=cli). The selector detects it in PATH or `~/.local/bin/agy`.

Hermes, Cursor CLI and Kimi Code install using their official installers on first launch as the current user. Select them in the menu or run `argvus-ai launch hermes`, `argvus-ai launch cursor` or `argvus-ai launch kimi`. Authentication and updates are managed by each agent.

Gemini CLI is included through Arch's `gemini-cli` package dependency. Use `argvus-ai list` to check availability and `argvus-ai launch gemini` to start it; Google authentication is handled by Gemini CLI.
