---
title: Agents IA
description: Ouvrir les agents de programmation depuis le bureau ARGVUS.
---
`argvus-ai` est une intégration de bureau optionnelle pour **OpenCode**, **OpenAI Codex** et **Claude Code**. Elle fournit un sélecteur Rofi partagé, des entrées de lancement d'application et l'icône du robot dans le groupe d'utilitaires de la barre des tâches. Les agents s'exécutent dans une nouvelle fenêtre de terminal ARGVUS et conservent le répertoire de travail de l'appelant.

Ouvrez le sélecteur avec **SUPER + A** ou cliquez sur **nf-md-robot** dans la barre des tâches, à côté du microphone et des contrôles audio. Vous pouvez également sélectionner un agent individuel dans le lanceur d'applications.

OpenCode et Codex sont installés en tant que dépendances de package. Claude Code est installé avec mise, en tant qu'utilisateur, uniquement lorsque vous le sélectionnez pour la première fois. L'installation du package, l'ouverture/annulation du sélecteur ou la vérification du statut ne télécharge jamais Claude. Le package ne configure pas les comptes, les clés API ou les abonnements ; suivez les invites d'authentification de l'agent sélectionné.

Lisez [Installation](/docs/argvus-ai/installation/) et [Utilisation et dépannage](/docs/argvus-ai/usage/).

## Langues

Le catalogue `ai` est fourni dans les dix langues ARGVUS et utilise la sélection partagée `argvus i18n` ainsi que la langue anglaise par défaut. Les traductions sont installées en tant que données sans modifier la configuration de l'utilisateur.

## Agents disponibles

L’intégration prend en charge OpenCode, Codex et Qwen Code fournis par le paquet, Claude Code via mise, Antigravity lorsqu’il est installé séparément, ainsi que Hermes, Cursor CLI et Kimi, installés au premier lancement à l’aide de leurs installateurs officiels. Consultez le [guide d’utilisation](usage/) pour savoir comment lister et désinstaller les agents externes gérés par ARGVUS.
