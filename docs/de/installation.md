---
title: Installation
description: Installiere argvus-ai und verstehe, wie jeder Agent bereitgestellt wird.
---
## Das Paket installieren

Unter Arch Linux mit den konfigurierten ARGVUS-Repositories, sobald `argvus-ai` dort veröffentlicht ist:

```sh
sudo pacman -S argvus-ai
```
Für einen unveröffentlichten lokalen Build führen Sie `make validate` und `make build` im Quellrepository `argvus-ai` aus und installieren dann das resultierende `.pkg.tar.zst` aus `build/dist/` mit `sudo pacman -U /path/to/package.pkg.tar.zst`. Pacman muss in der Lage sein, seine Abhängigkeiten aufzulösen, einschließlich des Master-Pakets `argvus`.

Das Paket erfordert `argvus`, `rofi`, `jq`, `mise`, `opencode` und `openai-codex`; Arch stellt `/bin/sh` über `bash` bereit. OpenCode läuft als `opencode`, und das Paket `openai-codex` stellt `codex` bereit.

## Desktop-Integration

Verwenden Sie die aktualisierten Pakete `argvus-hyprland` und `argvus-taskbar`. Hyprland lädt das optionale Lua-Modul, das von `argvus-ai` bereitgestellt wird. Der Pacman-Hook der Integration aktualisiert die Standard-Systemkonfiguration nach der Installation oder Entfernung. Eine benutzerdefinierte Root-Konfiguration oder deaktiviertes Autoreload kann ein explizites Neuladen erfordern. Bestehende persönliche Shortcut-Überschreibungen bleiben maßgeblich.

Der aktualisierte `argvus-appearance` Projektor bewahrt das Taskleistenmodul und berücksichtigt **Kontrollzentrum > Darstellung > Taskleiste > Symbole > Optionale Module > KI-Agenten**. Die Option ist standardmäßig aktiviert; klicken Sie auf **Übernehmen**, nachdem Sie sie geändert haben. Das Aktivieren installiert keine Agenten.

## Claude Code bei der ersten Verwendung

Wählen Sie Claude Code im Rofi-Auswahlmenü oder Anwendungsstarter aus. Das ARGVUS-Terminal öffnet sich und führt `mise install claude` als Ihr regulärer Benutzer aus, wenn keine installierte Version gefunden wird. Für diese Erstinstallation ist Netzwerkzugang erforderlich. Der Wrapper löst die installierte ausführbare Datei auf und fügt ihr Verzeichnis zum gestarteten Prozess-PATH hinzu; er bearbeitet keine Shell-Startdateien und installiert nicht als Root. Spätere Starts verwenden die Installation erneut.

## Entfernen

```sh
sudo pacman -R argvus-ai
```
Das paket-eigene Lua-Modul und die Desktop-Einträge werden entfernt, und das Taskleistenmodul versteckt sich, wenn sein Helfer fehlt. Die Standard-Hyprland-Konfiguration lädt automatisch neu, um die Bindung zu entfernen. Benutzer-eigene mise-Tools, Agenteneinstellungen und Anmeldedaten werden beibehalten. Pacman entfernt bei diesem Befehl nicht automatisch die Agentenabhängigkeiten.

Das ARGVUS-AI-Paket installiert keine externen Agenten bei der Paketinstallation. Hermes, Cursor CLI und Kimi werden beim ersten Start installiert; Benutzerdaten bleiben außerhalb des Pakets. Anweisungen zum Entfernen stehen im Nutzungshandbuch.
