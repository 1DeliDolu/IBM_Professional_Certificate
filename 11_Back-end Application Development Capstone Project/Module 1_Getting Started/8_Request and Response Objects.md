# 📦 Request ve Response Nesneleri

“Request ve Response Nesneleri”ne hoş geldiniz. Bu videoyu izledikten sonra şunları yapabileceksiniz: Flask *Request* nesnesini açıklamak ve Flask *Response* nesnesini açıklamak.

Flask’te rotaları nasıl özelleştireceğimizi öğrenelim. Yolu ( *path* ) `route` dekoratörü ile tanımlarsınız. `@app.route` dekoratörü varsayılan olarak **GET** metodunu kullanır. İstemciler, belirtilen yola yalnızca **GET** istekleri gönderebilir. Bir yolun hangi HTTP metodlarına yanıt vereceğini kontrol etmek için `methods` adlı ikinci bir argüman geçebilirsiniz.

Örneğin, aynı olan aşağıdaki iki metoda bakın. Bu kodda **GET** metodu örtüktür. Bu kodda ise **GET** metodu açıkça belirtilmiştir.

Bir başka örnek: `"/health"` URL’i **GET** ve **POST** isteklerine yanıt verir. İstek **GET** ise kod, `ok` durumunu ve **GET** metodunu çıktı verir. İstek **POST** ise kod, `ok` durumunu ve **POST** metodunu çıktı verir.

Bu, **GET** `curl` komutunun çıktısıdır. Bu ise **POST** `curl` komutunun çıktısıdır.

Flask’e yapılan tüm HTTP çağrıları, `Flask.Request` sınıfından oluşturulan  *request object* ’i içerir. Bir istemci Flask sunucusundan bir kaynak istediğinde, bu istek `@app.route` dekoratörü tarafından ele alınır. Aynı metot içinde  *request object* ’i inceleyip keşfedebilirsiniz.

---

## 🧾 Request Nesnesinde Bulunan Bilgiler

*Request object* içinde şu bilgiler mevcuttur:

* Sunucunun adresi (tuple biçiminde: `host`, `port`)
* İstekle gönderilen `headers` ve istek tarafından talep edilen kaynak olan URL
* `access_route`: Birden fazla kez yönlendirilmiş istekler için tüm IP adreslerini listeler
* `full_path`: Sorgu dizgesi ( *query string* ) dahil isteğin tam yolunu temsil eder
* `is_secure`: İstemci HTTPS veya WSS protokolüyle istek yapıyorsa `true` olur
* `is_JSON`: İstek JSON verisi içeriyorsa `true` olur
* `Cookies` sözlüğü: İstekle gönderilen cookie’leri içerir

---

## 🧠 Header Üzerinden Erişilebilen Ek Veriler

Buna ek olarak, header’dan aşağıdaki verilere erişebilirsiniz:

* `Cache-Control`: Tarayıcılarda nasıl cache’leneceğine dair bilgi tutar
* `Accept`: İstemcinin hangi içerik türünü anladığını tarayıcıya bildirir
* `Accept-Encoding`: Kod içeriğini belirtir
* `User-Agent`: İstemciyi, uygulamayı, işletim sistemini veya sürümü tanımlar
* `Accept-Language`: Belirli bir dil ve yerel ayar ( *locale* ) talep eder
* `Host`: İstenen sunucunun host ve port numarasını belirtir

---

## 🧩 Özel Request Nesnesi Kullanma

`request` nesnesini özel bir *request object* ile değiştirebilirsiniz; bu genellikle isteğe bağlıdır çünkü Flask `Request` sınıfının öznitelikleri ve metotları çoğu zaman yeterlidir.

Şimdi, bir istemci istek yaptığında sunucuda yazdırılan bazı gerçek değerlere bakalım. Bu durumda istemci, terminalden çalıştırılan **CURL** komutudur. *request server* `127.0.0.1` veya `localhost` ve port `5000`’dir.

Sonra bazı header’ları yazdırırsınız:

* Host: `localhost:5000`’in tam yolu
* User-Agent: `curl` sürüm `7.79.1`
* İstemci `application/JSON` içerik türünü talep etmiştir

---

## 🔍 Request Nesnesinden Diğer Öznitelikler

 *Request object* ’ten bazı başka özniteliklere bakalım:

* İstenen URL: `http://localhost:5000`
* `access_route` listesi tek bir değer içerir: `127.0.0.1`
* İsteğin `full_path`’i, tek bir ileri eğik çizgi ile gösterilen ana yoldur
* **GET** isteği ile veri göndermediğimiz için `is_JSON` `false`’tur
* URL **HTTP** olduğu ve **HTTPS** olmadığı için `is_secure` `false`’tur
* Cookies sözlüğünün uzunluğu `0`’dır

---

## 🧰 Request Nesnesinden Veri Alma Yöntemleri

 *Request Object* ’ten bilgi almanın birden fazla yolu vardır.

* **POST** isteğinden veriyi byte olarak almak için `get_data` kullanın. Bu veriyi parse etmek sizin sorumluluğunuzdadır.
* `get_JSON()` metodunu kullanarak, **POST** isteğinden parse edilmiş JSON verisini alabilirsiniz.

Flask ayrıca, veriyi belirli bir türe parse etmenize gerek kalmadan istekten tam bilgiyi alabileceğiniz daha odaklı metotlar sağlar:

* `args`: Query parametrelerini sözlük olarak verir
* `JSON`: Veriyi sözlüğe parse eder
* `files`: Kullanıcının yüklediği dosyaları sağlar
* `form`: Form gönderiminde post edilen tüm değerleri içerir
* `values`: `args` verisini `form` verisiyle birleştirir

---

## 🧷 Query Parametrelerinden Değer Çekme

Artık  *request object* ’in nasıl göründüğünü ve request parametreleri ile body’den veri almak için metotları bildiğinize göre, bu veriden belirli değerleri nasıl çıkaracağımıza bakalım.

Şimdiye kadar gördüğünüz metotların dönüş türleri `MultiDict`, `ImmutableMultiDict` veya `CombinedMultiDict` olabilir. Bu veri yapılarının tümü bir Python sözlüğü gibi davranır ve değerleri almak için indeksleme veya `get` metodunu kullanabilirsiniz.

Verilen URL için `"capstone"` ve `"rating"` query parametrelerini çıkarmak istiyorsunuz.

Önce, metot içinde Flask ve `request` modüllerini import edersiniz. `course` argümanının değerini indeksleme kullanarak çıkarırsınız. Sonra `rating` argümanının değerini `get` metodunu kullanarak çıkarırsınız.

`get` metodu, argüman mevcut değilse `None` döndürür; indeksleme metodu ise hata üretir ve sunucuyu `"400 Bad Request"` ile durdurur.

Mesaj, tarayıcıda `course` değeri `capstone` ve `rating` değeri `10` olacak şekilde isteği gösterir.

---

## 📤 Response Nesnesi

Flask, bir *request object* sağladığı gibi bir *response object* de sağlar. İstemciye geri yanıt göndermeden önce  *response object* ’i kullanarak özel öznitelikler ve header’lar gönderebilirsiniz.

Bazı yaygın response öznitelikleri şunları içerir:

* `status_code`: İsteğin başarı ya da başarısızlığını belirtir
* `headers`: Yanıt hakkında daha fazla bilgi verir
* `content_type`: İstenen kaynağın medya türünü gösterir
* `content_length`: Yanıt mesaj gövdesinin boyutudur
* `content_encoding`: Yanıta uygulanan encoding’i belirtir; istemci veriyi nasıl decode edeceğini bilir
* `mime-type`: Yanıtın medya türünü ayarlar
* `expires`: Yanıtın hangi tarih veya saatten sonra süresi geçmiş sayılacağını içerir

---

## 🍪 Response Üzerindeki Standart Metotlar

Response nesnelerindeki bazı standart metotlar:

* `set_cookie`: İstemcide bir tarayıcı cookie’si ayarlar
* `delete_cookie`: İstemcide bir cookie’yi siler

---

## 🧪 Flask’in Response Nesnesiyle Çalışması

Flask’in farklı metotlarla response nesnesiyle nasıl çalıştığını öğrenelim:

* `@route` metodundan veri döndürdüğünüzde, `status_code` değeri `200` ve `mime-type` değeri **HTML** olan bir *Response object* sizin için otomatik olarak oluşturulur.
* `JSONify` de otomatik olarak bir *Response object* oluşturur.
* Özel bir response oluşturmak için `make_response` kullanabilirsiniz.
* Flask, `redirect` adlı özel bir metot sağlar; bu metot `302` status-code döndürür ve istemciyi başka bir URL’e yönlendirir.
* Son olarak Flask, hata koşuluna sahip bir response döndürmek için `abort` metodunu sağlar.

---

## 🧾 Özet

Bu videoda şunları öğrendiniz:

* Flask, her istemci çağrısı için bir *Request* ve bir *Response* nesnesi sağlar.
* Flask *Request* üzerinden header’lar gibi ek bilgilere erişebilirsiniz.
* *Request Object* ’i parse ederek query parametrelerini, body’yi ve diğer argümanları alabilirsiniz.
* İstemciye yanıt göndermeden önce *Response* nesnelerinde status ayarlayabilirsiniz.
