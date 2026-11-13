---
title: Uso y solución de problemas
description: Seleccione agentes, controle el icono de la barra de tareas y diagnostique integraciones faltantes.
---
## Abrir un agente

Presiona **SUPER + A**, haz clic en el robot de la barra de tareas o elige una entrada de aplicación de un agente. El selector ofrece instalaciones ejecutables de OpenCode/Codex y ofrece Claude Code para la instalación de primer uso cuando mise existe. **Esc** cancela sin lanzar ni descargar nada.

El terminal hereda el directorio de trabajo del llamador; los lanzamientos gráficos usualmente comienzan desde el directorio de inicio de la sesión. Inicia un agente desde un terminal de proyecto cuando necesites un directorio de trabajo en particular.

## Visibilidad de la barra de tareas

Abre **Centro de Control > Apariencia > Barra de tareas > Iconos > Módulos opcionales**, activa **Agentes de IA**, luego **Aplicar**. El robot pertenece a `group/right-2`; si su cajón está colapsado, expande el grupo de utilidades. La preferencia es `/taskbar/icons/ai_agents_enabled`, por defecto es verdadera y sobrevive a la regeneración. Controla solo el icono: los accesos directos y entradas de escritorio siguen estando disponibles. La disponibilidad en tiempo de ejecución aún puede ocultar un icono activado.

## Comandos de diagnóstico

```sh
argvus-ai list
argvus-ai status
argvus-ai status --check
argvus-ai menu
argvus-ai launch opencode
argvus-ai launch codex
argvus-ai launch claude
```
`list` informa solo sobre los agentes instalados. `status` emite JSON de Waybar, mientras que `status --check` informa si hay una opción de menú instalada o instalable a través de su estado de salida. Solo seleccionar/lanzar a Claude puede iniciar su instalación; `run-claude` es un punto de entrada interno del terminal.

Si el acceso directo aún usa la combinación antigua, inspecciona su anulación personal en la página de atajos de teclado del Centro de Control; los valores predeterminados empaquetados no lo sobrescriben. Si el robot desaparece después de aplicar la configuración de apariencia, actualiza `argvus-appearance` y regenera/aplica la configuración de la barra de tareas. Evita editar directamente los archivos generados de Waybar/Lua.

Si la instalación de Claude falla, verifique los errores en la terminal, el acceso a la red y la versión de mise instalada, luego seleccione Claude nuevamente. Las consultas de mise se ejecutan desde el directorio home, por lo que una configuración específica del proyecto no selecciona una herramienta diferente. El envoltorio no requiere shims de mise en el PATH gráfico. La detección de OpenCode/Codex utiliza el PATH gráfico, sin alias de shell ni scripts de inicio interactivos.

Regrese a [AI Agents](/docs/argvus-ai/).

Los agentes se abren en una ventana flotante centrada de Kitty titulada `ARGVUS AI Agent`, con un encabezado y pie ARGVUS. Presione **Ctrl + E** para cerrar la ventana del agente. Este atajo está reservado por el marco; Esc y Ctrl+C permanecen disponibles para el agente.

El perfil dedicado de Kitty `ai-agents` oculta las pestañas y elimina los accesos directos heredados para pestañas, divisiones y pantalla completa. Los atajos del portapapeles Ctrl+Shift+C y Ctrl+Shift+V permanecen disponibles. Su configuración generada es `kitty-tui/kitty-ai-agents.conf` bajo el directorio de caché ARGVUS. El módulo del paquete Hyprland flota y centra ventanas con la clase `argvus-ai` a 1399 × 920.

## Desinstalar agentes

`argvus-ai list` muestra los agentes instalados. Ejecuta `argvus-ai uninstall` para seleccionar una instalación de Hermes, Cursor CLI o Kimi gestionada por ARGVUS y confirma la eliminación. También puedes ejecutar `argvus-ai uninstall hermes`, `argvus-ai uninstall cursor` o `argvus-ai uninstall kimi`. Las instalaciones externas no se modifican, salvo una instalación antigua de Cursor CLI que el comando explícito reconoce si `~/.local/bin/agent` apunta dentro de `~/.local/share/cursor-agent/versions/`. Hermes utiliza su desinstalador oficial. Se eliminan los binarios de Cursor y Kimi, preservando la configuración, las sesiones y las credenciales del usuario.

Comprueba con `argvus-ai list`; ejecútalo con `argvus-ai launch gemini` o selecciónalo en el menú. Autentícate con Google en Gemini CLI.
