## 🎙️ Uzman Görüşleri: Node.js’te Anonim Callback Fonksiyonları Kullanımı

Node.js’te anonim callback fonksiyonlarını kullanma: Uzman Görüşleri’ne hoş geldiniz. Bu videoda, birkaç uygulama geliştirme profesyonelinin Node.js’te anonim callback fonksiyonlarını kullanmayı bilmenin ne zaman faydalı olduğunu ve geliştirdikleri çözümlerde nasıl kilit rol oynadığını tartıştuklarını dinleyeceğiz.

Node.js’te uygulamanızın dışına bir istek yapmanızı gerektiren her şeyde (büyük olasılıkla yapacaksınız), callback’lerin nasıl çalıştığını anlamak çok önemlidir.

---

## 🌡️ Örnek Senaryo: Hava Durumu API’sine İstek Atmak

Anonim callback dediğimizde, callback’lerin anonim olması gerekmez. Hatta çoğu zaman isimli fonksiyonlar yazar ve callback’e ihtiyaç duyan fonksiyonlara argüman olarak bunları geçiririm. Bir örnek vereyim.

Diyelim ki ana sayfada sıcaklığı gösteren bir web sitesi geliştiriyorsunuz.

Sıcaklığı almak için büyük olasılıkla başka bir web sitesini, muhtemelen JSON girdi kabul eden ve JSON çıktı döndüren başka bir web servisi çağırıyorsunuz.

Kullanıcı web sitenize geldiğinde yukarı aşağı kaydırıyor. Eğer bunu bloklar ve hava durumu API’sine isteği yaparsanız, kullanıcı yukarı aşağı bile kaydıramaz.

Tarayıcıda tek seferde bir şey yapılır. Node.js tek iş parçacıklıdır ( *single-threaded* ), dolayısıyla bu isteği yaparken her şey bloklanır.

Bunu düşünürseniz, hava durumu API’si herhangi bir nedenle yanıt vermiyorsa; belki kimlik bilgileriniz yanlıştır, belki sunucu çökmüştür; o zaman kullanıcılarınız beklemek zorunda kalır.

Bu durumda callback fonksiyonları kullanışlı hale gelir.

Yaptığınız şey, hava durumu API’sine isteği gönderirsiniz ve işinize devam edersiniz. Yanıt geldiğinde, o yanıtı ele alabilir ve bilgiyi kullanıcıya gösterebilirsiniz.

---

## 🧠 Callback’leri Anlamak ve JavaScript Temelleri

Callback’leri anlamak JavaScript’te ustalaşmanın (a) anahtarıdır.

Fonksiyonlar JavaScript’te birinci sınıf ( *first class* ) nesnelerdir ve bu nedenle başka fonksiyonlara parametre olarak geçirilebilirler.

Callback fonksiyonu, özellikle callback desenini takip eder ve bir fonksiyonun başka bir fonksiyona parametre olarak geçirilmesini içerir; dıştaki fonksiyon çalışmasını tamamladıktan sonra callback fonksiyonu çağrılır.

Callback fonksiyonu bir  *closure* ’dır; callback fonksiyonu, onu kapsayan fonksiyonun kapsamındaki ( *scope* ) değişkenlere erişebilir.

Callback fonksiyonları anonim veya isimli olabilir; burada anonim callback fonksiyonlarından bahsediyoruz.

---

## 🧾 Anonim Callback Ne Zaman Daha İyi?

Anonim fonksiyonlar bazen daha okunabilirdir ve callback fonksiyonunun yeniden kullanılmasının amaçlanmadığı durumlarda iyi bir çözümdür.

Diğer durumlarda, Async.js gibi bir yardımcı modül asenkron JavaScript ile başa çıkmaya yardımcı olabilir.

Anonim callback fonksiyonları JavaScript’te harikadır. Kodunuzu temiz tutmak ve “anında” bir fonksiyon tanımlamak için çok kullanışlıdır.

---

## ✉️ Mesajlaşma ve “Anında” İşleme

Mesajlaşmayla uğraşırken bunları çok yoğun kullandım.

Fikir şu: Mesaj gönderiyorum ve mesaj alıyorum, bu mesajları işlemek istiyorum.

Her seferinde nasıl işleyeceğim için mutlaka tam bir fonksiyon tanımlamak istemiyorum.

Sadece şunu söylemek istiyorum: bu mesajı aldığımda basit bir şey yapacağım.

Bu yüzden çoğu zaman, bir mesaj alan, işleyen, bir şey yapan ve sonra bir daha asla düşünmek zorunda kalmadığım çok basit bir anonim callback fonksiyonu oluşturmak hem çok kolay hem de çok faydalı.

---

## 🛣️ Web Geliştirme: Route Tanımlarken Callback Kullanımı

Node.js’i web geliştirme için kullanmayı planlıyorsanız, callback fonksiyonları kavramı kavramanız gereken ilk şeylerden biridir.

Web sunucunuzda route’ları tanımlarken, size `request` ve `response` nesneleri sağlayan bir kütüphaneye güvenirsiniz.

Bunlar callback fonksiyonunuza argüman olarak verilir; callback fonksiyonunuz da isteği okur ve yanıtı değiştirerek istemcinin istenen sonucu almasını sağlar.

Burada callback fonksiyonlarınız için isimli fonksiyonlar kullanmak mümkün olsa da, anonim fonksiyonlar çoğunlukla tercih edilir; çünkü her route’un mantığı benzersizdir ve başka yerde tekrar edilmez.

Bu yüzden anonim fonksiyonlar kullanmak kodunuzu temiz ve okunabilir tutar.

---

## 🧱 Kapsamlı Kod Bloğu ve Arrow Syntax ile Pipeline Yazımı

Anonim callback fonksiyonları, daha sonra tekrar kullanabileceğiniz kapsamlı ( *scoped* ) bir kod bloğu yazmanıza olanak tanır.

Anonim fonksiyonlar, *arrow syntax* ile birleştiğinde, diziler ( *arrays* ) içindeki verileri manipüle etmek için JavaScript’te açık ve kısa pipeline’lar yazmamızı sağlar.
