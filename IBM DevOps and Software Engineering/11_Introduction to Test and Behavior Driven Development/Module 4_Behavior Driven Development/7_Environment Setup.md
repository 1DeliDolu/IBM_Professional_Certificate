# 🧰 Ortam Kurulumu

Bu videoyu izledikten sonra, Behave’deki her bir test fikstürünü açıklayabilecek ve bir test ortamı kurma sürecini ve Behave’de test fikstürlerini tanımlamayı özetleyebileceksiniz.

Behave, test yürütme ortamını kontrol etmek için özellik senaryolarından, adımlardan veya etiketlerden önce ya da sonra çalıştırabileceğiniz bir dizi test fikstürüne sahiptir. Gelin bu fonksiyonların her birine bakalım.

---

## 🧩 Genel Fikstürler

Bir test fikstürü seti `before_all` ve `after_all` fonksiyonlarını içerir. İsimlerinden de anlaşılacağı gibi, bu fikstürlere koyduğunuz herhangi bir kod tüm özelliklerden önce bir kez çalışır ve ardından tüm özelliklerden sonra tekrar çalışır.

Bu set, Selenium gibi araçlardan web sürücülerini kurmak için idealdir. Selenium sürücüleriyle testlerinizi gerçekleştirmek için gerçek bir tarayıcı kullanabilirsiniz.

Bu set ayrıca, tüm adımların erişebileceği `context` değerlerini oluşturmak ve Behave tüm özellikleri işledikten sonra herhangi bir sürücüyü kapatmak için de idealdir.

---

## 🗂️ Feature Seviyesi Fikstürler

Bir sonraki nokta `before_feature` ve `after_feature` fonksiyonlarıdır. Bu fonksiyonlar her bir feature’dan önce ve sonra çalışır.

Her bir feature parametresi,  *feature class* ’ının bir örneğidir. Birden fazla feature kullanıyorsanız, bu set her feature çalışmadan önce ve sonra temiz bir ortam hazırlamak için ideal olabilir.

---

## 🎬 Senaryo Seviyesi Fikstürler

Bir sonraki kontrol seti `before_scenario` ve `after_scenario` fonksiyonlarıdır. İsimlerinden tahmin edeceğiniz gibi, bu fonksiyonlar her bir senaryodan önce ve sonra çalışır.

Senaryo,  *scenario class* ’ının bir örneği olarak parametre geçilir. Bu fonksiyonlarla, her senaryonun çalıştırma ortamı üzerinde daha da ayrıntılı kontrol sağlayabilirsiniz.

---

## 👣 Adım Seviyesi Fikstürler

Sonra `before_step` ve `after_step` vardır. Bunlar her adımın öncesinde ve sonrasında çalışır.

Parametre olarak geçen adım,  *step class* ’ının bir örneğidir. Bu çok ayrıntılı bir kontroldür. Ben hiçbir zaman her adım arasında ortamı değiştirme ihtiyacı duymadım, ama ihtiyacınız olursa yapabilirsiniz.

---

## 🏷️ Etiket Seviyesi Fikstürler

Ortamı kontrol eden bir son fonksiyon seti de `before_tag` ve `after_tag`’dir. Bu kursta etiketleri ele almıyorum çünkü etiketleme daha gelişmiş bir fonksiyondur; bu nedenle bu fonksiyonları yalnızca kısaca tartışacağım.

Feature dosyanızın bölümlerini bir adla etiketleyebilirsiniz ve ardından bu fonksiyonlar, belirli bir adla etiketlenmiş bölümden önce ve sonra çalışır. Behave, etiketleri feature dosyasında bulundukları sıraya göre çağırır.

---

## 🗃️ environment.py ile Ortam Tanımlama

Behave ortamınızı `environment.py` adlı bir dosyada kurarsınız ve test fikstürlerinizi burada tanımlarsınız. `before_all` ve `after_all` fonksiyonlarını kullanan basit bir `environment.py`’ye bakalım.

Önce import’larınızla başlarsınız.

Ortamdan herhangi bir yapılandırma parametresini import etmeniz gerekir. Bu yüzden önce OS paketinden *get environment* fonksiyonunu import etmelisiniz. Bu örnekte ayrıca test sırasında uygulamanızın kullanıcı arayüzünü manipüle etmek için Selenium kullanacaksınız. Sonraki import Selenium paketinden `WebDriver`’dır.

---

## 🌍 Ortam Değişkenleri ve Global Değerler

Sonra ortamdan almak istediğiniz global değişkenleri tanımlamalısınız. Bu örnekte, Selenium’un UI’dan bir yanıt bekleme süresini kontrol eden `wait_seconds` adlı bir ortam değişkeni alırsınız.

Ayrıca test edilen sistemin konumunu söyleyen `Base_URL` adlı bir ortam değişkeni de alırsınız.

Base URL ortam değişkenini değiştirerek, Behave’i yerel bilgisayarınıza veya test etmek istediğiniz herhangi bir uzak bilgisayara yönlendirebilirsiniz.

---

## 🧱 before_all Fonksiyonu

Tanımladığınız ilk fonksiyon `before_all`’dır ve Behave herhangi bir feature dosyasını işlemeden önce çalışır.

Bu fonksiyonun `context` olarak geçen bir parametresi olduğuna dikkat edin. Bu context, test paketinizdeki her adıma aktarılır. Dolayısıyla bu context’e atadığınız herhangi bir şey tüm adımlar tarafından kullanılabilir olacaktır.

Context içinde yerinde tanımladığınız ilk öğe `WebDriver`’dır. Seçenekleri *Headless Chrome driver* kullanacak şekilde ayarlarsınız, ancak Firefox ya da Safari sürücüsü veya diğer pek çok sürücüden herhangi birini de kullanabilirdiniz.

Tek ön koşul, Behave’i çalıştıran test sisteminde web tarayıcısının kurulu olmasıdır.

Bu sürücüyü context’te `driver` adlı bir değişkene atarsınız. Yine, bu context her adıma aktarılır; böylece tüm adımlar `context.driver`’a referans vererek WebDriver’a erişebilir ve bunu UI üzerindeki eylemlerini sürmek için kullanır.

---

## ⏱️ Bekleme Süresi ve Implicit Wait

Ardından `wait_seconds` global değişkenini context’e kaydedersiniz. Bu şekilde tüm adımlar UI’ın yanıt vermesi için ne kadar bekleyeceklerini bilmek üzere buna erişebilir.

Sonra WebDriver üzerinde varsayılan olarak bu kadar saniye *implicit wait* yapması için bir attribute ayarlarsınız.

---

## 🔗 base_url Tanımlama

Son olarak context içinde `base_url` adlı bir değişken oluşturur ve onu ortamdan aldığınız global `base_URL` değişkenine ayarlarsınız.

Bu şekilde her adım, testi hangi URL’ye karşı çalıştıracağını bilecektir.

Tüm bu Python ifadeleri, Behave herhangi bir feature dosyasını işlemeden önce bir kez çalışır. Birlikte, bu ifadeler BDD testlerini çalıştırmak için başlangıç ortamını kurar.

---

## 🧹 after_all Fonksiyonu

Tanımladığınız son fonksiyon `after_all`’dır ve tek bir satır koda sahiptir: `context.driver.quit`.

Bu fonksiyon, tüm testler tamamlandıktan sonra web tarayıcısına kapanmasını söyler ve böylece sonrasında bellekte birden fazla web tarayıcısı çalışır halde bırakmadığınızdan emin olursunuz.

Açıkça, bu dosyaya daha fazla test fikstürü ekleyebilir ve onların her feature, senaryo, adım veya etiket öncesi ve sonrası çalışmasını sağlayabilirsiniz. Bu tek dosya `environment.py`, ihtiyaç duyduğunuz ayrıntı seviyesinde ortamı kontrol eder.

---

## ✅ Video Özeti

Bu videoda, Behave’in feature’lardan, senaryolardan, adımlardan veya etiketlerden önce ya da sonra çalıştırabileceğiniz bir dizi test fikstürüne sahip olduğunu öğrendiniz.

Behave ortamını kurmak için `getenv()` ve diğer gerekli modülleri import edersiniz. Ortamdan global değişkenleri tanımlarsınız ve test fikstürlerinizi tanımlarsınız.
