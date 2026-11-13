---
title: Penggunaan dan pemecahan masalah
description: Pilih agen, kontrol ikon taskbar dan diagnosa integrasi yang hilang.
---

## Buka agen

Tekan **SUPER + A**, klik robot taskbar atau pilih entri aplikasi agen. Pemilih menawarkan instalasi OpenCode/Codex yang dapat dieksekusi dan menawarkan Claude Code untuk instalasi penggunaan pertama ketika mise ada. **Esc** membatalkan tanpa meluncurkan atau mengunduh apa pun.

Terminal mewarisi direktori kerja pemanggil; peluncuran grafis biasanya dimulai dari direktori home sesi. Mulai agen dari terminal proyek ketika Anda membutuhkan direktori kerja tertentu.

## Visibilitas taskbar

Buka **Control Center > Appearance > Taskbar > Icons > Optional modules**, aktifkan **AI Agents**, lalu klik **Apply**. Robot tersebut milik `group/right-2`; jika lacinya tersembunyi, perluas grup utilitas. Preferensi adalah `/taskbar/icons/ai_agents_enabled`, default true, dan bertahan saat regenerasi. Ini hanya mengontrol ikon: pintasan dan entri desktop tetap tersedia. Ketersediaan saat runtime masih bisa menyembunyikan ikon yang diaktifkan.

## Perintah diagnostik

```sh
argvus-ai list
argvus-ai status
argvus-ai status --check
argvus-ai menu
argvus-ai launch opencode
argvus-ai launch codex
argvus-ai launch claude
```

`list` hanya melaporkan agen yang terpasang. `status` menghasilkan JSON Waybar, sementara `status --check` melaporkan apakah ada pilihan menu yang terpasang atau dapat dipasang melalui status keluarannya. Hanya memilih/meluncurkan Claude yang dapat memulai pemasangannya; `run-claude` adalah titik masuk terminal internal.

Jika pintasan masih menggunakan kombinasi lama, periksa pengaturan pribadi di halaman pintasan keyboard di Control Center; default yang dikemas tidak menimpanya. Jika robot menghilang setelah menerapkan pengaturan tampilan, perbarui `argvus-appearance` dan buat ulang/terapkan pengaturan taskbar. Hindari mengedit file Waybar/Lua yang dihasilkan secara langsung.

Jika instalasi Claude gagal, periksa kesalahan terminal, akses jaringan, dan versi mise yang terpasang, lalu pilih Claude lagi. Kueri mise dijalankan dari home sehingga konfigurasi spesifik proyek tidak memilih alat yang berbeda. Pembungkus tidak memerlukan shim mise di PATH grafis. Penemuan OpenCode/Codex menggunakan PATH grafis, tanpa alias shell atau skrip startup interaktif.

Kembali ke [AI Agents](/docs/argvus-ai/).

Agen terbuka di jendela Kitty mengambang di tengah berjudul `ARGVUS AI Agent`, dengan header dan footer ARGVUS. Tekan **Ctrl + E** untuk menutup jendela agen. Pintasan ini dicadangkan oleh frame; Esc dan Ctrl+C tetap tersedia untuk agen.Profil Kitty khusus `ai-agents` menyembunyikan tab dan menghapus shortcut yang diwarisi untuk tab, split, dan layar penuh. Shortcut clipboard Ctrl+Shift+C dan Ctrl+Shift+V tetap tersedia. Konfigurasi yang dihasilkan adalah `kitty-tui/kitty-ai-agents.conf` di bawah direktori cache ARGVUS. Modul paket Hyprland memfloat dan memusatkan jendela dengan kelas `argvus-ai` pada 1399 × 920.

## Menghapus instalasi agen

`argvus-ai list` menampilkan agen yang terpasang. Jalankan `argvus-ai uninstall` untuk memilih instalasi Hermes, Cursor CLI, atau Kimi yang dikelola ARGVUS, lalu konfirmasi penghapusan. Anda juga dapat menjalankan `argvus-ai uninstall hermes`, `argvus-ai uninstall cursor`, atau `argvus-ai uninstall kimi`. Instalasi dari luar ARGVUS tidak diubah, kecuali instalasi lama Cursor CLI dikenali oleh perintah khusus jika `~/.local/bin/agent` mengarah ke dalam `~/.local/share/cursor-agent/versions/`. Hermes menggunakan penghapus instalasi resminya. Biner Cursor dan Kimi dihapus, sedangkan pengaturan, sesi, dan kredensial pengguna dipertahankan.

Periksa dengan `argvus-ai list`; jalankan `argvus-ai launch gemini` atau pilih dari menu. Autentikasi Google dilakukan di Gemini CLI.
