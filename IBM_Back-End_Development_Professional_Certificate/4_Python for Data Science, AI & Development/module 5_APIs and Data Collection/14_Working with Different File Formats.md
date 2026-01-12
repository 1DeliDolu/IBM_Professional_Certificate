# 📂 Farklı Dosya Biçimleriyle Çalışmak

## 👋 Giriş ve Öğrenme Hedefleri

Merhaba. **Farklı Dosya Biçimleriyle Çalışmak** dersine hoş geldiniz.

Bu videoyu izledikten sonra şunları yapabileceksiniz:

* `csv`, `xml` ve `json` gibi farklı dosya biçimlerini tanımlamak.
* Veriyi okumak ve çıktısını almak için basit programlar yazmak.
* Veriyi çıkarmak için hangi Python kütüphanelerine ihtiyaç duyulduğunu listelemek.

Veri toplarken, veri odaklı bir hikâyeyi veya analizi tamamlayabilmek için toplanması ya da okunması gereken pek çok farklı dosya biçimi olduğunu göreceksiniz.

Verileri toplarken, Python önceden tanımlanmış kütüphaneleri sayesinde bu süreci daha basit hâle getirebilir, ancak Python'u incelemeden önce gelin önce çeşitli dosya biçimlerine göz atalım.

## 🧾 Dosya Uzantıları ve Dosya Türleri

Bir dosya adına bakarken, başlığın sonunda bir uzantı fark edeceksiniz.

Bu uzantılar, dosyanın hangi türde olduğunu ve onu açmak için neye ihtiyaç duyulduğunu size bildirir.

Örneğin, `FileExample.csv` gibi bir başlık görürseniz, bunun bir `csv` dosyası olduğunu bilirsiniz.

Bu, farklı dosya türlerinden yalnızca bir örnektir; `json` veya `xml` gibi daha birçok tür vardır.

Bu farklı dosya biçimleriyle karşılaştığımızda ve içlerindeki veriye erişmeye çalıştığımızda, bu süreci kolaylaştırmak için Python kütüphanelerinden yararlanmamız gerekir.

Tanımanız gereken ilk Python kütüphanesinin adı  **Pandas** ’tır.

Bu kütüphaneyi kodun başında içe aktararak farklı dosya türlerini kolayca okuyabilir hâle geliriz.

## 📥 Panda Kütüphanesi ile İlk `csv` Dosyasını Okuma

Artık **Panda** kütüphanesini içe aktardığımıza göre, onu ilk `csv` dosyasını okumak için kullanalım.

Bu örnekte `FileExample.csv` dosyasıyla karşılaştık.

İlk adım, dosyayı bir değişkene atamaktır.

Ardından, dosyayı **Panda** kütüphanesinin yardımıyla okumak için başka bir değişken oluştururuz.

Daha sonra `read_csv` fonksiyonunu çağırarak verinin ekrana çıktısını alabiliriz.

Bu örnekte verinin başlıkları olmadığı için, ilk satırı başlık olarak eklemiştir.

Verinin ilk satırını başlık olarak istemediğimizden, bu sorunu nasıl düzelteceğimizi öğrenelim.

## 📊 `csv` Verisini Daha Düzenli Görüntüleme

Artık bir `csv` dosyasındaki veriyi nasıl okuyup çıktısını alacağımızı öğrendiğimize göre, bunu biraz daha düzenli hâle getirelim.

Son örnekte veriyi yazdırabildik, ancak dosyada başlıklar olmadığı için ilk veri satırını başlık olarak yazdırdı.

Bu durumu, bir *dataframe* niteliği ekleyerek kolayca çözeriz.

Dosyayı çağırmak için `df` değişkenini kullanır ve ardından `columns` niteliğini ekleriz.

Programımıza bu tek satırı ekleyerek, veri çıktısını her sütun için belirtilen başlıklar altında düzgün bir şekilde düzenleyebiliriz.

## 🧱 `json` Dosya Biçimi

İnceleyeceğimiz bir sonraki dosya biçimi `json` dosya biçimidir.

Bu tür bir dosyada metin, dilden bağımsız bir veri biçiminde yazılır ve bir Python sözlüğüne ( *dictionary* ) benzer.

Bu tür bir dosyayı okumanın ilk adımı, `json` modülünü içe aktarmaktır.

`json` içe aktarıldıktan sonra, dosyayı açmak için bir satır ekleyebilir, dosyayı okumaya başlamak için `json` modülünün `load` niteliğini çağırabilir ve son olarak dosyayı yazdırabiliriz.

## 📄 `xml` Dosya Biçimi

Sıradaki dosya biçimi `xml`’dir.

Bu tür bir dosya, *Extensible Markup Language* olarak da bilinir.

Pandas kütüphanesinin bu tür bir dosyayı okumak için bir niteliği bulunmadığından, şimdi bu tür bir dosyayı nasıl ayrıştıracağımızı inceleyelim.

Bu tür bir dosyayı okumanın ilk adımı, `xml` modülünü içe aktarmaktır.

Bu kütüphaneyi içe aktararak, `xml` dosyasını ayrıştırmak için `etree` niteliğini kullanabiliriz.

## 🔁 `xml` Verisini Döngü ile DataFrame’e Eklemek

Sonrasında sütun başlıklarını ekler ve bunları  *dataframe* ’e atarız.

Ardından, gerekli verileri toplamak ve veriyi bir  *dataframe* ’e eklemek için belgenin üzerinden geçen bir döngü oluştururuz.

## ✅ Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* Farklı dosya türlerini nasıl tanıyacağınızı.
* Veriyi çıkarmak için Python kütüphanelerini nasıl kullanacağınızı.
* Verileri toplarken  *dataframe* ’leri nasıl kullanacağınızı.
