## 🧪 Test Kapsamıyla Test Vakalarını Çalıştırma Demo

Running Test Cases with Coverage laboratuvarına hoş geldiniz. Bu laboratuvarda, *coverage* aracını nasıl kullandığımı göstermek istiyorum; özellikle de *missing coverage report* ile bana test vakası olmayan eksik satırları göstermesini, sonra da gidip o satırlar için test vakaları yazmamızı ve kod kapsamımızı artırmamızı.

Her zamanki gibi, *nose* testlerini çalıştırarak başlıyoruz. Hadi bunu yapalım. Testleri çalıştıracağız ve nerede olduğumuza bakacağız.

Tamam, geçen iki test vakamız var ve ikisi de geçiyor; yüzde 72 kod kapsamımız var ve `models` klasöründeki `accounts.py` dosyasında kapsamı eksik olan bir sürü satır var. Bu, o satırların test edilmediği anlamına geliyor.

Bu satırları çalıştıracak test vakaları yazmak istiyoruz. 26’yı hatırla; IDE ortamımıza geçelim.

---

## 🧰 Test Dosyalarını ve Fixture’ları İnceleme

Bu lab için test coverage klasörünü açacağım, sonra `tests` altına bakacağız ve `test_account.py` dosyasına bakıp elimizde ne var göreceğiz.

Görünüşe göre burada bizi başlatacak biraz kod var. Bazı import’lar var, global bir *account data* değişkeni var ve `setup` metodunda tüm tabloları oluşturuyoruz; sonra da test fixture’lardan `account_data.json` içindeki bir şeyi bu global account değişkenine yüklüyoruz.

Hadi onlara bakalım. `fixtures` klasörüne gidelim, `account_data.json`’a bakalım ve test vakası için yüklenecek bir sürü account verisi var.

`name`, `email`, `phone number` ve `disabled` var. Bu veride bulunan dört attribute bunlar. Bunu bilmek iyi.

Sonra `accounts`’a geri dönüyoruz ve bir *tear down* yaptığını görüyoruz: session’ı kapatıyor, tabloları temizliyor. Bu ne? Rastgele bir sayı oluşturmak için *random range* kullanıyor; bunu `self.rand`’e atıyor ve 0 ile account verisinin uzunluğu arasında rastgele bir sayı oluşturuyor. Bu, rastgele account seçmemize izin verecek.

Ve  *account data* ’ya bakarsanız, bu gerçekten önemli. Buradaki telefon numaralarına bakın: hepsi aynı değil. Bazılarının dahili numarası var, bazıları Avrupa telefon numarası, İngiliz telefon numarası, her türden farklı telefon numarası var. Test vakasına aynı string’i tekrar tekrar göndermemeniz gerçekten önemli. Tabii ki çalışacak. Rastgele string’ler, rastgele veri göndermek istiyoruz. Yani bu iyi. Burada random range iyi bir seçim.

Test vakalarına bakarsak, bir tanesinin *account data* üzerinden dolaştığını, bir sürü account oluşturduğunu, sonra hepsinin oluşturulduğunu assert ettiğini görüyoruz. Sonra tek bir account oluşturuyor; rastgele bir ticket oluşturuyor gibi görünüyor, o rastgele değerden veri alıp oluşturuyor, sonra da oluşturulduğunu assert ediyor.

Tamam, 26. Unutma.

---

## 🧱 `models/account.py` İncelemesi ve Eksik Satırlar

Şimdi `models`’a gidelim. `account.py`’a gidelim ve orada ne var bakalım.

Bu *Account* sınıfı var, *SQLAlchemy* kullanıyor. Bazı attribute’ları var: ID, name, email, phone number, disabled. Sunucunun ürettiği ekstra bir *date join* var; onu test etmeyeceğiz.

Sonra bunu string olarak temsil etmek için bir dizi fonksiyon var; dictionary’ye çevirme, dictionary’den oluşturma; veri tabanı işlemleri için ihtiyaç duyduğunuz create, update, delete gibi şeyler.

Bütün account’ları geri getirmek için `"all"` adlı bir class method’u var ve bir `"find"` class method’u var; böylece bir account bulabiliyorum ve sadece ID’ye göre buluyor.

Şimdi 26. 26. Bundan bahsetmiş miydim? 26. Peki 26 ne? 26, string olarak temsil kısmı. Bu satır ne yapıyor? Bunu string olarak temsil ettiğinizde — ayrıca string fonksiyonu da var, çift alt çizgili string, yani `__str__` — `string` fonksiyonunu tanımlamadığımız için dönen şey olarak bunu kullanacak.

Peki bu nasıl görünecek? Bu şeyleri denemek için Python interpreter’ını açmaktan korkmayın.

Örneğin:

```python
from models.account, import account
```

Account’ı alalım. `a=account` geldi ve `name=foo` diyeceğiz. Doğru, içeri girerken account adını geçeceğiz; sonra `STR, a` deriz.

Gördüğümüz şeyi geri getiriyor: account, angle bracket’lar ve ilginç bir şekilde, `foo` tek tırnak içinde.

Sadece `foo`’yu geri vermiyor. Bu, not edilmesi ilginç bir şey.

Bunu panoma kopyalayacağım; işe yarayabilir. Panoya kopyalayacağız, `test_account`’a geri döneceğiz ve ilk testimizi yazacağız.

---

## 🧾 String Temsili için İlk Testi Yazma (Satır 26)

`def` yazacağız ve sonra `test represent as string` (çünkü string olarak yapacağız), `self`, ve sonra güzel bir docstring vereceğiz:

“Bir account’u string olarak temsil etmeyi test et.”

Peki ne yapmamız gerekiyor? Interpreter’da yaptığım şeyi yapmamız gerekiyor.

Tek yapmanız gereken şunu demek:

```python
account=Account name=foo
```

Bu account’u oluşturacak. Bu yanlış yazıldı. Parmaklarım klavyede neredeydi bilmiyorum. `Name=foo`, bunu aldık.

Şimdi assert edeceğiz:

`self.assertEqual` ile, `STR account` dediğimizde (account’u string’e cast ederek string fonksiyonunu çağırıyoruz), kopyaladığım şeyi geri alacağız. Şimdi yapıştır. Böylece o `foo` geri gelecek.

Bunu kaydedeceğim ve *nose* testlerini çalıştıracağız; interpreter’dan çıkıp nose testlerini çalıştıracağız ve ne elde ettiğimize bakacağız.

Yüzde 74, iyi görünüyor.

Şimdi üç testimiz geçiyor.

---

## 🗂️ `to dictionary` Fonksiyonu için Test (Satır 30)

Şimdi test edilmesi gereken bir sonraki satır 30. `account.py`’a geri dönelim ve 30. satıra bakalım. 30. satır `to dictionary` fonksiyonu. Bu `to dictionary`. Bir account’tan dictionary üretmeyi çalıştırmamışız.

Hadi bunu yapalım.

Sanırım burada bir account oluşturmak için biraz kod “çalabilirim” ve sonra `to dictionary` yapabilirim. O yüzden bunu kesip buraya yapıştıracağım ve adı değiştireceğim: `test to dictionary`.

Docstring’i de biraz daha güzel yapacağız: `test to dictionary`.

Bu iyi bir başlangıç.

Rastgele bir account alıyorum, gidip oluşturuyorum ve sonra:

`result = account.to_dictionary` diyorum.

Şimdi o `result`, bir account’un dictionary temsili olmalı.

Şimdi assert’ler yazmaya başlayabilirim: `self.assertEqual`.

Şunu assert edeceğim: O `result` içinden `name` anahtarını çektiğimde, `account.name`’e eşit olacak.

Bunu hepsi için yapacağım: name, email, phone number, disabled.

Name… sonra `email` = `account.email` ve `phone number` için underscore kullanmak zorundayız: `account.phone_number`, sonra disabled… `account.disable`.

Bunu test etmek için yeterli olmalı; o yüzden testleri tekrar çalıştıralım.

Tüm testler geçiyor ve bir sonraki eksik satırlar 34 ve 35.

---

## 🔁 `from dictionary` Fonksiyonu için Test (Satır 34–35)

Şimdi `account`’a geri dönüyoruz ve 34 ve 35’e bakıyoruz.

34 ve 35 `from dictionary`. `to dictionary`’nin tersi: `from dictionary`.

O halde `from dictionary` yapacak bir test vakası yazalım.

Şununla başlamak istiyorum: Rastgele bir account alan ve oluşturan bu kodu kullanacağım; bana bir sürü yazım tasarrufu sağlayacak. O yüzden bunun adı `test from dictionary`.

“Dictionary’den account oluşturmayı test et.”

Bu testte datayı account’a içeri girerken geçmemize gerek yok. Aslında bu account’u, datayı geçmeden oluşturmak istiyoruz; çünkü veriyi dictionary’den çekmek istiyoruz.

Bu yüzden `account data`’dan veriyi alıyoruz: rastgele bir account, boş bir account oluşturuyoruz ve sonra:

`account.from_dictionary` diyoruz ve data’yı veriyoruz.

Bu, bir account oluşturmanın alternatif bir yolu.

Bu, bir web uygulaması kullanıyorsanız ve bir  *REST API* ’niz varsa ve birileri size *JSON* gönderiyorsa iyi olur; şimdi o JSON’u alıp bir account’u güncellemek istersiniz. Şöyle diyebilirsiniz: “Hey, her şeyi dictionary’den al,” çünkü JSON, Python dictionary olarak temsil edilir.

Şimdi bu bende olduğuna göre, aşağı yukarı daha önce yaptığım assert’lerin aynısına sahibim.

Sadece bu sefer `result` yerine `data`’yı almak istiyorum ve `data.name`’in `account.name`’e eşit olduğunu assert etmek istiyorum.

Aslında teknik olarak bunları ters yazardım; yani `account.name` = `data.name`. Ama eşitlikte hangi taraf olduğunuz fark etmez. Mantıksal olarak daha iyi okunur: “account name artık data name.” Ve “account email artık data email.”

Ama kısalık için bunu kaydedelim ve testimizi tekrar çalıştıralım.

Yaklaşıyoruz. Hissedebiliyorum.

Beş test vakası çalışıyor, yüzde 80 kod kapsamımız var. 45 ve 48 bir sonraki eksik satırlar.

Görüyor musunuz ne yaptığımızı: rinse, wash, repeat.

Peki burada ne var? 45 ve 48… 45 ve 48 `update`. Bu `update` metodu. Şimdi bir account’u güncellemek istiyoruz.


## ♻️ Kod Yeniden Kullanımıyla `update` Testi Yazma

Yine, ben kes-yapıştırın büyük bir savunucusuyum. Şu kod yeniden kullanılabilirliğini bulalım. Biraz kod yeniden kullanımı yapalım. Burada ufak bir kod yeniden kullanımı yapacağız.

Bir account oluşturmak yerine, bu sefer bir account’u güncelleyeceğiz ve  *account update* ’i test edeceğiz. Yani bir account oluşturuyor, veritabanına koyuyor ve orada olduğundan emin oluyor. Sonraki yapılacak şey onu güncellemek: `account.update`, onu bir şekilde değiştirmek.

Peki neyi değiştirmek istiyoruz? İsmi değiştireceğiz ve o veriye baktığımdan oldukça eminim: orada isim olarak `foo` yoktu. `foo` olarak değiştirirsem, başlangıçta `foo` değildi diye oldukça eminim; sonra bir `account.update` yapacağız, bu da veritabanındaki veriyi güncellemelidir.

Şimdi bir assertion yapmamız gerekiyor ama yapmadan önce şunu düşünelim: Eğer sadece account adının `foo` olduğunu assert edersem, bunun veritabanına yazıldığını kanıtlamaz; çünkü ben zaten `account.name`’i `foo` yaptım. Aslında veritabanından geri çekmem gerekiyor.

Ve hatırlayın: *Account* sınıfında bir `find` vardı; bir class parametresi `find`, ID ile account buluyor. O zaman yapmak istediğim şey: bunu veritabanından alıp gerçekten güncellendiğini kendime kanıtlamak.

O yüzden `found` diyeceğiz, çünkü bulacağımızdan eminim.

`found = ...` Şimdi bu bir class çağrısı:

`account.find`

Çünkü elinizde bir account yokken çağırmak istersiniz. Ve `account.ID`’yi geçmek istiyorum.

O ID’ye sahip account’u bul; sonra assertion yapabilirim: `self.assertEqual` ve `found.name`’in `account.name`’e eşit olduğunu assert edeceğim.

Bunu kaydedeceğim. Güzel görünüyor: bir account oluşturuyoruz, onunla ilgili bir şeyi güncelliyoruz. Sadece adı değil, birkaç şeyi daha güncelleyebiliriz. Ama `update` çağırıyoruz ve aslında tüm değişkenleri güncellemek isteyebilirsiniz ki hepsi içeri girdi mi kanıtlayasınız.

Ama hadi çalıştıralım.

---

## 🧨 `update` İçin Sad Path’i Yakalamak (Satır 47)

Tamam, *nose* testlerini tekrar çalıştıracağım ve bu sefer iyi görünüyor ama 47’de ne oldu? 45-48 vardı ve şimdi 47 çirkin yüzünü gösterdi; geri geldi.

O zaman 47. satırda ne oluyor, “update ile bunu düzelttim” sanmıştım.

Geri dönüp `accounts`’a bakacağız, `update`’i arayıp 47’ye bakacağız. Bu bir  *sad path* .

İşte kastettiğim şey bu: *happy path* ve *sad path* test etmelisiniz.

Bu satır:

`if not self.ID`

Eğer ID `None` ise, bir *data validation error* fırlatmalıyım; ID olmadan bir şeyi güncelleyemem. Bu bir sad path ve o satırı çalıştıracak bir test vakası düşünmemiz gerekiyor.

Bu önemli, çünkü ya bu data validation error içinde değişken ikamesi (substitution) vardıysa ve orada bir hata varsa?

O satırı hiç çalıştırmazsanız, bug’ı hiç bulamazsınız, o hatayı hiç bulamazsınız. O yüzden tüm kod satırlarını test etmelisiniz.

Ben sadece bir account oluşturup, ID’yi `None` yapıp, update çağırabilirim. Hadi yapalım.

---

## 🧯 ID Olmadan `update` Testi ve Exception Yakalama

Burada aynı şeyi yapacağız. Hatta bunu daha da kolay yapabileceğimi düşünüyorum. Veritabanında bile oluşturmayacağım, çünkü hiçbir yerde veritabanında olması gerektiği yazmıyor. `update`’i ID olmadan test edeceğim:  *update without ID* , yani ID olmadan update ve test account update without ID.

Bu yüzden herhangi bir veriye ihtiyacım yok, hiçbir şeye ihtiyacım yok. Tek yapmanız gereken: ID’si olmayan bir account üzerinde update çağırmak.

ID’nin `None` olduğundan emin olmak için onu `None` yapacağım:

`Account.ID = None`

Şimdi `account.update` çağırmam mümkün değil. Çünkü `account.update` çağırırsam, *data validation error* fırlatacak ve testlerimi durduracak. Testler patlayacak.

Ama assertion’larda exception yakalamak için bir assertion vardı.

O yüzden burada bir `account.update` yapmak yerine, `assertRaises` kullanacağım: bir exception fırlattığını assert edeceğim ve fırlattığı exception bu  *data validation error* .

Bunu kopyalayıp yapıştıracağım.

Bunun çalışmasının nedeni: Bunu zaten yukarıda import ettik. `DataValidationError` zaten `models`’dan import edildi.

Eğer “data validation error’ın ne olduğunu bilmiyorum” gibi bir şey alırsanız, import etmeyi unutmayın. Bir tane geçecekseniz, ihtiyacınız olacak.

`Raises DataValidationError`

Bir sonraki parametre, çağırmak istediğiniz fonksiyon: `account.update`.

Hepsi bu. `account.update` için başka parametre yok.

Bir account oluşturuyoruz, ID’sini `None` yapıyoruz, sonra update çağırırsak `if ID is None` yolunu geçeceğini ve *data validation error* fırlatacağını assert ediyoruz; bu da `data validation error`’ı yakalıyor ve test vakası geçiyor.

Exception fırlatmış olmanız bu durumda iyi bir şey.

Bunu kaydediyorum ve *nose* testlerini tekrar çalıştırıyoruz ve çalıştı.

Tüm bu test vakaları geçiyor.

---

## 🗑️ `delete` Metodu İçin Test Yazma (Satır 52–54)

Şimdi sonuncusu. 52-54, bunda ne oluyor?

Bakıyoruz ve 52-54 `delete`.

52 bir log mesajı; delete, commit ve o delete’i commit ediyor.

O yüzden bir account’u silen bir test vakası yazmamız yeterli.

Ve yine, bir account oluşturarak başlayacağız ve bunun bir kısmını “çalacağız”.

Bir account oluşturacağız, sonra gidip sileceğiz.

Aslında bir testten diğerine “create account” metodunu çağırabilirsiniz. Bunu sevmiyorum; çünkü birinin davranışını değiştirdiğinizde yan etkiler olabilir ve başka testlerin ona bağımlı olduğunu fark etmeyebilirsiniz. Kodu çoğaltmak benim için sorun değil.

Bir test yazacağız:  *test delete an account* ,  *test account deletion* .

Rastgele bir account alacak, veritabanında oluşturacak, veritabanında olduğunu kanıtlayacak.

Şimdi içeride, o halde `account.delete` çağıracağım.

Sonra bunu kopyalayıp yapıştıracağım ve `account.all` çağırırsam sıfır döndüğünü assert edeceğim.

Bunu kaydedeceğim; son bir kez *nose* testlerini çalıştıracağız ve yüzde 100 başarı.

Hepsini çalıştırdık, tüm test vakaları çalışıyor, yüzde 100 coverage var; *happy path* var, *sad path* var, her şey kapsandı.

Umarım coverage raporuna bakmanın, eksik kod satırlarını görmenin, o satırı bulup “bu satırı çalıştıracak bir test vakasını nasıl yazarım?” diye düşünmenin ne kadar kolay olduğunu görebiliyorsunuz.

Ve çoğu zaman bunlar `if`’ler olacak, `else`’ler olacak, `try-catch` kutusundaki catch’ler olacak. Test yazarken aklınıza gelmeyen o alternatif yollar olacaklar.

Ama bunları yazmanız gerçekten önemli; böylece o hata yakalayıcıların ve alternatif yolların gerçekten çalıştığından emin olursunuz.

Şimdi gidip bunu projelerinizde deneyin. Test vakaları yazın, o test raporunu alın, hangi satırların eksik olduğuna bakın, sonra da o satırları çalıştıracak daha fazla test vakası yazın.
