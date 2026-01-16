## 📌 Proje Genel Bakış

Bu final projenizde, çevrimiçi kitap inceleme uygulaması geliştirerek *Node.JS* ve *Express.JS* kullanma becerilerinizi, bilginizi ve yetkinliklerinizi pratik etme ve uygulama fırsatına sahip olacaksınız.

---

## 🎯 Final Proje Senaryosu

Bu projede, kitap satan bir çevrimiçi perakendeci için çalışan bir *back-end developer* rolünü üstleneceksiniz. Kitap puanlamalarını ve incelemelerini depolayan, getiren ve yöneten bir sunucu tarafı uygulaması geliştirmeniz isteniyor.

Sunucu tarafı uygulamanızın, kullanıcıların aşağıdaki işlemleri yapabilmesini sağlayacak özellik ve yetenekleri sunması gerekmektedir:

* Kitapçıda mevcut olan tüm kitapların listesini almak
* Kitapların *ISBN* koduna, yazar adlarına ve başlıklara göre belirli kitapları aramak ve ayrıntılarını almak
* Belirtilen kitaplar için incelemeleri/yorumları almak
* Uygulamaya yeni kullanıcı olarak kayıt olmak
* Uygulamaya giriş yapmak
* Bir kitap için yeni bir inceleme eklemek ( *yalnızca giriş yapmış kullanıcılar* )
* Bir kitap incelemesini değiştirmek ( *giriş yapmış kullanıcılar yalnızca kendi incelemelerini değiştirebilir* )
* Bir kitap incelemesini silmek ( *giriş yapmış kullanıcılar yalnızca kendi incelemelerini silebilir* )
* (Birden fazla kullanıcı) Aynı anda uygulamaya erişerek farklı kitap incelemelerini eş zamanlı görüntülemek ve yönetmek

---

## 🏗️ Projeyi Tamamlama Yaklaşımı

Çoğu yazılım geliştirme projesinde olduğu gibi, ekipteki farklı kişiler uygulamanın farklı parçaları üzerinde çalışır. Ekibinizdeki başka bir  *front-end developer* , sunucu tarafı uygulamanızla *REST* kullanarak iletişim kuracak web tabanlı istemci tarafı uygulaması üzerinde çalışmaktadır. Bu nedenle sizin göreviniz, sunucu tarafı uygulamanızı *RESTful* bir web servisi olarak uygulamaktır. Ekibinizdeki bir yazılım mimarı, *Node.js* ve *Express.js* kullanarak sunucu tarafı uygulamanız için iskelet (skeleton) kodu yazmıştır.

Projeyi tamamlamak için; iskelet kodu kendi deponuza ( *repo* ) **fork** edeceksiniz, yerel geliştirme ortamınıza **clone** edeceksiniz ve Express sunucunuzda yukarıda listelenen CRUD yeteneklerini  *HTTP method* ’ları olarak geliştirecek ve *cURL/Postman* ile test edeceksiniz. Ayrıca yalnızca giriş yapmış kullanıcıların belirli işlemleri yapabilmesi için *Session* ve *JWT* kimlik doğrulamasını uygulayacaksınız. Referansınız için bu uygulama, tüm kitap bilgileriyle önceden yüklenmiş olarak gelir.

Ayrıca, birden fazla kullanıcının uygulamayla aynı anda etkileşim kurabilmesi ve birbirlerinin işlemlerinin tamamlanmasını beklememesi için kodunuzu  *Promises* , *Callbacks* veya *Async/Await* fonksiyonlarını kullanarak geliştirmelisiniz.

---

## ✅ Değerlendirme Kriterleri – Toplam 30 Puan

Proje teslimlerinizi aşağıdaki yöntemlerden biriyle gönderebilirsiniz:

### 🤖 Seçenek 1: AI-Değerlendirmeli Teslim ve Değerlendirme

Seçenek 1’i seçtiğinizde, teslimlerinizi yükleyebileceğiniz bir AI aracına yönlendirilirsiniz; teslimleriniz URL’ler, terminal çıktıları, kod parçacıkları veya ekran görüntülerini içerebilir. Ardından, ilerleme sayfanıza otomatik olarak yansıyacak şekilde AI tarafından oluşturulan bir not alırsınız.

### 👥 Seçenek 2: Akran-Değerlendirmeli Teslim ve Değerlendirme

Seçenek 2’yi seçtiğinizde, URL’ler, terminal çıktıları, kod parçacıkları veya ekran görüntüleri gibi teslimlerinizi **My Submission** bölümünden yüklersiniz. Tesliminiz daha sonra akranlarınız veya AI değerlendirici tarafından incelenir.

Daha hızlı değerlendirme için Seçenek 1’i kullanmanızı öneririz. Ancak herhangi bir sorun yaşarsanız veya erişemezseniz, Seçenek 2’yi kullanabilirsiniz.

Notlandırma ile ilgili sorun yaşarsanız, lütfen Discussion Forums üzerinden Course Team ile iletişime geçin.

---

## 🤖 Seçenek 1 Kriterleri: AI-Değerlendirmeli Teslim ve Değerlendirme

Final ödevinizde her görev için belirtilen metni (*cURL komutu* ve çıktısı) laboratuvar talimatlarında belirtildiği şekilde kaydedin. Bu proje final notunuza 30 puan katkı sağlar ve aşağıdaki gibi ağırlıklandırılır:

**Not:** Değerlendirme için, depodaki kitap ayrıntılarını içeren *JSON* dosyası kullanılacaktır.

### 👤 Genel Kullanıcılar

* **Görev 1:** *cURL* komutunu ve çıktısını kopyalayıp yapıştırın; tüm kitap(lar)ın alındığını gösteren metni `getallbooks` olarak kaydedin. – **2 Puan**
* **Görev 2:** *cURL* komutunu ve çıktısını kopyalayıp yapıştırın; belirtilen  *ISBN* ’e göre alınan kitap(lar)ı gösteren metni `getbooksbyISBN` olarak kaydedin. – **2 Puan**
* **Görev 3:** *cURL* komutunu ve çıktısını kopyalayıp yapıştırın; belirtilen yazara göre alınan tüm kitapları gösteren metni `getbooksbyauthor` olarak kaydedin. – **2 Puan**
* **Görev 4:** *cURL* komutunu ve çıktısını kopyalayıp yapıştırın; belirtilen başlığa göre alınan tüm kitapları gösteren metni `getbooksbytitle` olarak kaydedin. – **2 Puan**
* **Görev 5:** *cURL* komutunu ve çıktısını kopyalayıp yapıştırın; başlangıçtaki kitap incelemesini gösteren metni `getbookreview` olarak kaydedin. – **2 Puan**
* **Görev 6:** *cURL* komutunu ve çıktısını kopyalayıp yapıştırın; yeni bir kullanıcının başarılı şekilde kaydını doğrulayan mesajı gösteren metni `register` olarak kaydedin. – **3 Puan**
* **Görev 7:** *cURL* komutunu ve çıktısını kopyalayıp yapıştırın; kayıtlı bir kullanıcı olarak giriş yapma sonucunu gösteren metni `login` olarak kaydedin. – **3 Puan**

### 🔐 Kayıtlı Kullanıcılar

* **Görev 8:** *cURL* komutunu ve çıktısını kopyalayıp yapıştırın; bir kitap incelemesi ekledikten veya değiştirdikten sonra mesajı ve incelemeleri gösteren metni `reviewadded` olarak kaydedin. – **2 Puan**
* **Görev 9:** *cURL* komutunu ve çıktısını kopyalayıp yapıştırın; bir kitap incelemesini sildikten sonra silme mesajını gösteren metni `deletereview` olarak kaydedin. – **2 Puan**

### 🧰 4 Metotlu Node.JS Programı

Dört metodun tamamı için *Node.js* içinde *Axios* ile *Async/Await* veya *Promises* kullanın.

* **Görev 10:** *promise callbacks* veya *async/await* ile *Axios* kullanarak; tüm kitapları ve yazar, başlık ve  *ISBN* ’e göre ayrıntılarını alma kod uygulamasını içeren `general.js` dosyasının  *GitHub URL* ’sini gönderin. – **8 Puan**
* **Görev 11:** *cURL* komutunu ve çıktısını kopyalayıp yapıştırın; *GitHub* deponuzun `ibm-developer-skills-network/expressBookReview` deposundan fork edildiğini gösteren metni `githubrepo` olarak kaydedin. – **2 Puan**

---

## 👥 Seçenek 2 Kriterleri: Akran-Değerlendirmeli Teslim ve Değerlendirme

Akran değerlendirmeniz için, laboratuvar talimatlarında belirtildiği şekilde her bir görev için ilgili ekran görüntülerini alın. Bu projeyi, aynı oturumda kursu tamamlayan akranlarınız değerlendirecektir. Proje final notunuza 30 puan katkı sağlar ve aşağıdaki gibi ağırlıklandırılır:

### 👤 Genel Kullanıcılar

* **Görev 1:** Mağazada mevcut kitap listesini alın. – **2 Puan**
* **Görev 2:**  *ISBN* ’e göre kitapları alın. – **2 Puan**
* **Görev 3:** Yazara göre tüm kitapları alın. – **2 Puan**
* **Görev 4:** Başlığa göre tüm kitapları alın. – **2 Puan**
* **Görev 5:** Kitap incelemesini alın. – **2 Puan**
* **Görev 6:** Yeni kullanıcı kaydı. – **3 Puan**
* **Görev 7:** Kayıtlı kullanıcı olarak giriş yapın. – **3 Puan**

### 🔐 Kayıtlı Kullanıcılar

* **Görev 8:** Bir kitap incelemesi ekleyin/değiştirin. – **2 Puan**
* **Görev 9:** İlgili kullanıcı tarafından eklenen kitap incelemesini silin. – **2 Puan**

### 🧰 4 Metotlu Node.JS Programı

Dört metodun tamamı için *Node.js* içinde *Axios* ile *Async/Await* veya *Promises* kullanın.

* **Görev 10:** Tüm kitapları alın – *async callback function* kullanarak. – **2 Puan**
* **Görev 11:** *ISBN* ile arama – *Promises* kullanarak. – **2 Puan**
* **Görev 12:** Yazara göre arama. – **2 Puan**
* **Görev 13:** Başlığa göre arama. – **2 Puan**
* **Görev 14:** Proje *GitHub* bağlantısının teslimi. – **2 Puan**

---

## ⏭️ Sonraki Adımlar

Adım adım talimatlara başlamadan önce Genel Bakış’ı okuduğunuzdan emin olun.

---

## ✍️ Yazar(lar)

Lavanya T S
Sapthashree K S
Sameep
