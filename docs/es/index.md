---
title: Agentes de IA
description: Abre agentes de programación desde el escritorio de ARGVUS.
---
`argvus-ai` es una integración opcional de escritorio para **OpenCode**, **OpenAI Codex** y **Claude Code**. Proporciona un selector compartido Rofi, entradas de lanzador de aplicaciones y el icono de robot en el grupo de utilidades de la barra de tareas. Los agentes se ejecutan en una nueva ventana de terminal ARGVUS y conservan el directorio de trabajo del llamador.

Abre el selector con **SUPER + A** o haz clic en **nf-md-robot** en la barra de tareas, junto a los controles de micrófono y audio. También puedes seleccionar un agente individual en el lanzador de aplicaciones.

OpenCode y Codex se instalan como dependencias de paquete. Claude Code se instala con mise, como tu usuario, solo cuando lo seleccionas por primera vez. Instalar el paquete, abrir/cancelar el selector o verificar el estado nunca descarga Claude. El paquete no configura cuentas, claves API o suscripciones; sigue las indicaciones de autenticación del agente seleccionado.

Lea [Installation](/docs/argvus-ai/installation/) y [Usage and troubleshooting](/docs/argvus-ai/usage/).

## Idiomas

El catálogo `ai` se proporciona en los diez idiomas ARGVUS y utiliza la selección compartida `argvus i18n` y la opción de respaldo en inglés. Las traducciones se instalan como datos sin modificar la configuración del usuario.

## Agentes disponibles

La integración ofrece OpenCode, Codex y Qwen Code mediante el paquete; Claude Code mediante mise; Antigravity si se instala por separado; y Hermes, Cursor CLI y Kimi mediante sus instaladores oficiales en el primer inicio. Consulta la [guía de uso](usage/) para listar y desinstalar agentes externos gestionados por ARGVUS.
