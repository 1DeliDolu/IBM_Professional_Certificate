# 🧪 Test Güdümlü Geliştirme Uygulaması Demosu

## 👋 TDD Laboratuvarına Hoş Geldiniz

Test Güdümlü Geliştirme’yi ( *TDD* ) uygulama laboratuvarına hoş geldiniz. Bu demoda, *test güdümlü geliştirme*yi gerçekten uygulama iş akışını göstereceğim; yani, sahip olmayı dilediğiniz kod için testleri yazmak ve ardından testleri geçirecek kodu yazmak.

Bu demonun sonuçları, laboratuvarlarınız için başlangıç noktası olacak; sonra siz devralıp daha fazla test vakası ve daha fazla kod yazacaksınız.

## 📁 Proje Klasörü ve Gereksinimler

Ben zaten practice TDD klasörüne girdim. Burada gereksinimlerin olduğunu göreceksiniz. Ben onları zaten kurdum. Hata kodlarımızı kontrol ederken kullanabileceğimiz bazı HTTP hata kodlarını içeren bir `status.py` modülü var.

Gereksinimleri belgelemek için, yalnızca gereksinimleri oluşturmak amacıyla `counters.py` dosyasını zaten oluşturdum ki ne olduklarını görebilelim. Kod yok.

Birden fazla sayacı takip edebilen bir servis oluştur. *RESTful* olmalı. Bu bize nasıl olması gerektiğini söyler: oluştur, getir, güncelle, sil; dönüş kodları ne olacak, *RESTful* yönergelerini takip edecek şekilde. Endpoint’in adı `/counters` olmalı. Şimdi counters endpoint’i olduğunu biliyoruz.

Bunu `counter` adlı bir modüle koyacağız; tekil. `counters` koleksiyon, o yüzden çoğul. Bir sayaç oluştururken, adı path içinde belirtirsiniz. Adı path içinde geçirmenize izin vereceğiz. Sonra eğer oluşturulan ad zaten mevcutsa, `409 conflict` döndürürsünüz.

Bu demoda bu iki şeyi yapacağız, sonra siz laboratuvarda daha fazlasını yapacaksınız.

## 🧩 Test Sınıfını Oluşturma ve Uygulamayı İçe Aktarma

Her test vakası şu şekilde başlar: `unittests`’ten `TestCase` sınıfını içe aktar.

```python
from unittests import TestCase
```

Sonra `class Countertest` deriz; sınıf adı tekil olmalı. `TestCase`’ten türetiriz, çok önemli. `nosetests` çalıştırdığımızda docstring gösterileceği için bir docstring koymak istiyorum. `nosetests`’i çalıştırırken bize docstring’i gösterecek. Bunun counter testleri olduğunu söyleyeceğiz.

Sonra testlerimizi yazmaya başlayabiliriz. İlk yapmak istediğimiz şeyin, test edilen kodu içe aktarmak olduğunu düşünelim.

Ama kodumuz yok. Ama olsaydı, onu nasıl içe aktarırdık? İçe aktarımlara çıkıp, “Ben bu counters sınıfını koyduğum `counter` adlı bir modüle sahip olurdum” diyeceğim. O yüzden şunu diyeceğim: `from counter import`.

Şimdi, bunun bir *Flask* uygulaması olacağını biliyorum. Tüm *Flask* uygulamaları gelenek gereği, bir standart olarak `app` diye adlandırılır: A-P-P. Orada `app` adlı bir *Flask* uygulaması olacağını biliyorum. Olmalı.

Şunu diyeceğim:

```python
from counter import app
```

Şimdi, neden `app`’i içe aktarıyorum? Çünkü  *Flask* ’ın bir test çalıştırıcısı var ve testleri çalıştırmak için *Flask* uygulamasındaki test çalıştırıcıyı kullanacağız.

Bunu kaydedeceğim, `from counter import app`, sonra `nosetests` çalıştırıp nerede olduğumuza bakacağım.

```bash
nosetests
```

`nosetests` çalıştırdığımda bir hata görüyorum: Modül bulunamadı, `counter` adlı modül yok. Hadi bunu düzeltelim.

## 🛠️ counter.py Modülünü ve Minimal Flask App’i Oluşturma

Bu, yazacağımız ilk kod parçası. Klasöre sağ tıklayıp yeni dosya diyeceğim ve `counter.py` adlı bir modül oluşturacağım. Orada, sadece bunu oluşturarak `nosetests`’i tekrar çalıştıracağım ve “Şimdi mutlu musun?” diyeceğim.

Diyecek ki: “Hayır, pek değil. `counter`’dan `app` içe aktarılamıyor.” Biraz daha ilerledik: `counter` var, `app` yok.

O zaman, bunu mutlu etmek için minimal bir *Flask app* oluşturalım.

```python
from flask import Flask

app = Flask(__name__)
```

Bunu kaydedeceğim ve testlerin geçmesi için bunun yeterli olması gerekir.

Şimdi `nosetests`’i tekrar çalıştıracağım ve hepsi mutlu. Coverage aracının `counter`, `status` ve `test counter` üzerinde coverage yaptığını fark edeceğim.

Ben hepsinde coverage istemiyorum. `setup.cfg` dosyama gidip, “Hey, ben sadece `counter` sınıfı üzerinde coverage istiyorum. Aslında ilgilendiğim tek şey bu” diyeceğim, sonra `nosetests`’i tekrar çalıştırırım ve sadece `counter`’ı alırım; çünkü odaklanacağımız o.

Şimdi başlangıç uygulamam var. Geri dönüp ilk test vakamızı yazabiliriz.

## 🧪 İlk Test: Sayaç Oluşturma

Yapmak istediğiniz ilk şey bir sayaç oluşturmak. O yüzden diyeceğim ki: bir fonksiyon tanımlayalım; test vakalarının hepsi `test_` ile başlamalı.

`test_create_a_counter` yazalım. Bu bir sınıf üzerindeki metod olduğu için `self` geçiririz. Bir docstring veririz çünkü docstring gösterilecek. *RSpec* söz dizimini kullanacağım.

“Bir sayaç oluşturmalı.” “Create” kelimesini doğru yazalım. Bir sayaç oluşturmalı.

Şimdi bir sayaç nasıl oluşturulur diye düşünelim.

*RESTful* bir API olduğunu biliyoruz. İhtiyacım olan ilk şey, `app`’ten test client’ı almak. Hatırlayın, bir test client olduğunu söylemiştim; o yüzden şöyle diyeceğim:

```python
client = app.test_client
```

 *Flask* ’tan test client’ı böyle alırsınız. Artık bir test client’ım var. Bu test client üzerinde `post`, `get`, `delete` çağırabilirim; tıpkı gerçek *Flask* uygulamasıyla konuşuyormuşum gibi.

Bunu yapalım. `result` adlı bir değişken oluşturup şöyle diyeceğim: `result = client.` ve `/counters`’a post etmek ve ona bir ad geçirmek istiyorum.

Yani `/counters`’a post, sonra bir ad verelim. `foo` adını vereceğim. Bu bir sayaç oluşturmak için yeterli olmalı.

Şimdi assert yapmamız gerekiyor. Bir  *REST API* ’de oluşturmanın, *RESTful* yönergeleri takip ediliyorsa `201 created` döndürmesi gerektiğini biliyoruz. Bunu assert edeceğim: `self.assert`… `assert equals` yapacağız.

HTTP sonucunda geri gelen `result.statuscode`’un `201`’e eşit olduğunu assert edeceğiz.

Ben bu yalın sayıları kullanmayı sevmiyorum. Status kullanmanın çok daha kolay olduğunu düşünüyorum. Hatırlayın, `status.py` vardı. O `status.py`’yi içe aktaracağım.

```python
import status
```

Şimdi tüm o güzel status kodlarına sahibim.

`201` yerine şunu diyeceğim:

```python
status.HTTP_201_CREATED
```

Bence bu, programcının bakış açısından çok daha hoş görünüyor. “Bu kod ne yapıyor?” görebiliyorum, değil mi? “201 neydi?” Oluşturuldu. Programcının ne olup bittiğini anlamasına yardımcı oluyor.

Yani test client’ımız var. `counters.foo` üzerinde bir post yapıyoruz, bir `foo` sayacı oluşturmalı. Sonra `201 Created`.

Bunu çalıştıralım. Tekrar `nosetests` çalıştıracağız. Bu sefer kırmızı alıyoruz. Yani Red/Green/Refactor; kırmızı aşamasındayız ve aldığımız hata assertion error: `404` `201`’e eşit değil.

`404` nereden geldi? `404`, bulunamadı. Dediği şey şu: “`/counters` adlı bir endpoint bulamadım, o yüzden oraya post edemem.”

O zaman, yazmamız gereken bir sonraki kod bu. Hadi `counters`’a gidip o endpoint’i oluşturalım.

## 🌐 /counters Endpoint’ini Yazma

`app` decorator’ını kullanacağız. `/counters` adlı bir route oluşturacağız. Ayrıca o route içine bir değişken koyabileceğinizi belirteceğiz ve bu değişkene `name` diyeceğiz.

Sonra  *Flask* ’a, bu route üzerinde izin verilen tek metodun `post` olacağını bildireceğiz. `methods` eşittir diyeceğiz ve `methods` bir array, bir liste. Ama izin vermek istediğim tek şey `post`.

Bu şimdi şunu söylüyor: “Eğer biri name geçirerek `post` ile `/counters` çağırırsa, bu decorator ile sardığım fonksiyon çağrılacak fonksiyon olacak.”

Şimdi fonksiyonu tanımlayacağız: `create_counter`. Ve `name` geçiriyoruz. URL’de hangi değişken ikameleri varsa, onları doğrudan içine koyabilirsiniz ve aynı isim olmak zorundalar.

Burada `name` ise, `name` olmalı. Şimdi o `name`’i geçiriyor.

Tamam, şimdi fonksiyona başlayacağım. Bir docstring verip “Bir sayaç oluşturur” diyeceğim.

Sonra logging’i severim; şimdi öde, sonra öde. `app.logger` yapacağım.  *Flask* ’ta bir logger var. `info`.

Ben her şeyi loglamayı severim. “Sayaç oluşturma isteği” ve sonra adı.

Güvenin bana, bunu debug ederken “create isteği”, “update isteği”, “delete isteği” loglarına sahip olmayı seveceksiniz. Harika olacak.

Şimdi bir veritabanımız yok ve sonra ekleyeceğiz. Bu minimum uygulanabilir ürün.

O yüzden önce API’yi çalışır hale getirelim. Sadece global bir dictionary oluşturacağım. `counters` diyeceğiz. Dictionary yapacağız. Python’da global değişkenler genelde büyük harf olmalı. Ben onu büyük harf yaparım. Ama sonra bunu bir fonksiyon içinde değiştirmek istersem, bunun lokal bir değişken olmadığını Python’a bildirmek için `global` demem gerekir ve bu fonksiyonun bu global counters değişkenini değiştireceğini söylemem gerekir.

Şimdi, o adla bir sayaç oluşturuyorum. `counters name equals 0` yapacağız. Sayaç oluşturuldu.

Yapmamız gereken son şey, sayacı dönüş koduyla birlikte geri göndermek. `return` diyeceğiz ve `name` döndüreceğiz. Sonra `counters.name`, daha doğrusu name ile dereference edilmiş `counters`. Oraya kopyalayıp yapıştıracağım ki yanlış yazmayayım.

Dönüşün ikinci parçası olarak, gerçek status kodunu koymak istiyoruz. Status kodu bir status olacak. Aa, `status`’u içe aktarmadım. Hadi `status` içe aktaralım.

`import status`, ve `status.HTTP_201_CREATED`, sonra kaydedeceğim.

Şimdi, bu ilk endpoint’i uyguladım; testin geçmesini sağlamalı. Geri dönüp `nosetests`’i tekrar çalıştıralım.

İkinci kez çalıştırıyorum ve yeşil. “Counter test” diyor. Bu, sınıfa verdiğim ad. “Bir sayaç oluşturmalı” yeşil, yüzde 100 coverage, hazırız.

## 🚫 İkinci Test: Aynı İsimle Oluşturma ve 409 Conflict

Bir tane daha yapalım, sonra siz laboratuvarda daha fazlasını yapacaksınız.

İkinci yapmak istediğim, şu gereksinim: “Eğer oluşturulan ad zaten mevcutsa, `409 conflict` döndür.”

Buradaki fonksiyonun çoğu bunun tekrarı. O yüzden kod yeniden kullanımı yapacağım; diğer adıyla kopyala-yapıştır.

`test_duplicate_counter`.

Burada diyeceğiz ki: “Tekrarlarda bir hata döndürmeli.”

Şimdi `app` test client’ını tekrar alıyorum. Bu noktada şöyle diyorum: “Şey, bu metodun ilk işinde `app` client’ı alıyorum. Sonraki metodda da ilk iş o. Muhtemelen bir sonraki metodda da ilk iş olacak.”

İşte testleri gerçekten refactor etmeye başladığınız yer burası. “setup” denen bir fonksiyon var, değil mi? Bir test fixture. Bunu öğrendik. Onu kullanacağım. `def`.

Bu `setup` test fixture’ını kullanacağız.

Bu client’ı alıp bu sınıfta bir instance variable yapabilirim. O yüzden şimdi diyeceğim:

```python
self.client = app.test_client
```

Sonra bu satırı silebilirim. *DRY* uygulamaya çalışıyoruz: kendini tekrar etme.

Bunu sileriz, bunu sileriz. Bu client’lar artık `self` ile başlamalı çünkü instance variable’lar.

Ve kodu sıkılaştırdım. Yani sürekli refactor edip kodu daha iyi hale getiriyorsunuz.

Tamam, tekrarlara bakalım. Bu sefer `bar` yapacağız. `bar` adlı bir sayaç oluşturuyorum ve bunu iki kez yapacağım. Bunu kopyalayıp yapıştıracağım.

Ama ikinci sefer, `201 created` dönmesini beklemiyorum. `409 conflict` dönmesini bekliyorum.

Yani ilk sefer oluşturulmasını bekliyorum. İkinci sefer `bar` oluşturmaya çalıştığımda `409 conflict` bekliyorum.

Test vakalarımızı tekrar çalıştıralım. Bir kez daha Red/Green/Refactor’ın kırmızı aşamasındayız.

“Tekrarlarda bir hata döndürmeli” başarısız oldu. Ve diyor ki: `201` `409`’a eşit değil.

O sayacı ikinci kez memnuniyetle oluşturdu; bu çok tehlikeli çünkü onu sıfıra ayarladı. Yani sayacı 1, 2, 3, 4, 5 diye güncelleriz, sonra aynı sayacı tekrar oluşturursak, onu sıfıra resetleyecek. İstediğimiz bu değil.

O yüzden hadi bunu düzeltelim. `counters.py`’ye gidip diyeceğim ki: Bence önce bu sayacın var olup olmadığını kontrol etmemiz gerekiyor.

O yüzden şunu yapacağım: `if name in counters`, sadece kontrol edelim. Eğer ad counters içindeyse, o zaman bir mesaj döndüreceğim.

Bu bir *REST API* olduğu için, tüm mesajlar Python dictionary’leri veya *JSON* olmalı. O yüzden diyeceğim: `message`, iki nokta üst üste, sonra “Sayaç adı zaten mevcut.” Bu da güzel bir hata mesajı verir; adı onun içine gömerek.

Sonra yapmak istediğim şey dönüş kodunu göndermek. `status`, ve `409 conflict` statüsü istiyorum.

Bunu kaydedeceğiz. Şimdi yeni davranışla güncelledim.

Sahip olmayı dilediğim kod için testi yazdım. Şimdi kodu yazıyorum.

O yüzden diyoruz ki: Eğer name counters içindeyse, sayaç zaten vardır. Yoksa sayacı oluşturabiliriz.

Şimdi `nosetests`’i tekrar çalıştıracağım. Ve bu sefer hepsi yeşil. İkisi de yeşil.

“Bir sayaç oluşturmalı” yeşil. “Tekrarlarda bir hata döndürmeli” yeşil.

## ✅ Kapanış: Red/Green/Refactor

Red/Green/Refactor’ın olayı bu: sahip olmayı dilediğiniz kod için bir test vakası yazmak, sonra o testi geçirecek kodu yazmak.

O kadar da zor değil. Test vakası, kodun davranışını tanımlar. Yani kodun davranışını düşünürsünüz, sonra o kodun o davranışa sahip olduğunu kontrol edecek bir test vakası yazarsınız.

İşte hepsi bu.
