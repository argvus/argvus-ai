---
title: Kurulumu
description: argvus-ai'yi yükleyin ve her aracının nasıl sağlandığını anlayın.
---

## Paketi yükleyin

ARGVUS depoları yapılandırılmış Arch Linux'ta, argvus-ai orada yayınlandıktan sonra:

```sh
sudo pacman -S argvus-ai
```

Yayımlanmamış yerel bir derleme için, `argvus-ai` kaynak deposunda `make validate` ve `make build` çalıştırın, ardından ortaya çıkan  `argvus-ai` `.pkg.tar.zst`'yu `build/dist/`'den `sudo pacman -U /path/to/package.pkg.tar.zst` ile kurun. Pacman, ana `argvus` paketi de dahil olmak üzere bağımlılıklarını çözebilmelidir.

Paket, `argvus`, `rofi`, `jq`, `mise`, `opencode` ve `openai-codex`'yi gerektirir; Arch, `/bin/sh`'den `bash`'ye kadar sağlar. OpenCode, `opencode` olarak çalışır ve `openai-codex` paketi `codex`'yi sağlar.

## Masaüstü entegrasyonu

Güncellenmiş `argvus-hyprland` ve `argvus-taskbar` paketlerini kullanın. Hyprland, `argvus-ai` tarafından sağlanan isteğe bağlı Lua modülünü yükler. Entegrasyonun Pacman kancası, kurulum veya kaldırma sonrasında standart sistem yapılandırmasını yeniler. Özelleştirilmiş bir kök yapılandırması veya devre dışı bırakılmış otomatik yeniden yükleme, açık bir yeniden yükleme gerektirebilir. Mevcut kişisel kısayol geçersiz kılmaları yetkili olmaya devam eder.

Güncellenmiş `argvus-appearance` projektör, görev çubuğu modülünü korur ve **Kontrol Merkezi > Görünüm > Görev Çubuğu > Simgelemeler > Opsiyonel Modüller > Yapay Zeka Ajanları** ayarına saygı gösterir. Seçenek varsayılan olarak etkindir; değiştirdikten sonra **Uygula**ya tıklayın. Etkinleştirmek, ajanları yüklemez.

## Claude Kod ilk kullanımda

Rofi seçicisinden veya uygulama başlatıcısından Claude Code'u seçin. ARGVUS terminali açılır ve yüklü bir sürüm bulunamazsa `mise install claude`'yu normal kullanıcı olarak çalıştırır. Bu ilk kurulum için ağ erişimi gereklidir. Sarıcı, yüklü yürütülebilir dosyayı çözer ve başlatılan sürecin PATH'ine dizinini ekler; kabuk başlangıç dosyalarını düzenlemez veya root olarak kurulum yapmaz. Daha sonraki başlatmalar kurulumu yeniden kullanır.

## Kaldır

```sh
sudo pacman -R argvus-ai
```

Paket tarafından sahip olunan Lua modülü ve masaüstü girdileri kaldırılır ve yardımcı programı olmadığında görev çubuğu modülü gizlenir. Standart Hyprland yapılandırması bağı kaldırmak için otomatik olarak yeniden yüklenir. Kullanıcıya ait mise araçları, ajan ayarları ve kimlik bilgileri korunur. Pacman bu komutla ajan bağımlılıklarını otomatik olarak kaldırmaz.

ARGVUS AI paketi, paket kurulumu sırasında harici aracıları yüklemez. Hermes, Cursor CLI ve Kimi ilk başlatmada yüklenir; kullanıcı verileri paketin dışında kalır. Kaldırma talimatları için kullanım kılavuzuna bakın.

Arch Extra deposundaki `gemini-cli`, `argvus-ai` bağımlılığı olarak kurulur; ayrıca npm kurulumu gerekmez.
