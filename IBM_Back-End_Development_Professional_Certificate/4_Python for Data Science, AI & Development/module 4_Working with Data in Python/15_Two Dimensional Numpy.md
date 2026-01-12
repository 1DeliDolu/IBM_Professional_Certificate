# 📐 İki Boyutlu NumPy

## 🎯 Genel Bakış

Birden fazla boyuta sahip NumPy dizileri oluşturabiliriz. Bu bölüm yalnızca 2D dizilere odaklanacak, ancak NumPy’ı çok daha yüksek boyutlarda diziler oluşturmak için de kullanabilirsiniz.

Bu videoda, 2D için temel kavramları ve dizi oluşturmayı, 2D’de indeksleme ve dilimlemeyi ve 2D’de temel işlemleri ele alacağız.

## 🧱 Listeyi 2D NumPy Dizisine Dönüştürme

`a` listesine bakalım; bu liste, her biri aynı boyutta olan üç iç içe liste içerir. Basitlik açısından her liste renk kodludur.

Listeyi aşağıdaki gibi bir NumPy dizisine dönüştürebiliriz. NumPy dizisini dikdörtgen bir dizi olarak hayal etmek faydalıdır; her iç içe liste, matrisin farklı bir satırına karşılık gelir.

## 🧭 `ndim` Özelliği: Eksen / Boyut Sayısı

Eksen veya boyut sayısını (*rank* olarak da anılır) elde etmek için `ndim` özniteliğini kullanabiliriz. `Rank` terimi, bir matriste olduğu gibi doğrusal olarak bağımsız sütunların sayısına karşılık gelmez.

`ndim`’i iç içe listelerin sayısı olarak düşünmek faydalıdır. İlk liste birinci boyutu temsil eder. Bu liste, başka bir liste kümesi içerir. Bu da ikinci boyutu veya ekseni temsil eder.

Listenin içerdiği liste sayısı boyutla ilgili değil, listenin şekliyle ilgilidir.

## 📐 `shape` ve `size`: Şekil ve Eleman Sayısı

1D bir dizide olduğu gibi, `shape` özniteliği bir demet ( *tuple* ) döndürür. Dikdörtgen gösterimi kullanmak da faydalıdır.

Demetteki ilk eleman, orijinal listenin içerdiği iç içe liste sayısına, ya da dikdörtgen gösterimdeki satır sayısına karşılık gelir; bu örnekte bu sayı üçtür.

İkinci eleman, iç içe listelerin her birinin boyutuna ya da dikdörtgen dizideki sütun sayısına karşılık gelir,  *sıfır* . Yerleşik kullanım, bu ekseni sıfır, şu ekseni ise bir olarak aşağıdaki gibi etiketlemektir.

Dizinin boyutunu ( *toplam eleman sayısını* ) elde etmek için `size` özniteliğini de kullanabiliriz. Üç satır ve üç sütun olduğunu görürüz.

Sütun ve satır sayılarını birbiriyle çarptığımızda toplam eleman sayısını elde ederiz; bu örnekte sonuç dokuzdur. Farklı şekillerdeki diziler ve diğer öznitelikler için laboratuvar çalışmalarına ( *labs* ) göz atın.

## 🎯 2D Dizilerde İndeksleme

Dizinin farklı elemanlarına erişmek için köşeli parantezleri kullanabiliriz. Aşağıdaki görsel, liste benzeri gösterim için indeksleme kuralları arasındaki ilişkiyi gösterir.

İlk parantezdeki indeks, her biri farklı renkle gösterilen iç içe listelere karşılık gelir. İkinci parantez, iç içe listenin içindeki belirli bir elemanın indeksine karşılık gelir.

Dikdörtgen gösterimi kullanırken ilk indeks satır indeksine, ikinci indeks sütun indeksine karşılık gelir.

Elemanlara aşağıdaki gibi tek bir parantez kullanarak da erişebiliriz.

## 🔍 İndeks Örnekleri

Aşağıdaki sözdizimini ele alalım. Bu indeks ikinci satıra, şu indeks ise üçüncü sütuna karşılık gelir; değer 23’tür.

Şu örneği düşünelim: Bu indeks birinci satıra, ikinci indeks birinci sütuna karşılık gelir ve değer 11’dir.

## ✂️ 2D Dizilerde Dilimleme (Slicing)

NumPy dizilerinde dilimleme ( *slicing* ) de kullanabiliriz. İlk indeks birinci satıra karşılık gelir. İkinci indeks ilk iki sütuna erişir.

Bu örnekte, ilk indeks ilk iki satıra karşılık gelir. İkinci indeks son sütuna erişir.

## ➕ Dizilerin Toplanması

Dizileri de toplayabiliriz; süreç, matris toplamına tamamen özdeştir.

`X` matrisini ele alalım; her bir eleman farklı bir renkle gösterilmiştir. `Y` matrisini ele alalım. Benzer şekilde, her eleman farklı bir renkle gösterilmiştir.

Bu matrisleri toplayabiliriz. Bu, aynı konumdaki elemanların toplanmasına karşılık gelir; yani aynı renkli kutular içinde yer alan elemanları birbirine ekleriz.

Sonuç, `Y` veya `X` matrisiyle aynı boyuta sahip yeni bir matristir. Bu yeni matrisin her bir elemanı, `X` ve `Y` içindeki karşılık gelen elemanların toplamıdır.

NumPy’da iki diziyi toplamak için, önce diziyi tanımlarız; bu örnekte `X` dizisini. Sonra ikinci dizi `Y`’yi tanımlar, dizileri toplarız. Elde edilen sonuç, matris toplamıyla aynıdır.

## ✖️ Skaler ile Çarpma

Bir NumPy dizisini bir skalerle çarpmak, bir matrisi skalerle çarpmakla aynıdır.

`Y` matrisini ele alalım. Matrisi bu skaler iki ile çarparsak, matrisin her bir elemanını iki ile çarpmış oluruz. Sonuç, her elemanı ikiyle çarpılmış, aynı boyutta yeni bir matristir.

`Y` dizisini ele alalım. Önce diziyi tanımlarız, ardından diziyi aşağıdaki gibi bir skalerle çarpar ve sonucu `Z` değişkenine atarız. Sonuç, her elemanı ikiyle çarpılmış yeni bir dizidir.

## ⭕ Eleman Bazlı ( *Hadamard* ) Çarpım

İki dizinin çarpımı, eleman bazlı bir çarpıma, yani *Hadamard çarpımına* karşılık gelir.

`X` dizisini ve `Y` dizisini ele alalım.  *Hadamard çarpımı* , aynı konumdaki her elemanın çarpılmasına karşılık gelir; yani aynı renkli kutular içinde yer alan elemanları birbiriyle çarparız.

Sonuç, `Y` veya `X` matrisiyle aynı boyuta sahip yeni bir matristir. Bu yeni matrisin her bir elemanı, `X` ve `Y` içindeki karşılık gelen elemanların çarpımıdır.

`X` ve `Y` dizilerini ele alalım. İki dizi `X` ve `Y`’nin çarpımını tek satırda hesaplayabilir ve sonucu aşağıdaki gibi `Z` değişkenine atayabiliriz. Elde edilen sonuç, *Hadamard çarpımı* ile aynıdır.

## ✳️ Matris Çarpımı

NumPy dizileriyle matris çarpımı da gerçekleştirebiliriz. Matris çarpımı biraz daha karmaşıktır, ancak temel bir genel bakış sunalım.

Her satırı farklı bir renkle gösterilen `A` matrisini düşünün. Ayrıca, her sütunu farklı bir renkle gösterilen `B` matrisini düşünün.

Lineer cebirde, `A` matrisini `B` matrisiyle çarpmadan önce, `A` matrisindeki sütun sayısının (bu örnekte üç) `B` matrisindeki satır sayısına (bu örnekte yine üç) eşit olduğundan emin olmalıyız.

Matris çarpımında, yeni matrisin i’inci satır ve j’inci sütunundaki elemanı elde etmek için, `A` matrisinin i’inci satırı ile `B` matrisinin j’inci sütunlarının *nokta çarpımını* alırız.

Birinci sütun, birinci satır için, `A` matrisinin birinci satırının `B` matrisinin birinci sütunuyla nokta çarpımını aşağıdaki gibi alırız. Sonuç sıfırdır.

Yeni matrisin birinci satırı ve ikinci sütunu için, `A` matrisinin birinci satırının nokta çarpımını alırız, ancak bu kez `B` matrisinin ikinci sütununu kullanırız; sonuç ikidir.

Yeni matrisin ikinci satırı ve birinci sütunu için, `A` matrisinin ikinci satırının `B` matrisinin birinci sütunuyla nokta çarpımını alırız; sonuç sıfırdır.

Son olarak, yeni matrisin ikinci satırı ve ikinci sütunu için, `A` matrisinin ikinci satırının `B` matrisinin ikinci sütunuyla nokta çarpımını alırız; sonuç ikidir.

## ✅ Kapanış

NumPy’da `A` ve `B` NumPy dizilerini tanımlayabiliriz. Matris çarpımını gerçekleştirip sonucu `C` dizisine atayabiliriz. Sonuç `C` dizisidir. Bu, `A` ve `B` dizilerinin matris çarpımına karşılık gelir.

NumPy ile bunun ötesinde yapabileceğiniz çok daha fazla şey vardır. `numpy.org` adresine göz atın.

Bu videoyu izlediğiniz için teşekkürler.
