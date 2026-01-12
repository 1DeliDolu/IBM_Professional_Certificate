# 🧩 Fonksiyonlar

## ⚙️ Genel Bakış ve Yeniden Kullanım

Bu videoda fonksiyonları ele alacağız. Python'un yerleşik bazı fonksiyonlarını nasıl kullanacağınızı ve ayrıca kendi fonksiyonunuzu nasıl oluşturacağınızı öğreneceksiniz. Fonksiyonlar bir girdi alır, sonra bir çıktı veya değişiklik üretir. Fonksiyon, tekrar tekrar kullanabileceğiniz bir kod parçasıdır. Kendi fonksiyonunuzu uygulayabilirsiniz, ancak birçok durumda başkalarının fonksiyonlarını kullanırsınız. Bu durumda, yalnızca fonksiyonun nasıl çalıştığını ve bazı durumlarda fonksiyonların nasıl içe aktarılacağını bilmeniz gerekir. Turuncu ve sarı karelerin benzer kod bloklarını temsil ettiğini varsayalım.

Kodu bazı girdilerle çalıştırabilir ve bir çıktı elde edebiliriz. Eğer görevi yerine getirecek bir fonksiyon tanımlarsak, tek yapmamız gereken fonksiyonu çağırmaktır. Küçük karelerin, fonksiyonu çağırmak için kullanılan kod satırlarını temsil ettiğini düşünelim. Bu uzun kod satırlarını, fonksiyonu birkaç kez çağırarak değiştirebiliriz. Artık sadece fonksiyonu çağırabiliriz. Kodumuz çok daha kısadır. Kod aynı görevi yerine getirir.

Süreci şu şekilde düşünebilirsiniz. Fonksiyon  *f1* 'i çağırdığımızda, fonksiyona bir girdi aktarırız. Bu değerler, yazdığınız tüm o kod satırlarına iletilir. Bunun sonucunda bir değer döner. Bu değeri kullanabilirsiniz. Örneğin, bu değeri yeni bir fonksiyona,  *f2* 'ye girdi olarak verebilirsiniz. Bu yeni fonksiyon  *f2* 'yi çağırdığımızda, değer başka bir kod satırları kümesine aktarılır.

Fonksiyon bir değer döndürür. Bu süreç, çağırdığınız fonksiyona değerleri aktararak tekrarlanır. Bu fonksiyonları kaydedip yeniden kullanabilirsiniz ya da başkalarının fonksiyonlarını kullanabilirsiniz.

---

## 🧰 Python’un Yerleşik Fonksiyonları

Python'un birçok yerleşik fonksiyonu vardır. Bu fonksiyonların içten içe nasıl çalıştığını bilmek zorunda değilsiniz; yalnızca hangi görevi yerine getirdiklerini bilmeniz yeterlidir. `len` fonksiyonu, bir dizi türündeki girdi (örneğin bir string veya liste) ya da bir koleksiyon türündeki girdi (örneğin bir sözlük veya küme) alır ve bu dizinin veya koleksiyonun uzunluğunu döndürür. Aşağıdaki listeyi ele alalım.

`len` fonksiyonu bu listeyi bir argüman olarak alır ve sonucu `l` değişkenine atarız. Fonksiyon, listede sekiz öğe olduğunu belirler ve sonra listenin uzunluğunu, bu durumda sekizi, döndürür.

`sum` fonksiyonu, bir demet (tuple) veya liste gibi yinelenebilir bir yapı alır ve tüm öğelerin toplamını döndürür. Aşağıdaki listeyi ele alalım. Listeyi `sum` fonksiyonuna aktarır ve sonucu `s` değişkenine atarız. Fonksiyon, tüm öğelerin toplamını hesaplar ve ardından bunu döndürür. Bu durumda değer 70'tir.

---

## 🔀 Bir Listeyi Sıralamanın İki Yolu: `sorted` ve `sort`

Bir listeyi sıralamanın iki yolu vardır. İlki, `sorted` fonksiyonunu kullanmaktır. Ayrıca listenin `sort` metodunu da kullanabiliriz. Metotlar fonksiyonlara benzer. Aradaki farkı göstermek için bunu bir örnek olarak kullanalım. `sorted` fonksiyonu, yeni bir sıralanmış liste veya demet döndürür. *album ratings* listesini ele alalım.

*album ratings* listesine `sorted` fonksiyonunu uygulayabilir ve yeni bir liste *sorted album rating* elde edebiliriz. Sonuç, yeni bir sıralanmış listedir. *album ratings* listesine baktığımızda hiçbir şeyin değişmediğini görürüz. Genelde fonksiyonlar, bu örnekte bir liste olan bir girdi alır. Yeni bir çıktı üretirler; bu örnekte bu, sıralanmış bir listedir.

Eğer `sort` metodunu kullanırsak, *album ratings* listesi değişecek ve yeni bir liste oluşturulmayacaktır. Süreci açıklamaya yardımcı olması için diyagramı kullanalım. Bu durumda, dikdörtgen *album ratings* listesini temsil eder. Listeye `sort` metodunu uyguladığımızda, *album rating* listesi değişir. Önceki durumdan farklı olarak, *album rating* listesinin değiştiğini görürüz. Bu durumda yeni bir liste oluşturulmaz.

---

## 🏗️ Kendi Fonksiyonlarımızı Oluşturmak

Artık Python'da fonksiyonların nasıl kullanılacağını gördüğümüze göre, kendi fonksiyonlarımızı nasıl oluşturacağımıza bakalım. Şimdi, Python'da kendi fonksiyonlarınızı yazmaya başlamanız için bir giriş yapacağız. Bu, girdi değerini alıp üzerine bir ekleyerek döndüren bir Python fonksiyonu örneğidir.

### ✏️ Fonksiyon Tanımı

Bir fonksiyonu tanımlamak için `def` anahtar sözcüğü ile başlarız. Fonksiyonun adı, yaptığı işi betimleyici olmalıdır. Parantez içinde fonksiyonun biçimsel parametresi `a` bulunur ve ardından iki nokta üst üste gelir. Girintili bir kod bloğumuz vardır. Bu durumda `a`'ya bir ekler ve sonucu `b`'ye atarız. `b` değerini döndürür, yani çıktı olarak veririz. Fonksiyonu tanımladıktan sonra onu çağırabiliriz.

Fonksiyon, beşe bir ekler ve altı döndürür. Fonksiyonu tekrar çağırabiliriz; bu sefer sonucu `c` değişkenine atarız. `c` değeri 11'dir.

### 🔄 Fonksiyon Çağrısına İlişkin Basitleştirilmiş Model

Bunu biraz daha ayrıntılı inceleyelim. Bir fonksiyonu çağırdığınızda ne olduğuna dair bir örnek üzerinden gidelim. Bunun, Python'un basitleştirilmiş bir modeli olduğunun ve Python'un perde arkasında tam olarak böyle çalışmadığının unutulmaması gerekir. Fonksiyonu, ona beş girdisini vererek çağırırız.

Beş değerinin fonksiyona aktarılmış gibi düşünülmesi yardımcı olur. Şimdi komut dizileri çalıştırılır. `a`'nın değeri beştir. `b`'ye altı değeri atanır. Sonra `b` değerini döndürürüz. Bu durumda `b`'ye altı atandığı için, fonksiyon altı değeri döndürür. Fonksiyonu tekrar çağırırsak, süreç en baştan başlar. Bu sefer sekiz değerini aktarırız.

Ardından gelen işlemler gerçekleştirilir. Önceki çağrıda olan her şey, bu kez `a` için farklı bir değerle yeniden gerçekleşir. Fonksiyon bir değer döndürür; bu durumda bu değer dokuzdur. Yine, bunun sadece yardımcı bir benzetme olduğunu unutmayın. Şimdi bu fonksiyonu biraz daha karmaşık hale getirmeyi deneyelim.

---

## 📄 Fonksiyonları Belgelemek ve `help` Kullanımı

Geleneksel olarak, fonksiyonu ilk birkaç satırda belgelersiniz. Bu, fonksiyonu kullanan herkese fonksiyonun ne yaptığını söyler. Bu dokümantasyon üç tırnak işaretiyle çevrelenir. Fonksiyon üzerindeki dokümantasyonu göstermek için `help` komutunu aşağıdaki şekilde kullanabilirsiniz. Bu, fonksiyonun adını ve dokümantasyonunu yazdıracaktır. Kalan örneklerde dokümantasyonu dahil etmeyeceğiz.

---

## ✖️ Çoklu Parametreli Bir Fonksiyon: `mult`

Bir fonksiyonun birden fazla parametresi olabilir. *mult* fonksiyonu iki sayıyı çarpar. Başka bir deyişle, bu sayıların çarpımını bulur.

Tamsayı iki ve üçü geçirirsek, sonuç yeni bir tamsayı olur. Tamsayı 10 ve kayan noktalı sayı 3.14'ü geçirirsek, sonuç 31.4 olan bir float olur. Tamsayı iki ve *Michael Jackson* string'ini geçirirsek, *Michael Jackson* string'i iki kez tekrarlanır. Bunun nedeni, çarpma sembolünün aynı zamanda bir diziyi tekrar etmek anlamına da gelebilmesidir. Yanlışlıkla iki tamsayı yerine bir tamsayı ile bir string'i çarparsanız, bir hata almazsınız. Bunun yerine bir string elde edersiniz ve programınız, bir tamsayı beklerken elinizde bir string olduğu için daha sonra başarısız olma potansiyeliyle, çalışmaya devam eder. Bu özellik kod yazmayı basitleştirir, ancak kodunuzu daha kapsamlı bir şekilde test etmeniz gerekir.

---

## ⛔ `return` Olmayan Fonksiyonlar ve `None` Nesnesi

Birçok durumda, bir fonksiyonun `return` ifadesi yoktur. Bu durumlarda Python, özel `None` nesnesini döndürür. Pratik olarak, fonksiyonunuzun `return` ifadesi yoksa, fonksiyon hiçbir şey döndürmüyormuş gibi davranabilirsiniz. *MJ* fonksiyonu yalnızca *Michael Jackson* adını yazdırır. Fonksiyonu çağırırız. Fonksiyon  *Michael Jackson* 'ı yazdırır. Hiçbir görev yerine getirmeyen *no work* adlı fonksiyonu tanımlayalım.

Python, bir fonksiyonun boş bir gövdeye sahip olmasına izin vermez, bu yüzden hiçbir şey yapmayan ama gövdenin boş olmaması gerekliliğini karşılayan `pass` anahtar sözcüğünü kullanabiliriz. Fonksiyonu çağırıp sonucu yazdırırsak, fonksiyon `None` döndürür. Arka planda, `return` ifadesi çağrılmazsa Python otomatik olarak `None` döndürür. *no work* fonksiyonunu aşağıdaki `return` ifadesiyle birlikte düşünmek faydalıdır. Genellikle fonksiyonlar birden fazla görev yerine getirir. Bu fonksiyon bir ifade yazdırır ve sonra bir değer döndürür. Fonksiyon çağrıldıkça farklı değerleri göstermek için bu tabloyu kullanalım.

Fonksiyonu 2 girdisiyle çağırırız. `b` değerini buluruz. Fonksiyon, `a` ve `b` değerini içeren ifadeyi yazdırır. Son olarak fonksiyon, bu durumda 3 olan `b` değerini döndürür.

---

## 🔁 Fonksiyonların İçinde Döngü Kullanmak

Fonksiyonlarda döngüler kullanabiliriz. Bu fonksiyon, bir döngünün veya bir demetin değerlerini ve indekslerini yazdırır. Fonksiyonu, *album ratings* listesini girdi olarak vererek çağırırız.

Sağ tarafta listeyi, ona karşılık gelen indekslerle birlikte gösterelim.  *Stuff* , `enumerate` fonksiyonuna girdi olarak kullanılır. Bu işlem, indeksi `i`'ye ve listedeki değeri `s`'ye aktaracaktır. Fonksiyon döngü boyunca yinelemeye başlayacaktır. Fonksiyon, ilk indeksi ve listedeki ilk değeri yazdıracaktır. Döngü boyunca yinelemeye devam ederiz. `i` ve `s` değerleri güncellenir.

`print` ifadesine ulaşılır. Benzer şekilde, listenin ve indeksin bir sonraki değerleri yazdırılır. Süreç tekrarlanır. `i` ve `s` değerleri güncellenir. Listedeki son değerler yazdırılana kadar yinelemeye devam ederiz.

---

## 🧮 Değişken Sayıda Parametre (Variadic Parameters)

Değişken sayıda parametre (variadic parameters), değişken sayıda öğe girmemize olanak tanır. Aşağıdaki fonksiyonu ele alalım.

Fonksiyonun parametre adlarının üzerinde bir yıldız işareti vardır. Fonksiyonu çağırdığımızda, üç parametre *names* adlı demete paketlenir. Daha sonra döngü boyunca yineleme yaparız. Değerler buna göre yazdırılır. Aynı fonksiyonu giriş olarak yalnızca iki parametreyle çağırırsak, *names* değişkeni yalnızca iki öğe içerir. Sonuç olarak yalnızca iki değer yazdırılır.

---

## 🌍 Değişken Kapsamı (Scope)

Bir değişkenin kapsamı ( *scope* ), o değişkenin programın içinde erişilebilir olduğu kısımdır.

Herhangi bir fonksiyonun dışında tanımlanan değişkenlerin, tanımlandıktan sonra programın her yerinden erişilebildiği anlamına gelen global kapsam içinde olduğu söylenir. Burada, parametre `x`'e *dc* string'ini ekleyen bir fonksiyonumuz var. `x` değerinin *ac* olarak ayarlandığı kısma ulaştığımızda, bu global kapsam içindedir; yani `x`, tanımlandıktan sonra her yerden erişilebilir. Global kapsamda tanımlanan bir değişkene global değişken denir.

Fonksiyonu çağırdığımızda, yeni bir kapsama veya *add dc* fonksiyonunun kapsamına gireriz. *add dc* fonksiyonuna, bu durumda *ac* değerini argüman olarak geçiririz. Fonksiyonun kapsamı içinde `x` değeri *ac dc* olarak ayarlanır.

Fonksiyon değeri döndürür ve bu değer `z`'ye atanır. Global kapsam içinde `z` değeri *ac dc* olarak ayarlanır. Değer döndürüldükten sonra fonksiyonun kapsamı silinir.

### 📦 Yerel Değişkenler

Yerel değişkenler yalnızca bir fonksiyonun kapsamı içinde var olur. *thriller* fonksiyonunu ele alalım. Yerel değişken  *date* , 1982 olarak ayarlanır. Fonksiyonu çağırdığımızda yeni bir kapsam oluştururuz.

Fonksiyonun bu kapsamı içinde *date* değişkeninin değeri 1982 olarak ayarlanır. *date* değerinin global kapsamda bir karşılığı yoktur. Global kapsam içindeki değişkenler, yerel kapsam içindeki değişkenlerle aynı ada sahip olabilir ve bu bir çakışmaya neden olmaz. *thriller* fonksiyonunu tekrar ele alalım. Yerel değişken *date* 1982 olarak ayarlanmıştır. Global değişken *date* ise 2017 olarak ayarlanmıştır. Fonksiyonu çağırdığımızda yeni bir kapsam oluştururuz.

Bu kapsam içinde *date* değerinin 1982 olarak ayarlandığını görürüz. Fonksiyonu çağırırsak, yerel kapsam içindeki *date* değerini döndürür; bu durumda bu değer 1982'dir. Global kapsamda yazdırma işlemi yaptığımızda, global değişkenin değerini kullanırız. Değişkenin global değeri 2017'dir. Bu nedenle değer 2017 olarak ayarlanır. Bir değişken bir fonksiyon içinde tanımlı değilse, Python global kapsamı kontrol edecektir.

### 🔎 Global Değişkeni Fonksiyon İçinde Kullanmak

*ac dc* fonksiyonunu ele alalım. Fonksiyonun içinde, herhangi bir değer atanmamış *rating* adlı bir değişken vardır. *rating* değişkenini global kapsamda tanımlar ve sonra fonksiyonu çağırırsak, Python *rating* değişkeni için bir değer olmadığını görecektir. Bunun sonucunda Python, kapsamdan çıkar ve *rating* değişkeninin global kapsamda olup olmadığını kontrol eder. *ac dc* fonksiyonunun kapsamı içinde, global kapsamda yer alan *rating* değerini kullanır. Fonksiyon içinde 9 yazdırırız. Bir eklediğimiz için, global kapsamda `z` değeri 10 olacaktır.

Global kapsam içinde *rating* değerinin kendisi değişmeden kalacaktır.

### 🧾 `global` Anahtar Sözcüğü ile Global Değişken Oluşturma

*Pink Floyd* fonksiyonunu ele alalım. `global` anahtar sözcüğüyle *claimed sales* değişkenini tanımlarsak, bu değişken global bir değişken olacaktır. *Pink Floyd* fonksiyonunu çağırırız. *claimed sales* değişkeni, global kapsamda *45 million* string'ine ayarlanır. Değişkeni yazdırdığımızda, 45 million değerini elde ederiz. Fonksiyonlarla yapabileceğiniz çok daha fazla şey vardır. Daha fazla örnek için laboratuvar çalışmasına göz atın.
