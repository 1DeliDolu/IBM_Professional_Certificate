# 🧪 Selenium

Bu videoyu izledikten sonra Selenium’u tanımlayabilecek ve BDD testleri için değerini tartışabilecek, Selenium’u başlatmak için gereken adımları listeleyebilecek ve Selenium kullanarak HTML öğelerini nasıl bulup manipüle edeceğinizi özetleyebileceksiniz. Selenium, web tarayıcısı etkinliğini otomatikleştirmek için kullanılan bir araçlar koleksiyonudur. Temelinde Selenium, Chrome, Firefox, Safari ve Edge gibi popüler tarayıcılar arasında (yalnızca birkaçını saymak gerekirse) birbirinin yerine çalıştırabileceğiniz komut setleri yazmanıza olanak tanıyan bir arayüz olan bir  *WebDriver* ’dır. Yalnızca birkaç satır kodla, tıpkı gerçek bir insanın yapacağı gibi bir web tarayıcısını kontrol edebilirsiniz. Alanlara veri girebilir, alanlardan veriyi geri okuyabilir, bağlantılara tıklayabilir, düğmelere tıklayabilir; gerçek bir kullanıcının yapabileceği her şeyi yapabilirsiniz. Bu kontrol, Selenium’u ortak bir kullanıcı arayüzünü paylaşan birden fazla mikroservisin entegrasyon testleri için mükemmel hale getirir. Selenium, bu testleri manuel olarak çalıştırmak için harcanan saatlerden tasarruf sağlar.

---

## 🧩 Selenium’u Başlatma

Selenium’u başlatmak için önce, kullanmak istediğiniz web tarayıcısının test sistemine kurulu olması gerekir. Chrome ile test etmek istiyorsanız Chrome’un kurulu olması gerekir. Firefox ile test etmek istiyorsanız Firefox’un kurulu olması gerekir. Selenium bir emülasyon değil, gerçek bir web tarayıcısı kullanır; bu nedenle gerçek tarayıcı yazılımını kurmanız gerekir.

Sonrasında, aynı türden bir sürücü örneği (driver) oluşturursunuz; yani Chrome için bir sürücü, Firefox için bir sürücü veya kullanmak istediğiniz tarayıcı hangisiyse onun için bir sürücü. Bu örnekte, Chrome sürücüsü için bazı seçenekler ayarlıyorum. Seçeneklerden biri sürücünün *headless* olmasıdır; yani tarayıcı arayüzünün (GUI) görünmesini istemiyorum. Bir diğer seçenek, testinize müdahale edebilecek *sandboxing* gibi güvenlik özelliklerini kapatır. Ardından bu seçeneklerle bir Chrome sürücüsü oluştururum.

---

## 🔎 Selenium ile HTML Öğelerini Bulma ve Manipüle Etme

Selenium’u kullanmak için önce, HTML sayfasında etkileşime geçmek istediğiniz öğenin hangisi olduğunu belirtmeniz gerekir. Selenium öğeleri; sınıf adı, CSS seçici, ID adı, XPath, bağlantılar, kısmi bağlantılar, metin etiket adları ile bulabilir. Seçebileceğiniz zengin bir seçici setidir. Python için Selenium, bu seçicilerin her biri için fonksiyon çağrılarına sahiptir. Selenium’un ayrıca, web sayfasındaki öğelerin birden fazlasını bulan, sonunda **S** olan bir sürümü vardır:  *find elements by* .

Bu derste, basit tutacağız ve yalnızca `find_element_by_id()` kullanacağız. Bu metotların nasıl kullanılacağına dair bir örneğe bakalım. ID’ye göre bir öğe bulmak için bir adım (step) implementasyonu olan bir fonksiyonla başlarsınız. Bu fonksiyonun iki parametresi vardır. Biri, her Python adımına aktarılan  *context* ’tir. Diğeri ise aranacak metin dizesidir; bu, seçici metodu için ihtiyaç duyduğunuz ek bir parametredir. Sonra `element` adında bir değişken oluşturur ve sürücü (driver) üzerinde *find element by ID* çağrısının sonucunu buna atarsınız; aradığınız öğenin ID adını geçirirsiniz: `customer_ID`.

Ardından, Selenium bu öğeyi bulduğunda ne olacağını belirtirsiniz. Metin dizesinin, öğenin `value` niteliğinde (attribute) bulunması gerektiğini *assert* edersiniz.

Şimdi buna karşılık gelen web sayfası öğesine bakalım. Bu bir metin girişi ( *text input* ) öğesidir. *Find element by ID* çağrıldığında, fonksiyon HTML içinde `customer_ID` ID’sine sahip bir öğe arar ve metin girişi öğesini döndürür. Bu öğe, kodunuzda manipüle ettiğiniz öğe haline gelir. Öğeleri bulmak bu kadar.

Öğeleri ada göre, sınıfa göre, XPath ile veya başka herhangi bir yöntemle bulmak için bir metot kullanabilirdiniz. Ben ID’leri kullanmayı en doğru yöntem olarak buluyorum; çünkü benzersizliklerini kolayca kontrol edebiliyorum ve sayfada öğeleri taşısanız bile değişmiyorlar.

---

## 🛠️ Bulunan Öğeyle Yapılabilecek İşlemler

Bir öğeyi bulduktan sonra, onunla yalnızca içeriğini incelemekten daha fazlasını yapabilirsiniz. O öğeyi temizleyebilir ve ardından `send_keys` fonksiyonunu kullanarak metin dizesini giriş alanına yazabilirsiniz. Test senaryolarınızın çoğu bunu yapar: metin ararlar, metin girerler ve düğmelere ile bağlantılara tıklarlar.

Ayrıca bir değerin gelmesini beklemekten de bahsetmeliyiz. Web arayüzünde test yaparken sık sık gecikme (latency) yaşarsınız; bu yüzden bir şeyin görünmesini beklemeniz gerekir. Neyse ki WebDriver’ın bunu yapmak için bir *web driver wait* fonksiyonu vardır. Ekrandaki kod, web driver wait kullanarak ID’ye göre öğe bulmanın eşdeğeridir. Sürücüye, bir şeyin görünmesi için belirli sayıda saniye beklemesini söyler. Çok fazla kod gibi görünür, ancak gecikme içerebilecek uzak uygulamalara çağrı yaparken çok faydalıdır.

---

## ✅ Özet

Bu videoda, Selenium ile gerçek kullanıcılar için bir web arayüzünün ne kadar iyi çalıştığını hızlıca test edebileceğinizi öğrendiniz. Selenium’u, bir web tarayıcısı kurup o tarayıcı için uygun sürücüyü (driver) örnekleyerek başlatırsınız. Selenium ile HTML’yi manipüle etmek için, bir öğeyi bulma yöntemini seçmeniz ve o öğeyle ne yapacağınızı belirtmeniz gerekir.
