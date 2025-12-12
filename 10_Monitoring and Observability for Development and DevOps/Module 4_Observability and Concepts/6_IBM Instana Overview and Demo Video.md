# 🧭 IBM Instana Genel Bakış ve Demo Videosu

IBM Instana genel bakış ve demo videosuna hoş geldiniz. Bu videoyu izledikten sonra,  *Instana* ’yı ve kullanım alanlarını açıklayabileceksiniz.

---

## 🔎 IBM Instana Observability Nedir ve Ne İşe Yarar?

IBM Instana Observability, yaygın olarak *Instana* olarak bilinir; tamamen otomatikleştirilmiş bir *uygulama performans yönetimi* ( *APM* ) çözümüdür. *Mikroservisleri* ve *bulut yerel (cloud-native)* uygulamaları yönetmenin zorluklarının üstesinden gelmek için tasarlanmıştır.

Instana; uygulamalarınızı ve servislerinizi otomatik olarak görünür hâle getirir, gözlemlenen bilgilere bağlam kazandırır ve bu bilgilere dayanarak akıllı aksiyonlar almanızı sağlar.

---

## 🧩 İzleme Kapsamı ve Otomasyon Yetenekleri

Instana; uygulamalarınızı, servislerinizi, altyapınızı, web’i, tarayıcıları, mobil uygulamaları ve daha fazlasını, 200’den fazla alan-özel (domain-specific) teknoloji için izler ve analiz eder.

Instana; tam yığın (full stack) boyunca bağımlılık haritalamasını otomatikleştirir, esnek uygulama perspektifleri sunar ve güçlü, kullanımı kolay veri analitiği sağlar.

Instana; müşterilerinizin, uygulamalarınızdaki performans veya kararlılık sorunlarından etkilendiği durumları etki başladıktan sonraki birkaç saniye içinde size bildirir.

---

## 🧠 Kök Neden Analizi, Metrikler ve İzler

Buna ek olarak Instana; olay korelasyonu, performans eşikleri, hatalar, değişiklikler ve *servis seviyesi anlaşması* veya *SLA* ihlallerinin analizi ile kök neden analizini otomatikleştirir.

Instana ayrıca 1 saniye ayrıntı düzeyinde gerçek zamanlı gözlemlenebilirlik metrikleri sağlar ve uçtan uca, mobil, web ve uygulama işlemlerinin her birini izler (trace eder).

Otomatik akıllı alarmlar, hazır (out-of-the-box) şablonlara dayalı olarak eşik tabanlı uyarılar sağlar.

---

## 🧰 Teknoloji Alanları ve Altyapının Rolü

Instana; bulut ve altyapı ile ilgili teknolojiler, izleme (tracing), uyarılama (alerting), bildirimler, CI/CD, loglama ve metrikler gibi alanlarda 200’den fazla teknolojiyi izler.

Altyapı, özellikle modern mimarilerde, uygulamalar için ilgili kaynak ve servisleri sağlamak üzere temel katmandır. Altyapı sürekli değişir ve güvenilirlik, ölçekleme ve esneklik sağlamak için kümelenme (clustering) ve otomatik ölçeklendirme (autoscaling) gibi kavramlardan yararlanır.

Instana, altyapının her an izlenmesini ve olduğu gibi temsil edilmesini sağlar. Altyapıda tespit edilen tüm sorunlar ve değişiklikler, uygulama ve son kullanıcı seviyesinde meydana gelen sorunlar ve olaylarla sürekli olarak ilişkilendirilir. Bu da kullanıcılara, uygulamayı sunan tüm parçaların kapsamlı bir şekilde anlaşılmasını sağlar.

---

## 🗺️ Instana Altyapı Haritası

Instana altyapı haritası, izlenen tüm sistemlerin adlandırılmış bölgeler (named zones) altında gruplanmış hâlde genel bir görünümünü sağlar.

Her bölgenin içinde, opak bloklardan oluşan sütunlar (pillars) bulunur. Her bir sütun, ilgili sistem üzerinde çalışan bir ajanı bir bütün olarak temsil eder. Sütunların içindeki her bir blok ise o sistemde çalışan yazılım bileşenlerini temsil eder ve bileşenin sağlığını yansıtmak için renk değiştirir.

---

## 📊 Tipik Instana Panosundaki Bileşenler

Tipik bir Instana panosunda kullanıcılar çeşitli bileşenleri görebilir:

* Veri merkezi veya kullanılabilirlik bölgeleri (availability zones) gibi fiziksel bileşenler
* Ana makineler/hostlar veya makineler
* Her host; darboğaz olabilen CPU, bellek ve IO kaynaklarına sahiptir
* Konteynerler bir host üzerinde çalışır ve Kubernetes veya Apache Mesos gibi bir zamanlayıcı (scheduler) tarafından yönetilebilir
* Süreçler (processes), konteyner içinde veya host üzerinde çalışır
* Kümeler (clusters), birçok servisin bir grup/küme olarak hareket etmesini sağlar; böylece dış dünyaya tek bir dağıtık süreç gibi görünür
* Servisler, API uç noktaları, izler (traces) ve çağrılar (calls) gibi mantıksal bileşenler
* İş servisleri ve süreçler gibi iş bileşenleri

Instana, yaygın kullanım senaryolarını desteklemek ve özel panolara olan ihtiyacı ortadan kaldırmak için derlenmiş (curated) panolar sunar. Ancak kullanıcının özel pano oluşturabileceği durumlar da vardır.

---

## 🧩 Instana Ajanları ve Sensörler

Teknoloji yığınlarınızı ihtiyacınıza göre izlemek için Instana ajanlarını yükleyebilirsiniz.

Bir host ajanı (host agent), Instana arka ucuna göndermeden önce çeşitli sensörlerden gelen birleştirilmiş verileri toplamak için host üzerinde çalışır.

Host ajanını; sanal makine (VM), fiziksel host, Kubernetes, Cloud Foundry, VMware Tanzu veya benzeri platformlara yükleyebilirsiniz.

Host ajanını yükledikten sonra, belirli teknolojileri izlemek üzere tasarlanmış Instana sensörleri otomatik olarak yüklenir. Ancak bazı sensörler için bu sensörlerin çalışması adına ek yapılandırma yapmanız gerekebilir.

Ekranda ajan yüklemek için desteklenen platformların listesini görebilirsiniz.

---

## 🌐 Web Sitesi İzleme ve Mobil Uygulama İzleme

Web sitesi izleme, genellikle *son kullanıcı izleme* veya *EUM* ya da *gerçek kullanıcı izleme* veya *RUM* olarak adlandırılır; dijital kullanıcı deneyimini anlamak için önemli bir araçtır.

Instana, gerçek tarayıcı istek sürelerini ve rota yükleme sürelerini analiz ederek web sitesi izlemeyi destekler. Kullanıcıların web’de gezinme deneyimine dair ayrıntılı içgörüler ve uygulama çağrı yollarına derin görünürlük sağlar.

Instana, gerçek URL istek sürelerini analiz ederek mobil uygulama izlemeyi destekler; kullanıcıların uygulama deneyimine dair ayrıntılı içgörüler ve uygulama çağrı yollarına net görünürlük sunar.

Instana uygulama izleme çözümü, mobil uygulamalara bağımlılık (dependency) olarak kurulan bir iOS veya Android ajanı kullanır.

---

## 📈 Sınırsız Analitik ve Etiket Tabanlı Analiz

Instana’nın sınırsız (unbounded) analitiği, örneklenmemiş (unsampled) yüksek kardinaliteli verilerin tamamından yeni içgörüler üretmek için sonsuz esneklik sağlar.

Bu yetenek; etiket tabanlı filtreleme, gruplama ve görselleştirme aracılığıyla Dev ve Ops ekiplerindeki tüm üyeler için değer ortaya çıkarır.

Tüm veri kaynakları ve etiketler emrinizdedir; etiket tabanlı sorgu oluşturucu sayesinde öğrenilmesi gereken karmaşık yeni bir sorgu dili yoktur.

---

## 🧱 Analyze Infrastructure Özelliği

Analyze Infrastructure; altyapı merkezli, ad hoc keşif (exploration) çözümü sunar. Bu çözüm, çeşitli özelleştirilebilir ana metrikler üzerinden altyapı varlıklarının çok değişkenli karşılaştırmalarını (multivariate comparisons) kısa ve öz bir tabloda yapmanıza olanak tanır.

Mevcut kaynak özniteliklerini veya etiketleri kullanarak altyapı varlıklarınızı filtreleyip gruplayabilir; varlık kümelerini dinamik olarak karşılaştırabilir ve altyapı sorunlarının kapsamını hızlıca izole edebilirsiniz.

Analyze Infrastructure, şu anda yalnızca IBM Instana Observability SaaS sunumunda kullanılabilen, açık beta (open beta) bir özelliktir.

---

## 🧾 Yerleşik Olaylar ve Özel Olaylar

Yerleşik olaylar (built in events), entegre algoritmalara dayalı önceden tanımlanmış sağlık imzalarıdır (health signatures) ve izleme sisteminizin sağlığını gerçek zamanlı anlamanıza yardımcı olur.

Eğer bir yerleşik olay izlenen sistem için uygun değilse devre dışı bırakılabilir.

Yerleşik olayların sayısı, Instana’nın izlenen sistemlerin sağlığına dair daha iyi içgörüler sağlayacak yeni kurallar üzerinde sürekli çalışması nedeniyle düzenli olarak artmaktadır.

Ayrıca kendi özel olaylarınızı (custom events) yapılandırabilir ve özel sorunları (custom issues) tetikleyebilirsiniz.

Her olayın durumu, etkin (active) veya devre dışı (disabled) olarak da görüntülenir. İstediğiniz zaman bir olayı devre dışı bırakabilirsiniz; ancak yalnızca özel olayları silebilirsiniz.

---

## ✅ Özet

Bu videoda, Instana’nın mikroservis ve bulut yerel uygulamaları yönetmenin zorluklarını aşmak için tasarlanmış, tamamen otomatikleştirilmiş bir uygulama performans yönetimi çözümü olduğunu öğrendiniz.

Ayrıca Instana’nın özelliklerini ve kullanım alanlarını, Instana panolarının çeşitli bileşenlerini incelediniz.

Son olarak, teknoloji yığınlarınızı ihtiyacınıza göre izlemek için Instana ajanlarını yükleme sürecini ve Analyze Infrastructure özelliğini ve faydalarını öğrendiniz.
