---
title: Uso e risoluzione dei problemi
description: Seleziona gli agenti, controlla l'icona della barra delle applicazioni e diagnostica le integrazioni mancanti.
---
## Apri un agente

Premi **SUPER + A**, clicca sul robot della barra delle applicazioni o scegli una voce dell'applicazione dell'agente. Il selettore offre installazioni eseguibili di OpenCode/Codex e propone Claude Code per l'installazione al primo utilizzo quando mise è disponibile. **Esc** annulla senza avviare o scaricare nulla.

Il terminale eredita la directory di lavoro del chiamante; gli avvii grafici solitamente partono dalla directory home della sessione. Avvia un agente da un terminale di progetto quando hai bisogno di una directory di lavoro particolare.

## Visibilità nella barra delle applicazioni

Apri **Centro di Controllo > Aspetto > Barra delle applicazioni > Icone > Moduli opzionali**, attiva **Agenti AI**, quindi **Applica**. Il robot appartiene a `group/right-2`; se il suo cassetto è chiuso, espandi il gruppo di utilità. La preferenza è `/taskbar/icons/ai_agents_enabled`, impostata di default su vero, e sopravvive alla rigenerazione. Controlla solo l'icona: scorciatoie e voci del desktop rimangono disponibili. La disponibilità in tempo reale può comunque nascondere un'icona abilitata.

## Comandi diagnostici

```sh
argvus-ai list
argvus-ai status
argvus-ai status --check
argvus-ai menu
argvus-ai launch opencode
argvus-ai launch codex
argvus-ai launch claude
```
`list` riporta solo gli agenti installati. `status` emette JSON per Waybar, mentre `status --check` segnala se esiste una scelta di menu installata o installabile tramite il suo stato di uscita. Solo selezionare/avviare Claude può avviare la sua installazione; `run-claude` è un punto di ingresso interno al terminale.

Se il collegamento utilizza ancora la vecchia combinazione, verifica la sua sovrascrittura personale nella pagina delle scorciatoie da tastiera del Centro di Controllo; i valori predefiniti pacchettizzati non la sovrascrivono. Se il robot scompare dopo aver applicato le impostazioni di aspetto, aggiorna `argvus-appearance` e rigenera/applica le impostazioni della barra delle applicazioni. Evita di modificare direttamente i file generati di Waybar/Lua.

Se l'installazione di Claude fallisce, controlla gli errori nel terminale, l'accesso alla rete e la versione di mise installata, quindi seleziona di nuovo Claude. Le query di mise vengono eseguite dalla home, quindi una configurazione specifica del progetto non seleziona uno strumento diverso. Il wrapper non richiede shim di mise nel PATH grafico. La scoperta OpenCode/Codex utilizza il PATH grafico, senza alias della shell o script di avvio interattivi.

Torna a [AI Agents](/docs/argvus-ai/).

Gli agenti si aprono in una finestra flottante centrata di Kitty intitolata `ARGVUS AI Agent`, con un'intestazione e un piè di pagina ARGVUS. Premi **Ctrl + E** per chiudere la finestra dell'agente. Questa scorciatoia è riservata dal frame; Esc e Ctrl+C rimangono disponibili all'agente.

Il profilo dedicato Kitty `ai-agents` nasconde le schede e cancella le scorciatoie ereditate per schede, suddivisioni e schermo intero. Le scorciatoie degli appunti Ctrl+Shift+C e Ctrl+Shift+V rimangono disponibili. La sua configurazione generata è `kitty-tui/kitty-ai-agents.conf` nella directory della cache ARGVUS. Il modulo del pacchetto Hyprland galleggia e centra le finestre con classe `argvus-ai` a 1399 × 920.

## Disinstallare gli agenti

`argvus-ai list` mostra gli agenti installati. Esegui `argvus-ai uninstall` per selezionare un’installazione di Hermes, Cursor CLI o Kimi gestita da ARGVUS e conferma la rimozione. Puoi anche eseguire `argvus-ai uninstall hermes`, `argvus-ai uninstall cursor` o `argvus-ai uninstall kimi`. Le installazioni esterne non vengono modificate, tranne una vecchia installazione di Cursor CLI riconosciuta dal comando esplicito se `~/.local/bin/agent` punta all’interno di `~/.local/share/cursor-agent/versions/`. Hermes usa il suo programma di disinstallazione ufficiale. I binari Cursor e Kimi vengono rimossi, mantenendo impostazioni, sessioni e credenziali utente.
