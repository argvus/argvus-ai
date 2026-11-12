---
title: AI Agents
description: Buka agen pemrograman dari desktop ARGVUS.
---

`argvus-ai` adalah integrasi desktop opsional untuk **OpenCode**, **OpenAI Codex** dan **Claude Code**. Ini menyediakan pemilih Rofi bersama, entri peluncur aplikasi dan ikon robot di grup utilitas bilah tugas. Agen berjalan di jendela terminal ARGVUS baru dan mempertahankan direktori kerja pemanggil.

Buka pemilih dengan **SUPER + A** atau klik **nf-md-robot** di taskbar, di samping mikrofon dan kontrol audio. Anda juga dapat memilih agen individual di peluncur aplikasi.

OpenCode dan Codex diinstal sebagai dependensi paket. Claude Code diinstal dengan mise, sebagai pengguna Anda, hanya saat Anda pertama kali memilihnya. Menginstal paket, membuka/membatalkan pemilih, atau memeriksa status tidak pernah mengunduh Claude. Paket ini tidak mengonfigurasi akun, kunci API, atau langganan; ikuti perintah autentikasi agen yang dipilih.

Baca [Instalasi](/docs/argvus-ai/installation/) dan [Penggunaan dan pemecahan masalah](/docs/argvus-ai/usage/).

## Bahasa

Katalog `ai` disediakan dalam sepuluh bahasa ARGVUS dan menggunakan pilihan `argvus i18n` bersama dan fallback bahasa Inggris. Terjemahan diinstal sebagai data tanpa menulis konfigurasi pengguna.

## Supported agents

The integration supports package-provided OpenCode, Codex and Qwen Code; Claude Code through mise; Antigravity when installed separately; and Hermes, Cursor CLI and Kimi through their official installers on first launch. Use the [usage guide](usage/) for listing and uninstalling ARGVUS-managed external agents.
