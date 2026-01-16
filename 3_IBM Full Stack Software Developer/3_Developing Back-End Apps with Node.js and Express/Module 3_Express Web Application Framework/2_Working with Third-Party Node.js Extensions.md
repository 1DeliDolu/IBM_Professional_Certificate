
## 🧑‍💼 Expert Viewpoints: Üçüncü Taraf Node.js Uzantılarıyla Çalışmak

Üçüncü taraf Node.js Uzantılarıyla Çalışmak: Expert Viewpoints’e hoş geldiniz. Bu videoda, birkaç uygulama geliştirme profesyoneli, yaygın olarak hangi üçüncü taraf Node.js uzantılarını kullandıklarını ve bu uzantıların çoğu zaman uygulama geliştiricilerine nasıl fayda sağlayabileceğini tartışacak.

*NPM* Node.js paketlerinden en çok kullandıklarımdan biri *serverless framework*tür; çünkü bu, bulutta  *serverless microservices* ’ları çok fazla kaynak ve altyapı (*resource* ve  *infrastructures* ) kodunu kendiniz yazmadan çok kolay şekilde dağıtmanıza olanak tanır.

---

## 🧰 Sık Kullanılan Node.js Uzantıları

Sürekli kullandığım birçok Node.JS uzantısı var. Örneğin, koleksiyonlar ve dizilerle (*collections* ve  *arrays* ) çalışmak, doğru öğeleri bulmak, sıralamak ve benzeri işler için harika bir paket olan *Lodash* kullanıyorum. Çok zaman kazandırıyor.

*Axios* da *RESTful APIs* ile çalışmak ve `GETS`, `PUTS`, `POSTS` göndermek gibi işler için çok kullanışlıdır.

Ayrıca *Express* uygulamalarımda bir sürü *middleware* var; özellikle *authentication* ve *JWT tokens* ile ilgili  *middleware* ’ler. Bunların hepsi son derece kullanışlıdır ve bulutta hizmetler ve diğer araçlar oluşturan herhangi bir bulut geliştiricisini gerçekten hızlandırmaya yardımcı olur.

---

## 🌐 Web Servislerine İstek Atma: Axios

Node.js ile çalışırken, günlük olarak kullandığım en sevdiğim paketlerden ikisini paylaşacağım. İlki, web servislerine istek yapmaktır.

Uygulamam büyük olasılıkla başka bir web servisinden bilgi istemek zorunda kalır. Bu, benim yazdığım bir web servisi de olabilir ya da başka birinin yazdığı bir web servisi de olabilir. Her durumda, bazı giriş parametreleriyle dışarı bir istek göndermem ve sonra isteğin geri gelmesini ya da yanıtın ( *response* ) geri gelmesini bekleyip o yanıtı ele almam gerekir.

Tüm bu kodu kendim yazmak yerine, doğru başlıklarla ( *headers* ) bu istekleri oluşturmama yardımcı olan ve ayrıca geri dönen yanıtları ele alabilmem için callback fonksiyonları ve/veya *promises* sağlayan *Axios* gibi bir kütüphane kullanıyorum.

---

## 🗄️ Veritabanlarıyla Çalışma İçin NPM Paketleri

İkinci paketim ise veritabanlarıyla çalışırken olur; ilişkisel ( *relational* ) bir veritabanı ya da *NoSQL database* olup olmamasına bakmaksızın, harici bir veritabanıyla konuşmak için büyük olasılıkla *NPM* paketleri kullanırım.
