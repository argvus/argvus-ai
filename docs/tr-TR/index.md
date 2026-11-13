---
title: Yapay Zeka Aracıları
description: ARGVUS masaüstünden programlama aracılarını açın.
---

`argvus-ai`, **OpenCode**, **OpenAI Codex** ve **Claude Code** için isteğe bağlı bir masaüstü entegrasyonudur. Paylaşılan bir Rofi seçici, uygulama başlatıcı girişleri ve görev çubuğu yardımcı program grubunda robot simgesi sağlar. Aracılar yeni bir ARGVUS terminal penceresinde çalışır ve arayanın çalışma dizinini korur.

Seçiciyi **SUPER + A** ile açın veya görev çubuğunda mikrofon ve ses kontrollerinin yanındaki **nf-md-robot** seçeneğine tıklayın. Ayrıca uygulama başlatıcısında tek bir aracıyı da seçebilirsiniz.OpenCode ve Codex paket bağımlılıkları olarak kurulmuştur. Claude Code, ancak ilk kez seçtiğinizde, kullanıcı olarak mise ile kurulur. Paketi yüklemek, seçiciyi açmak/iptal etmek veya durumu kontrol etmek Claude'u asla indirmez. Paket, hesapları, API anahtarlarını veya abonelikleri yapılandırmaz; seçilen aracın kimlik doğrulama istemlerini takip edin.

Kurulum [Installation](/docs/argvus-ai/installation/) ve [Kullanım ve sorun giderme](/docs/argvus-ai/usage/) belgelerini okuyun.

## Diller

The The The The The The The The `ai` katalog tüm 18'de sağlanmaktadır. ARGVUS arayüz dilleri ve paylaşılanları kullanır `argvus i18n` Seçim ve İngilizce geri çekilme. Seçilen arayüz dili depolanır `ARGVUS_LANGUAGE` Kullanıcının içinde `locale.conf`; Sistem bölgesel yerel ayrı kalır. Çeviriler kullanıcı yapılandırması olmadan veri olarak kurulur.

## Desteklenen aracılar

Bu entegrasyon; paketle sunulan OpenCode, Codex ve Qwen Code’u, mise aracılığıyla Claude Code’u, ayrıca kurulduğunda Antigravity’yi ve ilk çalıştırmada resmî kurulum programlarıyla yüklenen Hermes, Cursor CLI ve Kimi’yi destekler. ARGVUS’un yönettiği harici ajanları listeleme ve kaldırma hakkında bilgi için [kullanım kılavuzuna](usage/) bakın.
