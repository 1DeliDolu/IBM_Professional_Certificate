## 🧩 Middleware ve Router’lara Giriş

Bu makalede, *middleware* ve *routes* terimlerini ele alacağız.

---

## 🔗 Middleware Nedir?

 *Middleware* , uygulamalar, veritabanları veya servisler arasında yer alan ve bu farklı teknolojilerin iletişim kurmasını sağlayan yazılımdır. Dağıtık bir sistemde son kullanıcı için kesintisiz etkileşimler oluşturur.

---

## 📨 Express ve Mesajlaşma Framework’leri

Express,  *routes* ’ları yönetmek ve *middleware* yazmak için kullanılan bir mesajlaşma çatısıdır ( *messaging framework* ). Bir uygulamanın ön ucu ( *front end* ), ön uç ve arka uç ( *back end* ) servislerinin aynı dili kullanmasına gerek kalmadan arka uçtaki bileşenler arasında iletişimi kolaylaştırmak için Express’i kullanır. Ön uç, arka uçla doğrudan değil, *middleware* ile iletişim kurar.

Express gibi mesajlaşma çatılarında yaygın olarak  **JSON** , **REST API’ler** ve **web servisleri** bulunur. Daha eski mesajlaşma çatıları, sırasıyla JSON ve REST API’ler yerine **genişletilebilir biçimlendirme dili (XML)** ve **basit nesne erişim protokolleri (SOAP)** içerebilir. Mesajlaşma çatısı, farklı uygulamalar arasında veri aktarımını yönetmek için standartlaştırılmış bir yol sağlar.

---

## 🌐 Web Sunucusu, Route ve Routing

Bir web sunucusu, bir web sitesini bir veritabanına bağlayan *middleware* örneğidir. Web sunucusu iş mantığını ( *business logic* ) yönetir ve isteğe göre veritabanından gelen veriyi yönlendirir.

Bir  *route* ,  **GET** , **POST** veya **DELETE** gibi bir HTTP isteğini bir URL ile ve o URL’yi işleyen çağrılan fonksiyonla ilişkilendiren kod bölümüdür.

 *Routing* , web geliştirmede tarayıcının URL’si tarafından belirlenen kurallara göre bir uygulamanın kullanıcı arayüzünü ( *user interface* ) bölmek için kullanılır.

---

## 🧭 Router Fonksiyonları ve Middleware Zinciri

Router fonksiyonlarına topluca “ *middleware* ” denir.  *Middleware* , bir HTTP isteğine yanıt vermekten veya *middleware chain* içindeki başka bir fonksiyonu çağırmaktan sorumludur.

Express, Router sınıfı üzerinden router fonksiyonlarını yönetir; örneğin `Router.get()` gibi. Adından da anlaşılacağı üzere, `Router.get()` HTTP **GET** isteklerini işler. Diğer Router fonksiyonları arasında çoğunlukla aynı şekilde çalışan `Router.post()`, `Router.put()`, `Router.delete()` bulunur.

Bu yöntemler iki argüman alır: bir URL yolu ( *URL path* ) ve bir callback fonksiyonu.

---

## 🛡️ Routing Dışındaki Middleware Sorumlulukları

Routing’e ek olarak  *middleware* , servisler arasında veriyi şifreleyip şifresini çözerek güvenli bağlantılar sağlamaktan, trafiği farklı sunuculara dağıtarak uygulama yüklerini yönetmekten ve veri istemciye döndürülmeden önce veriyi sıralamaktan veya filtrelemekten de sorumludur.
