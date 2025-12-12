# 🧩 Distributed Logging and Tracing

Distributed Logging and Tracing’e hoş geldiniz. Bu videoyu izledikten sonra, *dağıtık loglama* ve *izleme (tracing)* tekniklerini tanımlayabilecek ve *dağıtık loglamayı uygulama adımlarını* listeleyebileceksiniz.

Günümüzün hızlı tempolu ve birbirine bağlı yazılım geliştirme dünyasında, dağıtık sistemlerin sorunsuz çalışmasını sağlamak önemlidir. Uygulamaların karmaşıklığı arttıkça, farklı bileşenlerin nasıl etkileşime girdiğini anlamak, sorunları tespit etmek ve performansı optimize etmek de zorlaşır.

Dağıtık bir ortamda ya da monolitik bir ortamda, bir şeyler ters gittiğinde hata ayıklama için uygulama logları çok kritiktir.

---

## 🗂️ Dağıtık Loglama Nedir?

Önce *dağıtık loglamanın* ne olduğunu anlayalım.

Dağıtık loglama, farklı düğümler veya sunucular üzerindeki birden fazla kaynaktan log verisini toplamak ve depolamak için bilişim sistemlerinde kullanılan bir tekniktir.

Bu, sistem performansının merkezi olarak izlenmesini ve analiz edilmesini sağlar; ayrıca hata ayıklamayı ve sorun gidermeyi kolaylaştırır. Logları analiz ederek bir sorunun kök nedenini belirleyebilir ve buna göre düzeltebilirsiniz.

Dağıtık bir loglama sisteminde log verisi genellikle merkezi bir log sunucusuna veya hizmetine gönderilir; bu merkez, veriyi kolay arama ve analiz için birleştirir ve indeksler. Bu, sorunlar ya da hatalar birden çok düğüme veya sunucuya dağılmış olsa bile, tüm sistem genelinde tespit edilmesine yardımcı olabilir.

---

## 🧵 Dağıtık İzleme Nedir?

Diğer yandan, *dağıtık izleme (distributed tracing)* özellikle birçok *mikroservisten* oluşan uygulamaları profillemek ve izlemek için kullanılan bir yöntemdir.

Geliştiricilerin, uygulamadaki farklı servisler boyunca ilerleyen istekleri takip etmesine olanak tanır; performans darboğazlarını ve hataları belirlemeye yardımcı olur. İzleme ayrıca servis bağımlılıklarını izlemek ve bir sistemin tüm parçalarının doğru çalıştığından emin olmak için de kullanılabilir.

Farklı servisler tarafından istek yolu boyunca üretilen tüm logları ve metrikleri ilişkilendirerek, dağıtık izleme tüm sistem üzerinde uçtan uca görünürlük sağlar. Bu, çok sayıda hareketli parçaya sahip karmaşık uygulamalarda sorun giderme sırasında çok değerli olabilir.

---

## 🧠 Özet: Loglama ve İzleme Arasındaki Fark

Özetlemek gerekirse, hem dağıtık loglama hem de izleme, karmaşık dağıtık sistemleri anlamak ve sorun gidermek için önemli uygulamalardır; ancak farklı amaçlara hizmet ederler.

 *Dağıtık loglama* , sistemle ilgili genel sorunları belirlemeye yardımcı olurken, *izleme* o sistem içindeki tekil istekleri takip eder.

---

## 🔎 Dağıtık İzlemede Temel Kavramlar

Şimdi, dağıtık izlemeye ilişkin bazı temel kavramları inceleyelim.

### 🧵 Trace

Bir  *trace* , bir dizi  *span* ’den oluşur;  *span* ’ler, tek bir mantıksal isteği veya iş akışını temsil eden, zamanlanmış tekil olaylardır.

### ⏱️ Span

Bir  *span* , bir trace içindeki tek bir işlemi temsil eder.

Bir başlangıç ve bitiş zamanına sahiptir ve şu gibi meta verileri içerebilir:

* işlemi gerçekleştiren servisin adı
* işlem için bir ID
* ek bağlam sağlayan etiketler ( *tags* )

### 🆔 Trace ID

 *Trace ID* , bir trace’in tamamı için benzersiz tanımlayıcıdır. Aynı trace’e ait tüm span’ler aynı  *trace ID* ’ye sahiptir.

### 🌳 Parent-Child Relationship

Span’ler birbirleriyle ilişkilere sahip olabilir.

Bir span, işleminin bir parçası olarak başka bir span’i çağırdığında, çağıran span *parent (ebeveyn)* olur ve çağrılan span *child (çocuk)* olur.

### 🔁 Contexts Propagation

 *Contexts propagation* , bir trace’e ilişkin bilginin farklı servisler ve sistemler arasında nasıl aktarıldığıdır.

Bu, dağıtık bir sistemin tüm parçalarının tek bir trace’e katkıda bulunmasını sağlar.

### 🛠️ Instrumentation

 *Instrumentation* , trace ve span üretmek için uygulamalara veya servislere kod eklenmesidir.

Instrumentation, geliştiricilerin açıkça kod eklemesini gerektirip gerektirmemesine bağlı olarak *manuel* veya *otomatik* olabilir; otomatik yaklaşım genellikle bunu otomatikleştiren kütüphanelere veya framework’lere dayanır.

---

## 🧾 Dağıtık Loglamaya Geçiş

Dağıtık izleme ile ilgili önemli kavramları öğrendiğinize göre, şimdi dağıtık loglamaya geçeceğiz.

Dağıtık loglama, birden çok kaynaktan logları toplayıp bir araya getirmenizi sağlar; bu da dağıtık bir sistem genelinde sorunları analiz etmeyi ve gidermeyi kolaylaştırır.

---

## ✅ Dağıtık Loglamayı Uygulama Adımları

Şimdi, dağıtık loglamayı uygulama adımlarını konuşalım.

### 1) 🧰 Bir Loglama Framework’ü Seçin

Apache log for J2, log back ve Fluent D gibi dağıtık loglamayı destekleyen çeşitli loglama framework’leri vardır; ihtiyaçlarınıza uygun olanı seçin.

### 2) ⚙️ Logları Merkezi Bir Konuma Gönderecek Şekilde Yapılandırın

Uygulama kodunuzda logları, log olaylarını merkezi bir konuma gönderecek şekilde yapılandırın.

Bu amaçla TCP veya UDP protokollerini kullanabilirsiniz. Log, aşağıdaki gibi ilgili bilgileri içermelidir:

* zaman damgaları ( *timestamps* )
* önem dereceleri ( *severity levels* )
* diğer bağlamsal veriler

### 3) 🗄️ Merkezi Bir Log Sunucusu Kurun

Tüm logların toplanacağı ve depolanacağı merkezi bir log sunucusu kurun.

Bu, Elastic Search, gray log veya Kafka gibi açık kaynak araçlar kullanılarak yapılabilir.

### 4) 🧹 Log Saklama Politikalarını Tanımlayın

Logları ne kadar süre saklamak istediğinizi tanımlayın ve eski logları arşivleme ve temizleme ( *purging* ) için bir politika oluşturun.

### 5) 📈 Logları İzleyin

Her şey kurulduktan sonra, uygulamanızdaki herhangi bir sorunu veya anomaliyi tespit etmek için loglarınızı düzenli olarak izleyin.

---

## 🧾 Video Özeti

Bu videoda, dağıtık loglamanın, farklı düğümler veya sunucular üzerindeki birden çok kaynaktan loglanmış veriyi toplamak ve depolamak için bilişim sistemlerinde kullanılan bir teknik olduğunu öğrendiniz.

Dağıtık izleme ise, dağıtık bir sistem boyunca hareket eden tek bir isteği veya işlemi izleme uygulamasıdır.

Ayrıca dağıtık loglamayı uygulama adımlarını ve dağıtık izlemeye ait şu önemli kavramları öğrendiniz:  *trace* ,  *span* ,  *trace ID* ,  *parent-child relation* , *contexts propagation* ve  *instrumentation* .
