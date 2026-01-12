# 🧪 Uygulamalı Lab: Dosya ve Dizinlerde Gezinti ve Yönetim

---

## 🎯 Öğrenme Hedefleri

Bu labı tamamladıktan sonra şunları yapabileceksiniz:

* Geçerli çalışma dizininizin konumunu elde etmek
* Bir dizin içindeki dosya ve dizinleri listelemek
* Yeni bir dizin oluşturmak
* Geçerli çalışma dizininizi değiştirmek
* Yeni bir dosya oluşturmak
* Dosyaları aramak ve bulmak
* Bir dosyayı silmek, yeniden adlandırmak, taşımak veya kopyalamak

---

## 💻 Skills Network Cloud IDE Hakkında

Skills Network Cloud IDE (Theia ve Docker tabanlı), kurs ve proje ile ilgili lab’ler için uygulamalı lab ortamı sağlayan bir ortamdır. Theia, masaüstünde veya bulutta çalıştırılabilen açık kaynaklı bir Tümleşik Geliştirme Ortamıdır ( *Integrated Development Environment – IDE* ).

Bu labı tamamlamak için, Theia tabanlı Cloud IDE’yi kullanacaksınız.

---

## ⚠️ Bu Lab Ortamı Hakkında Önemli Uyarı

Lütfen bu lab ortamına ait oturumların kalıcı olmadığını unutmayın.

Bu nedenle, bu lab’a her bağlandığınızda sizin için yeni bir ortam oluşturulur ve önceki oturumda kaydetmiş olabileceğiniz tüm veri veya dosyalar kaybolur.

Verilerinizi kaybetmemek için, bu lab’leri tek bir oturumda tamamlamayı planlayın.

---

## 🧭 Alıştırma 1 – Dosyalarda ve Dizinlerde Gezinti

Bu alıştırmalarda, dosya ve dizinlerde gezinti ve yönetim için komutları kullanma pratiği yapacaksınız.

---

### 📌 1.1. Geçerli Çalışma Dizinini Görüntüleme – `pwd`

Linux terminalinde çalışırken her zaman bir dizin içinde çalışırsınız. Varsayılan olarak, ev dizininizde başlarsınız.

Geçerli çalışma dizininizin mutlak yolunu almak için aşağıdakini girin:

```bash
pwd
```

Bu komut, şu anda çalıştığınız dizinin adını ekrana yazdıracaktır.

---

### 📂 1.2. Bir Dizin İçindeki Dosya ve Dizinleri Listeleme – `ls`

Geçerli dizindeki dosya ve dizinleri listelemek için aşağıdakini girin:

```bash
ls
```

Eğer dizininiz boşsa, `ls` hiçbir şey döndürmez.

Aşağıdaki komut, `/bin` (binaries) dizininizde bulunan birçok ikili ( *binary* ) ve çalıştırılabilir ( *executable* ) dosyayı listeleyecektir:

```bash
ls /bin
```

`/bin` dizini, `ls` ve `pwd` gibi Linux komutlarının saklandığı yerdir. Örneğin, aşağıdakini girerek `ls` komutunun orada bulunduğunu görebilirsiniz:

```bash
ls /bin/ls
```

`/bin` dizininde **b** harfi ile başlayan tüm dosyaları listelemek için şunu deneyin:

```bash
ls /bin/b*
```

**İpucu:** Yıldız `*`, *wildcard* adı verilen özel bir karakterdir. Herhangi bir karakter dizisini temsil etmek için kullanılır.

`/bin` dizininde **r** harfi ile biten tüm dosyaları listelemek için şunu girin:

```bash
ls /bin/*r
```

Son değiştirilme tarihi gibi ek bilgiler içeren daha uzun bir dosya listesi yazdırmak için aşağıdakini girin:

```bash
ls -l
```

#### 📋 `ls` Komutunun Yaygın Seçenekleri

`ls` komutuyla deneyebileceğiniz bazı yaygın seçenekler:

| Seçenek | Açıklama                                                                       |
| -------- | -------------------------------------------------------------------------------- |
| -a       | Gizli dosyalar da dahil olmak üzere tüm dosyaları listele                     |
| -d       | Yalnızca dizinleri listele, dosyaları dahil etme                               |
| -h       | `-l`ve `-s`ile birlikte, boyutları `1K`,`234M`,`2G`şeklinde yazdır  |
| -l       | İzinler, sahip, boyut ve son değiştirilme tarihi gibi öznitelikleri dahil et |
| -S       | Dosya boyutuna göre sırala, en büyük en başta                               |
| -t       | Son değiştirilme tarihine göre sırala, en yeni en başta                     |
| -r       | Sıralama düzenini tersine çevir                                               |

`/etc` dizinindeki tüm dosyaların, gizli olanlar da dahil olmak üzere, uzun bir listesini almak için aşağıdakini girin:

```bash
ls -la /etc
```

Burada, `-l` ve `-a` seçeneklerini, daha kısa gösterim olan `-la` şeklinde birleştirdik.

---

### 📂 2.1. Dizin Oluşturma – `mkdir`

`mkdir` komutu, yeni bir dizin oluşturmak için kullanılır.

Geçerli dizininizde `scripts` adlı bir dizin oluşturmak için şu komutu çalıştırın:

```bash
mkdir scripts
```

`scripts` dizininin oluşturulup oluşturulmadığını doğrulamak için `ls` komutunu kullanın:

```bash
ls
```

`scripts` adlı bir dizinin listelendiğini görmelisiniz.

---

### 🔁 2.2. Geçerli Çalışma Dizinini Değiştirme – `cd`

Geçerli çalışma dizininizi `scripts` dizini olacak şekilde değiştirmek için şu komutu çalıştırın:

```bash
cd scripts
```

Şimdi, geçerli çalışma dizininizin beklendiği gibi değişip değişmediğini doğrulamak için `pwd` komutunu kullanın:

```bash
pwd
```

Ev dizininize geri dönmek için dizin adı belirtmeden `cd` komutunu girebilirsiniz:

```bash
cd
```

Ardından, geçerli çalışma dizininizin değişip değişmediğini doğrulamak için tekrar `pwd` komutunu girin:

```bash
pwd
```

`..` sözdizimi, geçerli dizininizin üst dizinine ( *parent directory* ) başvuran bir kısayoldur. Dizin hiyerarşisinde bir seviye yukarı çıkmak için aşağıdaki komutu çalıştırın:

```bash
cd ..
```

---

### 📄 2.3. Boş Bir Dosya Oluşturma – `touch`

Önce, aşağıdakini girerek ev dizininize geri dönün:

```bash
cd
```

Sonra, `touch` komutunu kullanarak `myfile.txt` adlı boş bir dosya oluşturun:

```bash
touch myfile.txt
```

`myfile.txt` dosyasının oluşturulduğunu doğrulamak için `ls` komutunu kullanın:

```bash
ls
```

Eğer dosya zaten mevcutsa, `touch` komutu dosyanın erişim zaman damgasını veya son değiştirilme tarihini günceller. Bunu görmek için:

```bash
touch myfile.txt
```

komutunu girin ve tarih değişimini doğrulamak için `date` komutunu kullanın:

```bash
date -r myfile.txt
```

---

## 🗂️ Alıştırma 3 – Dosya ve Dizin Yönetimi

---

### 🔎 3.1. Dosyaları Arama ve Bulma – `find`

`find` komutu, bir dizin içinde dosyaları aramak için kullanılır. Dosyaları, dosya adı, türü, sahibi, boyutu veya zaman damgası gibi farklı özniteliklere göre arayabilirsiniz.

`find` komutu, verilen dizin adından başlayarak tüm dizin ağacını tarar.

Örneğin, aşağıdaki komut, `/etc` dizinindeki ve tüm alt dizinlerindeki tüm `.txt` dosyalarını bulur:

```bash
find /etc -name '*.txt'
```

Kopyalandı!

Satır Kaydırma Değiştirildi!

Aşağıdaki komutla `.conf` dosyalarını da arayabilirsiniz:

```bash
find /etc -name '*.conf'
```

**Not:** Terminal, tüm `.txt` dosyalarını listelemenin yanında `"Permission denied"` hataları da döndürebilir.

Bu hatalar normaldir; çünkü lab makinesinde sınırlı erişim izinlerine sahipsiniz.

---

### 🗑️ 3.2. Dosya Silme – `rm`

`rm` komutu, dosyaları silmek için kullanılır. İdeal olarak, her silme işleminden önce onay sormasını sağlayan `-i` seçeneğiyle birlikte kullanılmalıdır.

`myfile.txt` dosyasını silmek için aşağıdaki komutu girin ve silme işlemini onaylamak için `y`, reddetmek için `n` tuşuna basın:

```bash
rm -i myfile.txt
```

Silme işlemini doğrulamak için `ls` komutunu kullanın:

```bash
ls
```

Kopyalandı!

Satır Kaydırma Değiştirildi!

**İpucu:** Sadece tek bir dosyayı `rm` komutuyla siliyorsanız, `-i` seçeneği çok gerekli değildir. Ancak, bir örüntüye ( *pattern* ) uyan tüm dosya adlarını bulmak için *wildcard* kullanarak birden çok dosyayı kaldırmak istediğinizde, her silme işlemine onay vermek veya reddetmek için `-i` seçeneğini eklemek en iyi uygulamadır.

Dosya veya dizinleri silerken dikkatli olun! Silinen bir dosyayı geri getirmek için genellikle bir yol yoktur; çünkü bir çöp klasörü yoktur. Bu nedenle, önemli dosyalarınızı her zaman yedeklemeniz veya arşivlemeniz gerekir. Dosyaları arşivleme hakkında yakında daha fazla şey öğreneceksiniz.

---

### 📦 3.3. Dosya Taşıma ve Yeniden Adlandırma – `mv`

`mv` komutunu, dosyaları bir dizinden başka bir dizine taşımak ve/veya yeniden adlandırmak için kullanabilirsiniz.

Bunu yapmadan önce, `users.txt` adlı yeni bir dosya oluşturalım:

```bash
touch users.txt
```

Bir dosyayı taşırken her zaman dikkatli olmalısınız. Hedef dosya zaten varsa, kaynak dosya tarafından üzerine yazılır (*overwrite* edilir) veya değiştirilir.

Ancak, kaynak ve hedef dizinler aynı olduğunda, `mv` komutunu bir dosyayı yeniden adlandırmak için kullanabilirsiniz.

Bunu göstermek için, aşağıdaki komutu girerek `users.txt` dosyasını `user-info.txt` olarak yeniden adlandırmak için `mv` komutunu kullanın:

```bash
mv users.txt user-info.txt
```

Kopyalandı!

Satır Kaydırma Değiştirildi!

Kaynak ve hedef dizinler aynı olduğu için (geçerli çalışma dizininiz), `mv` komutu dosyayı yeniden adlandıracaktır.

Şimdi, isim değişikliğini doğrulamak için `ls` komutunu kullanın:

```bash
ls
```

Artık `user-info.txt` dosyasını aşağıdaki şekilde `/tmp` dizinine taşıyabilirsiniz:

```bash
mv user-info.txt /tmp
```

Taşıma işlemini doğrulamak için `ls` komutunu iki kez kullanın:

```bash
ls
```

```bash
ls -l /tmp
```

Kopyalandı!

Satır Kaydırma Değiştirildi!

---

### 📄 3.4. Dosya Kopyalama – `cp`

`cp` komutunu, artık `/tmp` dizininde bulunan `user-info.txt` dosyasını geçerli çalışma dizininize kopyalamak için kullanabilirsiniz:

```bash
cp /tmp/user-info.txt user-info.txt
```

Kopyalamanın başarılı olduğunu doğrulamak için `ls` komutunu kullanın:

```bash
ls
```

Kopyalandı!

Satır Kaydırma Değiştirildi!

Bazen var olan bir dosyanın içeriğini yeni bir dosyaya kopyalamak isteyebilirsiniz.

Aşağıdaki komut, `/etc/passwd` dosyasının içeriğini, geçerli dizinde `users.txt` adlı bir dosyaya kopyalar:

```bash
cp /etc/passwd users.txt
```

Tekrar, kopyalamanın başarılı olup olmadığını doğrulamak için `ls` komutunu kullanın:

```bash
ls
```

---

## 🧠 Uygulama Alıştırmaları

1. **`/home` dizininin içeriğini görüntüleyin.**
   *İpucu için buraya tıklayın*

   `ls` komutunu kullanın.
   *Çözüm için buraya tıklayın*

   ```bash
   ls /home
   ```

   Kopyalandı!

   Satır Kaydırma Değiştirildi!

---

2. **Ev dizininizde olduğunuzdan emin olun.**
   *İpucu için buraya tıklayın*

   Ev dizininize geçmek için `cd` komutunu kullanın ve ardından doğrulamak için `pwd` komutunu kullanın.
   *Çözüm için buraya tıklayın*

   ```bash
   cd
   pwd
   ```

---

3. **`tmp` adlı yeni bir dizin oluşturun ve oluşturulduğunu doğrulayın.**
   *İpucu için buraya tıklayın*

   `mkdir` ve `ls` komutlarını kullanın.
   *Çözüm için buraya tıklayın*

   ```bash
   mkdir tmp
   ls
   ```

---

4. **`tmp` dizininde `display.sh` adlı yeni, boş bir dosya oluşturun ve oluşturulduğunu doğrulayın.**
   *İpucu için buraya tıklayın*

   `cd`, `touch` ve `ls` komutlarını kullanın.
   *Çözüm için buraya tıklayın*

   ```bash
   cd tmp
   touch display.sh
   ls -l
   ```

   Kopyalandı!

   Satır Kaydırma Değiştirildi!

---

5. **Aynı dizin içinde `display.sh` dosyasının `report.sh` adlı bir kopyasını oluşturun.**
   *İpucu için buraya tıklayın*

   `cp` komutunu kullanın.
   *Çözüm için buraya tıklayın*

   ```bash
   cp display.sh report.sh
   ```

---

6. **Kopyaladığınız `report.sh` dosyasını, dizin ağacında bir seviye yukarıdaki üst dizine taşıyın. Değişikliklerinizi doğrulayın.**
   *İpucu için buraya tıklayın*

   `mv` ve `ls` komutlarını kullanın ve geçerli çalışma dizininizin üst dizinine göreli yolu gösteren kısayol gösterimini hatırlayın.
   *Çözüm için buraya tıklayın*

   ```bash
   mv report.sh ../
   ls
   ls ../
   ```

---

7. **`display.sh` dosyasını silin.**
   *İpucu için buraya tıklayın*

   `rm` komutunu kullanın.
   *Çözüm için buraya tıklayın*

   ```bash
   rm -i display.sh
   ```

---

8. **`/etc` dizinindeki dosyaları erişim zamanına göre artan sırada listeleyin.**
   *İpucu için buraya tıklayın*

   `ls` komutunu doğru seçeneklerle kullanın.
   *Çözüm için buraya tıklayın*

   ```bash
   ls -ltr /etc/
   ```

---

9. **`/var/log/bootstrap.log` dosyasını geçerli dizininize kopyalayın.**
   *İpucu için buraya tıklayın*

   Dosyayı geçerli dizininize (`.`) kopyalamak için `cp` komutunu kullanın.
   *Çözüm için buraya tıklayın*

   ```bash
   cp /var/log/bootstrap.log .
   ```

---

## ✅ Özet

Bu lab’da, aşağıdaki komutları kullanabileceğinizi öğrendiniz:

* `pwd` – geçerli çalışma dizininizin konumunu almak için
* `ls` – bir dizin içindeki dosya ve dizinleri listelemek için
* `mkdir` – yeni bir dizin oluşturmak için
* `cd` – geçerli çalışma dizininizi değiştirmek için
* `touch` – yeni bir dosya oluşturmak için
* `find` – dosyaları aramak ve bulmak için
* `rm` – bir dosyayı silmek için
* `mv` – bir dosyayı yeniden adlandırmak veya taşımak için
* `cp` – bir dosyayı kopyalamak için
