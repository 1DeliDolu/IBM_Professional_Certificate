## 🌱 Your First Express Web Application

Your First Express Web Application uygulamanıza hoş geldiniz. Bu videoyu izledikten sonra, Express kullanarak bir uygulama oluşturabilecek ve Express’i yüklemek için beş adımı tanımlayabileceksiniz.

![1768335214735](image/5_YourFirstExpressWebApplication/1768335214735.png)

Express ile çalışmak için bu beş adımı izleyin:

1. Express’i Node.js projenizin paket bildiriminde ( *package manifest* ) bir bağımlılık ( *dependency* ) olarak tanımlayın.
2. Eksik modülleri indirmek için `npm` komutunu çalıştırın.
3. Express modülünü içe aktarın ( *import* ) ve bir Express uygulaması oluşturun.
4. Yeni bir rota işleyicisi ( *route handler* ) oluşturun.
5. Belirli bir port numarası üzerinde bir **Hiper Metin Aktarım Protokolü (HTTP)** sunucusu başlatın.

Express’i Node.js projenizde bir bağımlılık olarak tanımlayıp eksik modülleri indirdiğinizde, proje klasörünüzde bir `mynodeserver.js` dosyası oluşturabilirsiniz.

![1768335241519](image/5_YourFirstExpressWebApplication/1768335241519.png)

---

## 🧩 İlk Express Programınızla Kodlamaya Başlama

Artık ilk Express programınızla kodlamaya başlayabilirsiniz. Bu örnekte, mevcut hava durumu koşullarını almak için bir program yazıyorsunuz.

![1768335272797](image/5_YourFirstExpressWebApplication/1768335272797.png)

Express web uygulama çatısının ( *framework* ) bir kopyasını içe aktardıktan sonra, çatıdan ( *framework* ) `app` JavaScript nesnesinin bir örneğini ( *instance* ) oluşturun.

![1768335310689](image/5_YourFirstExpressWebApplication/1768335310689.png)

Ardından, yeni bir rota işleyicisi ( *route handler* ) oluşturun.

![1768335323807](image/5_YourFirstExpressWebApplication/1768335323807.png)

Uygulamanızda web uygulaması isteklerini işlemek için, bir HTTP yöntemini ve bir web kaynak yolunu ( *web resource path* ) JavaScript fonksiyonuna eşleyin.

Burada, gelen HTTP **GET** isteklerini dinliyorsunuz; bu istekler `temperature` kaynak yoluna istek yapar.

Ayrıca, `temperature` kaynak yolundan sonra gelen değeri `location_code` adlı bir değişkende saklıyorsunuz.

![1768335367799](image/5_YourFirstExpressWebApplication/1768335367799.png)

---

## 🧷 Path Parametreleri ve Değişken Kullanımı

Yoldaki ( *path* ) değişkene `request.params.location_code` kullanarak erişebilir ve değeri “location” adlı bir konum değişkenine saklayabilirsiniz.

`weather.current` fonksiyonunu çalıştırdığınızda, kaynak yolundan alınan `location` parametresini geçirirsiniz.

![1768335394797](image/5_YourFirstExpressWebApplication/1768335394797.png)

---

## 🚀 HTTP Sunucusunu Başlatma

Son adımda, belirli bir port numarası üzerinde bir HTTP sunucusu başlatırsınız.

Sunucunun bir örneğini ( *instance* ) `app` üzerinden oluşturmak için, belirtilen port üzerinde gelen istekleri dinleyen bir web sunucusu nesnesi (yani bir örnek) oluşturmak üzere `app.listen` çağrısı yapın.

![1768335419812](image/5_YourFirstExpressWebApplication/1768335419812.png)

`app` gelen istekleri dinler; örneğin, **8080** portunda.

İkinci parametre, Express çatısının ( *framework* ) sunucu nesnesinin bir örneğini oluşturduğunda çağırdığı anonim bir fonksiyonu tanımlar.

![1768335448198](image/5_YourFirstExpressWebApplication/1768335448198.png)

Sonuç için, tarayıcınızda **uniform resource locator (URL)** değerini girin.

![1768335460786](image/5_YourFirstExpressWebApplication/1768335460786.png)

---

## ✅ Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

Express’i Node.js projenizde bir bağımlılık olarak tanımlayıp eksik modülleri indirdiğinizde, bir uygulama oluşturabilir ve Express ile kodlamaya başlayabilirsiniz.

Ayrıca Express’i yüklemek için beş adım vardır:

1. Express’i bir Node.js projesinin paket bildiriminde ( *package manifest* ) bir bağımlılık ( *dependency* ) olarak tanımlayın.
2. Eksik modülleri indirmek için `npm` komutunu çalıştırın.
3. Express modülünü içe aktarın ( *import* ) ve bir Express uygulaması oluşturun.
4. Yeni bir rota işleyicisi ( *route handler* ) oluşturun.
5. Belirli bir port numarası üzerinde bir HTTP sunucusu başlatın.

![1768335499867](image/5_YourFirstExpressWebApplication/1768335499867.png)
