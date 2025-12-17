# 🏭 Factories and Fakes Demo

## 🧪 Laba Hoş Geldiniz

Factories and fakes labına hoş geldiniz. Bu labda, diğer lablarda üzerinde çalıştığımız account için bir factory, özellikle de bir account factory oluşturma konusunda uygulamalı deneyim kazanacağız. Böylece *JSON* dosyasına önceden kaydedilmiş verileri olan test fixtures kullanmamıza gerek kalmayacak. Bu account’ları test verileriyle anlık olarak oluşturabiliriz.

Her zamanki gibi, *nose* testlerini çalıştırarak başlıyoruz. Zaten lab klasöründeyim ve sadece *nose* testlerini çalıştırıp nerede olduğumuza bakacağım.

```bash
nosetests
```

Gayet iyi görünüyor, burada yapılacak bir şey yok.

## 🔁 Fixtures’tan Factory’ye Geçiş

Şey, aslında bunlar fixtures kullanılarak yapılan testler. Bizim yapmak istediğimiz, fixtures kullanmaktan factory kullanmaya dönüşmek. O hâlde geçiş yapalım ve bu labın içinde ne olduğuna bir bakalım.

Lab 5’i açacağım, factories ve fakes. Gidip bakacağız ve test fixture’ın hâlâ orada olduğunu göreceğiz çünkü kod hâlâ orada. Ama bir de `factories.py` var ve onun içinde bazı bilgiler var. Burada, *faker providers* hakkında daha fazla bilgi edinmek için bazı dokümantasyon bağlantıları bıraktım.

Bunları ve attributes’ları,  *fuzzy attributes* ’ları nasıl kullanacağımızı kullanacağız. Ama size başlangıç olarak burada bir base fuzzy class, bir factory class verdik. Sonra `test_account` içinde, geçen tüm testler burada, ama bu `account.json`’u kullanıyorlar. Bu test fixture’ı kullanıyorlar.

Yani bu labda, sabit verisi olan bir test fixture kullanmaktan, bir factory ile dinamik olarak veri üretmeye geçeceğiz.

## 🏗️ Factory’yi Oluşturma

İlk yapmamız gereken şey, factory’yi oluşturmak. İşte factory class’ımız.

Attributes buraya gelir diye yorum satırı ekledik. Account factory’yi aldık, onu `factory.Factory`’den subclass ettik; “Import factory here” diyor. Bazı *fuzzy choice* ve *fuzzy date* zaten import edilmiş, onları kullanacağız ve  *fuzzy date* ’i oluşturmak için bir `date` var. Modelimizin bu account modeli olduğunu da zaten söyledik.

Account modeline gidip bakalım. `models`’i açacağız, `account`’a gideceğiz ve işte attributes’lar: id, name, email, phone_number. `disabled` bir  *Boolean* , yani bunların hepsi string; id bir int idi, sonra `date_joined` var, o da bir date.

Dolayısıyla bu veriyi uyduracak (fabricate) bir factory oluşturmak istiyoruz. Bu yüzden factory’de, gerçek account class’ında olan attributes’ların aynısı olmalı. Bir id, name, email, phone_number, disabled ve date_joined vereceğiz.

Factory’ye geri döneceğiz ve attributes’lardan bazılarını girmeye başlayalım.

## 🧬 Attributes’ları Tanımlama

### 🆔 ID

ID, veritabanında sadece bir sequence.  *Factory Boy* ’da kullanabileceğimiz bir `Sequence` class’ı var. O yüzden `id` için şöyle diyeceğim: id eşittir `factory.Sequence` ve ona bir Lambda değeri verebiliriz.

```python
id = factory.Sequence(lambda n: n)
```

Lambda’yı doğru yazayım. Tamam, ve sonra `: n`. Bu sadece n üretecek; yani 1, 2, 3, 4, 5. Bu bizim id’miz.

### 👤 Name

Sıradaki name. `name` alanını yapacağız ve  *Factory Boy* ’un içinde bir *Faker* class’ı var. *Faker* sahte veriler oluşturmamızı sağlar; sahte isimler, sahte e-postalar, sahte telefon numaraları.

Eğer burada *faker providers* bağlantısına gidip bakarsanız, hepsi orada listelenmiştir. Gidip tıklayabilir ve tüm farklı provider’lara bakabilirsiniz. Ama hangilerini kullanacağımızı ben söyleyeceğim.

Bu *Faker* class’ı ve Faker, provider adını vererek “name” diyerek isim üretir. `name` bir isim üretir; `first_name`, `last_name` de üretir. `name` sadece bir first name ve last name üretir. Bizim için gereken bu.

```python
name = factory.Faker("name")
```

### 📧 Email

Email var, o hâlde email eşittir… ve bu bir `factory.Faker`. Tuşa biraz erken bastım orada.

Dokümana bakarsanız, gerçekten bir email provider’ı var ve adı `email`. Onu kullanacağız.

```python
email = factory.Faker("email")
```

### 📞 Phone Number

Sonra phone number: `phone_number`. Bunlar account’takiyle aynı olmalı.

Bunları kafadan uyduramayız. Bunların account’la bire bir eşleşmesi gerekir. Phone number ve sonra yine bunun için bir faker kullanacağız; Faker’ın sahte telefon numaraları var ve tesadüfen adı da `phone_number`.

```python
phone_number = factory.Faker("phone_number")
```

Bu sahte telefon numaraları üretecek.

### 🚫 Disabled

Geriye `disabled` kalıyor. Doğru yazdım mı? Disabled eşittir… Şimdi, sahte *Boolean* üreten bir generator yok ama *Boolean* zaten sadece iki değere sahip.

Fark ederseniz, yukarıda *fuzzy choice* import ettik.  *FuzzyChoice* , verdiğiniz listeden rastgele bir seçim yapar. *FuzzyChoice* kullanacağız. Eğer *fuzzy choice* import etmeseydik, `factory.fuzzy.FuzzyChoice` dememiz gerekirdi.

Aynı şekilde, `from factory import fuzzy` gibi import edebilirdik ve o zaman `factory.Faker` yazmak zorunda kalmazdık, sadece `Faker` kullanabilirdik. Nasıl import etmek istediğiniz size kalmış. İhtiyacınız olan bir iki şeyi import edebilirsiniz.

Sequence’i ve Faker’ı import edebilirdik, o zaman `factory` yazmak zorunda kalmazdık; ama bu standart Python işi.

Disabled için *FuzzyChoice* var, onu kullanalım. İşte `FuzzyChoice`. `FuzzyChoice` `choices` diye bir parametre alır. O yüzden `choices` eşittir diyeceğiz ve bir liste vereceğiz. Bir liste açacağız ve sadece iki seçenek var. Bu bir  *Boolean* .

Ya true’dur ya false’dur. Ve bu, true ve false arasında rastgele seçecek; böylece disabled ve disabled olmayan account’ları rastgele üretecek.

```python
disabled = FuzzyChoice(choices=[True, False])
```

### 📅 Date Joined

Sonuncusu `date_joined`. Onun için `FuzzyDate` kullanacağız. Yine, yukarıdaki linke bakarsanız, burada fuzzy attribute provider’ları var. Fuzzy attributes dokümantasyonunu okuyabilirsiniz; `FuzzyDate`, `FuzzyText`, `FuzzyInt` ve float’lar ve her türlü fuzzy şey var.

`FuzzyDate` sadece bir date alır. `datetime`’dan `date` import ettiğimiz için, ona doğrudan bir date verebiliriz.

Bu, temel (base) tarih olacak. Geçmişte, en erken tarih olarak hangi tarihi istiyorsanız onu verirsiniz, sonra o tarihle bugün arasında rastgele tarihler üretir. Bir yıl sonra, bir yıllık tarih aralığını da bunun üstüne eklemiş olacak.

Date ve sonra bir date oluşturacağız: 2008, 1, 1. Oluşturduğum tarih 1 Ocak 2008. Bu kadar. Kaydedeceğim.

```python
date_joined = FuzzyDate(date(2008, 1, 1))
```

## 🧪 Factory’nin Çalıştığını Test Etme

Şimdi sadece test edelim ve çalışıyor mu görelim. Aşağıdaki Python interpreter’a geleceğim ve `python` yazacağım. Labda `python3` yazmanız gerekebilir. Ben bir *virtual environment* içindeyim, bu yüzden sadece `python` yazabiliyorum.

Şimdi bunu import edelim ve çalışıyor mu bakalım. `from` diyeceğim ve `tests.factories` içinden, çünkü test package’ının içinde, sonra `factories` modülü var ve adı `AccountFactory`.

```python
from tests.factories import AccountFactory
```

Şimdiye kadar iyi görünüyor. O yüzden `a = AccountFactory` diyeceğim. `AccountFactory`’yi doğru yazmalıyım, F büyük harfle. `a = AccountFactory` ve şimdi `a.name` diyebilirim ve bir isim alırım. `a.phone_number` ve bir telefon numarası almalıyım. Fikri anladınız. Phone number yazmayı doğru yapabilirsem, işte telefon numarası. `a.email`, vb.

```python
a = AccountFactory()
a.name
a.phone_number
a.email
```

Çalışıyor gibi görünüyor. Yani şimdi yaptığımız şey, factory’yi oluşturmak oldu. Bu ilk adım.

## 🛠️ Testleri Yeni Factory’yi Kullanacak Şekilde Güncelleme

Artık bir factory’miz var, factory çalışıyor gibi görünüyor; şimdi yapacağımız şey testleri bu yeni factory’yi kullanacak şekilde güncellemek.

`testaccount.py`’ye gideceğiz ve bu yeni factory’yi yükleyeceğiz. Yapmamız gereken şeylerden biri, `AccountFactory`’yi import etmek:

```python
from factories import AccountFactory
```

`AccountFactory`’ye ihtiyacımız var. Bunu kullanacağız.

Şimdi, bunu labda yapacağınızdan biraz farklı yapacağım. Labda, bu `account` verilerini tek tek kaldırıp yerine bunu koymanız, bunu kaldırmanız, bir sonrakini kaldırmanız; yani hepsini tek tek dolaşıp değiştirmeniz söylenecek. Bu tamam. Labı öyle yapmalısınız.

Ben biraz farklı yapacağım. Lab, “bunların hepsini değiştir, sonra gidip account referanslarını sil” diyor. Ben tersini yapacağım. Referansları sileceğim ve sonra test case’leri düzelteceğim; sadece alternatif bir çalışma şeklini göstermek için. Ama günün sonunda testler aynı olacak.

Neye ihtiyacım var? Artık bu account’a ihtiyacım yok. Global account’a ihtiyacım yok. Test fixtures’ı artık açmaya ihtiyacım yok. Dolayısıyla JSON’a artık ihtiyacım yok. Yani buna ihtiyacım yok.

İsteseydim random range ile rastgele şeyler oluşturmayı sürdürebilirdim, ama gerçekten random range’e de ihtiyacım olduğunu düşünmüyorum.

Random range’i çıkaracağız ve şimdi ben bu random range’i çıkarıyorum. Tamam, bunu kaydedeceğim.

## 🧪 `nosetests --stop` ile Hata Odaklı İlerleme

Ve şimdi `nosetests` çalıştıracağım ama tabii ki hepsi başarısız olacak. Ama `nosetests --stop` çalıştıracağım; bu ilk başarısız test case’de duracak ve sonra onu düzelteceğiz, bir sonrakini çalıştıracağız, düzelteceğiz, bir sonrakini çalıştıracağız, düzelteceğiz, bir sonrakini çalıştıracağız, düzelteceğiz.

Çünkü gerçek hayatta böyle çalışacaksınız. Gerçek hayatta insanlar size ne yapacağınızı söylemeyecek. Gidip bunun neyi bozduğunu kendiniz bulacaksınız.

Şimdi `nosetests --stop` çalıştıralım. Bu, `nosetests` çalıştırır ve ilk başarısız nosetest’te durur.

```bash
nosetests --stop
```

Bu test “test creating multiple accounts” ve `testaccount.py` dosyasında 37. satırda; “account data bulamıyorum” diyor. Evet, biliyorum, sildim.

## 🔁 “Multiple Accounts” Testini Factory ile Düzeltme

37. satıra gidelim ve diyelim ki, bu for döngüsü. Artık data’ya ihtiyacım yok. Burada bir underscore kullanacağım.

Sonra sadece bir `range` kullanacağım. 10 tane oluşturalım. Sanırım labda 10 tane oluşturuyoruz. Yani `range(10)`.

Şimdi 1-10 veya 0-9 yapacak, ama artık account data yerine `AccountFactory` koyuyorum. Bu account factory’lerini oluşturacak ve artık account’ın uzunluğu yerine sadece 10 diyeceğiz. Sadece 10’unun da veritabanına gittiğinden emin olacağız.

Bunu kaydetmek için Control S, Mac’te Command S yapacağım. Şimdi nosetest’i tekrar çalıştıracağım.

```bash
nosetests --stop
```

Ve şimdi code coverage’ım arttı. Demek ki bir şey çalıştı, ilki çalıştı. Bunları düzelte düzelte ilerleyeceğiz.

## 🧾 “Known Data” ile Account Creation Testini Düzeltme

Sıradaki “test account creation using known data”.

Yani bu. Hadi bunu düzeltelim. Bunu düzeltmek için artık data’ya ihtiyacımız yok. Account artık account factories. Birinden diğerine nasıl geçileceğini gördünüz. Account şimdi account, bana bir account factory ver.

Ve sonra bu kadar; kaydet, tekrar çalıştır, o tamam olmalı.

İki tanesi çalışıyor, yaşasın.

## 🔄 Test Sırası ve “Update Using Known Data”

Sırada “test account update using known data”. Dikkat edin, bu bir sonraki test case değil. Test runner bunları pseudo-random çalıştırıyor. Testlerinizin sırasına bağımlı olmamanızı sağlıyor. Çalıştırdığı sıra, sizin yazdığınız sıradan farklı; bu iyi bir şey.

Tamam, “test accounts update using known data”. Bu bir update. Update nerede?

Bu “test account update using known data”. Şikâyet eden bu. Hadi bunu düzeltelim.

Ve yine, bu çok basit; bunları alıp “AccountFactory, create” diyeceğiz. Diğer her şey iyi olmalı.

Ancak burada bir şeyi değiştireceğim. Şunu yapmak isterim: Ve biliyorum, son labda bunu yapmadım ama, güncellenmediği durumda bu name’in güncellenip güncellenmediğini kontrol etmek isterim.

Bundan emin olmak istiyorum, o yüzden string’i iki tarafa da koyacağım ve sonra tekrar `nosetests --stop` çalıştırıp ne aldığımıza bakayım.

Hâlâ “updating account with known data” çalışmıyor diyor. Bana ne söylüyor? Sanırım doğru olanı seçmedim. O zaman buraya gidelim ve…

Sanırım, bir account sildiğimde onu update etmedim. Bu “test account delete”. O yüzden beni kandırıyor. Bu delete için, ama aynı şey.

## 🗑️ Delete Testini Factory ile Düzeltme

Bu delete için, ama aynı şey. Account data’yı çıkarıyoruz. Test fixtures kullanabildiğimiz her yerde, onun yerine factory koyuyoruz.

Factory ile çalışabildiğimiz her yerde bunu yapabiliriz. Bunu çalıştıracağım, çalıştığından emin olacağım.

Şimdi hepsi çalışıyor ve “deleting account” diyor.

## 🗂️ “Account From Dictionary” Testini Düzeltme

“Test account from dictionary.” Account from dictionary nerede? Bu test case burada.

Yine, random data’ya ihtiyacım yok. Sadece şunu diyebilirim: instantiated account yerine bir account factory instantiate ediyorum.

Ve sonra “Oh, şimdi biraz data’ya ihtiyacım var.” Account equals account factory, belki şöyle yaparız. “account = AccountFactory”. Sonra “data = account.to_dictionary”.

Yani bir account factory oluşturacağız. Account’ın bir `to_dictionary` metodu var. Onu çağırabiliriz; bu artık bize dictionary formatında data verecek ve sonra o data’yı içeri geçebiliriz ve diğer her şey çalışmalı.

Account name, tüm bu şeyler, hepsi eşleşmeli. Hadi deneyelim. Nose testlerini çalıştırıp ne olduğuna bakalım ve çalıştı.

Bir tane daha çalışıyor; from dict şimdi çalışıyor.

## 🆔 “Invalid ID” Testini Düzeltme

Sıradaki invalid ID. Invalid ID olanı bulalım. Bu test case burada.

Bu sefer yine bir account factory oluşturacağız, yani data’ya ihtiyacımız yok: account factory.

Sonra account ID’yi `None` yapıyoruz. Bu, account factory’nin ayarladığı değeri geçersiz kılacak.

Nose testlerini çalıştıracağım ve o da düzgün çalışıyor olmalı.

İyi, hızlı hızlı ilerliyoruz.

## 📘 “Account To Dictionary” Testini Düzeltme ve Kapsam

Sıradaki “test account to the dictionary”. Bu, from’dan önceydi; yani “test account to the dictionary”.

Artık bu data’ya ihtiyacımız yok. Bu sefer bir account factory oluşturmak istiyoruz. Yani AccountFactory.

Sonra geçen sefer yaptığımız gibi yapıyoruz: `result = to_dictionary` ve sonuçların, orijinal account’taki değerlerle gerçekten eşleştiğinden emin oluyoruz. Bana doğru geliyor. Hadi yapalım.

%100 coverage.

## ✅ Fixture’ları Silme ve Ne Zaman Kullanılırlar

Böylece, o test fixture’daki `account_data` kullanımının hepsini düzelttik. Artık bu fixture’ı doğrudan kodunuzdan silip kullanmayı tamamen bırakabilirsiniz.

Ancak bazen bu test fixtures’ı kullanmak iyidir. Bir not gibi iyidir. Bazen gerçekten çok karmaşık veriniz olur. Bu karmaşık veriyi üretmek için bir factory oluşturmayacaksınız.

Test fixtures burada gerçekten parlar. Çünkü JSON içinde JSON içinde çoklu nested objeler veya objeler listeleri vb. olur. Ve bunları API’nizden alırsınız. Statik olarak yüklersiniz, sonra onları taklit edebilir, mock’lar için ve her türlü şey için kullanabilirsiniz.

Ama bizim burada yapmamız gereken tek şey, onları silmek ve sonra tüm account’ları account factories’e dönüştürmekti.

Bu account, foo’da kalınca sorun yoktu çünkü sadece bir account’tan string ürettiğimizde kontrol ediyordu.

Ama diğerlerinin hepsini baştan sona account factory yaptık: account factory, account factory, account factory… Yani gerçek bir account kullanabildiğiniz, data ile yükleyebildiğiniz her yerde, bir account factory kullanabilirsiniz.

## 🎯 Sonuç ve Meydan Okuma

Umarım bu, test case’leriniz için test verisi üretmenin başka bir yolunu göstermiştir. Factories kullanarak, fakers kullanarak, Faker içindeki provider’ları kullanarak… Social security number’lar, kredi kartı numaraları ve her türlü şey için pek çok farklı provider var.

O dokümantasyona gidip bakın, hangi provider’lar var görün.

Meydan okuma şudur: Projelerinizdeki objelerden biri için bir factory oluşturun ve onu sahte verilerle doldurmak için fakers’ı, fuzzy choice’ları, fuzzy date’leri ve benzerlerini kullanın ve sonra bunları test case’lerinizde kullanın.
