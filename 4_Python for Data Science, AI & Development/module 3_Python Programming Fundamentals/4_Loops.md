# 🔁 Döngüler

## 🎯 Döngülere Giriş

Bu videoda, özellikle `for` döngüleri ve `while` döngüleri olmak üzere döngüleri ele alacağız.

Bu videoda pek çok görsel örnek kullanacağız. Veriye dayalı örnekler için laboratuvar ( *lab* ) çalışmalarına bakın.

Döngülerden bahsetmeden önce, `range` fonksiyonunu gözden geçirelim.

`range` fonksiyonu, sıralı bir diziyi (`i` adlı bir liste) çıktı olarak verir. Eğer girdi pozitif bir tam sayıysa, çıktı bir dizidir. Bu dizi, girdi ile aynı sayıda eleman içerir ama 0’dan başlar.

## 📏 `range` Fonksiyonu

Örneğin, girdi 3 ise, çıktı şu dizi olur: 0, 1, 2.

Eğer `range` fonksiyonunun iki girdisi varsa ve ilk girdi ikinci girdiden küçükse, çıktı ilk girdiden başlayan bir dizidir.

Dizi, ikinci sayıya kadar (ikinci sayı *hariç* olmak üzere) ilerler. Girdiler 10 ve 15 olduğunda aşağıdaki diziyi elde ederiz.

`range` fonksiyonunun daha fazla özelliği için lab’lere bakın.

Lütfen unutmayın: Eğer Python 3 kullanıyorsanız, `range` fonksiyonu Python 2’deki gibi açıkça bir liste üretmez.

Bu bölümde `for` döngülerini ele alacağız.

---

## 🔂 `for` Döngüleri ve Listelere Odaklanma

Listelere odaklanacağız, ancak işlemlerin çoğu demetler ( *tuple* ) üzerinde de kullanılabilir.

Döngüler, bir görevi tekrar tekrar gerçekleştirir. Renkli karelerden oluşan bir grup düşünün.

Diyelim ki, her renkli kareyi beyaz bir kareyle değiştirmek istiyoruz.

Her bir kareye bir numara verelim ki işler biraz daha kolay olsun ve karelerin tüm grubuna `squares` (kareler) diyelim.

Eğer birine 0 numaralı kareyi beyaz bir kare ile değiştirmesini söylemek isteseydik, şöyle derdik:

“0 numaralı kareyi beyaz kare ile değiştir.”

Ya da şöyle diyebiliriz:

“`squares` içinde kare 0 için, kare 0 beyaz kareye eşittir.”

Benzer şekilde, bir sonraki kare için şöyle diyebiliriz:

“`squares` içinde kare 1 için, kare 1 beyaz kareye eşittir.”

Bir sonraki kare için şöyle diyebiliriz:

“`squares` içinde kare 2 için, kare 2 beyaz kareye eşittir.”

Her kare için bu işlemi tekrarlarız. Değişen tek şey, bahsettiğimiz karenin indeksidir.

---

## 📋 Kareleri Listeyle Temsil Etmek

Python’da benzer bir görevi gerçekleştirecek olursak, gerçek kareleri kullanamayız. Bu yüzden kutuları temsil etmek için bir liste kullanalım.

Listedeki her bir eleman, rengi temsil eden bir dizgedir ( *string* ).

Listedeki her elemandaki renk adını “white” (beyaz) olarak değiştirmek istiyoruz.

Listedeki her elemanın aşağıdaki gibi bir indeksi vardır.

Bu, Python’da bir döngü gerçekleştirmek için kullanılan sözdizimidir. Girintiye ( *indent* ) dikkat edin.

`range` fonksiyonu bir liste üretir. Kod, girinti içindeki her şeyi 5 kez tekrar edecektir.

Eğer değeri 6’ya değiştirirseniz, bu işlemi 6 kez yapar.

Buna karşılık, `i` değişkeninin değeri her seferinde 1 artırılır.

Bu kısımda, listenin `i`’inci elemanını `"white"` dizgesine değiştiririz.

`i`’nin değeri 0 olarak ayarlanır. Döngünün her yinelemesi, girintinin başından başlar.

Sonra girintideki her şeyi çalıştırırız. Listedeki ilk eleman `"white"` olarak ayarlanır.

Sonra tekrar girintinin başına gideriz.

Her satırda aşağıya doğru ilerleriz. Listenin değerini değiştiren satıra ulaştığımızda, 1 numaralı indeksin değerini `"white"` yaparız.

`i`’nin değeri 1 artar. Aynı işlemi 2 numaralı indeks için tekrarlarız.

Bu süreç, son elemana ulaşana kadar sıra gelen her bir indeks için devam eder.

---

## 🧱 Listeler ve Demetler Üzerinde Doğrudan Döngü

Ayrıca Python’da bir liste veya demet üzerinde doğrudan yineleme yapabiliriz; indisleri kullanmamıza bile gerek yoktur.

İşte `squares` adlı liste.

Listenin her yinelemesinde, `squares` listesindeki bir elemanı `square` adlı değişkene geçiririz.

Bu bölümde `square` değişkeninin değerini gösterelim.

İlk yinelemede, `square` değişkeninin değeri `"red"`’dir.

Sonra ikinci yinelemeye başlarız. İkinci yinelemede, `square`’ın değeri `"yellow"` olur.

Ardından üçüncü yinelemeye başlarız.

Son yinelemede, `square` değişkeninin değeri `"green"` olur.

---

## 🧮 `enumerate` ile İndis ve Eleman

Veri üzerinde yineleme yapmak için yararlı bir fonksiyon da `enumerate`’dir.

Bu fonksiyon, listedeki indisi ve elemanı elde etmek için kullanılabilir.

Her karenin indeksini temsil eden numaralarla kutu benzetmesini kullanalım.

Bu, bir liste üzerinde yineleme yapmak ve her elemanın indeksini sağlamak için kullanılan sözdizimidir.

`squares` listesini kullanır ve renkli kareleri temsil etmek için renk adlarını kullanırız.

`enumerate` fonksiyonunun argümanı listedir; bu durumda `squares` listesidir.

`i` değişkeni indeks, `square` değişkeni ise listedeki ilgili elemandır.

Ekranın sol tarafını, döngünün farklı yinelemeleri için `square` ve `i` değişkenlerinin farklı değerlerini göstermek için kullanalım.

İlk yinelemede, değişkenin değeri `"red"`’dir; bu, 0’ıncı indekse karşılık gelir ve `i`’nin değeri 0’dır.

İkinci yinelemede, `square` değişkeninin değeri `"yellow"`’dur ve `i`’nin değeri, yani 1, onun indeksine karşılık gelir.

Son indeks için de aynı işlemi tekrar ederiz.

---

## ♻️ `while` Döngüleri

`while` döngüleri, `for` döngülerine benzer; ancak bir ifadeyi belirli sayıda kez çalıştırmak yerine, `while` döngüsü yalnızca bir koşul sağlandığı sürece çalışır.

Diyelim ki, `squares` listesindeki tüm turuncu kareleri `new_squares` listesine kopyalamak istiyoruz, ancak turuncu olmayan bir kareyle karşılaşırsak durmak istiyoruz.

`squares` değerlerini önceden bilmiyoruz.

Basitçe, kare turuncu olduğu sürece işleme devam ederiz ya da karenin `"orange"` olup olmadığını kontrol ederiz.

Eğer değilse, dururuz.

İlk örnek için, karenin turuncu olup olmadığını kontrol ederiz. Koşul sağlanır, bu yüzden kareyi kopyalarız.

İkinci kare için de aynı işlemi tekrarlarız. Koşul sağlanır, bu yüzden kareyi kopyalarız.

Sonraki yinelemede, mor bir kareyle karşılaşırız. Koşul sağlanmaz, bu yüzden süreci durdururuz.

Bu, özünde bir `while` döngüsünün yaptığı şeydir.

Kodun temsil edilmesi için soldaki şekli kullanalım.

Farklı kareleri temsil etmek için renk adlarından oluşan bir liste kullanacağız.

Boş bir `new_squares` listesi oluştururuz.

Gerçekte, bu listenin boyutu belirsizdir.

İndisi 0’dan başlatırız.

`while` deyimi, parantezin içindeki koşul yanlış olana kadar girinti içindeki ifadeleri tekrar tekrar çalıştıracaktır.

`squares` listesinin ilk elemanının değerini `new_squares` listesine ekleriz.

`i`’nin değerini 1 artırırız.

`squares` listesinin ikinci elemanının değerini `new_squares` listesine ekleriz.

`i`’nin değerini tekrar artırırız.

Artık `squares` dizisindeki değer `"purple"`’dır.

Bu nedenle, `while` deyimi için koşul yanlıştır ve döngüden çıkarız.

Döngülerle ilgili, çoğu gerçek veri içeren daha fazla örnek için lab’lere göz atın.

---

## 🔁 Aynı İçeriğin Zaman Kodlu Sürümü

Bu videoda, özellikle `for` döngüleri ve `while` döngüleri olmak üzere döngüleri ele alacağız.

Bu videoda pek çok görsel örnek kullanacağız.

Veriye dayalı örnekler için lab çalışmalarına bakın.

Döngülerden bahsetmeden önce, `range` fonksiyonunu gözden geçirelim.

`range` fonksiyonu, `i` adlı bir liste olarak sıralı bir dizi üretir.

Eğer girdi pozitif bir tam sayıysa, çıktı bir dizidir.

Dizi, girdi ile aynı sayıda eleman içerir ama 0’dan başlar.

Videoyu ::28 zamanından başlatarak oynatın ve transkripti 0:28’den itibaren takip edin.

Örneğin, girdi 3 ise, çıktı 0, 1, 2 dizisidir.

Eğer `range` fonksiyonunun iki girdisi varsa veya ilk girdi ikinci girdiden küçükse, çıktı, ilk girdiden başlayan bir dizidir.

Daha sonra dizi, ikinci sayıya kadar (ikinci sayı  *hariç* ) yineleme yapar.

Girdiler 10 ve 15 olduğunda, aşağıdaki diziyi elde ederiz.

`range` fonksiyonunun daha fazla yeteneği için lab’lere bakın.

Lütfen unutmayın: Eğer Python 3 kullanıyorsanız, `range` fonksiyonu Python 2’deki gibi açıkça bir liste üretmeyecektir.

Bu bölümde `for` döngülerini ele alacağız.

Videoyu 1:05 zamanından başlatarak oynatın ve transkripti 1:05’ten itibaren takip edin.

Listelere odaklanacağız, ancak prosedürlerin çoğu demetlerde de kullanılabilir.

Döngüler bir görevi tekrar tekrar gerçekleştirir.

Renkli karelerden oluşan bir grup düşünün.

Diyelim ki, her renkli kareyi beyaz bir kareyle değiştirmek istiyoruz.

Her kareye bir numara verelim ki işler biraz daha kolay olsun ve karelerin tüm grubuna `squares` diyelim.

Eğer birine 0 numaralı kareyi beyaz kare ile değiştirmesini söylemek isteseydik, şöyle derdik:

“0 numaralı kareyi beyaz kare ile değiştir.”

Ya da şöyle de diyebiliriz:

“`squares` içinde kare 0 için, kare 0 beyaz kareye eşittir.”

Videoyu 1:42 zamanından başlatarak oynatın ve transkripti 1:42’den itibaren takip edin.

Benzer şekilde, bir sonraki kare için şöyle diyebiliriz:

“`squares` içinde kare 1 için, kare 1 beyaz kareye eşittir.”

Bir sonraki kare için şöyle diyebiliriz:

“`squares` içinde kare 2 için, kare 2 beyaz kareye eşittir.”

Her kare için bu işlemi tekrarlarız.

Değişen tek şey, bahsettiğimiz karenin indeksidir.

Python’da benzer bir görev gerçekleştireceksek, gerçek kareleri kullanamayız.

Bu yüzden kutuları temsil etmek için bir liste kullanalım.

Listedeki her eleman, rengi temsil eden bir dizgedir.

Videoyu 2:18 zamanından başlatarak oynatın ve transkripti 2:18’den itibaren takip edin.

Listedeki her elemandaki renk adını `"white"` olarak değiştirmek istiyoruz.

Listedeki her elemanın aşağıdaki gibi bir indeksi vardır.

Bu, Python’da bir döngü gerçekleştirmek için kullanılan sözdizimidir.

Girintiye dikkat edin.

`range` fonksiyonu bir liste üretir.

Kod, girintideki her şeyi 5 kez tekrar edecektir.

Değeri 6 olarak değiştirirseniz, bunu 6 kez yapar.

Videoyu 2:41 zamanından başlatarak oynatın ve transkripti 2:41’den itibaren takip edin.

Buna karşılık, `i`’nin değeri her seferinde 1 artar.

Bu bölümde, listenin `i`’inci elemanını `"white"` dizgesine değiştiririz.

`i`’nin değeri 0 olarak ayarlanır.

Döngünün her yinelemesi, girintinin başından başlar.

Sonra, girintideki her şeyi çalıştırırız.

Listedeki ilk eleman `"white"` olarak ayarlanır.

Sonra girintinin başına geri döneriz.

Videoyu 3:02 zamanından başlatarak oynatın ve transkripti 3:02’den itibaren takip edin.

Her bir satırda aşağıya doğru ilerleriz.

Listenin değerini değiştiren satıra ulaştığımızda, 1 numaralı indeksin değerini `"white"` olarak ayarlarız.

`i`’nin değeri 1 artırılır.

2 numaralı indeks için süreci tekrarlarız.

Süreç, son elemana ulaşana kadar bir sonraki indeks için devam eder.

Ayrıca Python’da doğrudan bir liste veya demet üzerinde yineleme yapabiliriz.

İndisleri kullanmamıza bile gerek yoktur.

Videoyu 3:29 zamanından başlatarak oynatın ve transkripti 3:29’dan itibaren takip edin.

İşte `squares` listesi.

Listenin her yinelemesinde, `squares` listesinden bir elemanı `square` değişkenine geçiririz.

Bu bölümde `square` değişkeninin değerini gösterelim.

İlk yinelemede, `square`’ın değeri `"red"`’dir.

Sonra ikinci yinelemeye başlarız.

İkinci yinelemede, `square`’ın değeri `"yellow"` olur.

Sonra üçüncü yinelemeye başlarız.

Videoyu 3:52 zamanından başlatarak oynatın ve transkripti 3:52’den itibaren takip edin.

Son yinelemede, `square` değişkeninin değeri `"green"` olur.

Veri üzerinde yineleme yapmak için yararlı bir fonksiyon da `enumerate`’dir.

Bu fonksiyon, listedeki indeksi ve elemanı elde etmek için kullanılabilir.

Her karenin indeksini temsil eden numaralarla kutu benzetmesini kullanalım.

Bu, bir liste üzerinde yineleme yapmak ve her elemanın indeksini sağlamak için kullanılan sözdizimidir.

`squares` listesini kullanır ve renkli kareleri temsil etmek için renk adlarını kullanırız.

`enumerate` fonksiyonunun argümanı listedir; bu durumda `squares` listesidir.

Videoyu 4:23 zamanından başlatarak oynatın ve transkripti 4:23’ten itibaren takip edin.

`i` değişkeni indeks, `square` değişkeni ise listedeki ilgili elemandır.

Ekranın sol tarafını, döngünün farklı yinelemeleri için `square` ve `i` değişkenlerinin farklı değerlerini göstermek için kullanalım.

İlk yinelemede, değişkenin değeri `"red"`’dir; bu, 0’ıncı indekse karşılık gelir ve `i`’nin değeri 0’dır.

İkinci yinelemede, `square` değişkeninin değeri `"yellow"`’dur ve `i`’nin değeri, yani 1, onun indeksine karşılık gelir.

Son indeks için de aynı işlemi tekrarlarız.

`while` döngüleri, `for` döngülerine benzer; fakat belirli sayıda kez bir ifade çalıştırmak yerine, `while` döngüsü yalnızca bir koşul sağlandığı sürece çalışır.

Videoyu 5:07 zamanından başlatarak oynatın ve transkripti 5:07’den itibaren takip edin.

Diyelim ki, `squares` listesindeki tüm turuncu kareleri `new_squares` listesine kopyalamak istiyoruz, ancak turuncu olmayan bir kareyle karşılaşırsak durmak istiyoruz.

`squares` değerlerini önceden bilmiyoruz.

Basitçe, kare turuncu olduğu sürece işleme devam ederiz ya da karenin `"orange"` olup olmadığını kontrol ederiz.

Eğer değilse, dururuz.

İlk örnek için, karenin turuncu olup olmadığını kontrol ederiz. Koşul sağlanır, bu yüzden kareyi kopyalarız.

İkinci kare için süreci tekrarlarız.

Videoyu 5:37 zamanından başlatarak oynatın ve transkripti 5:37’den itibaren takip edin.

Koşul sağlanır, bu yüzden kareyi kopyalarız.

Sonraki yinelemede, mor bir kareyle karşılaşırız.

Koşul sağlanmaz, bu yüzden süreci durdururuz.

Bu, özünde bir `while` döngüsünün yaptığı şeydir.

Soldaki şekli, kodu temsil etmek için kullanalım.

Farklı kareleri temsil etmek için renk adlarından oluşan bir liste kullanacağız.

Boş bir `new_squares` listesi oluştururuz.

Videoyu 6:00 zamanından başlatarak oynatın ve transkripti 6:00’dan itibaren takip edin.

Gerçekte, bu listenin boyutu belirsizdir.

İndisi 0’dan başlatırız.

`while` deyimi, parantezin içindeki koşul yanlış olana kadar girinti içindeki ifadeleri tekrar tekrar çalıştıracaktır.

`squares` listesinin ilk elemanının değerini `new_squares` listesine ekleriz.

`i`’nin değerini 1 artırırız.

`squares` listesinin ikinci elemanının değerini `new_squares` listesine ekleriz.

`i`’nin değerini artırırız.

Videoyu 6:28 zamanından başlatarak oynatın ve transkripti 6:28’den itibaren takip edin.

Artık `squares` dizisindeki değer `"purple"`’dır.

Bu nedenle, `while` deyimi için koşul yanlıştır ve döngüden çıkarız.

Döngülerle ilgili, çoğu gerçek veri içeren daha fazla örnek için lab’lere göz atın.

---

## 📎 Seçim ve Not Alma Arayüz Metni

Bu videoda, özellikle `for` döngüleri ve `while` döngülerini içeren döngüleri ele alacağız.

Bu videoda pek çok görsel örnek kullanacağız.

Seçime eklendi.

Not olarak kaydetmek için `[CTRL + S]` tuşlarına basın.

Beğen

Beğenme

Bir sorun bildir

Seçime eklendi.

Not olarak kaydetmek için `[CTRL + S]` tuşlarına basın.

Beğen

Beğenme

Bir sorun bildir

Seçime eklendi.

Not olarak kaydetmek için `[CTRL + S]` tuşlarına basın.
