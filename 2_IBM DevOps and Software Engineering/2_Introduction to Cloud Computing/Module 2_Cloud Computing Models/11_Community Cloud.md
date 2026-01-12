# 🌐 Community Cloud

Bu okumada, *community cloud* kavramını ve Google Cloud örneği üzerinden nasıl uygulandığını öğreneceksiniz.

## 🧩 Community cloud nedir?

Bir  *community cloud* , NIST SP 800-145 tarafından şu şekilde tanımlanır:

“Belirli bir tüketici topluluğunun, ortak endişelere (ör. misyon, güvenlik gereksinimleri, politika ve uyumluluk değerlendirmeleri) sahip kuruluşlardan oluştuğu durumlarda, yalnızca bu topluluğun kullanımına özel olarak sağlanan bulut altyapısı. Topluluktaki kuruluşlardan biri veya birkaçı, bir üçüncü taraf ya da bunların bir kombinasyonu tarafından sahip olunabilir, yönetilebilir ve işletilebilir ve kurum içinde veya kurum dışında bulunabilir.”

## 🎯 Neden community cloud?

*Community cloud* yaklaşımı, kuruluşlar tarafından şu nedenlerle kullanılır:

* *Community cloud* üyeleri aynı güvenlik kontrolleri seti altında çalışır.
* Yaklaşım, üyelere vatandaşlık ve yetkilendirme kontrolleri gibi aynı nitelikleri sağlarken, kaynaklara sınırlı fiziksel ve/veya mantıksal erişim verir.
* Ayrıca, *community cloud* veri merkezlerinin konumuna bağlı olarak veri yerelleştirmeyi ve bazı veri egemenliği gereksinimlerini destekler.
* Yaklaşım,  *community cloud* ’u kapsayan bir çevre (perimeter) güvenlik modelini tanımlar.

## 🛡️ Yazılım tanımlı community cloud uygulaması

Bir güvenlik çevresi oluşturmak için, çoğu eski (legacy) *community cloud* başka bulutlardan fiziksel ayrışmaya dayanır. Ancak bu uygulama, sektörün ileri düzey güvenlik, yönetilebilirlik veya uyumluluk gereksinimlerini karşılayamaz.

Modern mimaride, gerekli faydaları sunmak üzere *software-defined community cloud* tasarlanır. Google Cloud, eski yaklaşımların katı fiziksel altyapı kısıtları olmadan güvenlik ve uyumluluk güvenceleri sağlayan yazılım tanımlı bir yaklaşımdır. Google  *community cloud* ’ları, aşağıdakileri yapabilen “ *assured clouds* ” olarak adlandırılan teknolojilerin bir kombinasyonunu kullanır:

* Ortak projeler, güvenlik ve uyumluluk gereksinimleri ve politika etrafında toplulukları tanımlamak.
* Paylaşılan topluluk projelerini diğer projelerden ayırmak.
* Politika tarafından kontrol edilen ve denetlenen (audited) yapılandırma değişikliklerine göre bir topluluğun sınır (boundary) yeteneklerini değiştirmek.

## 📊 Geleneksel ve yazılım tanımlı community cloud karşılaştırması

 *Software-defined community cloud* , geleneksel *community cloud* uygulamasına kıyasla kullanıcılara birçok fayda sağlar. Aşağıdaki tablo, NIST’in verdiği tanımda belirtilen özelliklere göre iki uygulamanın karşılaştırmasını göstermektedir.

| Özellik                                                  | NIST Tanımı SP 800-145                                                                                                                            | Geleneksel Cloud Community Uygulaması                                                                       | Yazılım Tanımlı Community Cloud                                                                                                                      |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Altyapı Münhasırlığı                                | Bulut altyapısı, ortak endişelere sahip kuruluşlardan belirli bir tüketici topluluğu için yalnızca özel kullanım amacıyla sağlanır     | Ayrı altyapıya sahip ayrı veri merkezleri                                                                 | Her proje, izole altyapı ilkel (primitive) bileşenleriyle etkin biçimde bir*private cloud* ’dur                                                    |
| Tüm kullanıcılar ortak güvenlik kontrollerine tabidir | (örtük)                                                                                                                                           | Topluluk tarafından paylaşılan münhasır altyapının tamamında aynı güvenlik kontrolleri geçerlidir | *Assured Workloads*kontrolleri topluluk kapsamına alınır ve hizmet şartları aracılığıyla uygulanır                                           |
| Destek personelinin kişiliği ve vatandaşlığı        | Topluluk içindeki kuruluşlardan biri/birkaçı, üçüncü taraf veya kombinasyonu tarafından sahip olunabilir, yönetilebilir ve işletilebilir | Personel, fiziksel olarak ayrılmış tesislerde bulunmak zorundadır                                        | Erişim yönetimi servisi, desteği gerekli niteliklere sahip personelle sınırlar (*personhood* , vatandaşlık, çalışma konumu ve daha fazlası) |
| Veri yerelleştirme                                       | Kurum içinde veya dışında bulunabilir                                                                                                           | Topluluğa adanmış depolama cihazları                                                                     | Yazılımla zorunlu kılınır                                                                                                                           |
| Tanımlı güvenlik parametresi                           | (örtük)                                                                                                                                           | Topluluk bir*enclave* ’dir                                                                                | Her proje kendi*enclave* ’idir                                                                                                                        |

## 🏛️ Google’da yazılım tanımlı community cloud: Yeni bir “Government Cloud” türü

Google Cloud Platform (GCP)’de bir  *project* , “ *infrastructure primitives* ” için benzersiz, mantıksal bir gruplamadır. Bu bağlamda, bir  *infrastructure primitive* , GCP’deki herhangi bir atomik kapasite birimidir — bir sanal makine ( *VM* ), kalıcı disk ( *PD* ), bir depolama kovası ( *storage bucket* ) ve diğerleri.  *Projects* , herhangi bir bölge ( *region* ) veya bölge altı ( *zone* ) üzerinden *infrastructure primitives* atanabilen “global kaynaklar”dır.

Her  *project* , diğer müşterilerin projelerinden ayrı, bireysel bir projedir.  *Hypervisor* ’lar, Google Cloud Storage ( *GCS* )’nin altında yatan dağıtık blok deposundaki ( *distributed blockstore* ) bloklar ve diğer bileşenler gibi düşük seviyeli kaynaklar, izolasyonu hem mantıksal hem de kriptografik olarak zorunlu kılan kaynak soyutlamalarıyla izole edilir.

NIST SP 800-145’te *Private Cloud* dağıtım modeli şu şekilde tanımlanır:

Bulut altyapısı, birden çok tüketiciyi (iş birimleri gibi) içeren tek bir kuruluşun yalnızca özel kullanımına sağlanır. Kuruluşun kendisi, bir üçüncü taraf ya da bunların bir kombinasyonu tarafından sahip olunabilir, yönetilebilir ve işletilebilir ve kurum içinde veya kurum dışında bulunabilir.

GCP içinde bir *project* oluşturulduğunda, o projeye atanan *infrastructure primitives* yalnızca o proje kapsamına alınır ( *scoped* ). Bu *infrastructure primitives* kapsamlaması, her *Project* için etkili biçimde bir “ *enclave* ” oluşturur.

Veri ikameti ( *data residency* ), destek personeli nitelikleri ve o topluluğa ortak güvenlik kontrolleri için *Assured Workloads* kısıtlarıyla üst üste bindirildiğinde, proje başına bu  *private cloud enclave* ’leri yazılım tanımlı  *community cloud* ’lara dönüşür.

## ✅ Yazılım tanımlı community cloud’un faydaları

Google Cloud’un benimsediği yaklaşım, güvenlik ve uyumluluk gereksinimlerini karşılamak gibi birçok fayda getirir. Yeni donanım, yeni servisler ve mevcut servislerdeki iyileştirmelere, geleneksel  *community cloud* ’lara kıyasla daha hızlı erişilir. Yeni bulut teknolojisinin sisteme alınması ( *onboarded* ) ve kullanılabilir hâle getirilmesi süreci de daha hızlıdır. Genel verimlilik, topluluğa sunulan altyapı ölçeği sayesinde artar; bu da daha iyi erişilebilirlik ( *availability* ) ve performansa dönüşebilir. Güvenlik iyileştirmeleri daha hızlı ölçeklenebilir ve uygulanabilir.

## 🧾 Tanımlar

* **Community Cloud:** Misyon, güvenlik ve uyumlulukla ilgili endişeleri paylaşan kuruluşlardan oluşan belirli bir tüketici topluluğunun yalnızca özel kullanımına sağlanan bulut altyapısı.
* **Software-Defined Community Cloud:** Geleneksel  *community cloud* ’ların fiziksel kısıtları olmadan güvenlik ve uyumluluk sağlayan; daha esnek ve verimli kaynak yönetimine olanak tanımak için modern teknolojiden yararlanan yazılım tanımlı  *community cloud* .
* **Infrastructure Exclusivity:** Paylaşılan endişelerin ele alınmasını sağlamak için bulut kaynaklarının belirli bir topluluğun yalnızca özel kullanımına sunulması.
* **Assured Workloads:** Google Cloud’da  *community cloud project* ’leri için güvenlik ve veri ikameti gereksinimlerine uyumu sağlayan kontrol seti.
