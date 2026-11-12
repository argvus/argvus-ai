---
title: Utilisation et dépannage
description: Sélectionnez des agents, contrôlez l'icône de la barre des tâches et diagnostiquez les intégrations manquantes.
---
## Ouvrir un agent

Appuyez sur **SUPER + A**, cliquez sur le robot de la barre des tâches ou choisissez l'entrée d'application d'un agent. Le sélecteur propose les installations exécutables OpenCode/Codex et offre Claude Code pour une installation lors de la première utilisation lorsque mise existe. **Échap** annule sans lancer ni télécharger quoi que ce soit.

Le terminal hérite du répertoire de travail de l'appelant ; les lancements graphiques démarrent généralement depuis le répertoire personnel de la session. Lancez un agent depuis un terminal de projet lorsque vous avez besoin d'un répertoire de travail particulier.

## Visibilité de la barre des tâches

Ouvrez **Centre de contrôle > Apparence > Barre des tâches > Icônes > Modules optionnels**, activez **Agents IA**, puis **Appliquer**. Le robot appartient à `group/right-2` ; si son tiroir est réduit, développez le groupe d’utilitaires. La préférence est `/taskbar/icons/ai_agents_enabled`, sa valeur par défaut est true, et elle survit à la régénération. Elle contrôle uniquement l'icône : les raccourcis et les entrées du bureau restent disponibles. La disponibilité en temps réel peut toujours masquer une icône activée.

## Commandes de diagnostic

```sh
argvus-ai list
argvus-ai status
argvus-ai status --check
argvus-ai menu
argvus-ai launch opencode
argvus-ai launch codex
argvus-ai launch claude
```
`list` rapporte uniquement les agents installés. `status` émet du JSON Waybar, tandis que `status --check` indique s'il existe un choix de menu installé ou installable via son code de sortie. Seule la sélection/le lancement de Claude peut démarrer son installation ; `run-claude` est un point d'entrée terminal interne.

Si le raccourci utilise encore l'ancienne combinaison, vérifiez son override personnel dans la page des raccourcis clavier du Centre de contrôle ; les valeurs par défaut empaquetées ne l'écrasent pas. Si le robot disparaît après l'application des paramètres d'apparence, mettez à jour `argvus-appearance` et régénérez/appliquez les paramètres de la barre des tâches. Évitez de modifier directement les fichiers Waybar/Lua générés.

Si l'installation de Claude échoue, vérifiez les erreurs du terminal, l'accès au réseau et la version de mise installée, puis sélectionnez à nouveau Claude. Les requêtes mise s'exécutent depuis le dossier personnel, donc une configuration spécifique à un projet ne sélectionne pas un outil différent. Le wrapper n'a pas besoin de shims mise dans le PATH graphique. La découverte OpenCode/Codex utilise le PATH graphique, sans alias shell ni scripts de démarrage interactifs.

Revenir à [AI Agents](/docs/argvus-ai/).

Les agents s'ouvrent dans une fenêtre flottante centrée de Kitty intitulée `ARGVUS AI Agent`, avec un en-tête et un pied de page ARGVUS. Appuyez sur **Ctrl + E** pour fermer la fenêtre de l'agent. Ce raccourci est réservé par le cadre ; Esc et Ctrl+C restent disponibles pour l'agent.

Le profil dédié Kitty `ai-agents` masque les onglets et supprime les raccourcis hérités pour les onglets, les divisions et le plein écran. Les raccourcis du presse-papiers Ctrl+Shift+C et Ctrl+Shift+V restent disponibles. Sa configuration générée est `kitty-tui/kitty-ai-agents.conf` sous le répertoire de cache ARGVUS. Le module du package Hyprland fait flotter et centre les fenêtres avec la classe `argvus-ai` à 1399 × 920.

## Désinstaller les agents

`argvus-ai list` affiche les agents installés. Exécutez `argvus-ai uninstall` pour sélectionner une installation Hermes, Cursor CLI ou Kimi gérée par ARGVUS, puis confirmez la suppression. Vous pouvez aussi exécuter `argvus-ai uninstall hermes`, `argvus-ai uninstall cursor` ou `argvus-ai uninstall kimi`. Les installations externes restent intactes, sauf une ancienne installation Cursor CLI reconnue par la commande explicite si `~/.local/bin/agent` pointe dans `~/.local/share/cursor-agent/versions/`. Hermes utilise son désinstalleur officiel. Les binaires Cursor et Kimi sont supprimés, tandis que les paramètres, sessions et identifiants utilisateur sont conservés.
