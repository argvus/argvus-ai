---
title: KI-Agenten
description: Öffnen Sie Programmieragenten vom ARGVUS-Desktop.
---
`argvus-ai` ist eine optionale Desktop-Integration für **OpenCode**, **OpenAI Codex** und **Claude Code**. Sie bietet einen gemeinsamen Rofi-Selektor, Einträge im Anwendungsstarter und das Roboter-Symbol in der Taskleisten-Dienstgruppe. Agenten werden in einem neuen ARGVUS-Terminalfenster ausgeführt und behalten das Arbeitsverzeichnis des Aufrufers bei.

Öffnen Sie den Selektor mit **SUPER + A** oder klicken Sie auf **nf-md-robot** in der Taskleiste, neben den Mikrofon- und Audiosteuerungen. Sie können auch einen einzelnen Agenten im Anwendungsstarter auswählen.

OpenCode und Codex sind als Paketabhängigkeiten installiert. Claude Code wird mit mise, als Ihr Benutzer, nur beim ersten Auswählen installiert. Das Installieren des Pakets, das Öffnen/Abbrechen des Selektors oder das Überprüfen des Status lädt Claude niemals herunter. Das Paket konfiguriert keine Konten, API-Schlüssel oder Abonnements; folgen Sie den Authentifizierungsanweisungen des ausgewählten Agenten.

Lesen Sie [Installation](/docs/argvus-ai/installation/) und [Verwendung und Fehlerbehebung](/docs/argvus-ai/usage/).

## Sprachen

Der `ai`-Katalog wird in allen zehn ARGVUS-Sprachen bereitgestellt und verwendet die gemeinsame `argvus i18n`-Auswahl sowie die englische Rückfalloption. Übersetzungen werden als Daten installiert, ohne die Benutzerkonfiguration zu schreiben.

## Unterstützte Agenten

Die Integration umfasst OpenCode, Codex und Qwen Code als Paketabhängigkeiten, Claude Code über mise, separat installiertes Antigravity sowie Hermes, Cursor CLI und Kimi über ihre offiziellen Installer beim ersten Start. Im [Nutzungshandbuch](usage/) finden Sie Anleitungen zum Auflisten und Entfernen von ARGVUS-verwalteten externen Agenten.
