---
title: Agentes de IA
description: Abre agentes de programación desde el escritorio de ARGVUS.
---
`argvus-ai` es una integración opcional de escritorio para **OpenCode**, **OpenAI Codex** y **Claude Code**. Proporciona un selector compartido Rofi, entradas de lanzador de aplicaciones y el icono de robot en el grupo de utilidades de la barra de tareas. Los agentes se ejecutan en una nueva ventana de terminal ARGVUS y conservan el directorio de trabajo del llamador.

Abre el selector con **SUPER + A** o haz clic en **nf-md-robot** en la barra de tareas, junto a los controles de micrófono y audio. También puedes seleccionar un agente individual en el lanzador de aplicaciones.

OpenCode y Codex se instalan como dependencias de paquete. Claude Code se instala con mise, como tu usuario, solo cuando lo seleccionas por primera vez. Instalar el paquete, abrir/cancelar el selector o verificar el estado nunca descarga Claude. El paquete no configura cuentas, claves API o suscripciones; sigue las indicaciones de autenticación del agente seleccionado.

Lea [Installation](/docs/argvus-ai/installation/) y [Usage and troubleshooting](/docs/argvus-ai/usage/).

## Idiomas

El `ai` catálogo se suministra en todos los 18 ARGVUS idiomas de interfaz y utiliza el `argvus i18n` selección e ingles. El idioma de interfaz seleccionado se almacena como `ARGVUS_LANGUAGE` en el usuario `locale.conf`; el sistema regional local sigue siendo separado. Las traducciones se instalan como datos sin escribir la configuración del usuario.

## Agentes disponibles

La integración es compatible con OpenCode, Codex y Qwen Code, incluidos en el paquete; con Claude Code mediante mise; con Antigravity, si se instala por separado; y con Hermes, Cursor CLI y Kimi, que se instalan con sus instaladores oficiales al ejecutarlos por primera vez. Consulta la [guía de uso](usage/) para saber cómo enumerar y desinstalar los agentes externos gestionados por ARGVUS.
