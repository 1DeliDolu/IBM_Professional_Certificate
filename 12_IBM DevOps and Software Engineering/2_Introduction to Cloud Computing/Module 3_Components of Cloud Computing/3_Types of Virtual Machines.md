# 🖥️ Sanal Makine Türleri

Sanal Makineler (*Virtual Machines* veya  *VMs* ), bulut sağlayıcısına bağlı olarak  *Virtual Servers* , *Virtual Instances* ya da kısaca *instances* olarak da bilinir. Çeşitli bulut sağlayıcıları, farklı kullanım senaryolarına hizmet etmek için VM’leri çok çeşitli konfigürasyonlar ve dağıtım seçenekleriyle sunar.

Bulutta bir sanal sunucu oluşturduğunuzda, sunucunun sağlanmasını istediğiniz **Region** ve **Zone** veya  **Data Center** ’ı ve üzerinde çalışmasını istediğiniz  **Operating System** ’i belirtirsiniz. Paylaşımlı (yani  *multi-tenant* ) VM’ler veya adanmış (yani  *single-tenant* ) VM’ler arasında seçim yapabilirsiniz. Ayrıca saatlik veya aylık faturalandırma arasında seçim yapabilir ve sanal sunucu için depolama ile ağ seçeneklerini belirleyebilirsiniz.

Şimdi bulutta sağlanabilen birkaç farklı VM türüne bakalım.

---

## ☁️ Paylaşımlı veya Genel Bulut VM’leri

Paylaşımlı veya Genel Bulut VM’leri, sağlayıcı tarafından yönetilen, *multi-tenant* dağıtımlardır ve önceden tanımlanmış boyutlarla talep üzerine sağlanabilir.

*Multi-tenant* olması, altta yatan fiziksel sunucunun sanallaştırıldığı ve diğer kiracılar veya kullanıcılarla paylaşıldığı anlamına gelir. Farklı iş yüklerini karşılamak için bulut sağlayıcıları, tek bir sanal çekirdek ve az miktarda RAM’den, birden fazla sanal çekirdeğe ve çok daha yüksek RAM miktarlarına kadar değişen ön tanımlı boyutlar ve konfigürasyonlar sunar.

Örneğin, *Compute Intensive* iş yükleri, *Memory intensive* iş yükleri veya *High Performance I/O* için konfigürasyonlar olabilir. Yalnızca önceden tanımlanmış boyutlardan seçmek yerine, bazı sağlayıcılar kullanıcıların çekirdek sayısını, RAM’i ve yerel depolama özelliklerini tanımlamasına izin veren özel konfigürasyonlar da sunar.

Genel VM’ler genellikle saatlik (bazı durumlarda saniyelik) fiyatlandırılır ve konfigürasyonlar saat başına birkaç kuruş gibi düşük seviyelerden başlayabilir. Bazı sağlayıcılar aylık VM seçenekleri de sunar; bu, VM’yi en az bir ay çalıştıracağınızı biliyorsanız maliyet tasarrufu sağlayabilir, ancak ayın ortasında VM’yi *de-commission* etmeye karar verirseniz yine de tüm ay için ücretlendirilirsiniz.

---

## ⚡ Geçici veya Spot VM’ler

Geçici veya Spot VM’ler, bir bulut veri merkezindeki kullanılmayan kapasiteden yararlanır.

Bulut sağlayıcıları bu kullanılmayan kapasiteyi, benzer boyutlardaki normal VM’lere kıyasla çok daha düşük bir maliyetle kullanıcılara sunar. Ancak Geçici VM’ler büyük bir indirimle sunulsa da, bulut sağlayıcı herhangi bir zamanda bunları *de-provision* etmeyi ve kaynakları normal, daha yüksek fiyatlı VM’leri sağlamak için geri almayı seçebilir.

Veri merkezindeki kapasite azaldığında bu VM’leri kaybetme riski taşıdığınız için, bu VM’ler test ve uygulama geliştirme gibi üretim dışı ( *non-production* ) iş yükleri için çok uygundur. Ayrıca durumsuz ( *stateless* ) iş yüklerini çalıştırmak, ölçeklenebilirliği test etmek veya büyük veri ile yüksek performanslı hesaplama ( *HPC* ) iş yüklerini düşük maliyetle çalıştırmak için de yararlıdır.

---

## 📌 Rezerve Sanal Sunucu Instance’ları

Rezerve sanal sunucu instance’ları, kapasite ayırmanıza ve gelecekteki dağıtımlar için kaynakları garanti altına almanıza olanak tanır.

İstediğiniz miktarda sanal sunucu kapasitesini rezerve eder, ihtiyaç duyduğunuzda bu kapasiteden instance’lar sağlarsınız ve rezerve kapasiteniz için 1 yıl veya 3 yıl gibi bir süre ( *term* ) seçersiniz. Sözleşme süresi boyunca, seçtiğiniz veri merkezi içinde bu kapasite size garanti edilir.

Daha uzun bir süreye taahhüt ederek, saatlik veya aylık instance’lara kıyasla maliyetlerinizi de düşürebilirsiniz. Bu, belirli bir süre boyunca en az belirli bir seviyede bulut kapasitesine ihtiyacınız olduğunu bildiğiniz durumlarda faydalı olabilir.

Rezerve kapasitenizi aşarsanız, planlanmamış kullanım ve kapasite gereksinimlerinizi saatlik veya aylık VM’lerle desteklemeyi her zaman seçebilirsiniz. Ancak tüm ön tanımlı VM ailelerinin veya konfigürasyonlarının rezerve olarak mevcut olmayabileceğini unutmayın.

---

## 🏢 Adanmış Host’lar

Adanmış host’lar, *single-tenant* izolasyon sunar. Bu, belirli bir host üzerinde yalnızca sizin VM’lerinizin çalıştığı ve böylece alttaki donanımın tam kapasitesi ile kaynaklarının münhasır kullanımının mümkün olduğu anlamına gelir.

Adanmış bir host sağlarken, host’un yerleştirilmesini istediğiniz **data center** ve  **POD** ’u belirtmeniz gerekir. Ardından instance’ları, yani sanal makineleri belirli bir host’a atarsınız. Bu, iş yükü yerleşimi üzerinde maksimum kontrol sağlar.

Adanmış host’lar genellikle uyumluluk ve düzenleyici gereksinimleri karşılamak veya belirli lisanslama şartlarını sağlamak için kullanılır.

---

## ✅ Kapanış

Sanallaştırma ve VM’ler, bulut bilişimin merkezindedir ve birçok fayda sağlar. Bir sonraki videoda,  *bare metal servers* ’ı, bunların ne olduğunu ve ne sağladıklarını tartışacağız.
