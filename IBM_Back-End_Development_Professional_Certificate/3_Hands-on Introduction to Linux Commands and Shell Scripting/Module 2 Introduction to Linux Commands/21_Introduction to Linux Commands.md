# 🧾 Modül 2 Hızlı Başvuru Kılavuzu – Linux Komutlarına Giriş

---

## ℹ️ Bilgi Alma

**Kullanıcı adınızı döndürün:**

```bash
whoami
```

**Kullanıcı ve grup kimliğinizi (ID) döndürün:**

```bash
id
```

**İşletim sistemi adını, kullanıcı adını ve diğer bilgileri döndürün:**

```bash
uname -a
```

**Bir komutun başvuru kılavuzunu görüntüleyin:**

```bash
man top
```

**Her komut için kısa bir açıklama içeren, mevcut tüm *man* sayfalarını listeleyin:**

```bash
man -k .
```

**Herhangi bir komut hakkında yardım alın (örneğin: `curl`):**

```bash
curl --help
```

Bu, `curl` komutunun kullanımına ve seçeneklerine dair kısa bir genel bakış sunar.

**Geçerli tarih ve saati döndürün:**

```bash
date
```

---

## 📂 Dizinlerde Gezinme ve Onlarla Çalışma

**Dosya ve dizinleri tarihe göre, en yenisi en sonda olacak şekilde listeleyin:**

```bash
ls -lrt
```

**Dizin ağacında `.sh` ile biten dosyaları bulun:**

```bash
find -name "*.sh"
```

**Geçerli çalışma dizininizin yolunu döndürün:**

```bash
pwd
```

**Yeni bir dizin oluşturun:**

```bash
mkdir new_folder
```

---

### 🔁 Geçerli Dizini Değiştirme

**Bir seviye yukarı çıkın:**

```bash
cd ../
```

**Ev dizinine ( *home* ) gidin:**

```bash
cd ~
```

veya

```bash
cd
```

**Başka bir dizine gidin:**

`path_to_directory` dizinine geçmek için:

```bash
cd path_to_directory
```

**Bir dizini ayrıntılı ( *verbose* ) biçimde kaldırın:**

```bash
rmdir temp_directory -v
```

---

## 📊 Sistem Performansını ve Durumunu İzleme

**Çalışan süreçlerin ve PID’lerinin bir seçimini/tamamını listeleyin:**

```bash
ps
```

```bash
ps -e
```

**Kaynak kullanımını görüntüleyin:**

```bash
top
```

**Bağlı dosya sistemlerini ve kullanım durumlarını listeleyin:**

```bash
df
```

---

## 🧱 Dosya Oluşturma, Kopyalama, Taşıma ve Silme

**Boş bir dosya oluşturun veya mevcut bir dosyanın zaman damgasını güncelleyin:**

```bash
touch a_new_file.txt
```

**Bir dosyayı kopyalayın:**

```bash
cp file.txt new_path/new_name.txt
```

**Bir dosyanın adını veya yolunu değiştirin:**

```bash
mv this_file.txt that_path/that_file.txt
```

**Bir dosyayı ayrıntılı ( *verbose* ) biçimde silin:**

```bash
rm this_old_file.txt -v
```

---

## 🔐 Dosya İzinleriyle Çalışma

**Tüm kullanıcılar için dosya izinlerini “çalıştırılabilir” ( *execute* ) olacak şekilde değiştirin/düzenleyin:**

```bash
chmod +x my_script.sh
```

**Yalnızca sizin, yani geçerli kullanıcının, “çalıştırma” iznini alacak şekilde dosya izinlerini değiştirin/düzenleyin:**

```bash
chmod u+x my_file.txt
```

**Gruptan ve diğer kullanıcılardan “okuma” ( *read* ) iznini kaldırın:**

```bash
chmod go-r
```

---

## 📜 Dosya ve Dizge (String) İçeriklerini Görüntüleme

**Dosya içeriğini görüntüleyin:**

```bash
cat my_shell_script.sh
```

**Dosya içeriğini sayfa sayfa görüntüleyin:**

```bash
more ReadMe.txt
```

**Bir dosyanın ilk 10 satırını görüntüleyin:**

```bash
head -10 data_table.csv
```

**Bir dosyanın son 10 satırını görüntüleyin:**

```bash
tail -10 data_table.csv
```

**Bir dizgeyi veya değişken değerini görüntüleyin:**

```bash
echo "I am not a robot"
echo "I am $USERNAME"
```

---

## ✂️ Temel Metin İşleme ( *Text Wrangling* )

### 🔤 Satırları Sıralama ve Yinelenenleri Atma

**Bir dosyanın satırlarını alfabetik/alfa-sayısal ( *alphanumerically* ) olarak sıralayıp görüntüleyin:**

```bash
sort text_file.txt
```

**Ters sırada:**

```bash
sort -r text_file.txt
```

**Art arda gelen yinelenen satırları atın ve sonucu görüntüleyin:**

```bash
uniq list_with_duplicated_lines.txt
```

---

### 📊 Temel İstatistikleri Görüntüleme

**Bir dosyadaki satır, kelime veya karakter sayılarını görüntüleyin:**

**Satır sayısı:**

```bash
wc -l table_of_data.csv
```

**Kelime sayısı:**

```bash
wc -w my_essay.txt
```

**Karakter sayısı:**

```bash
wc -m some_document.txt
```

---

## 🔍 Belirli Bir Deseni İçeren Satırları Çıkarma

`grep` komutu için sık kullanılan bazı seçenekler:

| Seçenek | Açıklama                                                          |
| -------- | ------------------------------------------------------------------- |
| `-n`   | Eşleşen satırlarla birlikte satır numaralarını yazdır        |
| `-c`   | Eşleşen satırların sayısını al                               |
| `-i`   | Eşleştirme yaparken metnin büyük/küçük harf durumunu yok say |
| `-v`   | Deseni içermeyen tüm satırları yazdır                          |
| `-w`   | Yalnızca desen tüm kelimeyle eşleşiyorsa eşleştir             |

**“hello” kelimesini içeren satırları, büyük/küçük harfe duyarsız ve yalnızca tam kelime eşleşmesi olacak şekilde çıkarın:**

```bash
grep -iw hello a_bunch_of_hellos.txt
```

**Geçerli dizindeki `.txt` ile biten tüm dosyalardan, “hello” desenini içeren satırları çıkarın:**

```bash
grep -l hello *.txt
```

---

## 📎 Dosyaları Satır Satır Birleştirme

**İki veya daha fazla dosyayı satır satır, sütunlar halinde hizalayarak birleştirin:**

Diyelim ki müşterilerinizin adlarını ve soyadlarını içeren, ayrıca telefon numaralarını barındıran üç dosyanız var.

**Her müşteri için bir satır olacak şekilde, dosya içeriklerini sekme ( *Tab* ) ile ayrılmış bir tabloya hizalamak için `paste` kullanın:**

```bash
paste first_name.txt last_name.txt phone_number.txt
```

**Varsayılan sekme ( *Tab* ) ayıracı yerine virgül kullanın:**

```bash
paste -d "," first_name.txt last_name.txt phone_number.txt
```

---

## 🔪 Tablo Benzeri Dosyalardan Sütun Çekme – `cut` Kullanımı

Diyelim ki satırları, virgülle ayrılmış müşteri ad ve soyadlarından oluşan bir metin dosyanız var.

**İlk adları satır satır çıkarın:**

```bash
cut -d "," -f 1 names.csv
```

**Bir dosyanın her satırından, ikinci ile beşinci karakterleri (baytları) çıkarın:**

```bash
cut -b 2-5 my_text_file.txt
```

**Bir dosyanın her satırından, 10. bayttan satır sonuna kadar olan karakterleri çıkarın:**

```bash
cut -b 10- my_text_file.txt
```

---

## 📦 Sıkıştırma ve Arşivleme

**Bir dizi dosyayı arşivleyin:**

```bash
tar -cvf my_archive.tar.gz file1 file2 file3
```

**Bir dizi dosyayı sıkıştırın:**

```bash
zip my_zipped_files.zip file1 file2
zip my_zipped_folders.zip directory1 directory2
```

**Sıkıştırılmış bir zip arşivinden dosyaları çıkarın:**

```bash
unzip my_zipped_file.zip
unzip my_zipped_file.zip -d extract_to_this_direcory
```

---

## 🌐 Ağ Komutlarıyla Çalışma

**Ana makine adını yazdırın:**

```bash
hostname
```

**Bir URL’ye paket gönderin ve yanıtı yazdırın:**

```bash
ping www.google.com
```

Kopyalandı!

Satır kaydırma geçişi yapıldı ( *Wrap Toggled!* ).

**Sistem ağ arayüzlerini görüntüleyin veya yapılandırın:**

```bash
ip
```

**Bir URL’deki dosyanın içeriğini görüntüleyin:**

```bash
curl <url>
```

**Bir URL’den dosya indirin:**

```bash
wget <url>
```
