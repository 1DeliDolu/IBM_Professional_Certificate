# 🧩 Dynamic Rotalar (Dynamic Routes)

“Dynamic Routes” dersine hoş geldiniz. Bu videoyu izledikten sonra şunları yapabileceksiniz: Flask’te harici bir API’nin nasıl çağrılacağını açıklamak ve Flask’te rotalara parametrelerin nasıl geçirileceğini açıklamak.

---

## 🌐 Flask’te Harici API Çağırma

Flask’te harici bir API’yi nasıl çağırabileceğinize dair bir örneğe bakalım. En kolay yol Python *requests* kütüphanesini kullanmaktır.

Harici API’den dönen  *JSON* ’u doğrudan istemcinize geri döndürebilirsiniz. Ancak, istemciye göndermeden önce sonuçları işleyebilirsiniz.

Bu örnekte önce *flask* ve *request* modüllerini içe aktarırsınız.

Kod burada *requests* kütüphanesini zaten yüklediğinizi varsayar. Sonra rotanızı tanımlayabilirsiniz. *requests* kütüphanesini kullanarak  *openlibrary API* ’sine istek atar ve yazar Michael Crichton hakkında bilgi ararsınız. Yanıtı *res* adlı bir değişkende saklarsınız.

Ardından,  *openlibrary API* ’sinden gelen yanıtın *status code* değerinin 200 olup olmadığını kontrol edersiniz. Yanıt 200 ise  *JSON* ’u istemciye döndürürsünüz. Yanıt 404 olursa “Something went wrong." mesajı gönderirsiniz.

Son olarak, bu varsayımsal durumda yanıt başka bir şey ise 500 durumuyla birlikte “Server error.” mesajını döndürürsünüz.

---

## 🧷 RESTful API’lerde Resource-ID Kullanımı ve Dinamik Rotalar

RESTful API geliştirirken, istek URL’inin bir parçası olarak bir *resource-id* gönderebilirsiniz.

Örneğin, International Standard Book Number ( *ISBN* ) ile kitap bilgisi döndüren bir endpoint oluşturmak istiyorsunuz; ancak ISBN’yi *hard code* etmek yerine, istemcinin bunu URL’in parçası olarak göndermesini istiyorsunuz. Flask bu amaçla *dynamic routing* sağlar.

Somut bir örneğe bakalım: URL’in dinamik bir parçası olarak *isbn* adlı değişkeni eklersiniz. Sonra bu değişkeni  *openlibrary API* ’sine geçirirsiniz. Sonuç daha sonra istemciye gönderilir.

---

## 🧱 Parametre Tipleri ve Doğrulama

Flask ayrıca parametre tipini ayarlamanıza izin verir. Framework bu bilgiyi gelen istekleri doğrulamak için kullanır.

Örneğin, San Francisco havaalanındaki terminal sayısını almak için *terminals* ve *SFO* endpoint’i oluşturabilirsiniz. Bu  *route decorator* , kullanıcı URL’in sonuna bir *string* gönderirse tetiklenir.

Benzer şekilde, önceki örnekte ISBN’nin bir sayı olmasını sağlayabilirsiniz.

Flask’te bazı diğer parametre tiplerine örnekler şunlardır:  *string* , *int* ve *float* basit parametrelerken; *path* gibi web yolu veya klasör yolu belirtmek için kullanılan karmaşık tipler ya da Universal unique identifier ( *UUID* ) gibi Globally Unique Identifier ( *GUID* ) benzeri benzersiz bir kimliği belirtmek için kullanılan tipler de vardır.

---

## 🆔 UUID Örneği

UUID için bir örnek burada verilmiştir.

Ağ hakkında bilgi almak için belirli bir UUID içeren “network” endpoint’ini oluşturabilirsiniz. Şu şekilde bir kod yazabilirsiniz: rota, *uuid* tipinde bir değişken *uuid* bekler; bu *uuid* metoda argüman olarak geçirilir; *uuid* bulunursa bir başarı mesajı döndürürsünüz, aksi halde uygun bir mesajla bir hata kodu döndürürsünüz.

---

## ✅ Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* Query parametrelerini, body’yi ve diğer argümanları almak için  *Request Object* ’i ayrıştırabilirsiniz.
* Yanıtı istemciye göndermeden önce *Response object* üzerinde status ayarlayabilirsiniz.
* RESTful endpoint’ler oluşturmak için *dynamic routes* kullanabilirsiniz.
