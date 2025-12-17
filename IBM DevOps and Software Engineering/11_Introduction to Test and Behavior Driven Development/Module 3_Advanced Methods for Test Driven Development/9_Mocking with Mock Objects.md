# 🎭 Mock Nesnelerle Mocking

Bu videoyu izledikten sonra şunları yapabileceksiniz: *Mock nesnelerin* ne olduğunu ve test için neden yararlı olduklarını açıklamak, Python’da **Mock** ve **MagicMock** sınıflarını nasıl uygulayacağınızı özetlemek ve *patch* ile *mock nesneleri* birlikte nasıl kullanacağınızı anlatmak.

Bazen bir fonksiyonun dönüş değerini bir *return code* veya bir *string* ile patch’lemek yeterli değildir. Peki ya patch etmek istediğiniz fonksiyonun dönüş değeri, birden fazla değeri ve metodu olan bir nesne ise? Tüm nesneyi başka bir nesneyle değiştirebilirsiniz: bir  *mock nesne* .

Bir  *mock nesne* , gerçek bir nesnenin davranışını sizin kontrol edebileceğiniz şekilde simüle eden (taklit eden) bir nesnedir. Mock nesnenin nasıl davrandığını ve ne döndürdüğünü kontrol edebilirsiniz. Üzerine birden fazla öznitelik (attribute) tanımlayabilir ve yerine geçtiği gerçek nesne gibi davranmasını sağlayabilirsiniz.

---

## 🧩 Mock ve MagicMock

Python’ın **unittest** paketinde gelen iki Mock nesnesi **Mock** ve  **MagicMock** ’tur. Aralarındaki tek fark,  **MagicMock** ’un Python’daki tüm  *magic function* ’ları uygulamasıdır. Bunlar isimleri çift alt çizgiyle çevrili fonksiyonlardır ( *double underscore* ).  *Magic function* ’lar sayesinde mock nesneleri, container’lar veya Python protokollerini uygulayan diğer nesnelerin yerine kullanabilirsiniz. Bu  *magic function* ’lara ihtiyacınız yoksa **Mock** sınıfı ihtiyaçlarınızı gayet iyi karşılar.

---

## 🧪 Mock Sınıfının Davranışı

**Mock** sınıfından herhangi bir sınıf gibi bir örnek (instance) oluşturabiliriz.

Üzerinde **foo()** gibi bir metot çağırırsak, hiç hata vermeden memnuniyetle bir *mocked method* döndürür. Bir mock nesne üzerinde çağırdığınız herhangi bir metot, hata vermeden çalışır.

Bir mock nesneyi bir fonksiyona parametre olarak verebilir ve daha sonra o fonksiyonun, mock nesnenin metodunu doğru şekilde çağırıp çağırmadığını sorgulayabilirsiniz. Bu örnekte, **foo()** metodunun çağrılıp çağrılmadığını kontrol edersek ve çağrıldıysa **True** döner. **bar()** metodunu çağırmadıysak ve çağrılıp çağırılmadığını kontrol edersek **False** döner.

---

## 🏷️ Mock Nesneye Attribute Ekleme

Mock nesneyi oluştururken attribute’lar ekleyebiliriz. Bunlar test vakamız için ihtiyaç duyduğumuz herhangi attribute olabilir.

Bu örnekte bir mock nesne oluştururuz, **status_code** attribute’unu verip  **status_code** ’u 200’e ayarlarız. Sonra  **status_code** ’u kontrol edersek, oluştururken verdiğimiz **200** değerini geri alırız.

Attribute’ları nesne oluşturulduktan sonra da gerçek nesnelerdeki gibi ayarlayabiliriz. Bu örnekte **name** attribute’unu `"Foo"` yapıyoruz. Mock nesnenin aslında `"name"` adında bir attribute’u olmamasına rağmen, bunu anında (on-the-fly) oluşturur, hata vermez ve atanan değeri kabul eder. **name** attribute’unu yazdırdığımızda, gerçek bir nesnede olduğu gibi `"Foo"` değerini beklediğimiz şekilde geri alırız.

---

## 🧷 spec ile Gerçek Sınıfı Taklit Ettirme

Bir mock’un, attribute ve metotları anlık oluşturmak yerine belirli bir sınıfı taklit etmesini de sağlayabilirsiniz.

Bu örnekte **requests** paketinden **Response** sınıfını import ediyoruz. Mock’layacağımız sınıf budur. Ardından **spec** parametresini kullanarak, bu mock’un **Response** sınıfı gibi davranmasını istediğimizi belirtip bir **Mock** oluşturuyoruz. Ayrıca  **status_code** ’u 404 yapıyor ve **content** attribute’una bir hata mesajı koyuyoruz.

Artık **m.foo()** çağırdığımızda **AttributeError** alırız çünkü **Response** sınıfında **foo()** diye bir metot yoktur. **spec** parametresini kullanmadan önce **foo()** çalışıyordu. Şimdi ise **Response** sınıfı gibi davranan bir mock sınıfımız var.

Sonra **m.json()** çağırırız. **Mock** sınıfı dinamik olarak bir **json()** metodu oluşturur ve hata vermeden döndürür çünkü **Response** sınıfında gerçekten **json()** metodu vardır. **m.status_code** çağırınca gerçek nesnede olacağı gibi **404** kodunu alırız. **m.text** çağırırsak hata almayız çünkü gerçek **Response** sınıfında **text** attribute’u vardır. Ancak **m.name** çağırırsak **AttributeError** alırız çünkü gerçek **Response** sınıfında **name** attribute’u yoktur.

Yani mock nesneler, gerçek bir nesneden (bu durumda  **Response** ) tam olarak beklediğimiz şekilde davranabilir.

---

## 🧠 Patch ile Mock Nesneyi Birleştirme

Şimdi patch ve mock nesneyi birlikte kullanarak her şeyi bir araya getirelim.

Daha karmaşık bir mock’u ele almak için daha öncekiyle aynı patch tekniğini kullanacağız. **requests** paketini import ederek başlarız. Patch edeceğimiz fonksiyon **requests.get()** fonksiyonudur. Ardından **unittest.mock** içinden **patch** ve **MagicMock** import ederiz. Testlerimizde **patch** fonksiyonunu ve **MagicMock** sınıfını kullanacağız.

Şimdi **imdb_info()** metodunu daha sağlam (robust) olacak şekilde yeniden yazarız. Hâlâ başlık (title) olarak bir string alır ve bir dictionary döndürür.

Ne yaptığını programcıların bilmesi için iyi bir docstring ekleriz. Sonra aradığımız filmin adını yazdırırız. Bu üretim (production) kodu olsaydı print yerine logging kullanırdık, ama fikri anladınız.

Ardından IMDB veritabanına çağrı yaparız. Bu, daha sonra patch edeceğimiz **requests.get()** çağrısıdır. Daha sağlam bir uygulama yaptığımızı söylemiştim. Bu kez, sonuçları almaya çalışmadan önce dönüş kodunun iyi olup olmadığını kontrol ederiz.

Bu satır, neden önceki örnekteki gibi sadece bir return value koyarak geçemeyeceğimizin nedenlerinden biridir. **requests.get()** metodundan dönen gerçek sonuçlar gibi davranan bir şey döndürmemiz gerekir.

Eğer dönüş kodu **200** ise, sonucu JavaScript Object Notation yani **JSON** olarak almak için **results.json()** fonksiyonunu çağırırız. Umarım bunun mock’lanmasının, önceki örnekteki gibi tek bir return value’dan çok daha fazlasını gerektirdiğini görüyorsunuz. Eğer dönüş kodu **200** değilse, boş bir dictionary döndürürüz.

---

## 🧪 Testin Ana Kısmı

Testin ana kısmını yazmaya hazırız. Ana programımızdaki **requests.get()** fonksiyonunu patch etmek için bir **with** ifadesi kullanırız. Patch edilmiş fonksiyonu temsil eden **"imdb_mock"** adlı bir değişken oluştururuz.

Bir sonraki satırda  **imdb_mock** ’un  **return_value** ’sunu bir **MagicMock** olacak şekilde ayarlarız. Bu, **imdb_info()** fonksiyonumuz içinde **requests.get()** çağrıldığında, bunun yerine **MagicMock** nesnesinin döndürüleceği anlamına gelir.

Sonra **spec** parametresi ile  **MagicMock** ’a **requests.Response** spesifikasyonunu uygulamasını söyleriz. **requests.get()** bir **Response** nesnesi döndürdüğünden, bu **MagicMock** geri döndürüldüğünde kodumuzun beklediği **Response** nesnesi gibi davranmasını isteriz.

Ardından  **status_code** ’u **200** yaparız çünkü yeni **imdb_info()** fonksiyonu bu return code’u bekler. Daha sonraki testlerde bunu farklı değerlere ayarlayarak hata koşullarını simüle edebiliriz.

**imdb_info()** fonksiyonunun, **requests.get()** çağrısından dönen **Response** nesnesi üzerinde **json()** fonksiyonunu çağıracağını biliyoruz. Bu yüzden  **MagicMock** ’a bir **json()** metodu oluşturmasını ve bu metodun  **return_value** ’sunu testimizde dönmesini istediğimiz JSON olacak şekilde ayarlamasını söyleriz. Tam olarak ne döneceğini tamamen kontrol ettiğimize dikkat edin.

Son adım olarak **imdb_info()** fonksiyonunu çağırır ve bir film adı geçiririz. Bunu yaptığımızda her şey beklediğimiz gibi çalışır ve mock’umuzda belirttiğimiz film bilgilerini geri alırız.

Tekrar vurgulamak gerekirse: **requests.get()** satırı çağrıldığında, patch devreye girer ve yerine mock’u koyar. Dönen sonuç, aslında gerçek bir **Response** nesnesi gibi davranacak şekilde spec verilmiş bir  **MagicMock** ’tur. Status code kontrol edildiğinde bizim belirttiğimiz gibi **200** döner. Ve payload’ı almak için **json()** metodu çağrıldığında, bizim belirttiğimiz verinin aynısını döndürür.

Umarım bu, özellikle patch edilmiş fonksiyon çağrılarının dönüş değeri olarak **Mock** ve **MagicMock** gibi mock nesneleri kullanmanın ne kadar güçlü olduğunu gösteriyordur.

---

## ✅ Özet ve Dikkat Edilmesi Gerekenler

Mock nesnelerle, test vakanızın ihtiyaç duyduğu herhangi bir davranışı taklit etmek için tam kontrol elde edersiniz. İyi return code’ları olduğu kadar kötü return code’ları da simüle etmek için ihtiyaç duyduğunuz tüm kodları kontrol edebilirsiniz. Hatta örneğimizdeki **json()** fonksiyonunda olduğu gibi, fonksiyon çağrılarının ne döndüreceğini bile kontrol edebilirsiniz.

Mock’ları, normal şartlar altında oluşturulması imkânsız olabilecek test koşullarını üretmek için kullanırız. Ancak mock’ları ölçülü kullanmalısınız çünkü kodunuzu değil, mock’larınızı test ediyor olmaktan emin olmanız gerekir.

Bu videoda şunları öğrendiniz:

* Mock nesneler, gerçek nesnelerin davranışını kontrol edebileceğiniz şekilde simüle eden nesnelerdir.
* Bir **Mock** veya **MagicMock** nesnesinin, verilen gerçek bir nesneyi taklit etmesi için, gerçek nesnenin adını **spec** parametresi olarak belirtin.
* Bir mock nesneyi de gerçek bir nesneyi patch ettiğiniz şekilde patch edersiniz.
