---
title: Usage and troubleshooting
description: Select agents, control the taskbar icon and diagnose missing integrations.
---

## Open an agent

Press **SUPER + A**, click the taskbar robot or choose an agent's application entry. The selector offers executable OpenCode/Codex installations and offers Claude Code for first-use installation when mise exists. **Esc** cancels without launching or downloading anything.

The terminal inherits the caller's working directory; graphical launches usually start from the session's home directory. Start an agent from a project terminal when you need a particular working directory.

## Taskbar visibility

Open **Control Center > Appearance > Taskbar > Icons > Optional modules**, toggle **AI Agents**, then **Apply**. The robot belongs to `group/right-2`; if its drawer is collapsed, expand the utilities group. The preference is `/taskbar/icons/ai_agents_enabled`, defaults to true, and survives regeneration. It controls only the icon: shortcuts and desktop entries remain available. Runtime availability can still hide an enabled icon.

## Diagnostic commands

```sh
argvus-ai list
argvus-ai status
argvus-ai status --check
argvus-ai menu
argvus-ai launch opencode
argvus-ai launch codex
argvus-ai launch claude
```

`list` reports installed agents only. `status` emits Waybar JSON, while `status --check` reports whether there is an installed or installable menu choice through its exit status. Only selecting/launching Claude can start its installation; `run-claude` is an internal terminal entry point.

If the shortcut still uses the old combination, inspect its personal override in Control Center's keyboard shortcuts page; packaged defaults do not overwrite it. If the robot disappears after applying appearance settings, update `argvus-appearance` and regenerate/apply the taskbar settings. Avoid editing generated Waybar/Lua files directly.

If Claude installation fails, check terminal errors, network access and the installed mise version, then select Claude again. mise queries run from home so a project-specific configuration does not select a different tool. The wrapper does not require mise shims in the graphical PATH. OpenCode/Codex discovery uses the graphical PATH, without shell aliases or interactive startup scripts.

Return to [AI Agents](/docs/argvus-ai/).

Agents open in a centered floating Kitty window titled `ARGVUS AI Agent`, with an ARGVUS header and footer. Press **Ctrl + E** to close the agent window. This shortcut is reserved by the frame; Esc and Ctrl+C remain available to the agent.

The dedicated Kitty profile `ai-agents` hides tabs and clears inherited shortcuts for tabs, splits and fullscreen. Clipboard shortcuts Ctrl+Shift+C and Ctrl+Shift+V remain available. Its generated configuration is `kitty-tui/kitty-ai-agents.conf` under the ARGVUS cache directory. The package Hyprland module floats and centers windows with class `argvus-ai` at 1399 × 920.

Google Antigravity CLI (`agy`) must be installed separately using the [official instructions](https://antigravity.google/docs/getting-started?tab=cli). It is detected in the graphical PATH or `~/.local/bin/agy`. Launch it with `argvus-ai launch agy`.

Qwen Code is provided by the `qwen-code` Arch package. Select it from the menu or run `argvus-ai launch qwen`.

Hermes, Cursor CLI and Kimi Code install using their official installers on first launch as the current user. Select them in the menu or run `argvus-ai launch hermes`, `argvus-ai launch cursor` or `argvus-ai launch kimi`. Authentication and updates are managed by each agent.

Kimi installations in `~/.kimi-code/bin/kimi` are detected without changing the graphical PATH. If installation fails, check the terminal output.
