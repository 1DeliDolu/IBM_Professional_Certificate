# 📄 Dosya İçeriğini Görüntüleme

## 🧾 Giriş

Dosya içeriğini görüntülemeye hoş geldiniz. Bu videoda, dosyalar üzerinde çalışan komutları kullanarak bir dosyanın içeriğini kullanışlı şekillerde nasıl görüntüleyebileceğinizi ve satır, kelime ve karakter sayılarını nasıl belirleyebileceğinizi öğreneceksiniz.

Dosya içeriğini görüntülemek için kullanabileceğiniz birkaç yararlı komut vardır.

---

## 🐱 `cat` komutu ile dosya içeriğini yazdırma

Başlangıç olarak, tüm dosyayı standart çıktıya yazdırmak için `cat` komutunu kullanabilirsiniz.

Geçerli dizininizde `numbers.txt` adlı tek bir dosya olduğunu varsayalım; bunu şu komutla görebilirsiniz:

```bash
ls
```

Bu dosyanın içeriğini standart çıktıya yazdırmak için şunu yazabilirsiniz:

```bash
cat numbers.txt
```

Bu komut, 89'dan 99'a kadar olan sayılardan oluşan ve burada gösterilen çıktıyı üretir. Çıktının tüm terminal penceresini kapladığını görebilirsiniz.

Dosya, burada gördüğünüz on iki satırdan çok daha uzundur. Bu nedenle, içerikleri görüntülemek için her zaman `cat` komutunu kullanmak istemeyebilirsiniz. Neyse ki, bu gibi durumlar için alternatif komutlar vardır.

---

## 📄 `more` komutu ile sayfa sayfa görüntüleme

`more` komutu, bir dosyanın içeriğini sayfa sayfa bir formatta görüntülemenizi sağlar.

Şu komutu yazarak:

```bash
more numbers.txt
```

1. sayfada, gösterildiği gibi 0–8 arasındaki sayıları görürsünüz. Burada “sayfa” derken, yalnızca geçerli terminal penceresini kastediyoruz.

Terminal pencerenizi dikey olarak genişletirseniz, sayfa boyutunu da artırmış olursunuz.

Boşluk (space) tuşuna bastığınızda, 9–17 arasındaki sayıları gösteren bir sonraki sayfayı görürsünüz.

`Q` tuşuna basmak, `more` programından çıkmanızı ve komut istemine geri dönmenizi sağlar.

---

## 🔝 `head` komutu ile dosya başını görüntüleme

Dosyanızın ilk 10 satırını yazdırmak için `head` komutunu kullanabilirsiniz.

```bash
head numbers.txt
```

Bu komut, gösterildiği gibi ilk 10 satırı, yani 0–9 arasındaki sayıları döndürür.

`head` komutunun kaç satır döndüreceğini belirtmek için `-n` seçeneğini kullanabilirsiniz.

Şu komutu yazarak:

```bash
head -n 3 numbers.txt
```

`numbers.txt` dosyasının ilk üç satırını, yani 0, 1, 2 değerlerini geri alırsınız.

---

## 🔚 `tail` komutu ile dosya sonunu görüntüleme

`tail` komutu, bir dosyanın son 10 satırını yazdırmak için kullanılır.

```bash
tail numbers.txt
```

Bu komut, `numbers.txt` dosyasının son 10 satırını, yani 90–99 arasındaki sayıları döndürür.

Tıpkı `head` komutunda olduğu gibi, döndürülen satır sayısını değiştirmek için `-n` seçeneğini kullanabilirsiniz:

```bash
tail -n 3 numbers.txt
```

Bu komutla `numbers.txt` dosyasının son üç satırını, yani 97, 98 ve 99 değerlerini geri alırsınız.

---

## 🔢 `wc` komutu ile satır, kelime ve karakter sayımı

`wc` komutunu, dosyanızdaki karakter, kelime veya satır sayısını hesaplamak için kullanabilirsiniz.

`pets.txt` adlı bir dosyanız olduğunu hayal edin.

```bash
cat pets.txt
```

Bu komut, dosyanın her satırda ya **cat** kelimesini ya da **dog** kelimesini içerdiğini gösterir.

Şu komutu yazarak:

```bash
wc pets.txt
```

Şu sonucu elde edersiniz:

```text
7 7 28 pets.txt
```

Bu, dosyanızın 7 satır, 7 kelime ve 28 karakter içerdiği anlamına gelir.

---

## 🧮 Yeni satır karakterlerinin sayılması

Ancak 7 çarpı 3, 21 eder; peki `wc` neden 28 karakter görür?

Bunun nedeni, *yeni satır (newline) karakterlerini* de saymasıdır. Onları orada göremezsiniz, ancak biri dosya sonunu temsil eden toplam yedi yeni satır karakteri vardır.

---

## 📊 Yalnızca satır, kelime veya karakter sayısını görüntüleme

Yalnızca satır sayısını görmek için `-l` seçeneğini kullanabilirsiniz; bu, şu sonucu döndürür:

```bash
wc -l pets.txt
```

```text
7 pets.txt
```

Benzer şekilde, yalnızca kelime sayısını görmek için `-w` seçeneğini, yalnızca karakter sayısını görmek için ise `-c` seçeneğini kullanabilirsiniz:

```bash
wc -w pets.txt
wc -c pets.txt
```

---

## ✅ Öğrendikleriniz

Bu videoda, dosya içeriklerini birden fazla şekilde görüntülemek için `cat`, `more`, `head` ve `tail` komutlarını; ayrıca bir dosyanın satır, kelime ve karakter sayılarını belirlemek için `wc` komutunu nasıl uygulayacağınızı öğrendiniz.
