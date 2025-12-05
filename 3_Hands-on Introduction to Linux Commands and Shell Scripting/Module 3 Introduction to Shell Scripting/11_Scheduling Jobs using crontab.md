# ⏱️ crontab Kullanarak İş Zamanlama için Uygulamalı Laboratuvar

## 🎯 Amaçlar

Bu laboratuvarı tamamladıktan sonra şunları yapabileceksiniz:

* Mevcut cron işlerini listelemek
* Bir cron işi eklemek
* Cron işlerini kaldırmak

---

## 💻 Skills Network Cloud IDE Hakkında

*Skills Network Cloud IDE* (Theia ve Docker tabanlı), kurs ve projelere ait uygulamalı laboratuvarlar için bir ortam sağlar.

 *Theia* , masaüstünde veya bulutta çalıştırılabilen, açık kaynaklı bir IDE’dir ( *Integrated Development Environment* ).

Bu laboratuvarı tamamlamak için, Docker konteynerinde çalışan Theia tabanlı Cloud IDE’yi kullanacağız.

---

## ⚠️ Bu Laboratuvar Ortamı Hakkında Önemli Not

Bu laboratuvar ortamındaki oturumların kalıcı olmadığını lütfen unutmayın.

Bu laboratuvar ortamına her bağlandığınızda, sizin için yeni bir ortam oluşturulur. Önceki oturumda kaydetmiş olabileceğiniz verilerin tümü kaybolur.

Veri kaybını önlemek için, bu laboratuvarları tek bir oturumda tamamlamayı planlayın.

---

## 🧩 Alıştırma 1 – crontab Dosyası Söz Dizimini Anlama

 **Cron** , belirlenmiş zamanlarda arka planda istenen görevleri yürütmek için kullanılan bir sistem  *daemon* ’ıdır.

Bir **crontab** dosyası, belirli zamanlarda çalıştırılması amaçlanan komutların listesini içeren basit bir metin dosyasıdır. `crontab` komutu kullanılarak düzenlenir.

Bir crontab dosyasındaki her satır:

* beş adet zaman ve tarih alanı,
* ardından bir komut,
* ardından bir satır sonu karakteri (`\n`)

içerir. Alanlar boşluklarla ayrılır.

Beş zaman/tarih alanı boşluk içeremez ve izin verilen değerleri aşağıdaki gibidir:

| Alan    | İzin verilen değerler                     |
| ------- | ------------------------------------------- |
| minute  | 0–59                                       |
| hour    | 0–23,`0`= gece yarısı ( *midnight* ) |
| day     | 1–31                                       |
| month   | 1–12                                       |
| weekday | 0–6,`0`= Pazar ( *Sunday* )            |

---

## 📋 Alıştırma 2 – Cron İşlerini Listeleme

Menü çubuğundan **Terminal → New Terminal** seçeneğini tıklayarak yeni bir terminal açın.

Bu, ekranın altında yeni bir terminal penceresi açacaktır.

Yeni açılan terminalde aşağıdaki komutları çalıştırın.

`crontab` komutunun `-l` seçeneği, geçerli crontab’ı yazdırır.


```bash
crontab -l 
```

Crontab’iniz boşsa, `no crontab for theia` mesajını alabilirsiniz.

---

## 🛠️ Alıştırma 3 – crontab Dosyasına Bir İş Ekleme

### 3.1 🧾 crontab’e Bir İş Ekleyin

Bir cron işi eklemek için aşağıdaki komutu çalıştırın:

1

```bash
crontab -e
```

Bu komut, (eğer henüz yoksa) sizin için yeni bir crontab dosyası oluşturur. Artık yeni bir cron işi eklemeye hazırsınız.

Crontab dosyanız, aşağıdaki görüntüde olduğu gibi bir düzenleyicide açılacaktır:

<resim gelecek bek kendim eklecegim >

Ok tuşlarını kullanarak dosyanın sonuna kadar aşağı kaydırın:

<resim gelecek bek kendim eklecegim >

Crontab dosyasının sonuna aşağıdaki satırı ekleyin:

```bash
1 0 21 * * * echo "Welcome to cron" >> /tmp/echo.txt
```

<resim gelecek bek kendim eklecegim >

Yukarıdaki iş, dakika 0 ve saat 21 olduğunda `echo` komutunun çalıştırılmasını belirtir. Bu, işin her gün saat 21.00’de (akşam 9.00’da) çalışacağı anlamına gelir.

Komutun çıktısı `/tmp/echo.txt` dosyasına gönderilmelidir.

Değişiklikleri kaydetmek için **Ctrl + x** tuşlarına basın.

Onaylamak için `y` tuşuna basın.

<resim gelecek >

Düzenleyiciden çıkmak için **Enter** tuşuna basın.

Aşağıdaki komutu çalıştırarak işin crontab’e eklenip eklenmediğini kontrol edin:


```bash
crontab -l
```

Çıktıda yeni eklenen işi görmelisiniz.

<resom gelecek >

---

### 3.2 📜 Bir Kabuk Betiğini Zamanlama

Şimdi, geçerli zamanı ve geçerli disk kullanım istatistiklerini yazdıran basit bir kabuk betiği oluşturalım.

**Adım 1:** Laboratuvar ekranındaki menüden **File → New File** seçeneğini kullanarak yeni bir dosya oluşturun.

**Adım 2:** Dosya adını `diskusage.sh` olarak verin ve  **OK** ’e tıklayın.

**Adım 3:** Aşağıdaki komutları kabuk betiğine kaydedin:

```bash
#! /bin/bash
# print the current date time
date
# print the disk free statistics
df -h
```

**Adım 4:** **File → Save** menü seçeneğini kullanarak dosyayı kaydedin.

**Adım 5:** Betiğin çalıştığını doğrulayın:

```bash
chmod u+x diskusage.sh
./diskusage.sh 
```

<resim gelecek >

Betiğin, geçerli zaman damgasını ( *timestamp* ) ve disk kullanım istatistiklerini yazdırması gerekir.

Bu betiği her gün gece yarısı 12:00’de (24 saatlik saatte saat 0 iken) çalışacak şekilde zamanlayalım.

Bu betiğin çıktısının `/home/project/diskusage.log` dosyasının sonuna eklenmesini istiyoruz.

Crontab’i düzenleyin:


```bash
crontab -e
```

Dosyanın sonuna aşağıdaki satırı ekleyin:

```bash
1  0 0 * * * /home/project/diskusage.sh >>/home/project/diskusage.log 
```

Değişiklikleri kaydetmek için **Ctrl + x** tuşlarına basın.

Onaylamak için `y` tuşuna basın.

Düzenleyiciden çıkmak için **Enter** tuşuna basın.

Aşağıdaki komutla işin crontab’e eklenip eklenmediğini kontrol edin:

```bash
1  crontab -l
```

Çıktıda yeni eklenen işi görmelisiniz.

---

## 🗑️ Alıştırma 4 – Geçerli Crontab’i Kaldırma

`-r` seçeneği, geçerli crontab’in kaldırılmasına neden olur.

**Dikkat:** Bu, tüm cron işlerinizi kaldırır. Bu komutu bir üretim sunucusunda kullanırken son derece dikkatli olun.


```bash
crontab -r
```

Crontab’inizin kaldırılıp kaldırılmadığını doğrulayın:


```bash
crontab -l
```

---

## 🧪 Pratik Alıştırmalar

1. Aşağıdaki görevi her dakika çalıştıran bir cron işi oluşturun:

```bash
date >> /tmp/everymin.txt
```

**İpucu için buraya tıklayın**

Crontab söz dizimi açıklamasına bakın.

**Çözüm için buraya tıklayın**

Crontab dosyasını düzenleyin:


```bash
crontab -e
```

Dosyanın sonuna aşağıdaki satırı ekleyin:


```bash
* * * * * date >> /tmp/everymin.txt
```

Dosyayı kaydedin ve düzenleyiciden çıkın.

---

## ✅ Özet

Bu laboratuvarda şunları öğrendiniz:

* `crontab -l` komutunu kullanarak cron işlerini listelemeyi
* `crontab -e` komutunu kullanarak cron işleri eklemeyi
* `crontab -r` komutunu kullanarak geçerli crontab’i kaldırmayı
