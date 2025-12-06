# 📚 Listeler ve Demetler

## 🎥 Video Hakkında

Bu videoda listeleri ( *lists* ) ve demetleri ( *tuples* ) ele alacağız.

Bunlara bileşik veri tipleri ( *compound data types* ) denir ve Python’daki temel veri yapısı türlerinden bazılarıdır.

---

## 🔗 Demetler ( *Tuples* )

### 📐 Demetlerin Tanımı

Demetler ( *tuples* ), sıralı bir dizilimdir ( *ordered sequence* ).

İşte `ratings` adında bir demet örneği.

Demetler, parantez içinde virgülle ayrılmış öğeler şeklinde ifade edilir.

Bunlar, parantezlerin içindeki değerlerdir.

Python’da `string`, `integer`, `float` gibi farklı türler vardır.

Bunların hepsi bir demetin içinde bulunabilir, ancak değişkenin tipi `tuple` olur.

---

### 🔢 Demetlerde İndeksleme

Bir demetin her bir öğesine bir indeks aracılığıyla erişilebilir.

Aşağıdaki tablo, indekle demetteki öğeler arasındaki ilişkiyi gösterir.

İlk öğeye, demetin adı yazılarak ve ardından köşeli parantez içinde indeks numarası belirtilerek erişilebilir.

Bu durumda indeks `0`’dır.

İkinci öğeye de aynı şekilde erişebiliriz.

Son öğeye de erişebiliriz.

Python’da negatif indeks kullanabiliriz.

İlişki şöyledir.

Karşılık gelen değerler burada gösterilmiştir.

---

### ➕ Demetleri Birleştirme ve Dilimleme

Demetleri toplama işlemiyle birleştirebilir veya bir araya getirebiliriz.

Sonuç, aşağıdaki gibi, şu indekslere sahip olur.

Bir demetten birden fazla öğe almak istersek, demetleri dilimleyebiliriz ( *slice* ).

Örneğin, ilk üç öğeyi istiyorsak, şu komutu kullanırız.

Son indeks, istediğiniz indeks değerinden bir fazladır.

Benzer şekilde, son iki öğeyi istiyorsak, şu komutu kullanırız.

Son indeksin, demetin son indeksinden bir büyük olduğuna dikkat edin.

Bir demetin uzunluğunu elde etmek için `len` komutunu kullanabiliriz.

Beş öğe olduğundan sonuç beştir.

---

### 🔒 Demetlerin Değiştirilemezliği ( *Immutability* )

Demetler değiştirilemezdir ( *immutable* ), yani onları değiştiremeyiz.

Bunun neden önemli olduğunu görmek için, `ratings 1` değişkenini `ratings`’e eşitlediğimizde ne olduğuna bakalım.

Nelerin gerçekleştiğini basitleştirilmiş şekilde açıklamak için görseli kullanalım.

Her bir değişken bir demet içermez; bunun yerine aynı değiştirilemez demet nesnesine başvurur.

Nesneler hakkında daha fazla bilgi için Nesneler ve Sınıflar ( *Objects and Classes* ) modülüne bakın.

Diyelim ki indeks `2`’deki öğeyi değiştirmek istiyoruz.

Demetler değiştirilemez olduğu için bunu yapamayız.

Bu nedenle, demet değiştirilemez olduğu için, yani onu değiştiremeyeceğimiz için, `ratings` değiştiğinde `ratings 1` etkilenmez.

`ratings` değişkenine farklı bir demet atayabiliriz.

`ratings` değişkeni artık başka bir demete başvurur.

Değiştirilemezliğin bir sonucu olarak, bir demeti değiştirmek ( *manipulate* ) istersek, bunun yerine yeni bir nesne oluşturmamız gerekir.

Örneğin, bir demeti sıralamak istersek, `sorted` fonksiyonunu kullanırız.

Girdi, orijinal demettir.

Çıktı ise yeni, sıralanmış bir listedir.

Fonksiyonlar hakkında daha fazla bilgi için fonksiyonlarla ilgili videomuza bakın.

---

### 🌳 İç İçe Demetler ( *Nesting* )

Bir demet, başka demetler ile birlikte diğer karmaşık veri tiplerini de içerebilir.

Bu duruma iç içe yerleştirme ( *nesting* ) denir.

Bu öğelere standart indeksleme yöntemlerini kullanarak erişebiliriz.

Eğer bir indeksin karşılığında bir demet seçersek, aynı indeks kuralı geçerlidir.

Böylece demetin içindeki değerlere erişebiliriz.

Örneğin, ikinci öğeye erişebiliriz.

Bu indekslemeyi doğrudan `nt` adlı demet değişkenine uygulayabiliriz.

Bunu bir ağaç gibi hayal etmek faydalıdır.

Bu iç içe yapıyı bir ağaç gibi görselleştirebiliriz.

Demetin aşağıdaki indeksleri vardır.

Eğer diğer demetlerle birlikte indeksleri ele alırsak, `2` numaralı indekste yer alan demetin iki öğe içeren bir demet olduğunu görürüz.

Bu iki indekse erişebiliriz.

Aynı kural `3` numaralı indeks için de geçerlidir.

Bu demetlerin içindeki öğelere de erişebiliriz.

Bu işlemi sürdürmeye devam edebiliriz.

Ağaca daha derin seviyelerde de erişmek için bir köşeli parantez daha ekleyebiliriz.

String içindeki farklı karakterlere veya ilk demetin içinde bulunan ikinci demetteki çeşitli öğelere erişebiliriz.

---

## 📋 Listeler ( *Lists* )

### 📐 Listelerin Tanımı ve Özellikleri

Listeler de Python’da popüler bir veri yapısıdır.

Listeler de sıralı bir dizilimdir ( *ordered sequence* ).

İşte `L` adlı bir liste.

Bir liste, köşeli parantezlerle gösterilir.

Pek çok açıdan listeler, demetlere benzer.

Önemli farklardan biri, listelerin değiştirilebilir ( *mutable* ) olmasıdır.

Listeler `string`, `float`, `integer` içerebilir.

Başka listeleri iç içe yerleştirebiliriz.

Ayrıca demetleri ve diğer veri yapılarını da iç içe yerleştiririz.

İç içe yerleştirme için aynı indeksleme kuralları geçerlidir.

---

### 🔢 Listelerde İndeksleme ve Dilimleme

Demetlerde olduğu gibi, bir listenin her öğesine bir indeks aracılığıyla erişilebilir.

Aşağıdaki tablo, indekle listedeki öğeler arasındaki ilişkiyi gösterir.

İlk öğeye, listenin adı yazılarak ve ardından köşeli parantez içinde indeks numarası belirtilerek erişilebilir;

bu durumda indeks `0`’dır.

İkinci öğeye de şu şekilde erişebiliriz.

Son öğeye de erişebiliriz.

Python’da negatif indeks kullanabiliriz.

İlişki şöyledir.

Karşılık gelen indeksler de şöyledir.

Listelerde de dilimleme ( *slicing* ) yapabiliriz.

Örneğin, bu listedeki son iki öğeyi istiyorsak, şu komutu kullanırız.

Son indeksin, listenin uzunluğundan bir büyük olduğuna dikkat edin.

Listeler ve demetler için indeksleme kuralları aynıdır.

Daha fazla örnek için lab’lere bakın.

---

### ➕ Listeleri Birleştirme

Listeleri toplama işlemiyle birleştirebilir veya bir araya getirebiliriz.

Sonuç aşağıdaki gibidir.

Yeni listenin aşağıdaki indeksleri vardır.

---

### ✏️ Listeleri Değiştirme: `extends` ve `append`

Listeler değiştirilebilir olduğundan, onları değiştirebiliriz.

Örneğin, `extends` metodunu, önce bir nokta, ardından metodun adı ve sonra parantezler ekleyerek uygularız.

Parantezlerin içindeki argüman, orijinal listeyle birleştireceğimiz yeni listedir.

Bu durumda, yeni bir liste `L1` oluşturmak yerine, orijinal liste `L`, iki yeni öğe eklenerek değiştirilir.

Metotlar hakkında daha fazla bilgi edinmek için Nesneler ve Sınıflar ( *objects and classes* ) ile ilgili videomuza göz atın.

Benzer bir başka metot da `append`’tir.

`extended` yerine `append` uygularsak, listeye bir öğe ekleriz.

İndekslere baktığımızda yalnızca bir öğe daha olduğunu görürüz.

`3` numaralı indeks, eklediğimiz listeyi içerir.

Her seferinde bir metot uyguladığımızda, liste değişir.

`extend` uygularsak listeye iki yeni öğe ekleriz.

`L` listesi, iki yeni öğe eklenerek değiştirilir.

Eğer string `A`’yı `append` edersek, listeyi daha da değiştirir ve string `A`’yı eklemiş oluruz.

Listeler değiştirilebilir olduğundan, onları değiştirebiliriz.

---

### 🗑️ Listelerde Öğeleri Silme

Örneğin, ilk öğeyi şu şekilde değiştirebiliriz.

Liste artık `HardRock 10 1.2` olur.

Bir listedeki öğeyi `del` komutunu kullanarak silebiliriz.

Yalnızca, argüman olarak kaldırmak istediğimiz liste öğesini belirtiriz.

Örneğin, ilk öğeyi kaldırmak istiyorsak, sonuç `10 1.2` olur.

İkinci öğeyi de silebiliriz.

Bu işlem, listedeki ikinci öğeyi kaldırır.

---

### 🔁 String’leri Listeye Dönüştürme: `split`

Bir string’i `split` kullanarak listeye dönüştürebiliriz.

Örneğin, `split` metodu, aralarında boşluk bulunan her karakter grubunu, listenin bir öğesine dönüştürür.

`split` fonksiyonunu, sınırlayıcı ( *delimiter* ) olarak bilinen belirli bir karakter üzerinde string’leri ayırmak için kullanabiliriz.

Bölmek istediğimiz sınırlayıcıyı, bu durumda bir virgülü, argüman olarak geçiririz.

Sonuç, her bir öğesi virgülle ayrılmış karakter gruplarına karşılık gelen bir listedir.

---

### 🧬 Aliasing ve Liste Klonlama

Bir değişken `b`’yi `a`’ya eşitlediğimizde, hem `a` hem de `b` aynı listeye başvurur.

Aynı nesneye başvuran birden fazla isim olmasına *aliasing* denir.

Liste slaytından, `b` içindeki ilk öğenin `HardRock` olarak ayarlandığını biliyoruz.

Eğer `a`’daki ilk öğeyi `banana` olarak değiştirirsek, bir yan etki elde ederiz.

`b`’nin değeri de bunun bir sonucu olarak değişir.

`a` ve `b` aynı listeye başvurduğundan, `a`yı değiştirirsek, `b` listesi de değişir.

Liste `a`yı değiştirdikten sonra `b`’nin ilk öğesini kontrol edersek, `HardRock` yerine `banana` elde ederiz.

Liste `a`nın bir kopyasını oluşturmak için şu söz dizimini kullanabilirsiniz.

`a` değişkeni bir listeye başvurur.

`b` değişkeni ise orijinal listenin yeni bir kopyasına veya klonuna başvurur.

Artık `a`yı değiştirirseniz, `b` değişmeyecektir.

---

### ℹ️ Daha Fazla Bilgi: `help`

Listeler, demetler ve Python’daki daha birçok nesne hakkında daha fazla bilgi edinmek için `help` komutunu kullanabiliriz.

Yalnızca listeyi, demeti veya başka herhangi bir Python nesnesini argüman olarak geçirmeniz yeterlidir.

Listelerle yapabileceğiniz diğer şeyler için lab’lere bakın.
