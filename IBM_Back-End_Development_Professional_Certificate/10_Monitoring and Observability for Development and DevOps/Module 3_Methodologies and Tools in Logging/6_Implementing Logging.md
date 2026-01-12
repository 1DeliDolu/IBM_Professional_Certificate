# 🛠️ Loglamayı Uygulama

Loglamayı Uygulamaya hoş geldiniz. Bu videoyu izledikten sonra, uygulama loglarının farklı türlerini açıklayabilecek, loglamanın nasıl uygulanacağını açıklayabilecek, logların nasıl biçimlendirileceğini ve yapılandırılacağını tarif edebilecek ve log ayrıştırma (parsing) kavramını ve adımlarını açıklayabileceksiniz.

Günümüzün hızlı tempolu yazılım geliştirme ortamında, BT ekipleri sağlam uygulamaları verimli şekilde oluşturmak, dağıtmak ve sürdürmek için çabalar. Bu hedefe ulaşmanın temel unsurlarından biri loglamayı uygulamaktır.

Loglama; uygulama gözlemlenebilirliğini artırmada, sorun gidermede ve genel sistem performansında kritik bir rol oynar.

---

## 🧾 Yaygın Uygulama Log Türleri

Uygulama loglarının bazı yaygın türlerini belirleyelim.

 **Olay logları (Event logs)** , giriş denemeleri ve veri değişiklikleri gibi uygulama olaylarını ve kullanıcı eylemlerini kaydeder. Sorun gidermek ve güvenlik ihlallerini tespit etmek için kullanışlıdır.

 **Hata logları (Error logs)** , uygulama veya sistem tarafından üretilen hata mesajlarını kaydeder. İstisnalar,  *stack trace* ’ler ve hata kodları hakkında bilgi içerir; bu da geliştiricilerin sorunları teşhis edip düzeltmesine yardımcı olabilir.

 **Erişim logları (Access logs)** , uygulamaya kimin eriştiğini, ne zaman eriştiğini ve hangi eylemi gerçekleştirdiğini kaydeder. Denetim (auditing) ve kullanıcı etkinliğini izleme için yardımcı olabilir.

 **Performans logları (Performance logs)** , yanıt süreleri, CPU kullanımı, bellek tüketimi ve ağ trafiği gibi uygulamanın performansına ilişkin metrikleri izler. Darboğazları belirlemek ve performansı optimize etmek için kullanışlıdır.

 **Hata ayıklama logları (Debugging logs)** , değişkenler, metot çağrıları ve diğer hata ayıklama verileri hakkında ayrıntılı bilgi içerir. Geliştiriciler tarafından geliştirme sürecinde program akışını izlemek ve hataları belirlemek için kullanılır.

---

## 🧩 Loglama Çerçeveleri ve Ortak Özellikler

Farklı programlama dilleri için çeşitli loglama çerçeveleri mevcuttur. Loglama çerçevelerinin çoğu bazı ortak özellikleri paylaşır.

Loglama çerçeveleri genellikle  **DEBUG** ,  **INFO** , **WARNING** veya **ERROR** gibi birkaç seviyeye sahiptir. Her seviye, log mesajlarının farklı bir önem derecesini belirtir.

 **Log mesajları** , loglamak istediğiniz gerçek mesajı temsil eder ve genellikle bir zaman damgası, önem seviyesi ve olayla ilgili diğer ayrıntıları içerir.

 **Hedefler (Destinations)** , loglarınızın nereye gönderilmesini istediğinizi ifade eder; örneğin konsol çıktısı ya da bir dosya.

---

## 🐍 Python ile Loglamayı Uygulama Örneği

Bu, Python’da yerleşik `logging` modülünü kullanarak loglamayı nasıl uygulayabileceğinizi gösteren bir örnektir.

Bu örnekte `logging` modülünü içe aktarırsınız; loglayıcıyı `example.log` adlı bir dosyaya yazacak şekilde yapılandırırsınız ve log seviyelerini **DEBUG** olarak ayarlarsınız.

Fonksiyonun çalıştırılmasına başladığınızı kaydetmek için `logging.info` metodunu çağırırsınız.

---

## ☕ Java ile Loglamayı Uygulama Örneği

Bu, Java’da loglamayı nasıl uygulayacağınıza bir örnektir.

Java, farklı hedeflere mesaj loglamak için kullanılabilen `java.util.logging` adlı yerleşik bir loglama çerçevesi sağlar.

Önce loglama paketini içe aktarmanız gerekir, ardından benzersiz bir adla bir *logger* nesnesi oluşturmanız gerekir. Bununla, bu *logger* nesnesini mesaj loglamak için kullanabilirsiniz; bu, içeriği **Hello World** olan bilgilendirici bir mesajı loglar.

Ayrıca, seviyesini ayarlayarak ve farklı hedefler için  *handler* ’lar ekleyerek  *logger* ’ı yapılandırabilirsiniz. Örneğin, verilen kod, tüm log mesajlarını konsola yazdıran bir konsol  *handler* ’ı ekler.

---

## 🧱 Logları Biçimlendirme ve Yapılandırma

Uygulamaların etkili hata ayıklaması ve sorun giderimi için doğru log biçimlendirmesi kritik önemdedir.

Logların biçimlendirilmesi için izleyebileceğiniz bazı adımlar vardır:

* Öncelikle, programlama dilinize ve ihtiyaçlarınıza uygun bir loglama kütüphanesi seçin. Örneğin: Java için `log4j`, Python için `logging`, Go için `Logrus`.
* İkinci olarak, kullanmak istediğiniz farklı log seviyelerini tanımlayın; örneğin  **INFO** , **DEBUG** veya  **ERROR** .
* Sonrasında, zaman damgası, log seviyesi, *logger* adı, *thread ID* ve loglanan gerçek mesaj gibi ilgili bilgileri içeren tutarlı bir biçimde log mesajını formatlayın.
* Ardından, logların nereye yazılacağına karar verin; örneğin konsol çıktısı veya dosya çıktısı ve loglama kütüphanenizi buna göre yapılandırın.
* Son olarak, gerekli tüm bilgileri yakaladığından emin olmak için loglama kurulumunuzu kapsamlı şekilde test edin ve ihtiyaç oldukça biçimlendirme ile seviyeleri ayarlayın.

---

## 🧾 Yapılandırılmış Loglama

Yapılandırılmış loglama, zahmetsiz ayrıştırma ( *parsing* ), sorgulama ( *querying* ) ve analitik için standart log formatlarını mümkün kılar.

Yapılandırılmış loglama, geleneksel düz metin loglara göre birçok fayda sağlar; bunlar arasında log verilerini daha kolay sorgulama ve filtreleme, daha verimli depolama ve işleme ve sistem davranışına daha iyi görünürlük yer alır.

*JavaScript Object Notation* ya da  **JSON** , yapılandırılmış loglama için fiili standarttır; ancak uygulama loglarınız için anahtar-değer çiftleri, XML veya başka bir format kullanmayı da düşünebilirsiniz.

Eklenti ( *addon* ) sağlayıcınızın otomatik olarak ayrıştırabildiği desteklenen formatları gözden geçirmeniz gerekir.

---

## 🧠 Yapılandırılmış Logları Uygulama Adımları

Loglarınızın iyi yapılandırılmış olmasını ve uygulamanızın performansı ile davranışı hakkında değerli içgörüler sağlamasını garanti etmek için bazı adımları izlemelisiniz:

* Öncelikle, loglanacak ilgili verileri belirleyin.
* Ardından, JSON veya CSV gibi verilerinizi loglamak için tutarlı bir format tanımlayın.
* Sonra, tanımlanan formatı kullanarak ihtiyaç duyulan yerlerde kod tabanınız boyunca yapılandırılmış log ifadeleri ekleyin.
* Son olarak, yapılandırılmış logları toplamak ve analiz etmek için bir loglama kütüphanesi veya aracı kullanın.

---

## 🧩 Log Ayrıştırma (Parsing) ve Log Yönetim Sistemleri

Bir log yönetim sistemi, loglardan anlamlı bilgileri çıkarmak için önce dosyaları ayrıştırmalıdır.

Log ayrıştırma, log dosyalarını log yönetim sisteminiz için okunabilir bir formata dönüştürür; veri okuma, indeksleme ve depolamayı mümkün kılar. Anahtar-değer bilgisinin filtrelenmesini, analizini ve manipülasyonunu basitleştirir.

Genellikle log ayrıştırıcılar ( *parsers* ) log yönetim yazılımının motoruna gömülüdür. Çoğu log yönetim çözümü, Windows olay logları, JSON, CSV veya W3C gibi yaygın veri türleri için yerleşik ayrıştırıcıya sahiptir.

Ayrıştırıcılar; kaynak, veri yapısı ve dosya uzantılarına göre bu log türlerini tanıyacak şekilde yapılandırılır.

---

## 🧭 Logları Ayrıştırmak için Genel Adımlar

Logları ayrıştırmak için gereken genel adımları ele alalım:

* Öncelikle log dosyalarınızın formatını belirleyin; örneğin CSV, JSON veya düz metin.
* Ardından, log dosyalarında analiziniz için hangi alanların ilgili olduğunu belirleyin.
* Sonra, belirlediğiniz log dosyası formatını ayrıştırmayı destekleyen bir araç veya kütüphane seçin; örneğin CSV dosyaları için Python `csv` modülü.
* Log verisini okumak ve ilgili alanları çıkarmak için kod yazın.
* Son olarak, çıkarılan veriyi analiz için uygun yapılandırılmış bir formatta saklayın; örneğin bir veritabanında.

---

## ✅ Özet

Bu videoda, uygulama loglarının bazı yaygın türlerinin olay logları, hata logları, erişim logları, performans logları ve hata ayıklama logları olduğunu öğrendiniz.

Loglama çerçevelerinin çoğu; seviyeler, log mesajları ve hedefler gibi bazı ortak özellikleri paylaşır.

Uygulamaların etkili hata ayıklaması ve sorun giderimi için doğru log biçimlendirmesi kritiktir.

Yapılandırılmış loglar, zahmetsiz ayrıştırma, sorgulama ve analitik için standart log formatlarını mümkün kılar.

Ve log yönetim sistemlerinin loglardan anlamlı bilgileri çıkarmak için dosyaları ayrıştırması gerekir.

Çoğu log yönetim çözümü yerleşik ayrıştırıcılara sahiptir.
