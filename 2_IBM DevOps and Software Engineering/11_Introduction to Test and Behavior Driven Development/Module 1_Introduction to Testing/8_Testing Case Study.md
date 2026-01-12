# 🧪 Test Vaka Çalışması

Bu videoyu izledikten sonra, test vakalarını kullanmanın amacını özetleyebilecek ve geliştiricilerin neden test edilmemiş koda asla güvenmemesi gerektiğini açıklayabileceksiniz.

Test etmenin neden bu kadar önemli olduğunu gösteren bir test vaka çalışması üzerinden sizi geçirmek istiyorum. Bu çalışma, tek bir satır kodla ne kadar çok şeyin ters gidebileceğini gösteriyor. Evet, tek bir satır kod. Ne ters gidebilir?

Bir üçgenin alanını hesaplayan bir fonksiyon yazmanız isteniyor. Geometriye aşina olmayanlarınız için, bir üçgenin alanı, tabanın yarısını alıp yükseklikle çarparak hesaplanır. Başka bir deyişle formül:  **taban / 2 × yükseklik** .

Bu fonksiyonu Python’da yazmanız isteniyor. Önce bir fonksiyon tanımlayarak başlıyorsunuz. Adını `area_of_a_triangle` koyuyorsunuz. İyi Python konvansiyonlarına uyarak kelimeleri ayırmak için alt çizgi kullanıyorsunuz çünkü Python *snake case* kullanır.

Ayrıca hesaplamada kullanılmak üzere fonksiyona aktarılacak iki parametre tanımlıyorsunuz: `base` ve `height`. Bu fonksiyon tek satırla uygulanabildiği için, **taban / 2 × yükseklik** formülündeki sonucu döndürüyorsunuz.

Bu noktada kendinizle oldukça gurur duyuyorsunuz. Yani ne ters gidebilir ki? Tek satır kod. Bitti. Prod’a gönder. Sonraki göreve geç.

Sonra hatırlıyorsunuz ki kodunuzu test etmelisiniz; bunun için bazı test vakaları yazmalısınız.

## 🧾 Test Vakası Nedir

Bir test vakası, bilinen bir girdi (ör. örnek veri) verildiğinde kodunuzu çağırıp beklenen bir çıktıyı doğrulamak için kullanabileceğiniz bir kod parçasıdır. Kodun doğru çalıştığından emin olmak için test vakaları kullanırsınız.

Bu yüzden, herhangi bir test çatısı (framework) kullanmadan Python’da bazı testler yazmaya başlıyorsunuz. Fonksiyonunuza, programcılara nasıl çağıracaklarını söyleyen bir *doc string* veya Python ipuçları eklemediğiniz için, fonksiyonunuza istedikleri veri tipini geçebilirler. Bu yüzden, fonksiyonun çağırıcısının geçebileceği bu veri tiplerinden hiçbirinin davranışı bozmadığından emin olmak için test etmeniz gerekir.

Test üçgenlerinizin sırasıyla taban ve yüksekliğini temsil edecek tuple’lardan oluşan bir liste oluşturarak başlıyorsunuz. İki adet kayan noktalı sayı ile başlıyorsunuz. Listeye iki tamsayı, `2` ve `5` ekliyorsunuz. Sonra `0` ve `5`. Negatif bir sayı, bir *Boolean* ve son olarak bir *string* ekliyorsunuz.

Bunların hepsini test ediyorsunuz çünkü neyin geçirileceğini bilmiyorsunuz. Bir web uygulaması bir URL’den veya bir API çağrısından veri alabilir ve sonra bu veriyi fonksiyonunuza olduğu gibi aktarabilir. Uygulama, fonksiyonunuzun veriyle ne yapacağını bildiği varsayımıyla çalışır.

Sonra liste üzerinde dönmek için bir `for` döngüsü oluşturuyorsunuz. Şunu yazıyorsunuz: `for data in test_data`. Döngünün her çalışmasında, değişkenleri yerleştirmek için bir mesaj yazdırıyorsunuz. Bu değişkenler `data` ve `data`’yı fonksiyonunuza geçirince dönen `area_of_a_triangle` sonucudur. Python, fonksiyonun döndürdüğü her şeyi mesajın içine yerleştirir.

Diyelim ki kodu `triangle.py` adlı bir dosyaya koydunuz. Şimdi bu kodu çalıştırmanız gerekiyor. Şunu yazıyorsunuz:

```bash
python triangle.py
```

## 🐞 İlk Uygulama Sonuçları ve Hatalar

Döngünün ilk çalışmasında şöyle yazdırıyor: tabanı `3.5`, yüksekliği `8.5` olan bir üçgenin alanı `14.875`.

Şimdilik her şey iyi.

Döngü sonraki çalışmada şunu söylüyor: `2,5` için bir üçgenin alanı `5.0`. Hâlâ oldukça iyi.

Sonraki çalışmada: `0,5` için bir üçgenin alanı `0.0`. Kod hâlâ çalışıyor. Tabanı sıfır olan bir üçgen alan vermez.

Sonra ilk hatayı alıyorsunuz: `-2,5` için bir üçgenin alanı `-5.0`. Bu, negatif sayılar için açıkça bir bug.

Sonra `true,5` için bir üçgenin alanı `2.5` döndürüyor. Belki bu durumda *true* değeri `1`’e dönüştürülüyordur; düşünürseniz, sıklıkla `1` ve `0` değerlerini *true* ve *false* anlamında kullanırsınız. Yani Python’un yapabildiği en iyi dönüşüm, *true* değerini bir tamsayı gibi `1`’e dönüştürmek olmuş olabilir. Yine de bu bir bug.

Buradaki daha korkutucu problem şu: Bu noktaya kadar hiçbir hata fırlatılmadı. Bu fonksiyon sessizce yanlış cevaplar veriyor. Bu problem prod ortamında bulması zor olacak çünkü fonksiyon çalışıyor gibi görünüyor ama yanlış cevap döndürüyor.

Sonra bir *string* geçiriyorsunuz ve her şey çöküyor. Sonunda Python tarafından kabul edilen ilk hatayı alıyorsunuz. Şu *type error* mesajını görüyorsunuz: bölme işlemi için desteklenmeyen operand tipleri; bir tamsayı bekliyordu ama siz bir *string* geçtiniz.

Bu yüzden, o fonksiyonun prod’a koymak için henüz hazır olmadığı açık.

Görünüşte basit bir hesap yapan tek bir satır kod, fonksiyonun gerçekten doğru girdiyi almasını sağlamak için daha fazla savunmacı programlama ile çevrelenmelidir.

## 🛡️ Daha Sağlam Bir Uygulama

Daha sağlam bir uygulamaya bakalım. Fonksiyonu en baştan sağlam bir şekilde yazarsanız şöyle görünür.

Fonksiyon bazı tip ipuçları ( *type hinting* ) içerir. Bu, çağıranların kötü veri geçmesini engellemez ama en azından sizden hangi veri tipini beklediğinizi bilmelerini sağlar. Bu durumda *floating-point numbers* bekliyorsunuz.

Fonksiyon ayrıca geliştiricilere, negatif olmayan bir sayı beklediğinizi daha da açık etmek için bir *doc string* de içerir.

Koda yapılan bir sonraki ekleme, doğru tipi aldığınızı kontrol etmektir. `float` ipucu iyi ama Python’da herhangi bir tip geçebilirsiniz; bu yüzden bunu açıkça kontrol etmelisiniz.

Eğer `base` tipiniz veya `height` tipiniz `int` veya `float` listesinin içinde değilse, `"base or height must be a number"` mesajıyla bir *type error exception* fırlatırsınız.

Böylece, beklediğiniz sayı tipinde olmayan her şeyi daha en baştan ayıklarsınız. Bu,  *boolean* ,  *string* ,  *dictionary* , *list* ve dahil olmak üzere fonksiyonunuzun baş edemeyeceği *complex numbers* gibi atılabilecek diğer tüm Python tiplerini ortadan kaldırır.

Veri bu kontrolden geçince, elinizde ya bir `int` ya da bir *floating-point number* olduğunu bilirsiniz.

Sonra, pozitif bir sayı aldığınızdan emin olmak için kontrol edersiniz; eğer `base` veya `height` sıfırdan küçükse bir *value error exception* fırlatırsınız.

İlk istisna ( *exception* ) bir *type error* idi çünkü tip yanlıştı. Bu ikinci istisnada tip doğrudur; sadece beklediğiniz değer aralığında değildir, bu yüzden *value error exception* kullanırsınız.

Şunu da belirtmeliyim: çok geniş bir istisna fırlatmaktan kaçınmak istersiniz; mümkün olduğunca açık olmalısınız.

*Value error* mesajı, hataya hangisinin sebep olduğuna bağlı olarak `"base must be a positive number"` veya `"height must be a positive number"` mesajını döndürür. Çağırana, hataya hangi parametrenin sebep olduğunu söylemek önemlidir. Bu, çağıranın pozitif bir sayı göndermesi gerektiğine dair iyi bilgi verir.

Son olarak, hesaplamayı yapan orijinal tek satır kodu alırsınız: tabanın yarısı çarpı yükseklik ve sonucu döndürür.

Bu, bir satır kodu hobi olarak yazmakla, prod’a koymak istediğiniz kodu geliştirmek için iyi yazılım mühendisliği uygulamalarını kullanmak arasındaki farktır.

Prod’da fonksiyonunuz çağrılacaktır ve kimin çağıracağını ya da neyin geçirileceğini bilmezsiniz; bu yüzden savunmacı kod yazmalısınız. Kodunuzu bozmanın kaç yolu varsa, olası sonuçların mümkün olduğunca çoğu için test vakaları yazmalısınız.

Dediğim gibi, test edilmemiş koda güvenilmemelidir. Bana bir test vakasıyla çalıştığını kanıtlayamıyorsanız, benim için çalışmıyordur. Çalışıyor gibi görünebilir ama ona garip veriler atarsanız, kesinlikle çökecektir. Bunu kodunuzda istemezsiniz.

Test vakaları bizi, kodumuzun hangi şekillerde bozulabileceğini düşünmeye zorlar; sonra kodun bozulması için test vakaları yazarız ve ardından kodun tekrar “zarifçe” başarısız olması için gereken kodu yazar ve test vakasının geçmesini sağlarız.

## ✅ Video Özeti

Bu videoda, geliştiricilerin kodlarının doğru çalıştığından emin olmak için test vakaları kullandığını öğrendiniz. Test vakaları, geliştiricilerin kodlarının bozulabilecek kısımlarını tespit etmelerine ve düzeltmelerine yardımcı olur.
