## 🧩 Node.js ve Express ile Back-End Uygulama Geliştirme: Özet

### 🖥️ 1. Sunucu Tarafı JavaScript’e Giriş

Back-end teknolojileri; programlama dilleri, framework’ler ve diğer donanımlar gibi çeşitli sunucu türlerini ve destekleyici altyapıları içerir.

Node.js, JavaScript’in sunucu tarafı bileşenidir. Node.js kullanmak uygulama performansını artırabilir ve express.js, Node.js uygulamaları oluşturmanıza yardımcı olan bir framework’tür.

`require` ifadesi uygulama kodunun herhangi bir yerinden çağrılabilir, dinamik olarak bağlanır ve senkrondur; buna karşılık `import` ifadesi yalnızca bir dosyanın başında çağrılabilir, statik olarak bağlanır ve asenkrondur.

İstemci tarafı JavaScript, front-end kullanıcı arayüzü öğelerini işlemek için kullanılır; sunucu tarafı JavaScript ise farklı türde sunuculara ve web uygulamalarına erişimi mümkün kılmak için kullanılır.

Sunucu tarafı JavaScript ile Node.js uygulamaları, istemciden gelen web servis isteklerini işler ve yönlendirir.

Bir fonksiyonu veya değeri, modülünüzü içe aktaran ( *import* ) Node.js uygulamalarına kullanılabilir hale getirmek için, örtük ( *implicit* ) `exports` nesnesine bir özellik ekleyin.

Çekirdek ( *core* ) modüller asgari işlevselliği içerir, yerel ( *local* ) modüller uygulamanız için oluşturduğunuz modüllerdir ve üçüncü taraf modülleri Node.js topluluğu oluşturur.

Yerel kurulum ( *local install* ), yalnızca kurulumun yapıldığı dizindeki uygulamanın pakete erişebilmesi anlamına gelir; global kurulum ( *global install* ) ise makinedeki herhangi bir uygulamanın pakete erişebilmesi anlamına gelir.

---

## 🔄 2. Callback Programlama ile Asenkron G/Ç

Asenkron ağ işlemleri, JavaScript kodunun bloklanmasını önlemek için callback fonksiyonları kullanılarak yönetilebilir.

Bir callback fonksiyonunun, Node.js modülü bir yanıt mesajı aldıktan sonra Node.js modülünden ana uygulamaya bir mesaj iletmek için başka bir callback fonksiyonunu çağırması gerekir.

İç içe callback’ler okunması ve hata ayıklaması zor olabilir. Kontrolün tersine çevrilmesi ( *inversion of control* ), üçüncü taraf kodla çalışırken güven sorunlarına neden olur.

Promise nesneleri, zaman alan ve kaynakları bloke edebilen işlemler için en kullanışlıdır.

`JSON.parse()` ve `JSON.stringify()`, JSON nesnelerini ayrıştırmak için kullanılan iki metottur.

---

## 🌐 3. Express Web Uygulama Framework’ü

Geliştiriciler, Node.js’i genişletmek için üçüncü taraf paketlere güvenir.

Node.js framework kurulumunuzda Node.js paketlerini yönetmek için `npm` uygulamasını kullanabilirsiniz.

Model-view-controller (MVC) mimari stili, bir back-end uygulamasını üç bölüme ayırır: model, view ve controller.

REST API framework’leri, birbirleriyle iletişim kurmak için HTTP metotlarını kullanır.

Express, düşük seviyeli detayları soyutlar.

Routing, uygulama seviyesinde veya router seviyesinde ele alınabilir.

Beş tür middleware şunlardır: uygulama seviyesi, router seviyesi, hata yönetimi ( *error handling* ), yerleşik ( *built-in* ) middleware ve üçüncü taraf middleware.

Template rendering, sunucunun dinamik içeriği doldurabilme yeteneğidir.

Kullanıcı kimlik doğrulaması yapmak için bir Express uygulamasında `npm jsonwebtoken` paketinin `require` edilmesi gerekir.
