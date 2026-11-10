---
title: Instalación
description: Instala argvus-ai y entiende cómo se proporciona cada agente.
---
## Instalar el paquete

En Arch Linux con los repositorios ARGVUS configurados, una vez que `argvus-ai` se publique allí:

```sh
sudo pacman -S argvus-ai
```
Para una compilación local no publicada, ejecute `make validate` y `make build` en el repositorio de código fuente `argvus-ai`, luego instale el `.pkg.tar.zst` resultante desde `build/dist/` con `sudo pacman -U /path/to/package.pkg.tar.zst`. Pacman debe poder resolver sus dependencias, incluido el paquete maestro `argvus`.

El paquete requiere `argvus`, `rofi`, `jq`, `mise`, `opencode` y `openai-codex`; Arch proporciona `/bin/sh` a través de `bash`. OpenCode se ejecuta como `opencode`, y el paquete `openai-codex` proporciona `codex`.

## Integración de escritorio

Utilice los paquetes actualizados `argvus-hyprland` y `argvus-taskbar`. Hyprland carga el módulo opcional de Lua proporcionado por `argvus-ai`. El hook de Pacman de la integración actualiza la configuración estándar del sistema después de la instalación o eliminación. Una configuración raíz personalizada o la recarga automática deshabilitada pueden requerir una recarga explícita. Las anulaciones existentes de accesos directos personales siguen siendo autorizadas.

El proyector actualizado `argvus-appearance` conserva el módulo de la barra de tareas y respeta **Centro de Control > Apariencia > Barra de tareas > Iconos > Módulos opcionales > Agentes de IA**. La opción está habilitada por defecto; haga clic en **Aplicar** después de cambiarla. Activarla no instala agentes.

## Claude Code en el primer uso

Seleccione Claude Code desde el selector Rofi o el lanzador de aplicaciones. Se abre el terminal ARGVUS y ejecuta `mise install claude` como su usuario habitual si no se encuentra una versión instalada. Se necesita acceso a la red para esta primera instalación. El envoltorio resuelve el ejecutable instalado y agrega su directorio al PATH del proceso iniciado; no edita archivos de inicio del shell ni instala como root. Los lanzamientos posteriores reutilizan la instalación.

## Eliminar

```sh
sudo pacman -R argvus-ai
```
El módulo Lua propiedad del paquete y las entradas de escritorio se eliminan, y el módulo de la barra de tareas se oculta cuando su auxiliar está ausente. La configuración estándar de Hyprland se recarga automáticamente para eliminar el enlace. Se conservan las herramientas mise, la configuración del agente y las credenciales propiedad del usuario. Pacman no elimina automáticamente las dependencias del agente con este comando.
