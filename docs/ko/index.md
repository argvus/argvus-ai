---
title: AI 에이전트
description: ARGVUS 바탕화면에서 프로그래밍 에이전트를 엽니다.
---
`argvus-ai`는 **OpenCode**, **OpenAI Codex**, **Claude Code**용 선택적 데스크탑 통합 기능입니다. 공유 Rofi 선택기, 애플리케이션 런처 항목, 작업 표시줄 유틸리티 그룹의 로봇 아이콘을 제공합니다. 에이전트는 새로운 ARGVUS 터미널 창에서 실행되며 호출자의 작업 디렉토리를 유지합니다.

선택기는 **SUPER + A**를 눌러 열거나, 작업 표시줄에서 마이크와 오디오 컨트롤 옆의 **nf-md-robot**을 클릭하여 열 수 있습니다. 또한 애플리케이션 런처에서 개별 에이전트를 선택할 수도 있습니다.

OpenCode와 Codex는 패키지 의존성으로 설치됩니다. Claude Code는 사용자가 처음 선택할 때만 mise로 설치됩니다. 패키지를 설치하거나 선택기를 열거나 취소하거나 상태를 확인해도 Claude는 다운로드되지 않습니다. 이 패키지는 계정, API 키 또는 구독을 설정하지 않으며, 선택한 에이전트의 인증 안내를 따르십시오.

[설치](/docs/argvus-ai/installation/) 및 [사용법 및 문제 해결](/docs/argvus-ai/usage/)를 읽으십시오.

## 언어

더 보기 `ai` 모든 18 카탈로그가 제공됩니다. ARGVUS 인터페이스 언어 및 공유 `argvus i18n` 선택과 영어 fallback. 선택한 인터페이스 언어는 저장됩니다. `ARGVUS_LANGUAGE` 사용자의 `locale.conf`; 체계 지역 Locale는 분리됩니다. 번역은 사용자 구성을 작성하지 않고 데이터로 설치됩니다.

## 지원되는 에이전트

이 통합은 패키지로 제공되는 OpenCode, Codex, Qwen Code와 mise를 통해 설치하는 Claude Code를 지원합니다. Antigravity는 별도로 설치해야 하며, Hermes, Cursor CLI, Kimi는 처음 실행할 때 공식 설치 프로그램을 통해 설치됩니다. ARGVUS가 관리하는 외부 에이전트의 목록을 확인하고 제거하는 방법은 [사용 안내서](usage/)를 참조하세요.

Gemini CLI는 Arch `gemini-cli` 의존성으로 제공되며 `gemini` 명령을 사용할 수 있으면 선택기에 표시됩니다.
