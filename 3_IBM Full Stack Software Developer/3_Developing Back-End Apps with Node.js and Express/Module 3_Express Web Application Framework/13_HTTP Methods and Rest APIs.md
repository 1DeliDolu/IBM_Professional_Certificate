## 🌐 HTTP Yöntemleri ve REST API’leri

**Tahmini gerekli süre:** 30 dakika

---

## 🎯 Amaçlar

Bu dokümanı okuduktan sonra şunları yapabiliyor olmalısınız:

* HTTP yöntemleriyle ilgili terimleri tanımlamak
* REST API’leri yazmak için yönergeleri ve en iyi uygulamaları açıklamak

---

## 🧩 İstemci-Sunucu Mimarisi ve HTTP

İnternet, bir istemci-sunucu mimarisine dayanır. Son kullanıcı istemciyle etkileşime girerken, sunucular uygulamaları çalıştıran servisleri1, iş mantığını ve veriyi barındırır. İstemciler, son kullanıcı için istenen işlevselliği elde etmek üzere sunucularla iletişim kurar. Veri, istemci ile sunucu arasında **hypertext transfer protocol** ile, daha yaygın adıyla **HTTP2** kullanılarak aktarılır. Bu iletişim genellikle **API’ler3** aracılığıyla gerçekleşir.

2000 yılında, istemci-sunucu mimarisi için bu API’leri yazmaya yönelik bir yönergeler seti geliştirildi ve bunlara **REST4 API’ler** adı verildi.

“REST” kısaltması **REpresentational State Transfer** anlamına gelir. Bu terimi daha ayrıntılı açıklamadan önce, önce HTTP yöntemlerini ve bazı terminolojiyi ele alalım.

---

## 🧱 Kaynaklar, Route, Endpoint ve Request/Response

Bir istemci/sunucu mimarisinde uygulamalar, sunucularda bulunan bir veya daha fazla servisten oluşur. Bu servisler **kaynaklar5** içerir. İstemci, bir kaynak için bir **istek6** yapar; bunu, servis içindeki bir **endpoint9** barındıran bir **route8** kullanarak bir **request object7** üzerinden gerçekleştirir. Uygulama, bu isteği yerine getirmek için istemciye bir **response object10** gönderir11.

Bir request object üç bölüm içerir: bir  **URL12** , bir **request header13** ve bir  **request body14** . Sunucu, URL’yi; servis ve servis içinde üzerinde işlem yapılan endpoint’i tanımlamak için kullanır. URL dört bölüm içerir: bir  **protocol15** , bir  **hostname16** , bir **path17** ve bir  **query string18** . Request header, istekte bulunan istemcinin kaynağına ilişkin metaveri içerir; örneğin  **user agent19** ,  **host20** ,  **content type21** , **content length22** ve istemcinin yanıtta hangi tür veriyi beklemesi gerektiği.

Sunucu, bir **response object** ile yanıt verir; bu nesne bir  **header23** , bir **body24** ve bir **status code25** içerir. Response object body’si, istemciye veriyi geri sağlamak için çoğunlukla bir **JSON26 payload27** içerir.

---

## 🧰 REST API’lerde Kullanılan HTTP Yöntemleri

REST API’de istemci ile bir servis arasında etkileşime izin veren bir dizi HTTP yöntemi kullanılabilir. En yaygın yöntemler  **GET28** ,  **POST29** ,  **PUT30** , **DELETE31** ve  **PATCH32** ’tir.

Yöntemin adı, yöntem uygulandığında kaynağa ne olduğunu açıklar. Aynı API yöntemi birden çok kez çağrıldığında **PUT** ve **DELETE** yöntemleri **idempotent33** veri ile sonuçlanır.

HTTP’nin parametre aktarmak için üç yolu vardır:  **URL path parameter34** , **URL query parameter35** ve  **header parameter36** . Path ve query parametreleri URL’nin bir parçası olarak aktarılır; header parametresi ise tarayıcı tarafından doğrudan servise gönderilir.

---

## 🧾 HTTP Status Code Kategorileri

Bir servis bir isteği tamamladığında bir yanıt döndürür. HTTP status code, bu yanıtın bir parçası olmalıdır. HTTP status code, yanıtın tamamlanıp tamamlanmadığını belirtir. Yanıt kodu kategorileri aşağıdaki tabloda gösterilmiştir.

| Status Code Aralığı | Anlamı               |
| ---------------------- | --------------------- |
| 200-299                | Her şey yolunda      |
| 300-399                | Kaynak taşındı     |
| 400-499                | İstemci tarafı hata |
| 500-599                | Sunucu tarafı hata   |

---

## 🧭 RESTful Olma Gereksinimleri

Daha önce belirtildiği gibi REST bir yönergeler setidir. Bir API’nin RESTful sayılabilmesi için beş gereksinim ve bir isteğe bağlı kriter vardır:

1. API, HTTP üzerinden yönetilen ve teslim edilen kaynaklardan oluşan bir istemci-sunucu mimarisinden yararlanır.
2. İstemci ile sunucu arasındaki iletişim  **stateless37** ’tir.
3. Performansı istemci tarafında artırmak için veri  **cacheable38** ’dır.
4. Arayüz standart bir formatta aktarılır; böylece sunucuda saklanan istenen kaynaklar, istemciye gönderilen temsilden ayrıdır. İstemciye gönderilen temsil, istemcinin temsili manipüle edebilmesi için yeterli veri içerir.
5. İstekler ve yanıtlar, **middleware39** gibi farklı katmanlar üzerinden iletişim kurar. İstemci ve sunucu sıklıkla doğrudan birbirleriyle iletişim kurmaz.
6. (İsteğe bağlı) Kaynaklar genellikle statiktir ancak çalıştırılabilir kod da içerebilir. Kod yalnızca istemci talep ettiğinde çalıştırılmalıdır.

İstemci bir istek yaptığında, durumuna ilişkin bilgiyi de sunucuya iletmelidir. İstemci ile sunucu arasındaki her iletişim, isteği gerçekleştirmek için gereken tüm bilgiyi içermelidir. Durumu servis değil, istemci korur. Her istek, sunucunun isteği anlayabilmesi için gerekli bilgiyi içermelidir. Örneğin kullanıcı bir veritabanı kaydını görüntülüyorsa ve bu kaydın güncellenmesi gerekiyorsa, istemci hangi kaydın güncelleneceğini de göndermelidir. Sunucu, o anda hangi kaydın görüntülendiğini bilmez.

---

## 🧷 RESTful Servis Tanımlama

RESTful bir servis tanımlanırken `@app.route()` metodu kullanılır. Bu metot iki parametre alır: üzerinde işlem yapılan servise URL’den giden route ve  **POST** , **GET** gibi isteğe bağlı bir HTTP yöntem parametresi.

Route parametresi `<username>` gibi değişkenler içerebilir. Bir route’un kökü `'/'` ile gösterilir. Örneğin route’un `www.mywebsite.com/accounts` olmasını istiyorsanız, `@app.route()` fonksiyonunda route parametresi olarak yalnızca `'/accounts'` belirtmeniz yeterlidir.

---

## 🧱 REST API Özellikleri

REST API’ler aşağıdaki özelliklere sahiptir:

* Kaynak tabanlıdır; yani kaynak kümelerini tanımlar
* Yalnızca isimler ( *nouns* ) içerir, fiiller ( *verbs* ) içermez
* Tekil bir kaynaktan bahsederken tekil isimler, bir kaynak koleksiyonundan bahsederken çoğul isimler kullanır
* Her zaman URL’lerle tanımlanır

---

## ✅ RESTful Olmayan ve RESTful Eşdeğerleri

| RESTful olmayan API’ler                    | RESTful eşdeğerleri                     |
| ------------------------------------------- | ----------------------------------------- |
| `GET http://api.myapp.com/getUser/123`    | `GET http://api.myapp.com/users/123`    |
| `POST http://api.myapp.com/addUser`       | `POST http://api.myapp.com/users`       |
| `GET http://api.myapp.com/removeUser/123` | `DELETE http://api.myapp.com/users/123` |

---

## 🧾 URL Biçim Yönergeleri

* Dizin yapısında hiyerarşik ilişkiyi belirtmek için `'/'` eğik çizgisini kullanmalıdır
* Sonda eğik çizgi kullanmaktan kaçınmalıdır; ör. `/resource/`
* Camel case değil, tire ( *hyphen* ) kullanmalıdır; ör. `/my-resource`, `/myResource` değil
* URL’de alt çizgi (`'_'`) kullanmamalıdır; ör. `/my-resource`, `/my_resource` değil
* Küçük harf kullanmalıdır
* URL’de nokta (`'.'`) kullanmamalıdır
* URL’de birden fazla alt kaynak ve ID içerebilir; ör. `GET /resource/{id}/subordinate/{id}`

---

## 📚 Terimler ve Tanımlar

| Terim                   | Açıklama                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Service              | Bir uygulamanın bir bölümünü oluşturan ve belirli bir amaca hizmet eden bir yazılım bileşeni. Genellikle bir servis, bir istemciden veya başka bir servisten girdi alır ve bir çıktı üretir.                                                                                                                                                                                                                                                                                                                                  |
| 2. HTTP                 | İnternette istemci-sunucu mimarisinde kaynak verisini getirmek veya değiştirmek için kullanılan protokol.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 3. API                  | **Application Programming Interface** , iki servisin birbiriyle iletişim kurmasını sağlayan tanımlar ve protokoller kümesidir. API, bir kaynak ile o kaynaktan döndürülen sonuçlar arasında değiş tokuş edilebilecek veriyi ister.                                                                                                                                                                                                                                                                                       |
| 4. REST                 | Genellikle bir istemci ve sunucu olmak üzere iki bileşen arasındaki arayüzün (API) nasıl yazılacağını tanımlayan bir mimari yönergeler seti. REST,**REpresentational State Transfer**anlamına gelir. REST, kaynakların standart bir şekilde tanımlanmasını ve manipüle edilmesini açıklar. REST, istemci ile sunucu arasında iletilen mesajların kendini tanımlayıcı olmasını ve istemcinin sunucudaki kaynaklara erişmek için nasıl etkileşime girdiğini belirtmesini sağlar.                       |
| 5. Resource             | RESTful bir API’nin temel kavramıdır. Tanımlı bir tipe, ilişkili verilere, diğer kaynaklarla ilişkilere ve üzerinde işlem yapabilen yöntemler kümesine sahip bir nesnedir. Bir kaynak genellikle JSON formatında tanımlanır ancak XML de olabilir.                                                                                                                                                                                                                                                                            |
| 6. Request              | Bir istemcinin, bir sunucudaki bir host’a bir kaynağa erişmek için yaptığı istektir. İstemci, kaynaktan ihtiyaç duyulan bilgiyi belirlemek için URL’nin bölümlerini kullanır. En yaygın istek yöntemleri**GET** , **POST** , **PUT** ,**PATCH**ve **DELETE** ’tir; ayrıca **HEAD** , **CONNECT** , **OPTIONS** ,**TRACE**ve**PATCH**de bulunur.                                                                                                                |
| 7. Request Object       | HTTP istek verisini içerir. Üç bölüm içerir: bir URL, bir header ve bir body.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 8. Route                | Bir HTTP yöntemi ile kaynağa giden path’in, path kökünden itibaren olan birleşimidir.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 9. Endpoint             | Sunucuda erişilen kaynağın bir REST API tarafından belirtilen konumudur. Genellikle API’nin HTTP yönteminde URL üzerinden tanımlanır.                                                                                                                                                                                                                                                                                                                                                                                               |
| 10. Response Object     | Bir isteğe yanıt olarak HTTP response verisini içerir. Bir header, bir body ve bir status içerir.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 11. Response            | Bir sunucu tarafından yapılan ve istemciye gönderilen yanıttır; istemciye istenen kaynağı sağlamak, istenen eylemin tamamlandığını söylemek veya bir hata oluştuğunu bildirmek için gönderilir.                                                                                                                                                                                                                                                                                                                             |
| 12. URL                 | “Uniform Resource Identifier” terimi URL ile birbirinin yerine kullanılır. Bunlar, istenen kaynağın endpoint’ini konumlandıran ve bu endpoint’in nasıl manipüle edilmesi gerektiğine dair veriyi içeren RESTful bir API’nin parçasıdır. İstemci, kaynağı manipüle etmek için URI/URL kullanarak HTTP isteği oluşturur. Dört bölümden oluşmalıdır: hostname, path, header ve query string.                                                                                                                      |
| 13. Request Header      | Sunucuya, getirilen kaynak veya istekte bulunan istemci hakkında aktarılan bilgidir. Örnekler: Endpoint ile yöntem:`POST /car-reviews`User-agent: istemcinin kullandığı tarayıcı türü. Host: bir ağ üzerinde diğer host’larla iletişim kuran bilgisayar. ContentType: metin, ses veya görsel gibi bir kaynağın medya türü. Content length: bir yanıtta gönderilen veri bayt sayısı. Accept-Encoding: beklenen dönüş veri formatı; ör.`application/json`Connection bilgisi.                                 |
| 14. Request Body        | Sunucuya iletilen veriyi sağlar.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 15. Protocol            | Verinin sunucu ile istemci arasında nasıl aktarılacağını servise söyler.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 16. Hostname            | Bir ağ üzerindeki bir cihazın adı; sıklıkla site adı olarak da adlandırılır.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 17. Path                | Path, kaynağın servis içindeki konumunu ve endpoint’ini tanımlar. Örneğin:`https://www.customerservice/customers/{customer_id}`                                                                                                                                                                                                                                                                                                                                                                                                     |
| 18. Query String        | URL’nin query’yi içeren kısmıdır.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 19. User-agent          | İstemcinin kullandığı tarayıcı türü.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 20. Host                | Bir ağ üzerinde diğer host’larla iletişim kuran bir bilgisayar.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 21. Content type        | Metin, ses veya görsel gibi bir kaynağın medya türü.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 22. Content length      | Bir yanıtta gönderilen veri bayt sayısı.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 23. Response Header     | Yanıtla ilgili metaveriyi içerir; örneğin zaman damgası, caching control, güvenlik bilgisi, content type ve response body’deki bayt sayısı.                                                                                                                                                                                                                                                                                                                                                                                         |
| 24. Response Body       | İstenen kaynaktan gelen veri istemciye geri gönderilir.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 25. Response Status     | İsteğin durumunun sonucunu ileten dönüş kodudur.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 26. JSON                | “JavaScript Object Notation”, genellikle bir sunucudaki servisten istemciye veri göndermenin bir yolu olarak veriyi saklama ve taşıma formatıdır. Anahtar-değer çiftlerinden oluşur ve kendini tanımlayıcıdır. JSON verisinin formatı, JavaScript nesneleri oluşturma koduyla aynıdır; bu, veriyi JavaScript nesnelerine dönüştürmeyi kolaylaştırır ancak herhangi bir programlama dilinde yazılabilir. JSON’un üç veri tipi vardır: scalar’lar (sayılar, string’ler, Booleans, null), diziler ve nesneler. |
| 27. Payload             | Payload, bir API isteği nedeniyle sunucudan istemciye taşınan, bir yanıtın body’sindeki veridir.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 28. GET                 | GET yöntemi, bir kaynağın temsilini (*representation* ) geri getiren bir istek olarak kullanılır.`GET()`hiçbir zaman bir kaynağı değiştirmemeli, yalnızca istenen kaynağın bir temsilini döndürmelidir.                                                                                                                                                                                                                                                                                                                   |
| 29. POST                | Sunucuya bir kaynak oluşturmak için veri gönderen HTTP yöntemidir ve `201_CREATED`status code’u döndürmelidir.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 30. PUT                 | Bir kaynağı güncelleyen veya var olan bir kaynağın yerine geçen HTTP yöntemidir. PUT’ı arka arkaya birden fazla kez çağırmak yan etki oluşturmaz; POST oluşturur. Kaynak varsa ve güncellenebiliyorsa `200_OK`döndürmeli; kaynak yoksa `404_NOT_FOUND`döndürmelidir.                                                                                                                                                                                                                                                  |
| 31. DELETE              | Bir kaynağı silen HTTP yöntemidir ve kaynak varsa ve sunucu tarafından silinebiliyorsa `204_NO_CONTENT`döndürür; ya da kaynak bulunamazsa (yani zaten silinmiştir) aynı durum geçerlidir.                                                                                                                                                                                                                                                                                                                                        |
| 32. PATCH               | Bir kaynağa kısmi değişiklikler uygulayan HTTP yöntemidir.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 33. Idempotent          | Bir kümenin bir elemanını, aynı istekler birden fazla kez yapıldığında değişmeden kalan şekilde tanımlar. PUT ve DELETE yöntemleri, aynı API yöntemi birden çok kez çağrıldığında idempotent veri ile sonuçlanır.                                                                                                                                                                                                                                                                                                    |
| 34. URL Path Parameter  | İstemci tarafından URL’nin path’i içinde bir değişken olarak operasyona aktarılır.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 35. URL Query Parameter | Genellikle JSON formatında anahtar-değer çiftleri içerir ve path’ten `'?'`ile ayrılır. Birden fazla anahtar-değer çifti varsa `'&'`ile ayrılmalıdır. Query, operasyonun döndürdüğü sonuçlara uygulanacak bir filtre geçirmek için kullanılabilir.                                                                                                                                                                                                                                                                   |
| 36. Header Parameter    | İsteğe ilişkin ek metaveri içerir; örneğin operasyona çağrı yapan istemciyi tanımlama gibi.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 37. Stateless           | Bir istemciden bir sunucuya kaynaklar için yapılan tüm istekler birbirinden bağımsız (*isolation* ) şekilde gerçekleşir. Sunucu, istemcideki uygulamanın durumundan habersizdir; bu nedenle bu bilgi her istekle birlikte aktarılmalıdır.                                                                                                                                                                                                                                                                                     |
| 38. Cacheable           | İstemcide veriyi depolayabilme ve bu verinin gelecekteki bir istekte kullanılabilmesi yeteneği.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 39. Middleware          | Uygulamalar, veritabanları veya servisler arasında yer alan ve bu farklı teknolojilerin iletişim kurmasını sağlayan yazılım.                                                                                                                                                                                                                                                                                                                                                                                                        |
