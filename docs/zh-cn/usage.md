---
title: 使用与故障排除
description: 选择代理，控制任务栏图标并诊断缺失的集成。
---
## 打开代理

按 **SUPER + A**，点击任务栏上的机器人或选择代理的应用入口。选择器提供可执行的 OpenCode/Codex 安装，并在首次使用时提供 Claude Code 安装，当 mise 存在时。**Esc** 可以取消，而不会启动或下载任何内容。

终端会继承调用者的工作目录；图形界面启动通常从会话的主目录开始。当你需要特定的工作目录时，请从项目终端启动代理。

## 任务栏可见性

打开 **控制中心 > 外观 > 任务栏 > 图标 > 可选模块**，切换 **AI 代理**，然后点击 **应用**。该机器人属于 `group/right-2`；如果其抽屉被折叠，请展开实用工具组。首选项是 `/taskbar/icons/ai_agents_enabled`，默认值为 true，并且在重生后仍然有效。它只控制图标：快捷方式和桌面条目仍然可用。运行时可用性仍然可以隐藏已启用的图标。

## 诊断命令

```sh
argvus-ai list
argvus-ai status
argvus-ai status --check
argvus-ai menu
argvus-ai launch opencode
argvus-ai launch codex
argvus-ai launch claude
```
`list` 仅报告已安装的代理。`status` 输出 Waybar JSON，而 `status --check` 通过其退出状态报告是否存在已安装或可安装的菜单选项。只有选择/启动 Claude 才能开始其安装；`run-claude` 是内部终端入口点。

如果快捷方式仍然使用旧的组合键，请在控制中心的键盘快捷键页面检查其个人覆盖；打包的默认设置不会覆盖它。如果在应用外观设置后机器人消失，请更新 `argvus-appearance` 并重新生成/应用任务栏设置。避免直接编辑生成的 Waybar/Lua 文件。

如果 Claude 安装失败，请检查终端错误、网络访问情况以及已安装的 mise 版本，然后再次选择 Claude。mise 查询从主目录运行，因此特定项目的配置不会选择不同的工具。图形界面的 PATH 中不需要 mise shims。OpenCode/Codex 发现使用图形界面 PATH，而不使用 shell 别名或交互式启动脚本。

返回 [AI Agents](/docs/argvus-ai/)。

Agents 会在一个居中的浮动 Kitty 窗口中打开，标题为 `ARGVUS AI Agent`，带有 ARGVUS 页眉和页脚。按 **Ctrl + E** 关闭代理窗口。此快捷键由框架保留；Esc 和 Ctrl+C 仍可用于代理。

专用的 Kitty 配置文件 `ai-agents` 会隐藏标签页并清除继承的标签页、拆分和全屏快捷键。剪贴板快捷键 Ctrl+Shift+C 和 Ctrl+Shift+V 仍然可用。其生成的配置位于 ARGVUS 缓存目录下的 `kitty-tui/kitty-ai-agents.conf`。Hyprland 模块包会使类 `argvus-ai` 的窗口浮动并居中，尺寸为 1399 × 920。

## 卸载智能体

`argvus-ai list` 会列出已安装的智能体。运行 `argvus-ai uninstall`，选择由 ARGVUS 管理的 Hermes、Cursor CLI 或 Kimi 安装，然后确认卸载。也可直接运行 `argvus-ai uninstall hermes`、`argvus-ai uninstall cursor` 或 `argvus-ai uninstall kimi`。不会改动 ARGVUS 之外的安装；但显式指定 Cursor 的命令会识别旧版 Cursor CLI，前提是 `~/.local/bin/agent` 指向 `~/.local/share/cursor-agent/versions/` 内的可执行文件。Hermes 使用其官方卸载程序。Cursor 和 Kimi 的可执行文件会被移除，用户设置、会话和凭据会保留。
