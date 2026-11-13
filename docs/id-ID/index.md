---
title: Agen AI
description: Buka agen pemrograman dari desktop ARGVUS.
---

`argvus-ai` adalah integrasi desktop opsional untuk **OpenCode**, **OpenAI Codex** dan **Claude Code**. Ini menyediakan pemilih Rofi bersama, entri peluncur aplikasi dan ikon robot di grup utilitas bilah tugas. Agen berjalan di jendela terminal ARGVUS baru dan mempertahankan direktori kerja pemanggil.

Buka pemilih dengan **SUPER + A** atau klik **nf-md-robot** di taskbar, di samping mikrofon dan kontrol audio. Anda juga dapat memilih agen individual di peluncur aplikasi.

OpenCode dan Codex diinstal sebagai dependensi paket. Claude Code diinstal dengan mise, sebagai pengguna Anda, hanya saat Anda pertama kali memilihnya. Menginstal paket, membuka/membatalkan pemilih, atau memeriksa status tidak pernah mengunduh Claude. Paket ini tidak mengonfigurasi akun, kunci API, atau langganan; ikuti perintah autentikasi agen yang dipilih.

Baca [Instalasi](/docs/argvus-ai/installation/) dan [Penggunaan dan pemecahan masalah](/docs/argvus-ai/usage/).

## Bahasa

The `ai` katalog disediakan dalam semua 18 ARGVUS antar bahasa dan menggunakan berbagi `argvus i18n` seleksi dan mundur Inggris. Bahasa antar muka yang dipilih disimpan sebagai `ARGVUS_LANGUAGE` di pengguna `locale.conf`; sistem lokal regional tetap terpisah. Terjemahan diinstal sebagai data tanpa konfigurasi pengguna menulis.

## Agen yang didukung

Integrasi ini mendukung OpenCode, Codex, dan Qwen Code yang disertakan dalam paket; Claude Code melalui mise; Antigravity jika dipasang secara terpisah; serta Hermes, Cursor CLI, dan Kimi yang dipasang lewat installer resminya saat pertama kali dijalankan. Lihat [panduan penggunaan](usage/) untuk melihat daftar dan menghapus agen eksternal yang dikelola ARGVUS.
