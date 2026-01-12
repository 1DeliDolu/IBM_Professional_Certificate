# 🧾 Kapsamlı Kopya Kâğıdı – Linux Komutlarına ve Kabuk Betiklemeye Uygulamalı Giriş

---

## 🐧 Linux’a Giriş

| Komut                   | Sözdizimi                        | Açıklama                                             | Örnek                      |
| ----------------------- | --------------------------------- | ------------------------------------------------------ | --------------------------- |
| List                    | `ls [OPTIONS] [FILE/DIRECTORY]` | Belirtilen yoldaki dosya ve dizinleri listeler         | `ls /home/user/documents` |
| Print Working Directory | `pwd`                           | Geçerli çalışma dizinini yazdırır                | `pwd`                     |
| Change Directory        | `cd [DIRECTORY]`                | Geçerli dizini değiştirir                           | `cd /home/user/documents` |
| Super user do           | `sudo [COMMAND]`                | Komutu süper kullanıcı yetkileriyle çalıştırır | `sudo apt update`         |
| Text Editor             | `nano [FILE]`                   | Dosyayı Nano metin editörü ile açar                | `nano myfile.txt`         |

---

## 💻 Linux Komutlarına Giriş

### 📊 Bilgi, Gezinme ve Yönetim Komutları

| Komut                     | Sözdizimi                              | Açıklama                                              | Örnek                                 |
| ------------------------- | --------------------------------------- | ------------------------------------------------------- | -------------------------------------- |
| Who Am I                  | `whoami`                              | Kullanıcı adını döndürür                         | `whoami`                             |
| User ID                   | `id`                                  | Geçerli kullanıcı veya grup ID’sini döndürür     | `id`                                 |
| System Information        | `uname [OPTIONS]`                     | Sistem bilgilerini gösterir                            | `uname -a`                           |
| Manual Pages              | `man [COMMAND]`                       | Bir komut için kılavuz sayfasını gösterir          | `man ls`                             |
| Curl                      | `curl [OPTIONS] [URL]`                | Sunucuya/veriden veri aktarır                          | `curl https://some_website.com`      |
| Date                      | `date [OPTIONS]`                      | Geçerli tarih ve saati gösterir                       | `date`                               |
| Find                      | `find [DIRECTORY] [OPTIONS]`          | Belirtilen yoldaki dosya ve dizinleri bulur             | `find /home/user -name '*.txt'`      |
| Make Directory            | `mkdir [DIRECTORY]`                   | Yeni dizin oluşturur                                   | `mkdir myfolder`                     |
| Remove Directory          | `rmdir [DIRECTORY]`                   | Boş dizini siler                                       | `rmdir myfolder`                     |
| Process Status            | `ps [OPTIONS]`                        | Süreç durum bilgilerini gösterir                     | `ps -ef`                             |
| Table of Processes        | `top`                                 | Canlı sistem kaynak kullanımını gösterir           | `top`                                |
| Disk Usage                | `df [OPTIONS] [FILESYSTEM]`           | Disk alanı kullanımını gösterir                    | `df -h`                              |
| Create Empty File         | `touch [FILE]`                        | Yeni dosya oluşturur veya zaman damgasını günceller | `touch myfile.txt`                   |
| Copy                      | `cp [OPTIONS] [SOURCE] [DESTINATION]` | Dosya veya dizinleri kaynaktan hedefe kopyalar          | `cp myfile.txt /home/user/documents` |
| Move                      | `mv [OPTIONS] [SOURCE] [DESTINATION]` | Dosya ve dizinleri taşır veya yeniden adlandırır    | `mv myfile.txt /home/user/documents` |
| Remove                    | `rm [OPTIONS] [FILE/DIRECTORY]`       | Dosyaları siler                                        | `rm my_scratch_file.txt`             |
| Remove nonempty directory | `rm -r path_to_temp_directory`        | Boş olmayan dizini (özyinelemeli) siler               | `rm -r path_to_temp_directory`       |
| Remove empty directory    | `rmdir [OPTIONS] [DIRECTORY]`         | Boş dizini siler                                       | `rmdir path_to_my_directory`         |
| Change Mode               | `chmod [OPTIONS] [MODE] [FILE]`       | Dosya veya dizin izinlerini değiştirir                | `chmod u+x myfile.txt`               |

---

## 📂 Metin Dosyalarıyla Çalışma, Ağ ve Arşivleme Komutları

| Komut                                              | Sözdizimi                          | Açıklama                                                                           | Örnek                                          |
| -------------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------- |
| Concatenate                                        | `cat [FILE]`                      | Bir dosyanın içeriğini görüntüler                                              | `cat myfile.txt`                              |
| Concatenate and display contents of multiple files | `cat file1 file2`                 | Birden fazla dosyanın içeriğini ardışık gösterir                              | `cat file1 file2`                             |
| More                                               | `more [FILE]`                     | Dosyayı ekran ekran gösterir                                                       | `more myfile.txt`                             |
| Head                                               | `head [OPTIONS] [FILE]`           | Dosyanın ilk N satırını gösterir                                                | `head -5 myfile.txt`                          |
| Tail                                               | `tail [OPTIONS] [FILE]`           | Dosyanın son N satırını gösterir                                                | `tail -5 myfile.txt`                          |
| Echo                                               | `echo [ARGUMENTS]`                | Argümanları konsola yazdırır                                                     | `echo Hello, World!`                          |
| Sort                                               | `sort [OPTIONS] [FILE]`           | Dosya içeriğini alfabetik olarak sıralar                                          | `sort file.txt`                               |
| Unique                                             | `uniq [OPTIONS] [FILE]`           | Dosyadaki ardışık tekrar eden satırları raporlar veya kaldırır                | `uniq file.txt`                               |
| Word Count                                         | `wc [OPTIONS] [FILE]`             | Dosyadaki satır, kelime ve karakter sayısını yazdırır                          | `wc file.txt`                                 |
| Grep                                               | `grep [OPTIONS] PATTERN [FILE]`   | Dosyada belirtilen deseni arar                                                       | `grep "hello" file.txt`                       |
| Paste                                              | `paste [OPTIONS] [FILE1] [FILE2]` | Dosya satırlarını yan yana birleştirir                                           | `paste file1.txt file2.txt`                   |
| Cut                                                | `cut [OPTIONS] [FILE]`            | Dosyadaki her satırdan belirli bölümleri keser                                    | `cut -d":" -f1 /etc/passwd`                   |
| Tar                                                | `tar [OPTIONS] [FILE]`            | Dosyaları tek bir arşiv dosyasında birleştirir                                   | `tar -czvf archive.tar.gz /directory`         |
| Zip                                                | `zip [OPTIONS] [FILE]`            | Dosyaları zip arşivine sıkıştırır                                             | `zip archive.zip file1.txt file2.txt`         |
| Unzip                                              | `unzip [OPTIONS] [FILE]`          | Zip arşivinden dosyaları açar                                                     | `unzip archive.zip`                           |
| Hostname                                           | `hostname`                        | Geçerli ana makinenin adını yazdırır                                            | `hostname`                                    |
| Ping                                               | `ping [OPTIONS] HOSTNAME/IP`      | Bir ağ ana makinesine ICMP ECHO_REQUEST paketleri gönderir                         | `ping google.com`                             |
| ip                                                 | `ip [INTERFACE]`                  | Ağ arayüzü parametrelerini gösterir veya yapılandırır                         | `ip addr`                                     |
| IP                                                 | `ip [OPTIONS]`                    | Yönlendirme, aygıtlar, politika yönlendirme ve tünelleri gösterir veya yönetir | `ip addr`                                     |
| Curl                                               | `curl [OPTIONS] URL`              | Sunucuya/veriden veri aktarır                                                       | `curl https://some_website.com`               |
| Wget                                               | `wget [OPTIONS] URL`              | Web’den dosya indirir                                                               | `wget https://some_website.com/some_file.txt` |

---

## 🐚 Kabuk Betiklemeye Giriş

| Komut              | Sözdizimi                  | Açıklama                                                      | Örnek              |
| ------------------ | --------------------------- | --------------------------------------------------------------- | ------------------- |
| Shebang            | `#!/bin/[shell]`          | Kabuk betiğinin ilk satırı                                   | `#!/bin/bash`     |
| Pipe               | `filter1 \| filter2`       | İstediğin sayıda filtreyi zincirler                          | `ls \| sort -r`    |
| Locate executable  | `which [EXECUTABLE]`      | Bash yürütülebilir dosyasının yerini gösterir             | `which bash`      |
| Bash               | `bash [SCRIPT]`           | Betiği Bash kabuğu ile yorumlayıp çalıştırır            | `bash script.txt` |
| Set                | `set [OPTION]`            | Tüm kabuk değişkenlerini listeler                            | `set`             |
| Define variable    | `[VARIABLE_NAME]=[VALUE]` | Kabuk değişkeni tanımlar ve değer atar                      | `name="John"`     |
| Read               | `read [VARIABLE]`         | Standart girdiden okur ve sonucu değişkende saklar            | `read name`       |
| Env                | `env`                     | Tüm ortam değişkenlerini ve değerlerini yazdırır          | `env`             |
| Export             | `export [VARIABLE]`       | Yerel değişkenin kapsamını tüm alt süreçlere genişletir | `export name`     |
| Crontab            | `crontab [OPTIONS]`       | Varsayılan crontab editörünü açar                          | `crontab -e`      |
| List all cron jobs | `crontab -l`              | Tüm cron görevlerini listeler                                 | `crontab -l`      |

### ⏱️ Cron ile Görev Zamanlama

`cron` artalan sürecini kullanarak görevleri belirli zamanlarda çalışacak şekilde zamanla:

```text
m h dom mon dow command
```

* Her Pazar saat 18:15’te (6:15 pm) tarih/saat bilgisini bir dosyanın sonuna ekle:
  ```bash
  15 18 * * 0 date >> sundays.txt
  ```
* Her Pazartesi saat 03:00’te ev dizinini yedekle:
  ```bash
  0 3 * * 1 tar -cvf my_backup_path\my_archive.tar.gz $HOME\
  ```
* Her ayın ilk gününün ilk dakikasında kabuk betiğini çalıştır:
  ```bash
  1 0 1 * * ./My_Script.sh
  ```
