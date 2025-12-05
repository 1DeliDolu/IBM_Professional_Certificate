# 🧪 Uygulamalı Lab: Komut Satırında Metin Dosyalarını Düzenleme

## 🧾 Metin Dosyalarını Veri Olarak Düşünmek

Herhangi bir metin dosyasının, potansiyel olarak bir tür veri kümesi olarak yorumlanabileceğini düşünün. Örneğin, metin dosyanız aşağıdakileri içerebilir:

* Bir haber makalesinde veya blog gönderisinde bulabileceğiniz türde metin
* Bir web sayfasını tanımlayan HTML kaynak kodu
* Virgül veya Sekme (Tab) gibi bir ayırıcıyla ayrılmış metin alanlarından oluşan tablo benzeri bir yapı
* Bir şarkıyı veya filmi kodlayan veri akışı
* Tamamen rastgele bir karakter dizisi, örneğin:
  * bir şifreleme anahtarı veya parola
  * sayısallaştırılmış rastgele gürültü dizisi

Metin dosyanız ne olursa olsun, verinizi ihtiyaç duyduğunuz şekilde birleştirmek, düzenlemek, temizlemek ve entegre etmek için temel metin işleme işlemlerini gerçekleştirebilmenizden fayda sağlayabilirsiniz.

---

## 🎯 Öğrenme Hedefleri

Bu labdeki alıştırmalar üzerinde çalışmak, bazı temel ama önemli metin düzenleme ( *text wrangling* ) işlemlerini gerçekleştirmenizi sağlayacaktır.

Bu işlemler, metin dosyalarıyla şunları yapmanıza olanak tanıyacaktır:

* Dosya içeriklerini görüntüleme ve keşfetme
* Metnin ilk veya son **N** satırlarını çıkarma ve görüntüleme
* Metindeki satır, kelime ve karakter sayılarını görüntüleme
* Metin satırlarını (satırları/satırları) sıralama
* Art arda gelen yinelenen metin satırlarını bırakma ( *dropping consecutively duplicated lines* )
* Bir desen eşleşmesi içeren metin satırlarını çıkarma
* Metin satırlarından alanlar çıkarma
* Metin dosyalarını hizalı metin sütunları olarak birleştirme

Bunlar, metin dosyalarını filtrelemenin bazı yapı taşlarıdır. Bu dersin ilerleyen kısımlarında, bu tür işlemleri nasıl birleştireceğinizi öğreneceksiniz. Bu da size, **veri hatları (data pipelines)** adı verilen karmaşık veri işleme akışları oluşturarak verileriniz için gelişmiş görünümler tasarlama gücü kazandıracaktır.

---

## 💻 Skills Network Cloud IDE Hakkında

**Skills Network Cloud IDE** (Theia ve Docker tabanlı), ders ve proje ile ilgili labler için bir uygulamalı lab ortamı sunar.

 **Theia** , masaüstünde veya bulutta çalıştırılabilen açık kaynaklı bir IDE’dir ( *Integrated Development Environment – Tümleşik Geliştirme Ortamı* ).

Bu labi tamamlamak için, Theia tabanlı Cloud IDE’yi kullanacaksınız.

---

## ⚠️ Lab Ortamı Hakkında Önemli Not

Bu lab ortamındaki oturumların **kalıcı** olmadığını lütfen unutmayın.

Bu nedenle, her bağlandığınızda sizin için yeni bir ortam oluşturulur ve önceki bir oturumda kaydetmiş olabileceğiniz veri veya dosyaların tümü kaybolur.

Verilerinizi kaybetmemek için, bu lableri tek bir oturumda tamamlamayı planlayın.

---

## 🧪 Alıştırma 1 – Dosya içeriklerini görüntüleme

Bu alıştırmada, dosya içeriklerini terminal pencerenizde görüntülemek için `cat`, `more` ve `less` komutlarını kullanarak dosya içeriklerini nasıl keşfedeceğinizi öğreneceksiniz.

Başlangıç olarak, varsayılan **home** dizininize, `~` veya `\home\theia` dizinine geçin:

```bash
cd ~
```

`ls` komutunu kullandığınızda, `entrypoint.sh` adlı bir dosya görmelisiniz. `.sh` uzantısı, bir metin dosyasının kabuk betiği ( *shell script* ) olduğunu belirtmek için kullanılan bir kuraldır.

Şimdi bu dosyanın içine bakalım.

---

### 📜 1.1. `cat` komutu ile dosya içeriğini görüntüleme

`cat` komutu, dosyanın içeriğini görüntüler ve aşağıdaki gibi komut istemine geri döner:

```bash
cat entrypoint.sh
```

Bu komut yalnızca dosyanın son kısmını görüntüler; dolayısıyla, dosya terminale sığmayacak kadar uzunsa, içeriğin bir kısmını göremezsiniz.

`cat` komutu, özellikle daha büyük dosyalar için dosya içeriğini görüntülemenin en iyi yolu olmayabilir; ancak kabuk betikleme uygulamaları için oldukça kullanışlıdır.

Örneğin, bir dosyayı başka bir dosyanın sonuna eklemek, yani **birleştirmek (concatenate / append)** için sıklıkla kullanılır.

---

### 📖 1.2. `more` komutu ile dosya içeriğini görüntüleme

Dosya içeriklerini görüntülemek için `cat` komutuna göre daha iyi bir alternatif, `more` komutudur.

Aşağıdaki komutu girerek:

```bash
more entrypoint.sh
```

önce dosyanın üst kısmını görürsünüz.

> İpucu: Bu dosyanın ilk satırı olan `#!/bin/bash` satırına **shebang** denir. Temel olarak, bu shebang satırı, `bash` kabuğunu çağırarak dosyayı bir bash betiği yapar. Shebang satırları hakkında bu dersin ilerleyen bölümlerinde daha fazla bilgi edineceksiniz.

`more` komutunu kullanırken, bir seferde yalnızca terminal pencerenize sığan kadar satır görebilirsiniz.

Dosyanın bir sonraki kısmını görmek için sadece **boşluk (space)** tuşuna basın. Dosyanın sonuna ulaşana kadar bu şekilde, boşluğa basarak sayfa sayfa ilerleyebilirsiniz. Son sayfaya ulaştığınızda, komut istemine geri dönerek çıkarsınız.

Çıkmanın bir başka yolu da sadece `q` yazmaktır; bu komut, `quit` eder ve komut istemine geri döner.

---

### 📜 1.3. `less` komutu ile dosya içinde kaydırma

Peki, yalnızca aşağı değil de, dosya içinde hem yukarı hem aşağı hareket etmek isterseniz ne olur? Bu durumda `less` komutunu kullanabilirsiniz:

```bash
less entrypoint.sh
```

Tıpkı `more` komutunda olduğu gibi, `less` komutu da dosyanın ilk sayfasını görüntüler.

`less` komutunun yararlı yanı, dosyada **Sayfa Yukarı (Page Up)** ve **Sayfa Aşağı (Page Down)** tuşlarını kullanarak sayfa sayfa hareket edebilmenizi sağlamasıdır.

Ayrıca, dosya içinde **Yukarı Ok** ve **Aşağı Ok** tuşlarını (↑ ve ↓) kullanarak satır satır yukarı ve aşağı kaydırma yapabilirsiniz.

`more` komutundan farklı olarak, `less` komutu dosyanın sonuna ulaştığınızda otomatik olarak çıkmaz; dosya içinde gezinmeye devam etme seçeneğiniz olur.

İstediğiniz zaman `q` yazarak çıkabilirsiniz.

---

## 🧪 Alıştırma 2 – Metin dosyası içeriklerini görüntüleme

Bu alıştırmada, metin dosyalarının içeriğini görüntülemek için birkaç komutla daha çalışacaksınız.

Başlamak için aşağıdaki komutları çalıştırın:

```bash
cd /home/project
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt
```

`wget` komutu, verilen URL’den `usdoi.txt` adlı bir metin dosyası indirir. Bu komutu, ağ (networking) komutları bağlamında daha sonra tekrar göreceksiniz.

`ls` komutunu kullanarak, `usdoi.txt` dosyasını başarıyla indirip indirmediğinizi kontrol edebilirsiniz.

---

### 🔝 2.1. `head` komutu ile bir dosyanın ilk N satırını görüntüleme

Varsayılan olarak `head`, bir dosyanın ilk 10 satırını yazdırır.

`usdoi.txt` ile kullanmak için aşağıdakini girin:

```bash
head usdoi.txt
```

Ayrıca yazdırılacak satır sayısını da belirtebilirsiniz.

`usdoi.txt` dosyasının yalnızca ilk 3 satırını yazdırmak için şunu girin:

```bash
head -3 usdoi.txt
```

---

### 🔚 2.2. `tail` komutu ile bir dosyanın son N satırını görüntüleme

Varsayılan olarak `tail`, `usdoi.txt` dosyasının son 10 satırını yazdırır:

```bash
tail usdoi.txt
```

Tıpkı `head` komutunda olduğu gibi, yazdırılacak satır sayısını belirtebilirsiniz.

`usdoi.txt` dosyasının son 2 satırını yazdırmak için aşağıdakini girin:

```bash
tail -2 usdoi.txt
```

---

## 🧪 Alıştırma 3 – Temel metin dosyası istatistikleri alma

### 🔢 3.1. `wc` komutu ile metin dosyasındaki satır, kelime ve karakterleri sayma

`usdoi.txt` gibi bir dosyada satır, kelime ve karakter sayısını bulmak istiyorsanız, aşağıdaki komutu girin:

```bash
wc usdoi.txt
```

Çıktı, sırasıyla:

1. Satır sayısını
2. Kelime sayısını
3. Dosyadaki karakter sayısını

içerir.

Yalnızca `usdoi.txt` dosyasındaki satır sayısını almak için `-l` seçeneğini kullanın:

```bash
wc -l usdoi.txt
```

Benzer şekilde, `usdoi.txt` dosyasındaki kelime sayısı için `-w` seçeneğini kullanın:

```bash
wc -w usdoi.txt
```

`usdoi.txt` dosyasındaki karakter sayısını yazdırmak için `-c` seçeneğini kullanın:

```bash
wc -c usdoi.txt
```

---

## 🧪 Alıştırma 4 – Temel metin düzenleme: satırları sıralama ve tekrarları bırakma

### 🔤 4.1. `sort` komutu ile dosya satırlarını alfasayısal olarak sıralama

Bir dosyanın satırlarını alfasayısal olarak sıralamak için `sort` komutunu kullanabilirsiniz.

`usdoi.txt` dosyasının satırlarını alfasayısal olarak görüntülemek için:

```bash
sort usdoi.txt
```

komutunu girin.

Bu satırları ters sırada görüntülemek için:

```bash
sort -r usdoi.txt
```

komutunu girin.

---

### 🔁 4.2. Art arda gelen yinelenen satırları bırakma ve sonucu `uniq` ile görüntüleme

Önce aşağıdaki dosyayı indirin:

```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/module%201/zoo.txt
```

`zoo.txt` dosyasının ham içeriğini `cat` komutuyla görüntüleyin:

```bash
cat zoo.txt
```

Ardından, `zoo.txt` dosyasının içeriğini, aynı ve **art arda gelen** satırların bırakılmış hâliyle `uniq` komutunu kullanarak görüntüleyin:

```bash
uniq zoo.txt
```

`uniq` komutu, dosyadaki **aynı ve art arda gelen** satırları bırakır. Bu, “tekrarlananları bırakma ( *dropping duplicates* )” olarak bilinene benzer bir işlemdir.

Ancak, bu örnekte görebileceğiniz gibi, tekrar eden satırlar  **hemen peş peşe gelmiyorsa** , dosyada yine de yinelenen satırlar kalabilir.

---

## 🧪 Alıştırma 5 – Temel metin düzenleme: satır ve alan çıkarma

### 🔍 5.1. `grep` komutu ile belirli bir ölçüte uyan satırları çıkarma

`grep` komutu, bir desen ( *pattern* ) belirtmenize ve bir dosyada bu desene uyan satırları aramanıza olanak tanır.

Örneğin, aşağıdaki komut:

```bash
grep people usdoi.txt
```

`usdoi.txt` dosyasında **people** kelimesini içeren tüm satırları yazdırır.

`grep` için sık kullanılan bazı seçenekler şunlardır:

| Seçenek | Açıklama                                                             |
| -------- | ---------------------------------------------------------------------- |
| `-n`   | Eşleşen satırlarla birlikte satır numaralarını da yazdır        |
| `-c`   | Eşleşen satırların sayısını al                                  |
| `-i`   | Eşleştirme sırasında metnin büyük/küçük harf durumunu yok say |
| `-v`   | Deseni içermeyen tüm satırları yazdır                             |
| `-w`   | Desen yalnızca tam kelimeyle eşleşirse eşleştir                   |

Bu seçenekleri kullanarak, `/etc/passwd` dosyasından **login** desenini içermeyen tüm satırları şu komutla yazdırabilirsiniz:

```bash
grep -v login /etc/passwd
```

---

### ✂️ 5.2. `cut` komutu ile metin satırlarından alanlar çıkarma

`cut` komutu, bir dosyadaki her metin satırından yalnızca belirli alanları görmenizi sağlar.

Örneğin, `-c` seçeneği ile her satırın yalnızca ilk iki karakterini görüntülemek için:

```bash
cut -c -2 zoo.txt
```

komutunu kullanabilirsiniz.

Veya her satırı ikinci karakterden itibaren görüntülemek için:

```bash
cut -c 2- zoo.txt
```

komutunu kullanabilirsiniz.

`cut` komutu, **ayrılmış (delimited)** bir dosyadan bir alan çıkarmak için de kullanılabilir.

Bunu göstermek için önce aşağıdaki virgülle ayrılmış dosyayı indirin ve inceleyin:

```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/v4_new_content/labs/names_and_numbers.csv
cat names_and_numbers.csv
```

Şimdi, dosyada listelenen her kişi için yalnızca telefon numaralarını çıkarmak için `-d` (delimiter – ayırıcı) ve `-f` (field – alan) seçeneklerini aşağıdaki gibi kullanabilirsiniz:

```bash
cut -d "," -f2 names_and_numbers.csv
```

Burada:

* `-d ","` komutu, ayırıcının bir **virgül** olduğunu belirtir.
* `-f2` ise ikinci alanın çıkarılacağını belirtir.

---

## 🧪 Alıştırma 6 – Temel metin düzenleme: satırları alanlar olarak birleştirme

### 📎 6.1. `paste` komutu ile metin dosyalarını satır satır, sütunlar hâlinde birleştirme

`paste` komutunu, birden fazla dosyanın satırlarını birleştirmek için kullanın.

Aşağıdaki dosyayı indirin:

```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/module%201/zoo_ages.txt
```

Ardından, iki dosyayı satır satır, sütunlar hâlinde ve varsayılan ayırıcı olarak bir **Tab** karakteri kullanarak birleştirilmiş olarak görmek için:

```bash
paste zoo.txt zoo_ages.txt
```

komutunu kullanın.

Ayırıcıyı değiştirmeyi deneyin. Varsayılan Tab ayırıcı yerine bir **virgül** `,` belirtebilir ve aşağıdaki gibi kullanabilirsiniz:

```bash
paste -d "," zoo.txt zoo_ages.txt
```

---

## 🧪 Pratik Alıştırmalar

Başlamadan önce, aşağıdakini girerek **home** dizininizde çalıştığınızdan emin olun:

```bash
cd ~
pwd
```

---

### 1️⃣ 1. `/etc/passwd` dosyasındaki satır sayısını görüntüleyin.

**İpucu için buraya tıklayın**

`wc` komutunu uygun seçenekle kullanın.

 **Çözüm için buraya tıklayın** :

```bash
wc -l /etc/passwd
```

---

### 2️⃣ 2. `/var/log/bootstrap.log` dosyasında "not installed" ifadesini içeren satırları görüntüleyin.

**İpucu için buraya tıklayın**

`grep` komutunu kullanın.

 **Çözüm için buraya tıklayın** :

```bash
grep "not installed" /var/log/bootstrap.log
```

---

### 3️⃣ 3. `https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/top-sites.txt` adresindeki metin dosyası, popüler web sitelerinin bir listesini içerir. Listede **"org"** kelimesi geçen tüm web sitelerini bulun.

**İpucu için buraya tıklayın**

Dosyayı indirmek için `wget` komutunu kullanın.

Aramak için `grep` komutunu kullanın.

 **Çözüm için buraya tıklayın** :

```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/top-sites.txt
grep org top-sites.txt
```

 **Alternatif Çözüm** :

```bash
curl -o top-sites.txt https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/top-sites.txt
grep org top-sites.txt
```

---

### 4️⃣ 4. `top-sites.txt` dosyasının ilk yedi satırını yazdırın.

**İpucu için buraya tıklayın**

`head` komutunu doğru argümanlarla kullanın.

 **Çözüm için buraya tıklayın** :

```bash
head -n 7 top-sites.txt
```

---

### 5️⃣ 5. `top-sites.txt` dosyasının son yedi satırını yazdırın.

**İpucu için buraya tıklayın**

`tail` komutunu doğru argümanlarla kullanın.

 **Çözüm için buraya tıklayın** :

```bash
tail -n 7 top-sites.txt
```

---

### 6️⃣ 6. `top-sites.txt` dosyasındaki her satırın ilk üç karakterini yazdırın.

**İpucu için buraya tıklayın**

`cut` komutunu doğru argümanlarla kullanın.

 **Çözüm için buraya tıklayın** :

```bash
cut -c -3 top-sites.txt
```

---

### 7️⃣ 7. `names_and_numbers.csv` dosyasından telefon numaraları olmadan yalnızca isimleri çıkarın ve görüntüleyin.

**İpucu için buraya tıklayın**

`names_and_numbers.csv` dosyasının bulunduğu `/home/project` dizinine dönmek için `cd` komutunu kullanın.

`cut` komutunu doğru argümanlarla kullanın.

 **Çözüm için buraya tıklayın** :

```bash
cd /home/project
cut -d "," -f 1 names_and_numbers.csv
```

---

## ✅ Özet

Bu labde şunları öğrendiniz:

* Dosya içeriklerini `cat`, `more` ve `less` komutlarıyla görüntülemek
* Bir dosyanın ilk ve son **N** satırını `head` ve `tail` kullanarak görmek
* Bir dosyadaki satır, kelime ve karakter sayılarını `wc` komutuyla bulmak
* Satırları sıralamak ve tekrarları `sort` ve `uniq` komutlarıyla bırakmak
* Bir dosyadan satır ve alan çıkarmak için `grep` ve `cut` komutlarını kullanmak
* Metin dosyalarını `paste` komutuyla birleştirmek
