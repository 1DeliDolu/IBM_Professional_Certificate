# 📦 Dosya Arşivleme ve Sıkıştırma Komutları

File Archiving and Compression Commands’e hoş geldiniz.

Bu videoyu izledikten sonra şunları yapabileceksiniz:

* Dosya arşivlemeyi dosya sıkıştırmadan ayırt etmek
* Arşivlenmiş dosyalar oluşturmak ve bunları açmak
* Dosyaları arşivlerden sıkıştırmak, sıkıştırmayı açmak ve çıkarmak için komutlar uygulamak

---

## 🗃️ Arşivleme ve Sıkıştırma Nedir?

Arşivleme ve sıkıştırma genellikle birlikte kullanılan, ancak birbirinden farklı iki işlemdir.

 **Arşivleme** , düzenli olarak kullanmadığınız fakat saklamak istediğiniz bilgileri depolama işlemidir.

Arşivlenmiş bir dosya, tek bir dosya olarak saklanan veri dosyaları ve dizinlerden oluşan bir koleksiyondur.

Arşivleme:

* Koleksiyonu daha taşınabilir hale getirir
* Kayıp veya bozulma durumuna karşı bir **yedek** görevi görür

**Dosya sıkıştırma** ise, bir dosyanın içerdiği bilginin tekrarlarından yararlanarak dosya boyutunu küçültme işlemidir.

Sıkıştırmanın başlıca avantajları şunlardır:

* Depolama alanını korumak
* Dosya transferlerini hızlandırmak
* Bant genişliği yükünü azaltmak

---

## 📁 Örnek Dizin Yapısı: `notes` Klasörü

Diyelim ki, ders materyallerinizi takip etmek için bir `notes` dizini oluşturdunuz.

Bu notlarınızı ileride ihtiyaç duyabileceğiniz düşüncesiyle arşivlemenin iyi bir fikir olduğuna karar veriyorsunuz.

`notes` dizin ağacının yapısı şu şekildedir:

* `notes` adlı bir üst dizin
  * `math` adlı bir alt klasör
  * `physics` adlı bir alt klasör
  * Her bir alt klasörde aynı isimlere sahip dosyalar:
    * `week1`
    * `week2`

`ls` komutunu `-R` seçeneğiyle kullanarak, geçerli dizin ağacınızdaki tüm dizin ve dosyaları özyinelemeli (recursive) olarak listeleyebilirsiniz:

```bash
ls -R
```

Böylece, grafiksel dizin yapısıyla olan karşılığı görebilirsiniz:

* Üstte `notes` dizini
* Alt dizinler olarak `math` ve `physics`
* Bu dizinlerin içinde `week1` ve `week2` dosyaları

---

## 🎞️ `tar` Komutu ile Arşivleme

`tar` (tape archiver) komutunu, dosya ve dizinleri arşivlemek ve arşivden çıkarmak için kullanabilirsiniz.

Arşivlenmiş bir `tar` dosyası için popüler bir terim  **tar ball** ’dır.

Tüm `notes` dizininizi, alt dizinleri ve içlerindeki tüm dosyalarla birlikte arşivlemek için şu komutu girebilirsiniz:

```bash
tar -cf notes.tar notes
```

Burada:

* `-c` seçeneği, yeni bir arşiv oluşturmak anlamına gelir
* `-f` bayrağı, `tar` komutuna girdisini **dosyadan** almasını söyler; aksi halde varsayılanı **standart girdi**dir

`ls` komutunu girdiğinizde, geçerli dizininizde hem orijinal `notes` klasörünün, hem de `notes.tar` arşiv dosyasının bulunduğunu görebilirsiniz:

```bash
ls
```

---

## 🌀 `gzip` ile Sıkıştırılmış `tar` Arşivi Oluşturma

Arşivinizin sıkıştırılmış olmasını da istiyorsanız, aynı komutu girip bu kez `-z` seçeneğini ekleyebilirsiniz.

`-z` seçeneği, arşivi `gzip` adlı yeni bir sıkıştırma programı üzerinden filtreler.

Çıktı adının sonuna `.gz` soneki eklemek, örneğin Windows tabanlı programların dosya türünü doğru biçimde tanımasını sağlar:

```bash
tar -czf notes.tar.gz notes
```

`ls` komutunu girdiğinizde, artık oluşturduğunuz sıkıştırılmış `notes.tar.gz` dosyasını görebilirsiniz:

```bash
ls
```

---

## 📄 `tar` Arşivinin İçeriğini Listeleme

Arşivlenmiş `notes` dosyanızın içeriğini kontrol etmek için, `tar` komutunu `tar ball` üzerinde `-t` (veya list) seçeneği ile çağırabilirsiniz:

```bash
tar -tf notes.tar
```

Bu komut, `tar` arşivinizdeki tüm dosya ve dizinleri listeleyecektir.

Beklendiği gibi, yapı orijinal `notes` klasörünüzle aynıdır:

* Üst dizin: `notes`
* Alt dizinler: `math` ve `physics`
* Uç düğümler (terminal nodes): `week1` ve `week2` dosyaları

---

## 📂 `tar` ile Arşivi Açma (De-archive / Extract)

Arşivlenmiş dosyalarınızı açmak veya arşivden çıkarmak için yine `tar` komutunu kullanabilirsiniz.

Aşağıdaki komutu girebilirsiniz:

```bash
tar -xf notes.tar notes
```

Burada:

* `-x` seçeneği, `tar` komutuna arşivden dosya ve dizin nesnelerini çıkarmasını söyler
* `notes` isteğe bağlı bir hedef adıdır ve bu örnekte **varsayılan** ile aynıdır

Ardından, şu komutu girerek sonucu görebilirsiniz:

```bash
ls -R
```

Bu listede:

* `notes` adlı bir üst klasör
* `math` ve `physics` adlı alt klasörler
* Başlangıçta sahip olduğunuz dört dosya: `week1` ve `week2` (her iki klasörün içinde)

görünür.

Bu, `notes` dizininizin orijinal yapısının **bozulmadan korunduğunu** doğrular.

---

## 🗜️ `tar.gz` Arşivlerini Açma ve Sıkıştırmayı Çözme

Benzer şekilde, bir `.tar.gz` dosyasını da sıkıştırmasını açabilir ve içindeki dosyaları çıkarabilirsiniz.

Sıkıştırılmış `notes.tar.gz` dosyasını açıp sıkıştırmasını çözmek için:

```bash
tar -xzf notes.tar.gz notes
```

Komuttan sonra yine:

```bash
ls -R
```

girdiğinizde, dizin ve dosyaların beklendiği gibi açılıp yerleştirildiğini görebilirsiniz.

---

## 📦 `zip` Komutu ile Sıkıştırma ve Paketleme

`zip` komutunu, dosyaları ve dizinleri sıkıştırmak ve bunları tek bir arşiv içinde paketlemek için kullanabilirsiniz.

`zip`’in uyguladığı işlem sırasına dikkat edin:

* `zip`, dosyaları  **önce sıkıştırır** , ardından **paketler**
* Öte yandan `tar`, `-z` seçeneği ile, önce tüm dosyaları bir **tar ball** içinde paketler, ardından tüm `tar` dosyasına birden `gzip` uygular

`notes` dizininizi sıkıştırmak ve bir `zip` dosyasına paketlemek için:

```bash
zip -r notes.zip notes
```

Ardından `ls` komutunu girdiğinizde, `notes.zip` arşivinin oluşturulduğunu görebilirsiniz:

```bash
ls
```

---

## 🔓 `unzip` ile Zip Arşivlerini Açma

Tahmin edebileceğiniz gibi, `unzip` komutu, zip arşivinden sıkıştırılmış dosyaları çıkarır ve sıkıştırmalarını açar.

`notes.zip` dosyanızın sıkıştırmasını açmak için şunu girin:

```bash
unzip notes.zip
```

Daha sonra:

```bash
ls -R
```

girdiğinizde, `unzip` komutunun `notes` klasörünü oluşturduğunu ve dizinlerinizi, `week1` ve `week2` dosyalarınızı beklendiği gibi açıp yerleştirdiğini görebilirsiniz.

---

## ✅ Özet

Bu videoda şunları öğrendiniz:

* Dosya sıkıştırmanın başlıca avantajlarının, depolama alanını korumak, dosya transferlerini hızlandırmak ve bant genişliği yükünü azaltmak olduğunu
* `zip` komutunu kullanarak dosya ve dizinleri sıkıştırıp, bunları tek bir arşiv içinde paketleyebileceğinizi
* `tar` komutuyla dosya ve dizinleri bir **tar ball** içine arşivleyebileceğinizi ve isteğe bağlı olarak bu `tar` dosyasına `gzip` sıkıştırması uygulayabileceğinizi
* `unzip` komutunu kullanarak sıkıştırılmış bir zip arşivini açıp sıkıştırmasını çözebileceğinizi
* Son olarak, `tar` komutunu kullanarak bir `.tar.gz` arşivinin sıkıştırmasını açıp içindeki dosyaları çıkarabileceğinizi
