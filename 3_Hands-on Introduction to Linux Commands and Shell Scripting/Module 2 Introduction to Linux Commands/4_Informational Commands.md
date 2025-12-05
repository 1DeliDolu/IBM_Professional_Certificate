# 🧪 Uygulamalı Lab: Bilgilendirici Komutlar


---

## 🎯 Öğrenme Hedefleri

Bu labı tamamladıktan sonra aşağıdaki komutları kullanarak şunları yapabileceksiniz:

* Sistem ve kullanıcı bilgilerini görüntülemek
* Kullanıcı ve grup kimlik bilgilerini görmek
* Çalışan süreçler ve sistem kaynak kullanımı hakkında bilgi edinmek
* Özel mesajlar görüntülemek
* Geçerli tarih ve saati göstermek
* Bir komutun başvuru kılavuzuna erişmek

---

## 💻 Skills Network Cloud IDE Hakkında

Skills Network Cloud IDE (Theia ve Docker tabanlı), kurs ve proje ile ilgili lab’ler için uygulamalı lab ortamı sağlayan bir ortamdır. Theia, masaüstünde veya bulutta çalıştırılabilen açık kaynaklı bir IDE’dir (*Integrated Development Environment* – Tümleşik Geliştirme Ortamı).

Bu labı tamamlamak için, Theia tabanlı Cloud IDE’yi kullanacaksınız.

---

## ⚠️ Bu Lab Ortamı Hakkında Önemli Uyarı

Lütfen bu lab ortamına ait oturumların kalıcı olmadığını unutmayın.

Bu nedenle, her bağlandığınızda sizin için yeni bir ortam oluşturulur ve önceki oturumda kaydetmiş olabileceğiniz tüm veri veya dosyalar kaybolur.

Verilerinizi kaybetmemek için, bu lab’leri tek bir oturumda tamamlamayı planlayın.

---

## 🧪 Alıştırma 1 – Bilgilendirici Komutlar

Bu alıştırmada, sistem ve kullanıcı bilgileri sağlayan yararlı komutlara alışacaksınız.

---

### 👤 1.1. Geçerli Kullanıcının Adını Görüntüleme

**Komut:** `whoami`

Geçerli kullanıcı adınızı döndürmek için `whoami` komutunu girin.

```bash
whoami
```

Bu komut, kullanıcı adını `theia` olarak gösterecektir; çünkü bu lab’a `theia` kullanıcısı ile giriş yapmış durumdasınız.

Mevcut oturum açmış kullanıcıların listesini `who` komutunu kullanarak alabilirsiniz, ancak bu komut şu anda Theia ortamında çalışmamaktadır.

---

### 🖥️ 1.2. İşletim Sistemi Hakkında Temel Bilgileri Alma

**Komut:** `uname`

Varsayılan olarak komut, çekirdek ( *kernel* ) adını yazdırır. `uname` içindeki `u`, *“unix-like OS”* ifadesine gönderme yapar.

```bash
uname
```

`uname` komutunu girerseniz, çıktıda `Linux` ifadesini görürsünüz.

Tüm sistem bilgilerini yazdırmak için `-a` seçeneğini kullanın:

```bash
uname -a
```

Sistem bilgilerini aşağıdaki sırayla göreceksiniz:

* Çekirdek adı
* Ağ düğümü ( *network node* ) ana bilgisayar adı
* Çekirdek sürümünün yayın tarihi
* Çekirdek sürümü
* Makine donanım adı
* Donanım platformu
* İşletim sistemi

---

### 👥 1.3. Kullanıcı ve Grup Kimlik Bilgilerini Alma

**Komut:** `id`

Bu komut, geçerli kullanıcının kullanıcı kimliği ( *user id – uid* ) ve grup kimliği ( *group id – gid* ) bilgilerini görüntüler.

```bash
id
```

Bu komut, kullanıcı `theia` için `uid` (user id) ve `gid` (group id) değerlerini gösterecektir.

---

### 💾 1.4. Kullanılabilir Disk Alanını Görüntüleme

**Komut:** `df`

`df` komutu, kullanılabilir disk alanını görüntülemek için kullanılır.

```bash
df
```

Bu komut, kullanılabilir disk alanını 512 baytlık bloklar cinsinden gösterecektir.

Kullanılabilir disk alanını “insan tarafından okunabilir” biçimde görmek için şu komutu girin:

```bash
df -h
```

Bu, kullanılabilir disk alanını gigabayt ve terabayt gibi birimlerle döndürecektir.

---

### 🧩 1.5. Çalışan Süreçleri Görüntüleme

**Komut:** `ps`

`ps` komutu, şu anda çalışan her süreci ve bunların süreç kimliklerini ( *PID – process id* ) listeler.

```bash
ps
```

Ancak, çıktı yalnızca size ait süreçleri içerir.

Sistemde çalışan tüm süreçleri görüntülemek için `-e` seçeneğini kullanabilirsiniz. Buna diğer kullanıcılara ait süreçler de dahildir.

```bash
ps -e
```

---

### 📊 1.6. Çalışan Süreçler ve Sistem Kaynakları Hakkında Bilgi Alma

**Komut:** `top`

`top` ( *table of processes* ) komutu, sisteminizin dinamik ve gerçek zamanlı bir görünümünü sağlar.

```bash
top
```

`top` komutu, çekirdek tarafından yönetilen ve şu anda çalışan süreçler veya iş parçacıklarıyla ilgili ayrıntılı bilgilerin yer aldığı bir tablo gösterir. Buna ek olarak, süreç başına CPU ve bellek kullanımıyla ilgili bilgileri de sağlar.

`top` komutunu başlattığınızda, ana `top` ekranında aşağıdaki öğelerle karşılaşırsınız:

* **Özet alanı (Summary area)** – sistem çalışma süresi ( *uptime* ), kullanıcı sayısı, yük ortalaması ( *load average* ) ve genel bellek kullanımı gibi bilgileri gösterir
* **Sütun başlığı (Column header)** – öznitelik adlarını gösterir
* **Görev alanı (Task area)** – her süreç için verileri gösterir (PID – process id)

Çıktı, siz `q` veya `Ctrl + c` tuşlarına basana kadar yenilenmeye devam eder.

Belirli bir yineleme ( *repetition* ) sayısından sonra komuttan otomatik olarak çıkmak isterseniz `-n` seçeneğini şu şekilde kullanın:

```bash
top -n 10
```

`top` çalışırken tabloyu sıralamak için `Shift` tuşu ile birlikte aşağıdaki tuşlara basabilirsiniz:

| Tuş | Sıralama Ölçütü                      |
| ---- | ----------------------------------------- |
| m    | Bellek kullanımı (*Memory* )          |
| p    | CPU kullanımı (*CPU Usage* )          |
| n    | Süreç kimliği (*Process ID – PID* ) |
| t    | Çalışma süresi (*Running Time* )    |

Örneğin, en çok bellek tüketen süreci bulmak için `Shift + m` tuşlarına basabilirsiniz.

---

### 💬 1.7. Mesaj Gösterme

**Komut:** `echo`

`echo` komutu, verilen metni ekranda gösterir. Örneğin, aşağıdaki komutu girdiğinizde:

```bash
echo "Welcome to the linux lab"
```

şu çıktıyı üretir:

```text
Welcome to the linux lab.
```

Bu özel karakterler, çıktınızı daha iyi biçimlendirmenize yardımcı olur:

| Özel Karakter | Etki                   |
| -------------- | ---------------------- |
| `\n`         | Yeni satır başlatır |
| `\t`         | Sekme (*tab* ) ekler |

Özel karakterlerle çalışırken `echo` komutunun `-e` seçeneğini kullanın. Örneğin:

```bash
echo -e "This will be printed \nin two lines"
```

şu çıktıyı verir:

```text
This will be printed
in two lines
```

---

### 🕒 1.8. Tarih ve Saati Görüntüleme

**Komut:** `date`

`date` komutu, geçerli tarih ve saati görüntüler.

```bash
date
```

Bu komutun, geçerli tarih ve saati farklı biçimlerde göstermenizi sağlayan birkaç seçeneği vardır.

Örneğin, aşağıdaki komut geçerli tarihi `aa/gg/yy` ( *mm/dd/yy* ) biçiminde gösterir:

```bash
date "+%D"
```

Deneyebileceğiniz bazı popüler biçim belirteçleri:

| Belirteç | Açıklama                                                       |
| --------- | ---------------------------------------------------------------- |
| `%d`    | Ayın gününü gösterir (01–31)                               |
| `%h`    | Kısaltılmış ay adını gösterir (Jan–Dec)                  |
| `%m`    | Yılın ayını gösterir (01–12)                               |
| `%Y`    | Dört basamaklı yılı gösterir                                |
| `%T`    | Saati 24 saat biçiminde `SS:DD:SS`(HH:MM:SS) olarak gösterir |
| `%H`    | Saati gösterir                                                  |

---

### 📚 1.9. Bir Komutun Başvuru Kılavuzunu Görüntüleme

**Komut:** `man`

`man` komutu, argüman olarak verdiğiniz herhangi bir komutun kullanıcı kılavuzunu ( *user manual* ) görüntüler.

Örneğin, `ls` komutunun kılavuz sayfasını görmek için şunu girin:

```bash
man ls
```

İhtiyacınız olan bilgiyi bulmak için komutun kılavuzunda gezin. İşiniz bittiğinde, çıkmak için `q` tuşuna basın.

Bazen sisteminizde  *man page* ’i olmayan bir komutla karşılaşırsınız. Mevcut tüm *man* sayfalarını ve her komutun kısa açıklamasını görmek için şunu girin:

```bash
man -k .
```

---

## 🧠 Uygulama Alıştırmaları ( *Practice exercises* )

1. **İşletim sistemi hakkında temel bilgileri alın.**
   *İpucu için buraya tıklayın*

   `uname` komutunu kullanın.
   *Çözüm için buraya tıklayın*

   ```bash
   uname
   ```

   Kopyalandı!

   Satır Kaydırma Değiştirildi!

---

2. **Sistemde çalışan tüm süreçleri görüntüleyin.**
   *İpucu için buraya tıklayın*

   Yalnızca size ait olanları değil, tüm süreçleri görmek için `ps` komutunu uygun seçenekle kullanın.
   *Çözüm için buraya tıklayın*

   ```bash
   ps -e
   ```

   Kopyalandı!

   Satır Kaydırma Değiştirildi!

---

3. **Süreç tablosunu alın ve bellek kullanımına göre sıralayın.**
   *İpucu için buraya tıklayın*

   `top` komutunu kullanın, ardından bellek kullanımına göre sıralamak için `Shift + m` tuşlarına basın.
   *Çözüm için buraya tıklayın*

   ```bash
   top
   ```

   Ardından `Shift + m` tuşlarına basın.

---

4. **Geçerli saati görüntüleyin.**
   *İpucu için buraya tıklayın*

   `date` komutunun `%T` biçim seçeneğini kullanın.
   *Çözüm için buraya tıklayın*

   ```bash
   date "+%T"
   ```

   Kopyalandı!

   Satır Kaydırma Değiştirildi!

---

5. **Tek bir komut kullanarak, “Hello!” ve “Goodbye!” mesajlarını yeni satırla ayrılmış şekilde görüntüleyin.**
   *İpucu için buraya tıklayın*

   `echo` komutunu `-e` seçeneği ve `\n` yeni satır karakteri ile kullanın.
   *Çözüm için buraya tıklayın*

   ```bash
   echo -e "Hello! \nGoodbye!"
   ```

---

## ✅ Özet

Bu lab’da, aşağıdaki komutları kullanabileceğinizi öğrendiniz:

* `whoami` – kullanıcı adınızı döndürmek için
* `uname` – çekirdek adını yazdırmak için
* `id` – kullanıcı ve grup kimliklerini görüntülemek için
* `df` – kullanılabilir disk alanını yazdırmak için
* `ps` – çalışan süreçleri ve bunların süreç kimliklerini listelemek için
* `top` – süreçlerin gerçek zamanlı tablosunu görüntülemek için
* `echo` – verilen metni yazdırmak için
* `date` – geçerli tarih ve saati görüntülemek için
* `man` – bir komutun kullanıcı kılavuzuna erişmek için
