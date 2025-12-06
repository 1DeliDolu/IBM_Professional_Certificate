# ✍️ Open ile Dosya Yazma

## 📝 Dosyalara Yazmak için `open` Fonksiyonunu Kullanma

Dosyalara yazmak için de `open` fonksiyonunu kullanabiliriz.

Bir metin dosyası oluşturmak için, bir dosya nesnesi elde etmek üzere Python'un `open` fonksiyonunu kullanacağız.

Bu dosyaya veri yazmak için `write` yöntemini ( *method* ) uygulayabiliriz.

Sonuç olarak, metin dosyaya yazılacaktır.

---

## 📄 `Example2.txt` Dosyasını Oluşturma

`Example2.txt` dosyasını aşağıdaki şekilde oluşturabiliriz.

`open` fonksiyonunu kullanırız.

İlk argüman, *dosya yoludur* ( *file path* ).

Bu yol, dosya adından (eğer bu dosya dizininizde varsa, üzerine yazılacaktır) ve dosya dizininden oluşur.

Mod ( *mode* ) parametresini yazma için `W` olarak ayarlarız.

Son olarak, elimizde dosya nesnesi vardır.

---

## 📌 `with` Deyimi ile Dosya Yönetimi

Önceden olduğu gibi, `with` deyimini kullanırız.

Kod, girintili ( *indent* ) blok içindeki her şeyi çalıştıracak, ardından dosyayı kapatacaktır.

`File1` dosya nesnesini oluştururuz. `open` fonksiyonunu kullanırız.

Bu, dizininizde `Example2.txt` adlı bir dosya oluşturur.

---

## ✏️ `write` Yöntemi ile Metin Yazma

Dosyaya veri yazmak için `write` yöntemini kullanırız.

Argüman, dosyaya girmek istediğimiz metindir.

`write` yöntemini art arda kullanırsak, her çağrıldığında dosyaya yazacaktır.

İlk kez çağrıldığında, yeni satırı temsil etmek için `\n` (slash-n) ile birlikte `"This is line A"` yazacağız.

Yöntemi ikinci kez çağırdığımızda, `"This is line B"` yazacak ve sonra dosyayı kapatacaktır.

---

## 📚 Listedeki Elemanları Dosyaya Yazma

Bir listedeki her öğeyi bir dosyaya yazabiliriz.

Önceden olduğu gibi, bir dosya oluşturmak için `with` komutunu ve `open` fonksiyonunu kullanırız.

`Lines` listesi, metinden oluşan üç öğeye sahiptir.

`Lines` listesinin her bir öğesini okumak için bir `for` döngüsü kullanır ve onu `line` değişkenine geçiririz.

Döngünün ilk yinelemesi, listenin ilk öğesini `Example2` dosyasına yazar.

İkinci yineleme, listenin ikinci öğesini yazar ve bu böyle devam eder.

Döngünün sonunda, dosya kapatılacaktır.

---

## ➕ `append` Modu ile Dosyaya Ekleme

Modu, küçük harf `a` kullanarak ekleme ( *appended* ) moduna ayarlayabiliriz.

Bu, yeni bir dosya oluşturmaz, yalnızca var olan dosyayı kullanır.

`write` yöntemini çağırırsak, yalnızca mevcut dosyaya yazacak, ardından `"This is line C"` ekleyecek ve sonra dosyayı kapatacaktır.

---

## 📂 Bir Dosyayı Yeni Bir Dosyaya Kopyalama

Bir dosyayı yeni bir dosyaya aşağıdaki şekilde kopyalayabiliriz.

Önce, `Example1` dosyasını okur ve onunla `readfile` dosya nesnesi aracılığıyla etkileşim kurarız.

Sonra, `Example3` adlı yeni bir dosya oluşturur ve onunla etkileşim kurmak için `writefile` dosya nesnesini kullanırız.

`for` döngüsü, `readfile` dosya nesnesinden bir satır alır ve `writefile` dosya nesnesini kullanarak bunu `Example3` dosyasında depolar.

İlk yineleme, ilk satırı kopyalar.

İkinci yineleme, dosyanın sonuna ulaşılana kadar ikinci satırı kopyalar.

Sonra her iki dosya da kapatılır.

---

## 🧪 Daha Fazla Alıştırma

Daha fazla örnek için laboratuvarlara ( *labs* ) göz atın.
