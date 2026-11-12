---
title: Kullanım ve sorun giderme
description: Aracıları seçin, görev çubuğu simgesini kontrol edin ve eksik entegrasyonları teşhis edin.
---

## Bir temsilci açın

**SUPER + A** tuşlarına basın, görev çubuğu robotuna tıklayın veya bir aracının uygulama girişini seçin. Seçici, yürütülebilir OpenCode/Codex kurulumları sunar ve yanlışlık mevcut olduğunda ilk kullanım kurulumu için Claude Kodu sunar. **Esc** herhangi bir şeyi başlatmadan veya indirmeden iptal edilir.Terminal arayanın çalışma dizinini devralır; Grafiksel başlatmalar genellikle oturumun ana dizininden başlar. Belirli bir çalışma dizinine ihtiyaç duyduğunuzda bir proje terminalinden bir aracı başlatın.

## Görev çubuğu görünürlüğüAçın **Kontrol Merkezi > Görünüm > Görev Çubuğu > Simgeler > İsteğe bağlı modüller**, **Yapay Zeka Ajanları**nı açıp kapatın, ardından **Uygula**'ya tıklayın. Robot `group/right-2`'ya aittir; çekmecesi kapalıysa, yardımcı araçlar grubunu genişletin. Tercih `/taskbar/icons/ai_agents_enabled`'dir, varsayılan olarak true’dur ve yeniden oluşturmayı da korur. Yalnızca simgeyi kontrol eder: kısayollar ve masaüstü girdileri kullanılabilir durumda kalır. Çalışma zamanı kullanılabilirliği, etkinleştirilmiş bir simgeyi yine de gizleyebilir.

## Tanısal komutlar

```sh
argvus-ai list
argvus-ai status
argvus-ai status --check
argvus-ai menu
argvus-ai launch opencode
argvus-ai launch codex
argvus-ai launch claude
```

`list` yalnızca yüklü aracıları bildirir. `status` Waybar JSON'u yayar, `status --check` ise çıkış durumu aracılığıyla yüklü veya kurulabilir bir menü seçeneği olup olmadığını bildirir. Yalnızca Claude seçildiğinde/başlatıldığında kurulumu başlatılabilir; `run-claude` dahili bir terminal giriş noktasıdır.

Kısayol hâlâ eski kombinasyonu kullanıyorsa Denetim Merkezi'nin klavye kısayolları sayfasında kişisel geçersiz kılmayı inceleyin; paketlenmiş varsayılanlar bunun üzerine yazmaz. Görünüm ayarlarını uyguladıktan sonra robot kaybolursa `argvus-appearance`'yu güncelleyin ve görev çubuğu ayarlarını yeniden oluşturun/uygulayın. Oluşturulan Waybar/Lua dosyalarını doğrudan düzenlemekten kaçının.Eğer Claude kurulumu başarısız olursa, terminal hatalarını, ağ erişimini ve kurulu mise sürümünü kontrol edin, ardından tekrar Claude'u seçin. mise sorguları ev dizininden çalıştırıldığından proje özelindeki bir yapılandırma farklı bir araç seçmez. Sarmalayıcı, grafiksel PATH içinde mise shims gerektirmez. OpenCode/Codex keşfi grafiksel PATH'i kullanır, kabuk takma adları veya etkileşimli başlangıç betikleri olmadan.

[AI Agents](/docs/argvus-ai/) sayfasına dönün.

Ajanlar, `ARGVUS AI Agent` başlıklı ortalanmış bir yüzen Kitty penceresinde, ARGVUS başlığı ve altbilgisi ile açılır. Ajan penceresini kapatmak için **Ctrl + E** tuşuna basın. Bu kısayol çerçeve tarafından ayrılmıştır; Esc ve Ctrl+C ajan tarafından kullanılabilir durumda kalır.

Özel Kitty profili `ai-agents` sekmeleri gizler ve sekmeler, bölmeler ve tam ekran için devralınan kısayolları temizler. Pano kısayolları Ctrl+Shift+C ve Ctrl+Shift+V kullanılabilir durumda kalır. Oluşturulan yapılandırması ARGVUS önbellek dizini altındaki `kitty-tui/kitty-ai-agents.conf`'dur. Hyprland modülü paketi, 1399 × 920'de `argvus-ai` sınıfına sahip pencereleri yüzdürür ve ortalar.

## Uninstalling agents

`argvus-ai list` shows installed agents. Run `argvus-ai uninstall` to select an ARGVUS-managed Hermes, Cursor CLI, or Kimi installation, then confirm removal. You can also run `argvus-ai uninstall hermes`, `argvus-ai uninstall cursor`, or `argvus-ai uninstall kimi`. Installations made outside ARGVUS are left untouched, except a legacy Cursor CLI install is recognized by the explicit Cursor command when `~/.local/bin/agent` resolves inside `~/.local/share/cursor-agent/versions/`. Hermes uses its official uninstaller. Cursor and Kimi binaries are removed while user settings, sessions, and credentials are preserved.
