# 🧩 Test Fixtures

Bu videoyu izledikten sonra şunları yapabileceksiniz:

* Test fixture’larını kullanmanın amacını özetlemek
* Test fixture’larının hangi durumlarda faydalı olduğunu belirlemek
* Bir modüldeki her test için uygun bir başlangıç durumunu kurmak üzere test fixture’larını nasıl kullanacağınızı açıklamak

Bir testi çalıştırmadan önce sistemin hangi durumda olduğunu nasıl bilirsiniz? Testleriniz, çalıştırmadan önce veritabanında belirli verilerin olduğunu varsayıyorsa ne olur? Bunu nasıl ele alırsınız? Bu soruların hepsinin cevabı test fixture’larını kullanmaktır.

Test fixture’larını, testleri çalıştırmadan önce ve sonra bilinen bir başlangıç durumu oluşturmak için kullanırız. Test fixture’ları ile, bir test (veya testler paketi) çalıştırılmadan önce test ortamının nasıl göründüğünü tanımlayabilir ve testten sonra ortamı tekrar tanımlayabiliriz. Bu özellikle testleri yalıtılmış şekilde çalıştırabilmemizi sağlar.

Her testten sonra sistemin sıfırlandığından emin oluruz; böylece bir testte yapılan değişiklikler başka bir testin davranışını etkilemez. Bu sıfırlama, tekrarlanabilir sonuçlar elde etmemizi sağlar; çünkü bir test her çalıştırıldığında aynı başlangıç durumundan çalıştığını biliriz.

---

## 🧪 Test Fixture’larının Kullanım Alanları

Bazı faydalı test fixture örnekleri; veri hazırlama ve sahte nesneler ( *fake objects* ) ya da mock nesneler ( *mock objects* ) kurma veya oluşturmadır.

Sahte ve mock nesnelere ilerideki bir derste daha derinlemesine gireceğiz; şimdilik onları “test mankenleri” veya “yerine geçenler” olarak düşünün. Test sırasında gerçek nesneler mevcut olmayabilir; bu nedenle bunları bir test fixture ile oluşturabilirsiniz.

Başka bir kullanım alanı, veritabanını belirli ve bilinen bir veri setiyle yüklemektir. Diyelim ki müşteri hesaplarının manipülasyonunu test edeceksiniz. Bu, veritabanında bazı müşterilerin bulunduğunu varsayabilir. Test fixture kullanarak veritabanını örnek müşterilerle doldurabilirsiniz.

Fixture’lar ile ilgili akılda tutulması gereken önemli bir özellik, her zaman aynı durumdan başlamalarıdır. Bu durumda veritabanı, her test için tam olarak aynı müşteri verilerini içerir. Bu, örneğin bir testte bir müşteriyi silmenin, başka bir testte o müşteriyi bulmayı etkilememesini sağlar.

Ayrıca, testlerinizin gerekirse bulabilmesi için belirli ve bilinen bir dosya kümesini kopyalamak üzere de test fixture’larını kullanabilirsiniz. Testlerinizi çalıştırmak için doğru ortamları kurmak adına yapmanız gereken her şey test fixture’ları ile gerçekleştirilebilir.

---

## 🧰 PyUnit’in Sağladığı Altı Test Fixture’ı

PyUnit’in bize verdiği altı test fixture’ına bakalım.

### 🧱 Modül Seviyesi Fixture’lar

* **`setUpModule`**
  Tüm Python modülünden önce bir kez çalışır. Unutmayın: modül sadece bir Python dosyasıdır. Bu durumda, testlerinizi içeren dosyadır. Modül birden fazla `TestCase` sınıfı içeriyorsa, bu sınıflardan herhangi biri çalışmadan önce bir kez çalışır.
* **`tearDownModule`**
  Modülün sonunda, tüm testler çalıştıktan sonra bir kez çalışır. Tüm testler tamamlandıktan sonra tek seferlik temizlik yapmak için bu fixture’ı kullanırız.

### 🏛️ Sınıf Seviyesi Fixture’lar (TestCase)

* **`setUpClass()`**
  Sınıftaki tüm testlerden önce bir kez çalışır.
* **`tearDownClass()`**
  Sınıftaki tüm testler çalıştıktan sonra bir kez çalışır.

### 🧩 Örnek (Instance) Seviyesi Fixture’lar

* **`setUp()`**
  Her testten önce çalışır.
* **`tearDown()`**
  Her testten sonra çalışır.

---

## 🔁 Çalıştırma Sırası

Test modülünüzde bu fixture’ların hepsini kullanırsanız, test runner şu sırayla çalıştırır:

Önce `setUpModule`, sonra `setUpClass`, sonra `setUp`; ardından bir testi çalıştırır. Testten sonra `tearDown` çağrılır.

Aynı test case içindeki her ek test için test runner `setUp`, sonra bir sonraki test, ardından tekrar `tearDown` çalıştırır.

O test case içindeki tüm testler çalıştıktan sonra test runner `tearDownClass` yürütür. Daha fazla `TestCase` sınıfı varsa, test runner onları çağırır ve en sonunda bittiğinde bir kez `tearDownModule` çalıştırır.

---

## 🧾 Kod Örneği: Kullanıcı Hesaplarını Test Etmek

Kullanıcı hesaplarını test etmek için bir kod örneğine bakalım.

Önce, `TestCase` alt sınıfı olan `TestAccountModel` adında bir sınıf bildirerek başlarız.

Sonra, sınıf metodu `setUpClass()` ile bir veritabanı bağlantısı kurarız. Veritabanı bağlantıları genellikle kurması pahalıdır; bu yüzden her test case için bir bağlantı kurmak istemeyiz. Bu, bu sınıftaki tüm testler için veritabanına yalnızca bir kez bağlanacaktır.

Ardından karşılıklı sınıf metodu `tearDownClass()` tanımlanır; bu metot veritabanı bağlantısını kapatır. Bu, tüm testler çalıştıktan sonra veritabanı bağlantısının kapatılmasını sağlar.

Sonra, her testten önce çalışan `setUp()` instance metodunu kullanarak tüm tabloları düşürür ve yeniden oluştururuz. Eğer tabloları truncate ederek veri kaldırmanın başka bir yolu varsa, onun yerine bunu kullanmak isteyebilirsiniz.

Elbette, bu testlerin veri kaldırıp yeniden oluşturmanın sorun olmadığı bir test veritabanına bağlandığını umuyoruz. Bunu yalnızca adanmış bir test veritabanıyla kullanırdım.

Son olarak, her testten sonra çalışan `tearDown()` karşılıklı instance metodunu tanımlarız; bu metot mevcut veritabanı oturumunu kaldırır ve tüm tabloları düşürür. Bu, her test çalışmasından sonra veritabanı oturumunun kaldırılmasını ve tabloların temizlenmesini sağlar.

Bu, PyUnit’te test fixture’larını kullanarak her testin bir veritabanı bağlantısına ve testlere başlamadan önce temiz bir tablo setine sahip olmasını sağlamanın sadece bir örneğidir.

---

## 📦 Fixture Klasörü ile Bilinen Veriyi Yüklemek

Bazen testleri çalıştırmadan önce bilinen bir veri setini yüklemeniz gerekir. Benim yapmayı sevdiğim şey şu.

Test case’lerin saklandığı test klasörünüzün altında `fixtures` adında bir klasör oluşturmayı severim.

Bu klasör adının özel bir anlamı yoktur; yalnızca içindeki dosyaların test fixture’larıyla ilgili olduğunu geliştiricilere işaret eder. Sonra bu klasörün içine veri dosyalarımı koyarım.

Bu örnekte `account_data.json` adında bir dosyam var; bu dosya, bir hesap oluşturmak için gereken veriyi JSON formatında temsil eder.

Bu klasörü test kodumuzda nasıl kullanabileceğimize bakalım.

Önce veriyi tutmak için global bir sözlük tanımlayarak başlarız. Global olmak zorunda değil; sınıf verisi ( *class data* ) da yapabilirsiniz; fakat bu örnekte global yaptık.

Sonra, sınıf metodu `setUpClass()` ile veriyi yükleriz.

Öncelikle `ACCOUNT_DATA` sözlüğünü değiştirmek üzere olduğumuzu belirtmemiz gerekir. Ardından “`test/fixtures/account_data.json`” adlı JSON veri dosyasını açar ve `ACCOUNT_DATA` sözlüğüne yükleriz.

Bu noktada artık testlerde hesap oluşturmak için kullanabileceğimiz global bir veri sözlüğümüz vardır.

Son olarak, bu veriyi kullanarak bir hesap oluşturan bir test yazarız.

`ACCOUNT_DATA` sözlüğünü geçirerek bir `Account` nesnesi oluştururuz; böylece sınıfı veriyle doldururuz. Sonra bunu veritabanına kaydeder ve tüm `Account` kayıtlarını alarak var olduğunu doğrularız; ardından bu koleksiyonun uzunluğunun 1 olduğunu assert ederiz; yani az önce oluşturduğumuz tek hesap.

Test verisini fixture’lar ile yüklemek çok kullanışlıdır; özellikle veri karmaşıksa ve başka türlü oluşturmak zor olacaktıysa.

---

## ✅ Video Özeti

Bu videoda şunları öğrendiniz:

* Test fixture’ları, her testten önce ve sonra bilinen bir başlangıç durumu oluşturur.
* Test fixture’ları birçok test senaryosu için faydalıdır.
* Test fixture’ları üç ayrıntı seviyesinde çalışır: modül, test case ve test.
