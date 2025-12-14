
# 🧭 Davranış Odaklı Geliştirme

Bu videoyu izledikten sonra, *davranış odaklı geliştirmeyi* (BDD) tanımlayabilecek, BDD’nin müşteri beklentilerini nasıl yönlendirebileceğini açıklayabilecek ve BDD’nin temel faydalarını tanımlayabileceksiniz. *Davranış odaklı geliştirme* (BDD), adından da anlaşılacağı üzere, sistemin dışarıdan gözlemlenen davranışına odaklanır. Bu, sistemin içeride nasıl çalıştığının detaylarına odaklanan *test odaklı geliştirmeden* (TDD) farklıdır.

BDD, tüm bileşenlerin birlikte nasıl davrandığını görmek için *entegrasyon testleri* açısından çok uygundur. Sizi “dışarıdan içeriye” düşünmeye zorlar. Başka bir deyişle, yalnızca iş çıktılarıyla en doğrudan ilişkili olan davranışları uygularsınız. BDD’nin avantajlarından biri, davranışları tek bir gösterimle tanımlamasıdır; bu gösterim alan uzmanları, test uzmanları, geliştiriciler ve müşteriler tarafından doğrudan erişilebilir. Bu da ekip içi iletişimi iyileştirir.

---

## 🔁 BDD ve TDD Karşılaştırması

BDD’yi TDD ile karşılaştırırsak, zıt yönlerden geldiklerini görürüz. BDD, sistemin davranışını “dışarıdan içeriye” tanımlar. Sisteme onu tüketen biri gibi bakar. TDD ise fonksiyonları “içeriden dışarıya” test eder. Her bir bileşenin doğru çalıştığından emin olurken, BDD daha üst seviyede hepsinin birlikte çalıştığından emin olur.

Başka bir ifadeyle, BDD doğru şeyi inşa ettiğinizden emin olur. Doğru yetenek setine ve bu davranışlara sahip misiniz? TDD ise şeyi doğru inşa ettiğinizden emin olur. Her özellik, amaçlanan görevi yerine getiriyor mu?

---

## 🧩 BDD İş Akışı ve Araçlar

İş akışı, geliştiriciler, testçiler ve müşterilerin problemin alanını keşfetmesi ve istedikleri davranışı tanımlayan somut örnekler üretmek için iş birliği yapmasıyla başlar. Bu davranışları, birazdan bahsedeceğim *Gherkin* adlı bir dil kullanarak belgelendirirler. Bu, doğal dil temsiline dayanan bir gösterimdir.

Sonrasında ekip, bu örnekleri otomatik kabul testleri olarak çalıştırmak için Python için  **Behave** , Java için **jBehave** veya Ruby için **Cucumber** gibi bir BDD aracı kullanır. Ekip çözüm üzerinde çalışırken, BDD aracı hangi örneklerin uygulanıp çalıştığını söyler ve uygulanmayanlar hakkında uyarır.

Çok geçmeden, elinizde hem yazılımınızın spesifikasyonu hem de testleri olan tek bir doküman olur.

---

## 🥒 Gherkin Sözdizimi

 *Gherkin* , tanıdık **Given... When... Then...** sözdizimini kullanan, okunması kolay bir doğal dil yapısıdır. Hem teknik hem de teknik olmayan kişiler tarafından kolayca anlaşılır. “Gherkin” adının nereden geldiğini merak ediyorsanız, bu sözdizimini kullanan ilk aracın adı **Cucumber** idi; *gherkin* bir turşudur ve turşular salatalıktan yapılır. Araçlar bazen böyle komik isimler üretebilir.

---

## 🧱 Given / When / Then / And Kullanımı

Gherkin sözdizimi şu şekilde kullanılır:

* **Given** bazı bağlam. Bu, test için sahneyi kuran bağlamı veya önkoşulu ayarlar. Amaç, kullanıcı (veya dış sistem) etkileşime başlamadan önce sistemi bilinen bir duruma getirmektir.
* **When** bazı olay gerçekleşir. Bu, neyin yapıldığını tanımlayan ana eylem veya eylemler dizisidir. Bu, sizi başlangıç durumundan yeni gözlemlenen duruma taşır.
* **Then** test edilebilir bir sonuç veya davranış doğrulanır.  **Then** , çıktıları gözlemlemek için kullanılır. Gözlemler, iş değeri veya özelliğin faydasıyla ilgili olmalıdır.
* **And** devamlar için kullanılır: **Given** şu **And** bu… **Then** şu **And** bu… ve benzeri. Daha fazla bağlam, olay veya sonuç eklemenin doğal bir yolunu sağlar.

---

## 🏪 Perakende Mağazası Örneği

Şimdi bir perakende mağazasından bir örneğe bakalım. Bunlara *feature file* veya *feature document* denir ve her dokümanda bir *feature* bulunur; bu feature’ı açıklayan birçok senaryo yer alır. Bu örnekte yalnızca bir senaryo var, ancak tüm permütasyonları kapsamak için elbette daha fazlası olabilir.

Bu feature’ın adı **“Returns go to stock.”** Bu feature, bir müşteri satın aldığı bir ürünü iade ettiğinde sistemin davranışıyla tanımlanır. Dikkat edin, **“As a,” “I need,” “So that”** sözdizimini kullanır; bunu *user story* yazarken kullanırız. Bunu, kabul kriterleri olan bir user story gibi düşünebilirsiniz; kabul kriterleri senaryolardır.

Bu ilk senaryonun adı **“Refunded items should be returned to stock.”** Şöyle okunur:

> Given that a customer previously bought a black sweater from me, And I have 3 black sweaters in stock, when they return the black sweater for a refund, Then I should have 4 black sweaters in stock.

Oldukça basittir. Paydaşlarınız buna bakıp “Evet, iade edilen ürünlerin stoğa dönmesi böyle çalışır.” diyebilmelidir. Ya da “Şu şekilde de olabilir.” diyebilirler. O zaman “Returns go to stock” özelliği için yeni bir senaryo belgelersiniz.

Önemli nokta şu: Paydaşlarınız, sistemin davranışını artık test edebileceğiniz resmi bir sözdiziminde tanımlamanıza fiilen yardımcı olur.

---

## ✅ Dokümandan Test Çalıştırma

Şunu tekrar söyleyeyim: Bu dokümana karşı gerçekten test çalıştırabilirsiniz. **Behave** ve **Cucumber** gibi BDD araçları, bu dokümanı başka bir düzenleme veya manipülasyon olmadan tüketebilir ve sistemin gerçekten bu davranışı sergilediğini kanıtlamak için test vakalarını çalıştırabilir.

Bu, geliştiricinizin yüzünü güldürür. Bu yüzden her user story’ye kabul kriterleri eklerim. Yazdığımız user story’lerde kabul kriterlerini tanımlamak için *Gherkin* sözdizimini kullanırım. Bir sprintin sonunda “done” tanımı üzerinde tartışma olmaz. Bu tartışmasızdır.

Kod ya bu davranışı sergiler ya da sergilemez.

---

## 🎯 BDD’nin Temel Faydaları

BDD, geliştiriciler, testçiler, ürün sahipleri ve diğer paydaşlar gibi ekip üyeleri arasındaki iletişimi iyileştirir. Sistemin nasıl davranması gerektiğine dair daha kesin yönlendirmeye yol açar. Bunu, günlük dile yakın ve TDD araçlarına kıyasla daha düşük öğrenme eğrisine sahip ortak bir sözdizimi sağlayarak yapar.

BDD yaklaşımını hedefleyen araçlar genellikle, BDD *feature specification* üzerinden teknik ve son kullanıcı dokümantasyonunun otomatik üretimini mümkün kılar. Davranışın net bir şekilde görünür olması daha yüksek kaliteli kodla sonuçlanır; bu da bakım maliyetini düşürür ve riski ortadan kaldırır.

Son olarak, BDD kabul kriterleriyle, gerçek geliştirme başlamadan önce user story’lere ve test senaryolarına zaten dönüştürülmüş olursunuz. Böylece testlerin otomasyonu, ürün test edilmeden önce bile test süreçlerini oluşturmaya başlayabilir.

---

## 🧾 Özet

Bu videoda, BDD’nin sistemin davranışına “dışarıdan içeriye” odaklandığını öğrendiniz. Sisteme onu tüketen biri gibi bakar. BDD, herkesin anlayabileceği erişilebilir bir sözdizimi kullanır. BDD’nin temel faydaları arasında iletişimin iyileştirilmesi, ortak bir sözdizimi ve user story’ler için kabul kriterleri bulunur.
