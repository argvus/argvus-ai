---
title: Instalasi
description: Pasang argvus-ai dan pahami bagaimana setiap agen disediakan.
---

## Pasang paket

Di Arch Linux dengan repositori ARGVUS dikonfigurasi, setelah `argvus-ai` diterbitkan di sana:

```sh
sudo pacman -S argvus-ai
```

Untuk build lokal yang belum dipublikasikan, jalankan `make validate` dan `make build` di repositori sumber `argvus-ai`, kemudian pasang `.pkg.tar.zst` yang dihasilkan dari `build/dist/` dengan `sudo pacman -U /path/to/package.pkg.tar.zst`. Pacman harus mampu menyelesaikan dependensinya, termasuk paket `argvus` utama.

Paket ini membutuhkan `argvus`, `rofi`, `jq`, `mise`, `opencode` dan `openai-codex`; Arch menyediakan `/bin/sh` sampai `bash`. OpenCode dijalankan sebagai `opencode`, dan paket `openai-codex` menyediakan `codex`.

## Integrasi Desktop

Gunakan paket `argvus-hyprland` dan `argvus-taskbar` yang diperbarui. Hyprland memuat modul Lua opsional yang disediakan oleh `argvus-ai`. Kait Pacman integrasi menyegarkan konfigurasi sistem standar setelah instalasi atau penghapusan. Konfigurasi root khusus atau muat ulang otomatis yang dinonaktifkan mungkin memerlukan muat ulang secara eksplisit. Penggantian pintasan pribadi yang ada tetap bersifat otoritatif.Proyektor `argvus-appearance` `mise install claude`  yang diperbarui mempertahankan modul taskbar dan menghormati **Control Center > Appearance > Taskbar > Icons > Optional modules > AI Agents**. Opsi ini diaktifkan secara default; klik **Apply** setelah mengubahnya. Mengaktifkannya tidak menginstal agen.

## Claude Code pada penggunaan pertama

Pilih Claude Code dari pemilih Rofi atau peluncur aplikasi. Terminal ARGVUS terbuka dan berjalan

 sebagai pengguna reguler Anda jika tidak ada versi terinstal yang ditemukan. Akses jaringan diperlukan untuk instalasi pertama ini. Pembungkusnya menyelesaikan executable yang diinstal dan menambahkan direktorinya ke proses yang diluncurkan PATH; itu tidak mengedit file startup shell atau menginstal sebagai root. Peluncuran kemudian menggunakan kembali instalasi.

## Hapus

```sh
sudo pacman -R argvus-ai
```

Modul Lua yang dimiliki paket dan entri desktop dihapus, dan modul taskbar menyembunyikan ketika pembantunya tidak ada. Konfigurasi standar Hyprland memuat ulang secara otomatis untuk menghapus bind. Alat mise yang dimiliki pengguna, pengaturan agen, dan kredensial dipertahankan. Pacman tidak secara otomatis menghapus dependensi agen dengan perintah ini.

Paket AI ARGVUS tidak menginstal agen eksternal pada waktu instalasi paket. Hermes, Cursor CLI dan Kimi diinstal pada peluncuran pertama; data pengguna mereka tetap berada di luar paket. Lihat panduan penggunaan untuk instruksi penghapusan.

Paket `gemini-cli` dari Arch Extra dipasang sebagai dependensi `argvus-ai`; npm terpisah tidak diperlukan.
