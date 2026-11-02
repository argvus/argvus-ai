---
title: AI Agents
description: Open programming agents from the ARGVUS desktop.
---

`argvus-ai` is an optional desktop integration for **OpenCode**, **OpenAI Codex** and **Claude Code**. It provides a shared Rofi selector, application launcher entries and the robot icon in the taskbar utility group. Agents run in a new ARGVUS terminal window and retain the caller's working directory.

Open the selector with **SUPER + A** or click **nf-md-robot** in the taskbar, next to the microphone and audio controls. You can also select an individual agent in the applications launcher.

OpenCode and Codex are installed as package dependencies. Claude Code is installed with mise, as your user, only when you first select it. Installing the package, opening/cancelling the selector or checking status never downloads Claude. The package does not configure accounts, API keys or subscriptions; follow the selected agent's authentication prompts.

Read [Installation](/docs/argvus-ai/installation/) and [Usage and troubleshooting](/docs/argvus-ai/usage/).
