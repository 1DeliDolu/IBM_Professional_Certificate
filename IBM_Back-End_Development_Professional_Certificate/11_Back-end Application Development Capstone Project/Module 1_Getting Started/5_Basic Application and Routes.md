# 🧭 Temel Uygulama ve Rotalar

“Temel Uygulama ve Rotalar”a hoş geldiniz. Bu videoyu izledikten sonra şunları yapabileceksiniz: Temel rotaları (routes) olan bir Flask uygulaması oluşturmak ve çalıştırmak. Sunucudan istemcilere JSON yanıtı döndürmeyi açıklamak. Flask’te mevcut çeşitli yapılandırma seçeneklerini açıklamak.

İlk Flask uygulamanızı oluşturmadan önce Flask’i kurduğunuzdan emin olun. Ardından sunucunuz olacak bir Python dosyası oluşturun. Bu dosyanın adını `app.py` yapalım.

---

## 🧩 İlk Flask Uygulamasını Yazma

Bu dosyaya kodu yazalım. Önce küçük f `flask` modülünden büyük F `Flask` sınıfını içe aktarın. Sonra `Flask` sınıfından bir nesneyi uygulamanız (`app`) olarak başlatın. Kurucu (constructor) `Scaffold` sınıfından tek bir argüman alır. İsmi (name) scaffold içinde, yerleşik `__name__` değişkenindeki uygulama modülünün adını geçirerek ayarlarsınız. Bu isim, dosya sistemindeki kaynakları bulmak ve eklentiler (extensions) tarafından hata ayıklama bilgisi sağlamak için kullanılır.

Artık sunucunuzu tanımladığınıza göre, ilk rotayı ekleyelim.

---

## 🛣️ İlk Route Oluşturma

Sunucunuzu bir yol (path) eklemeden çağırdıklarında istemciye bir mesaj döndürmek istiyorsunuz. Bir rota tanımlamak için `@app` decorator’ını kullanmanız gerekir. Decorator yolu argüman olarak alır. Son olarak, metottan metin veya HTML döndürebilirsiniz.

Koda bakalım. `@app` decorator’ı `hello_world` metodunun üzerinde tanımlanmıştır. `"/"` argümanını alır ve kalın olarak `"my first Flask application in action!"` HTML mesajını döndürür.

---

## ▶️ Uygulamayı Çalıştırma ve Ortam Değişkenleri

Sonraki adım uygulamanızı çalıştırmaktır. İlk adım birkaç sistem ortam değişkeni (environment variable) oluşturmaktır. Ana sunucu dosyasının adını içeren bir `FLASK_APP` değişkenine ihtiyacınız var. Ayrıca geliştirme (development) ya da üretim (production) ortamını tanımlayacak bir `FLASK_ENV` değişkenine ihtiyacınız var. Bu değişken Flask 2.3’te kullanımdan kaldırılacaktır (deprecated).

Gördüğünüz gibi `FLASK_APP` ortam değişkenini merkezi sunucuyu içeren dosya adı olarak ve `FLASK_ENV` değerini `development` olarak tanımladınız. Son olarak uygulamayı çalıştırmak için, `Flask` çerçevesine `run` argümanını `'Flask run'` komutunu çalıştırarak verin.

```bash
Flask run
```

Flask uygulaması varsayılan olarak 5000 portunda çalışır. Mesajınızı görmek için `http://localhost:5000` adresine gidebilirsiniz.

---

## 🔎 Tarayıcı Geliştirici Araçları ile Yanıtı İnceleme

Sunucunuzdan hangi bilginin döndüğünü görmek için tarayıcı geliştirici araçlarını da kullanalım. İstenen URL `http://localhost:5000`’dir. İstek metodu HTTP GET’tir. Yanıtın durumu 200’dür; bu başarılı bir yanıtı gösterir. Yanıt başlığındaki content type `"text/html"`’dir.

Sunucu, Python 3.6.15 sürümüyle çalışan Werkzeug’tur. İlk Flask uygulamanızı çalıştırdığınız için tebrikler. Uygulamanızı çalıştırmadan önce her uygulama için ortam değişkenlerini ayarlamanız gerekir.

---

## ⚙️ Komut Satırı ile Konfigürasyon Geçme

`"--app"` kullanarak çalıştırılacak Python dosyasını belirtip `flask` komutuna yapılandırma geçebilirsiniz. Geliştirme modunu etkinleştirmek için `"--debug"` ekleyin. Debug bayrağı ayrıca kaynak dosyalar değiştiğinde otomatik yeniden başlatmaları etkinleştirir ve uygulama geliştirirken değişikliklerinizi anında görmek istediğinizde kullanışlıdır.

Sizin durumunuzda uygulama `app.py` adlı bir dosyada saklanır, bu yüzden bu argümanı atlayabilirdiniz; çünkü Flask varsayılan olarak geçerli dizinde `app.py` arar. Çıktı buna benzer görünmelidir. Ekran, Flask uygulamasının daha önce olduğu gibi geliştirme modunda çalıştığını gösterir.

---

## 🧾 Flask’te JSON Döndürmenin Yolları

Flask uygulamanızdan JSON döndürmenin birden fazla yolu vardır.

### 1) Serileştirilebilir Nesne Döndürme

Bir yöntem, sözlük (dictionary) veya liste (list) gibi serileştirilebilir bir nesne döndürmektir. Verilen kodda bir Python sözlüğü döndürürsünüz. Flask, istemciye JSON döndürmek için Python JSON modülünü kullanacaktır.

Bunun çalışıp çalışmadığını `curl` komutunu kullanarak test edelim. `localhost:5000` adresine bir GET isteği yapacaksınız. 200 OK yanıt durumunu görebilirsiniz. HTML yerine `"application/JSON"` content type’ını da görebilirsiniz. Son olarak döndürülen JSON’u görebilirsiniz.

```bash
curl http://localhost:5000
```

Daha karmaşık bir nesne (örneğin bir sınıf) döndürüyorsanız, serileştirilebildiğinden emin olun.

### 2) `jsonify` Metodunu Kullanma

İkinci yol, Flask’in sağladığı `jsonify` metodunu kullanmaktır. Bu metot girdi olarak anahtar-değer çiftleri alır ve uygun JSON’u döndürür.

Bir örneğe bakalım. Önce Flask’ten `jsonify` içe aktarılır. Ardından anahtar-değer çiftleri `jsonify` içine geçirilir. Tarayıcıda daha öncekiyle aynı sonucu almalısınız. Geliştirici araçları da 200 OK durum kodunu ve `"application/JSON"` content type’ını döndürerek aynı görünmelidir.

---

## 🧰 Flask Konfigürasyon Seçenekleri

`FLASK_ENV` ve `FLASK_APP` değişkenleriyle iki yapılandırmaya baktınız. Flask, uygulamanızda kullanabileceğiniz çeşitli diğer yapılandırma seçenekleri sunar:

* `ENV` – Uygulamanın çalıştığı ortamı (production veya development) belirtir.
* `DEBUG` – Debug modunu etkinleştirir.
* `TESTING` – Test modunu etkinleştirir.
* `SECRET_KEY` – Oturum çerezini (session cookie) imzalamak için kullanılır.
* `SESSION_COOKIE_NAME` – Oturum çerezinin adı.
* `SERVER_NAME` – Host ve portu bağlar.
* `JSONIFY` – Varsayılan olarak `'application/JSON'`.

Ayrıca Flask’te yapılandırma seçenekleri sağlamanın başka yolları da vardır. Flask bir `config` nesnesi sağlar. Yapılandırma seçeneklerini bu nesneye ekleyebilirsiniz. Eğer zaten ortam değişkenleriniz varsa, bunları `config` nesnesine yükleyebilirsiniz.

Son olarak, yapılandırma seçeneklerini ayrı bir JSON dosyasında tutabilir ve `config` nesnesinin sağladığı `"from_file"` metodunu kullanarak yükleyebilirsiniz.

---

## 🗂️ Uygulama Büyüdükçe Dizin Yapısı

Uygulamanız büyüdükçe tek bir Python dosyası kullanmak yerine bir dizin yapısı oluşturmalısınız. Uygulamanızı yapılandırmanın birçok yolu vardır. İşte bir örnek: Ana kaynak kodunu modül dizininde saklayın ve tüm yapılandırmaları kendi dosyasında tutun. Görsel, JavaScript ve CSS gibi tüm statik varlıkları ayrı saklayın. Tüm dinamik içeriği bir template dizininde saklayın. Tüm test dosyalarını bir test dizininde konumlandırın ve doğru bağımlılık sürümünü kurmak için etkinleştirilebilen bir sanal ortam (virtual environment) bulundurun.

---

## ✅ Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz: `Flask` sınıfını başlatarak bir sunucu oluşturabileceğinizi, `@app` decorator’ını kullanarak URL işleyicileri (handlers) oluşturabileceğinizi, string mesajlar döndürebileceğinizi veya JSON nesneleri döndürmek için `jsonify()` metodunu kullanabileceğinizi ve uygulama konfigürasyonunu ortam değişkenlerinden, Python dosyalarından ve `app.config` nesnesinden doğrudan ayarlayabileceğinizi.
