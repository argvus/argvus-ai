# ARGVUS AI

OpenCode and Codex are Pacman dependencies. Claude Code installs on first launch: select Claude Code in the Rofi agents menu or its application launcher entry. The ARGVUS terminal opens, runs `mise install claude` as the current user if necessary, resolves the installed executable, adds its directory to that process PATH and starts Claude. Later launches reuse the installed version. No agent installation runs during package installation, as root or at login. No manual command is required.

The menu offers Claude when mise is present, even before installation. `argvus-ai list` reports installed agents only; `status` reports whether the menu has an installed or installable agent. Queries/cancelled menus never download. Installation errors are displayed and may be retried by opening Claude again. No shell startup files or personal PATH configuration are modified; the augmented PATH belongs to the running Claude process and its children. Existing credentials and mise tools are preserved.

SUPER + A and the taskbar icon call argvus-ai menu; desktop entries call argvus-ai launch AGENT. Claude resolution queries mise from HOME, while the launched agent retains the caller working directory. make validate and make build produce build/dist artifacts. AI-assisted implementation requiring human review before upstream submission.

The package owns the Lua binding module usr/share/argvus/ai/hyprland.lua. Update argvus-hyprland too: its optional loader and Pacman hook activate/remove SUPER + A using native config autoreload. User overrides for app.ai remain authoritative. The Control Center catalog and both cheatsheets use the same shortcut.
