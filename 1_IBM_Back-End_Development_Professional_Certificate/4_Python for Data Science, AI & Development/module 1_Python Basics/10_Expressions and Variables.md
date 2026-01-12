# 🧮 İfadeler ve Değişkenler

## 📌 İfadeler Nedir?

Bu videoda, *ifadeler* ve *değişkenleri* ele alacağız.

İfadeler, bilgisayarların gerçekleştirdiği bir tür işlemi tanımlar.

İfadeler, Python'un gerçekleştirdiği işlemlerdir.

Örneğin, birden fazla sayıyı toplamak gibi temel aritmetik işlemler bir ifadedir.

Bu durumda sonuç 160'tır.

Sayıları  *operand* , bu durumda toplama olan matematiksel sembolleri ise *operator* olarak adlandırırız.

## ➕➖✖️➗ Aritmetik İşlemler

Çıkarma işlemlerini, çıkarma işaretini kullanarak gerçekleştirebiliriz.

Bu durumda sonuç negatif bir sayıdır.

Çarpma işlemlerini `*` (yıldız) kullanarak gerçekleştirebiliriz.

Sonuç 25'tir.

Bu durumda işlemler, eksi işareti ve yıldız ile verilir.

Bölme işlemini `/` (eğik çizgi) ile de gerçekleştirebiliriz.

25'in 5'e bölümü 5'tir.

25'in 6'ya bölümü ise yaklaşık 4.167'dir.

Bu derste kullanacağımız sürüm olan Python 3'te, her iki durumda da sonuç bir `float` (ondalıklı sayı) olacaktır.

Sonucun yuvarlandığı tamsayı bölmesi için `//` (çift eğik çizgi) kullanabiliriz.

Dikkat edin, bazı durumlarda sonuçlar normal bölmeyle aynı değildir.

## 🧠 İşlem Sırası ve Parantezler

Python, matematiksel ifadeleri işlerken matematiksel kuralları uygular.

Aşağıdaki işlemler farklı bir sıradadır.

Her iki durumda da Python, nihai sonucu elde etmek için önce çarpmayı, sonra toplamayı gerçekleştirir.

Python ile yapabileceğiniz çok daha fazla işlem vardır.

Daha fazla örnek için laboratuvarlara göz atın.

Ayrıca ders boyunca daha karmaşık işlemleri de ele alacağız.

Parantez içindeki ifadeler önce gerçekleştirilir.

Sonra sonucu 60 ile çarparız.

Sonuç 1920'dir.

## 📦 Değişkenlere Giriş

Şimdi de değişkenlere bakalım.

Değerleri depolamak için değişkenleri kullanabiliriz.

Bu durumda, atama operatörünü, yani eşittir işaretini kullanarak `my_variable` (metinde *my underscore variable* olarak geçen) adlı değişkene 1 değerini atarız.

Daha sonra, değişkenin adını kodun başka bir yerinde tam olarak yazarak bu değeri kullanabiliriz.

Değişkenin değerini göstermek için iki nokta üst üste kullanacağız.

Atama operatörünü kullanarak `my_variable` için yeni bir değer atayabiliriz.

10 değerini atarız.

Değişkenin değeri artık 10'dur.

Değişkenin eski değeri önemli değildir.

İfadelerin sonuçlarını da depolayabiliriz.

Örneğin, birkaç değeri toplar ve sonucu `x` değişkenine atarız.

`x` artık sonucu depolar.

## 🔁 Değer Atama ve Güncelleme

`x` üzerinde de işlemler yapabilir ve sonucu yeni bir `y` adlı değişkende saklayabiliriz.

`y` artık 2.666 değerine sahiptir.

Ayrıca `x` üzerinde işlemler yapabilir ve sonucu yine `x`'e atayabiliriz.

`x` değişkeni artık 2.666 değerine sahiptir.

Daha önce olduğu gibi, `x`'in eski değeri önemli değildir.

Değişkenlerde de `type` komutunu kullanabiliriz.

## 🏷️ Anlamlı Değişken İsimleri

Bir değişkenin ne yaptığını sürekli takip etmek zorunda kalmamak için anlamlı değişken adları kullanmak iyi bir pratiktir.

Diyelim ki, vurgulanmış örneklerdeki dakika sayısını, aşağıdaki müzik veri setinde saat sayısına dönüştürmek istiyoruz.

Toplam dakika sayısını içeren değişkene `total_min` (metinde *total underscore min* olarak geçen) adını veriyoruz.

Yeni bir kelimenin başlangıcını göstermek için alt çizgi kullanmak yaygındır.

Bunun yerine büyük harf de kullanabilirsiniz.

Toplam saat sayısını içeren değişkene ise `total_hour` (metinde *total underscore hour* olarak geçen) adını veriyoruz.

Toplam saat sayısını, `total_min` değerini 60'a bölerek elde edebiliriz.

Sonuç yaklaşık 2.367 saattir.

İlk değişkenin değerini değiştirirsek, değişkenin değeri de değişir.

Nihai sonuç değerleri buna göre değişir, ancak geri kalan kodu değiştirmek zorunda kalmayız.
