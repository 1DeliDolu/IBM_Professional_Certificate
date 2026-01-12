# 🧩 Uygulama Projesi: Conference Expense Planner uygulaması

*Conference Expense Planner* uygulaması uygulama projesinde, kullanıcının bir kongre merkezinde konferans düzenlemekle ilgili giderleri fiyatlandırmasına olanak tanıyan bir uygulamanın ön yüzünü (front end) oluşturacaksınız. Laboratuvar, bu proje için gerekli uygulama öğelerinin geliştirilmesi boyunca size rehberlik edecektir.

 *Conference Expense Planner* ; bir  **açılış (landing) sayfasına** , bir **ürün seçimi sayfasına** ve bir **açılır özet penceresine** sahip olacaktır. Ürün seçimi sayfası, kullanıcıların odalarını, eklentilerini (add-ons) ve yemeklerini seçmelerine olanak tanır. Bu seçimlere dayanarak fiyatlandırma sağlar. Açılır pencere, ürün seçimi sayfasından kullanıcının yaptığı seçimlere göre giderleri bir tabloda özetler.

Nihai projeye başlamadan önce uygulama projesini tamamlamanızı şiddetle teşvik ediyoruz. Bu, nihai projenizde geliştirmeniz gerekecek birçok aynı öğe ve işlevi geliştirmeniz için pratik yapmanızı sağlayacaktır. Uygulama projesi laboratuvarı, bu uygulamada gereken kod için adım adım yönergeler içerir.

Konferans gider bütçeleme uygulamasının özelliklerini daha ayrıntılı şekilde ele alalım. Örnek ekran görüntüleri sağlanmıştır; ancak kod, bileşenler ve düzenlerle denemeler yapmaktan çekinmeyin.

---

## 🏁 Açılış sayfası

Açılış sayfası, nihai projenin açılış sayfasıyla aynı öğelere sahip olacaktır.

Ürün hattınızla müşterilerinizi etkileyecek ve ana uygulamaya giriş sağlayacak, aşağıdaki görsele benzer bir açılış sayfası oluşturacaksınız. Bu sayfanın nasıl görünebileceğine ilişkin bir görsel için bu bölümün sonundaki ekran görüntüsüne bakın.

Bu sayfadaki özellikler şunları içermelidir:

* Şirket hakkında bir paragraf
* Bir arka plan görseli
* Şirket adınız ve
* Ürün seçimi sayfasına bağlanan bir **Get Started** düğmesi

Açılış sayfanız şuna benzer görünecektir:

---

## 🧾 Ürün seçimi sayfası

**Get Started** seçildikten sonra, uygulama kullanıcıyı ürün seçimi sayfasına yönlendirmelidir. Bu sayfa, kullanıcıların mekândaki odaları, mikrofon ve hoparlör gibi sunumlar için gerekli eklentileri (add-ons) ve katılımcılar için ikram edilmesini istedikleri yemekleri seçmelerine olanak tanır. Bu sayfa üç bölümden oluşacaktır:  **oda seçimi** , **eklentiler (add-ons)** ve  **yemekler** . Her bölümün kendi başlığı olmalı; ayrıca her bölüme gezinme (navigation) sağlayan bir sayfa başlığı da bulunmalıdır.

Önerilen düzen, her bölüm için açıklamalı bir ekran görüntüsünde ve tüm sayfanın bir görselinde gösterilmiştir.

---

## 🏢 Oda seçimi ve gezinme çubuğu

Kullanıcılar 5 oda türü arasından seçim yapar:

* **Auditorium hall** – kapasite 200, adet başına $5500
* **Conference room** – kapasite 15, adet başına $3500
* **Presentation room** – kapasite 50, presentation room, adet başına $700
* **Large meeting room** – kapasite 10, adet başına $900
* **Small meeting room** – small meeting room, kapasite 5, adet başına $1100

Kullanıcının ihtiyaç duyduğu her oda türünün sayısını talep edebilmesi için her oda türü için bir **artırma (increment)** ve **azaltma (decrement)** düğmesi sağlayacaksınız.

Ürün seçimi sayfasında ayrıca bir gezinme çubuğu içeren bir üst bilgi (header) olmalıdır. Gezinme çubuğu, kullanıcının seçimleriyle ilgili verileri gösteren bir açılır pencere açan bir **Show Details** düğmesi göstermelidir.

---

## ➕ Add-ons seçimi

Kullanıcılar add-ons bölümünde ses/görüntü ekipmanlarını seçebilir:

* **Speakers** – adet başına $35
* **Microphones** – adet başına $45
* **Whiteboards** – adet başına $80
* **Projectors** – adet başına $200
* **Signage** – adet başına $80

Kullanıcının ihtiyaç duyduğu her tür AV ekipmanının sayısını talep edebilmesi için her ekipman türü için bir **artırma (increment)** ve **azaltma (decrement)** düğmesi sağlayacaksınız.

---

## 🍽️ Yemek seçimi

Kullanıcılar yemekler bölümünde aşağıdaki seçenekleri seçebilir:

* **Breakfast** – kişi başı $50
* **Lunch** – kişi başı $60
* **High tea** – kişi başı $25
* **Dinner** – kişi başı $70

Kullanıcının bu yemekler için kişi sayısını girebileceği bir metin giriş kutusu sağlayacaksınız.

---

## 🖼️ Örnek ürün seçimi sayfası (tüm bölümler)

Örnek ürün seçimi sayfası (tüm bölümler):

---

## 🪟 Show details açılır penceresi

Kullanıcıların seçimlerinin ayrıntılarını görmesi gerekecektir. Bu öğe için, bu bilgilere üst bilgideki **Show Details** düğmesi aracılığıyla erişebilirler. Kullanıcı düğmeyi seçtiğinde, dört sütunlu bir tablo gösteren bir pencere açılır. Tablonun her satırı; seçim türünü, birim maliyetini, belirtilen miktarı ve o öğe türünün miktarı için ara toplamı içerir. Ayrıca tüm öğeler için toplam maliyeti de gösterecektir.

---

## 🔁 Nihai proje benzerlikleri

Nihai proje, uygulama projesiyle ortak birçok öğeye sahiptir. Nihai projeniz için, ev bitkileri satın almaya yönelik bir alışveriş sepeti uygulaması oluşturacaksınız.

İki proje arasındaki benzer işlevler şunları içerir:

* Açılış sayfası
* Gezinme çubuğu
* Ürün öğeleri dizisi ve ilişkili veriler
* Seçilen öğe dizisi
* Bir dizi üzerinde yineleme yapmak için *`map()`* fonksiyonunun kullanımı
* Ara toplam ve toplam maliyet hesaplamaları
* Kullanıcı seçimlerine dayalı dinamik fiyatlandırma gösterimleri
* Ürün miktarı seçimi için artırma ve azaltma düğmeleri
* Uygulama durumlarını *Redux* ve *Redux toolkit* ile *'slices'* kullanarak yönetme
* Etkileşimli UI öğelerini sunmak için fonksiyon bileşenleri
