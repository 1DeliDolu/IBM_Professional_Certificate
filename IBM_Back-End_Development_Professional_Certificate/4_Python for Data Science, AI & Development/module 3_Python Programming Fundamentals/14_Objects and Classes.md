# 🧱 Nesneler ve Sınıflar

## 🔢 Python’daki Veri Tipleri ve Nesne Kavramı

Bu modülde nesneler ( *objects* ) ve sınıflardan ( *classes* ) bahsedeceğiz.

Python'da tamsayılar ( *integers* ), kayan noktalı sayılar ( *floats* ), dizgeler ( *strings* ), listeler ( *lists* ), sözlükler ( *dictionaries* ), Boole değerleri ( *Booleans* ) gibi birçok farklı veri tipi vardır.

Python'da bunların her biri bir nesnedir ( *object* ).

Her nesnenin şu özellikleri vardır: bir tür ( *type* ), içsel bir gösterim ve veriyle etkileşim kurmak için kullanılan, metotlar ( *methods* ) adı verilen bir dizi fonksiyon.

Bir nesne, belirli bir türün örneğidir ( *instance* ).

Örneğin, elimizde Type 1 ve Type 2 olmak üzere iki tür olsun. Sarı renkle gösterildiği gibi Type 1 türünden birkaç nesneye sahip olabiliriz.

Her nesne, Type 1 türünün bir örneğidir.

Ayrıca yeşil renkle gösterilen birkaç Type 2 nesnemiz de vardır. Her nesne, Type 2 türünün bir örneğidir.

Şimdi daha az soyut birkaç örnek yapalım.

Her tamsayı oluşturduğumuzda, *integer* türünün bir örneğini, yani bir tamsayı nesnesi oluşturmuş oluruz. Bu durumda, *integer* türünden beş örnek, yani beş tamsayı nesnesi oluşturuyoruz.

Benzer şekilde, her liste oluşturduğumuzda, *list* türünün bir örneğini, yani bir liste nesnesini oluşturmuş oluruz. Bu durumda, *list* türünden beş örnek, yani beş liste nesnesi oluşturuyoruz.

---

## 🔍 `type` Komutu ile Nesnenin Türünü Öğrenmek

Bir nesnenin türünü, `type` komutunu kullanarak öğrenebiliriz.

Bu örnekte, *list* türünden bir nesnemiz var. *integer* türünden bir nesnemiz var. *string* türünden bir nesnemiz var. Son olarak, *dictionary* türünden bir nesnemiz var.

---

## 🧩 Metotlar ve Nesnelerle Etkileşim

Bir sınıfın ( *class* ) ya da türün metotları, o sınıfın ya da türün her örneğinin sağladığı fonksiyonlardır.

Nesneyle bu metotlar aracılığıyla etkileşime girersiniz.

Şu ana kadar listeler üzerinde olduğu gibi metotları zaten kullanıyorduk.

Sıralama işlemi ( *sorting* ), nesnenin içindeki verilerle etkileşime giren bir metoda örnektir.

*ratings* adlı listeyi ele alalım.

Veriler, listenin içinde yer alan sayı dizisidir. `sort` metodu, nesnenin içindeki veriyi değiştirir.

Metodu, nesnenin adının sonuna bir nokta koyup ardından çağırmak istediğimiz metodun adını ve parantezleri yazarak çağırırız.

Turuncu renkle gösterilmiş *ratings* listemiz var. Listede yer alan veri, bir sayı dizisidir.

`sort` metodunu çağırırız. Bu, nesnenin içindeki veriyi değiştirir.

Nesnenin durumunu ( *state* ) değiştirdiğini söyleyebilirsiniz.

Liste üzerinde `reverse` metodunu çağırarak listeyi tekrar değiştirebiliriz.

Metodu çağırdığımızda, nesnenin içindeki dizinin sırasını tersine çevirmiş oluruz.

Çoğu durumda, bir sınıfın ve metotlarının iç işleyişini bilmenize gerek yoktur; yalnızca onları nasıl kullanacağınızı bilmeniz yeterlidir.

---

## 🛠️ Kendi Sınıflarımızı Oluşturmak

Şimdi kendi sınıflarınızı nasıl oluşturacağınızı ele alacağız.

Python'da kendi türünüzü ya da sınıfınızı oluşturabilirsiniz.

Bu bölümde bir sınıf oluşturacaksınız.

Sınıfın veri öznitelikleri ( *data attributes* ) vardır. Sınıfın metotları vardır.

Daha sonra o sınıftan örnekler, yani nesneler oluştururuz.

Sınıfın veri öznitelikleri, sınıfı tanımlar.

---

## ⚪ `circle` ve 🟦 `rectangle` Sınıflarının Tasarımı

İki sınıf oluşturalım.

İlk sınıf bir *circle* olacak. İkinci sınıf ise bir *rectangle* olacak.

Bir daireyi ( *circle* ) neyin oluşturduğunu düşünelim.

Bu görsele baktığımızda, bir daireyi tanımlamak için ihtiyacımız olan tek şeyin yarıçap ( *radius* ) olduğunu görürüz ve daha sonra sınıfın farklı örneklerini ayırt etmeyi kolaylaştırmak için bir de renk ekleyelim.

Dolayısıyla sınıfımızın veri öznitelikleri *radius* ve *color* olacaktır.

Benzer şekilde, bir dikdörtgeni ( *rectangle* ) tanımlamak için bu görsele baktığımızda, yüksekliğe ( *height* ) ve genişliğe ( *width* ) ihtiyaç duyduğumuzu görürüz.

Daha sonra örnekleri ayırt etmek için yine bir de renk ekleyeceğiz.

Bu nedenle veri öznitelikleri  *color* , *height* ve *width* olacaktır.

---

## 🧱 Sınıf Tanımı ve `object` Üst Sınıfı

`circle` sınıfını oluşturmak için, sınıf tanımını ( *class definition* ) yazmanız gerekir.

Bu, Python’a kendi sınıfınızı oluşturduğunuzu ve sınıfın adını bildirir.

Bu derste, parantez içinde her zaman `object` terimini koyacaksınız.

Bu, sınıfın ebeveynidir ( *parent* ).

`rectangle` sınıfı için sınıfın adını değiştiririz, ancak geri kalan her şey aynı kalır.

Sınıflar birer taslaktır; nesneleri oluşturmak için öznitelikleri ayarlmamız gerekir.

---

## 🧱 `circle` ve `rectangle` İçin Nesne Örnekleri

*circle* türünden bir örnek olan bir nesne oluşturabiliriz.

Bu nesnede *color* veri özniteliği  *red* , *radius* veri özniteliği ise *four* olacaktır.

*circle* türünden ikinci bir nesne de oluşturabiliriz.

Bu durumda *color* veri özniteliği *green* ve *radius* veri özniteliği *two* olacaktır.

Ayrıca *rectangle* türünden bir nesne de oluşturabiliriz.

Bu nesnede *color* veri özniteliği *blue* ve *height* ile *width* veri öznitelikleri *two* olacaktır.

İkinci nesne de *rectangle* türünden bir örnektir.

Bu durumda *color* veri özniteliği  *yellow* , *height* değeri *one* ve *width* değeri *three* olacaktır.

Artık `circle` sınıfından ya da *circle* türünden farklı nesnelerimiz var.

Ayrıca `rectangle` sınıfından ya da *rectangle* türünden farklı nesnelerimiz de var.

---

## ⚙️ `__init__` Kurucusu ve Veri Özniteliklerini Başlatma

Python’da `circle` sınıfını oluşturmaya devam edelim.

Önce sınıfımızı tanımlarız.

Daha sonra sınıfın her örneğini, sınıf kurucusunu ( *class constructor* ) kullanarak *radius* ve *color* veri öznitelikleriyle ilklendiririz.

`__init__` fonksiyonu bir kurucudur ( *constructor* ).

Bu, Python’a yeni bir sınıf oluşturduğunuzu söyleyen özel bir fonksiyondur.

Daha karmaşık sınıflar oluşturmak için Python’da başka özel fonksiyonlar da vardır.

*radius* ve *color* parametreleri, sınıf örneğinin *radius* ve *color* veri özniteliklerini ilklendirmek için kullanılır.

`self` parametresi, sınıfın yeni oluşturulmuş örneğine karşılık gelir.

*radius* ve *color* parametreleri, sınıf oluşturulurken sınıf kurucusuna geçirilen değerlere erişmek için kurucunun gövdesinde kullanılabilir.

*radius* ve *color* veri özniteliklerinin değerlerini, kurucu metoda geçirilen değerlere ayarlayabiliriz.

Benzer şekilde, Python’da `rectangle` sınıfını da tanımlayabiliriz.

Sınıfın adı farklıdır. Bu sefer sınıfın veri öznitelikleri  *color* , *height* ve  *width* ’tür.

---

## 📦 Nesne Kurucusu, `self` ve Özniteliklere Erişim

Sınıfı oluşturduktan sonra, `circle` sınıfından bir nesne oluşturmak için bir değişken tanımlarız.

Bu, nesnenin adı olacaktır.

Nesneyi, nesne kurucusunu ( *object constructor* ) kullanarak oluştururuz.

Nesne kurucusu, sınıfın adından ve parametrelerden oluşur. Bu parametreler, veri öznitelikleridir.

Bir `circle` nesnesi oluştururken, kodu bir fonksiyon çağırır gibi çağırırız.

`circle` kurucusuna geçirilen argümanlar, yeni oluşturulmuş `circle` örneğinin veri özniteliklerini ilklendirmek için kullanılır.

`self`’i, nesnenin tüm veri özniteliklerini içeren bir kutu gibi düşünmek faydalıdır.

Nesnenin adını yazıp ardından bir nokta ve veri özniteliğinin adını yazmak, bize o veri özniteliğinin değerini verir; örneğin  *radius* .

Bu örnekte *radius* değeri 10’dur.

Aynı şeyi *color* için de yapabiliriz.

Böylece `self` parametresi ile nesne arasındaki ilişkiyi görebiliriz.

Python’da ayrıca nesnenin adını, ardından bir nokta ve veri özniteliğinin adını yazarak bu veri özniteliğini doğrudan ayarlayabilir veya değiştirebiliriz; ardından eşittirle uygun değeri atarız.

*color* veri özniteliğinin değiştiğini doğrulayabiliriz.

Genellikle, bir nesnedeki veriyi değiştirmek için sınıf içinde metotlar tanımlarız.

---

## 🧮 Metotlar ile Nesnenin Durumunu Değiştirmek

Şimdi metotları tartışalım.

Veri özniteliklerinin, nesneleri tanımlayan verilerden oluştuğunu gördük.

Metotlar, veri öznitelikleriyle etkileşime giren ve onları değiştiren, yani nesnenin veri özniteliklerini kullanan veya değiştiren fonksiyonlardır.

Diyelim ki bir dairenin boyutunu değiştirmek istiyoruz.

Bu, *radius* özniteliğini değiştirmeyi gerektirir.

`circle` sınıfına *add radius* adlı bir metot ekleriz.

Bu metot, `self`’in yanı sıra başka parametreler de gerektiren bir fonksiyondur.

Bu durumda,  *radius* ’a bir değer ekleyeceğiz.

Bu değeri *r* olarak gösteririz. *radius* veri özniteliğine *r* değerini ekleyeceğiz.

Bir nesne oluşturup *add radius* metodunu çağırdığımızda bu kod parçasının nasıl çalıştığını görelim.

Daha önce olduğu gibi, nesneyi nesne kurucusuyla oluştururuz.

Kurucuya iki argüman geçiririz. *radius* ikiye, *color* ise  *red* ’e ayarlanır.

Kurucunun gövdesinde veri öznitelikleri ayarlanır. Nesnenin mevcut durumunu görmek için kutu benzetmesini kullanabiliriz.

Metodu, bir nokta, ardından metodun adı ve parantezleri yazarak çağırırız.

Bu durumda fonksiyonun argümanı, eklemek istediğimiz miktardır.

Metodu çağırırken `self` parametresini dert etmemize gerek yoktur.

Tıpkı kurucuda olduğu gibi, bununla Python ilgilenir.

Çoğu durumda, metodun tanımında `self` dışında hiçbir parametre olmayabilir; bu durumda fonksiyonu çağırırken argüman geçmeyiz.

İçeride, metot sekiz değeri ve uygun `self` nesnesiyle çağrılır.

Metot, `self.radius` için yeni bir değer atar.

Bu işlem, özellikle *radius* veri özniteliğini değiştirerek nesneyi değiştirir.

*add radius* metodunu çağırdığımızda, *radius* veri özniteliğinin değerini değiştirerek nesneyi değiştirmiş oluruz.

---

## 🎨 `drawCircle` Metodu ve Varsayılan Değerler

Bir sınıfın kurucusunun parametrelerine varsayılan değerler ekleyebiliriz.

Laboratuvarlarda ayrıca `drawCircle` adlı metodu da oluştururuz.

`drawCircle`’ın implementasyonu için laboratuvara bakın.

Laboratuvarlarda, kurucuyu kullanarak *circle* türünden yeni bir nesne oluşturabiliriz.

Bu nesnede *color* *red* ve *radius* üç olacaktır.

*radius* veri özniteliğine erişebiliriz. *color* özniteliğine erişebiliriz.

Son olarak `drawCircle` metodunu kullanarak daireyi çizebiliriz.

Benzer şekilde *circle* türünden yeni bir nesne daha oluşturabiliriz.

Bu nesnede *radius* veri özniteliğine erişebiliriz. *color* veri özniteliğine erişebiliriz.

`drawCircle` metodunu kullanarak daireyi çizebiliriz.

Özetle, `circle` sınıfından `RedCircle` adlı bir nesne oluşturduk; bu nesnenin *radius* özniteliği üç ve *color* özniteliği  *red* ’dir.

Ayrıca `circle` sınıfından `BlueCircle` adlı bir nesne oluşturduk; bu nesnenin *radius* özniteliği 10 ve *color* özniteliği  *blue* ’dur.

---

## 🟦 `rectangle` Sınıfı ve `drawRectangle` Metodu

Laboratuvarda, `rectangle` için benzer bir sınıfımız vardır.

Kurucuyu kullanarak *rectangle* türünden yeni bir nesne oluşturabiliriz.

*height* veri özniteliğine erişebiliriz.

*width* veri özniteliğine de erişebiliriz.

Aynı şeyi *color* veri özniteliği için de yapabiliriz.

`drawRectangle` metodunu kullanarak dikdörtgeni çizebiliriz.

---

## 📚 `dir` Fonksiyonu ile Öznitelikleri İncelemek

Bir sınıfımız ve o sınıfın bir gerçekleşimi ya da örneklenmesi ( *instantiation* ) olan bir nesnemiz vardır.

Örneğin, `circle` sınıfından iki nesne ya da `rectangle` sınıfından iki nesne oluşturabiliriz.

`dir` fonksiyonu, bir sınıfla ilişkili veri özniteliklerinin ve metotların listesini elde etmek için yararlıdır.

İlgi duyduğunuz nesne, bu fonksiyona argüman olarak geçirilir.

Dönen değer, o nesnenin veri özniteliklerinin bir listesidir.

Alt çizgilerle çevrili öznitelikler dahili kullanım içindir ve bunlar hakkında endişelenmenize gerek yoktur.

Normal görünen öznitelikler, ilgilenmeniz gereken özniteliklerdir.

Bunlar nesnenin metotları ve veri öznitelikleridir.

Python’da nesnelerle yapabileceğiniz çok daha fazla şey vardır.

Daha fazla bilgi için python.org’a bakın.
