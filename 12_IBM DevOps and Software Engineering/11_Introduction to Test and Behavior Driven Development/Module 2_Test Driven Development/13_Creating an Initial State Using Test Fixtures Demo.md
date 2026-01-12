## 🧪 Creating an Initial State Using Test Fixtures Demo

Creating Initial State Using Test Fixtures’a hoş geldiniz.  *Test fixture* ’lar, tüm testlerinizden önce ve sonra ya da tekil testlerden önce ve sonra veya tüm bir test modülünden önce ve sonra çalışır. Ve veritabanlarını başlatmak, veri dosyalarını başlatmak ve benzeri şeyler için kancalar (hooks) koymak adına harika bir yerdir.

Bu lab’da, bunlardan birkaçında test fixture kullanmaya bakacağız. Ortamı kurduktan sonra her lab’da olduğu gibi, nelerin çalıştığını ve nelerin çalışmadığını görmek için testleri çalıştırmayı seviyorum. Bu lab’da testleri çalıştırıyoruz ve  **sıfır test çalıştı** . Test yok.

Dolayısıyla sıfırdan başlayıp testleri adım adım inşa edeceğiz. Editörümüze geçeceğiz ve  *module three, lab three* ’ü açacağız.

---

## 🔍 Test Ettiğimiz Şeye Bakış

Öncelikle neyi test ettiğimize bakalım.  *models* ’ı açacağım ve bu *account* sınıfını görüyoruz. *Account* sınıfı *SQLAlchemy* kullanıyor.  *SQLAlchemy* ’nin `db.Model`’ından türetiliyor ve bir  *id* ,  *name* ,  *phone number* , *disabled* ve *date joined* alanlarına sahip. Ayrıca üzerinde çalıştırabileceğiniz birkaç metodu var.

Bu sınıflara karşı bazı test vakaları yazacağız:

* Veritabanını başlatmak
* Bir test fixture kullanarak bazı verileri başlatmak
* Sonra bu sınıflara karşı test vakaları yazmak

Şimdi  *tests* ’i açacağız,  *test_account* ’u açacağız.

---

## 📦 Fixtures Klasörü ve JSON Veri Dosyası

*fixtures* klasöründe bir şeye dikkatinizi çekmek istiyorum: `account_data.JSON` diye bir şey var. Bunun içinde zaten bazı *account* verileri bulunuyor. Yüzlerce, binlerce hesap olabilir; ne kadar veriye ihtiyacınız varsa o kadar. Biz de bunu kullanarak account verisini nasıl yükleyeceğimizi öğreneceğiz.

*test_account* dosyasıyla başlayalım. Buraya, ihtiyacınız olacak bazı şeyleri (*JSON* ve benzeri) yükledik. Size global bir `ACCOUNT_DATA` sözlüğü verdik ve `setUpClass`, `tearDownClass`, `setUp`, `tearDown` test fixture’larını olduğu gibi bıraktık. Tabii ki hiç test vakası yok.

---

## 🗄️ setUpClass ile Veritabanını Başlatma

İlk yapmak istediğimiz şey veritabanını başlatmak. Bunun için yukarıda `db` nesnesini zaten import ettik. Gri görünüyor çünkü kullanılmamış. `setUpClass` içine şunu yazacağız:

```python
db.create_all()
```

`setUpClass` tüm testlerden önce **bir kez** çalışır, sonra tüm testler çalışır ve en sonda `tearDownClass` çalışır.

`tearDownClass` için ise şunu yapmak istiyoruz:

```python
db.session.close()
```

Bunun yaptığı şey şu: Veritabanına bağlanır, tüm tabloları oluşturur ve tüm testler çalışmadan önce bunu yapar. Testler bittikten sonra da veritabanı bağlantısını kapatır. Bu yüzden `setUpClass` ve `tearDownClass` veritabanı bağlantıları gibi işler için harikadır.

Şimdi tekrar *nose* testlerini çalıştıracağım; hâlâ test yok ama en azından hata da yok. Bu iyi.

---

## 📥 setUpClass ile JSON Verisini Bir Kez Yükleme

Söylediğim gibi `account_data.JSON` var. Bu da `setUpClass`’a koymak için harika bir şey. Veriyi bir kere yüklersiniz, bir sürü test çalıştırırsınız; her testten önce tekrar tekrar yüklemeye gerek yok.

Şöyle yapacağız:

```python
with open('tests/fixtures/account_data.JSON') as json_data:
    global ACCOUNT_DATA
    ACCOUNT_DATA = json.load(json_data)
```

Burada dikkat edin: “account data burada erişilebilir değil” diye gri uyarı veriyor. Bu yüzden `global ACCOUNT_DATA` demem gerekiyor. Yani “bu global değişkeni değiştireceğim” diyorum, sonra dosyayı açıp veriyi bu global değişkene yüklüyorum.

Tekrar *nose* testlerini çalıştırıyoruz; hata yok.

---

## ✅ İlk Test Vakası: Hesap Oluşturma

Şimdi test vakaları yazmaya başlayacağız. İlk test vakası: bir hesap oluşturmak.

Test fonksiyonları `test_` ile başlar:

```python
def test_create_an_account(self):
    """Test Creating an Account"""
```

Peki account nasıl oluşturulur? Yukarıda sizin için `from models.account import Account` import ettik (henüz kullanmadık). Şimdi şöyle yapacağız: Gerçek bir account oluşturup o diziden veri geçeceğiz.

Size tekrar göstereyim: Bu bir  **array** . Köşeli parantezi görüyorsunuz. Yani `0`, `1`, `2` indeksleri var. İlk elemanı alıp account oluşturarak başlayabiliriz:

```python
account = Account(**ACCOUNT_DATA[0])
```

Bu, hesabı bellekte oluşturur ama veritabanına yazmak için *persist* etmemiz gerekir. O yüzden:

```python
account.create()
```

Bu, *Account* sınıfındaki `create` metodunu çağırır. Dikkat ederseniz sınıfta `to_dict`, `from_dict`, `create`, `update`, `delete` var. Ayrıca `Account.all()` ile tüm hesapları getirme ve bir hesabı bulma yöntemleri de var. Yani sınıfın ne yaptığını anlamanız gerekir.

---

## 🧾 Assertion Yazma ve İlk Hata

Şimdi assertion ekleyebiliriz:

```python
self.assertEqual(Account.all(), 1)
```

Bunu kaydedip *nose* testlerini çalıştırınca bir hata alıyoruz.

Aslında olan şu: `Account.all()` bir liste döndürüyor, ben ise “1’e eşit mi?” diye kontrol ettim. Ben listenin kendisini değil, kaç tane geldiğini bilmek istiyorum. Yani `len()` kullanmam lazım:

```python
self.assertEqual(len(Account.all()), 1)
```

Hatanın çıktısı bana ipucu veriyor. “creating Roberta Shaffer” ve “processing all accounts” gibi log’ları görüyorsunuz; bunlar logger’dan geliyor. Her account oluşturduğunuzda “creating” yazıyor ve account’un adını basıyor. Tüm hesapları istediğinizde de “processing all accounts” yazıyor. Böylece hem log’ları hem de nerede patladığını görüyorsunuz.

---

## 🔁 Testlerin Birbirini Etkilemesi ve Veritabanını Temizleme

Şimdi bunu düzelttikten sonra testleri yeniden çalıştırıyorum ve bu sefer diyor ki: “2, 1’e eşit değil.” Tekrar çalıştırıyorum: “3, 1’e eşit değil.”

Bu bana şunu anlatıyor: Her testten önce veritabanını temizlemiyorum. Bir testin yaptığı, sonraki testi etkiliyor. Yani `setUp`’ta veriyi temizlemem gerekiyor. Burada küçük bir not var:  *truncate tables* . Muhtemelen tabloları “truncate” etmeliyiz.

Buradaki komut şu şekilde:

```python
db.session.query(Account).delete()
```

Bu, `Account` tablosuna bir query çalıştırıp tüm hesapları siliyor.

Şimdi test vakasını tekrar çalıştırıyoruz ve bu sefer test geçiyor.

Yani yaptığım şey şu: `setUp` her testten önce çalışıyor, `tearDown` her testten sonra çalışıyor. Ve biz her testten önce tabloları temizliyoruz; yani tüm account’ları siliyoruz, sonra testi çalıştırıyoruz ki bu hatalar tekrar olmasın.

Tamam, bu ilk testti. Şimdi yapmak istediğimiz şey, bir sonraki testte tüm hesapları yüklemek. Bunun için `test_create_all_accounts` yapacağız ve güzel bir doc string vereceğiz:  *test creating all accounts* .

Şimdi birden fazla hesap oluşturacağımız için bir döngüye ihtiyacımız var. Şöyle diyeceğim:

```python
for data in ACCOUNT_DATA:
```

Bu, o küçük sözlüklerin (dictionary) her birini tek tek getirecek. Yani `for data in ACCOUNT_DATA` ile aslında aynı şeyi yapabiliriz.

Şunu yazacağım:

```python
account = Account(**data)
```

Bunu yapmasının sebebi şu: Bunu *name-value* çiftleri olarak geçirir; çünkü *SQLAlchemy* nesnesine doğrudan bir dictionary veremezsiniz, ne yapacağını bilemez. Ama `**data` koyunca, dictionary’yi  *name-value pairs* ’a dönüştürür ve SQLAlchemy *name-value pairs* ile ne yapacağını kesinlikle bilir. Alanları set eder ve veritabanına yazar.

Şimdi elimizde `account` var ve:

```python
account.create()
```

Bu da hesabı veritabanında oluşturur. Böylece tüm hesapları oluşturmuş olduk.

---

## ✅ Dinamik Assertion ile Doğrulama

Şimdi öncekiyle aynı türde bir assertion yazabiliriz. Kısalık için bunu kopyalayıp yapıştıracağım. Bu sefer `1` değil, `ACCOUNT_DATA`’nın uzunluğu olmalı:

```python
self.assertEqual(len(Account.all()), len(ACCOUNT_DATA))
```

Dikkat edin, bunu hard-code etmedim. Çünkü `account_data`’yı güncelleyip daha fazla hesap eklersek, “5 hesap” veya “10 hesap” diye sabit bir sayı yazmak testleri bozar.

Bu yüzden mümkün olduğunca hesaplayarak, veriyi dinamik tutmak istersiniz.

Şimdi bunu çalıştıracağız ve umarım iki test de çalışacak. Evet, ikisi de çalıştı.

---

## 📦 Fixture ile Veri Yükleme Mantığı

Bu sadece şunu göstermek içindi: JSON formatındaki veriyi bir Python dictionary koleksiyonu olarak yüklüyorsunuz. Bunu class seviyesinde sadece bir kez yapmanız yeterli.

Ayrıca veritabanı bağlantısını da bir kez açtım ve tüm testlerin sonunda session’ı kapattım.

Ve her testten önce, tüm hesapları silme işlemi yaptım. Burada bir hatırlatma görüyorum: “remove this session”. Sanırım burada bir `db.session.remove` var. Eğer yoksa ekleyip kaldıracağız; hadi bakalım çalışıyor mu diye kontrol edelim. Çalışıyor; demek ki doğru olan `db.session.remove`’muş. Bu, her test case çalıştığında session’ı temizlemeye yardımcı oluyor.

Yani her test koşusunda session’ı “clear” etmek için bunu kullanıyoruz.

Tekrar özetlersek: Testleri bir fixture’dan bir array’e veya dictionary’ye (nasıl isterseniz) yükledik. Sonra bu account verisini testlerde kullandık.

---

## 🎲 Rastgele Veri Seçimi Fikri

Bunu kısayoldan yaptım ama aynı şeyi şöyle de yapabilirdim: `data = ACCOUNT_DATA[0]` ya da belki random bir sayı ile farklı bir hesabı seçebilirdim. Sonra burada `data`’yı nasıl istiyorsanız öyle geçirirdiniz ve veriyi inceleyebilirdiniz.

Hatta rastgele sayılar üretiyor olabilirdiniz ve rastgele bir kayıt seçmek fena bir fikir değildir. Aslında `random range`’i buraya koyduğumuzu sanmıştım ama koymamışız. Ben bunun için `random range` kullanırım; şöyle derim: `0`’dan `ACCOUNT_DATA` uzunluğuna kadar bir random seç, sonra bana o kaydı getir.

Böylece her seferinde farklı bir account gelir. Bu test için genelde çok iyidir çünkü her seferinde farklı veri geldiğinde, bazen test ara sıra fail eder. O zaman gidip “hangi kayıt fail ettirdi?” diye bakmanız gerekir; çünkü sürekli aynı veriyle test ederseniz, hep çalışır.

Bu yüzden her zaman taze test verisine sahip olmak önemlidir.

---

## 🧹 Sonuç: Fixture ile Yükle, Test Et, İzole Et

Tamam, işte test fixture’ları bu şekilde kullanabilirsiniz. Özellikle de fixture’larla veri yükleme: Testlerinizden önce veritabanınızı, ihtiyacınız olan account’lar veya herhangi bir bilgiyle doldurabilirsiniz.

Ve unutmayın: Her test arasında tablolarınızı temizleyin veya bağlantılarınızı temizleyin ki bir test diğerini etkilemesin.
