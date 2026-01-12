# 🛡️ Erişim Yönetiminin Politikaları ve İlkeleri

## 📜 Politikalar

Bulut güvenliğinde bir  *politika* , kullanıcıların bir bulut ortamındaki kaynaklara nasıl erişmesi ve bu kaynakları nasıl koruması gerektiğini belirleyen kurallar ve yönergeler bütününü ifade eder. Bu politikalar; güvenliği sürdürmek, sektör düzenlemelerine uyumu sağlamak ve olası riskleri azaltmak için bir çerçeve sunar.

Bir politikanın formatı genellikle şunları içerir:

* Politika için açıklayıcı bir ad veya tanımlayıcı sağlayan bir başlık
* Politikanın kapsamı; politikanın uygulandığı belirli kaynakları, sistemleri veya kişileri tanımlar
* Politikanın amacı; hedeflerini ve amacını belirtir
* Politika beyanı; politikanın kurallarını, prosedürlerini ve kısıtlamalarını listeler
* Politikayı uygulayan ve politikaya uyan kişi ve grupların rol ve sorumlulukları
* Uyumluluk ve yaptırım ayrıntıları veya politika uyumluluğunu izlemek ve sağlamak için alınan önlemler
* Politikanın güncel ve etkili kalması için ne sıklıkla gözden geçirilip güncelleneceğini belirten inceleme ve revizyon bölümü

## 🏢 Hizmet sağlayıcı ve müşteri tarafından yönetilen politikalar

Bulut hizmet sağlayıcıları ( *Cloud Service Providers - CSPs* ) genellikle altyapılarının, veri merkezlerinin ve hizmetlerinin genel güvenliğini yöneten güvenlik politikalarına sahiptir. Bu politikalar, müşteri verileri için temel düzeyde güvenlik ve koruma sağlar. Hizmet sağlayıcı politikaları; fiziksel güvenlik, ağ güvenliği, veri şifreleme, erişim kontrolleri ve olay müdahalesi gibi çeşitli yönleri kapsar.

Hizmet sağlayıcı politikalarına ek olarak müşteriler, kendi politikalarını da uygulayabilir; bunlar *müşteri tarafından yönetilen politikalar* ( *customer-managed policies* ) olarak da bilinir. Bu politikalar, müşterilerin güvenlik önlemlerini kendi gereksinimlerine, sektör düzenlemelerine ve risk toleransına göre uyarlamasına olanak tanır. Müşteri tarafından yönetilen politikalar; ek güvenlik kontrolleri, erişim kısıtlamaları, veri koruma önlemleri ve uyumluluk çerçevelerini içerebilir.

Hizmet sağlayıcı ve müşteri tarafından yönetilen politikaları birleştirerek organizasyonlar, bulut hizmet sağlayıcısının sağladığı temel güvenlik önlemlerinden faydalanırken kendi benzersiz ihtiyaçlarıyla uyumlu kapsamlı bir güvenlik çerçevesi oluşturabilir.

## 🔒 En Az Ayrıcalık İlkesi

*En az ayrıcalık ilkesi* ( *principle of least privilege* ), yetkisiz erişim veya kaynakların yanlışlıkla kötüye kullanılma riskini azaltan erişim kontrolünde temel bir kavramdır. Organizasyonların, kullanıcılara görevlerini yerine getirebilmeleri için gerekli olan en az izinleri vermesi gerektiğini belirtir. En az ayrıcalık ilkesini izleyerek organizasyonlar, ele geçirilmiş kullanıcı hesaplarının neden olabileceği potansiyel zararı sınırlar.

## 👤 Kullanıcı Erişim Seviyesi

Bir bulut ortamında kullanıcı erişim seviyeleri, rollerine ve sorumluluklarına bağlı olarak değişir. Bazı kullanıcılar yalnızca konsola veya bulut hizmet sağlayıcısının kaynak yönetimi ve yapılandırma için sunduğu grafiksel kullanıcı arayüzüne ( *GUI* ) erişime ihtiyaç duyabilir. Bu kullanıcılar, kaynak sağlama ( *provisioning* ), izleme ve yönetim gibi görevleri gerçekleştirmek için konsol üzerinden bulutla etkileşime girer.

Diğer yandan yazılım geliştirmeyle ilgilenen kullanıcıların geliştirme ortamına erişime ihtiyacı olabilir. Bu ortam, bulutta uygulama oluşturmak, test etmek ve dağıtmak için gerekli araçları, API’leri ve hizmetleri içerir. Bu kullanıcılar, yalnızca konsola bağlı kalmak yerine API’ler ve komut satırı arayüzleri ( *CLI’ler* ) kullanarak bulut altyapısıyla etkileşime girer.

Organizasyonun gereksinimlerine bağlı olarak bazı kullanıcılar hem konsola hem de geliştirme ortamına erişebilir; bu da daha geniş bir görev ve sorumluluk yelpazesini yerine getirmelerini sağlar.

## 🧩 Kimlik ve Erişim Yönetimi (IAM)

*Kimlik ve Erişim Yönetimi* ( *Identity and Access Management - IAM* ), organizasyonların bulut ortamındaki kullanıcı kimliklerini ve kaynaklara erişimlerini yönetmesini ve doğrulamasını sağlar. Yalnızca yetkili kişilerin hassas sistemlere, uygulamalara ve verilere erişim ayrıcalıklarına sahip olmasını garanti eden süreçleri ve politikaları içerir. IAM, kullanıcı sağlama ( *provisioning* ), kimlik doğrulama ( *authentication* ) ve yetkilendirme ( *authorization* ) süreçlerini merkezileştirerek kullanıcı yönetimini basitleştirir; gerektiğinde erişim haklarını vermeyi veya iptal etmeyi kolaylaştırır. Bu süreç, organizasyonların güvenliği artırmasına, hassas bilgileri korumasına, düzenlemelere uyumu zorunlu kılmasına ve kullanıcı erişimiyle ilgili idari görevleri kolaylaştırmasına yardımcı olur.

## 🔑 Standart Parola Politikası

Buluta giriş yapan kullanıcılar için standart bir parola politikası, güçlü parola güvenliğini sağlamak amacıyla en iyi uygulamalara uygun olmalıdır. Tipik olarak bir parola politikası; minimum uzunluk ve büyük/küçük harfler, sayılar ve özel karakterlerin kombinasyonu gibi parola karmaşıklığı gereksinimlerini içerir. Politika ayrıca parola geçerlilik süresi aralıklarını tanımlayabilir; bu aralıklardan sonra kullanıcıların parolalarını değiştirmesi gerekir. Ek olarak, eski bir parolanın yeniden kullanılabilmesi için önce belirli sayıda benzersiz parola kullanmayı zorunlu kılan parola geçmişi ( *password history* ) uygulaması, parola tekrar kullanımına karşı ek bir koruma katmanı sağlar. Diğer parola politikaları arasında hesap kilitleme, çok faktörlü kimlik doğrulama ve kullanıcı farkındalığı ile eğitim yer alabilir. Bir parola politikasının özel gereksinimleri, organizasyonun ihtiyaçlarına, gereksinimlerine ve risk değerlendirmelerine bağlı olacaktır.

## 🧾 Kimlik sağlayıcı standartları (SAML, OpenID)

 *Kimlik sağlayıcı standartları* , kimlik sağlayıcılarının ( *IdPs* ) ve hizmet sağlayıcılarının ( *SPs* ) kimlik doğrulama ve kimlik bilgilerini güvenli biçimde nasıl değiş tokuş edeceğini tanımlayan protokoller ve çerçevelerdir. Bu standartlar, kimlik doğrulama ve erişim yönetimi için tutarlı ve standartlaştırılmış yaklaşımlar sağlar. Yaygın kullanılan iki kimlik sağlayıcı standardı şunlardır:

* *Security Assertion Markup Language (SAML)*
  SAML, IdP’ler ve SP’ler arasında yetkilendirme ve kimlik doğrulama verilerinin değiş tokuşu için kullanılan XML tabanlı bir standarttır. Güvenli tek oturum açma ( *SSO* ) ve kimlik federasyonunu mümkün kılar. SAML, kullanıcıların IdP’leriyle bir kez kimlik doğrulaması yapmasına ve ayrı ayrı kimlik doğrulama gerekmeksizin birden fazla SP’ye erişmesine olanak tanır. SAML iddiaları ( *assertions* ), kullanıcının kimliği ve öznitelikleri hakkında bilgi içerir; SP’ler bu bilgilere dayanarak kaynaklarına erişim izni verir.
* *OpenID Connect*
  OpenID Connect, OAuth 2.0 protokolü üzerine inşa edilmiş modern bir standarttır. Kimlik doğrulama ve kimlik federasyonu için bir çerçeve sunar. OpenID Connect, kullanıcıların seçtikleri OpenID sağlayıcısı ile kimlik doğrulaması yapmasına ve kimlikleri hakkında bilgi içeren bir *ID token* almasına olanak tanır. Hizmet sağlayıcılar, bu ID token’ı kullanıcıları doğrulamak ve kaynaklarına erişim sağlamak için kullanabilir.

Bu kimlik sağlayıcı standartları, bulut ortamları, web uygulamaları ve kurumsal sistemler dahil olmak üzere çeşitli bağlamlarda kimlik doğrulama ve erişim kontrolünü yönetmek için güvenli ve birlikte çalışabilir çözümler sunar. Organizasyonların kimlik sağlayıcılar ile hizmet sağlayıcılar arasında güven ilişkileri kurmasına, kullanıcı kimlik doğrulama deneyimlerini basitleştirmesine ve kimlik yönetimini merkezileştirerek güvenliği artırmasına yardımcı olur.

## 🧷 Tanımlar

* *Identity and Access Management (IAM):* Yalnızca yetkili kişilerin erişim ayrıcalıklarına sahip olmasını sağlayarak kullanıcı kimliklerini ve kaynaklara erişimi yöneten ve doğrulayan süreçler ve politikalar.
* *Principle of Least Privilege:* Kullanıcılara görevlerini yerine getirmek için gereken minimum izinleri vererek yetkisiz erişim riskini azaltan erişim kontrolünde temel bir kavram.
* *Standard Password Policy:* Buluta giriş yapan kullanıcılar için güçlü parola güvenliği sağlamak amacıyla parola karmaşıklığı, süresi dolma ve geçmişi gibi gereksinimlerin bir kümesi.
* *Identity Provider Standards (SAML, OpenID):* Kimlik sağlayıcıları ve hizmet sağlayıcıların kimlik doğrulama ve kimlik bilgilerini güvenli biçimde değiş tokuş etmesini tanımlayan ve tutarlı erişim yönetimi sağlayan protokoller.
* *Cloud Security Policy:* Bulut ortamında kullanıcıların kaynaklara nasıl erişmesi ve kaynakları nasıl koruması gerektiğini belirleyen; güvenlik ve uyumluluğu sağlayan kural ve yönergeler bütünü.

Bu içerik yapay zeka tarafından üretildi, bu nedenle lütfen olası hataları kontrol edin.
