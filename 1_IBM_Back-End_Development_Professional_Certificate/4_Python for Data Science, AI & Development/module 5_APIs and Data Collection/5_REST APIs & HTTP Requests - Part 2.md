# 🌐 REST API'ler & HTTP İstekleri - Bölüm 2

## 📚 `requests` Kütüphanesiyle HTTP Protokolü

Bu videoda, Python'da HTTP protokolüyle çalışmak için kullanılan popüler bir yöntem olan `requests` kütüphanesini kullanarak `HTTP` protokolünü tartışacağız.

`HTTP` protokolleriyle çalışmak için Python `requests` kütüphanesini gözden geçirecek ve `GET` istekleri ile `POST` isteklerine genel bir bakış sağlayacağız.

Şimdi Python'daki *request* modülünü gözden geçirelim. Bu, `HTTP` protokolüyle çalışabilen, `HTTPlib` ve `urllib` dâhil birkaç kütüphaneden biridir.

`Requests`, `HTTP/1.1` isteklerini kolayca göndermenizi sağlayan bir Python kütüphanesidir. Kütüphaneyi aşağıdaki gibi içe aktarabiliriz. `www.ibm.com` adresine `GET` yöntemi aracılığıyla bir `GET` isteği yapabilirsiniz.

## 📦 Yanıt Nesnesi `R` ve İstek Bilgileri

Elimizde `R` adlı yanıt nesnesi ( *response object* ) vardır. Bu nesne, isteğin durumu gibi istekle ilgili bilgileri içerir.

Durum kodunu, *status underscore code* özniteliğini (`status_code`) kullanarak görebiliriz; bu, başarı için `200` değerini alır. İstek başlıklarını ( *request headers* ) görüntüleyebilirsiniz.

Aşağıdaki satırda istek gövdesini ( *request body* ) görüntüleyebilirsiniz. `GET` isteği için bir gövde olmadığından, `None` elde ederiz. `HTTP` yanıt başlığını, `headers` özniteliğini kullanarak görüntüleyebilirsiniz.

## 🧾 Yanıt Başlıkları, Tarih, Tür ve Kodlama

Bu, `HTTP` yanıt başlıklarının yer aldığı bir Python sözlüğü ( *dictionary* ) döndürür. Sözlüğün değerlerine bakabiliriz.

İsteğin gönderildiği tarihi, `date` anahtarını ( *key* ) kullanarak elde edebiliriz. `content type` anahtarı, verinin türünü belirtir.

`R` yanıt nesnesini kullanarak kodlamayı ( *encoding* ) da kontrol edebiliriz. İçerik türü metin veya HTML olduğundan, gövdedeki HTML'yi göstermek için `text` özniteliğini kullanabiliriz. İlk 100 karakteri inceleyebiliriz.

## 🌐 `GET` Metodu ile İçerik Alma

Ayrıca başka içerikler de indirebilirsiniz. Daha fazlası için laboratuvar çalışmasına ( *lab* ) bakın.

Sorgunuzun sonuçlarını değiştirmek için, örneğin bir API'den veri almak amacıyla `GET` yöntemini kullanabilirsiniz. Laboratuvarda, basit bir `HTTP` istek ve yanıt hizmeti olan `httpbin.org`'u kullanacağız.

Sunucuya bir `GET` isteği göndeririz. Daha önce olduğu gibi, rotada ( *route* ) temel `URL` ( *base URL* ) bulunur. Sonuna `/get` ekleriz.

## 🔤 Sorgu Dizeleri ( *Query String* ) ve URL Parametreleri

Bu, bir `GET` isteği gerçekleştirmek istediğimizi belirtir. Bu durum aşağıdaki tabloda gösterilmiştir.

`GET` istendikten sonra, elimizde bir sorgu dizesi ( *query string* ) olur. Bu, bir *Uniform Resource Locator* ya da `URL`'nin bir parçasıdır ve web sunucusuna başka bilgiler gönderir.

Sorgu, bir soru işaretiyle başlar ve aşağıdaki tabloda gösterildiği gibi parametre ve değer çiftlerinden oluşan bir dizi ile devam eder. İlk parametrenin adı `name`, değeri ise `Joseph`tir. İkinci parametrenin adı `ID`, değeri ise `123`tür.

## 🧮 `payload` Sözlüğüyle Sorgu Dizisi Oluşturma

Her parametre–değer çifti bir eşittir işaretiyle (`=`) ayrılır. Çiftlerden oluşan seri, `&` işareti ( *ampersand* ) ile birbirinden ayrılır.

Python'da bir örneği tamamlayalım. Sonuna `GET` eklenmiş bir temel `URL`miz vardır.

Bir sorgu dizesi oluşturmak için `payload` adlı sözlüğü ( *dictionary* ) kullanırız. Anahtarlar parametre adlarıdır, değerler ise sorgu dizesindeki değerlerdir.

Daha sonra `payload` sözlüğünü, `GET` işlevinin `params` parametresine geçiririz.

## 📥 Yanıtın Metin ve JSON Olarak İncelenmesi

Adı ( *name* ) ve değerleri görmek için `URL`yi yazdırabiliriz. İstek gövdesini görebiliriz.

Bilgi `URL` içinde gönderildiğinden, gövdenin değeri `None` olur. Durum kodunu yazdırabiliriz.

Yanıtı metin olarak görüntüleyebilir ve içerik türüne bakmak için `content type` anahtarına göz atabiliriz. İçerik türü `JSON` içinde bulunduğundan, onu `JSON` yöntemi (`json`) kullanarak biçimlendiririz.

Bu yöntem bir Python sözlüğü ( *dict* ) döndürür. `args` anahtarı, sorgu dizesi için ad ve değerleri içerir.

## 📤 `POST` İsteğiyle Sunucuya Veri Gönderme

`GET` isteğinde olduğu gibi, `POST` isteği de bir sunucuya veri göndermek için kullanılır; ancak `POST` isteği veriyi `URL` içinde değil, istek gövdesinde gönderir.

`POST` isteğini bu `URL`ye göndermek için, rotayı `POST` olacak şekilde değiştiririz. Bu uç nokta ( *endpoint* ) veri bekleyecektir ve bir sunucuya veri göndermek üzere bir `HTTP` isteğini yapılandırmanın uygun bir yoludur.

Elimizde `payload` sözlüğü vardır. Bir `POST` isteği yapmak için `POST` işlevini kullanırız. `payload` değişkeni, `data` parametresine geçirilir.

## ⚖️ `GET` ve `POST` İsteklerinin Karşılaştırılması

`GET` ve `POST` yanıt nesnelerinin `URL` özniteliğini (`url`) kullanarak `URL`leri karşılaştırdığımızda, `POST` isteğinin `URL`si içinde hiçbir ad veya değer çifti olmadığını görürüz.

`POST` ve `GET` istek gövdelerini karşılaştırabiliriz. Yalnızca `POST` isteğinin bir gövdesi olduğunu görürüz.

Ve `payload` değerini elde etmek için `form` anahtarını görüntüleyebiliriz.
