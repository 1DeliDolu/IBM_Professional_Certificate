# 🛡️ Identity and Access Management

Cybersecurity Insiders tarafından yayımlanan Cloud Security Report’a göre, siber güvenlik profesyonellerinin bulut güvenliği konusundaki en büyük endişesi  **veri kaybı ve sızıntısıdır** . Çalışan kimlik bilgilerinin kötüye kullanılması ve uygunsuz erişim kontrolleri yoluyla  **yetkisiz erişim** , bulut güvenliği için algılanan en büyük tek güvenlik açığıdır; bunu **güvensiz arayüzler ve API’ler** izler.

Bu videoda, **Identity and Access Management** (IAM) olarak da bilinen  **erişim kontrolünün** , kullanıcıları **kimlik doğrulama (authenticate)** ve **yetkilendirme (authorize)** yoluyla doğrulayarak bulut kaynaklarına, hizmetlerine ve uygulamalarına **kullanıcıya özel erişim** sağlamada ilk savunma hattı olarak nasıl çalıştığına bakacağız.

Kapsamlı bir güvenlik stratejisi, geniş bir kitlenin güvenlik ihtiyaçlarını kapsamalıdır — buna  **kurumsal kullanıcılar** ,  **internet ve sosyal tabanlı kullanıcılar** , **üçüncü taraf iş ortakları** ve **tedarikçiler** dahildir.

## 👥 Kullanıcı Türleri

Üç ana kullanıcı türü vardır:  **Administrative Users** , **Developer Users** ve  **Application Users** .

### 🧑‍💼 Administrative Users

Administrative users; bulut platformu yöneticileri, operatörler ve yöneticileri içerir: — genellikle uygulama ve hizmet örneklerini  **oluşturan** , **güncelleyen** ve **silen** roller ve ayrıca ekip üyelerinin faaliyetleri hakkında içgörüye ihtiyaç duyarlar.

Bir saldırgan bir administrative hesabı ele geçirirse, üretim veritabanı hizmet örneklerinden  **veri çalabilir** , müşterinin etki alanı içinde **kötü amaçlı uygulamalar dağıtabilir** veya hatta mevcut uygulamaları **tahrif edebilir** ya da  **yok edebilir** .

### 🧑‍💻 Developer Users

Developer users; bulut uygulama geliştiricilerini, platform geliştiricilerini ve uygulama yayıncılarını içerir. Developer users, **hassas bilgileri okumaya** ve uygulamaları  **oluşturmaya** , **güncellemeye** ve **silmeye** yetkilidir.

### 👤 Application Users

Üçüncü kullanıcı türü  **Application user** ’dır. Bunlar, bulutta barındırılan uygulamaların kullanıcılarıdır.

## 🧩 Identity and Access Management’in Temel Bileşenleri

Identity and access management’in temel bileşenlerine ve nasıl çalıştıklarına bakalım.

### ✅ Authentication

Authentication veya  *identity service* , buluta dağıtılmış uygulamaların kullanıcıları uygulama düzeyinde kimlik doğrulamasını sağlar; aşağıdakiler gibi çeşitli kimlik sağlayıcılarına dayanabilir:

* bulut dizini ( *cloud directory* )
* Google, LinkedIn, Facebook ve Twitter gibi sosyal kimlik sağlayıcıları
* kurumsal barındırılan ( *enterprise-hosted* ) kimlik sağlayıcı
* bulut barındırılan ( *cloud-hosted* ) kimlik sağlayıcı

Bazen, *API keys* veya benzersiz tanımlayıcılar, çağıran uygulamayı veya kullanıcıyı tanımlamak için bir API’ye geçirilir.

### 🔐 Multifactor Authentication

 *Multifactor authentication* , uygulama kullanıcıları için ek bir kimlik doğrulama katmanı ekleyerek kimlik hırsızlığıyla mücadele etmek için kullanılır; örneğin tek kullanımlık şifreler veya PIN’ler, sertifikalar, token’lar, risk tabanlı kimlik doğrulama (kullanıcının konumundaki değişiklikler, geçmiş etkinliği ve tercihleri gibi).

### 📁 Cloud Directory Services

 *Cloud Directory services* , bir bulut ortamı içinde kullanıcı profillerini ve bunlarla ilişkili kimlik bilgilerini ve parola politikasını güvenli bir şekilde yönetmek için kullanılır.

Bulut içinde bir dizin hizmeti, bulutta barındırılan uygulamaların kendi kullanıcı deposunu kullanmasına gerek olmadığı anlamına gelir.

### 📊 Reporting

Reporting, kaynaklara erişimin kullanıcı merkezli bir görünümünü veya kullanıcıların erişiminin kaynak merkezli bir görünümünü sağlamaya yardımcı olur.

Raporlar genellikle şunlar hakkında bilgi verir: hangi kullanıcıların hangi kaynaklara erişimi olduğu, hangi kullanıcıların erişim haklarında değişiklikler olduğu, her kullanıcının hangi erişimi kullandığı ve hangi koşullar altında olduğu.

### 🧾 Audit and Compliance

Audit and compliance, hem bulut sağlayıcı hem de bulut tüketicisi için identity and access management çerçevesi içinde kritik bir hizmettir.

Denetçiler, uygulanan kontrolleri bir kuruluşun güvenlik politikasına, endüstri uyumluluğuna ve risk politikalarına göre doğrulamak — ve sapmaları raporlamak için bu süreçleri kullanır.

### 🔄 User and Service Access Management

User and service access management yeteneği, bulut uygulama ve hizmet sahiplerinin müşteri, iş ortağı ve tedarikçi kullanıcı profillerini minimum insan etkileşimiyle **provision** ve **de-provision** etmesini sağlar.

Bu, sahibin tanımladığı role, organizasyona ve erişim politikalarına göre erişim kontrolünü kolaylaştırır.

## 🧱 Hassas Hesapların Yaşam Döngüsü Kontrolleri

Yöneticilerin ve geliştiricilerin kullanıcı hesapları hassas bilgilere erişim sağlar. Bu hesapların ele geçirilmesi risklerini azaltmak için, bu kullanıcıların tüm yaşam döngüsü üzerinde maksimum kontrole ihtiyaç vardır.

Bu hassas hesapların güvenliğini sağlamaya yardımcı olabilecek bazı kontroller şunlardır:

* her kullanıcı için kaynaklar üzerinde roller belirterek kullanıcıları **provision** etmek
* özel karakterlerin kullanımı, minimum parola uzunlukları ve benzeri ayarları kontrol eden parola politikaları
* zaman tabanlı tek seferlik parolalar gibi multifactor authentication
* kullanıcılar ayrıldığında veya rol değiştirdiğinde erişimin anında **de-provision** edilmesi

## 🧩 Cloud Provider IAM Hizmetleri

Bulut sağlayıcıları, genellikle erişim grupları oluşturma, kullanıcıları erişim gruplarına ekleme ve mevcut kullanıcılar için erişimi yönetme yeteneğini içeren Identity Access and Management hizmetleri sunar.

Bir  *access group* , bir veya daha fazla erişim politikasıyla gruptaki tüm varlıklara aynı erişimin tek seferde atanabilmesi için oluşturulan kullanıcılar ve service ID’lerden oluşan bir gruptur.

## 📜 Access Policies

Access policies, hesap içindeki kullanıcıların, service ID’lerin ve access group’ların hesap kaynaklarına erişim izninin nasıl verildiğini tanımlar.

Politikalar şunları içerir:

* **subject** : kullanıcılar, service ID’ler veya access group’lar olabilir
* **target** : erişim vermek istediğiniz kaynak veya sağlanmış hizmet teklifi ( *provisioned service offering* )
* **role** : politikanın hedefinde izin verilen eylemleri tanımlar; yani erişimin verildiği kaynak üzerinde hangi işlemlere izin verildiği

Access groups, her kullanıcıya tek tek erişim atamaya kıyasla daha akıcı bir erişim atama süreci sağlar ve bir hesaptaki politika sayısını azaltmaya yardımcı olur.

## ✅ Sonuç

Bu videoda, Identity and Access Management’in bulutu güvence altına almak için ilk savunma hattı olarak nasıl çalıştığını öğrendik.
