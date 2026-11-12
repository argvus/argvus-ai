---
title: Агенты ИИ
description: Открывайте программные агенты с рабочего стола ARGVUS.
---
`argvus-ai` — это необязательная интеграция для рабочего стола для **OpenCode**, **OpenAI Codex** и **Claude Code**. Она предоставляет общий селектор Rofi, записи для запуска приложений и иконку робота в группе утилит панели задач. Агентов можно запускать в новом окне терминала ARGVUS, при этом сохраняется рабочая директория вызывающего процессa.

Откройте селектор с помощью **SUPER + A** или нажмите **nf-md-robot** в панели задач, рядом с микрофоном и элементами управления звуком. Также можно выбрать отдельного агента через запуск приложений.

OpenCode и Codex устанавливаются как зависимости пакета. Claude Code устанавливается через mise от имени вашего пользователя только при первом его выборе. Установка пакета, открытие/отмена селектора или проверка статуса никогда не загружает Claude. Пакет не настраивает аккаунты, ключи API или подписки; следуйте инструкциям аутентификации выбранного агента.

Прочитайте [Установку](/docs/argvus-ai/installation/)] и [Использование и устранение неполадок](/docs/argvus-ai/usage/)].

## Языки

Каталог `ai` предоставляется на всех десяти языках ARGVUS и использует общий выбор `argvus i18n` с английским вариантом по умолчанию. Переводы устанавливаются как данные без записи пользовательской конфигурации.

## Supported agents

The integration supports package-provided OpenCode, Codex and Qwen Code; Claude Code through mise; Antigravity when installed separately; and Hermes, Cursor CLI and Kimi through their official installers on first launch. Use the [usage guide](usage/) for listing and uninstalling ARGVUS-managed external agents.
