---
title: 사용법 및 문제 해결
description: 에이전트를 선택하고, 작업 표시줄 아이콘을 제어하며, 누락된 통합을 진단합니다.
---
## 에이전트 열기

**SUPER + A**를 누르고, 작업 표시줄의 로봇을 클릭하거나 에이전트의 애플리케이션 항목을 선택합니다. 선택기는 실행 가능한 OpenCode/Codex 설치를 제공하며, mise가 존재할 경우 최초 사용 설치를 위해 Claude Code를 제공합니다. **Esc**를 누르면 아무 것도 실행하거나 다운로드하지 않고 취소합니다.

터미널은 호출자의 작업 디렉토리를 상속합니다; 그래픽 실행은 보통 세션의 홈 디렉토리에서 시작됩니다. 특정 작업 디렉토리가 필요할 때에는 프로젝트 터미널에서 에이전트를 시작하세요.

## 작업 표시줄 가시성

오른쪽 **제어 센터 > 모양 > 작업 표시줄 > 아이콘 > 선택적 모듈**을 열고, **AI 에이전트**를 켠 다음, **적용**을 클릭하세요. 로봇은 `group/right-2`에 속하며, 서랍이 접혀 있다면 유틸리티 그룹을 확장하세요. 기본 설정은 `/taskbar/icons/ai_agents_enabled`이며, 기본값은 true이고, 재생성 시에도 유지됩니다. 아이콘만 제어하며, 바로 가기와 바탕화면 항목은 계속 사용할 수 있습니다. 런타임 가용성으로 인해 활성화된 아이콘이 숨겨질 수 있습니다.

## 진단 명령어

```sh
argvus-ai list
argvus-ai status
argvus-ai status --check
argvus-ai menu
argvus-ai launch opencode
argvus-ai launch codex
argvus-ai launch claude
```
`list`은 설치된 에이전트만 보고합니다. `status`은 Waybar JSON을 내보내며, `status --check`은 종료 상태를 통해 설치된 메뉴 선택 항목이 있는지 또는 설치 가능한지 보고합니다. Claude를 선택하거나 실행해야만 설치를 시작할 수 있으며, `run-claude`은 내부 터미널 진입점입니다.

단축키가 여전히 이전 조합을 사용한다면, 제어 센터의 키보드 단축키 페이지에서 개인 재정의를 확인하십시오; 패키지 기본값은 이를 덮어쓰지 않습니다. 외형 설정을 적용한 후 로봇이 사라지면, `argvus-appearance`를 업데이트하고 작업 표시줄 설정을 재생성/적용하십시오. 생성된 Waybar/Lua 파일을 직접 편집하는 것은 피하십시오.

클로드 설치에 실패하면 터미널 오류, 네트워크 접근 및 설치된 mise 버전을 확인한 후 클로드를 다시 선택하십시오. mise 쿼리는 홈 디렉토리에서 실행되므로 프로젝트별 구성은 다른 도구를 선택하지 않습니다. 래퍼는 그래픽 PATH에서 mise 쉼이 필요하지 않습니다. OpenCode/Codex 검색은 셸 별칭이나 인터랙티브 시작 스크립트 없이 그래픽 PATH를 사용합니다.

[AI Agents](/docs/argvus-ai/)로 돌아갑니다.

에이전트는 ARGVUS 헤더와 풋터가 있는 `ARGVUS AI Agent`라는 제목의 중앙에 떠 있는 Kitty 창에서 열립니다. 에이전트 창을 닫으려면 **Ctrl + E**를 누르십시오. 이 단축키는 프레임에 예약되어 있으며 Esc와 Ctrl+C는 에이전트에서 계속 사용할 수 있습니다.

전용 Kitty 프로필 `ai-agents`는 탭을 숨기고 탭, 분할 및 전체 화면에 대한 상속된 바로가기를 제거합니다. 클립보드 바로가기 Ctrl+Shift+C 및 Ctrl+Shift+V는 계속 사용할 수 있습니다. 생성된 구성은 ARGVUS 캐시 디렉터리 아래의 `kitty-tui/kitty-ai-agents.conf`입니다. 패키지 Hyprland 모듈은 클래스 `argvus-ai`의 창을 1399 × 920 크기로 띄우고 중앙에 배치합니다.

## Uninstalling agents

`argvus-ai list` shows installed agents. Run `argvus-ai uninstall` to select an ARGVUS-managed Hermes, Cursor CLI, or Kimi installation, then confirm removal. You can also run `argvus-ai uninstall hermes`, `argvus-ai uninstall cursor`, or `argvus-ai uninstall kimi`. Installations made outside ARGVUS are left untouched, except a legacy Cursor CLI install is recognized by the explicit Cursor command when `~/.local/bin/agent` resolves inside `~/.local/share/cursor-agent/versions/`. Hermes uses its official uninstaller. Cursor and Kimi binaries are removed while user settings, sessions, and credentials are preserved.
