# 🎭 Mock Nesnelerle Mocking Demo

## 🧪 Lab’a Hoş Geldiniz

Mock nesnelerle mocking lab’ına hoş geldiniz. Bu lab’da aslında IMDb veritabanına yapılan çağrıları *mock* edeceğiz. Basit bir *mock* ile başlayacağız ve sonra giderek daha karmaşık hale getireceğiz.

Her zamanki gibi *nose test* çalıştırarak başlayacağız, ama sizi uyarmalıyım: çok heyecan verici olmayacak çünkü henüz hiçbir test vakası yazmadık. Yine de başlangıç olması için çalıştıralım.

```bash
nosetests
```

*Nose tests* ve dediğim gibi %36 *test coverage* çünkü test yok, o yüzden IDE’mize geçelim.

## 🗂️ Test Edeceğimiz Model: `IMDb.py`

 *Mock objects lab* ’ımızı açalım ve ilk bakmak istediğim şey test edeceğimiz model. `IMDb.py` dosyasını seçeceğiz ve bu, IMDb veritabanına yapılan çok çok fazla çağrıdan sadece 3 tanesini yapan küçük bir sınıf.

Sadece üçünü yapıyor. Yani bir  *constructor* ’ı var, bir *API key* alıyor ve sonra üç çağrısı var:  *Search titles* , *Get movie reviews* ve  *Get movie ratings* . Bunların gerçekten IMDb servisine `request.get` çağrıları yaptığını görebilirsiniz: biri *search titles* için, biri *reviews* için, biri *ratings* için.

Bir başlık ( *title* ) gönderiyorsunuz, bir başlık alıyorsunuz; *reviews* veya *ratings* almak için bir *movie ID* gönderiyorsunuz ve sizin için bu  *API key* ’i de ekliyor.

Buradaki önemli kısım şu: bu gerçekten bir çağrı yapıyor ve sonra geri gelen sonuçların `200` olup olmadığına bakıyor. Eğer `200` ise, isteğe şunu söylüyor: “Bana geri aldığın  *JSON* ’ı getir.”

Aksi halde boş bir *dictionary* döndürüyor. Bu davranışı anlamak önemli, çünkü test etmek istediğimiz davranış bu.

## 🧷 Test Dosyası ve Test Fixture’ı

Şimdi bakmak istediğimiz bir sonraki şey bunlar: `test_IMDb` dosyası. `test_IMDb` dosyasında `patch` ve `mock` zaten import edilmiş. `requests`’ten bir `response` import edilmiş, yani bir  *response* ’ı taklit edeceğiz. Ve tabii ki test edilen model var: `models` paketimizden `IMDb` sınıfı.

Sonra `IMDb_Data` diye global bir değişken oluşturuyor ve bu, `setup` sınıfında yükleniyor.

Şimdi gidip o  *test fixture* ’a bakalım, içinde ne var.  *Test fixture* ’a baktığımızda görüyoruz: “Aa, bunlar gerçek IMDb veritabanından alınmış gerçek *JSON* yanıtları.”

Yani gerçekten gidip çağrılar yaptık. Kötü bir *API key* verdik ve hata mesajının gerçekten “invalid API key” olduğunu gördük. Sonra bunları alıp bu dosyaya koyduk.

Artık  *good reviews* ,  *invalid movies* ,  *bad reviews* , *good ratings* vs. gibi her şeyi geri döndürebilecek şekilde bu veriyi kontrol edebiliyoruz; yani bu veriler, o çağrıları taklit etmemize ya da *mock* etmemize yardım ediyor.

## 🧩 Lab Talimatları ve Başlangıç Durumu

Lab’ınızda test vakaları olmayacak; boş olacak. Ancak lab talimatlarının ilk maddesi şu: iyi kodu kopyala-yapıştır ve sonra *mock* et. Sonrakini kopyala-yapıştır ve sonra *mock* et.

Benim yaptığım şey şu: lab’da yapacağınız her şeyi kopyalayıp yapıştırdım ve hepsini yorum satırına aldım. Yani başlarken aynı koda sahip olacaksınız. Şimdi ilkini yorumdan çıkararak başlayayım ve ne yapacağımızı anlatayım.

## 🧱 İlk Test: `search_titles` Çağrısını Bypass Etmek

Bu ilkinde  *search* ’ü atlamak istiyoruz, bu yüzden `@patch` kullanacağız.

Şimdi neyi *patch* edeceğimizi konuşalım. Bu `search_titles` çağrısını *patch* etmek istiyorum ve `IMDb`’yi modülümüze import ettim; bu önemli çünkü mesele tamamen  *namespacing* .

Bir kez `from models import IMDb` dediğimizde, `IMDb` artık `models` namespace’inde değil. Bizim namespace’imize geliyor ve bu modülün adı `test_IMDb`.

Dolayısıyla bu sınıf üzerinde bir method çağrısını *patch* etmek istiyorsanız, aslında şunu *patch* etmeniz gerekir:

```text
test_IMDb.IMDb.<patch_edilecek_method>
```

Doğru  *namespace* ’leri yakalamak ve doğru şeyi *patch* etmek önemli. `models` içindekini *patch* etmek istemiyoruz; import ettiğimiz şeyi *patch* etmek istiyoruz, davranışını değiştirdiğimiz şey o.

Bu ilk patch, `test_IMDb` içindeki `IMDb` sınıfına ve buradaki `search_titles` çağrısına olacak. Yanlış yazmamak için ben sadece kesip yapıştıracağım. O `search_titles` çağrısı yapıldığında patch oluşacak.

Bir test vakasına patch eklediğinizde, patch’i temsil eden *mock* için yeni bir parametre geçirmeniz gerekir. Ben buna `IMDB_mock` diyeceğim. Neden olmasın?

Şimdi bu mock elimde ve bununla bir şey yapmak istiyoruz; yani  *return value* ’u patch edeceğiz:

`IMDb_mock.return_value = ...`

Ve kendime küçük bir not: lab’da talimatlarınız olacak, “good search” ile patch etmek istiyoruz. Bu yüzden bu global değişkeni alacağız: `IMDB_Data` ve o dictionary’yi `GOOD_SEARCH` ile dereference edeceğiz.

Yani şunu geri döndüreceğiz:

```text
IMDB_Data['GOOD_SEARCH']
```

Ve bu bir patch gibi görünüyor.

Böylece `IMDb.search_titles`’ın bizim versiyonunu patch ettik, o `IMDb_mock`’u ekstra parametre yaptık ve bu parametrede “return value’u değiştir” dedik. “Bu good search’ü geri döndür” dedik.

Sonra test vakası hiç değişmiyor. Canlı (live) olanla aynı test vakası, değil mi? Bir `API key` ile `IMDb`’yi instantiate ediyor. Sonra `Bambi` için `search_titles` çağırıyor ve sonuçların `None` olmadığını kontrol ediyor. Sonra `error_message`’ın `None` olduğunu doğruluyor.

Yani hata mesajı yok. Sonra gidip sonuçları alıyor ve o `ID`’nin içeride olduğundan emin oluyor; JSON’a bakarsanız gerçekten orada.

Şimdi *nose tests* çalıştıralım ve bunun çalışıp çalışmadığını görelim.

```bash
nosetests
```

İşte oldu, çalıştı. Başlığa göre arama bitti.

## 🧠 İkinci Test: Bu Kez `requests.get` Patch (404 Senaryosu)

Şimdi bir sonrakine geçelim. Yorumdan çıkaracağım; lab’da siz kopyala-yapıştır yapacaksınız. Kopyala-yapıştır yaptığınızda elinizde bu olacak.

Sonra bazı talimatlar olacak ve talimatlar şöyle diyecek: bu sefer bir `404` patch etmek istiyoruz ama bu kez biraz daha sofistike bir patch yapacağız.

Bu sefer `request.get`’i patch etmek istiyoruz. Aslında `search_titles`’ı çağırmak istiyoruz; onun çalışmasını istiyoruz. `search.get`’e geldiğinde patch devreye girsin istiyoruz ve sonra  *return code* ’un *OK* olup olmadığına baktığında bunun da gerçekleşmesini istiyoruz.

Yine patch ile başlıyoruz: `@patch`.

Bu sefer patch edeceğimiz şey: bu modülün içindeki `requests` paketini patch etmek istiyoruz ve özellikle `requests.get`. Yine *namespacing* önemli.

Bu, `IMDb` modülünün içinde. `IMDb` içine import edilen `requests` ve `get` metodu; dolayısıyla bunu bu şekilde nitelendirmeniz gerekir. Ha, bu arada `models` paketinde, çünkü `IMDb`’nin kendisi `models` paketinde; yani:

```text
models.IMDb.requests.get
```

Bunu yapalım: `models`, sonra modülün adı olan `IMDb`, sonra `requests` (çünkü `IMDb` içine import ettiğimiz requests paketi) ve sonra `get`. Böylece `IMDb` modellerindeki `get` çağrısını patch etmiş oluyoruz.

Yine mock’u temsil etmesi için bir parametre geçiriyoruz: tutarlılık olsun diye `IMDb_mock`.

Şimdi bu mock biraz farklı. Sadece *JSON* geri gönderemem, değil mi? Yani `IMDb_mock.return_value` eğer sadece *JSON* olsaydı, şöyle olacak:

Koda gidip bakıyoruz: `request.get` yapıyor, sonuçları geri alıyor. Sonuçlar bir  *dictionary* , değil mi? *JSON* Python dictionary.

Ama bir sonraki satır şunu diyor: `results.status_code`. Dictionary’de `.status_code` attribute’u yok, yani bu patlayacak. Bu çalışmayacak.

Sadece böyle bir *return value* kullanamayız; o yüzden *return value* gerçek bir nesne olmalı. Bir  *mock object* . Ve yapacağımız şey de bu.

Diyeceğiz ki *return value* bir  *mock* . Sonra o mock’a şunu söyleyeceğiz: “Hey mock, sende bir `status_code` var.”


# 🚦 `status_code` ile Mock’un Davranışını Tamamlamak

Ve senin  *status code* ’un `404`. Aslında `200` dışında herhangi bir şey olabilir, değil mi?  *Status code* ’un `404`.

Bunu kaydediyorum; artık *request* yaptığımızda, *request* bir *mock* geri döndürecek. Mock üzerinde `mock.status_code` diyebilirim ve bir *status code* alırım; bu yüzden bu kod mock kullanarak çalışacak.

Tekrar *nose tests* çalıştıralım.

```bash
nosetests
```

Ve görünen o ki bu da geçti, evet. Böylece ikisi de geçti. Başarılı olduk.

# 🧩 Sonraki Adım: Geçersiz API (Invalid API)

Şimdi bir sonraki üzerinde çalışalım; sıradaki görünüyor ki… geçersiz bir API’ye sebep olacak.

Bu biraz daha sofistike olacak çünkü *invalid API* için, değil mi? `request.get` çağırdığı gerçeğini patch etmemiz gerekecek ve sonra `200` *status code* döndürecek. Bu da `results.json` çağırmasına sebep olacak; yani bu daha da sofistike.

Bunun gerçekten bir request gibi davranmasını istiyoruz. Öncekiyle aynı patch’i alacağım çünkü geri kalanların hepsi sadece `request.get` patch’leyecek; bu patch bizim için çalışacak.

Ayrıca buna da `IMDb` diyeceğiz, kolay olsun diye kopyalayıp yapıştıracağım. Sonra `IMDb_mock` ve şimdi bu `IMDb_mock`’u alıp  *return value* ’unu patch edeceğim.

Bu *return value* başka bir *mock* olacak.

```python
IMDb_mock.return_value = Mock()
```

Bu mock biraz daha sofistike olacak. Bunun bir request gibi davranmasını istiyorum.

## 📐 `spec` Parametresiyle Gerçek `Response` Davranışı

Şimdi `spec` parametresini kullanacağım. Yani “işte uyman gereken spesifikasyon” diyeceğim. Buradan bu request’i alacağım… daha doğrusu `response`’u; yani  *request library* ’den gerçek bir response gibi davranmasını istiyorum.

Şöyle diyeceğiz: işte `response`.

Sonra `status_code`’u `200` yapacağım; yani iyi bir status code ve şimdi `json` çağıracağını biliyoruz, değil mi? Gördük zaten. `200` aldıktan sonra `json` isimli bir metoda çağrı yapacak.

Dolayısıyla bu mock’a `json` diye bir metod vermem gerekiyor; bu metod da gerçek JSON’ı, yani  *invalid API* ’ye ait gerçek Python dictionary’sini döndürmeli.

Bu `json` metodunu tanımlayacağız; yani `json` bu mock üzerinde geçerli bir çağrı olacak ve `json = ...` diyeceğim, o da başka bir mock olacak.

Ve bu mock’ta `return_value` kullanacağız, değil mi? Bu mock’un `return_value`’u `IMDb_data` olacak.

Ve yine burada küçük bir ipucu bırakmıştım:  *invalid API key* ’i geri göndereceğim. Eğer gidip fixture’a tekrar bakarsak, *invalid API key* olanı geri göndereceğim ve o da “invalid API key” hata mesajını verecek. O anahtarı buraya koyayım. Kaydedelim.

## 🔁 Sonuç: Mock Zinciri Nasıl Çalışıyor?

Şimdi burada olan şey şu:

* `request.get` patch ediliyor.
* `request.get` bir *mock* döndürüyor.
* Bu mock, gerçek bir HTTP response gibi davranıyor ( *masquerading* ).
* `status_code`’u `200`.
* Eğer `json()` metodunu çağırırsanız, o da bir *mock* döndürüyor ve onun `return_value`’u  *invalid API key* .

Böylece artık `IMDb`’yi kötü bir API key ile instantiate ediyoruz, sonra search yapıyoruz, sonra `results`’un `None` olmadığını assert ediyoruz ve `error_message`’ın “invalid API key” olduğuna eşit olduğunu assert ediyoruz.

Bu fixture’ın gerçekten o *invalid API key* hata mesajını geri döndüreceğini biliyoruz.

Şimdi bunu çalıştıralım ve çalışıyor mu görelim. Tekrar *nose test* çalıştıracağız.

```bash
nosetests
```

Ve bu da çalıştı. Böylece üç tanesini çalıştırmış olduk.

# ⭐ Son Adım: İyi Bir Rating Döndürmek

Şimdi bir tane daha kaldı. Bu lab’daki son adım: iyi bir rating mock etmek.

Artık  *happy path* . İyi bir rating geri dönecek. Yine aynı patch’i kullanacağım çünkü sadece `request.get` patch’leyeceğiz.

Ve sonra `self, IMDb_mock`.

Test case’e dokunmayacağız ve aslında yukarıda kullandığımız aynı mock’u kullanacağız çünkü bu da daha karmaşık olacak.

Çünkü koda bakarsak… `IMDb.py` içinde şuna bakacağız: bu bir rating yapacak, değil mi? Rating isteyecek… sadece kontrol ediyorum. Bu `get movie ratings` çağrısı; yani aynı şeyi yapacak:

* `request.get`
* `status_code` kontrolü
* `json`’dan sonuç alma (yani `results.json()` çağrısı)

Dolayısıyla aynı türde bir mock’a ihtiyacımız var.

Tek yapacağımız şey: geri dönen veriyi *invalid API* yerine *good rating* yapmak.

Yani `200` ile bir response gibi davranan mock döndürecek ve içinde istediğimiz data olacak:  *good rating* . Sonra servisi çağıracağız, `movie_ratings` çağıracağız; bu gerçekten çalışacak. Kod `get` satırına kadar çalışacak, `get` bu mock’u geri getirecek (yukarıdaki mock) ve sonra sonuçlarda şu doğrulamaları yapacak:

Başlık `Bambi` ve `filmAffinity` `3` ve `Rotten Tomatoes`, değil mi?

Eğer dataya gidersek, *good rating* içinde `movie DB`, `Rotten Tomatoes` ve birkaç şey daha var; birkaç tanesini kontrol ediyor, sadece geri iyi bir rating geldiğinden emin olmak için.

Şimdi son kez *nose test* çalıştırıp ne aldığımıza bakalım.

```bash
nosetests
```

Ve çalışıyor. Hepsi çalışıyor.

# 🧠 Kapanış: Namespace ve Mock Zinciri

Dış sistemlere çağrıları patch etmenin ne kadar kolay olduğunu göstermek istedim.

 *Namespace* ’i düşünmeniz gerekiyor. Bu en kritik şey.  *Namespace* ’i düşünün, değil mi? Çağrı nerede? Hangi namespace içinde? O namespace’teki çağrıyı patch ederim ve sonra  *return value* ’u alıp bir mock döndürürüm:

* içinde *return codes* olan,
* `json` gibi çağrıları olan,
* bir `response` spesifikasyonuna (`spec`) göre davranan,

her türlü şeyi yapabilirsiniz.

Şimdi sizin göreviniz: projenizdeki test case’lere gidin ve dış sistemlere ya da kontrolünüz altında olmayan başka sistemlere birkaç çağrıyı mock edip edemeyeceğinize bakın ve test case’inizin her zaman çalışması için daha fazla kontrol kazanın.

Çünkü artık iyi dönüş kodları, kötü dönüş kodları gönderebilirsiniz.  *Error handler* ’larınızı test edebilirsiniz; neye ihtiyacınız varsa.
