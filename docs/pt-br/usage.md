---
title: Uso e solução de problemas
description: Selecione agentes, controle o ícone da taskbar e diagnostique integrações ausentes.
---

## Abrir um agente

Pressione **SUPER + A**, clique no robô da taskbar ou escolha uma entrada de agente no lançador de aplicativos. O seletor oferece instalações executáveis de OpenCode/Codex e oferece Claude Code para instalação no primeiro uso quando o mise está disponível. **Esc** cancela sem abrir agentes nem baixar nada.

O terminal herda o diretório de trabalho de quem o chamou; aberturas gráficas normalmente começam no diretório pessoal da sessão. Inicie o agente pelo terminal de um projeto quando precisar de um diretório específico.

## Visibilidade na taskbar

Abra **Control Center > Appearance > Taskbar > Icons > Optional modules**, altere **Agentes de IA** e clique em **Aplicar**. O robô pertence a `group/right-2`; se a gaveta estiver recolhida, expanda o grupo de utilitários. A preferência é `/taskbar/icons/ai_agents_enabled`, vem habilitada e sobrevive à regeneração. Controla somente o ícone: atalhos e entradas de aplicativos continuam disponíveis. A disponibilidade em runtime ainda pode ocultar um ícone habilitado.

## Comandos de diagnóstico

```sh
argvus-ai list
argvus-ai status
argvus-ai status --check
argvus-ai menu
argvus-ai launch opencode
argvus-ai launch codex
argvus-ai launch claude
argvus-ai uninstall
```

`list` informa somente agentes instalados. `status` emite JSON para Waybar; `status --check` informa pelo código de saída se há uma opção instalada ou instalável no menu. Somente selecionar/abrir Claude pode iniciar sua instalação; `run-claude` é uma entrada interna usada pelo terminal.

`argvus-ai uninstall` oferece somente Hermes, Cursor CLI e Kimi registrados como instalados pelo ARGVUS. Confirme a remoção no seletor. O comando explícito `argvus-ai uninstall cursor` também reconhece instalações antigas do Cursor CLI somente quando `~/.local/bin/agent` aponta para dentro de `~/.local/share/cursor-agent/versions/`. Outras instalações sem registro não são alteradas. Hermes usa seu desinstalador oficial; Cursor CLI e Kimi têm seus binários removidos, preservando configurações e sessões.

Se o atalho continuar usando a combinação antiga, confira o override pessoal na página de atalhos do Control Center; os padrões do pacote não o sobrescrevem. Se o robô desaparecer após aplicar a aparência, atualize `argvus-appearance` e regenere/aplique os ajustes da taskbar. Evite editar arquivos Waybar/Lua gerados diretamente.

Se a instalação do Claude falhar, confira os erros no terminal, o acesso à rede e a versão do mise; depois selecione Claude novamente. As consultas mise são feitas a partir do diretório pessoal para evitar a seleção de outra ferramenta pela configuração de um projeto. O wrapper não exige shims mise no PATH gráfico. OpenCode/Codex são descobertos pelo PATH gráfico, sem aliases ou scripts de inicialização interativos.

Voltar para [Agentes de IA](/pt/docs/argvus-ai/).

Os agentes abrem em uma janela Kitty flutuante e centralizada com título `ARGVUS AI Agent`, cabeçalho ARGVUS e rodapé. Pressione **Ctrl + E** para fechar a janela do agente. A moldura reserva esse atalho; Esc e Ctrl+C continuam disponíveis para o agente.

O perfil Kitty dedicado `ai-agents` oculta as abas e remove os atalhos herdados de abas, divisões e tela cheia. Os atalhos de clipboard Ctrl+Shift+C e Ctrl+Shift+V continuam disponíveis. A configuração gerada fica em `kitty-tui/kitty-ai-agents.conf` no cache ARGVUS. O módulo Hyprland do pacote abre a classe `argvus-ai` em janela flutuante centralizada de 1399 × 920.

Instale o Google Antigravity CLI (`agy`) separadamente conforme as [instruções oficiais](https://antigravity.google/docs/getting-started?tab=cli). Ele é detectado no PATH da sessão gráfica ou em `~/.local/bin/agy`. Execute `argvus-ai launch agy` para abri-lo.

O Qwen Code é fornecido pelo pacote Arch `qwen-code`. Selecione-o no menu ou execute `argvus-ai launch qwen`.

Hermes, Cursor CLI e Kimi Code são instalados pelos instaladores oficiais na primeira abertura, como usuário comum. Selecione-os no menu ou use `argvus-ai launch hermes`, `argvus-ai launch cursor` ou `argvus-ai launch kimi`. Cada agente gerencia sua autenticação e atualizações.

Instalações do Kimi em `~/.kimi-code/bin/kimi` são detectadas sem alterar o PATH gráfico. Se a instalação falhar, verifique a saída do terminal.

## Desinstalar agentes

`argvus-ai list` lista os agentes instalados. Execute `argvus-ai uninstall` para selecionar uma instalação do Hermes, Cursor CLI ou Kimi gerenciada pelo ARGVUS e confirme a remoção. Também é possível executar `argvus-ai uninstall hermes`, `argvus-ai uninstall cursor` ou `argvus-ai uninstall kimi`. Instalações feitas fora do ARGVUS não são alteradas, exceto uma instalação antiga do Cursor CLI, reconhecida pelo comando explícito quando `~/.local/bin/agent` aponta para dentro de `~/.local/share/cursor-agent/versions/`. O Hermes usa seu desinstalador oficial. Os binários do Cursor e do Kimi são removidos, preservando configurações, sessões e credenciais do usuário.
