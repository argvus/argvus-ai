---
title: Installation
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

Select Claude Code from the Rofi selector or application launcher. The ARGVUS terminal opens and runs 

 as your regular user if no installed version is found. Network access is needed for this first installation. The wrapper resolves the installed executable and adds its directory to the launched process PATH; it does not edit shell startup files or install as root. Later launches reuse the installation.

## Remove

```sh
sudo pacman -R argvus-ai
```

Modul Lua yang dimiliki paket dan entri desktop dihapus, dan modul taskbar menyembunyikan ketika pembantunya tidak ada. Konfigurasi standar Hyprland memuat ulang secara otomatis untuk menghapus bind. Alat mise yang dimiliki pengguna, pengaturan agen, dan kredensial dipertahankan. Pacman tidak secara otomatis menghapus dependensi agen dengan perintah ini.

The ARGVUS AI package does not install external agents at package-install time. Hermes, Cursor CLI and Kimi install on first launch; their user data remains outside the package. See the usage guide for removal instructions.
