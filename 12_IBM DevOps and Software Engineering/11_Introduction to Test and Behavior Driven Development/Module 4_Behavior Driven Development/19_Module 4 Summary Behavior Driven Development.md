# 📘 Modül 4 Özeti: Davranış Odaklı Geliştirme

Tebrikler! Bu modülü tamamladınız. Bu noktada kursta şunları biliyorsunuz:

---

## 🧠 BDD Temelleri

*Davranış odaklı geliştirme* ( *behavior driven development - BDD* ), bir uygulamanın amaçlandığı gibi davrandığından emin olan, **önce test** ( *test-first* ) yaklaşımıyla geliştirme yapma yöntemidir.

Yazılım test sürecinde, BDD uygulamak için uygun seviyeler  **entegrasyon** , **sistem** ve **kabul** ( *acceptance* ) testleridir.

BDD, alan uzmanlarının, test uzmanlarının, geliştiricilerin ve paydaşların kolayca anlayabileceği tek bir sözdiziminde davranışları açıklar.

---

## 🔁 BDD İş Akışı

BDD iş akışı üç adımdan oluşur:

* İstenen davranışı tanımlamak için örnekler veya senaryolar oluşturmak
* Bu örnekleri otomatik testler olarak çalıştırmak
* Gerektikçe ek testler yazmak

BDD iş akışı, yazılımınız için hem spesifikasyon hem de test görevi gören tek bir dokümana götürür.

BDD spesifikasyonu oluşturmak için, **Given, When, Then** sözdizimini kullanarak bir *feature* ve senaryolar yazın.

*Cucumber* ve *Behave* gibi BDD araçları *Gherkin* sözdizimini kullanırken, *Concordion* gibi araçlar başka spesifikasyon sözdizimlerini kullanır.

Bir BDD aracı seçerken, desteklediği programlama dilleri ve spesifikasyon sözdizimlerini dikkate almalısınız.

---

## 📂 Behave Çalıştırma ve Yapısı

*Behave* çalıştırmak için, özellik ( *feature* ) dosyaları için bir **Features** klasörü ve bunun altında Python adım ( *steps* ) dosyaları için bir **Steps** klasörü oluşturmanız gerekir.

Behave çalıştırıldığında şu işlemleri gerçekleştirir:

* Her özellik dosyasındaki Gherkin ifadelerini okur.
* Adım dosyalarında eşleşen Python adımlarını arar.
* Python adımlarına gömülü test fonksiyonlarını çalıştırır.

---

## 🧰 Behave Ortamı Kurulumu

Behave ortamını kurmak için şunları yapmalısınız:

* *getenv()* ve diğer gerekli modülleri içe aktarmak.
* Ortamdan global değişkenleri tanımlamak.
* Test fikstürlerinizi ( *test fixtures* ) tanımlamak.

---

## ✍️ Feature Dosyası Yazma İpuçları

Bir feature dosyası yazarken şu ipuçlarını izlemelisiniz:

* Tutarlılık sağlamaya çalışın.
* Kullanıcı deneyimini dikkate alın.
* Sistemin bir isteğe yanıt verdiğini gösteren ipuçları ( *cues* ) ekleyin.

Bir feature içinde, her senaryodan önce aynı başlangıç durumunu kolayca kurmak için **Background** bölümü kullanabilirsiniz.

---

## 🖥️ Selenium ile Web Etkileşimlerini Otomatikleştirme

*Selenium* ile web sayfası etkileşimlerini otomatikleştirmek için şunları yapmalısınız:

* Ortamda ( *environment* ) Selenium’u başlatmak.
* Selenium’un bir elementi türüne göre bulma yöntemlerinden birini seçmek.
* O elementle ne yapılacağını belirtmek.

---

## 🧩 Python Adımı Yazma

Bir Python adımı yazmak için şunları yapmalısınız:

* Bir Gherkin ifadesinin anahtar kelimesini ve string’ini not etmek.
* Bu ifadeye karşılık gelen bir Python adımı yazmak.
* Bu adımı uygulamak için bir fonksiyon yazmak.

---

## 🧾 Behave ile Test Verisi Çekme ve Yükleme

Behave ile test verisini çıkarmak ve yüklemek için, bir feature’ın **Background** bölümüne bir veri tablosu ekleyebilir ve sonra bu tablonun içeriği üzerinde bir **‘for’** döngüsü ile dolaşabilirsiniz.
