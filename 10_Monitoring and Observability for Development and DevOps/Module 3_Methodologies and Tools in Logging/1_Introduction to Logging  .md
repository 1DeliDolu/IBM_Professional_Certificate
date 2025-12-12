# 🧾 Logging’e Giriş

Logging’e Giriş’e hoş geldiniz! Bu videoyu izledikten sonra şunları yapabileceksiniz: Uygulama logging’i tanımlamak, Hangi bilgi ve verilerin loglanacağını nasıl belirleyeceğinizi açıklamak ve Uygulama logging’inin neden önemli olduğunu tanımlamak.

Logging, bir uygulamanın etkinliklerinin kaydedilmiş bir günlüğünü sağlayan, uygulamadan gelen bir dizi mesajdır. Log mesajları, bir uygulamayı hata ayıklarken geliştiriciler ve üretimde uygulamaları yöneten sistem yöneticileri için önemli bilgiler sağlar.

Bir uygulama logu, bir yazılım uygulaması içinde gerçekleşmiş olaylara ilişkin bilgiler içerir. Bu olaylar uygulama tarafından loglanır ve kaydedilir. Hataları, bilgilendirici olayları ve uyarıları içerebilir.

---

## ☁️ Bulut-Native Yaklaşım ve Log Akışları

Geçmişte, uygulama logları dosyalara gönderilirdi; ancak cloud-native uygulamalar logları olay akışları olarak ele alır ve `stdout`’a log yazar; böylece veri toplayıcılar tarafından kolayca işlenebilirler.

Bir uygulama normalde, çeşitli türde olayları bir uygulama günlüğüne kaydetmek için kod içerir. Log, mesaj akışı sorunlarını ve uygulama problemlerini ortaya çıkarabilir. Ayrıca gerçekleşmiş kullanıcı ve sistem eylemlerine ilişkin bilgi de içerebilir.

Loglanan olaylar genellikle aşağıdakilerle ilgili mesajları ve uyarıları içerebilir:

* Uygulama mesajları
* İşlem (transaction) akışı olayları
* Düşük disk alanı
* Tamamlanan işlemler
* Uygulamanın başlamasını engelleyen hata olayları
* Güvenlik olaylarını göstermek için başarı denetimleri (audit) (ör. başarılı oturum açmalar)
* Başarısız olayları göstermek için başarısızlık denetimleri (ör. oturum açma hataları)

Hangi bilginin toplanması gerektiğini ve bunun nasıl kullanılacağını belirlemek, logging’in önemli bir parçasıdır.

---

## 🧩 Log Tasarımı: Ne, Nasıl ve Ne Zaman?

Uygulamalar gibi loglar da tasarlanmalı, uygulanmalı ve test edilmelidir; çünkü uygulama geliştiricileri uygulama bilgisi ve verisini neyi, nasıl ve ne zaman loglayacaklarını tanımlamalıdır.

Ardından geliştiriciler, loglardan anlamlı veriyi nasıl çıkaracaklarını belirlemelidir.

---

## 📨 Ne Loglanmalı: Mesajlar ve İstek-Yaşam Döngüsü

Ne loglanacağını belirlerken aşağıdakileri göz önünde bulundurmalısınız:

Gelen ve giden mesajların her ikisi de şu bilgilerle kaydedilmelidir: uygulama performans göstergesi (ya da API) endpoint URL’leri, istek parametreleri, istek kaynağı ve aracı IP’ler, istek header’ları, kimlik doğrulama bilgileri, istek ve yanıt gövdeleri, iş bağlamı, zaman damgaları ve dahili işleme adımları.

Bir servis veya fonksiyon çağrıldığında, bağlamını daha düşük bir log seviyesinde çoğunlukla hata ayıklama amaçları için loglamak iyi bir pratiktir (`TRACE` veya `DEBUG` kullanın). Bu loglara sahip olmak, iş mantığıyla ilgili sorunları araştırmaya yardımcı olur.

---

## 🧭 İş Bağlamı: Kullanıcı Yolculukları ve İçgörüler

Her uygulamanın kendine özgü iş durumları ve kullanıcı yolculukları vardır ve bunlar sistemdeki alan uzmanları için birçok içgörü ortaya çıkarır.

Örneğin, belirli bir işlemin çok uzun sürüp sürmediği veya son kullanıcıların sürekli belirli bir işlevde takılıp kalıp kalmadığı, kullanıcı deneyimi açısından çok kritik bilgi parçalarıdır.

Diğer iş ile ilgili bilgiler, örneğin işlem hacimleri ve aktif kullanıcılar ile bunların aşamaları, iş içgörüleri çıkarmak için önemlidir ve hatta iş zekâsı amaçları için de kullanılabilir.

---

## 🔐 Güvenlik ve Uyumluluk Logları

Güvenlik ve uyumluluk için, birçok kurumsal uygulamada veriyle ilgili işlemler için ayrı bir log tutmak zorunludur. Bu loglar; erişim ID’leri, kullanılan kesin servis instance’ları ve rol ayrıcalıkları, zaman damgaları, veri katmanı sorguları ve değiştirilen veri kümesinin hem önceki hem de yeni durumlarının anlık görüntüleri gibi önemli bilgileri içermelidir.

---

## 🖥️ Sistem Olayları ve Operasyonel Telemetri

Sistem olayları şu davranış olayları hakkında bilgi yakalamalıdır: başlatmalar, durdurmalar, yeniden başlatmalar, güvenlik olayları; geçiş modları (cold, warm, hot); servisler arası iletişim (handshake’ler, bağlantı kurma durumları — `connect`, `disconnect`, `reconnect`, `retry` olayları); servis instance ID’leri; aktif olarak hizmet veren API’ler; aktif olarak dinlenen IP ve port aralıkları; yüklenen konfigürasyonlar (ilk yükleme ve dinamik güncellemeler); genel servis sağlığı ve sistemin davranışını anlamaya yardımcı olan her şey.

Performans istatistikleri, örneğin servislerde anormallikler veya ani beklenmedik bozulmalar (çoğunlukla ele alınmamış hatalar ve bozulmuş veri nedeniyle), herhangi bir zamanda meydana gelebilir. Bunları tanımlamak için, genel sistem sağlığı ve performansına ilişkin istatistikleri yayınlamak her zaman önerilir.

---

## 🎯 Neden Önemli: Diagnostik ve Denetim

Uygulama loglarının genel stratejinizde önemli rol oynamasının iki ana nedeni vardır: diagnostik ve denetim (auditing).

Uygulama loglarını diagnostik için, belirli bilgileri izleyip ilişkilendirerek ve bunu yazılımınız üzerinde analitik yapmak için kullanabilirsiniz. İzlemek ve analiz etmek için faydalı olabilecek bazı bilgi örnekleri: müşteri işlemleri, güvenlik tehditleri, zaman aşımları ve tüketici davranışı.

Log yönetimi araçları, halihazırda topladığınız bilgilerden değerli içgörüler sağlayabilir. Uygulama logları, sorunları teşhis etmek için de kullanılabilir. Üretim ortamında hataları tanımlamak ve çözmek için uygulama loglarını kullanabilirsiniz. Bu süreç, yazılım geliştirme sırasında düzenli olarak gerçekleşir. Ve bir uygulamanın uzun vadeli optimal performansını sağlamak için kritiktir.

Uygulama loglarının bir diğer önemli nedeni, denetim amaçları için de kullanılabilmeleridir. Bu loglanan mesajlar, uygulamadaki önemli olayları ve yönetim ile finansla ilgili bilgileri içerir. Bu bilgi günlük bazda o kadar fayda sağlamayabilir; ancak iş gereksinimlerini karşılamak için önemlidir.

---

## 🗣️ Eğitmen Notu: “Loglar Ne Diyor?”

Biliyorsunuz, öğrencilerimden biri veya ekibimin bir üyesi buluta yeni bir uygulama deploy ettiğinde ve işler iyi gitmediğinde, benden debug için yardım istiyorlar; sorduğum ilk sorular “loglar ne diyor?” olur.

Onlar da kaçınılmaz olarak geri dönüp loglarda hiçbir şey olmadığını söylediklerinde, onlara şunu söylerim… “O halde uygulamana geri dönme ve aktivitelerini loglamaya başlama zamanı!” Logların, uygulamanın üretimde ne yaptığını anlamanın ilk seviyesidir. Logging’den kısmayın.

---

## ✅ Bu Videoda Öğrendikleriniz

* Uygulama logging’i, uygulamanın etkinliklerinin loglanmış bir kaydını sağlamak için uygulamadan gelen bir dizi mesajdır.
* Bir uygulama logu, bir yazılım uygulaması içinde gerçekleşmiş olaylara ilişkin bilgi içerir.
* Ne loglanacağını belirlerken; bir uygulamanın gelen ve giden mesajlarını, servis ve fonksiyonlarını, iş durumlarını ve kullanıcı yolculuklarını, veri operasyonlarını, sistem olaylarını, performans istatistiklerini ve tehditleri ile güvenlik açıklarını göz önünde bulundurarak belirleyin.
* Uygulama logging’i önemlidir; çünkü izlenen bilgileri ilişkilendirme ve sorunları tanımlama, teşhis etme ve çözme gibi diagnostik amaçlara ilişkin bilgi sağlar ve ayrıca yönetim ve finans verisi sağladığı için denetim amaçları açısından gereklidir.
