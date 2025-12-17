# 🧩 Patch ile Mocking

Bu videoyu izledikten sonra şunları yapabileceksiniz:

* *Patching* ’i tanımlamak
* Python’un *mock* kütüphanesinde bulunan iki *patching* tekniğini listelemek
* Her bir *patching* tekniğinin hangi durumlarda faydalı olduğunu açıklamak

İnceleyeceğimiz ilk *mocking* türüne *“patching”* denir. *Patching* ile bir fonksiyon çağrısının davranışını değiştirebilirsiniz.  *Patching* , fonksiyonun kontrolünüz altında olmayan harici bir sistemi çağırdığı durumlarda özellikle faydalıdır. Bu, test sırasında bu hataları gerçekten oluşturamayacağınız hâlde hata koşullarını simüle etmek istediğinizde de kullanışlıdır.

Python’daki *mock* kütüphanesi size iki şekilde *patching* yapma imkânı verir:

* Bir fonksiyonun  *return value* ’sunu  *patch* ’lemek
* Bir fonksiyonu başka bir fonksiyonla değiştirmek (buna *side effect* denir)

Şimdi bunların her birini sırasıyla ele alalım.

---

## 🎯 Return Value Patch

Bir fonksiyonun  *return value* ’sunu  *patch* ’leyebilirsiniz. Bu, hata yakalayıcıları ( *error handlers* ) test etmek için faydalıdır; çünkü hata koşul kodlarını geri döndürebilir ve uygulamanızın bu dönüş kodlarını aldığında nasıl davrandığını görebilirsiniz. Bu yöntem, bir fonksiyon çağrısından dönen veriyi kontrol etmek için de faydalıdır. Programınızın beklediği herhangi bir veri yapısını veya nesneyi geri döndürebilirsiniz.

*return_value*  *patch* ’ini kullanarak, bir fonksiyon çağrısından dönüş değeri olarak geri gönderilebilecek her şeyi döndürebilirsiniz. Şimdi bir fonksiyonun  *return value* ’sunun nasıl  *patch* ’leneceğine bakalım.

IMDB veritabanı örneğine geri dönelim ve aynı çağrıdan çeşitli davranışlar elde etmek için *"with"* ifadesini nasıl kullanabileceğimizi görelim. IMDB veritabanını çağıran bir fonksiyon oluşturmak istiyoruz ve adını *"imdb_info"* koyuyoruz. Bir filmin başlığını parametre olarak alıyoruz. Bu fonksiyondaki ilk adım, aradığımız başlığı bize gösteren bir mesaj yazdırmaktır. Bunu neden eklediğimizi birazdan göreceksiniz. Sonra IMBD API’sini çağırarak hangi film başlığını arayacağını söylüyoruz. Son olarak sonuçları *JavaScript Object Notation* yani *JSON* olarak döndürüyoruz.

Şimdi bu yeni fonksiyon çağrısının hata koşullarını nasıl ele aldığını test edelim. Bunu yapmak için bir *patch* ve iki farklı dönüş değeri kullanacağız. Önce *"with"* kullanırız ve *imdb_info* fonksiyonunu *status code 200* döndürecek şekilde  *patch* ’leriz.  *200* , *OK* anlamına gelir; yani çağrı başarılıdır. Bu testi çalıştırdığımızda, *imdb_info* fonksiyonu asla çalışmaz. Bunun yerine *status_code 200* dönüş değeri doğrudan çağırana geri döndürülür.

Sonra *imdb_info()* çağrısını yaparız, başlık olarak *"Bambi"* göndeririz ve dönüş değerini yazdırırız. Gerçekten de *status code 200* döndürür.

Ancak döndürmediği şey, *imdb_info* fonksiyonunun ilk satırında yazdırdığımız mesajdır. Bu, fonksiyonun hiç çağrılmadığını kanıtlar.  *return value* ’yu  *patch* ’leyerek fonksiyonu tamamen atladık.

Sonra *imdb_info()* çağrısını tekrar  *patch* ’leriz, ama bu sefer *"with"* ifadesinin sonunda tanımladığımız *imdb* değişkenini kullanırız. Bu sadece  *patching* ’in alternatif bir yoludur. *imdb* değişkeninin dönüş değerini *"status_code 404"* yaparız. *404* *“not found”* demektir.

Belki web tarayıcınız bir web sayfasını bulamadığında size bir iki kez bu kodu döndürmüştür. Bu durumda, filmin bulunamadığı anlamına gelir. Şimdi *imdb_info* fonksiyonunu çağırıp başlık olarak *"Bambi"* gönderdiğimizde, *status code 404* geri alırız.

Gerçek hayatta bu hata koşulunu oluşturmak için gerçekten bulunmayan bir başlık göndermeniz gerekirdi. Ancak *patching* ile, gerçek ve mevcut bilgilerin bulunmasını engelleyerek bu hata koşullarını test edebiliriz.

Bu örnek, *patching* ile bir fonksiyonun bize ne döndüreceği üzerinde tam kontrol sağlayabileceğimizi gösterir. Böylece gerçek servisi çağırmadan veya onu kötü bir dönüş kodu döndürmeye zorlamaya çalışmadan, iyi dönüş kodlarını ve kötü dönüş kodlarını test edebiliriz.  *Patching* ’i biraz daha derinlemesine inceleyelim.

![1765965793655](image/8_MockingwithPatch/1765965793655.png)

---

## 🎯 Hassas Patch Uygulama

 *Patching* ’i hassas şekilde yapabilirsiniz. Sadece sizin yazdığınız bir fonksiyonu  *patch* ’lemekle sınırlı değilsiniz. Aslında bir üçüncü taraf ( *third-party* ) kütüphaneyi istediğiniz şeyi döndürecek şekilde  *patch* ’leyebilirsiniz.

Önceki örneğin küçük bir varyasyonuna bakalım. Öncekiyle aynı *imdb_info* fonksiyonuyla başlarız. Bu sefer, *requests* paketindeki *get()* fonksiyonunu *mock.patch* ile  *patch* ’leriz. Bu Python kütüphanesini ilk satırda import etmiştik.

Normalde onun üzerinde kontrolümüz olmazdı. Ancak *patch* ile, *requests.get()* her çağrıldığında, fonksiyon hiç çağrılmadan bizim belirttiğimiz değer döndürülür. Bu da test sırasında IMDB veritabanı servisini gerçekten çağırmayacağı anlamına gelir.

Şimdi *imdb_info()* fonksiyonu normal şekilde çalışır. Tüm satırlar yürütülür. Sadece uzak çağrı  *patch* ’lenmiştir. Son olarak *imdb* fonksiyonunu çağırdığımızda, fonksiyonun ilk satırındaki mesajı yazdırır.

Sonra fonksiyon  *requests.get()* ’i çağırır ama bu çağrı gerçekte hiçbir zaman tamamlanmaz. Yalnızca dönüş değeri geri verilir. *imdb_info* fonksiyonu devam eder ve IMDB veritabanıyla hiç iletişime geçmediğini bilmeden *status code 200* döndürür.

Bu örnek,  *patching* ’i ne kadar hassas yapabileceğinizi gösterir. Sadece fonksiyonumuz içindeki uzak çağrıyı  *patch* ’ledik. Eğer dönüş kodlarını kontrol eden veya dönüş değerlerini daha fazla işleyen başka kodlar olsaydı, onlar da çalıştırılacaktı.

Bazen bir  *patch* ’in yalnızca değer döndürmesinden daha fazlasını yapması gerekir.

![1765965823747](image/8_MockingwithPatch/1765965823747.png)

---

## 🔁 Side Effect Tekniği

*Patching* ile bir fonksiyonu başka bir fonksiyonla da değiştirebilirsiniz. Buna *“side effect”* denir. *Side effect* tekniğiyle, test sırasında gerçek fonksiyon yerine çağrılacak kendi fonksiyonunuzu sağlayabilirsiniz. Şimdi  *side effect* ’in nasıl kullanılacağına bakalım.

Önce *unittest.mock* kütüphanesinden *patch* import ederiz. (Bu, *unittest* kütüphanesini sevmemin bir başka nedeni; pek çok faydalı araç gömülü gelir.)  *patch* ’i import ettikten sonra iki fonksiyon tanımlarım: biri *bye()* ve *“bye”* string’ini döndürür, diğeri *hello()* ve *“hello”* string’ini döndürür.

Sonra *test()* adında bir fonksiyon tanımlarız. Bu fonksiyon, az önce yazdığımız *hello()* fonksiyonunun çağrısından dönen sonucu döndürür. Normal koşullarda bu fonksiyonun dönüş değerinin *"hello"* string’i olmasını bekleriz. Ama bunlar normal koşullar değildir.

Bu *test* fonksiyonunu bir *mock* ile, özelde bir *mock.patch* ile dekore ederim. Python’da  *decorator* ’lar, bir fonksiyonun etrafına kod sarmalamanın bir yoludur. Bir  *decorator* ’ı her zaman tanıyabilirsiniz çünkü başında *"@"* sembolü vardır; bu, ilgili şeyin bir *decorator* olduğunu gösterir.

Bir *decorator* ile, biri *test()* fonksiyonunu her çağırdığında önce *patch()* çağrılır ve sonra  *patch()* , *test* fonksiyonunu çağırır. Ayrıca  *patch()* ’e bazı parametreler verdiğimize dikkat edin. İlk parametre,  *patch* ’lemek istediğimiz fonksiyonu temsil eden bir string’dir. Bu durumda ana Python programımızdaki *hello* fonksiyonunu  *patch* ’liyoruz. İkinci parametre ya bir *side effect* ya da bir *return value* olabilir. Bu örnekte *side effect* kullanıyoruz. *Side effect* alternatif bir yol izler.

*Side effect* değerinin *bye* fonksiyonuna bir işaretçi ( *pointer* ) olduğuna dikkat edin. Eğer henüz tahmin etmediyseniz: bu *patch* etkinken, *hello* fonksiyonuna yapılan her çağrı bunun yerine *bye* fonksiyonunu çağıracaktır.

Bunun ne kadar güçlü olduğunu düşünün. Test sırasında ihtiyaç duyduğumuz her koşulu oluşturmak için, tam olarak istediğimiz şeyi yapan bir fonksiyon yazabiliriz. Bu sayede test çalıştığında ne döneceğini tam olarak kontrol ederiz.

Son olarak bir ana program yazarız ve çalıştırdığımızda *hello()* fonksiyonunu çağırır ve *"hello"* yazdırır. *bye()* fonksiyonunu çağırır ve *"bye"* yazdırır.

Ancak *test()* fonksiyonunu çağırdığında *"bye"* yazdırır, çünkü *hello* fonksiyonunu bunun yerine *bye* fonksiyonunu çağıracak şekilde  *patch* ’ledik.

![1765965851658](image/8_MockingwithPatch/1765965851658.png)

---

## 📌 Özet

Bu videoda şunları öğrendiniz:

* *Patching* , geliştiricilerin bir fonksiyon çağrısının davranışını değiştirdiği bir *mocking* tekniğidir.
* Python’un *mock* kütüphanesi iki *patching* tekniği sağlar:
  * Bir fonksiyonun  *return value* ’sunu  *patch* ’lemek
  * Bir fonksiyonu başka bir fonksiyonla değiştirmek (*side effect* tekniği)
