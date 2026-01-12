# 🗄️ Log Saklama

Log saklamaya hoş geldiniz. Bu videoyu izledikten sonra, log verilerini saklamanın başlıca nedenlerini belirleyebilecek ve logları saklamaya yönelik en iyi uygulamaları tanıyabileceksiniz. Logları izlemek ve analiz etmek, ağın gözlemlenebilirliğini artırarak bulut bilişim ortamında şeffaflık ve görünürlük sağlar. Gözlemlenebilirlik birincil hedef olmasa da, gerçek iş hedeflerini gerçekleştirmek için bir araç olarak görülmelidir. Bu gözlemlenebilirlik, log verilerinin saklanmasıyla elde edilebilir.

Log verilerini saklamanın birçok nedeni vardır. Bu nedenleri inceleyelim.

## ✅ Sistem Güvenilirliğini Artırma

İlk olarak, log verileri sistemlerin güvenilirliğini artırmaya yardımcı olur. Log dosyaları, sistem performansına ilişkin bilgiler içerir; bu da kullanıcı deneyimini iyileştirmek için kapasite artırımı gereksinimini belirlemeye yardımcı olur. Log dosyalarını; yavaş sorguları, işlemleri uzatan hataları veya uygulamanın performansını etkileyen bug’ları tespit etmek için kullanabilirsiniz.

## 🛡️ Güvenlik Duruşunu Koruma

Log verilerini saklamanın bir diğer nedeni, ortamın güvenlik duruşunu korumaktır. Log dosyaları; başarısız oturum açma girişimleri, kimlik doğrulama hataları veya beklenmedik sunucu aşırı yüklenmeleri gibi olayları kaydeder ve bu olaylar analistlere devam eden olası bir siber saldırıyı gösterebilir. Gelişmiş güvenlik izleme araçları, ağ üzerinde bu tür olayları tespit ettiğinde hızlıca uyarılar gönderebilir ve yanıtları otomatikleştirebilir.

## 📊 IT Sistemlerinde Karar Vermeyi İyileştirme

Log verilerini saklamanın bir sonraki nedeni, BT sistemlerinin karar verme süreçlerini iyileştirmektir. Kullanıcının bir uygulamayla olan davranışı log dosyalarında kaydedilir ve saklanır. Bu durum, *kullanıcı davranışı analitiği* olarak bilinen bir araştırma alanına yol açar. Kullanıcı eylemlerini analiz ederek geliştiriciler, kullanıcıların hedeflerine daha hızlı ulaşmasını sağlamak için uygulamayı geliştirebilir; böylece müşteri memnuniyeti artar ve gelir yükselir.

## 🧾 Denetim Amaçları

Saklanan loglar denetim amaçları için de kullanılabilir. Log mesajları, önemli uygulama olaylarını ve yönetim ile finans bilgilerini kapsar. Bunlar günlük faydalar sağlamayabilir; ancak iş gereksinimlerini karşılamak için kritik öneme sahiptir.

## 📈 Zaman İçinde Davranış ve Performans Değişimlerini Görselleştirme

Bir uygulamanın davranışı ve performans değişimlerine zaman içinde içgörü kazanmak için, günler veya haftalar boyunca uzanan log verilerini görselleştirmek gerekir. Bu da örüntülerin ve trendlerin belirlenmesini sağlar.

## ⏳ Log Saklama (Retention) Politikaları ve Uyumluluk

Log saklama politikaları açısından, denetim gereksinimlerine ve ilgili kurallara uyum genellikle log verilerinin uzun süreler boyunca, hatta yıllarca tutulmasını gerektirir. Bu gibi durumlarda, eski logların erken silinmesi ciddi sonuçlara yol açabilir.

## ☁️ Bulutta Log Saklama ve Ölçeklenebilirlik

Logları bulutta saklamak, hızlı erişilebilirlikten ödün vermeden log veri ihtiyacına uygun ölçeklenebilir depolama kapasitesi sağlar. Kapasiteyi veya log verisini artırmak, geri getirme hızını etkilemez. Amazon S3 gibi depolama servisleri, bekleyen veriler için AES-256 şifreleme kullanarak log verilerini bulutta güvenli şekilde saklama imkânı sunar.

## 🧠 Uzun Dönem Saklama ve Retention Stratejisine Dahil Etme

Log toplamak, uzun dönem saklama ve retention kabiliyeti sağlar. Birçok uyumluluk zorunluluğu log saklama ve retention gereksinimlerine sahiptir; bu nedenle bunu log toplama stratejinize dahil etmek kritik önemdedir. Genel olarak, gelecekte gerekebilecek incelemeleri kolaylaştırmak için log verilerinin minimum bir yıl saklanması önerilir.

## 🏢 On-Premises veya Bulutta Yedekleme

Logları saklarken veriyi şirket içi (on-premises) sunuculara veya buluta yedeklemeyi seçebilirsiniz. Bu karar çoğu zaman şirketin dijital dönüşümü ve kaynakların çevrimiçi ortama taşınmasıyla ilişkilidir.

---

# 🧩 Log Retention Politikaları için Analitik Boyutlar

Log retention politikaları için, retention süresinin ne kadar olması gerektiğine dair göreli bir fikir veren analitik boyutları ele alalım.

## 🧱 Kritiklik

İlk olarak *kritiklik* dikkate alınmalıdır. Retention politikaları, sistemin farklı bölümleri için önem derecesine göre değişebilir. Kritik bileşenler daha yüksek güvence için daha uzun retention sürelerine sahip olabilir. Örneğin, küçük değere sahip servislerin logları iki gün içinde silinebilir.

## 🔐 Güvenlik

İkinci boyut *güvenlik*tir. Hassas veya kişisel veri içeren ve yüksek riskli işlem yapan uygulamalar daha uzun bir retention politikasına sahip olmalıdır. Örnekler; kredi kartı yetkilendirmesinden ve kullanıcı kimlik doğrulamasından sorumlu servisleri içerir. Buna karşılık, uygulamayı iyileştirmek için müşteri davranışını takip eden servisler daha uzun bir retention politikasına ihtiyaç duymayabilir.

## 🧪 Sistem Olgunluğu

Bir sonraki boyut, sistemin *olgunluğu*dur. Süregelen özellik geliştirmesi sınırlı olan, iyi yerleşik sistemlerde yeni sorunların ortaya çıkması seyrektir. Bu nedenle, olgun olmayan yazılım sistemlerinde depolama maliyetini azaltmak için kısa bir retention politikası uygun olabilir.

## 🔁 Çalışma Sıklığı

Bir diğer boyut *sıklık*tır. Örneğin ayda bir çalışan uygulamalar, geliştiricilerin birden fazla çalıştırmayı doğrulayarak bir sorunun kaynağını bulmasına yardımcı olmak için daha uzun retention politikalarından faydalanır. Seyrek çalıştırma nedeniyle yapılan debug süreçlerinde, zamanda geriye gidip iz sürmek gerekir.

## 💰 Maliyet Etkinliği

Retention politikasında *maliyet etkinliği* boyutu da dikkate alınmalıdır. Retention politikasına karar vermeden önce projenin maliyet uyumluluğunu değerlendirmelisiniz. Hedeflenen süre için veri üretimini ve depolama maliyetlerini tahmin edin. Güvenliği ve uzun dönem saklamayı önceliklendirmek istenebilir; ancak daha maliyet etkin bir alternatif seçmek de makul olabilir.

## 🧯 Keşif ve Çözüm Süresi

Son olarak, *keşif ve çözüm* boyutunu da dikkate almalısınız. Geliştirme ekibinizin problemleri tespit edip düzeltmesi için ortalama ne kadar süre gerektiğini izlemelisiniz. Log retention politikasının, debug için yeterli alan sağladığından emin olmalısınız.

---

# 🧰 Log Saklamaya Yönelik En İyi Uygulamalar

Log saklamaya ilişkin bazı en iyi uygulamalara bakalım.

* Sorunları hızlıca belirlemek ve teşhis etmek için hangi bilgileri loglamanız gerektiğini belirlemek önemlidir.
* Logları tek bir sistemde merkezileştirmek, özellikle birden fazla sunucu veya uygulamanız varsa yönetimi ve analizi kolaylaştırır.
* İhtiyaçlarınıza bağlı olarak AWS CloudWatch gibi bulut tabanlı bir çözüm veya Elasticsearch gibi self-hosted bir çözüm kullanmak isteyebilirsiniz.
* Logları düzenli olarak döndürmek (rotate etmek), depolama alanının dolmasını ve performans sorunlarına yol açmasını önleyebilir.
* Güvenliği ve gizliliği korumak için yalnızca yetkili personelin loglara erişebilmesini sağlayın.
* Log verilerini düzenli olarak gözden geçirmek, büyük problemlere dönüşmeden önce trendleri veya olası sorunları belirlemeye yardımcı olabilir.
* Bazı organizasyonlar, yasal veya düzenleyici gereklilikler nedeniyle log verilerini belirli bir süre saklamak zorunda olabilir; bu nedenle bu konudaki yükümlülüklerinizi bilmelisiniz.

---

# 🧱 Log Saklama Araçları

Log saklama için birçok araç vardır. Bunlardan birkaçını inceleyelim.

* **Elasticsearch** , logları saklamak ve analiz etmek için kullanılabilen dağıtık bir RESTful arama ve analiz motorudur.
* **Splunk** , web tarzı bir arayüz üzerinden makine tarafından üretilen büyük verileri aramak, izlemek ve analiz etmek için kullanılan bir yazılım platformudur.
* **Graylog** , yapılandırılmış ve yapılandırılmamış log verilerini toplayan, indeksleyen ve analiz eden açık kaynaklı bir log yönetim platformudur.
* **Logstash** , Elastic tarafından geliştirilen; logları toplamak, ayrıştırmak ve daha sonra Elasticsearch veya diğer analiz platformlarıyla kullanılmak üzere saklamak için kullanılan bir araçtır.
* **Fluentd** , loglama altyapısını birleştirmek üzere tasarlanmış açık kaynaklı bir veri toplayıcıdır.
* Son olarak  **Sumo Logic** , kullanıcıların logları gerçek zamanlı olarak içe aktarmasına, analiz etmesine ve görselleştirmesine olanak tanıyan bulut tabanlı bir log yönetim platformudur.

---

# 🧾 Video Özeti

Bu videoda, logları izlemenin ve analiz etmenin ağın gözlemlenebilirliğini artırarak bulut bilişim ortamında şeffaflık ve görünürlük sağladığını öğrendiniz. Log verilerini saklamayı düşünmenin başlıca nedenleri; sistemlerin güvenilirliği, ortamların güvenlik duruşu ve denetimdir. Log verilerini saklamaya yönelik stratejiler; retention süresi, logları bulutta saklama, uzun dönem log saklama ve log verilerini yedeklemeyi içerir.  *Kritiklik* ,  *güvenlik* , *sıklık* ve  *maliyet etkinliği* , retention süresinin ne kadar olması gerektiğine dair göreli bir kavrayış sağlayan analitik boyutlardır. Öne çıkan log saklama araçları ise Elasticsearch, Splunk, Graylog, Fluentd ve Sumo Logic’tir.
