---
title: 설치
description: argvus-ai를 설치하고 각 에이전트가 어떻게 제공되는지 이해하세요.
---
## 패키지 설치

ARGVUS 리포지토리가 구성된 Arch Linux에서, argvus-ai가 게시되면 그곳에서:

```sh
sudo pacman -S argvus-ai
```
미발행 로컬 빌드를 위해, `argvus-ai` 소스 저장소에서 `make validate`와 `make build`를 실행한 후, `argvus-ai`에서 나온 `.pkg.tar.zst`를  `build/dist/` `sudo pacman -U /path/to/package.pkg.tar.zst`로 설치합니다. Pacman은 마스터 `argvus` 패키지를 포함한 의존성을 해결할 수 있어야 합니다.

이 패키지는 `argvus`, `rofi`, `jq`, `mise`, `opencode` 및 `openai-codex`가 필요하며, Arch는 bash를 통해 `/bin/sh`를 제공합니다. OpenCode는  `bash` `opencode`로 실행되며, `openai-codex` 패키지는 `codex`를 제공합니다.

## 데스크톱 통합

업데이트된 `argvus-hyprland` 및 `argvus-taskbar` 패키지를 사용합니다. Hyprland는 `argvus-ai`에서 제공하는 선택적 Lua 모듈을 로드합니다. 통합 Pacman 훅은 설치 또는 제거 후 표준 시스템 구성을 새로 고칩니다. 사용자 지정 루트 구성이나 자동 다시 로드 비활성화는 명시적 재로드가 필요할 수 있습니다. 기존 개인 단축키 재정의는 여전히 우선권을 가집니다.

업데이트된 `argvus-appearance` 프로젝터는 작업 표시줄 모듈을 유지하며 **제어 센터 > 모양 > 작업 표시줄 > 아이콘 > 선택적 모듈 > AI 에이전트**를 존중합니다. 이 옵션은 기본적으로 활성화되어 있으며, 변경 후 **적용**을 클릭하십시오. 활성화해도 에이전트가 설치되지는 않습니다.

## 최초 사용 시 Claude Code

Rofi 선택기나 애플리케이션 실행기에서 Claude Code를 선택하십시오. 설치된 버전이 없으면 ARGVUS 터미널이 열리고 일반 사용자 권한으로 `mise install claude`를 실행합니다. 초기 설치에는 네트워크 접근이 필요합니다. 래퍼는 설치된 실행 파일을 확인하고 해당 디렉터리를 실행된 프로세스 PATH에 추가합니다; 셸 시작 파일을 수정하거나 root로 설치하지는 않습니다. 이후 실행에서는 설치를 재사용합니다.

## 제거

```sh
sudo pacman -R argvus-ai
```
패키지 소유 Lua 모듈과 데스크톱 항목이 제거되며, 도우미가 없으면 작업 표시줄 모듈이 숨겨집니다. 표준 Hyprland 구성은 바인드를 제거하기 위해 자동으로 다시 로드됩니다. 사용자 소유의 mise 도구, 에이전트 설정 및 자격 증명은 유지됩니다. Pacman은 이 명령으로 에이전트 종속성을 자동으로 제거하지 않습니다.

The ARGVUS AI package does not install external agents at package-install time. Hermes, Cursor CLI and Kimi install on first launch; their user data remains outside the package. See the usage guide for removal instructions.
