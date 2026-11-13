---
title: KI-Agenten
description: Öffnen Sie Programmieragenten vom ARGVUS-Desktop.
---
`argvus-ai` ist eine optionale Desktop-Integration für **OpenCode**, **OpenAI Codex** und **Claude Code**. Sie bietet einen gemeinsamen Rofi-Selektor, Einträge im Anwendungsstarter und das Roboter-Symbol in der Taskleisten-Dienstgruppe. Agenten werden in einem neuen ARGVUS-Terminalfenster ausgeführt und behalten das Arbeitsverzeichnis des Aufrufers bei.

Öffnen Sie den Selektor mit **SUPER + A** oder klicken Sie auf **nf-md-robot** in der Taskleiste, neben den Mikrofon- und Audiosteuerungen. Sie können auch einen einzelnen Agenten im Anwendungsstarter auswählen.

OpenCode und Codex sind als Paketabhängigkeiten installiert. Claude Code wird mit mise, als Ihr Benutzer, nur beim ersten Auswählen installiert. Das Installieren des Pakets, das Öffnen/Abbrechen des Selektors oder das Überprüfen des Status lädt Claude niemals herunter. Das Paket konfiguriert keine Konten, API-Schlüssel oder Abonnements; folgen Sie den Authentifizierungsanweisungen des ausgewählten Agenten.

Lesen Sie [Installation](/docs/argvus-ai/installation/) und [Verwendung und Fehlerbehebung](/docs/argvus-ai/usage/).

## Sprachen

Die `ai` Der Katalog ist in allen 18 ARGVUS Schnittstellensprachen und verwendet die geteilten `argvus i18n` Auswahl und englischer Fallback. Die gewählte Schnittstellensprache wird gespeichert als `ARGVUS_LANGUAGE` im Benutzer `locale.conf`; das System regional locale bleibt getrennt. Übersetzungen werden als Daten installiert, ohne die Benutzerkonfiguration zu schreiben.

## Unterstützte Agenten

Die Integration unterstützt OpenCode, Codex und Qwen Code aus dem Paket, Claude Code über mise, separat installiertes Antigravity sowie Hermes, Cursor CLI und Kimi, die beim ersten Start über ihre offiziellen Installationsprogramme eingerichtet werden. Wie Sie von ARGVUS verwaltete externe Agenten auflisten und entfernen, erfahren Sie im [Nutzungshandbuch](usage/).
