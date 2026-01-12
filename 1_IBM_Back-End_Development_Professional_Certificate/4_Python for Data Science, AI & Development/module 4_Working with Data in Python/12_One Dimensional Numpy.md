# 📏 Tek Boyutlu NumPy

## 🧮 1D NumPy ve  *ndarray* ’lere Giriş

Bu videoda, özellikle  *ndarray* ’ler olmak üzere 1 boyutlu (1D) NumPy’yi ele alacağız. NumPy, bilimsel hesaplama için bir kütüphanedir. Birçok kullanışlı fonksiyona sahiptir. Hız ve bellek gibi başka birçok avantajı da vardır.

NumPy aynı zamanda pandas’ın temelidir, bu yüzden pandas videomuza da göz atın. Bu videoda temelleri, dizi oluşturmayı, indeksleme ve dilimlemeyi, temel işlemleri ve evrensel fonksiyonları ele alacağız. Şimdi bir NumPy dizisinin nasıl oluşturulacağını inceleyelim.

---

## 📦 Python Listeleri ve NumPy Dizileri ( *ndarray* )

Bir Python listesi, veriyi saklamanıza ve erişmenize izin veren bir kaptır. Her öğe bir indeksle ilişkilidir. Her bir öğeye köşeli parantez kullanarak aşağıdaki şekilde erişebiliriz.

Bir NumPy dizisi ya da  *ndarray* , listeye benzer. Genellikle boyutu sabittir ve her bir öğe aynı türdendir. Bu örnekte öğeler tam sayıdır ( *integer* ).

Bir listeyi NumPy dizisine dönüştürmek için önce NumPy’yi içe aktarabiliriz. Daha sonra listeyi şu şekilde dönüştürürüz.

Veriye bir indeks aracılığıyla erişebiliriz. Listelerde olduğu gibi, her öğeye bir tamsayı ve köşeli parantez ile erişebiliriz. `a`’nın değeri şu şekilde saklanır.

Dizinin türünü ( *type* ) kontrol edersek `NumPy.ndarray` elde ederiz. NumPy dizileri aynı türde veri içerdiği için, dizinin öğelerinin veri türünü elde etmek amacıyla `dtype` özelliğini kullanabiliriz. Bu örnekte 64 bitlik bir tam sayıdır.

---

## 🧱 NumPy Dizilerinin Temel Özellikleri

Şimdi `a` dizisini kullanarak bazı temel dizi özelliklerini gözden geçirelim.

`size` özelliği, dizideki öğe sayısıdır. Beş öğe olduğundan, sonuç beştir.

Sonraki iki özellik daha yüksek boyutlara geçtiğimizde daha anlamlı olacaktır, ancak yine de inceleyelim.

`ndim` özelliği, dizinin boyut sayısını ya da dizinin derecesini ( *rank* ) temsil eder; bu örnekte bu değer birdir.

`shape` özelliği, dizinin her bir boyuttaki boyutunu belirten tam sayılardan oluşan bir demettir ( *tuple* ).

Gerçek sayılarla bir NumPy dizisi oluşturabiliriz. Dizinin türünü kontrol ettiğimizde yine `NumPy.ndarray` elde ederiz.

`dtype` özelliğini incelediğimizde, öğeler tam sayı olmadığı için `float 64` görürüz. Daha birçok özellik vardır. NumPy.org’a göz atın.

---

## ✂️ İndeksleme ve Dilimleme ( *Slicing* ) Yöntemleri

Bazı indeksleme ve dilimleme yöntemlerini gözden geçirelim.

Dizinin ilk öğesini şu şekilde 100 olarak değiştirebiliriz. Dizinin ilk değeri artık 100’dür.

Dizinin beşinci öğesini de şu şekilde değiştirebiliriz. Beşinci öğe artık sıfırdır.

Listeler ve demetler ( *tuple* ) gibi, bir NumPy dizisini de dilimleyebiliriz. Dizinin öğeleri aşağıdaki indekse karşılık gelir.

Birden üçe kadar olan öğeleri seçip, bunları yeni bir NumPy dizisi `d`’ye şu şekilde atayabiliriz. `d` içindeki öğeler ilgili indekslere karşılık gelir.

Listelerde olduğu gibi, son indekse karşılık gelen öğeyi saymayız. İlgili indeksleri yeni değerlere şu şekilde atayabiliriz.

`c` dizisinin artık yeni değerleri vardır. NumPy ile neler yapabileceğiniz konusunda daha fazla örnek için laboratuvarları veya NumPy.org’u inceleyin.

---

## 🧮 1D Dizilerde İşlemler ve Vektörler

NumPy, veri biliminde yaygın olarak gerçekleştirilen birçok işlemi yapmayı kolaylaştırır. Aynı işlemler, normal Python’a kıyasla NumPy’de genellikle hesaplama açısından daha hızlıdır ve daha az bellek gerektirir.

Şimdi bu işlemlerden bazılarını tek boyutlu diziler üzerinde gözden geçireceğiz.

Daha ilginç hale getirmek için pek çok işlemi Öklidyen vektörler bağlamında ele alacağız.

Vektör toplama, veri biliminde yaygın olarak kullanılan bir işlemdir. İki öğeli `u` vektörünü ele alalım. Öğeler farklı renklerle ayırt edilir. Benzer şekilde, iki bileşenli `v` vektörünü düşünelim.

Vektör toplamında, bu iki vektörden yeni bir vektör oluştururuz; bu durumda bu vektör `z`’dir. `z`’nin ilk bileşeni, `u` ve `v` vektörlerinin ilk bileşenlerinin toplamıdır. Benzer şekilde, ikinci bileşen `u` ve `v`’nin ikinci bileşenlerinin toplamıdır.

Bu yeni `z` vektörü artık `u` ve `v` vektörlerinin doğrusal bir bileşimidir. Vektör toplamını doğru parçaları veya oklarla temsil etmek yardımcı olur.

---

## 🎯 Vektörlerin Görselleştirilmesi ve Toplama

İlk vektör kırmızı ile temsil edilir. Vektör, iki bileşenin yönünde işaret eder.

Vektörün ilk bileşeni 1’dir. Sonuç olarak, ok yatay yönde orijinden bir birim kadar kayar.

İkinci bileşen 0’dır. Bu bileşeni dikey yönde temsil ederiz. Bu bileşen 0 olduğundan, vektör dikey yönde işaret etmez.

İkinci vektörü mavi ile temsil ederiz. İlk bileşen 0’dır. Bu nedenle ok yatay yöne işaret etmez.

İkinci bileşen 1’dir. Sonuç olarak, vektör dikey yönde bir birim işaret eder.

`u` ve `v` vektörlerini topladığımızda yeni `z` vektörünü elde ederiz. İlk bileşeni toplarız. Bu, yatay yöne karşılık gelir.

İkinci bileşeni de toplarız.

Vektörleri toplarken, `v` vektörünün kuyruğunu `u` vektörünün ucuna yerleştirmek, yani *uçtan kuyruğa* yöntemini kullanmak faydalıdır.

Yeni `z` vektörü, ilk `u` vektörünün tabanı ile ikinci `v` vektörünün kuyruğunu birleştirerek oluşturulur.

Aşağıdaki üç satır kod, iki listeyi toplar ve sonucu `z` listesine yerleştirir.

Ayrıca, tek satırlık NumPy kodu ile de vektör toplama yapabiliriz. Sağ tarafta gösterildiği gibi, iki liste üzerinde vektör toplama yapmak için birden çok satıra ihtiyaç duyulur.

Buna ek olarak, NumPy kodu çok daha hızlı çalışacaktır. Bu, çok fazla veriniz olduğunda önemlidir.

---

## ➖ Vektör Çıkarma ve Skalerle Çarpma

Toplama işaretini çıkarma işaretine çevirerek vektör çıkarma da yapabiliriz. Sağ tarafta gösterildiği gibi, iki liste üzerinde vektör çıkarma yapmak için de birden çok satıra ihtiyaç duyulur.

Bir vektörün skalerle çarpılması da yaygın olarak yapılan bir işlemdir. `y` vektörünü ele alalım. Her bileşen farklı bir renkle belirtilmiştir.

Vektörü, bu örnekte 2 olan bir skaler değerle çarparız. Vektörün her bileşeni 2 ile çarpılır. Bu durumda her bileşen iki katına çıkar.

Neler olduğunu görselleştirmek için doğru parçalarını veya okları kullanabiliriz. Orijinal `y` vektörü mor renktedir.

`y`’yi 2 değerine sahip bir skalerle çarptıktan sonra vektör, kırmızı ile gösterildiği gibi 2 birim uzar.

Yeni vektör her yönde iki kat daha uzundur.

---

## ✖️ Hadamard Çarpımı ve Noktasal Çarpım ( *Dot Product* )

Skalerle vektör çarpımı, NumPy kullanarak yalnızca tek satır kod gerektirir. Sağ tarafta gösterildiği gibi, Python listeleriyle aynı görevi gerçekleştirmek için birden çok satıra ihtiyaç duyulur. Buna ek olarak, işlem çok daha yavaş olacaktır.

Hadamard çarpımı, veri biliminde yaygın olarak kullanılan bir diğer işlemdir.

Aşağıdaki iki vektörü, `u` ve `v`’yi ele alalım. `u` ve `v`’nin Hadamard çarpımı, yeni bir `z` vektörüdür.

`z`’nin ilk bileşeni, `u` ve `v`’nin ilk öğelerinin çarpımıdır. Benzer şekilde, ikinci bileşen `u` ve `v`’nin ikinci öğelerinin çarpımıdır.

Ortaya çıkan vektör, `u` ve `v`’nin eleman bazında çarpımından oluşur.

NumPy ile Hadamard çarpımını da tek satır kod ile gerçekleştirebiliriz. Sağ tarafta gösterildiği gibi, iki liste üzerinde Hadamard çarpımı yapmak için birden çok satıra ihtiyaç duyulur.

Noktasal çarpım ( *dot product* ), veri biliminde yaygın olarak kullanılan bir başka işlemdir.

`u` ve `v` vektörlerini ele alalım. Noktasal çarpım, aşağıdaki terimle verilen ve iki vektörün ne kadar benzer olduğunu ifade eden tek bir sayıdır.

İlk olarak `v` ve `u`’nun ilk bileşenlerini çarparız.

Daha sonra ikinci bileşenleri çarpar ve sonucu toplarız. Ortaya çıkan sonuç, iki vektörün ne kadar benzer olduğunu temsil eden bir sayıdır.

Ayrıca, NumPy’nin `dot` fonksiyonunu kullanarak noktasal çarpım gerçekleştirebilir ve sonucu aşağıdaki gibi `result` değişkenine atayabiliriz.

---

## 📊 Yayılım ( *Broadcasting* ) ve Evrensel Fonksiyonlar

`u` dizisini ele alalım. Dizi aşağıdaki öğeleri içerir. Dizinin üzerine bir skaler değer eklersek, NumPy bu değeri dizinin her öğesine ekler.

Bu özelliğe *broadcasting* (yayılım) denir.

Evrensel bir fonksiyon ( *universal function* ),  *nd array* ’ler üzerinde çalışan bir fonksiyondur. Evrensel bir fonksiyonu bir NumPy dizisine uygulayabiliriz.

`a` dizilerini ele alalım. `mean` metodunu kullanarak `a` içindeki tüm öğelerin ortalamasını ya da ortalama değerini hesaplayabiliriz. Bu, tüm öğelerin ortalamasına karşılık gelir. Bu durumda sonuç sıfırdır.

Daha birçok fonksiyon vardır.

Örneğin, `b` NumPy dizilerini ele alalım. `max` metodunu kullanarak en büyük değeri bulabiliriz. En büyük değerin 5 olduğunu görürüz. Bu nedenle `max` metodu 5 döndürür.

NumPy’yi, NumPy dizilerini yeni NumPy dizilerine eşleyen fonksiyonlar oluşturmak için kullanabiliriz.

Ekranın sol tarafında biraz kod uygular ve ekranda sağ tarafı, neler olduğunu göstermek için kullanırız.

NumPy’de `pi` değerine aşağıdaki gibi erişebiliriz.

---

## 🌊 Sinüs Fonksiyonu ve Radyan Dizileri

Radyan cinsinden aşağıdaki NumPy dizisini oluşturabiliriz. Bu dizi, aşağıdaki vektöre karşılık gelir.

`sine` fonksiyonunu `x` dizisine uygulayabilir ve değerleri `y` dizisine atayabiliriz. Bu, sinüs fonksiyonunun dizideki her bir öğeye uygulanması anlamına gelir.

Bu, sinüs fonksiyonunun vektörün her bir bileşenine uygulanmasına karşılık gelir.

Sonuç, `x` dizisindeki her öğeye sinüs fonksiyonunun uygulanmasına karşılık gelen her değerin bulunduğu yeni bir `y` dizisidir.

---

## 📈 `line space` ile Örnekleme ve Grafik Çizimi

Matematiksel fonksiyonları çizmek için yararlı bir fonksiyon `line space`’tir.

`line space`, belirtilen aralık boyunca eşit aralıklı sayılar döndürür.

Dizinin başlangıç noktasını, bitiş noktasını belirtiriz; `num` parametresi, üretilecek örnek sayısını belirtir; bu örnekte bu değer 5’tir.

Örnekler arasındaki aralık 1’dir.

`num` parametresini 9 olarak değiştirirsek, −2 ile 2 aralığı boyunca eşit aralıklı 9 sayı elde ederiz.

Sonuç olarak, ardışık örnekler arasındaki fark, daha önce 1 iken bu sefer 0.5’tir.

`line space` fonksiyonunu, 0 ile `2 pi` aralığı boyunca eşit aralıklı 100 örnek üretmek için kullanabiliriz.

NumPy’nin `sine` fonksiyonunu kullanarak `x` dizisini yeni bir `y` dizisine eşleyebiliriz.

Fonksiyonu çizmemize yardımcı olması için `pi plot` kütüphanesini `plt` takma adıyla içe aktarabiliriz.

Bir Jupyter notebook kullandığımız için grafiği göstermek üzere şu komutu kullanırız:

```text
matplotlib inline
```

Aşağıdaki komut bir grafik çizer. İlk girdi, yatay ya da x eksenine karşılık gelen değerlere karşılık gelir.

İkinci girdi, düşey ya da y eksenine karşılık gelen değerlere karşılık gelir.

NumPy ile yapabileceğiniz çok daha fazla şey vardır. Daha fazlası için laboratuvarlara ve numpy.org’a göz atın.

Teşekkürler, bu videoyu izlediğiniz için.
