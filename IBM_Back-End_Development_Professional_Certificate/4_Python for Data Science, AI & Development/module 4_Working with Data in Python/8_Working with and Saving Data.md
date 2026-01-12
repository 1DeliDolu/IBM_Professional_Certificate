# 💾 Verilerle Çalışmak ve Verileri Kaydetmek

## 🎨 Benzersiz Öğeleri Bulma

Bir  *data frame* 'imiz olduğunda verilerle çalışabilir ve sonuçları başka formatlarda kaydedebiliriz.

Farklı renklerden oluşan 13 blokluk bir yığını düşünün. Üç benzersiz renk olduğunu görebiliriz.

Diyelim ki bir  *data frame* 'deki bir sütunda kaç tane benzersiz öğe olduğunu bulmak istiyorsunuz. Bu çok daha zor olabilir, çünkü 13 öğe yerine milyonlarca öğeniz olabilir.

 *Pandas* , bir *data frame* sütunundaki benzersiz öğeleri belirlemek için `unique` adlı bir metoda sahiptir. Diyelim ki veri setindeki albümlerin benzersiz yıllarını belirlemek istiyoruz.

## 🎯 1980 Sonrası Şarkıları Seçme

 *Data frame* 'in adını yazarız, ardından köşeli parantez içinde `Released` sütununun adını gireriz. Sonra `unique` metodunu uygularız.

Sonuç, `Released` sütunundaki tüm benzersiz öğelerdir.

Diyelim ki 1980'lerden ve sonrasından şarkılardan oluşan yeni bir veri tabanı oluşturmak istiyoruz. `Released` sütununa bakarak 1979'dan sonra yapılmış şarkıları bulabilir, ardından ilgili satırları seçebiliriz.

Bunu *Pandas* ile tek satırlık bir kod içinde başarabiliriz. Ama gelin adımlara bölelim.

## ⚙️ Eşitsizlik Operatörleri ve Boolean Filtreleme

 *Pandas* 'ta tüm *data frame* için eşitsizlik ( *inequality* ) operatörlerini kullanabiliriz. Sonuç, Boolean değerlerden oluşan bir seri olur.

Bizim durumumuzda, yalnızca `Released` sütununu ve 1979'dan sonra çıkan albümler için eşitsizlik ifadesini belirtiriz. Sonuç, Boolean değerlerden oluşan bir seri olur.

Koşul sağlandığında sonuç `True`, aksi halde `False` olur.

Belirtilen sütunları tek satırda seçebiliriz. Basitçe  *data frame* 'in adını ve köşeli parantezler içine az önce yazdığımız eşitsizlik ifadesini yazarız ve bunu `df1` değişkenine atarız.

## 💽 Yeni Data Frame'i Kaydetme

Artık her albümün 1979'dan sonra yayımlandığı yeni bir  *data frame* 'imiz var.

Bu yeni  *data frame* 'i `to_csv` metodu ile kaydedebiliriz. Argüman, csv dosyasının adıdır.

`.csv` uzantısını eklediğinizden emin olun.

 *Data frame* 'i başka formatlarda kaydetmek için başka fonksiyonlar da vardır.
