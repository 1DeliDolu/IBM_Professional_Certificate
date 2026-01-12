# 🧩 Kümeler

## 📚 Kümelere Giriş

Kümeleri ele alalım. Onlar da bir tür  *collection* 'dır. Kümeler bir *collection* türüdür. Bu, listeler ve tuple'lar gibi farklı Python türlerini girdi olarak kullanabileceğiniz anlamına gelir.

Listeler ve tuple'lardan farklı olarak, sırasızdırlar. Bu, kümelerin elemanların konumunu kaydetmediği anlamına gelir. Kümelerde yalnızca benzersiz elemanlar bulunur. Bu, bir kümede belirli bir elemandan yalnızca bir tane olduğu anlamına gelir.

---

## 🧱 Küme Tanımlama ve Listeyi Küme Yapma

Bir küme tanımlamak için süslü parantezler kullanırsınız. Bir kümenin elemanlarını süslü parantezlerin içine yerleştirirsiniz. Yinelenen öğeler olduğunu fark edersiniz.

Gerçek küme oluşturulduğunda, yinelenen öğeler mevcut olmayacaktır. Bir listeyi `set` fonksiyonunu kullanarak bir kümeye dönüştürebilirsiniz. Buna *typecasting* denir. Basitçe listeyi `set` fonksiyonuna girdi olarak kullanırsınız. Sonuç, kümeye dönüştürülmüş bir liste olacaktır.

---

## 💡 Örnek: Listeden Küme Oluşturma

Bir örnek üzerinden gidelim. Bir listeyle başlarız. Listeyi `set` fonksiyonuna girdi olarak veririz. `set` fonksiyonu bir küme döndürür.

Dikkat ederseniz, yinelenen hiçbir eleman yoktur. Küme işlemlerini ele alalım. Bunlar kümeyi değiştirmek için kullanılabilir.

---

## 🔴 Küme `A` ve `add` / `remove` Metodları

`A` kümesini ele alalım. Bu kümeyi bir daire ile temsil edelim. Kümelere aşinaysanız, bu bir Venn diyagramının parçası olabilir. Bir Venn diyagramı, genellikle kümeleri temsil etmek için şekiller kullanan bir araçtır.

Bir kümeye bir öğe eklemek için `add` metodunu kullanabiliriz. Sadece kümenin adını yazıp sonuna bir nokta koyar, ardından `add` metodunu yazarız. Argüman, kümeye eklemek istediğimiz yeni elemandır; bu durumda `inSync`.

Artık küme `A`, `inSync` öğesine sahiptir. Aynı öğeyi iki kez eklersek, bir kümede yinelenen eleman olamayacağı için hiçbir şey olmayacaktır.

Diyelim ki `inSync` öğesini küme `A`dan kaldırmak istiyoruz. Bir öğeyi bir kümeden kaldırmak için de `remove` metodunu kullanabiliriz. Yine kümenin adını yazıp sonuna bir nokta koyar, ardından `remove` metodunu yazarız. Argüman, kümeden kaldırmak istediğimiz elemandır; bu durumda `inSync`.

`remove` metodu kümeye uygulandıktan sonra, küme `A` `inSync` öğesini içermez.

---

## 🔍 `in` Komutuyla Üyelik Kontrolü

Bu metodu kümedeki herhangi bir öğe için kullanabilirsiniz.

Bir elemanın kümede olup olmadığını `in` komutunu kullanarak şu şekilde doğrulayabiliriz. Komut, bu durumda `ACDC` olan öğenin kümede olup olmadığını kontrol eder. Eğer öğe kümede ise `true` döndürür.

Kümede olmayan bir öğeyi ararsak, bu durumda `Who` öğesini, öğe kümede olmadığından `false` elde ederiz. Bunlar, matematiksel küme işlemlerinin türleridir. Yapabileceğimiz başka işlemler de vardır.

---

## ♾️ Kümeler Arası Matematiksel İşlemler

Kümeler arasında yapabileceğimiz pek çok yararlı matematiksel işlem vardır. `AlbumSet1` kümesini tanımlayalım. Bunu kırmızı bir daire ya da bir Venn diyagramı kullanarak temsil edebiliriz.

Benzer şekilde `AlbumSet2` kümesini de tanımlayabiliriz. Bunu da mavi bir daire ya da bir Venn diyagramı kullanarak temsil edebiliriz.

İki kümenin kesişimi, her iki kümede de bulunan elemanları içeren yeni bir kümedir. Venn diyagramlarını kullanmak faydalıdır.

Kümeleri temsil eden iki daire birleşir. Örtüşen bölge yeni kümeyi temsil eder. Örtüşen bölge kırmızı daire ve mavi daireden oluştuğundan, kesişimi AND açısından tanımlarız.

Python'da iki kümenin kesişimini bulmak için *ampersand* kullanırız. Kümenin değerlerini dairelerin üzerine bindirip ortak elemanları örtüşen alana yerleştirirsek, bu karşılığı görürüz.

Kesişim işlemini uyguladıktan sonra, her iki kümede de bulunmayan tüm öğeler ortadan kaybolur. Python'da, yalnızca iki kümenin arasına ampersand koyarız.

Her iki kümede de hem `ACDC` hem de `BackInBlack` olduğunu görürüz. Sonuç, `AlbumSet1` ve `AlbumSet2` kümelerinin her ikisindeki tüm elemanları içeren yeni bir küme `AlbumSet3` olur.

İki kümenin birleşimi, her iki kümedeki tüm öğeleri içeren yeni elemanlar kümesidir. `AlbumSet1` ve `AlbumSet2` kümelerinin birleşimini şu şekilde bulabiliriz. Sonuç, `AlbumSet1` ve `AlbumSet2` kümelerinin tüm elemanlarına sahip yeni bir kümedir.

Bu yeni küme yeşil olarak temsil edilir. Yeni albüm `SetAlbumSet3`ü ele alalım.

Küme, `ACDC` ve `BackInBlack` elemanlarını içerir. `AlbumSet3`teki tüm elemanlar `AlbumSet1`de bulunduğundan, bunu bir Venn diyagramı ile temsil edebiliriz.

`AlbumSet1`i temsil eden daire, `AlbumSet3`ü temsil eden daireyi kapsar. Bir kümenin alt küme olup olmadığını `isSubset` metodunu kullanarak kontrol edebiliriz.

`AlbumSet3`, `AlbumSet1`in bir alt kümesi olduğundan sonuç `true` olur. Kümelerle yapabileceğiniz daha pek çok şey vardır. Daha fazla örnek için laboratuvara göz atın.
