# 🔄 TDD ve BDD

Bu videoyu izledikten sonra, *test-driven development* (TDD) ile *behavior-driven development* (BDD) yaklaşımlarını karşılaştırıp aralarındaki farkları açıklayabilecek ve geliştiricilerin neden hem TDD’ye hem de BDD’ye ihtiyaç duyduğunu anlatabileceksiniz.

---

## 🧭 Behavior-Driven Development (BDD)

 *Behavior-driven development* , adından da anlaşılacağı gibi, sistemin  **içeriden nasıl çalıştığının ayrıntılarıyla değil** , dışarıdan gözlemlenen **davranışıyla** ilgilenir. BDD, tüm bileşenlerin birlikte nasıl davrandığını görmek için *integration testing* açısından oldukça etkilidir. Düşünme biçiminizi dışarıdan içeriye doğru zorlar.

Başka bir deyişle, yalnızca iş çıktılarıyla en doğrudan şekilde ilişkilendirilen davranışları uygularsınız. BDD’nin avantajlarından biri, davranışları tek bir sözdizimiyle tanımlamasıdır; bu sözdizimi, alan uzmanları, testçiler, geliştiriciler ve müşteriler tarafından kolayca anlaşılabilir.

Bu durum ekip genelinde iletişimi geliştirir. BDD sistemi dışarıdan ele alırken, *test-driven development* sistemin içeriden nasıl çalıştığına odaklanır.

---

## 🧪 Test-Driven Development (TDD)

 *TDD* , testlerin kodunuzun tasarımını ve geliştirilmesini yönlendirmesi anlamına gelir. Önce kodu yazıp sonra testleri yazmazsınız. Önce testi yazarsınız. Sahip olmayı dilediğiniz kod için testleri yazarsınız, ardından bu testlerin geçmesini sağlayacak kodu yazarsınız.

Bu ilk bakışta sezgiye aykırı gelebilir. Henüz yazmadığınız bir kod için nasıl test yazabilirsiniz? Ancak biraz düşünün. Kodunuz için bir tasarımı nasıl yazarsınız? Henüz yazılmamış olsa bile, kodun nasıl davranması gerektiğini tanımlarsınız ve ardından o şekilde davranan kodu yazarsınız. TDD bundan farklı değildir.

Test senaryosu, kodun sahip olmasını istediğiniz davranışı tanımlar. Bu sizi kodun amacına odaklı tutar. Yani kodun ne yapması gerektiğine. Kod yazmaya başlamadan önce bunu kesinlikle tanımlayabilmelisiniz. Aksi takdirde ne yazacağınızı nasıl bilebilirsiniz?

Bu yaklaşım aynı zamanda, istemcilerin kodunuzu nasıl çağıracağını düşünmenizi sağlar.

---

## 🛒 BDD ile Dıştan Bakış Açısı

 *Behavior-driven development* , sistemin davranışını dışarıdan içeriye doğru test eder ve sistemin nasıl davranması gerektiğini ele alır. İç işleyişlerle ilgilenmez.

Örneğin, çevrimiçi bir alışveriş sepetinde olduğunuzu ve ürün sipariş ettiğinizi düşünün. BDD için sorulacak soru şudur: Sepetime bir şey eklediğimde, sepette görünüyor mu? Hangi API’nin çağrıldığı umurumda değil. Hangi verinin aktarıldığıyla ilgilenmiyorum. Sadece sepette görünmesini bekliyorum. Görünüyor mu?

BDD, *integration* ve *acceptance testing* için kullanılır.

---

## ⚙️ TDD ile İçten Bakış Açısı

 *Test-driven development* , sistemin fonksiyonlarını içeriden dışarıya veya aşağıdan yukarıya doğru test eder. Fonksiyonun iç işleyişini test eder.

TDD’de çağrılar önemlidir. Doğru çağrı yapıldı mı? Doğru yanıt döndü mü? Doğru veri ve doğru formatta mı geldi? Bu gibi ayrıntılar önemlidir.

TDD, *unit testing* için kullanılır. Bu nedenle TDD daha düşük seviyeli bir test yaklaşımıdır; BDD ise daha yüksek seviyeli bir test yaklaşımıdır.

---

## 🔁 TDD ve BDD’nin Birlikte Kullanımı

Geliştirme sırasında TDD testleri ile BDD testleri arasında ileri geri döngü kurarsınız ve sonra tekrar TDD’ye dönersiniz. Zıt yönlerden gelirler, ancak birbirlerini tamamladıkları için her ikisine de ihtiyaç vardır.

BDD, sistemi tüketici bakış açısından ele alarak dış davranışlarını test eder. TDD ise sistemin iç fonksiyonlarını test eder. Her bir bileşenin doğru çalıştığından emin olurken, BDD bunların daha üst seviyede birlikte doğru çalıştığını garanti eder.

Başka bir ifadeyle, BDD doğru şeyi inşa ettiğinizden emin olur. Doğru yeteneklere ve davranışlara sahip misiniz? TDD ise şeyi doğru inşa ettiğinizden emin olur. Her özellik, amaçlandığı görevi yerine getiriyor mu?

---

## 🧾 Özet

Bu videoda şunları öğrendiniz:

* BDD, sisteme dışarıdan içeriye odaklanır.
* TDD, sisteme içeriden dışarıya odaklanır.
* BDD, *integration* ve *acceptance testing* için kullanılır.
* TDD, *unit testing* için kullanılır.
* BDD ve TDD, geliştirme yaşam döngüsü boyunca birbirini tamamlar.
* BDD, doğru şeyi inşa ettiğinizden emin olurken, TDD şeyi doğru inşa ettiğinizden emin olur.
