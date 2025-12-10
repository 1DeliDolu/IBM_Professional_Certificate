
# 🔗 Service Binding

## 🎯 Service Binding’e Giriş

Service Binding’e hoş geldiniz. Bu videoyu izledikten sonra, service binding’in rollerini ve hedeflerini açıklayabilecek, bir Kubernetes kümesini harici bir servise nasıl bağlayacağınızı anlatabilecek, Kubernetes kümenizdeki  *secret* ’ları almak için kullanılan komutları tanımlayabilecek ve uygulamalarda service binding’in nasıl kullanılacağını açıklayabileceksiniz.

Service binding nedir?

Service binding, uygulamalarımızda REST API’ler, veritabanları ve  *event bus* ’lar da dâhil olmak üzere harici servisleri veya  *backing service* ’leri tüketmek için gereken süreçtir.

Service binding, hassas verileri korurken arka uç servisler için yapılandırmayı ve kimlik bilgilerini yönetir.

---

## 🧩 Service Binding’in Genel Çalışma Prensibi

Buna ek olarak, service binding, servis kimlik bilgilerini size otomatik olarak bir *secret* olarak sunar. Service binding, uygulamayı bir  *deployment* ’a bağlayarak harici servisi tüketir. Ardından uygulama kodu,  *binding* ’deki kimlik bilgilerini kullanır ve ilgili servisi çağırır.

Burada, bir Kubernetes kümesinin harici bir servise bağlanmasını gösteren bir mimari diyagram görebilirsiniz.

Sonraki olarak, servisi uygulamanıza bağlamak için gereken adımları öğrenelim. Bir IBM Cloud Service örneği kullanalım. Service binding, bir IBM Cloud servisi için servis kimlik bilgilerini hızlı bir şekilde oluşturur.

---

## ☁️ IBM Cloud Servisini Kümenize Bağlama

Servis kimlik bilgilerini, IBM’in Public Cloud servis  *endpoint* ’ini kullanarak oluşturur ve ardından bu servis kimlik bilgilerini, kümenizdeki bir Kubernetes  *secret* ’ına kaydeder veya bağlarsınız.

Bir IBM Cloud servisini kümenize şu şekilde bağlarsınız:

Önce, servisin bir örneğini ( *instance* ) sağlarsınız (*provision* edersiniz). Ardından, servisi, Public Cloud servis  *endpoint* ’ini kullanan servis kimlik bilgilerini oluşturmak için kümenize bağlarsınız.

Sonra, kimlik bilgilerini bir Kubernetes  *secret* ’ında saklarsınız. Son olarak, uygulamanızı, Kubernetes  *secret* ’ındaki servis kimlik bilgilerine erişecek şekilde yapılandırırsınız.

IBM Cloud kataloğu, görsel tanımadan doğal dil işlemeye ve *chat bot* oluşturmaya kadar uzanan çeşitli servisler sunar.

---

## 🧠 Örnek Servis: Tone Analyzer

Service binding’i açıklamak için *tone analyzer* servisini kullanıyoruz. Bu servis, verilen bir metindeki tonu algılamak için dilbilimsel analiz kullanır.

Servis, JavaScript’te bir SDK sağlar. Servisi, kimlik bilgilerinin otomatik olarak kullanılabilir olması için  *deployment* ’a bağlarsınız.

Daha sonra kod,  *binding* ’den gelen kimlik bilgilerini kullanır ve *tone analyzer* servisini çağırır.

Artık adımları bildiğinize göre, biraz da koda bakalım. İlk adımda, komut satırı arayüzünü ( *command line interface* ) kullanarak servis örneğini oluşturarak servisin bir örneğini sağlarsınız.

---

## 💻 Servis Örneği ve Service Bind Komutu

Servis örneğini, IBM Cloud web sitesindeki katalogu kullanarak da sağlayabilirsiniz.

İkinci adımda, yeni oluşturulan bu servis örneğini `service bind` komutunu kullanarak kümenize bağlarsınız. IBM Cloud Service Binding, servis kimlik bilgileriyle otomatik olarak bir Kubernetes  *secret* ’ı oluşturur.

Bir servis örneğinin kimlik bilgileri *base64* ile kodlanır ve  *secret* ’ınızın içinde JSON formatında saklanır.

Artık servis kümenize bağlandığına göre, burada 3. adımda *secret* nesnenizi doğrulayabilirsiniz. `Get Secrets` komutu, Kubernetes kümenizdeki tüm  *secret* ’ları gösterir.

Ya da aynı  *secret* ’ları, Kubernetes *dashboard* kullanıcı arayüzünde ve IBM Cloud Kubernetes Service üzerinde de alabilirsiniz.

---

## 🔑 Secret İçindeki Verilere Erişim Yöntemleri

 *Secret* ’ınızdaki verilere erişmek için aşağıdaki seçeneklerden birini seçin.

1. **Secret’ı bir volume olarak bağlamak:**

   *Secret* ’ı, 1. adımda verilen özelliklere ( *specifications* ) göre Pod’unuza bir *volume* olarak bağlayın (*mount* edin). Bu işlem, *Volume Mounts* dizininde saklanan ve `binding` adlı, JSON formatlı bir dosya oluşturur.
   `binding` dosyası, IBM Cloud Service’e erişmek için gereken tüm bilgi ve kimlik bilgilerini içerir.
2. **Ortam değişkenleriyle kullanmak:**

   *Secret* ’a ortam değişkenleri ( *environment variables* ) üzerinden referans verebilirsiniz.
   `binding`, `API key`, `binding.username` ve `binding.password` ortam değişkenleri, önceki adımda oluşturulan Watson Tone Analyzer servis örneğinin API Key kullanıcı adı ve parolasına karşılık gelir.

Gösterilen kod parçası, IBM Cloud Kubernetes Service’e *deploy* edilecek bir Express.js uygulamasında, `binding.API Key`, `binding.username` ve `binding.password` ortam değişkenlerini kullanan örnek bir Node.js uygulamasını göstermektedir.

---

## ✅ Özet: Bu Videodan Ne Öğrendiniz?

Bu videoda, harici bir servisi  *deployment* ’ınıza bağlamanın, servis kimlik bilgilerini kod içinde kullanmanız için otomatik olarak sağladığını öğrendiniz.

Kimlik bilgileri,  *volume mount* ’lar ve  *volume* ’lar kullanılarak tüketilebilen bir *secret* olarak saklanır.

Binding, hassas verileri korurken arka uç servisler için yapılandırmayı ve kimlik bilgilerini yönetir ve uygulamanızı  *secret* ’ta saklanan kimlik bilgilerini kullanacak şekilde yapılandırabilirsiniz; bunu ya  *secret* ’ı Pod’unuza bir *volume* olarak bağlayarak ya da  *secret* ’a ortam değişkenleri üzerinden referans vererek yapabilirsiniz.
