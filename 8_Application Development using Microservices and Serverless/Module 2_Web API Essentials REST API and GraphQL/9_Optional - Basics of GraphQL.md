# 🧩 İsteğe Bağlı: GraphQL’in Temelleri

## 🎬 GraphQL Temellerine Hoş Geldiniz

‘GraphQL’in Temelleri’ne hoş geldiniz. Bu videoyu izledikten sonra şunları yapabileceksiniz:  *GraphQL* ’i açıklamak, bir  *GraphQL API* ’nin temel özelliklerini açıklamak ve  *GraphQL API* ’lerini kullanmanın faydalarını açıklamak.

![1765364453858](image/9_Optional-BasicsofGraphQL/1765364453858.png)

 *GraphQL* , API’niz için bir sorgu ( *query* ) dilidir. İstemcilerin API’den yalnızca ihtiyaç duydukları veriyi talep etmelerine olanak tanıyan standart bir yol sağlar. Ve dil bağımsız ( *language agnostic* ) olduğundan, herhangi bir programlama dili kullanılarak geliştirilebilir.

 *GraphQL* , API’den tam olarak ihtiyacınız olanı elde etmenizi sağlar. Bu, talep etmediğiniz verileri almadığınız anlamına gelir.

![1765364481732](image/9_Optional-BasicsofGraphQL/1765364481732.png)

---

## 🎯 Tam İhtiyaç Duyulan Veriyi Alma

Bu aynı zamanda, farklı kaynaklardan geliyor olsa bile, tam olarak ihtiyaç duyduğunuz veriyi aldığınız anlamına gelir.  *RESTful API* ’nin aksine, *GraphQL* ihtiyaç duyduğunuz her şeyi almak için yalnızca tek bir uç nokta ( *endpoint* ) gerektirir.

Ve bu ürün örneğinde görülebileceği gibi, yalnızca ada ihtiyaç duyarsınız ve aldığınız şey de tam olarak odur.

![1765364510295](image/9_Optional-BasicsofGraphQL/1765364510295.png)

---

## 🔄 REST ve GraphQL Arasındaki Farklar

 *REST* ’te, API’leriniz belirli bir işlemi bir *HTTP* yöntemi kullanarak gerçekleştirmek için uç noktalar sağlayan kaynaklardır.

 *GraphQL* ’de ise, şemada tanımladığınız  *type* ’lar düğümlerdir ( *nodes* ).

*REST* ile sunucuya birden fazla çağrı yapar ve sunucunun gönderdiği her ne ise onu alırsınız. Ancak  *GraphQL* ’de yalnızca ihtiyaç duyduğunuz şeyi istersiniz ve onu alırsınız.

![1765364534195](image/9_Optional-BasicsofGraphQL/1765364534195.png)

---

## 🧱 GraphQL API’lerini Genişletme, Sorgular ve Mutasyonlar

 *GraphQL API* ’nizi genişletmek için yeni bir sürüme ihtiyaç yoktur; yeni alanları, mevcut istemcileri bozmadan eklersiniz, çünkü istemciler yalnızca ihtiyaç duyduklarını talep ediyorlardı.

Bir  *Query* , verilerinizi sorgulamak için kullanılır; bu,  *RESTful API* ’deki bir *GET* isteğine daha çok benzer. En basit hâliyle  *GraphQL* , nesneler üzerindeki belirli alanlar için isteklerde bulunur.

Bir  *mutation* , verilerinizi yönetmek ve değiştirmek için kullanılır. Ve *mutation* tipindeki her alan,  *RESTful API* ’deki bir  *POST* , *PUT* veya *DELETE* isteği olarak düşünülebilir.

![1765364574779](image/9_Optional-BasicsofGraphQL/1765364574779.png)

---

## 🎥 Netflix ve Studio API Örneği

 *Netflix* , gevşek bağlı ( *loosely coupled* ) ve yüksek ölçeklenebilir ( *highly scalable* ) mikroservis mimarisiyle tanınmaktadır.  *Netflix* , özgün içerikleri hızlandırılmış bir tempoyla üretmektedir.

Bir TV programı veya filmin ortaya atıldığı andan Netflix’te izlenebilir hâle geldiği ana kadar, perde arkasında pek çok şey olur.

Başlangıçta, varlıklar arasındaki ilişkiler dağınıktı ve çeşitli mikroservisler içinde bulunuyordu. Bu zorlukların üstesinden gelmek için ekip, “ *Studio API* ” adlı, özenle tasarlanmış bir *Graph API* oluşturmaya başladı.

Bunun hedefi, verilerin ve ilişkilerin üzerinde birleşik bir soyutlama ( *unified abstraction* ) sağlamaktır.

Bu yeni tasarımda  *Studio API* , şemadan ve sorguları çözümlemeden ( *resolving queries* ) sorumludur.

Dolayısıyla *Netflix* mühendislik ekibi burada durmadı ve her ekibin kendi alanlarının sahipliğine sahip olduğu federe bir mimariye ( *federated architecture* ) bir adım daha ilerledi.

![1765364591192](image/9_Optional-BasicsofGraphQL/1765364591192.png)

![1765364604523](image/9_Optional-BasicsofGraphQL/1765364604523.png)

![1765364617132](image/9_Optional-BasicsofGraphQL/1765364617132.png)

![1765364640037](image/9_Optional-BasicsofGraphQL/1765364640037.png)

---

## ✅ Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:  *GraphQL* , API’niz için dil bağımsız bir sorgu dilidir; size ne eksik ne fazla, tam olarak ihtiyacınız olan veriyi sağlar ve yalnızca bir uç noktaya ( *endpoint* ) sahiptir.

![1765364657860](image/9_Optional-BasicsofGraphQL/1765364657860.png)
