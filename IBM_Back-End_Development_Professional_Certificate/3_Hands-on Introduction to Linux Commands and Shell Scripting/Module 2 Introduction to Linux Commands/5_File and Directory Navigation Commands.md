# 📂 Dosya ve Dizin Gezinti Komutları

## 🎬 “Dosya ve Dizin Gezinti Komutları”na Hoş Geldiniz

“File and Directory Navigation Commands” (Dosya ve Dizin Gezinti Komutları) başlığına hoş geldiniz.

Bu videoda şunları öğreneceksiniz:

* Bir dizinin içeriğini listelemek için *“list”* komutunu kullanmak
* *“change directory”* komutuyla farklı dizinler arasında gezinmek
* Göreli ( *relative* ) ve mutlak ( *absolute* ) yolları açıklamak
* *“find”* komutuyla dosya bulmak

---

## 📜 `ls` – Dizin İçeriğini Listeleme

`ls` veya *“list”* komutu, bir dizin içindeki dosya ve dizinleri listeler.

Ev dizininizde `ls` komutunu girerseniz, ev dizininizin içerdiği tüm dosya ve dizinleri görürsünüz.

Ayrıca `ls` komutuna `Downloads` gibi bir dizin adını parametre olarak verebilir ve Downloads klasörünüzün içeriğini listeleyebilirsiniz.

`ls` komutu, ek bilgiler listeleyen seçenekleri de destekler.

Diyelim ki şu anda `documents` klasörünüzde çalışıyorsunuz ve bu dizin içindeki dosyalar hakkında daha fazla bilgi istiyorsunuz. Bu durumda `ls` komutunu `-l` seçeneğiyle kullanabilirsiniz; bu, alt dosya ve dizinleri daha uzun ve daha ayrıntılı bir biçimde gösterir.

Terminalin tüm alt dosya ve dizinleri; izinler, son değiştirilme tarihi ve sahibi gibi ek ayrıntılarla birlikte listelediğini görebilirsiniz.

---

## 📍 `pwd` – Geçerli Çalışma Dizinini Yazdırma

Bazen şu anda hangi dizinde çalıştığınızı bilmeniz gerekebilir. Bu durumlarda, geçerli çalışma dizininizi öğrenmek için *“print working directory”* komutunu kullanabilirsiniz.

Komutu kullanmak için komut satırına şunu yazın:

```bash
pwd
```

Burada, şu anda ev dizininizde `/Users/me` içinde çalıştığınızı görebilirsiniz.

---

## 📁 `cd` – Çalışma Dizinini Değiştirme

Geçerli çalışma dizininizi değiştirmek istiyorsanız *“change directory”* komutunu kullanabilirsiniz.

*“change directory”* ya da `cd` komutu, üzerinde çalıştığınız dizini değiştirmek için kullanılır.

Diyelim ki ev dizininizdesiniz ve bunun içindeki bir alt dizine, örneğin `Documents` klasörüne geçmek istiyorsunuz. Çalışma dizininizi değiştirmek için sadece şunu yazın:

```bash
cd Documents
```

Şimdi `pwd` komutunu girerseniz, artık `Documents` alt dizininizde çalıştığınızı görebilirsiniz.

---

## 🧭 Göreli ve Mutlak Yollar ile `cd`

`cd` komutu, dizinleri hem göreli ( *relative* ) hem de mutlak ( *absolute* ) yollar kullanarak değiştirmenize olanak tanır.

Diyelim ki `Documents` dizin ağacınızın içindeki `Notes` klasöründesiniz. Geçerli klasörünüze göre üst dizine gitmek için, `cd` komutunu göreli yol simgesi `..` ile birlikte argüman olarak kullanın.

```bash
cd ..
```

Artık çalışma dizininiz, `Notes` klasörünüzün doğrudan üst dizini olan `Math` dizinidir.

---

## 🏠 `cd ~` – Ev Dizinine Gitme ve Mutlak Yol

Doğrudan ev klasörünüze gitmek istiyorsanız, `cd` komutunu tilde ( *~* ) simgesiyle birlikte kullanın. Bu sizi ev klasörünüze götürecektir.

Bu durumda, tilde simgesi ev dizinine giden bir mutlak yolu temsil eder.

Son olarak, bir dizine tam yol ( *full path* ) da verebilirsiniz. Burada, orijinal `Notes` dizini için mutlak yol adından bahsediyorsunuz.

Bekleneceği üzere, bu komut sizi başlangıçta bulunduğunuz `Notes` klasörüne geri götürecektir.

---

## 🔍 `find` – Dosya Aramak

Son olarak, `find` komutu, kullanıcı tarafından belirtilen bir ölçüte uyan her dosyanın yolunu döndüren güçlü bir araçtır.

Diyelim ki `Documents` klasörünüz, gösterildiği gibi, her birinde birkaç dosya bulunan iki alt klasöre sahip bir dosya yapısına sahip.

`Documents` klasörünüzde çalıştığınızı ve çalışma dizininiz içinde adı `a.txt` olan tüm dosyaların yollarını bulmak istediğinizi varsayalım. Bunu yapmak için şu komutu yazın:

```bash
find . -name 'a.txt'
```

Buradaki `.` argümanı *“burada ara”* anlamına gelir, bu yüzden komut yalnızca geçerli çalışma dizininiz içinde arama yapacaktır.

Aramanızın büyük/küçük harfe duyarsız ( *case-insensitive* ) bir sürümünü gerçekleştirmek için bunun yerine `-iname` seçeneğini kullanabilirsiniz.

```bash
find . -iname 'a.txt'
```

Bu durumda, aynı dosyayı ve ayrıca ismi aynı olan fakat `A` harfi büyük yazılmış başka bir dosyayı bulduğununuzu görürsünüz.

---

## ✅ Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* `ls` komutu, belirtilen bir dizin ağacının içinde yer alan tüm dosya ve dizinleri listeler.
* `cd` komutu, dizinler arasında gezinmek için kullanılır.
* Göreli yollar ( *relative paths* ), geçerli çalışma dizininize göredir; mutlak yollar ( *absolute paths* ) ise bağımsız olarak tek başlarına geçerlidir.
* `find` komutu, dizinlerinizdeki dosyaları bulmak için kullanılır.
