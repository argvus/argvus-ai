---
title: Installation
description: Install argvus-ai and understand how each agent is provided.
---

## Install the package

On Arch Linux with the ARGVUS repositories configured, once `argvus-ai` is published there:

```sh
sudo pacman -S argvus-ai
```

For an unpublished local build, run `make validate` and `make build` in the `argvus-ai` source repository, then install the resulting `.pkg.tar.zst` from `build/dist/` with `sudo pacman -U /path/to/package.pkg.tar.zst`. Pacman must be able to resolve its dependencies, including the master `argvus` package.

The package requires `argvus`, `rofi`, `jq`, `mise`, `opencode` and `openai-codex`; Arch provides `/bin/sh` through `bash`. OpenCode runs as `opencode`, and the `openai-codex` package provides `codex`.

## Desktop integration

Use the updated `argvus-hyprland` and `argvus-taskbar` packages. Hyprland loads the optional Lua module supplied by `argvus-ai`. The integration's Pacman hook refreshes the standard system configuration after installation or removal. A custom root configuration or disabled autoreload may require an explicit reload. Existing personal shortcut overrides remain authoritative.

The updated `argvus-appearance` projector preserves the taskbar module and respects **Control Center > Appearance > Taskbar > Icons > Optional modules > AI Agents**. The option is enabled by default; click **Apply** after changing it. Enabling it does not install agents.

## Claude Code on first use

Select Claude Code from the Rofi selector or application launcher. The ARGVUS terminal opens and runs `mise install claude` as your regular user if no installed version is found. Network access is needed for this first installation. The wrapper resolves the installed executable and adds its directory to the launched process PATH; it does not edit shell startup files or install as root. Later launches reuse the installation.

## Remove

```sh
sudo pacman -R argvus-ai
```

The package-owned Lua module and desktop entries are removed, and the taskbar module hides when its helper is absent. The standard Hyprland configuration autoreloads to remove the bind. User-owned mise tools, agent settings and credentials are retained. Pacman does not automatically remove the agent dependencies with this command.

The `qwen-code` dependency provides the `qwen` executable.
