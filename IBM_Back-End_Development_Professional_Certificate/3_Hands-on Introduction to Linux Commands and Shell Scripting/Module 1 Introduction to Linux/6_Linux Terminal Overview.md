# 🖥️ Linux Terminaline Genel Bakış

Linux Terminaline Genel Bakış'a hoş geldiniz.

## 🎯 Hedefler

Bu videoyu izledikten sonra şunları yapabileceksiniz:

Linux shell'in ne olduğunu açıklamak. Bir Linux terminalinin ne olduğunu açıklamak. Bir Linux terminali ile shell'in birlikte nasıl çalıştığını açıklamak. Ve dizinlerde gezinebilmek için bir Linux terminalini kullanmak.

---

## 🐚 Linux Shell ve Terminal

Linux shell, komutları yorumlayan, işletim sistemi seviyesinde bir uygulamadır. Unix ve Linux'un erken sürümlerinde, işletim sistemiyle etkileşim kurmanın tek yolu shell'di. Bugün grafiksel kullanıcı arayüzlerini de kullanabilirsiniz, ancak shell hâlâ popüler ve esnek bir seçenek olmaya devam eder ve betik dosyalarını çalıştırmanın kolay bir yoludur.

Shell komutlarını; dosyaları taşımak ve kopyalamak, dosyalara yazmak ve dosyalardan okumak, veriyi çıkarmak ve filtrelemek ve veri aramak gibi görevleri yerine getirmek için kullanabilirsiniz. Birçok shell sürümü vardır, ancak çoğunun temel işlevselliği aynıdır. Bazı popüler örnekler şunlardır: Bash ve Zsh.

Linux shell ile bir Linux terminali üzerinden etkileşim kurarsınız. Terminal, çalıştırmak istediğiniz komutları girdiğiniz ve bu komutlardan gelen çıktıyı aldığınız bir uygulama ya da kullanıcı arayüzüdür.

Örneğin, Python uygulamasını başlatmak ve **myprogram.py** adlı bir programı çalıştırmak için `python` boşluk `myprogram.py` yazın. Enter tuşuna bastığınızda, shell komutu çalıştırır. Bu program, terminale “Hello, World!” sözcüklerini yazdırır.

```bash
python myprogram.py
```

---

## ⚙️ Komutlar Nasıl Çalıştırılır?

Peki komutlar nasıl çalıştırılır? Önce, bir komut çalıştırmak isteyen bir kullanıcı vardır. Bu kullanıcı komutu bir terminale girer ve komut daha sonra shell'e iletilir.

İşletim sisteminin çekirdek bileşenleri ve kernel, komutu donanımın yerine getirebileceği bir biçime çevirir. Donanım komutu tamamladığında, kernel yapılan değişiklikleri veya sonuçları okur ve bunları kullanıcıya bilgi vermek için shell aracılığıyla terminale geri gönderir.

Terminal, uygulamaları çalıştırmanın ve makinenizle etkileşim kurmanın güçlü bir yoludur. Çoğu terminal, komut girmeniz için benzer bir kullanıcı arayüzüne sahiptir.

---

## ⌨️ Komut Satırı, Komut İstemi ve Çalışma Dizinleri

Komutları girdiğiniz alan, komut satırı olarak adlandırılır. Ve dikey çizgi, yani imleç, komut istemidir. Bu, yazdığınız metnin nerede görüntüleneceğini gösterir.

Bu örnekte, geçerli çalışma dizini, `home` dizini içindeki `me` dizini içindeki `Documents` dizinidir. Geçerli çalışma dizini, shell'in çalıştırılmasını belirttiğiniz herhangi bir komutu arayacağı konumdur; örneğin, önceki örnekteki Python programı.

Her terminal, geçerli dizininizin tam konumunu veya yolunu ( *path* ) göstermez, bu yüzden bazıları burada yalnızca `Documents` ifadesini görüntüler. Yol ( *path* ), Linux dosya sisteminde bir dizinin veya dosyanın insan tarafından okunabilir konumudur.

---

## 📁 Yollar ve Özel Semboller

`a/b` yapısı, `b` adlı dosya veya dizinin, `a` adlı dizinin içinde bulunduğunu gösterir.

Ayrıca özel yollar da vardır: Tek bir tilde (`~`) sembolü, kullanıcının *home* dizinine karşılık gelir. Bir yolun başındaki tek bir eğik çizgi (`/`), *root* dizinine karşılık gelir. İki nokta (`..`), geçerli dizinin üst dizinine karşılık gelir. Ve tek bir nokta (`.`), geçerli dizine karşılık gelir.

O hâlde, geçerli çalışma dizinini değiştirmek için terminali nasıl kullanabileceğinize bakalım. Bunun için, *change directory* ifadesinin kısaltması olan `cd` komutunu kullanırsınız.

![1764864465577](image/6_LinuxTerminalOverview/1764864465577.png)

---

## 📂 `cd` Komutu ile Dizin Değiştirme

`root` dizinine gitmek için `cd /` girin. Ve `bin` dizinine geçmek için `cd bin` girin.

```bash
cd /
cd bin
```

`root` içinde bulunan `bin` dizini, sistem tarafından gereken programları içerir. Bu programlardan, yani çalıştırılabilir dosyalardan birinin adı `ls`'dir.

Geçerli çalışma dizininde `./ls` yazarak `ls` programını çalıştırabilirsiniz. Bunu, geçerli dizin içindeki tüm dosya ve dizinlerin adlarını terminal penceresinde görüntülemek için kullanın.

```bash
./ls
```

`bin` klasöründe bulunan birçok komut aynı zamanda shell'in içine gömülüdür, bu nedenle onları başka konumlardan da çalıştırabilirsiniz.

`cd ~` kullanarak *home* dizininize gidin. Ve geçerli çalışma dizini olan `/home/me` `ls` programını içermese bile, komutu yine de başarıyla çalıştırabilirsiniz.

```bash
cd ~
```

![1764864538959](image/6_LinuxTerminalOverview/1764864538959.png)

---

## 🧭 Daha Fazla Dizin Gezinme Örneği

Biraz daha örneğe bakalım. Yine `/home` dizininden başlayarak, mevcut geçerli çalışma dizininin üst dizinine geçmek için `cd ..` yazın.

```bash
cd ..
```

Bu nedenle, bu örnekte `/home` dizininin üst dizini `/`, yani *root* dizinidir.

Ardından, `media` dizinindeki `my-usb-drive` adlı bir USB sürücüsüne gitmek için `cd /media/my-usb-drive` yazın.

```bash
cd /media/my-usb-drive
```

Ayrıca, tek bir komutla dizin ağacında yukarı ve aşağı da gezinebilirsiniz. Bunun için, önce `media` dizinine, ardından `root` dizinine kadar yukarı gitmek için `cd ../..` yazın ve sonra `home` dizinindeki `me` dizinindeki `Documents` dizinine aşağı inmek için `/home/me/Documents` yazın.

```bash
cd ../..
/home/me/Documents
```

Komutu göndermek ve `Documents` klasörüne geçmek için Enter tuşuna basın.

`/home/me` dizinine çıkalım, Python uygulamasını başlatalım ve `/home/me` dizininde bulunan **myprogram.py** adlı bir programı çalıştıralım. Bu program, terminal penceresine bir mesaj döndürür.


---

## ✅ Gözden Geçirme

Bu videoda şunları öğrendiniz:

Linux shell, komutları girmek ve bu komutların çıktısını görmek için kullanabileceğiniz, işletim sistemi seviyesinde bir uygulamadır. Shell'e komut göndermek için bir terminal kullanırsınız. Ve Linux dosya sisteminizde gezinmek için `cd` komutunu kullanabilirsiniz.


Şekilde geçen satırları adım adım açalım:

```bash
/home $ cd /
```

* `cd /` : Çalışma dizinini *root* (en üst) dizine geçirir.
* Prompt değişiyor ve başa sadece `/` geliyor.

---

```bash
/ $ cd bin
```

* `cd bin` : Root dizininin içindeki `bin` klasörüne geçer.
* `bin` genelde sistemdeki temel çalıştırılabilir programların bulunduğu dizindir.

---

```bash
/bin $ ./ls
```

* Burada artık `/bin` dizinindeyiz.
* `./ls` komutu: Bulunduğun dizindeki `ls` adlı programı **dosya yolu vererek** çalıştırır.
  * `./` = “şu anki dizin” anlamına gelir.
  * `ls` = dosya ve dizinleri listeleyen program.
* Çıktıda gördüğün `cat`, `cp`, `dash`, `dd`, `echo`, `expr`, `kill`, `ls`, `mv`, `ps`, `rm`, `sh`, `stty`, `tcsh`, `unlink` vs. hepsi `/bin` dizininde bulunan komut/program dosyalarıdır.

---

```bash
/bin $ cd ~
```

* `cd ~` : Kullanıcının *home* (ev) dizinine gider.
* `~` her zaman o anki kullanıcının home dizinini temsil eder (örneğin `/home/me`).

---

```bash
/home/me $
```

* Artık çalışma dizini `/home/me` olmuş.
* Buradan sonra kullanıcı başka komutlar çalıştırabilir; örneğin `ls`, `python myprogram.py` vb.



### 🐱 `cat`

* Açılımı: **con**catenate
* Görevi: Dosya içeriğini ekrana yazdırmak veya birden fazla dosyayı birleştirip tek çıktı almak.
* Örnek:
  ```bash
  cat dosya.txt
  cat a.txt b.txt > birlesik.txt
  ```

---

### 📄 `cp`

* Açılımı: **c**o**p**y
* Görevi: Dosya veya dizin kopyalamak.
* Örnek:
  ```bash
  cp kaynak.txt hedef.txt
  cp -r klasor1 klasor2
  ```

---

### 🐚 `dash`

* Açılımı: **D**ebian **a**lmquist **sh**ell
* Görevi: Hafif, hızlı, POSIX uyumlu bir shell.
* Genellikle `/bin/sh` için varsayılan shell olarak kullanılır (özellikle Debian/Ubuntu tabanlı sistemlerde).
* Son kullanıcıdan çok script çalıştırma tarafında karşına çıkar.

---

### 📦 `dd`

* Açılımı: “data description” olarak geçer.
* Görevi: Çok düşük seviyede kopyalama ve dönüştürme yapar. Disk imajı alma, USB’ye imaj yazma gibi işler için kullanılır.
* **Dikkat:** Yanlış kullanılırsa diski silebilirsin, çok güçlü ve tehlikeli bir araçtır.
* Örnek:
  ```bash
  dd if=ornek.iso of=/dev/sdb bs=4M status=progress
  ```

---

### 🗣️ `echo`

* Görevi: Kendisine verilen metni ekrana (stdout’a) yazdırır. Scriptlerde çok kullanılır.
* Örnek:
  ```bash
  echo "Merhaba Dünya"
  ```

---

### ➗ `expr`

* Açılımı: **expr**ession
* Görevi: Basit aritmetik ve string (metin) işlemleri yapmak için kullanılır (eski tarz).
* Örnek:
  ```bash
  expr 3 + 5
  expr length "merhaba"
  ```

---

### 💀 `kill`

* Görevi: Bir prosese (çalışan programa) sinyal gönderir. En sık kullanımı, bir süreci sonlandırmaktır.
* Varsayılan sinyal `TERM` (15) yani nazikçe sonlandırma isteği.
* Örnek:
  ```bash
  kill 1234        # PID 1234 olan süreci sonlandır
  kill -9 1234     # Zorla öldür (SIGKILL)
  ```

---

### 📂 `ls`

* Açılımı: **l**i**s**t
* Görevi: Bulunduğun dizindeki dosya ve dizinleri listelemek.
* Örnek:
  ```bash
  ls
  ls -l
  ls -la
  ```

---

### 📦➡️📦 `mv`

* Açılımı: **m**o**v**e
* Görevi: Dosya/dizin taşımak veya yeniden adlandırmak.
* Örnek:
  ```bash
  mv eski_ad.txt yeni_ad.txt
  mv dosya.txt /hedef/klasor/
  ```

---

### 🧠 `ps`

* Açılımı: **p**rocess **s**tatus
* Görevi: Sistemde çalışan süreçleri (process) listelemek.
* Örnek:
  ```bash
  ps
  ps aux   # Daha detaylı süreç listesi
  ```

---

### 🗑️ `rm`

* Açılımı: **r**e**m**ove
* Görevi: Dosya veya dizin silmek.
* **Geri dönüş yok** (çöp kutusu yok) — dikkatli kullan.
* Örnek:
  ```bash
  rm dosya.txt
  rm -r klasor/
  rm -rf klasor/   # Çok tehlikeli, her şeyi zorla siler
  ```

---

### 🐚 `sh`

* Açılımı: **sh**ell (Bourne shell / POSIX shell)
* Görevi: Temel, standart shell yorumlayıcısıdır. Genellikle başka bir shell’e (bash, dash vb.) yönlendirilmiş olur.
* Script dosyalarını çalıştırmak için sık kullanılır:
  ```bash
  sh script.sh
  ```

---

### 🎛️ `stty`

* Açılımı: **s**et **tty**
* Görevi: Terminalin (TTY) ayarlarını görmek ve değiştirmek. Örneğin satır düzenleme, kontrol tuşları gibi.
* Örnek:
  ```bash
  stty -a   # Mevcut tüm terminal ayarlarını göster
  ```

---

### 🐚 `tcsh`

* Açılımı: **T**ENEX **C** **sh**ell
* Görevi: C shell (`csh`)’in geliştirilmiş bir sürümüdür. Farklı özellikleri olan alternatif bir shell.
* Genellikle interaktif kullanım için tercih edilir (otomatik tamamlama vb. ek özellikler).

---

### 🔗 `unlink`

* Görevi: Tek bir dosyayı dosya sisteminden kaldırmak için kullanılan düşük seviye komut. Esasında sistem çağrısı olan `unlink()` fonksiyonunu doğrudan çağırır.
* `rm` ile çok benzerdir ama seçenekleri yoktur ve genelde tek dosya için kullanılır.
* Örnek:
  ```bash
  unlink dosya.txt
  ```

---

Bunların hepsi, sistemin temel işlevleri için gerekli “çekirdek” komut/programlar olduğu için `/bin` içinde tutulur. İstersen sıradaki merak ettiğin komutların çıktısını beraber inceleyebiliriz.
