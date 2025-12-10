# ⚙️ FaaS Modeline Giriş

“ **FaaS Modeline Giriş** ”e hoş geldiniz.

Bu videoyu izledikten sonra şunları yapabileceksiniz:

 *FaaS’in ne olduğunu açıklamak* , *FaaS modelinin faydalarını* anlatmak ve *FaaS’in ilkelerini ve en iyi uygulamalarını* açıklamak.

![1765369736217](image/3_IntroductiontotheFaaSModel/1765369736217.png)

---

## ☁️ FaaS Nedir?

 *Function-as-a-Service (FaaS)* , mikroservis tabanlı uygulamaları oluşturma ve yayına alma ile genellikle ilişkilendirilen karmaşık altyapıya ihtiyaç duymadan, olaylara (events) yanıt olarak kod çalıştırmanıza olanak tanıyan bir bulut bilişim ( *cloud-computing* ) hizmeti türüdür.

![1765369764146](image/3_IntroductiontotheFaaSModel/1765369764146.png)

FaaS aşağıdaki özelliklere sahiptir:

* *Serverless computing* ’in bir alt kümesidir.
* Uygulamaları birden çok fonksiyon şeklinde oluşturur; burada fonksiyon, herhangi bir programlama dilinde yazılabilen bir yazılım parçasıdır.
* FaaS, hem hibrit bulutlarda ( *hybrid clouds* ) hem de şirket içi ( *on-premises* ) ortamlarda kullanılabilir.
* *Stateless* (durumsuz) çalışır, ancak harici önbellekler ( *external caches* ) kullanarak durum bilgisini koruyabilir.

---

## ⚡ FaaS Fonksiyonlarının Çalışma Biçimi

Fonksiyonlar milisaniyeler içinde çalışır ve bireysel istekleri paralel olarak işler; bu da onları anında ölçeklenebilir hâle getirir.

FaaS:

* Hafiftir ve *decoupling* (bağımsızlaştırma) mimarisi mekanizmasını kullanır.
* Faturalama, sunucu örneği boyutlarına göre değil, fonksiyonların çalışma süresine göre yapılır.

![1765369818677](image/3_IntroductiontotheFaaSModel/1765369818677.png)

---

## 📉 Maliyet ve Zaman Kazancı

FaaS ile sunucuyu, otomatik ve birbirinden bağımsız olarak ölçeklenebilen fonksiyonlara bölebilirsiniz; böylece altyapıyı yönetmek zorunda kalmazsınız.

Bu da pazara çıkış süresini ( *time-to-market* ) kısaltan uygulama koduna odaklanmanızı sağlar.

FaaS modelinin en büyük faydalarından biri maliyettir:

* Yalnızca bir eylem gerçekleştiğinde ödeme yaparsınız.
* Eylem tamamlandığında her şey durur — hiçbir kod çalışmaz, hiçbir sunucu boşta kalmaz ve hiçbir maliyet oluşmaz.

---

## 📈 Ölçeklenebilirlik ve Yüksek Erişilebilirlik

Fonksiyonlar durumsuz, küçük ve bağımsız kod parçaları olduğu için:

* Gerektiğinde otomatik, bağımsız ve anında ölçeklenebilirler.
* Talep azaldığında da otomatik olarak küçülürler.

FaaS, bölgeler ( *regions* ) ve kullanılabilirlik bölgelerine ( *availability zones* ) yayılmış olduğu ve ek artan maliyetler olmaksızın dağıtılabildiği için doğası gereği yüksek erişilebilirlik ( *high availability* ) sunar.

![1765369866045](image/3_IntroductiontotheFaaSModel/1765369866045.png)

---

## 🧱 Sunucusuz (Serverless) Yığının Bileşenleri

Bir *serverless stack* (sunucusuz yığın), üç ana bileşenden oluşur:

* *Functions-as-a-Service (FaaS)*
* *Backend-as-a-Service (BaaS)*
* *API Gateway*

Şimdi sunucusuz bir yığındaki bileşenlerin nasıl çalıştığına bakalım.

---

## 🔄 Olay Akışı ve API Gateway Rolü

Olay (event) istekleri aşağıdaki gibi farklı kanallardan alınır:

* HTTP isteği
* Github ve Docker Hub gibi depolardaki webhook’lar
* Zamanlanmış işler ( *scheduled jobs* )

Bu istekler, ilgili fonksiyonları belirleyip onlara yönlendiren *API Gateway* üzerinden geçer.

Fonksiyonlar bu istekleri işler ve gerekirse daha ileri işleme ve/veya saklama için arka uç ( *backend* ) hizmetlere yönlendirir:

* Dosya ve nesne depolama
* Blok depolama
* Bildirim hizmetleri vb.

Çıktı veya yanıt daha sonra FaaS bileşeni ve *API Gateway* üzerinden istemciye geri gönderilir.

![1765369923870](image/3_IntroductiontotheFaaSModel/1765369923870.png)

---

## 🖼️ Gerçek Dünya Örneği: Profil Fotoğrafı Yükleme

Gerçek bir örnek olarak, bir web sitesine profil resmi yüklemeniz gereken bir durumu düşünün.

Web sitesi, bazı web sayfalarında görüntülemek için bu görselin bir küçük resmine (thumbnail) de ihtiyaç duyabilir.

Bu,  *Function-as-a-Service* ’in yaygın olarak kullanıldığı bir durumdur.

Adımlar:

1. Bir kullanıcı bir profil fotoğrafı seçer.
2. Görsel, bir nesne depolama kovasına ( *object storage bucket* ) yüklenir.
3. Bu olay, profil fotoğrafını işleyen ve bir küçük resim (thumbnail) oluşturan bir IBM Cloud fonksiyonunu tetikler.
4. Fonksiyon, oluşturduğu küçük resmi nesne depolamada saklar; böylece gerektiğinde web sitesi bu küçük resme erişebilir.

![1765369964351](image/3_IntroductiontotheFaaSModel/1765369964351.png)

---

## 🧪 FaaS Fonksiyon Tasarım İlkeleri

FaaS fonksiyonları, bir olaya yanıt olarak tek bir işi yapmak üzere tasarlanmalıdır.

Bu nedenle:

* Kod kapsamınızı sınırlı, verimli ve hafif olacak şekilde tasarlayın ki fonksiyonlar hızlıca yüklensin ve çalışsın.

FaaS’in değeri, fonksiyonların yalıtımında (isolation) yatar:

* Çok fazla fonksiyon kullanmak maliyetinizi artırır ve fonksiyonlarınızın yalıtımının getirdiği değeri ortadan kaldırır.
* Çok fazla üçüncü taraf kütüphane kullanmak, fonksiyonun başlatılmasını yavaşlatabilir ve ölçeklenmesini zorlaştırabilir.

![1765370024799](image/3_IntroductiontotheFaaSModel/1765370024799.png)

---

## 🧩 Yönetilen FaaS Sağlayıcıları

Yaygın yönetilen ( *managed* ) FaaS sağlayıcılarından bazıları şunlardır:

* Amazon’dan **AWS Lambda**
* **Google Cloud Functions**
* Microsoft’tan **Azure Functions**
* IBM tarafından sunulan **Cloud Functions**
* Red Hat’ten **OpenShift Cloud Functions**
* Ve  **Netlify** , **Oracle** ve **Twilio** gibi birkaç diğer sağlayıcı

![1765370043817](image/3_IntroductiontotheFaaSModel/1765370043817.png)

---

## 🛠️ Kendi Kendine Yönetilen (Self-Managed) FaaS Seçenekleri

Üçüncü taraf yönetilen platformlara bağımlı olmak istemezseniz, birçok kendi kendine yönetilen ( *self-managed* ) FaaS seçeneği de mevcuttur. Bunlara örnek olarak:

* **Fission** – Kubernetes üzerinde sunucusuz fonksiyonlar için bir framework
* **Fn Project** – konteyner-yerel ( *container-native* ) bir sunucusuz platform
* **Knative** – sunucusuz iş yüklerini ( *serverless workload* ) oluşturmak, dağıtmak ve yönetmek için Kubernetes tabanlı bir platform
* **OpenFaaS** – herhangi bir Linux veya Windows sürecini bir fonksiyona dönüştürmenize olanak tanır

![1765370074463](image/3_IntroductiontotheFaaSModel/1765370074463.png)

---

## 📌 Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* FaaS, olaylara yanıt olarak kod çalıştırmanıza olanak tanıyan ve karmaşık bir altyapıya ihtiyaç duymayan bir bulut bilişim hizmeti türüdür.
* FaaS, uygulamaları birden çok fonksiyon şeklinde oluşturan  *serverless computing* ’in bir alt kümesidir.
* FaaS, hem hibrit bulutlarda hem de şirket içi ortamlarda dağıtılabilir.
* FaaS’te faturalama, sunucu örneği boyutlarına göre değil, fonksiyonları çalıştırmak için harcanan süreye göre yapılır.
* Bir  *serverless stack* , FaaS, BaaS ve bir API Gateway’den oluşur.
* Seçebileceğiniz birçok farklı yönetilen ve kendi kendine yönetilen FaaS platformu bulunmaktadır.

![1765370108447](image/3_IntroductiontotheFaaSModel/1765370108447.png)
