# ☁️ Lesson 1 Özeti: Bulut Altyapısı

Bu derste şunları öğrendiniz:

Bulut altyapısı; veri merkezleri, depolama, ağ bileşenleri ve bilgi işlem kaynaklarından oluşur.

Sanallaştırma,  *hypervisor* ’lar sayesinde mümkün olan, fiziksel kaynakların yazılım tabanlı bir sürümünü oluşturma sürecidir.

Bulutta sağlanabilen birkaç farklı *Virtual Machine (VM)* türü vardır. Bunlar şunları içerir:

* Sağlayıcı tarafından yönetilen, çok kiracılı (multi-tenant) dağıtımlar olan ve önceden tanımlı boyutlarla isteğe bağlı (on-demand) sağlanabilen Paylaşımlı veya Genel Bulut VM’leri (Shared veya Public Cloud VMs)
* Bir bulut veri merkezindeki kullanılmayan kapasiteden yararlanan Geçici (Transient) veya Spot VM’ler
* Gelecekteki dağıtımlar için kapasite ayırmanıza ve kaynakları garanti etmenize olanak tanıyan Ayrılmış (Reserved) VM’ler
* Tek kiracılı (single-tenant) izolasyon sunan Dedicated host’lar

Bare metal sunucular, tek bir müşteriye adanmış tek kiracılı (single-tenant) fiziksel sunuculardır. Bare metal sunucular, yüksek performanslı bilgi işlem (HPC) ve veri yoğun uygulamaların zorlu ihtiyaçlarını karşılar. Yüksek düzeyde güvenlik veya uyumluluk gereksinimleri olan uygulamalar için idealdir.

Buluttaki ağ yetenekleri, raf tipi cihazlar (rack-mounted devices) biçiminde değil, hizmet olarak sunulur. VM’ler (veya VSI’lar), depolama, ağ bağlantısı ve yük dengeleyiciler (load balancers) gibi bulut kaynakları,  *Virtual Private Cloud (VPC)* ’ler içindeki  *subnet* ’lere dağıtılır. Özel (private) ve genel (public) subnet’lerin kullanılması, kullanıcıların çok katmanlı kurumsal uygulamaları güvenli bir şekilde dağıtmasına olanak tanır. Yük dengeleyiciler trafiği dağıtır ve uygulamaların duyarlı (responsive) olmasını sağlar.

Container’lar, uygulama kodu, kütüphaneleri ve bağımlılıklarının ortak bir şekilde paketlendiği, böylece masaüstlerinden geleneksel BT’ye ve buluta kadar her yerde çalıştırılabilen çalıştırılabilir yazılım birimleridir. Container’lar,  *Virtual Machine* ’lere göre daha hafiftir ve daha az kaynak tüketir; bu da bulut yerel (cloud native) uygulamaların geliştirilmesini ve dağıtımını kolaylaştırmaya yardımcı olur.
