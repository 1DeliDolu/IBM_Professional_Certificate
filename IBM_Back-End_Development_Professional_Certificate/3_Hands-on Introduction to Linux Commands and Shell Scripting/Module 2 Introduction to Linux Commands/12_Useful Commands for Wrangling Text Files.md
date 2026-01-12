# 🧰 Metin Dosyalarını Düzenlemek için Faydalı Komutlar

## 👋 Giriş

“Metin Dosyalarını Düzenlemek için Faydalı Komutlar”a hoş geldiniz.

Bu videoda, dosyalar üzerinde çalışan komutları kullanarak şunları yapmayı öğreneceksiniz:

* Satır satır sıralanmış bir görünüm oluşturmak.
* Tekrarlanan satırları hariç tutan bir görünüm oluşturmak.
* Belirli bir deseni içeren satırları çıkarmak.
* Her satırdan dilimler ve alanlar çıkarmak.
* Birden fazla dosyadaki satırları birleştirmek.

`sort` komutu, bir dosyanın satırlarını alfasayısal olarak sıralar ve sıralanmış sonucu standart çıktıya yazdırır.

---

## 🔤 `sort` komutu ile satırları sıralama

Aşağıdaki komutu girerek:

```bash
sort pets.txt
```

alfabetik olarak sıralanmış çıktıyı elde edersiniz; burada **“cat”** beş kez ve **“dog”** iki kez tekrar eder.

Şu komutu girerseniz:

```bash
sort -R pets.txt
```

satırları ters sırada sıralanmış olarak geri alırsınız; bu kez **“dog”** satırları **“cat”** satırlarından önce görünür.

---

## 🔁 `unique` komutu ile tekrar eden satırları filtreleme

Dosyanızda yinelenen satırlar varsa, tekrar eden satırları filtrelemek için `unique` komutunu kullanabilirsiniz.

`pets.txt` dosyasının içeriğini hatırlamak için:

```bash
cat pets.txt
```

komutunu girersiniz.

Ardından:

```bash
unique pets.txt
```

komutunu girerek  **“cat”** , **“dog”** ve **“cat”** çıktısını elde edersiniz.

`unique` komutunun, yalnızca art arda gelen (ardışık) satırlar aynıysa yinelenen satırları kaldırdığını unutmayın. Bu nedenle, **“cat”** sözcüğü burada iki kez görünür; çünkü  **“cat”** , iki **“dog”** satırından hem önce hem sonra yer alarak ardışık diziyi kesintiye uğratır.

---

## 🔍 `grep` komutu ile desen eşleştirme

`grep` komutu, **“global regular expression print”** ifadesinin kısaltmasıdır ve bir dosyada, *düzenli ifade* gibi belirtilen bir desene uyan satırları döndürür.

Ünlü kişilerin adlarının bulunduğu bir listenin, bir dosyada saklandığını varsayalım; bu dosyayı:

```bash
cat people.txt
```

komutunu girerek görüntüleyebilirsiniz.

`grep` komutunu, `people.txt` dosyasında art arda gelen **“c h”** karakterlerini içeren tüm satırları bulmak için kullanabilirsiniz. Bunu yapmak için, `grep` komutuna eşleşen terimi, yani **“c h”** ifadesini, ardından da dosya adını verirsiniz.

Çıktı, **“c h”** ifadesine küçük harf eşleşmesi içeren iki sonucu döndürür: **Dennis Ritchie** ve  **Erwin Schrodinger** .

Aynı işlemi bu kez **“minus i”** seçeneğiyle gerçekleştirdiğinizde ise, büyük harfle başlayan bir C içeren **Charles Babbage** adlı fazladan bir sonuç elde edersiniz. **“minus i”** seçeneği, deseni büyük/küçük harf duyarsız hâle getirerek arama kapsamını genişletir.

---

## ✂️ `cut` komutu ile satırlardan dilim ve alan çıkarmak

Ayrıca, dosyanızdaki her satırdan belirli bölümleri çıkarmak için `cut` komutunu kullanabilirsiniz.

Burada, **Alan Turing** ve **Charles Babbage** gibi ünlü isimlerden oluşan listeyi yeniden görüyorsunuz.

Her satırdan ikinci ile dokuzuncu karakterler arasını çıkarmak için şu komutu girebilirsiniz:

```bash
cut -C 2-9 people.txt
```

Çıktıdan, **“Alan Turing”** ifadesinin **“Lan Turi”** olarak döndürüldüğünü görebilirsiniz.

Şimdi, metin dosyalarıyla `cut` kullanmak için daha pratik bir örneğe bakalım. Listenizdeki her kişinin yalnızca soyadını çıkarmak istediğinizi varsayalım. Listenizdeki her satırın, kişinin **adı** ve **soyadı** olmak üzere iki alandan oluştuğunu biliyorsunuz.

---

### 🔠 Alan ayırıcı ve alan seçimi

Bu alanları bir boşluk ayırır.

Burada, her satırdan ikinci alanı çıkarmak için kesme işlemi yapıyorsunuz.

* **“minus d quote space quote”** seçeneğini kullanarak, alan ayırıcısının (alanlar arasındaki kırılmayı gösteren karakterin) bir **boşluk** olduğunu belirtebilirsiniz (`-d " "`).
* Ardından, her satırdan ikinci alanı döndürmek için **“minus f two”** seçeneğini (`-f 2`) kullanırsınız.

Bu, listedeki her kişinin **soyadını** döndürür.

---

## 📎 `paste` komutu ile birden fazla dosyanın satırlarını birleştirme

Ek olarak, birden fazla dosyadaki satırları birleştirmek için `paste` komutunu kullanabilirsiniz.

Her biri aynı sayıda satır içeren şu üç metin dosyasının size verildiğini hayal edin:

* İnsanların ilk adlarının listelendiği `first.txt` adlı bir metin dosyası.
* Aynı kişilerin soyadlarını içeren tamamlayıcı `last.txt` adlı bir metin dosyası.
* Her kişinin doğum yılının listelendiği `yob.txt` adlı üçüncü bir metin dosyası.

Bu dosyaları bir tablo olarak görüntülemek için:

```bash
paste first.txt last.txt yob.txt
```

komutunu girebilirsiniz.

Üç sütunun da düzgün hizalandığına dikkat edin; çünkü `paste`, varsayılan ayırıcı olarak bir **sekme (Tab)** kullanır.

Bu tabloyu kullanarak, örneğin  **Charles Babbage** 'ın **1791** yılında doğduğunu görebilirsiniz.

---

### 🔡 Ayırıcıyı değiştirmek

`paste` komutuyla, **“minus D”** seçeneğini kullanarak Tab dışında bir ayırıcı belirleyebilirsiniz.

Örneğin, çift tırnak içine alınmış bir virgülle birlikte **“paste minus D”** yazarak ve bunu  **“first”** , **“last”** ve **“yob”** metin dosyalarıyla birlikte kullanarak, ayırıcı olarak **virgül** belirleyebilirsiniz.

Bu komut, her alanın arasında virgül olacak şekilde üç dosyayı birleştiren bir tablo oluşturur; örneğin:

> **“Dennis virgül Ritchie virgül 1941”**

---

## ✅ Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* Bir dosyanın satırlarını `sort` kullanarak alfasayısal olarak görüntülemek.
* Görünümünüzden tekrarlanan satırları `unique` ile kaldırmak.
* İstediğiniz ölçütlerle eşleşen satırları `grep` kullanarak elde etmek.
* Satırlardan dilimler ve alanlar çıkarmak için `cut` komutunu kullanmak.
* Farklı dosyalardaki satırları `paste` komutuyla birleştirmek.
