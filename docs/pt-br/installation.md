---
title: Instalação
description: Instale argvus-ai e entenda como cada agente é disponibilizado.
---

## Instalar o pacote

No Arch Linux com os repositórios ARGVUS configurados, quando `argvus-ai` estiver publicado neles:

```sh
sudo pacman -S argvus-ai
```

Para uma versão local ainda não publicada, execute `make validate` e `make build` no repositório-fonte de `argvus-ai` e instale o `.pkg.tar.zst` gerado em `build/dist/` com `sudo pacman -U /caminho/do/pacote.pkg.tar.zst`. O Pacman precisa conseguir resolver as dependências, incluindo o pacote principal `argvus`.

O pacote requer `argvus`, `rofi`, `jq`, `mise`, `opencode` e `openai-codex`; no Arch, `bash` fornece `/bin/sh`. OpenCode usa `opencode`, enquanto o pacote `openai-codex` fornece `codex`.

## Integração com o desktop

Use as versões atualizadas de `argvus-hyprland` e `argvus-taskbar`. O Hyprland carrega o módulo Lua opcional fornecido por `argvus-ai`. O hook Pacman da integração atualiza a configuração padrão do sistema após instalação ou remoção. Uma configuração raiz própria ou o autoreload desabilitado pode exigir reload explícito. Overrides pessoais dos atalhos continuam tendo precedência.

O projetor atualizado de `argvus-appearance` preserva o módulo na taskbar e respeita **Control Center > Appearance > Taskbar > Icons > Optional modules > Agentes de IA**. A opção vem habilitada; clique em **Aplicar** após alterá-la. Habilitá-la não instala agentes.

## Claude Code no primeiro uso

Selecione Claude Code no seletor Rofi ou no lançador de aplicativos. O terminal ARGVUS abre e executa `mise install claude` como seu usuário, caso nenhuma versão instalada seja encontrada. O primeiro download exige rede. O wrapper resolve o executável instalado e adiciona seu diretório ao PATH do processo iniciado; não edita arquivos de inicialização do shell nem instala como root. As próximas aberturas reutilizam a instalação.

## Remover

```sh
sudo pacman -R argvus-ai
```

O módulo Lua e as entradas de aplicativos pertencentes ao pacote são removidos, e o módulo da taskbar fica oculto quando o helper está ausente. A configuração padrão do Hyprland recarrega para remover o bind. Ferramentas mise, configurações e credenciais do usuário são preservadas. Esse comando não remove automaticamente as dependências dos agentes.

A dependência `qwen-code` fornece o executável `qwen`.
