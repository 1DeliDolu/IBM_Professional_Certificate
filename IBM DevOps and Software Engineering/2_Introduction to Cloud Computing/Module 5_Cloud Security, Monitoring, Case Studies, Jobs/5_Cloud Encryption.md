# 🔐 Cloud Encryption

Veri güvenliği ve gizliliği konusundaki endişeler göz önüne alındığında, özellikle *public cloud* ortamlarında, *encryption* önemli bir rol oynar ve katmanlı bir güvenlik modelinde sıklıkla **son savunma hattı** olarak adlandırılır. Bu koruma yalnızca verileri şifrelemekle kalmaz, aynı zamanda sağlam  *data access control* , *key management* ve *certificate management* da sağlar. Bu videoda *cloud encryption* konusuna daha yakından bakacağız.

## 🧩 Encryption Tanımı ve Bileşenleri

 *Encryption* , veriyi okunamaz hale getirecek şekilde karıştırmak olarak tanımlanır. Bir şifreleme sisteminin iki parçası vardır: **encryption algorithm** ve  **decryption key** .

 *Encryption algorithm* , verinin okunamaz hale gelmesi için hangi kurallarla dönüştürüleceğini tanımlar. *Decryption key* ise şifrelenmiş verinin tekrar okunabilir veriye nasıl dönüştürüleceğini tanımlar.

## 🛡️ Encryption Ne Sağlar?

 *Encryption* , yalnızca yetkili kullanıcıların hassas verilere erişebilmesini sağlar ve yetkisiz şekilde erişildiğinde veya ele geçirildiğinde veriyi okunamaz ve anlamsız hale getirir.

Cloud sağlayıcıları çeşitli *cloud encryption services* sunar; bu, hassas olarak tanımlanan verilerin sınırlı şifrelenmesi veya cloud’a yüklenen tüm verilerin uçtan uca şifrelenmesi olabilir. Veri alındığı anda şifrelenir ve gerektiğinde veriyi çözmek için *encryption keys* müşterilere iletilir. Anahtarların güvenli biçimde yönetilmesi gerekir. Anahtarlarınızı kaybederseniz, verilerinizi okuyamazsınız.

## 🧊 Veri İçin Üç Durumda Koruma

Verinin üç durumda korunması gerekir:  **at rest** , **in transit** ve  **in use** .

### 🗄️ At Rest Encryption

 *Encryption at rest* , verinin bir veritabanında veya storage katmanında fiziksel olarak depolandığı sırada korunmasını sağlar.

Uygulama ve iş gereksinimlerine bağlı olarak *data at rest* şifrelemesi için birden fazla seçenek olabilir; örneğin *block and file storage* için şifreleme,  *built-in encryption* , *object storage* içinde şifreleme ve  *database encryption services* .

### 🚚 In Transit Encryption

 *Encryption in transit* , verinin bir konumdan diğerine iletildiği sırada korunmasını sağlar.

 *Encryption in transit* ; iletimden önce verinin şifrelenmesini, uç noktaların doğrulanmasını ve varışta verinin çözülüp doğrulanmasını içerir. *Secure Sockets Layer (SSL)* ve  *Transport Layer Security (TLS)* , *in transit encryption* için yaygın kullanılan protokollerdir. Bunlar yalnızca web sitelerine güvenli erişimde değil, aynı zamanda cloud içinde sunucular ve servisler arasında taşınan veriler için de kullanılır.

### 🧠 In Use Encryption

 *Encryption in use* , verinin hesaplamalar için bellek içinde kullanıldığı sırada korunmasını sağlar. Veriyi çözmeye gerek kalmadan şifreli metin üzerinde hesaplamaların yapılmasına olanak tanır.

## 🏷️ Cloud Storage Encryption Türleri

Cloud storage encryption *server-side* veya *client-side* olabilir.

### 🏢 Server-Side Encryption

 *Server-side encryption* , Cloud storage verinizi aldıktan sonra, ancak veri diske yazılıp depolanmadan önce gerçekleşir.

*Server-side encryption* için ya kendi şifreleme anahtarlarınızı oluşturup yönetebilirsiniz; bu, *customer supplied encryption keys* olarak bilinir. Ya da cloud storage sağlayıcısının sunduğu *key management services* kullanarak anahtarları oluşturup yönetebilirsiniz; bu da *customer managed encryption keys* olarak bilinir.

### 🧑‍💻 Client-Side Encryption

 *Client-side encryption* , veri Cloud storage’a gönderilmeden önce gerçekleşir. Bu şekilde kullanıcılar, cloud sağlayıcısı tarafından görünmeyen şifreleme anahtarları ve algoritmalarını kullanabilir; bu da cloud sağlayıcılarının barındırılan veriyi çözmesini pratik olarak imkânsız hale getirir.

## 🌐 Multi-Cloud Ortamlarında Tekil Koruma Stratejisi İhtiyacı

Günümüzde işletmelerin çoğunluğu *multi-cloud* ortamlarda faaliyet gösterdiğinden, enterprise genelinde  *on-premise* , *hybrid* ve *multi-cloud* dağıtımları boyunca tekil bir data protection stratejisi uygulama ihtiyacı vardır.

Bazı cloud sağlayıcıları,  *data access management* , entegre *key management* ve gelişmiş şifreleme gibi bir dizi özelliğe sahip *multi-cloud data encryption services* sunar. Bu özellikler bir araya gelerek, verinin nerede bulunduğundan bağımsız biçimde, enterprise genelindeki en hassas workload’ları korumaya yardımcı olacak ölçeklenebilirlik ve esneklik sağlar.

## 🧰 Multi-Cloud Data Encryption Console ile Yönetim

Bir *multi-cloud data encryption console* kullanarak erişim politikalarını tanımlayıp yönetebilir, şifreleme anahtarlarını oluşturabilir, rotasyonunu yapabilir ve yönetebilir, ayrıca erişim loglarını bir araya getirebilirsiniz.

*Encryption* veri güvenliği riskini ortadan kaldırmaz; güvenlik riskini verinin kendisinden ayırır ve güvenliği şifreleme anahtarlarına taşır. Bu anahtarların, veriyi güvenli tutmak için tehditlere karşı yönetilmesi ve korunması gerekir.

## 🔑 Key Management Services ve Yaşam Döngüsü Yönetimi

Bazı cloud sağlayıcılarının sunduğu  *key management services* , cloud servislerinde veya müşteri tarafından geliştirilen uygulamalarda kullanılan şifreleme anahtarları için yaşam döngüsü yönetimi yapmaya yardımcı olur.

Müşterilerin *at rest* durumundaki hassas verileri şifrelemesini sağlar ve veriyi şifrelemek için kullanılan kriptografik anahtarların tüm yaşam döngüsünü kolayca oluşturup yönetmelerine olanak tanır. Anahtarlar müşterinin elinde kaldığından, veri hem cloud service provider’lardan hem de diğer kullanıcılardan korunur.

## ✅ Encryption Key Management Best Practices

Şifreleme anahtarı yönetimi için bazı en iyi uygulamalar şunları içerir:

* Şifreleme anahtarlarını, şifrelenmiş veriden ayrı saklamak.
* Anahtar yedeklerini *off site* almak ve düzenli olarak denetlemek.
* Anahtarları periyodik olarak yenilemek.
* Hem *master* hem de *recovery keys* için *multi-factor authentication* uygulamak.
