---
title: تنصیب
description: argvus-ai ۔ﮯﮨ ﺎﺗﺎﺟ ﺎﯿﮐ ﻢﮨﺍﺮﻓ ﺡﺮﻃ ﺲﮐ ﻮﮐ ﭧﻨﺠﯾﺍ ﺮﮨ ﮧﮐ ﮟﯿﮭﺠﻤﺳ ﺭﻭﺍ ﮟﯾﺮﮐ ﻝﺎﭩﺴﻧﺍ
---

##                                                              ﮟﯾﺮﮐ ﻝﺎﭩﺴﻧﺍ ﺞﯿﮑﯿﭘ

:ﮯﮨ ﺎﺗﻮﮨ ﻊﺋﺎﺷ ﮞﺎﮨﻭ `argvus-ai` ﯽﮨ ﮯﺴﯿﺟ ،ﮟﯿﮨ ﯽﺌﮔ ﯼﺩ ﺐﯿﺗﺮﺗ ﺰﯾﺮﭨﺯﻮﭙﯾﺭ ARGVU

```sh
sudo pacman -S argvus-ai
```

For an unpublished local build, run make validate and make build in the argvus-ai source repository, then install the resulting .pkg.tar.zst from build/dist/ with sudo pacman -U /path/to/package.pkg.tar.zst. Pacman must be able to resolve its dependencies, including the master argvus package.

## ﻦﺸﯾﺮﮕﯿﭩﻧﺍ ﭖﺎﭨ ﮏﺴﯾﮈ



Claude Code ۔ﮯﺗﻮﮨ ﮟﯿﮩﻧ

## ﺮﭘ ﻝﺎﻤﻌﺘﺳﺍ ﮧﺒﺗﺮﻣ ﯽﻠﮩﭘ

Select Claude Code from the Rofi selector or application launcher. The ARGVUS terminal opens and runs  `make validate` `make build`   `argvus-ai`  `.pkg.tar.zst`  `build/dist/`  `sudo pacman -U /path/to/package.pkg.tar.zst`  openai-codex  opencode  bash  /bin/sh  openai-codex  opencode  mise  jq  rofi  `argvus`  `argvus`  `rofi`  `jq`  `mise` `opencode`  `openai-codex`  `/bin/sh`  `bash`  `opencode`  `openai-codex`  `codex`  `argvus-hyprland`  `argvus-taskbar`   `argvus-ai`  `argvus-appearance`  make validate `mise install claude` as your regular user if no installed version is found. Network access is needed for this first installation. The wrapper resolves the installed executable and adds its directory to the launched process PATH; it does not edit shell startup files or install as root. Later launches reuse the installation.

## Remove

```sh
sudo pacman -R argvus-ai
```

The ARGVUS AI package does not install external agents at package-install time. Hermes, Cursor CLI and Kimi install on first launch; their user data remains outside the package. See the usage guide for removal instructions.
