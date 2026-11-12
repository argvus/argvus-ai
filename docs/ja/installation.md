---
title: インストール
description: argvus-ai をインストールし、各エージェントがどのように提供されるかを理解する。
---
## パッケージをインストールする

ARGVUS リポジトリが設定されている Arch Linux では、argvus-ai が公開され次第、次のようにします:

```sh
sudo pacman -S argvus-ai
```
未公開のローカルビルドの場合、`argvus-ai` ソースリポジトリで `make validate` と `make build` を実行し、その後 `argvus-ai` から得られた `.pkg.tar.zst` を  `build/dist/` `sudo pacman -U /path/to/package.pkg.tar.zst` でインストールしてください。Pacman はマスター `argvus` パッケージを含む依存関係を解決できる必要があります。

このパッケージは `argvus`、`rofi`、`jq`、`mise`、`opencode`、および `openai-codex` を必要とします；Arch は bash を通じて `/bin/sh` を提供します。OpenCode は  `bash` `opencode` として実行され、`openai-codex` パッケージは `codex` を提供します。

## デスクトップ統合

更新された `argvus-hyprland` と `argvus-taskbar` パッケージを使用してください。Hyprland は `argvus-ai` によって提供されるオプションの Lua モジュールをロードします。統合の Pacman フックは、インストールまたは削除後に標準のシステム設定を更新します。カスタムルート設定や自動再読み込み無効化の場合は、明示的な再読み込みが必要になる可能性があります。既存の個人用ショートカットの上書きは引き続き優先されます。

更新された`argvus-appearance`プロジェクターはタスクバー モジュールを保持し、**コントロールセンター > 外観 > タスクバー > アイコン > オプションモジュール > AI エージェント**を尊重します。このオプションはデフォルトで有効になっています。変更後は**適用**をクリックしてください。有効化してもエージェントはインストールされません。

## 初回使用時のClaude Code

RofiセレクターまたはアプリケーションランチャーからClaude Codeを選択します。インストール済みバージョンが見つからない場合、ARGVUSターミナルが開き、通常ユーザーとして`mise install claude`を実行します。初回インストールにはネットワークアクセスが必要です。ラッパーはインストール済みの実行ファイルを解決し、起動プロセスのPATHにそのディレクトリを追加します。シェルの起動ファイルを編集したり、rootとしてインストールすることはありません。後の起動はインストール済みのものを再利用します。

## 削除

```sh
sudo pacman -R argvus-ai
```
パッケージ所有のLuaモジュールとデスクトップエントリは削除され、ヘルパーがない場合、タスクバーモジュールは非表示になります。標準のHyprland設定は、バインドを削除するために自動的にリロードされます。ユーザー所有のmiseツール、エージェント設定、および資格情報は保持されます。Pacmanは、このコマンドではエージェントの依存関係を自動的に削除しません。

The ARGVUS AI package does not install external agents at package-install time. Hermes, Cursor CLI and Kimi install on first launch; their user data remains outside the package. See the usage guide for removal instructions.
