# 🧪 Running Tests with Nose Demo

Running Test with Nose Demo lab’ine hoş geldiniz. Lab’da neler beklemeniz gerektiğini göstermek için sizinle uygulamalı bir çalışma yapmak istiyorum; ama daha önemlisi, bu kurs için neden test çalıştırıcısı olarak  *nose* ’u seçtiğimi açıklamak istiyorum. Python’daki varsayılan test çalıştırıcısını göstererek başlayacağım.

Şu anda bir sanal ortamdayım. Zaten lab klasöründeyim. Sadece Python’u çalıştıracağım. Siz Python 3 çalıştırmak zorunda kalabilirsiniz. Lab yönergeleri hangisini kullanacağınızı söyleyecek.

```bash
python -m unittest
```

Bu komut bir sürü nokta döndürüyor. Yani 11 test çalıştırdı, nokta, nokta, nokta. Her test bir nokta. Testlerden biri başarısız olsaydı, hata için bir “E” görürdünüz ve ardından neyin başarısız olduğuna dair bir açıklama alırdınız. Pek heyecan verici değil.

Bir `-v` ile biraz daha ayrıntılı çıktı alabilirim ve o zaman çok fazla çıktı verir. Ama burada olan şey, tekrarlar görüyorum. Aslında bu ikisi aynı test vakasını raporluyor: *area of a triangle* fonksiyon olarak ve ardından docstring.

## 📁 Test Dosyalarına Bakış

Bu testlerde neler olduğuna bakalım. Lab klasörünün altına girersem, bu bizim ilk lab’imiz ve testlerin olduğu `test_triangle.py` dosyasına bakarsam, tüm bu docstring’lerin turuncu olduğunu fark edersiniz. Ve bunlar (docstring’ler) görünüyor, ayrıca fonksiyon adları da görünüyor.

Bu çok yardımcı değil. Çok daha iyisini yapabiliriz; bu yüzden *nose* denen bir şeyi kuracağız.

## 🧰 Nose Kurulumu

Ekranı temizleyeyim. Bunu sıfırdan alıp nose’daki tüm eklentileri adım adım kurmak istiyorum.

```bash
pip install nose
```

Lab’a girdiğinizde `pip3 install` kullanmanız gerekebilir. Yönergeler size bunu söyleyecek. `pip install nose` yazarsınız ve nose’u kurar.

Artık nose çalıştırıcısı olan `nosetests`’i çalıştırabilirim. Yani `nosetests` yazarım ve evet,  *unittest* ’e benziyor. Ama aslında farklı davranması için birkaç seçenek vermeniz gerekiyor. Normalde sadece *unittest* gibi davranır.

## 🔎 Nose ile Ayrıntılı Çıktı

Ama `-v` yaptığımda farkı görürsünüz. Şimdi sadece docstring’leri görüyorum; bunlar fonksiyonun ne yaptığını söyleyen güzel İngilizce cümleler, daha şifreli fonksiyon adını kullanmak yerine. Bunu seviyorum, ama daha iyisini yapabiliriz.

## 🎭 Pinocchio Eklentisi ile Spec Çıktısı

Sonra *Pinocchio* denen bir eklenti kuracağız.

```bash
pip install Pinocchio
```

*Pinocchio* bize iki şey verecek: çıktıyı RSpec’e daha benzer hale getirip bir spesifikasyon formatı sağlayacak ve ayrıca bu spesifikasyonu renklendirmemize izin verecek.

`nosetests` ile başlayalım. Şimdi `--with-spec` diyeceğim. Bastığımda, pardon, `nosetests` çoğul, `with-spec`.

```bash
nosetests --with-spec
```

Bunu yaptığımda güzel bir çıktı alıyorum. Bir başlık alıyorum. Artık her bir test paketi (Python dosyalarındaki test sınıflarındaki test vakaları), kendi başlığı olan küçük bir bölüm gibi görünecek ve altında tüm testler listelenecek; tek uzun bir test satırı yerine.

## 🎨 Spec Çıktısına Renk Ekleme

Şimdi buna biraz renk ekleyeceğiz. Ekranı temizleyeceğim ve `with-spec --spec-color` yapacağım; bu da spec çıktısını renklendirir. Buraya bir boşluk koy. Böylece doğrudan güzel bir red-green refactor görürüm.

```bash
nosetests --with-spec --spec-color
```

Bunlardan biri başarısız olsaydı kırmızıya dönerdi. Şimdi bunun nasıl göründüğünü göstermek için bir tanesini bilerek bozalım. Sıfır tabanlı bir üçgenin alanının sıfır olması gereken yere bakacağım. Onu 5 yapacağım; bu yanlış cevap olacak.

Şimdi bunu tekrar çalıştıracağız; `with-spec` ve `with-color` ile. Elbette, işte kırmızı test vakam. Yani başarısız olanlar için güzel kırmızı test vakaları alıyorum ve tabii sonra açıklamayı da alıyorsunuz: assertion, `zero is not equal to 5`. O yüzden bunu tekrar çalışacak şekilde geri değiştireceğiz.

Ama bu red-green refactor fikrini anladınız.

## 📈 Coverage Kurulumu ve Çalıştırma

Şimdi yapmak istediğim bir sonraki şey şu: Kodunuzun ne kadarının test vakaları tarafından kapsandığını anlamak önemli. Bu yüzden coverage aracını kurmak ve onu çalıştırmak istiyorum.

```bash
pip install coverage
```

Coverage aracı bize küçük bir coverage raporu verir. Şimdi buna `with-spec with-color --with-coverage` ekleyeceğim. Bu, testler çalıştığında bir coverage raporu da üretir.

```bash
nosetests --with-spec --spec-color --with-coverage
```

Gördüğünüz gibi burada coverage raporu var. `triangle.py` dosyasının 10 statement’ı var. Hiçbiri kaçırılmamış, yüzde 100 kod kapsamı.

Coverage’ın izin verdiği bir başka şey de eksik satırlar için bir rapor almaktır. `coverage report -m` dersem (missing için), eksik satırları da ekler; ama 100% coverage olduğu için yok.

```bash
coverage report -m
```

## 🧩 Bilerek Eksik Kapsam Oluşturma

Şimdi bazı eksik satırlar oluşturalım. Şunların hepsini alacağım; negative base kısmından aşağıya kadar. Onları yorum satırına alacağım. Gidiyor olacaklar. Bu satırlar artık kapsanmayacak.

Şimdi `nosetests`’i tekrar `with-coverage` ile çalıştırıyorum ve 100% alıyorum; bu biraz garip ama coverage aracının çalışma şekli böyle. Kümülatiftir, yani bir anlamda size yalan söyler.

Bu yüzden her seferinde coverage’ı silmesini istersiniz. Bir parametre daha var: `--cover-erase`.

```bash
nosetests --with-coverage --cover-erase
```

Ve şimdi gerçek coverage’ı alıyorum: yüzde 60.

## ⚙️ setup.cfg ile Parametreleri Otomatikleştirme

Ama bu çok yazı yazmak demek. O yüzden bir yapılandırma dosyası oluşturabiliriz; böylece bu parametreleri her seferinde yazmak zorunda kalmayız. Haydi bunu yapalım; çünkü yazmaktan yoruldum.

Lab’da bunu siz yapacaksınız. Lab klasörüne sağ tıklayıp yeni bir dosya ekleyeceğim. Adı `setup.cfg`.

Bu `setup.cfg` dosyasında, `with-coverage` demek yerine burada yazabilirim: `with-spec with-coverage`. README’de zaten var; kesip yapıştırıyorum. İzleyip yazmak zorunda kalmayın.

Şimdi buraya şunları yapıştıracağız: `verbosity 2`, `with-spec`, `with-color`. Dikkat ederseniz tire tire yok; onlara gerek yok. Sadece flag’in adı girer.

Ayrıca, sadece aç/kapa olan bayraklar için, yani flag’den sonra bir değer gelmeyenler için, açmak ya da kapatmak üzere bir ya da sıfır koyabilirsiniz.

Burada “hangi paketin kapsanmasını istediğiniz” yazıyor; *triangle* paketini istediğinizi söylüyorsunuz. Burada da coverage’a “eksik satırları coverage raporunda yazdır” diyorsunuz.

Kaydettiğime göre, geri döneceğim ve hiçbir parametre vermeden `nosetests` çalıştıracağım; kursun geri kalanında da böyle çalıştıracaksınız.

```bash
nosetests
```

Ve işte gidiyoruz. Bu güzel raporu alıyoruz. Eksik olan `6, 8, 12, 14` satırları var; bu satırlar için test vakası yok çünkü yorum satırına almıştım.

## 🔍 Eksik Satırlara Bakma ve Kapsamı Artırma

Bu satırlara bakalım. `triangle.py` dosyasına gidersem ve 6 ile 8’e bakarsam, bunlar boolean ya da string gibi şeyler değil de sayı döndürüldüğünü kontrol ediyordu. `int` ya da `float` olmalı.

O yüzden `triangle.py`’ye geri döneceğiz; boolean kontrolü yaptığımız test vakalarını bulacağız, yani boolean ya da string gönderdiğimiz testleri. Şimdi onları çalıştıracağız.

Olan şu olacak: 6 ve 8 artık coverage raporunda görünmeyecek ve coverage yüzde 60’tan yükselecek. Bir daha çalıştıralım.

Evet, 6 ve 8 gitti; 12 ve 14 hâlâ eksik. Coverage yüzde 80’e çıktı. Sonra geri dönüp daha fazla test vakası yazarsınız. Gerçek hayatta sadece yorum satırlarını kaldırmak kadar kolay olmayacak. Bu demoda yapabiliyoruz.

Yorum satırlarını kaldırıyoruz; şimdi tüm test vakaları geri geldi. Sonra `nosetests`’i bir kez daha çalıştırıyoruz ve yüzde 100 alıyoruz.

## 🧠 Neden Bu Akışı Gösterdim

Bunun nasıl çalıştığını anlamanızı istedim. Sadece “Lab’da bir sihir var; lab’da bu güzel renkli çıktıyı alıyorum ama projede nose kurunca bunların hiçbiri gelmiyor” demenizi istemedim.

Sadece bilmenizi istedim: tüm bu parametreler `setup.cfg` dosyasında; *Pinocchio* spec ve rengi ekliyor; coverage aracı da coverage raporunu ekliyor.

Böylece projelerinizde testlerden gelen çıktınız da, repository’nin kök dizinine o `setup.cfg` dosyasını koyarsanız, buradaki kadar güzel görünebilir.

Bu lab için hepsi bu.
