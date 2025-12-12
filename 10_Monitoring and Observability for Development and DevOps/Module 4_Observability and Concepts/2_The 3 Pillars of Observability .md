# 🔭 Observability’nin 3 Temel Sütunu

Three Pillars of Observability’e hoş geldiniz. Bu videoyu izledikten sonra, *gözlemlenebilirliğin (observability) üç temel sütununu* tanımlayabilecek ve *bu üç sütunun avantajlarını* listeleyebileceksiniz.

Gelişmiş bir *mikroservis tabanlı uygulama* geliştiren bir yazılım mühendisi olduğunuzu hayal edin. Pek çok müşteriyi mutsuz eden ciddi bir performans problemini incelemeniz gerekiyor. Mevcut *logları* ve *metrikleri* analiz etmeye başlıyorsunuz, ancak bunlar sistemin davranışına dair yalnızca kısmi bir görünüm sağlıyor. Sorunu farklı servisler arasında izlemek ve kök nedeni anlamak zor. Hayal kırıklığına uğruyorsunuz; çünkü geleneksel izleme (monitoring), ihtiyaç duyduğunuz içgörüleri sağlamada yetersiz kalıyor.

Ancak  *loglar* , *metrikler* ve *izler (traces)* birlikte çalıştığında, sistem davranışı hakkında derin içgörüler ortaya çıkarırlar. Bunlara *gözlemlenebilirliğin üç temel sütunu* denir.  *Loglar* , *metrikler* ve *izleri* kullanarak performans problemlerini kapsamlı biçimde anlayabilir, darboğazları ve genel müşteri deneyimini etkileyen gecikmelere neden olan mikroservisleri belirleyebilirsiniz.

---

## 🧾 Loglar

İlk sütun  *loglardır* . Loglar, genellikle metinsel veya insan tarafından okunabilir biçimde olan olay kayıtlarıdır. Çoğunlukla ağ cihazları ve sunucular da dahil olmak üzere altyapı bileşenleri tarafından üretilirler.

*Platform yazılımları* (middleware ve işletim sistemleri dahil) da log üretebilir.

---

## 📊 Metrikler

İkinci sütun  *metriklerdir* . Bu tür gerçek zamanlı çalışma verilerine genellikle bir API aracılığıyla *pull (çekme)* veya *polling (periyodik sorgulama)* stratejisiyle erişilir ya da *push (itme)* veya *bildirim (notification)* gibi olay/telemetri üretimi şeklinde alınır.

Çoğu arıza yönetimi görevi metrikler tarafından motive edilir; çünkü bunlar  *olay odaklıdır (event-driven)* .

---

## 🧵 İzler

Gözlemlenebilirliğin son sütunu  *izlerdir (traces)* . Bunlar, bir iş öğesini (örneğin bir işlemi/transaction’ı) uygulama mantığının yönlendirdiği adımlar boyunca takip etmek için oluşturulan bilgi yollarının veya iş akışlarının kayıtlarıdır.

Bir  *trace* , bir uygulamanın mantığını değerlendirmek için dolaylı bir tekniktir; çünkü işin yönlendirilmesi sıklıkla tek tek bileşenlerin mantığının veya *service mesh* ya da *bus* gibi yönlendirme araçlarının sonucudur.

---

# 🔎 Sütunları Detaylı Anlamak

## 🧾 Loglar: Detay, Sıralı Kayıt ve Geriye Dönük İnceleme

Loglar çoğu zaman bir uygulamanın istek işleme (request processing) aşamalarına dair ayrıntılı detaylar içerir. Tekil olaylar veya işlemler hakkında ayrıntılı bilgi yakalar; ne olduğuna ilişkin sıralı bir kayıt sunar.

Loglardaki istisnalar (exceptions), bir uygulamadaki problemlere dair göstergeler sağlayabilir. Loglardaki hataları ve istisnaları izlemek, bir gözlemlenebilirlik çözümünün ayrılmaz parçasıdır. Logları ayrıştırmak (parsing), uygulama performansı hakkında da içgörü sağlayabilir.

### ✅ Logların Avantajları

Loglar üretmesi son derece kolay bir formattır; genellikle bir *timestamp* ve bir *payload* içerir. Uygulama geliştiricileri tarafından açık bir entegrasyon gerektirmez; bir *print statement* eklemek dışında.

Loglar çoğu zaman düz metin (plain text) olarak üretilir ve insan tarafından okunabilir. Tek tek uygulamalar veya bileşenler tarafından kaydedilen ayrıntılı (granular) bilgiler, destek olaylarının geriye dönük olarak yeniden oynatılmasına (retrospective replay) olanak tanır.

---

## 📊 Metrikler: Sayısal Ölçüm, Toplulaştırılmış Görünüm

İkinci sütun olan  *metrikler* , belirli bir sistem bileşeninin sağlığını gösteren, eşlik eden özniteliklere (attributes) sahip sayısal ölçümlerdir.

Metrikler; yanıt süreleri (response times) veya hata oranları (error rates) gibi toplulaştırılmış veriler sunarak sistem performansına dair üst seviye bir görünüm sağlar. CPU, bellek ve *disutilization* gibi sistem sağlığı göstergeleri çok belirgin olduğundan metrik toplama çoğu zaman sezgiseldir. Bu nedenle hangi metriklerin sürekli toplanacağına ve nasıl analiz edileceğine karar vermek büyük özen gerektirir.

### ✅ Metriklerin Avantajları

Metrikler oldukça niceldir (highly quantitative) ve alarm eşikleriyle (alerting thresholds) ilişkilendirmesi çoğu zaman sezgiseldir. Metrikler hafiftir (lightweight) ve depolaması ile geri çağırması ucuzdur.

Metrikler zaman içindeki trendleri takip etmekte ve bunları anlamakta çok iyidir. Ayrıca sistemlerin veya servislerin nasıl değiştiğini anlamada da etkilidir.

---

## 🧵 İzler: Uçtan Uca Akış, Gecikme Dağılımı ve Darboğaz Bulma

İzleme (tracing) görece yeni bir kavramdır. Bir trace üretmek için birden çok bileşenden gelen veriler bir araya getirilir (stitched together). Dağıtık bir sistemde tek bir isteğin uçtan uca iş akışını gösterir.

Tracing, uçtan uca gecikmeyi (end-to-end latency) parçalara ayırmaya ve bunu farklı katmanlara veya bileşenlere atfetmeye yardımcı olur; böylece darboğazların belirlenmesini sağlar.

### ✅ Tracing’in Avantajları

Serviste bir problem olduğundan eminseniz, izler problemin hangi bileşen veya adımda meydana geldiğini belirlemek için mükemmeldir.

İzler, isteklerin ve yanıtların akışına ilişkin ayrıntılı bir kayıt sunarak dağıtık bir sistemdeki sorunları ayıklayabilir (debug). Tracing; ele alınan belirli istek veya bu isteği yapan kullanıcı gibi sistem davranışına dair bağlama özgü (context specific) ayrıntılar sunabilir.

---

# 🧩 Sonuç: Üç Sütun ile Bütünsel Görünüm

Sonuç olarak gözlemlenebilirliğin üç sütunu olan  *loglar* , *metrikler* ve  *tracing* , ekiplerin sistem davranışını bütüncül biçimde anlamasını, karmaşık sorunları teşhis etmesini ve etkili problem çözmeyi yönlendirmesini sağlar.

Bu videoda, gözlemlenebilirliğin üç temel sütununun  *loglar* , *metrikler* ve *izler* olduğunu öğrendiniz. Loglar, tekil olaylar veya işlemler hakkında ayrıntılı bilgi yakalayarak ne olduğuna dair kronolojik bir kayıt sunar. Üretmesi kolaydır ve uygulama geliştiricileri tarafından açık bir entegrasyon gerektirmez.

Metrikler, belirli bir sistem bileşeninin sağlığını gösteren, eşlik eden özniteliklere sahip sayısal ölçümlerdir. Oldukça niceldir, depolaması ve geri çağırması ucuzdur ve zaman içindeki trendleri takip etmekte mükemmeldir.

İzler, bir iş öğesini (örneğin bir transaction’ı) takip etmek için oluşturulan bilgi yollarının veya iş akışlarının kayıtlarıdır. Bir problemin meydana geldiği bileşen veya adımları belirlemek için idealdir ve tüm sistemin davranışını anlamanıza olanak tanır.
