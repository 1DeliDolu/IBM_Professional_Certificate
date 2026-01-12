
# 🔐 ConfigMaps ve Secrets

## 🎯 Öğrenme Hedefleri

Config Maps ve Secrets bölümüne hoş geldiniz.

Bu videoyu izledikten sonra şunları yapabileceksiniz:

* Önemli *config map* özelliklerini tanımlamak
* *Config map* yeteneklerini açıklamak
* Bir *config map* oluşturmanın üç yolunu açıklamak
* Bir *secret* oluşturmanın üç yolunu açıklamak

---

## ⚙️ Yapılandırma Değişkenlerini Ayırma

Yazılım geliştiricileri olarak benimsenmesi iyi bir uygulama, yapılandırma değişkenlerini uygulama koduna *hard-code* etmemekten; yapılandırma değişkenlerini ayrı tutmaktan geçer. Böylece yapılandırma ayarlarındaki herhangi bir değişiklik için kod değişikliği yapmanız gerekmez.

---

## 🧱 Config Map Nedir?

Bir  *config map* , gizli olmayan veriyi anahtar–değer çiftleri hâlinde saklayan bir API nesnesidir ve gizlilik veya şifreleme sağlamadıkları için hassas olmayan bilgiler için tasarlanmıştır.

Buna ek olarak bir  *config map* , yapılandırma verisini  *pod* ’lara ve  *deployment* ’lara sağlar; böylece yapılandırma verisi uygulama kodunun içine *hard-code* edilmemiş olur.

Config map içinde saklanan veriler bir megabaytı aşamaz. Daha büyük miktarda veri için bir *volume* bağlamayı veya ayrı bir veritabanı ya da dosya servisi kullanmayı düşünün.

Bir *config map* isteğe bağlı `data` ve `binary data` alanlarına sahiptir ve bu durumda şablonda `spec` alanı yoktur ve config adının geçerli bir DNS alt alan adı olması gerekir.

---

## 🔁 Config Map Yeniden Kullanımı ve Tüketimi

Bir  *config map* , birden fazla *deployment* için yeniden kullanılabilir; böylece ortam,  *deployment* ’ların kendilerinden ayrıştırılmış olur.

Bir  *config map* ’i şu yollarla oluşturabilirsiniz:

* String sabitleri ( *string literals* ) kullanarak
* Mevcut bir *properties* veya *key equals value* (anahtar eşittir değer) dosyası kullanarak
* Bir *config map* YAML tanımlayıcı dosyası sağlayarak

İlk ve ikinci yöntemi, bu tür bir YAML dosyası oluşturmanıza yardımcı olması için kullanabilirsiniz.

*Deployment* veya  *pod* ’lar bir  *config map* ’i, `config map key ref` özniteliğine sahip ortam değişkenlerini ( *environment variables* ) kullanarak ya da *volumes* eklentisini kullanıp bir dosyayı bağlayarak tüketir.

Kubernetes,  *config map* ’i *pod* veya  *deployment* ’a, *pod* veya  *deployment* ’ı çalıştırmadan hemen önce uygular.

Ortam değişkenini doğrudan YAML dosyası içinde kullanırsınız. `message` değişkeni, JavaScript dosyasında `process.env.message` olarak kullanılır.

---

## 📝 Config Map Mesajını Descriptor Üzerinden Sağlama

Bu geliştirme tanımlayıcısını  *deployment* ’ımıza uyguladığımızda, uygulama `"hello from the config file"` şeklindeki string’i görüntüler.

Sonuç mükemmeldir, ancak mesaj descriptor dosyasında *hard-code* edilmiştir. Bu durumu bir *config map* kullanarak değiştirelim.

Bir *config map* sağlamanın en basit yolu, *config map* komutunun ortasında bir anahtar–değer çifti sağlamaktır.

Bu ilk adımdan sonra, ikinci adım olarak,  *deployment* ’ımıza yeni `message` değişkeninden haberdar olmasını söylemek ve alınacağı konumu belirtmek gerekir. Bunu, gösterildiği gibi *deployment* descriptor’ına `environment` bölümünü ekleyerek ve birinci adımda oluşturulan  *config map* ’i işaret etmek için `value from` özniteliğini kullanarak yaparsınız.

Bu durumda,  *deployment* , `myconfig` adlı *config map* içinde `message` adlı bir anahtar arayacaktır.

---

## 📄 Key=Value Dosyasıyla Config Map Oluşturma

`message` değişkenini  *config map* ’e eklemenin bir başka yolu, tüm ortam değişkenlerini `key equals value` formatında içeren bir dosya kullanmaktır. Böyle bir dosya, komut satırında bu değişkenleri tek tek listelemek yerine çok sayıda değişken eklemek için kullanışlıdır.

Burada yalnızca bir `message` anahtarı ve `"hello from the my.properties file"` değerine sahip bir dosya bulunmaktadır.

Artık  *config map* ’i `from file` bayrağını kullanarak oluşturabilirsiniz. *Deployment* descriptor bölümünde anahtarın `my.properties` olduğuna dikkat edin.

 *Config map* ’i `server.js` dosyasında kullanmak için ona `process.env.message` olarak başvurun.

YAML çıktısını almak için `describe` komutunu kullanın, ardından `environment` bölümünü görüntüleyin.

---

## 📂 Dizinlerden ve YAML Dosyalarından Config Map Yükleme

`from file` bayrağına bir dizin belirtirseniz, tüm dizin  *config map* ’e yüklenir.

Ayrıca, `from file equals key equals file name` formatını kullanarak bir anahtarla belirli bir dosyayı da yükleyebilirsiniz.

Son olarak, *config map* tanımlayıcısına sahip bir YAML dosyası kullanabilir ve bu dosyayı uygulayabilirsiniz. Bizim durumumuzda, `kubectl` çıktısını, *config map* almak için, `my-config.yaml` adlı bir YAML dosyası olarak kaydettik.

İlk komut, başlangıçta herhangi bir *config map* olmadığını gösterir.

Burada `config map.yaml` dosyasını oluşturuyorsunuz. Şimdi YAML dosyasını kümenize uygulayacaksınız; bu da  *config map* ’i oluşturur.

*Config map* dosyası açıklamasındaki mesaja dikkat edin. YAML dosyasını kullanmak, size diğer yöntemlerle aynı sonuçları verecektir.

---

## 🕵️ Secrets ile Çalışmak

Şimdi, bir *secret* ile çalışmak, bir *config map* ile çalışmaya benzer.

İlk olarak, bir  *secret* ’ı bir string sabit ( *string literal* ) kullanarak oluşturun. Sonraki adımda, `get` komutu,  *secret* ’ın oluşturulduğunu doğrular.

Son olarak,  *secret* ’ımızın gerçekten bir *secret* olduğunu kanıtlamak için `describe` komutunu kullanın ve ekranda herhangi bir  *secret* ’ın düz metin olarak yazılmadığını kontrol edin.

 *Secret* ’ı YAML formatında yazdırabilirsiniz ve değerin tamamen kodlanmış ( *encoded* ) olduğunu görürsünüz.

---

## 🔑 Secret’ı Ortam Değişkeni Olarak Kullanma

 *Secret* ’ı kullanmak için, gösterildiği gibi *deployment* descriptor’ına başka bir ortam değişkeni ekleyin ve ardından uygulama anahtarını `process.env.API_CREDS` olarak uygulamaya başvurarak kullanın.

Ekran görüntüsü,  *secret* ’ı `node.js` dosyasındaki diğer ortam değişkenleriyle birlikte gösterir.

---

## 📦 Secret’ı Volume Mount ile Kullanma

Uygulamanızda  *secret key* ’i kullanmanın bir başka yolu da  *volume mount* ’lar kullanmaktır.

Daha önce yaptığınız gibi aynı  *secret* ’ı oluşturun. Descriptor YAML dosyasında, *secret* için bir *volume* ve buna karşılık gelen bir *volume mount* kullanın.

Descriptor dosyasındaki her bir konteynerin kendi  *volume mount* ’u vardır, ancak aynı  *volume* ’u paylaşırlar.

`api-creds`  *secret* ’ı, `etc/API` yolunda bir dosya olarak bağlanır ve uygulama dosyayı okuyup işleyerek  *secret* ’ı çıkartır.

---

## ✅ Özet

Bu videoda, uygulamanıza değişkenler sağlamak için bir *config map* kullanabileceğinizi öğrendiniz.

Bir  *config map* ’i şu yollarla oluşturabilirsiniz:

* Bir string sabit ( *string literal* ) kullanarak
* Bir *properties* dosyası kullanarak
* YAML kullanarak

Uygulamanıza hassas bilgiler sağlamak için bir *secret* kullanabilirsiniz.

Bir  *secret* ’ı ise şu yollarla oluşturabilirsiniz:

* Bir string sabit ( *string literal* ) kullanarak
* Ortam değişkenlerini ( *environment variables* ) kullanarak
* *Volume mount* ’lar kullanarak
