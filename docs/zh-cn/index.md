---
title: 人工智能代理
description: 从 ARGVUS 桌面打开编程代理。
---
`argvus-ai` 是 **OpenCode**、**OpenAI Codex** 和 **Claude Code** 的可选桌面集成。它提供共享的 Rofi 选择器、应用启动器条目以及任务栏实用程序组中的机器人图标。代理会在新的 ARGVUS 终端窗口中运行，并保留调用者的工作目录。

通过 **SUPER + A** 打开选择器，或者点击任务栏中麦克风和音频控制旁的 **nf-md-robot**。你也可以在应用启动器中选择单个代理。

OpenCode 和 Codex 已作为软件包依赖安装。Claude Code 仅在你首次选择时，以你的用户身份通过 mise 安装。安装软件包、打开/取消选择器或检查状态时，从不会下载 Claude。该软件包不会配置账户、API 密钥或订阅；请按照所选代理的身份验证提示操作。

阅读 [Installation](/docs/argvus-ai/installation/) 和 [Usage and troubleshooting](/docs/argvus-ai/usage/)。

## 语言

`ai` 目录提供所有十种 ARGVUS 语言，并使用共享的 `argvus i18n` 选择和英语回退。翻译作为数据安装，而不会写入用户配置。

## 支持代理

此集成支持软件包提供的 OpenCode、Codex 和 Qwen Code，通过 mise 安装的 Claude Code，单独安装后使用的 Antigravity，以及首次启动时通过官方安装程序安装的 Hermes、Cursor CLI 和 Kimi。有关如何查看 ARGVUS 管理的外部代理列表并卸载它们，请参阅[使用指南](usage/)。
