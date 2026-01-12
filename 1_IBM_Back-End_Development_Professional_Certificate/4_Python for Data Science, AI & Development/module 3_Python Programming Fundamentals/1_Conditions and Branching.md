# 🔀 Koşullar ve Dallanma

## 🔢 Karşılaştırma İşlemleri ve Boolean Değerler

Bu videoda, koşullar ( *conditions* ) ve dallanma ( *branching* ) hakkında bilgi edineceksiniz. Karşılaştırma işlemleri, bazı değerleri veya işlenenleri ( *operand* ) karşılaştırır. Ardından, belirli bir koşula bağlı olarak bir *Boolean* (doğru/yanlış) değer üretirler.

Diyelim ki `a` değişkenine 6 değerini atıyoruz. İki değerin eşit olup olmadığını belirlemek için, iki eşittir işaretiyle gösterilen eşitlik işleçini kullanabiliriz. Bu durumda 7'nin 6'ya eşit olup olmadığını kontrol ederiz. 6, 7'ye eşit olmadığı için sonuç yanlıştır.

Eğer 6 değeri için bir eşitlik testi yapsaydık, iki değer eşit olurdu. Sonuç olarak koşul doğru olurdu. Aşağıdaki eşitlik karşılaştırma işleçini ele alalım:

Sol işlenenin, yani `i` değişkeninin değeri, sağ işlenenin, bu örnekte 5'in değerinden büyükse, koşul doğru olur; aksi hâlde yanlış olur. Solda `i` için bazı değerleri gösterelim. 5’ten büyük değerleri yeşil, geri kalanları kırmızı olarak düşünelim. `i`’yi 6 yaparsak, 6’nın 5’ten büyük olduğunu görürüz ve bunun sonucunda koşul doğru olur.

Aynı işlemleri ondalıklı sayılar ( *float* ’lar) için de uygulayabiliriz. İşleci şu şekilde değiştirirsek: Sol işlenen `i`, sağ işlenenin, bu örnekte 5’in değerinden **büyük veya eşit** ise, koşul doğru olur.

Bu durumda sayı doğrusuna 5 değerini de dahil ederiz ve bu noktaya karşılık gelen renk yeşile döner. `i`’nin değerini 5 yaptığımızda, işlemin sonucu doğru olur. `i` değerini 2 yaptığımızda ise, 2, 5’ten küçük olduğundan sonuç yanlış olur.

Eşitsizliği değiştirebiliriz. Sol işlenenin, yani `i`’nin değeri, sağ işlenenin, bu durumda 6’nın değerinden küçükse, koşul doğru olur. Bunu yine renkli bir sayı doğrusu ile gösterebiliriz.

Eşitsizliğin doğru olduğu bölgeler yeşil, yanlış olduğu bölgeler kırmızı ile işaretlenir. `i` değeri 2 olarak ayarlanırsa, 2, 6’dan küçük olduğu için sonuç doğrudur.

Eşitsizlik testi, eşittir işaretinin önüne gelen bir ünlem işareti kullanır. İki işlenen eşit değilse, koşul doğru olur. Bir sayı doğrusu kullanarak, koşulun doğru olduğu sayıları yeşil, yanlış olduğu sayıları ise kırmızı ile gösterebiliriz.

`i`’yi 2 yaptığımızda, 2, 6’ya eşit olmadığı için bu işlemin sonucu doğrudur.

Dizgeleri ( *string* ’leri) de karşılaştırabiliriz. AC, DC ile Michael Jackson’ı eşitlik testiyle karşılaştırdığımızda, dizgeler aynı olmadığından sonuç yanlıştır. Eşitsizlik testiyle karşılaştırdığımızda ise, dizgeler farklı olduğu için sonuç doğrudur.

Daha fazla örnek için laboratuvarları inceleyin.

Dallanma, farklı girdiler için farklı ifadelerin çalıştırılmasına olanak tanır. Bir `if` deyimini kilitli bir oda gibi düşünmek faydalıdır.

---

## 🚪 `if` Deyimi ve Dallanma Mantığı

Eğer ifade doğruysa, odaya girebilirsiniz ve programınız önceden tanımlanmış bir görevi çalıştırabilir. İfade yanlışsa, programınız bu görevi atlar.

Örneğin, bir AC, DC konserini temsil eden mavi bir dikdörtgeni ele alalım. Kişi 18 yaşında veya daha büyükse AC, DC konserine girebilir. 18 yaşın altındaysa konsere giremez. Birey konsere doğru ilerler. Yaşı 17’dir.

Bu nedenle konsere giriş izni verilmez ve devam etmek zorundadır. Eğer kişi 19 yaşındaysa, koşul doğrudur. Konsere girebilir ve ardından yoluna devam edebilir.

Bu, önceki örneğimizdeki `if` deyiminin sözdizimidir. Bir `if` deyimimiz vardır. Doğru veya yanlış olabilen bir ifademiz vardır. Köşeli parantezler gerekli değildir.

Bir iki nokta üst üste bulunur. Girintili blok içinde, koşul doğruysa çalıştırılan ifade yer alır. `if` deyiminden sonra gelen ifadeler ise, koşulun doğru ya da yanlış olmasından bağımsız olarak çalışacaktır.

Yaşın 17 olduğu durumda, `age` değişkeninin değerini 17 olarak ayarlarız. `if` deyimini kontrol ederiz. İfade yanlıştır. Bu nedenle program, `İçeri gireceksin.` ifadesini yazdıran deyimi çalıştırmaz. Bu durumda yalnızca `Devam et.` ifadesini yazdırır.

Yaşın 19 olduğu durumda, `age` değişkeninin değerini 19 yaparız. `if` deyimini kontrol ederiz. İfade doğrudur. Bu nedenle program, `İçeri gireceksin.` ifadesini yazdıran deyimi çalıştırır. Ardından sadece `Devam et.` ifadesini yazdırır.

---

## 🔁 `else` Deyimi: Alternatif Yol

`else` deyimi, aynı koşul yanlış olduğunda farklı bir kod bloğunun çalıştırılmasını sağlar. ACDC konseri benzetmesini tekrar kullanalım.

Kullanıcı 17 yaşındaysa ACDC konserine gidemez. Ancak mor kareyle temsil edilen meatloaf konserine gidebilir. Kişi 19 yaşındaysa, koşul doğrudur. ACDC konserine girebilirler. Sonra, önceki gibi yollarına devam edebilirler.

`else` deyiminin sözdizimi benzerdir. Basitçe `else` deyimini ekleriz. Ardından, girintili bir şekilde, çalıştırılmasını istediğimiz ifadeyi yazarız.

Yaşın 17 olduğu durumda, `age` değişkeninin değerini 17 olarak ayarlarız. `if` deyimini kontrol ederiz. İfade yanlıştır. Bu nedenle `else` deyimine geçeriz. Girintili blok içindeki ifadeyi çalıştırırız.

Bu, kişinin meatloaf konserine gitmesine karşılık gelir. Program daha sonra çalışmaya devam eder.

Yaşın 19 olduğu durumda, `age` değişkeninin değerini 19 olarak ayarlarız. `if` deyimini kontrol ederiz. İfade doğrudur. Bu nedenle program, `İçeri gireceksin.` ifadesini yazdıran deyimi çalıştırır. Program, `else` deyimindeki ifadeleri atlar ve geri kalan ifadeleri çalıştırmaya devam eder.

---

## 🔀 `elif` Deyimi: Ek Koşullar

`elif` deyimi, *else if* ifadesinin kısaltmasıdır ve ek koşulları kontrol etmemizi sağlar. Önceki koşul yanlışsa bu koşul değerlendirilir; koşul doğruysa, alternatif ifadeler çalıştırılır.

Konser örneğini tekrar ele alalım. Kişi 18 yaşındaysa, ACDC veya meatloaf konserlerine gitmek yerine Pink Floyd konserine gidecektir.

18 yaşındaki kişi, 19 yaşından büyük olmadığı için alana girer. ACDC’yi göremez. Ancak 18 yaşında olduğundan Pink Floyd’u izler. Pink Floyd’u gördükten sonra yoluna devam eder.

`elif` deyiminin sözdizimi benzerdir. Basitçe koşulla birlikte `elif` deyimini ekleriz. Ardından, ifade doğruysa çalıştırılmasını istediğimiz ifadeyi girintili olarak yazarız.

Soldaki kodu örnek olarak düşünelim. 18 yaşında biri içeri girer. 18 yaşından büyük değildir. Bu nedenle ilk koşul yanlıştır. Böylece `elif` deyimindeki koşul kontrol edilir.

Bu koşul doğrudur. Bu durumda `Pink Floyd’u görmeye git.` ifadesini yazdırırız. Ardından, önceki gibi devam ederiz.

`age` değişkeni 17 olsaydı, `Meatloaf’u görmeye git.` ifadesi yazdırılırdı. Benzer şekilde, yaş 18’den büyük olsaydı, `İçeri girebilirsin.` ifadesi yazdırılırdı.

Daha fazla örnek için laboratuvarları inceleyin.

---

## 🧠 Mantıksal Operatörler: `not`, `or`, `and`

Şimdi de mantıksal ( *logic* ) operatörlere bakalım. Mantıksal işlemler, *Boolean* değerleri alır ve yine *Boolean* değerler üretir.

### 🚫 `not` Operatörü

İlk işlem `not` işleçidir. Girdi doğruysa sonuç yanlıştır. Benzer şekilde, girdi yanlışsa sonuç doğru olur.

### ⚖️ `or` Operatörü

A ve B’nin *Boolean* değişkenleri temsil ettiğini varsayalım. `or` işleci, bu iki değeri alır ve yeni bir *Boolean* değer üretir. Farklı değerleri göstermek için bir tablo kullanabiliriz.

Birinci sütun A’nın mümkün değerlerini gösterir. İkinci sütun B’nin mümkün değerlerini gösterir. Son sütun ise `or` işleminin uygulanmasıyla elde edilen sonucu gösterir.

`or` işleçinin, yalnızca tüm *Boolean* değerleri yanlışsa yanlış ürettiğini görürüz.

Aşağıdaki kod satırları bir çıktı verecektir. *album year* değişkeni 80’lere denk gelmiyorsa, `Bu albüm 70’lerde ya da 90’larda yapıldı.` ifadesi yazdırılır.

Şimdi *album year* değerini 1990 yaptığımızda ne olduğuna bakalım. Koşul doğru olduğunda, renkli sayı doğrusunda ilgili kısım yeşil; koşul yanlış olduğunda ise kırmızı ile gösterilir.

Bu durumda ilk koşul yanlıştır. İkinci koşulu incelediğimizde, 1990’ın 1989’dan büyük olduğunu görürüz. Dolayısıyla ikinci koşul doğrudur.

Bunu, karşılık gelen ikinci sayı doğrusunu inceleyerek doğrulayabiliriz. Son sayı doğrusunda yeşil bölge, ifadenin doğru olduğu alanı gösterir. Bu bölge, en az bir ifadenin doğru olduğu yerleri temsil eder.

1990’ın bu alana düştüğünü görürüz. Bu nedenle ifade çalıştırılır.

### 🔗 `and` Operatörü

Yine A ve B’nin *Boolean* değişkenleri temsil ettiğini varsayalım. `and` işleci, bu iki değeri alır ve yeni bir *Boolean* değer üretir. Farklı değerleri göstermek için bir tablo kullanabiliriz.

Birinci sütun A’nın mümkün değerlerini, ikinci sütun B’nin mümkün değerlerini, son sütun ise `and` işleminin sonucu gösterir.

`and` işleçinin, yalnızca tüm *Boolean* değerleri doğru olduğunda doğru ürettiğini görürüz.

Aşağıdaki kod satırları bir çıktı verecektir: *album year* değişkeni 1980 ile 1989 arasındaysa, `Bu albüm 80’lerde yapıldı.` ifadesi yazdırılır.

Şimdi *album year* değerini 1983 yaptığımızda ne olduğuna bakalım. Daha önce olduğu gibi, koşulun nerede doğru olduğunu incelemek için renkli bir sayı doğrusu kullanabiliriz.

Bu durumda 1983, 1980’den büyüktür. Dolayısıyla ilk koşul doğrudur. İkinci koşulu incelediğimizde, 1990’ın 1983’ten büyük olduğunu görürüz. Bu nedenle ikinci koşul da doğrudur.

Bunu, karşılık gelen ikinci sayı doğrusunu inceleyerek doğrulayabiliriz. Son sayı doğrusunda yeşil bölge, ifadenin doğru olduğu alanı gösterir. Benzer şekilde, bu bölge her iki ifadenin de doğru olduğu yerleri temsil eder.

1983’ün bu alana düştüğünü görürüz. Bu nedenle ifade çalıştırılır.

---

Dallanma, farklı girdiler için farklı ifadelerin çalıştırılmasına imkân tanır.
