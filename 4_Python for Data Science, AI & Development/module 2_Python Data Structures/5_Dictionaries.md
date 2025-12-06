# 📚 Sözlükler (Dictionaries)

## 🧾 Python'da sözlüklere giriş

Python'da sözlükleri ele alalım. Sözlükler, Python'da bir tür koleksiyondur. Hatırlarsanız, bir `list` tamsayı indekslere sahiptir. Bunlar adresler gibidir. Bir `list` aynı zamanda öğelere sahiptir. Bir sözlük ise *anahtarlar* (`keys`) ve *değerler* (`values`) içerir.

Anahtar, indekse benzer bir kavrama sahiptir.

## 🔑 Anahtarlar ve adres benzetmesi

Bunlar adresler gibidir, ancak tamsayı olmak zorunda değillerdir. Genellikle karakterlerden oluşurlar. Değerler, bir listedeki öğelere benzer ve bilgi içerir.

Bir sözlük oluşturmak için süslü parantezler `{}` kullanırız. Anahtarlar ilk öğelerdir. Değiştirilemez ( *immutable* ) ve benzersiz olmaları gerekir. Her anahtarı, iki nokta üst üste `:` ile ayrılmış bir değer izler.

## 🧱 Değerler ve tabloyla görselleştirme

Değerler değiştirilemez ( *immutable* ), değiştirilebilir ( *mutable* ) olabilir ve tekrar edebilir. Her anahtar ve değer çifti virgül ile ayrılır.

Bir sözlük örneğini düşünelim. Albüm başlığı anahtardır ve değer, çıkış tarihidir. Anahtarları vurgulamak için sarı rengi kullanabilir ve değerleri beyaz bırakabiliriz.

Bir tablonun, bir sözlüğü görselleştirmede yardımcı olduğunu söyleyebiliriz; burada ilk sütun anahtarları, ikinci sütun ise değerleri temsil eder. Sözlüğe birkaç örnek daha ekleyebiliriz.

## 🔍 Sözlüğü değişkene atamak ve değer aramak

Sözlüğü bir değişkene de atayabiliriz. Anahtar, değeri aramak için kullanılır. Köşeli parantez `[]` kullanırız. Argüman, anahtar olur. Bu işlem, değeri çıktılar.

`back in black` anahtarını kullandığımızda, bu bize `1980` değerini döndürür. `the dark side of the moon` anahtarı bize `1973` değerini verir.

## ➕➖ Girdi ekleme, silme ve `in` komutu

`the bodyguard` anahtarını kullanmak bize `1992` değerini verir ve bu şekilde devam eder. Sözlüğe yeni bir girdi şu şekilde eklenebilir. Bu, `graduation` adlı yeni bir anahtarla `2007` değerini ekler.

Bir girdiyi şu şekilde silebiliriz. Bu, `thriller` anahtarını ve onun değerini ortadan kaldırır.

Bir öğenin sözlükte olup olmadığını `in` komutunu kullanarak şu şekilde doğrulayabiliriz. Komut, anahtarları kontrol eder.

## 🗝️ `keys` ve `values` metotları

Eğer sözlükteyseler, `True` dönerler. Aynı komutu sözlükte olmayan bir anahtarla denersek, `False` elde ederiz.

Bir sözlükteki tüm anahtarları görmek için `keys` metodunu kullanarak anahtarları alabiliriz. Çıktı, tüm anahtarları içeren liste benzeri bir nesnedir.

Benzer şekilde, `values` metodunu kullanarak değerleri elde edebiliriz. Sözlükler hakkında daha fazla örnek ve bilgi için laboratuvar çalışmalarına göz atın.

---

## ▶️ Video oynatma ve transkript işaretleri

Python'da sözlükleri ele alalım. Sözlükler, Python'da bir tür koleksiyondur. Hatırlarsanız, bir `list` tamsayı indekslere sahiptir. Bunlar adresler gibidir. Bir `list` aynı zamanda öğelere sahiptir. Bir sözlük ise anahtarlar (`keys`) ve değerler (`values`) içerir. Anahtar, indekse benzer bir kavrama sahiptir.

Videoyu ::17 zamanından oynatın ve transkripti takip edin0:17

Bunlar adresler gibidir, ancak tamsayı olmak zorunda değillerdir. Genellikle karakterlerden oluşurlar. Değerler, bir listedeki öğelere benzer ve bilgi içerir. Bir sözlük oluşturmak için süslü parantezler `{}` kullanırız. Anahtarlar ilk öğelerdir. Değiştirilemez ( *immutable* ) ve benzersiz olmaları gerekir. Her anahtarı, iki nokta üst üste `:` ile ayrılmış bir değer izler.

Videoyu ::37 zamanından oynatın ve transkripti takip edin0:37

Değerler değiştirilemez ( *immutable* ), değiştirilebilir ( *mutable* ) olabilir ve tekrar edebilir. Her anahtar ve değer çifti virgül ile ayrılır. Bir sözlük örneğini düşünelim. Albüm başlığı anahtardır ve değer, çıkış tarihidir. Anahtarları vurgulamak için sarı rengi kullanabilir ve değerleri beyaz bırakabiliriz. Bir tablonun, bir sözlüğü görselleştirmede yardımcı olduğunu söyleyebiliriz; burada ilk sütun anahtarları, ikinci sütun ise değerleri temsil eder. Sözlüğe birkaç örnek daha ekleyebiliriz.

Videoyu :1:7 zamanından oynatın ve transkripti takip edin1:07

Sözlüğü bir değişkene de atayabiliriz. Anahtar, değeri aramak için kullanılır. Köşeli parantez `[]` kullanırız. Argüman, anahtar olur. Bu işlem, değeri çıktılar. `back in black` anahtarını kullandığımızda, bu bize `1980` değerini döndürür. `the dark side of the moon` anahtarı bize `1973` değerini verir.

Videoyu :1:29 zamanından oynatın ve transkripti takip edin1:29

`the bodyguard` anahtarını kullanmak bize `1992` değerini verir ve bu şekilde devam eder. Sözlüğe yeni bir girdi şu şekilde eklenebilir. Bu, `graduation` adlı yeni bir anahtarla `2007` değerini ekler. Bir girdiyi şu şekilde silebiliriz. Bu, `thriller` anahtarını ve onun değerini ortadan kaldırır. Bir öğenin sözlükte olup olmadığını `in` komutunu kullanarak şu şekilde doğrulayabiliriz. Komut, anahtarları kontrol eder.

Videoyu :1:55 zamanından oynatın ve transkripti takip edin1:55

Eğer sözlükteyseler, `True` dönerler. Aynı komutu sözlükte olmayan bir anahtarla denersek, `False` elde ederiz. Bir sözlükteki tüm anahtarları görmek için `keys` metodunu kullanarak anahtarları alabiliriz. Çıktı, tüm anahtarları içeren liste benzeri bir nesnedir. Benzer şekilde, `values` metodunu kullanarak değerleri elde edebiliriz. Sözlükler hakkında daha fazla örnek ve bilgi için laboratuvar çalışmalarına göz atın.

Python'da sözlükleri ele alalım. Sözlükler, Python'da bir tür koleksiyondur. Hatırlarsanız, bir `list` tamsayı indekslere sahiptir. Bunlar adresler gibidir. Bir `list` aynı zamanda öğelere sahiptir. Bir sözlük ise anahtarlar ve değerler içerir. Anahtar, indekse benzer bir kavrama sahiptir.

Videoyu ::17 zamanından oynatın ve transkripti takip edin0:17

Bunlar adresler gibidir, ancak tamsayı olmak zorunda değillerdir. Genellikle karakterlerden oluşurlar. Değerler, bir listedeki öğelere benzer ve bilgi içerir. Bir sözlük oluşturmak için süslü parantezler `{}` kullanırız. Anahtarlar ilk öğelerdir. Değiştirilemez ve benzersiz olmaları gerekir. Her anahtarı, iki nokta üst üste `:` ile ayrılmış bir değer izler.

Videoyu ::37 zamanından oynatın ve transkripti takip edin0:37

Değerler değiştirilemez, değiştirilebilir olabilir ve tekrar edebilir. Her anahtar ve değer çifti virgül ile ayrılır. Bir sözlük örneğini düşünelim. Albüm başlığı anahtardır ve değer, çıkış tarihidir. Anahtarları vurgulamak için sarı rengi kullanabilir ve değerleri beyaz bırakabiliriz. Bir tablonun, bir sözlüğü görselleştirmede yardımcı olduğunu söyleyebiliriz; burada ilk sütun anahtarları, ikinci sütun ise değerleri temsil eder. Sözlüğe birkaç örnek daha ekleyebiliriz.

Videoyu :1:7 zamanından oynatın ve transkripti takip edin1:07

Sözlüğü bir değişkene de atayabiliriz. Anahtar, değeri aramak için kullanılır. Köşeli parantez `[]` kullanırız. Argüman, anahtar olur. Bu işlem, değeri çıktılar. `back in black` anahtarını kullandığımızda, bu bize `1980` değerini döndürür. `the dark side of the moon` anahtarı bize `1973` değerini verir.

Videoyu :1:29 zamanından oynatın ve transkripti takip edin1:29

`the bodyguard` anahtarını kullanmak bize `1992` değerini verir ve bu şekilde devam eder. Sözlüğe yeni bir girdi şu şekilde eklenebilir. Bu, `graduation` adlı yeni bir anahtarla `2007` değerini ekler. Bir girdiyi şu şekilde silebiliriz. Bu, `thriller` anahtarını ve onun değerini ortadan kaldırır. Bir öğenin sözlükte olup olmadığını `in` komutunu kullanarak şu şekilde doğrulayabiliriz. Komut, anahtarları kontrol eder.

Videoyu :1:55 zamanından oynatın ve transkripti takip edin1:55

Eğer sözlükteyseler, `True` dönerler. Aynı komutu sözlükte olmayan bir anahtarla denersek, `False` elde ederiz. Bir sözlükteki tüm anahtarları görmek için `keys` metodunu kullanarak anahtarları alabiliriz. Çıktı, tüm anahtarları içeren liste benzeri bir nesnedir. Benzer şekilde, `values` metodunu kullanarak değerleri elde edebiliriz. Sözlükler hakkında daha fazla örnek ve bilgi için laboratuvar çalışmalarına göz atın.

Python'da sözlükleri ele alalım. Sözlükler, Python'da bir tür koleksiyondur. Hatırlarsanız, bir `list` tamsayı indekslere sahiptir. Bunlar adresler gibidir. Bir `list` aynı zamanda öğelere sahiptir. Bir sözlük ise anahtarlar ve değerler içerir. Anahtar, indekse benzer bir kavrama sahiptir.

Videoyu ::17 zamanından oynatın ve transkripti takip edin0:17

Bunlar adresler gibidir, ancak tamsayı olmak zorunda değillerdir. Genellikle karakterlerden oluşurlar. Değerler, bir listedeki öğelere benzer ve bilgi içerir. Bir sözlük oluşturmak için süslü parantezler `{}` kullanırız.

Anahtarlar: Seçime eklendi. Not olarak kaydetmek için [CTRL + S] tuşlayın Beğen Beğenme Sorun bildir : Seçime eklendi. Not olarak kaydetmek için [CTRL + S] tuşlayın Beğen Beğenme Sorun bildir : Seçime eklendi. Not olarak kaydetmek için [CTRL + S] tuşlayın.
