---
title: Agentes de IA
description: Abra agentes de programação pelo desktop ARGVUS.
---

`argvus-ai` é uma integração opcional do desktop com **OpenCode**, **OpenAI Codex** e **Claude Code**. Fornece um seletor Rofi compartilhado, entradas no lançador de aplicativos e o ícone de robô no grupo de utilitários da taskbar. Os agentes abrem em uma nova janela do terminal ARGVUS e preservam o diretório de trabalho de quem os iniciou.

Abra o seletor com **SUPER + A** ou clique em **nf-md-robot** na taskbar, junto aos controles de microfone e áudio. Também é possível escolher cada agente no lançador de aplicativos.

OpenCode e Codex são instalados como dependências do pacote. O Claude Code é instalado pelo mise, no seu usuário, somente quando você o seleciona pela primeira vez. Instalar o pacote, abrir/cancelar o seletor ou consultar o status não baixa o Claude. O pacote não configura contas, chaves de API ou assinaturas; siga a autenticação solicitada pelo agente escolhido.

Leia [Instalação](/pt/docs/argvus-ai/installation/) e [Uso e solução de problemas](/pt/docs/argvus-ai/usage/).

## Idiomas

O catálogo `ai` está disponível nos dez idiomas do ARGVUS e usa a seleção compartilhada de `argvus i18n`, com fallback inglês. As traduções são instaladas como dados, sem gravar configurações do usuário.

## Agentes disponíveis

A integração oferece OpenCode, Codex e Qwen Code pelo pacote; Claude Code pelo mise; Antigravity quando instalado separadamente; e Hermes, Cursor CLI e Kimi pelos instaladores oficiais no primeiro uso. Consulte o [guia de uso](usage/) para listar e desinstalar agentes externos gerenciados pelo ARGVUS.
