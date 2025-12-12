# 🛡️ OWASP Top 7-10

## 🎬 Giriş

OWASP Top 7-10’a hoş geldiniz!

Bu videoyu izledikten sonra şunları yapabileceksiniz:

* Kimlik tespiti ve kimlik doğrulama hatalarını ve bunların önlenmesini açıklamak.
* Yazılım ve veri bütünlüğü hatalarını ve bunların nasıl önleneceğini belirlemek.
* Güvenlik günlüğe kaydetme ve izleme hatalarını ve bunlara yönelik önleme adımlarını tanımak.
* Sunucu taraflı istek sahteciliğini ( *Server-Side Request Forgery – SSRF* ) ve önleme yöntemlerini tartışmak.

---

## 👤 Kimlik ve Kimlik Doğrulama Hataları

### 🚨 Otomatik saldırılara izin verilmesi

Kimlik tespiti ve kimlik doğrulama hataları, uygulamanızın aşağıdakilere izin vermesi durumunda ortaya çıkar:

* *Credential stuffing*
* *Brute force* (kaba kuvvet)
* Diğer otomatik saldırılar

 *Credential stuffing* , bir saldırganın meşru kullanıcı adları ve parolalardan oluşan bir listeye sahip olması durumunda gerçekleşir. Saldırgan, bu parolaları bir saldırıda kullanmak için otomasyondan yararlanır.

---

### 🔑 Oturum kimlikleri ve oturum zaman aşımı

Oturum tanımlayıcı ( *session identifier – ID* ) bilgilerinin URL’lerde açığa çıkması da bir hatadır.

Oturum kimliğinizi ( *session ID* ) elinde bulunduran herhangi biri, web sitesini kandırarak gerçekten kendi bilgisayarınızda sizmişsiniz gibi davranabilir. Bu da saldırganlara, daha önce oturum açmış olduğunuz hesaba tam erişim sağlar.

Bir oturum, kullanıcı adı ve parola ile oturum açtığınızda oluşturulur. Oturum zaman aşımı, belirli bir süre hareketsiz kaldıktan sonra sizi otomatik olarak sistemden çıkarır; ancak uygulama geliştirme sırasında çoğu zaman göz ardı edilir.

Uygulamanız bu özelliği sağlamıyorsa, oturum açmış kullanıcıların bilgisayarlarının başından ayrılması, yetkisiz erişime ve veri ihlali riskine davetiye çıkarır.

---

### 🛡️ Kimlik ve kimlik doğrulama hatalarını önleme

Kimlik tespiti ve kimlik doğrulama hatalarını önlemek için yazılım tedarik zincirinden başlamalısınız.

Yazılım tedarik zinciri, yaşam döngüsü boyunca uygulamanıza dokunan veya onun geliştirilmesinde rol oynayan her şeyi kapsar. Yazılım tedarik zinciri güvenlik araçları, uygulama bileşenlerinizi tarayarak bilinen güvenlik açıklarından arınmış olduklarından emin olmanızı sağlar.

Yapılandırma değişiklikleri üzerinde düzenli kontroller ve incelemeler yapmak, yazılım hattınızın saldırıya uğrama riskini azaltır. Hassas verileri, şifrelenmemiş biçimde güvenilmeyen kaynaklara iletmekten kaçının.

Veri güvenliğini sağlamak ve kurcalamayı önlemek için dijital imzalar veya diğer türde bütünlük kontrollerini kullanabilirsiniz.

 *Credential stuffing* , *brute force* ve diğer otomatik saldırıları önlemek için çok faktörlü kimlik doğrulama (MFA) kullanın ve uygulamanızı varsayılan kimlik bilgileri etkin halde olacak şekilde dağıtmaktan kaçının.

Sunucu tarafında bir oturum yöneticisi uygulayarak yeni, rastgele oturum kimlikleri üretin ve oturum tanımlayıcılarının URL’lerde görünmediğinden emin olun. Bunları güvenli bir şekilde saklayın ve çıkış yaptıktan sonra, hem hareketsizlik (idle timeout) hem de mutlak zaman aşımı (absolute timeout) sonrasında geçersiz kılındıklarından emin olun.

---

## 🧱 Yazılım ve Veri Bütünlüğü Hataları

### 💥 Bütünlük hatalarının kaynağı

Yazılım ve veri bütünlüğü hataları, bunlara karşı koruma sağlamayan kod ve altyapı nedeniyle ortaya çıkar.

Uygulamaların dayandığı bileşenler, güvenilmeyen kaynaklardan geliyorlarsa güvenlik açıkları oluşturabilir. Günümüzdeki birçok uygulama, otomatik güncelleme yetenekleri sayesinde önceden güvenilen bir uygulamaya, yeterli bütünlük doğrulaması olmaksızın güncellemeler indirip kurar.

Saldırganların, dağıtım için güvensiz bir CI/CD hattına kötü amaçlı güncellemeler yüklemesi ve bunların tüm kurulumlara uygulanması mümkündür. Bu da veri ihlallerine veya diğer türde saldırılara yol açabilir.

---

### 🧪 Yazılım ve veri bütünlüğü hatalarını önleme

Yazılım ve veri bütünlüğü hatalarını aşağıdakileri yaparak önleyebilirsiniz:

* CI/CD hattınızı ayrıştırarak (segregate) ayrı katmanlara bölün.
* Hattın doğru biçimde yapılandırıldığından ve erişim kontrolünün eksiksiz ve doğru olduğundan emin olun. Bu, kodunuzun derleme ve dağıtım süreci boyunca bütünlüğünün korunmasına yardımcı olur.
* Uygulamanızın bileşenlerini, bilinen güvenlik açıkları için taramak üzere bir yazılım tedarik zinciri güvenlik aracı kullanın.
* Herhangi bir dijital imza veya bütünlük kontrolü olmadan, imzasız, şifrelenmemiş veya serileştirilmiş verileri güvenilmeyen istemcilere göndermeyin.

Dijital imzalar ve diğer türde bütünlük kontrolleri kullanmak, verinin veya kodun meşru bir kaynaktan geldiğini ve kurcalanmadığını doğrulamaya yardımcı olur.

---

## 📊 Güvenlik Günlüğe Kaydetme ve İzleme Hataları

### ⚠️ Yetersiz günlükleme ve izleme riskleri

Günlüğe kaydetme ( *logging* ) ve izleme ( *monitoring* ), ihlallerin tespit edilmesi ve bunlara yanıt verilmesi için kritik öneme sahiptir. Yetersiz günlüğe kaydetme ve izleme, ciddi sorunların üzerini örtebilir.

Eksik, zayıf veya kafa karıştırıcı girdilere sahip günlükler, sorun giderme sürecini zorlaştırır. İhlal girişimleri, oturum açma ve başarısız oturum açma gibi denetlenebilir olayları kaydetmeyen uygulamalar, faydadan çok zarar verir.

---

### 🕵️ Adli inceleme ve görünürlük eksikliği

Bir ihlal veya başka bir siber saldırı durumunda bu ayrıntıları günlükte yakalamak esastır. Günlüklerin çok hızlı bir şekilde üzerine yazılması, gecikmiş adli analiz üzerinde olumsuz etki yaratır.

Bir ihlal aylar önce gerçekleşmişse ve günlükleriniz çok hızlı bir şekilde üzerine yazılıyorsa, bunun ne zaman veya nasıl gerçekleştiğini – ve tekrar olup olmadığını – asla öğrenemeyebilirsiniz.

Bir izleme sisteminin eksikliği, altyapılarında neler olup bittiği konusunda herkesi karanlıkta bırakır. Sağlam bir izleme sistemi, sorunları, eğilimleri ve diğer problemleri tespit eder ve bunlar hakkında uyarı verir.

Güçlü bir güvenlik günlüğe kaydetme ve izleme sistemi olmadan, saldırganlar kuruluşunuzda kimsenin fark etmeyeceği kadar uzun süre kalabilir – ta ki çok geç olana kadar.

---

### ✅ Günlükleme ve izleme hatalarını önleme

Günlüğe kaydetme ve izleme hatalarını aşağıdakileri yaparak önleyebilirsiniz:

* Uygulamanızın doğru bilgileri, doğru biçimde ve doğru zamanda günlüklere yazdığından emin olun.
* Tüm günlüğe kaydetmeyi merkezileştirin ve ham günlük dosyalarının düzenli yedeklerini alın – ya da daha da iyisi, günlüklerinizi `logstash` gibi bir günlük toplayıcıya akıtın. Bu toplayıcı, günlükleri `elasticsearch` gibi bir veritabanında saklar; böylece bunlar `Kibana` gibi bir araçla görselleştirilebilir ve uzun süre saklanabilir.

Çoğu bulut-yerel ( *cloud-native* ) sistem, örneğin `Kubernetes`, bunu oldukça kolay bir şekilde yapmanıza olanak tanır.

Günlük biçimi, günlük analiz araçlarını kullanmayı planlıyorsanız önemlidir. Oturum açma, erişim kontrolü ve sunucu tarafı girdi doğrulaması gibi denetlenebilir olayları dahil edin.

Şüpheli veya kötü niyetli hesapları tanımlayabilmek için yeterli bağlam sağlayın ve verilerin, gecikmiş adli analiz için yeterince uzun süre günlüklerde tutulduğundan emin olun.

Eşik değerler, panolar (dashboards) ve uyarı mekanizmaları içeren sağlam bir izleme sistemi uygulayın; böylece şüpheli faaliyetler hızlı bir şekilde tespit edilip bunlara yanıt verilebilir.

Günlüklerinizi, saldırganlar tarafından yapılan kurcalama veya günlük dosyası manipülasyonu kanıtlarını aramak için periyodik olarak denetleyin. Çok sayıda günlük girdisini incelemek zorunda kalabilirsiniz.

---

## 🌐 Sunucu Taraflı İstek Sahteciliği (SSRF)

### 🧨 SSRF nedir ve nasıl çalışır?

Sunucu taraflı istek sahteciliği ( *Server-Side Request Forgery – SSRF* ), harici saldırganların diğer dahili sistemlere yönelik kötü amaçlı istekler oluşturmasına veya bunları kontrol etmesine olanak tanır.

Bunun nasıl çalıştığına bakalım: Bir saldırgan, dahili bir sunucuya doğrudan erişim sağlamaya çalışır ve bir güvenlik duvarı bu bağlantı girişimini engeller. Saldırgan şanslıdır ve SSRF saldırısına karşı savunmasız bir web sunucusu keşfeder ve bunu istismar eder.

SSRF saldırıları, dahili sistemler arasındaki güven ilişkisini kötüye kullanarak bunu yapar. SSRF saldırıları ayrıca güvenlik duvarlarını, VPN’leri ve Erişim Kontrol Listelerini ( *Access Control Lists – ACL* ) atlayabilir.

Artık etkilenen sunucu, daha fazla saldırı ve yoklamalar için bir araç haline gelir. Saldırganlar etkilenen sunucuyu kullanarak:

* Yerel veya harici ağlarda açık portları tarayabilir,
* Yerel dosyalara erişebilir,
* Diğer IP adreslerini keşfedebilir
* Ve uzaktan kod çalıştırma ( *remote code execution – RCE* ) elde edebilir.

SSRF saldırıları tehlikelidir.

---

### 🧮 SSRF türleri

SSRF saldırıları, dışarıdan normalde erişilmemesi gereken dahili sistemlere saldırganların sızmasına ve bu sistemleri manipüle etmesine olanak tanır.

Sunucu taraflı istek sahteciliğine biraz daha yakından bakalım. SSRF’nin üç türü vardır:

* **Temel (veya Kör – Blind) SSRF** : Bu durumda saldırgan, etkilenen sunucuya bir URL sağlar ancak URL’den alınan veriler hiçbir zaman saldırgana geri döndürülmez.
* **Yarı kör (Semi-blind) SSRF** : Bu durumda saldırgan, etkilenen sunucuya bir URL sağlar ancak saldırgana, daha fazla bilgi elde etmek için kullanabileceği sınırlı miktarda veri açığa çıkar.
* **Kör olmayan (Non-blind) SSRF** : Bunlar en tehlikelileridir. Bu durumda, herhangi bir *Uniform Resource Identifier* (veya URI) içindeki veriler, dahili bir servis tarafından saldırgana geri döndürülür.

---

### 🛡️ SSRF saldırılarını önleme ve genel özet

SSRF saldırılarını aşağıdaki kontrollerin bir kısmını veya tamamını kullanarak önleyebilirsiniz:

* İstemciler tarafından sağlanan tüm girdi verilerini temizleyin ( *sanitize* ) ve doğrulayın ( *validate* ).
* İzin verilen URL’leri, portları ve hedefleri zorunlu kılmak için bir beyaz liste ( *whitelist* ) oluşturun.
* Web sunucularını, HTTP yönlendirmelerine (redirects) izin vermeyecek şekilde yapılandırın.
* Uygulamalarınızın, doğrulama olmadan ham yanıtları istemcilere göndermesine izin vermeyin.

Bu videoda şunları öğrendiniz:

* Güvenlik açıklarını kapatarak, daha iyi günlükler oluşturarak ve kaliteli bir izleme ve uyarı sistemiyle görünürlük ekleyerek uygulamanızı ve altyapınızı daha güvenli hale getirebilirsiniz.
* Bütünlük kontrolleri ve dijital imzaların uygulanması, kurcalamayı önler. Bütünlük kontrolleri eksikse, yazılım güncellemeleri ve güvenilmeyen kaynaklardan gelen veri veya bileşenler üzerinde oynama yapılabilir.
* Girdi verileri her zaman temizlenmeli ve doğrulanmalıdır.
* İmzasız, şifrelenmemiş veya serileştirilmiş veriler hiçbir zaman güvenilmeyen istemcilere gönderilmemelidir.
* Web sunucunuzu belirli işlevlere izin vermeyecek şekilde doğru biçimde yapılandırmak, sunucu taraflı istek sahteciliğini azaltabilir.
