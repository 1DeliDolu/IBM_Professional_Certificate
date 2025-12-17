# 🧩 Adım Dosyaları Yazma

Bu videoyu izledikten sonra, *adım dosyalarının* ne olduğunu açıklayabilecek ve adım yazma iş akışını özetleyebileceksiniz. Daha önce adım dosyalarından bahsetmiştik. Şimdi bir tane nasıl oluşturacağınızı konuşalım.

Adım dosyaları, özellik ( *feature* ) dosyasındaki Gherkin ifadeleriyle eşleşen fonksiyonları içeren Python dosyalarıdır. *Behave* aracı,  **Given** , **When** ve **Then** ile eşleştirme yapmak için kullanılacak bir dizi Python *decorator* sağlar.

Behave, özellik dosyasında bir **Given** ifadesi bulduğunda, adım dosyasında *@given*  *decorator* ’ı ile işaretlenmiş ve eşleşen bir string içeren bir fonksiyon arar. Behave bir eşleşme bulduğunda, o fonksiyonu çalıştırır.

---

## 🧪 Örnek Üzerinden Süreci Anlamak

Süreci açıklamanın en iyi yolu, size bir örnek göstermektir; özellik dosyasıyla başlayalım.

Diyelim ki “ **The pet store catalog service** ” adlı bir Feature oluşturuyorsunuz. Bunu şöyle açıklıyorsunuz:

“As a Pet Store Owner, I need a RESTful catalog service, so that I can keep track of all my pets.”

Makul bir istek gibi görünüyor.

“ **The website is up** ” adlı bir senaryonuz var. Sadece web sitesinin çalışır durumda olup yanıt verip vermediğini kontrol ediyorsunuz. Gherkin ifadeleri şunlar:

“When I visit the ‘Home Page,’ Then I should see ‘Welcome to the Pet Shop,’ And I should not see ‘404 Not Found.’”

---

## 🧷 Gherkin İfadeleriyle Eşleşen Adım Dosyası Yazma

Artık bu üç ifadeyle eşleşen bir adım dosyası yazabilirsiniz.

Önce, Behave’den **when** ve **then**  *decorator* ’larını içe aktarmaya başlarsınız. Özellik dosyasında **Given** anahtar kelimesini kullanmadığınız için burada **Given**  *decorator* ’ını içe aktarmanıza gerek yoktur.

Sonra ilk Python adımınızı yazarsınız. *@when*  *decorator* ’ını, ‘I visit the “Home Page”’ string’i ile kullanırsınız. Bu kod, Behave’in “When I visit the home page.” ifadesi için bir eşleşme ararken, ardından gelen fonksiyonu çağırması gerektiğini gösterir.

Bu adımı uygulamak için, içinde *step_impl()* adlı bir fonksiyon tanımlarsınız;  *context* ’i parametre olarak geçirir ve uygun  *docstring* ’i eklersiniz.

*step_impl()* fonksiyonunu her adımda kullanırsınız çünkü Behave eşleştirme için fonksiyon adlarını kullanmaz; sadece  **given** , **when** ve **then**  *decorator* ’larındaki metin string’ine göre eşleştirme yapar.

---

## 🌐 WebDriver ve Context Değerlerini Kullanma

Bu adımı nasıl uygulamanız gerektiğini düşünelim.

*environment.py* dosyasında *context* içine bir web driver ve bir base URL eklediniz ve bunları sırasıyla *context.driver* ve *context.base_url* olarak adlandırdınız. Şimdi bu değişkenleri kullanma zamanı.

WebDriver, karşılık gelen HTTP fiili isteklerini yapmak için  **get** ,  **put** , **post** ve **delete** metodlarına sahiptir. Bu adımda, base_url ile temsil edilen ana sayfayı ( *home page* ) almak istiyorsunuz. Bu yüzden şu ifadeyi eklersiniz:

```python
context.driver.get(context.base_url)
```

Bu ifade, base URL’yi çağırmak için bir HTTP **GET** isteği yapacak ve ana sayfayı döndürecektir.

Bu adımda herhangi bir doğrulama ( *assertion* ) yapmadığınıza dikkat edin. Test güdümlü geliştirmede ( *test driven development* ), her fonksiyon bir test case’dir ve bir doğrulama içerir. Ancak BDD’de her adım, bir test case’in sadece bir parçasıdır; kendi başına tüm test case değildir.

Bir adım, örneğin bir durumu ( *state* ) kurmak gibi bir hazırlık olabilir ve onu izleyen adım o durum hakkında bir şey doğrular. Bu örnekteki ilk adımda, ifadenin belirttiği aksiyonu uyguladınız: ana sayfayı ziyaret etmek. Sonraki adımlarda ana sayfa hakkında doğrulamalar yaparsınız.

---

## ✅ Başlıkta “Welcome to the Pet Shop” Görünmeli

Bir sonraki adım için, *@then*  *decorator* ’ını şu string ile kullanırız:

‘I should see “Welcome to the Pet Shop” in the title’

Bu adım, senaryonuzdaki ikinci ifadeyle eşleşecektir. Yine *step_impl()* fonksiyonunu tanımlar,  *context* ’i geçirir ve uygun  *docstring* ’i eklersiniz.

Sonra bu adımın uygulamasını tamamlamak için, “Welcome to the Pet Shop” string’inin web driver’ın döndürdüğü sayfanın başlığında ( *title* ) olduğunu doğrularsınız. Bu başlık, *context.driver.title* içinde tutulur.

---

## 🚫 “404 Not Found” Görünmemeli

Son adım için, *@then*  *decorator* ’ını tekrar kullanırsınız. Bunu yaparsınız çünkü özellikte bu ifade **And** anahtar kelimesine sahip ve ondan önceki ifade **Then** içeriyor.

Şu string’i eklersiniz:

‘I should not see “404 Not Found”’

Bu adım, senaryonuzdaki üçüncü ifadeyle eşleşecektir. Bunun için bir fonksiyon tanımlar,  *context* ’i ve uygun bir  *docstring* ’i eklersiniz.

Bu adımı uygulamayı tamamlamak için önce web sayfasının HTML’indeki *body* elementini bulmanız gerekir. Web driver üzerinde *find_element()* fonksiyonunu kullanır ve fonksiyonun ‘body’ adlı tag’i aramasını belirtirsiniz. Bu elementi *element* adlı bir değişken olarak kaydedersiniz.

Sonra “404 Not Found” string’inin *element.text* içinde olmadığını doğrularsınız.

---

## 🔁 Adım Yazmanın Temelleri

Bunlar Behave için adım yazmanın temelleridir. Senaryonuzdaki her Gherkin ifadesi için bir adım yazarsınız, adımı Python’da uygularsınız ve tüm ifadelerin adımları olana kadar tekrarlarsınız.

Bu videoda şunları öğrendiniz:

* Adım dosyaları, Gherkin ifadeleriyle eşleşen adımları içerir.
* Her adım, bir test case’in sadece bir parçasıdır.
* Bir adım dosyası yazmak için, her Gherkin ifadesi için bir adım yazmalı, adımı Python’da uygulamalı ve tekrarlamalısınız.
