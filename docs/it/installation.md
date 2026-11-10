---
title: Installazione
description: Installa argvus-ai e comprendi come viene fornito ciascun agente.
---
## Installa il pacchetto

Su Arch Linux con i repository ARGVUS configurati, una volta che `argvus-ai` è pubblicato lì:

```sh
sudo pacman -S argvus-ai
```
Per una build locale non pubblicata, eseguire `make validate` e `make build` nel repository sorgente `argvus-ai`, quindi installare il risultato `.pkg.tar.zst` da `build/dist/` con `sudo pacman -U /path/to/package.pkg.tar.zst`. Pacman deve essere in grado di risolvere le sue dipendenze, incluso il pacchetto master `argvus`.

Il pacchetto richiede `argvus`, `rofi`, `jq`, `mise`, `opencode` e `openai-codex`; Arch fornisce `/bin/sh` tramite `bash`. OpenCode viene eseguito come `opencode`, e il pacchetto `openai-codex` fornisce `codex`.

## Integrazione desktop

Usare i pacchetti aggiornati `argvus-hyprland` e `argvus-taskbar`. Hyprland carica il modulo Lua opzionale fornito da `argvus-ai`. Il hook di integrazione di Pacman aggiorna la configurazione di sistema standard dopo l'installazione o la rimozione. Una configurazione root personalizzata o l'autoreload disabilitato può richiedere un reload esplicito. Le sovrascritture esistenti dei collegamenti personali rimangono vincolanti.

Il proiettore aggiornato `argvus-appearance` preserva il modulo della barra delle applicazioni e rispetta **Centro di Controllo > Aspetto > Barra delle applicazioni > Icone > Moduli opzionali > Agenti AI**. L'opzione è abilitata di default; clicca su **Applica** dopo averla modificata. Abilitandola non vengono installati agenti.

## Claude Code al primo utilizzo

Seleziona Claude Code dal selettore Rofi o dal launcher delle applicazioni. Si apre il terminale ARGVUS ed esegue `mise install claude` come utente normale se non viene trovata una versione installata. Per questa prima installazione è necessario l'accesso alla rete. Il wrapper risolve l'eseguibile installato e aggiunge la sua directory al PATH del processo lanciato; non modifica i file di avvio della shell né installa come root. I lanci successivi riutilizzano l'installazione.

## Rimuovi

```sh
sudo pacman -R argvus-ai
```
Il modulo Lua di proprietà del pacchetto e le voci del desktop vengono rimossi, e il modulo della barra delle applicazioni si nasconde quando il suo helper è assente. La configurazione standard di Hyprland si ricarica automaticamente per rimuovere il bind. Gli strumenti mise, le impostazioni dell'agente e le credenziali di proprietà dell'utente vengono mantenuti. Pacman non rimuove automaticamente le dipendenze dell'agente con questo comando.
