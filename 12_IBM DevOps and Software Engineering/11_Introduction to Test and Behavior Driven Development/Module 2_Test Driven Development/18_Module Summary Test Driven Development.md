## 🧪 Module Summary: Test Driven Development

Tebrikler! Bu modülü tamamladınız. Kursun bu noktasında şunları biliyorsunuz:

* *TDD* ’de test vakaları, kod tasarımını yönlendirir.

---

## 🔁 Red/Green/Refactor İş Akışı

*Red/Green/Refactor* iş akışı üç adımdan oluşur:

* Sahip olmayı istediğiniz kod için başarısız olan bir unit test vakası yazın
* Bu test vakasını geçmek için yeterli kod yazın
* Kalitesini artırmak için kodu *refactor* edin

---

## ⏱️ TDD ve DevOps Pipeline

* *TDD* , geliştirme süresinden tasarruf sağlar ve kodun beklendiği gibi çalışmasını garanti eder.
* Bir *DevOps pipeline* oluşturmak için tüm testleri otomatikleştirmeniz gerekir.

---

## 🧰 TDD için Test Framework’leri ve Araçlar

* *xUnit* serisi, TDD için en popüler test framework’lerinden biridir; diğerleri arasında JavaScript için  *Jasmine* , Node.js için *Mocha* ve PHP için *SimpleTest* bulunur.
* Python için en popüler iki test framework’ü *PyUnit* ve  *Pytest* ’tir.
* Python için diğer iki popüler test framework’ü *Doctest* ve  *RSpec* ’tir.
* *Nose* , test çıktısına renk ekleyebilen ve kod kapsamı (code coverage) aracını çağırabilen bir Python test runner’ıdır.

---

## 💻 Bash Üzerinden TDD Testlerini Çalıştırma

* Bash’te TDD testlerini çalıştırmak için `unittest`’i veya *Nose* yüklüyse `nosetests`’i çağırabilirsiniz.

```bash
python -m unittest
```

```bash
nosetests
```

---

## 🟢 Nose ve unittest Farkları

* `unittest`’ten farklı olarak  *Nose* ; test sonuçlarını renklendirebilir, kod kapsamını raporlayabilir ve eksik test vakalarını listeleyebilir.

---

## ✅ Assertions ve Test Koşulları

* Test framework’leri, test koşullarını basitleştiren araçlar sağlar.
* *Assertions* , testlerin geçip geçmediğini belirlemek için yapılan kontrollerdir.
* Python’da assertion oluşturmak için geliştiriciler `assert()` fonksiyonunu veya ek *PyUnit* assertion’larını kullanabilir.

---

## 🙂 Happy Path ve 🙁 Sad Path

* *Happy path* ’ler, bir fonksiyonun beklendiğinde pozitif sonuçlar döndürdüğünü doğrular.
* *Sad path* ’ler ise bir fonksiyonun istisnalara (exceptions) uygun şekilde ve bozulmadan yanıt verdiğini doğrular.

---

## 🧩 Test Fixtures

* *Test fixtures* , her testten önce ve sonra bilinen bir başlangıç durumu oluşturur.
* *Test fixtures* , mock object’ler oluşturma ve veritabanını bilinen bir veri setiyle yükleme gibi birçok test senaryosu için faydalıdır.

---

## 🧷 Test Fixtures Seviyeleri

*Test fixtures* üç özgüllük seviyesinde çalışır:

* Modül
* Test vakası
* Test
