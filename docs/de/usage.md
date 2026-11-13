---
title: Verwendung und Fehlerbehebung
description: Agenten auswählen, das Taskleistensymbol steuern und fehlende Integrationen diagnostizieren.
---
## Einen Agenten öffnen

Drücken Sie **SUPER + A**, klicken Sie auf den Roboter in der Taskleiste oder wählen Sie einen Anwendungseintrag eines Agenten aus. Der Selektor bietet ausführbare OpenCode/Codex-Installationen an und bietet Claude Code für die Erstinstallation an, wenn mise vorhanden ist. **Esc** bricht ab, ohne etwas zu starten oder herunterzuladen.

Das Terminal übernimmt das Arbeitsverzeichnis des Aufrufers; grafische Starts beginnen normalerweise im Heimatverzeichnis der Sitzung. Starten Sie einen Agenten von einem Projektterminal aus, wenn Sie ein bestimmtes Arbeitsverzeichnis benötigen.

## Sichtbarkeit in der Taskleiste

Öffnen Sie **Systemsteuerung > Darstellung > Taskleiste > Symbole > Optionale Module**, aktivieren Sie **KI-Agenten** und klicken Sie dann auf **Übernehmen**. Der Roboter gehört zu `group/right-2`; wenn seine Schublade eingeklappt ist, erweitern Sie die Dienstprogramme-Gruppe. Die Einstellung ist `/taskbar/icons/ai_agents_enabled`, standardmäßig auf true gesetzt, und überlebt eine Regeneration. Sie steuert nur das Symbol: Verknüpfungen und Desktop-Einträge bleiben verfügbar. Die Laufzeitverfügbarkeit kann ein aktiviertes Symbol trotzdem ausblenden.

## Diagnosebefehle

```sh
argvus-ai list
argvus-ai status
argvus-ai status --check
argvus-ai menu
argvus-ai launch opencode
argvus-ai launch codex
argvus-ai launch claude
```
`list` meldet nur installierte Agenten. `status` gibt Waybar JSON aus, während `status --check` darüber berichtet, ob eine installierte oder installierbare Menüauswahl über seinen Exit-Status vorhanden ist. Nur das Auswählen/Starten von Claude kann dessen Installation starten; `run-claude` ist ein interner Terminal-Einstiegspunkt.

Wenn die Verknüpfung immer noch die alte Kombination verwendet, prüfen Sie die persönliche Überschreibung auf der Seite Tastenkombinationen im Kontrollzentrum; verpackte Standardwerte überschreiben diese nicht. Wenn der Roboter nach Anwendung der Erscheinungseinstellungen verschwindet, aktualisieren Sie `argvus-appearance` und erzeugen/übernehmen Sie die Taskleisten-Einstellungen erneut. Vermeiden Sie das direkte Bearbeiten generierter Waybar/Lua-Dateien.

Wenn die Claude-Installation fehlschlägt, überprüfen Sie Terminalfehler, Netzwerkzugang und die installierte Mise-Version, und wählen Sie dann Claude erneut aus. Mise-Abfragen werden von Home ausgeführt, sodass eine projektspezifische Konfiguration kein anderes Tool auswählt. Der Wrapper benötigt keine Mise-Shims im grafischen PATH. Die OpenCode/Codex-Erkennung verwendet den grafischen PATH, ohne Shell-Aliase oder interaktive Startskripte.

Kehrt zu [AI Agents](/docs/argvus-ai/) zurück.

Agenten öffnen sich in einem zentrierten, schwebenden Kitty-Fenster mit dem Titel `ARGVUS AI Agent` und einem ARGVUS-Header und -Footer. Drücken Sie **Strg + E**, um das Agentenfenster zu schließen. Diese Tastenkombination ist vom Rahmen reserviert; Esc und Strg+C stehen dem Agenten weiterhin zur Verfügung.

Das dedizierte Kitty-Profil `ai-agents` versteckt Tabs und entfernt vererbte Shortcuts für Tabs, Splits und Vollbild. Die Zwischenablage-Shortcuts Strg+Shift+C und Strg+Shift+V bleiben verfügbar. Die erzeugte Konfiguration ist `kitty-tui/kitty-ai-agents.conf` im ARGVUS-Cache-Verzeichnis. Das Paket Hyprland-Modul verschiebt Fenster der Klasse `argvus-ai` und zentriert sie bei 1399 × 920.

## Agenten deinstallieren

`argvus-ai list` zeigt installierte Agenten. Führen Sie `argvus-ai uninstall` aus, wählen Sie eine von ARGVUS verwaltete Hermes-, Cursor-CLI- oder Kimi-Installation und bestätigen Sie die Entfernung. Alternativ können Sie `argvus-ai uninstall hermes`, `argvus-ai uninstall cursor` oder `argvus-ai uninstall kimi` ausführen. Externe Installationen bleiben unangetastet. Eine ältere Cursor-CLI-Installation wird beim expliziten Cursor-Befehl erkannt, wenn `~/.local/bin/agent` auf `~/.local/share/cursor-agent/versions/` verweist. Hermes verwendet sein offizielles Deinstallationsprogramm. Cursor- und Kimi-Binärdateien werden entfernt; Benutzereinstellungen, Sitzungen und Anmeldedaten bleiben erhalten.

Mit `argvus-ai list` prüfen; mit `argvus-ai launch gemini` starten oder im Menü auswählen. Die Google-Anmeldung erfolgt in Gemini CLI.
