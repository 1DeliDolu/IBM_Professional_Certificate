## 🔁 Genel Bakış: Sürekli Entegrasyon Eklemek

### ⏪ Önceki Modülde Neler Yaptınız?

Önceki modülde, bitirme (capstone) projeniz için bir RESTful servis geliştirdiniz ve *test-driven development (TDD)* kullanarak mikroservisinizin bileşenlerini oluşturarak  **Sprint 1** ’i tamamladınız.

---

## ⚙️ Bu Modülde Ne Yapacaksınız?

Bu modülde, **GitHub Actions** kullanarak bir **continuous integration (CI)** iş akışı ekleyeceksiniz. Bu, kodunuzu derleme ve test etme süreçlerini otomatikleştirmenize yardımcı olacaktır.

---

## 🗺️ Sprint 2 Planlaması

Öncelikle, yönlendirmeli öğretim laboratuvarı olan  **Sprint 2 Planning** ’i izleyerek **Sprint 2** için bir plan oluşturacaksınız.

Bu aşamada:

* Bir sonraki sprint için hikâyeler ( *stories* ) oluşturacak ve ekleyeceksiniz
* **Label** ’lar ve  **estimate** ’ler ekleyeceksiniz
* Ardından  **sprint backlog** ’unuzu oluşturacaksınız

Bir sonraki laboratuvara geçtiğinizde bu planı kullanacaksınız.

---

## 🧪 Hands-on Lab: Add Continuous Integration

Sonraki adımda, **Add Continuous Integration** uygulamalı laboratuvarında:

* GitHub deponuzda bir **event** gerçekleştiğinde tetiklenecek bir **GitHub Actions workflow** yapılandıracaksınız
  Örneğin:
  * **main branch** ’e bir **pull request** oluşturulduğunda
  * **main branch** ’e bir **push** gerçekleştiğinde

Workflow’unuz:

* Bir veya daha fazla **job** içerebilir
* Job’lar **sıralı (sequential)** veya **paralel (parallel)** çalışabilir

---

## 🧱 Sprint 2 Kapsamında CI Pipeline İçeriği

Sprint 2’nin bir parçası olarak:

* Deponuza yapılan her **push/pull request** için **build** ve **test** çalıştıracak bir workflow oluşturacaksınız
* Kodunuzu lint etmek için **Flake8** kullanacaksınız
* CI pipeline’ınıza **quality checks** ekleyeceksiniz
* Kod kapsamını ( *coverage* ) test etmek için  **nosetests** ’i yapılandıracaksınız

---

## 🗂️ Kanban Üzerinden İlerleme Takibi

İşiniz ilerledikçe:

* İlgili kullanıcı hikâyelerini kanban panonuzda uygun sütunlara taşıyacaksınız
* Bir hikâyeyi tamamladığınızda önce  **"Done"** , ardından **"Closed"** sütununa taşıyacaksınız

---

## 🚀 Başlayalım

Başarılar. Şimdi sürekli entegrasyon (CI) pipeline’ını yapılandırmaya başlayalım!
