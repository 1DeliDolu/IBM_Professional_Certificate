# 🧯 Hata Yönetimi (Error Handling)

“Error Handling” dersine hoş geldiniz. Bu videoyu izledikten sonra şunları yapabileceksiniz: API servislerinin döndürebileceği farklı HTTP status kodlarını tanımlamak, Flask’te hata yönetiminin nasıl çalıştığını açıklamak ve API endpoint’lerinizden hataların nasıl döndürüleceğini açıklamak.

---

## 🔢 HTTP Status Kodları

Her HTTP response, farklı hata ve başarı durumlarını belirten üç haneli bir kod içerir. İstemci bu hata kodunu tüketmekten sorumludur. Geçerli response kod aralığı 100 ile 599 arasındadır. Hata kodları, her bir yüzlük dilim halinde kategorilere ayrılmıştır.

100 ile 199 arasındaki error kodları, isteğin alındığını gösterir ve bilgilendiricidir.

200 ile 299 arasındaki error kodları, isteğin alındığını ve istenen işlemin başarılı olduğunu gösterir.

300’lü kodlar, sunucuda bir yönlendirme (redirection) olduğunu gösterir.

400 ile 499 aralığındaki kodlar, istekte (request) bir hata olduğunu gösterir.

Son olarak, 500 ile 599 arasındaki kodlar sunucu tarafında bir hata olduğunu gösterir.

Bu kursta yazacağınız API’ler bu adlandırmayı takip edecektir. Örneğin, istemci kullanılabilir olmayan bir kaynak için GET isteği gönderirse 404 response geri gönderebilirsiniz. Yanlış istekler için 400 status ile yanıt verebilirsiniz.

---

## ✅ Flask’te Varsayılan Status Kodları

Flask sunucusu, `@app.route` metodundan döndüğünüzde otomatik olarak `200 OK` status döndürür. Bir isteğe yanıt vermek için `jsonify()` metodunu kullandığınızda da varsayılan olarak `200` döndürülür.

Verilen kod çalıştığında, `200` status kodlu başarılı bir response geri gönderilir. Kodunuz varsayılan olandan farklı bir kod döndürebilir. Flask, response ile birlikte status kodunu bir tuple içinde göndermenize izin verir.

Kodda, `"my first application in action!"` HTML response’u `200` status koduyla geri gönderirsiniz.

Status kodunu açıkça ayarlamak için `make_response()` metodunu da kullanabilirsiniz. Bu kod, önceki kodla aynı HTML mesajını ve `200` HTTP status’unu döndürür; ancak burada `make_response()` metodunu kullanırsınız.

---

## 🧾 Bu Kursta Kullanabileceğiniz Bazı Status Kodları

`200` status’u varsayılan olarak döndürülür. İsteğin başarılı olduğunu belirtir.

`201`, sunucunun kaynağı başarıyla oluşturduğunu (created) istemciye bildirir.

`202`, isteğin kabul edildiğini ve işlemde olduğunu belirtir; batch processing işlemleri için yaygındır.

Sunucu, bir isteği başarıyla tamamladıktan sonra `204` döndürür; içerik (no content) geri döndürülmez. Bu status, tarayıcının herhangi bir aksiyon almasını istemediğiniz durumlarda kullanışlıdır. Örneğin, kullanıcı mevcut sayfasında kalır.

`400`, geçersiz bir isteği (invalid request) belirtir. Bu status, parametrelerin eksik veya uygunsuz olmasını ya da isteğin başka bir şekilde geçersiz olmasını ifade edebilir.

`401`, kimlik bilgilerinin (credentials) eksik veya geçersiz olduğunu belirtir.

`403`, istemci kimlik bilgilerinin isteği yerine getirmek için yeterli olmadığını belirtir.

Sunucu kaynağı bulamazsa `404` status döndürür.

`405`, istenen işlemin desteklenmediğini belirtir.

`500`, sunucuda bir hata olduğunda kullanılır.

---

## 🧪 Doğru Status Kodunu Döndürme Örneği

Artık farklı HTTP kodlarını bildiğinize göre, bir geliştirici olarak servisten doğru kodu döndürmeniz gerekir. Bir örneğe bakalım.

Bu `search_response` metodu, veritabanının query parametresi olan `q`’yu arar. Servis, query’yi parse ettikten sonra sahte (mock) `"fetch_from_database"` metodunu çağırır.

Kod, kaynak mevcutsa kaynağı istemciye döndürür. Sunucu `200` kodunu örtük olarak döndürür ve kaynak bulunamazsa `404` döndürür.

---

## 🧰 curl ile Endpoint Çağırma

Bu endpoint’i `curl` programını kullanarak çağıralım.

Query parametresi olmadan route’u çağırın. `curl` komutu `"input parameter missing"` mesajını `422` status ile döndürür.

Ardından route’u doğru resource ID ile çağırın. `curl` komutu body olarak kaynağı ve `200` status’unu döndürür.

Son olarak, var olmayan bir kaynakla route’u çağırın. `curl` komutu `"resource not found"` mesajını `404` status ile döndürür.

---

## 🧩 Flask’te Uygulama Seviyesinde Error Handler’lar

Flask, error mesajlarını uygulama seviyesinde yönetmek için bir yol sağlar. Burada, `404` hatasını işleyen ve `"API not found"` mesajını `404` status koduyla döndüren bir metot görürüz.

Benzer şekilde, bu parça `500` hataları için bir error handler oluşturur ve `"something went wrong on the server."` mesajını döndürür.

---

## 🧾 Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* HTTP response, isteğin işlendiğinde ne olduğunu belirtmek için bir status code gerektirir.
* Başarıyı, kullanıcı hatasını veya sunucu hatasını gösteren birden fazla HTTP status kod sınıfı vardır.
* Flask, response ile birlikte örtük olarak `200` başarı kodu döndürür.
* Status kodlarını açıkça sağlayabilirsiniz.
* Flask, uygulama seviyesinde error handler’lar sağlar.
