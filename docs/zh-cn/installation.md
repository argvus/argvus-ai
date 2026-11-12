---
title: 安装
description: 安装 argvus-ai 并了解每个代理是如何提供的。
---
## 安装软件包

在配置了 ARGVUS 仓库的 Arch Linux 上，一旦 argvus-ai 发布后：

```sh
sudo pacman -S argvus-ai
```
对于未发布的本地构建，在 `argvus-ai` 源代码仓库中运行 `make validate` 和 `make build`，然后使用 `argvus-ai` 从 build/dist/ 安装生成的 `.pkg.tar.zst`。Pacman 必须能够解析其依赖关系，包括主  `build/dist/` `sudo pacman -U /path/to/package.pkg.tar.zst` `argvus` 软件包。

该软件包需要 `argvus`、`rofi`、`jq`、`mise`、`opencode` 和 `openai-codex`；Arch 通过 bash 提供 `/bin/sh`。OpenCode 以  `bash` `opencode` 运行，而 `openai-codex` 软件包提供 `codex`。

## 桌面集成

使用更新的 `argvus-hyprland` 和 `argvus-taskbar` 软件包。Hyprland 加载 `argvus-ai` 提供的可选 Lua 模块。集成的 Pacman 钩子在安装或删除后刷新标准系统配置。自定义根配置或禁用自动重载可能需要显式重新加载。现有的个人快捷方式覆盖仍然具有优先权。

更新后的 `argvus-appearance` 投影仪保留了任务栏模块，并遵循 **控制中心 > 外观 > 任务栏 > 图标 > 可选模块 > AI 代理** 设置。该选项默认启用；更改后请点击 **应用**。启用此选项不会安装代理。

## 首次使用 Claude Code

从 Rofi 选择器或应用启动器中选择 Claude Code。如果未找到已安装版本，ARGVUS 终端将打开并以常规用户身份运行 `mise install claude`。首次安装需要网络访问。该包装程序会解析已安装的可执行文件并将其目录添加到启动进程的 PATH 中；它不会编辑 shell 启动文件或以 root 身份安装。后续启动会重复使用该安装。

## 删除

```sh
sudo pacman -R argvus-ai
```
包管理的 Lua 模块和桌面条目已被移除，当其辅助程序不存在时任务栏模块会隐藏。标准的 Hyprland 配置会自动重载以移除绑定。用户拥有的 mise 工具、代理设置和凭证会被保留。Pacman 不会使用此命令自动移除代理依赖项。

The ARGVUS AI package does not install external agents at package-install time. Hermes, Cursor CLI and Kimi install on first launch; their user data remains outside the package. See the usage guide for removal instructions.
