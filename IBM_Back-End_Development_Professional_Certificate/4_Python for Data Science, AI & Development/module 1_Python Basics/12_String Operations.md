# 🔡 String (Dize) İşlemleri

## 📜 String Nedir?

Python'da bir string, bir karakter dizisidir.

Bir string iki tırnak içinde yer alır. Tek tırnak da kullanabilirsiniz.

Bir string, boşluklardan veya rakamlardan oluşabilir.

Bir string ayrıca özel karakterler de olabilir.

Bir string'i başka bir değişkene bağlayabilir veya atayabiliriz.

Bir string'i, sıralı bir dizi olarak düşünmek faydalıdır.

## 🔢 İndeksleme ve Negatif İndeksleme

Dizideki her bir elemana, sayı dizisiyle temsil edilen bir indeks kullanarak erişilebilir.

İlk indekse aşağıdaki şekilde erişilebilir.

Altıncı indekse erişebiliriz.

Ayrıca 13. indekse de erişebiliriz.

Stringlerde negatif indekslemeyi de kullanabiliriz.

Son eleman, eksi bir indeksiyle verilir.

İlk eleman, eksi 15 indeksiyle elde edilebilir ve bu şekilde devam eder.

Bir string'i başka bir değişkene bağlayabiliriz.

String'i bir liste veya tuple olarak düşünmek faydalıdır.

String'i bir dizi gibi ele alabilir ve dizi işlemleri gerçekleştirebiliriz.

## ✂️ Dilimleme ve Adım (Stride)

Aşağıdaki gibi bir *stride* (adım) değeri de girebiliriz.

İki değeri, her ikinci değişkeni seçeceğimiz anlamına gelir.

Dilimlemeyi de dahil edebiliriz.

Bu durumda, dördüncü indekse kadar her ikinci değeri döndürürüz.

`len` komutunu kullanarak string'in uzunluğunu elde edebiliriz.

15 eleman olduğu için sonuç 15'tir.

## 🔗 String Birleştirme ve Tekrarlama

Stringleri birleştirebilir veya bir araya getirebiliriz.

Toplama sembollerini kullanırız.

Sonuç, her ikisinin kombinasyonu olan yeni bir string'tir.

Bir string'in değerlerini tekrarlayabiliriz.

String'i, kaç kez tekrarlamak istiyorsak o sayı ile çarpmamız yeterlidir – bu durumda üç.

Sonuç, yeni bir string'tir.

Yeni string, orijinal string'in üç kopyasından oluşur.

Bu, string'in değerini değiştiremeyeceğiniz, ancak yeni bir string oluşturabileceğiniz anlamına gelir.

Örneğin, yeni bir string oluşturmak için onu orijinal değişkene ayarlayıp yeni bir string ile birleştirebilirsiniz.

Sonuç, Michael Jackson'dan, *Michael Jackson is the best* ifadesine dönüşen yeni bir string'dir.

String'ler  *immutable* 'dır (değiştirilemez).

## 🧵 Kaçış Dizileri ve Ters Bölü Çizgisi

Ters bölü çizgileri, kaçış dizilerinin başlangıcını temsil eder.

Kaçış dizileri, girmesi zor olabilecek stringleri temsil eder.

Örneğin, `\n` yeni satırı temsil eder.

Çıktı, `\n` kaçış dizisiyle karşılaşıldıktan sonra yeni bir satırla verilir.

Benzer şekilde, `\t` bir sekmeyi (tab) temsil eder.

Çıktı, `\t` ters bölü çizgisinin olduğu yerde bir sekme ile verilir.

String'inize bir ters bölü çizgisi yerleştirmek istiyorsanız, çift ters bölü çizgisi kullanın (`\\`).

Sonuç, kaçış dizisinden sonra bir ters bölü çizgisidir.

Stringin önüne bir `"r"` de koyabiliriz.

## 🛠️ String Metotları

Şimdi string metotlarına bir göz atalım.

Stringler dizilerdir ve bu nedenle listeler ve tuple'lar üzerinde çalışan uygulama metotlarına sahiptirler.

Stringlerin ayrıca yalnızca stringler üzerinde çalışan ikinci bir metot kümesi vardır.

Bir metoda string `A` üzerinde uygulama yaptığımızda, `A`dan farklı olan yeni bir string `B` elde ederiz.

Şimdi birkaç örnek yapalım.

Metot olarak `"Upper"` ile deneyelim.

Bu metot, küçük harf karakterlerini büyük harf karakterlerine dönüştürür.

Bu örnekte, `A` değişkenini aşağıdaki değere ayarlarız.

`"Upper"` metodunu uygular ve sonucu `B`ye eşit olacak şekilde ayarlarız.

`B`nin değeri, `A`ya benzerdir, ancak tüm karakterler büyük harftir.

Metot, stringin bir bölümünü, yani bir alt stringi, yeni bir string ile değiştirir.

Değiştirmek istediğimiz string bölümünü gireriz.

İkinci argüman, bu bölümü ne ile değiştirmek istediğimizdir.

Sonuç, bir kısmı değiştirilmiş yeni bir string'tir.

`find` metodu, alt stringleri bulur.

Argüman, bulmak istediğiniz alt stringdir.

Çıktı, dizinin ilk indeksidir.

`Jack` alt stringini bulabiliriz.

Eğer alt string, string içinde yoksa çıktı eksi birdir.

Daha fazla örnek için laboratuvarlara göz atın.
