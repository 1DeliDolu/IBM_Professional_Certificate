# 📂 Open ile Dosya Okuma

Bu bölümde, Python'un yerleşik `open` fonksiyonunu kullanarak bir dosya nesnesi oluşturacak ve bir `txt` dosyasından verileri elde edeceğiz.

Python'un `open` fonksiyonunu bir dosya nesnesi elde etmek için kullanacağız. Bu nesneye, dosyadan veri okumak için bir yöntem ( *method* ) uygulayabiliriz.

---

## 📁 `open` Fonksiyonu ve Dosya Yolu

`example1.txt` dosyasını aşağıdaki şekilde açabiliriz.

`open` fonksiyonunu kullanırız. İlk argüman *dosya yoludur* ( *file path* ). Bu yol, dosya adı ve dosya dizininden oluşur.

---

## ⚙️ Dosya Modu ( *mode* ) ve Dosya Nesnesi

İkinci parametre ise  *mod* ’dur ( *mode* ). Yaygın kullanılan değerler şunlardır:

* `r` — okuma ( *reading* )
* `w` — yazma ( *writing* )
* `a` — ekleme ( *appending* )

Biz okuma için `r` kullanacağız.

Sonuçta elimizde bir *dosya nesnesi* ( *file object* ) olur. Artık bu dosya nesnesini, dosya hakkında bilgi edinmek için kullanabiliriz.

---

## 📑 Dosya Özniteliklerine ( *Attributes* ) Erişim

Dosya adını elde etmek için veri özniteliği `name`’i kullanabiliriz. Sonuç, dosyanın adını içeren bir string olur.

Nesnenin hangi modda olduğunu görmek için veri özniteliği `mode`’u kullanabiliriz ve burada `r`, okuma ( *read* ) modunu temsil edecek şekilde gösterilir.

---

## 🔒 Dosyayı Kapatma ve `with` Deyimi

Dosya nesnesini her zaman `close` yöntemiyle kapatmalısınız: `close()`.

Bu bazen yorucu hale gelebileceğinden, `with` deyimini kullanalım. Bir dosyayı `with` deyimiyle açmak daha iyi bir pratiktir, çünkü dosyayı otomatik olarak kapatır.

Kod, girintili ( *indent* ) blok içindeki her şeyi çalıştırır ve ardından dosyayı kapatır. Bu kod, `example1.txt` dosyasını okur. Bu süreçte `file1` dosya nesnesini kullanabiliriz.

Kod, girinti bloğundaki tüm işlemleri gerçekleştirir ve girintinin sonunda dosyayı kapatır.

---

## 📖 `read` Metodu ile Dosya İçeriğini Okuma

`read` yöntemi, dosyanın değerlerini string olarak `file underscore stuff` değişkeninde saklar.

Dosya içeriğini yazdırabilirsiniz. Dosya içeriğinin kapatılıp kapatılmadığını da kontrol edebilirsiniz, ancak girinti dışında ondan okuma yapamazsınız.

Buna rağmen, dosya içeriğini girintinin dışında da yazdırabilirsiniz. Dosya içeriğini yazdırabiliriz ve şöyle bir çıktı görürüz.

Ham stringi incelediğimizde, `\n` işaretini görürüz. Bu, Python’un yeni bir satıra başlaması gerektiğini bilmesi içindir.

---

## 📜 `readlines` Metodu ile Satır Satır Okuma

Her satırı, bir listenin elemanı olacak şekilde çıktı vermek için `readlines` yöntemini kullanabiliriz.

* İlk satır, listedeki ilk elemana karşılık gelir.
* İkinci satır, listedeki ikinci elemana karşılık gelir ve bu böyle devam eder.

---

## 🧵 `readline` Metodu ile Satır Okuma

Dosyanın ilk satırını okumak için `readline` yöntemini kullanabiliriz.

Bu komutu çalıştırırsak, ilk satır `file underscore stuff` değişkeninde saklanır ve ardından ilk satır yazdırılır.

`readline` yöntemini iki kez kullanabiliriz.

* İlk çağrıldığında, ilk satırı `file underscore stuff` değişkenine kaydeder ve ardından ilk satırı yazdırır.
* İkinci kez çağrıldığında, ikinci satırı `file underscore stuff` değişkenine kaydeder ve ardından ikinci satırı yazdırır.

---

## 🔁 Döngü ile Satır Satır Yazdırma

Her satırı tek tek yazdırmak için bir döngü kullanabiliriz.

Her karakteri, bir string içindeki bir ızgara ( *grid* ) olarak temsil edelim.

---

## 🔢 Karakter Sayısına Göre Okuma

Bir string’ten okumak istediğimiz karakter sayısını, `readlines` yöntemine argüman olarak belirtebiliriz.

`readlines` yöntemine argüman olarak `4` kullandığımızda, dosyadaki ilk dört karakteri yazdırırız.

Her seferinde yöntemi çağırdığımızda, metin içinde ilerleriz.

* Yöntemi `16` argümanıyla çağırırsak, ilk 16 karakter ve ardından yeni satır yazdırılır.
* Yöntemi ikinci kez çağırdığımızda, sonraki 5 karakter yazdırılır.
* Son olarak, yöntemi son kez `9` argümanıyla çağırırsak, son 9 karakter yazdırılır.

Laboratuvarları ( *labs* ) inceleyerek, yöntemlere ve diğer dosya türlerine ilişkin daha fazla örneğe göz atabilirsiniz.
