---
title: Installation
description: Installez argvus-ai et comprenez comment chaque agent est fourni.
---
## Installer le paquet

Sur Arch Linux avec les dépôts ARGVUS configurés, une fois que `argvus-ai` est publié là-bas :

```sh
sudo pacman -S argvus-ai
```
Pour une compilation locale non publiée, exécutez `make validate` et `make build` dans le dépôt source `argvus-ai`, puis installez le `.pkg.tar.zst` résultant depuis `build/dist/` avec `sudo pacman -U /path/to/package.pkg.tar.zst`. Pacman doit pouvoir résoudre ses dépendances, y compris le paquet maître `argvus`.

Le paquet requiert `argvus`, `rofi`, `jq`, `mise`, `opencode` et `openai-codex` ; Arch fournit `/bin/sh` via `bash`. OpenCode s'exécute en tant que `opencode`, et le paquet `openai-codex` fournit `codex`.

## Intégration au bureau

Utilisez les paquets `argvus-hyprland` et `argvus-taskbar` mis à jour. Hyprland charge le module Lua optionnel fourni par `argvus-ai`. Le hook Pacman de l'intégration actualise la configuration système standard après l'installation ou la suppression. Une configuration racine personnalisée ou une autorecharge désactivée peut nécessiter un rechargement explicite. Les remplacements de raccourcis personnels existants restent prioritaires.

Le projecteur `argvus-appearance` mis à jour conserve le module de la barre des tâches et respecte **Centre de contrôle > Apparence > Barre des tâches > Icônes > Modules optionnels > Agents IA**. L'option est activée par défaut ; cliquez sur **Appliquer** après l'avoir modifiée. L'activation de cette option n'installe pas d'agents.

## Claude Code lors de la première utilisation

Sélectionnez Claude Code depuis le sélecteur Rofi ou le lanceur d'applications. Le terminal ARGVUS s'ouvre et exécute `mise install claude` en tant qu'utilisateur normal si aucune version installée n'est trouvée. Un accès réseau est nécessaire pour cette première installation. L'enveloppe résout l'exécutable installé et ajoute son répertoire au PATH du processus lancé ; elle n'édite pas les fichiers de démarrage du shell ni ne s'installe en tant que root. Les lancements suivants réutilisent l'installation.

## Supprimer

```sh
sudo pacman -R argvus-ai
```
Le module Lua détenu par le paquet et les entrées de bureau sont supprimés, et le module de la barre des tâches se cache lorsque son assistant est absent. La configuration standard de Hyprland se recharge automatiquement pour supprimer le raccourci. Les outils mise, les paramètres de l'agent et les identifiants détenus par l'utilisateur sont conservés. Pacman ne supprime pas automatiquement les dépendances de l'agent avec cette commande.
