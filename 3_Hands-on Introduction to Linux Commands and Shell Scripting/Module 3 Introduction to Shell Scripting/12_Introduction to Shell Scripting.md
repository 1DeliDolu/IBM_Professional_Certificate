# 🧾 Modül 3 Hızlı Başvuru – Kabuk Betiklemeye Giriş

---

## 🐚 Bash Shebang

Bash shebang:


```bash
#!/bin/bash
```

---

## 🧭 Bir Komutun Yolunu Bulma

Bir komutun yolunu al:


```bash
which bash
```

---

## 🚰 Pipes, Filtreler ve Zincirleme (Chaining)

Filtre komutlarını pipe operatörü kullanarak zincirle:


```bash
ls | sort -r
```

`ls` komutunun kılavuz (`man`) çıktısını ilk 20 satırı göstermek için `head` komutuna *pipe* et:


```bash
man ls | head -20
```

Bir CSV dosyasından bir isim sütununu çıkarmak ve yinelenen (duplicate) isimleri atmak için bir *pipeline* kullan:


```bash
cut -d "," -f1 names.csv | sort | uniq
```

---

## 🌍 Kabuk ve Ortam Değişkenleri ile Çalışma

Tüm kabuk değişkenlerini listele:


```bash
set
```

`my_planet` adlı bir kabuk değişkeni tanımla ve değerini `Earth` olarak ata:


```bash
my_planet=Earth
```

Bir kabuk değişkeninin değerini göster:


```bash
echo $my_planet
```

Komut satırında kullanıcı girdisini bir kabuk değişkenine oku:


```bash
read first_name
```

İpucu: Bu komutu çalıştırdıktan sonra girdiğiniz metin dizisi, `first_name` değişkeninin değeri olarak saklanır.

Tüm ortam değişkenlerini listele:


```bash
env
```

Ortam değişkenleri: Değişken kapsamını alt süreçlere ( *child processes* ) tanımla/genişlet:


```bash
export my_planet
export my_galaxy='Milky Way'
```

---

## 🔣 Metakarakterler

Yorumlar `#`:


```bash
# The shell will not respond to this message
```

Komut ayırıcı `;`:


```bash
echo 'here are some files and folders'; ls
```

Dosya adı genişletme joker karakteri `*`:


```bash
ls *.json
```

Tek karakter joker karakteri `?`:


```bash
ls file_2021-06-??.json
```

---

## ✍️ Tırnaklama (Quoting)

Tek tırnaklar `''` – olduğu gibi ( *literally* ) yorumla:


```bash
echo 'My home directory can be accessed by entering: echo $HOME'
```

Çift tırnaklar `""` – olduğu gibi yorumla, ancak metakarakterleri değerlendir:


```bash
echo "My home directory is $HOME"
```

Ters eğik çizgi `\` – metakarakter yorumlamasını kaçır ( *escape* ):


```bash
echo "This dollar sign should render: \$"
```

---

## 🔀 Girdi/Çıktı Yönlendirme (I/O Redirection)

Çıktıyı bir dosyaya yönlendir ve mevcut içeriğin üzerine yaz:


```bash
echo 'Write this text to file x' > x
```

Çıktıyı dosyanın sonuna ekle:


```bash
echo 'Add this line to file x' >> x
```

Standart hatayı bir dosyaya yönlendir:


```bash
bad_command_1 2> error.log
```

Standart hatayı dosyanın sonuna ekle:


```bash
bad_command_2 2>> error.log
```

Dosya içeriğini standart girdiye yönlendir:


```bash
$ tr "[a-z]" "[A-Z]" < a_text_file.txt
```

Yukarıdaki girdi yönlendirme ifadesi, aşağıdakine denktir:


```bash
$cat a_text_file.txt | tr "[a-z]" "[A-Z]"
```

---

## 🔄 Komut Yerine Koyma (Command Substitution)

Bir komutun çıktısını yakala ve değerini echo ile yazdır:


```bash
THE_PRESENT=$(date)
echo "There is no time like $THE_PRESENT"
```

Bir komutun çıktısını yakala ve değerini echo ile yazdır:


```bash
echo "There is no time like $(date)"
```

---

## 💻 Komut Satırı Argümanları


```bash
./My_Bash_Script.sh arg1 arg2 arg3
```

---

## ⏱️ Yığın (Batch) vs. Eşzamanlı (Concurrent) Kipler

Komutları sırayla (ardışık) çalıştır:


```bash
start=$(date); ./MyBigScript.sh ; end=$(date)
```

Komutları paralel çalıştır:


```bash
./ETL_chunk_one_on_these_nodes.sh  & ./ETL_chunk_two_on_those_nodes.sh
```

---

## ⏰ cron ile İş Zamanlama

Crontab düzenleyicisini aç:


```bash
crontab -e
```

İş zamanlama sözdizimi:


```bash
m  h  dom  mon  dow   command
```

*(minute, hour, day of month, month, day of week)*

İpucu: `"any"` (herhangi) anlamına gelmesi için `*` joker karakterini kullanabilirsiniz.

Her Pazar saat 18:15’te tarih/zaman bilgisini bir dosyaya ekle:


```bash
15 18 * * 0 date >> sundays.txt
```

Her ayın ilk gününün ilk dakikasında bir kabuk betiği çalıştır:


```bash
1  0 1 * * ./My_Shell_Script.sh
```

Ev dizinini her Pazartesi saat 3:00’te yedekle:


```bash
0 3 * * 1  tar -cvf my_backup_path\my_archive.tar.gz $HOME\
```

Cron işini devreye al ( *deploy your cron job* ):

Crontab düzenleyicisini kapatın ve dosyayı kaydedin.

Tüm cron işlerini listele:


```bash
crontab -l
```

---

## 🔀 Koşullular (Conditionals)

`if-then-else` sözdizimi:

```bash
if [[ $# == 2 ]]
then
  echo "number of arguments is equal to 2"
else
  echo "number of arguments is not equal to 2"
fi
```

*Kopyalandı!*

*Satır kaydırma değiştirildi!*

`and` operatörü `&&`:


```bash
if [ condition1 ] && [ condition2 ]
```

*Kopyalandı!*

*Satır kaydırma değiştirildi!*

`or` operatörü `||`:


```bash
if [ condition1 ] || [ condition2 ]
```

---

## 🧠 Mantıksal Operatörler

| Operatör | Tanım                                               |
| --------- | ---------------------------------------------------- |
| `==`    | is equal to – eşittir                              |
| `!=`    | is not equal to – eşit değildir                   |
| `<`     | is less than – küçüktür                         |
| `>`     | is greater than – büyüktür                       |
| `<=`    | is less than or equal to – küçük veya eşittir   |
| `>=`    | is greater than or equal to – büyük veya eşittir |

---

## ➗ Aritmetik Hesaplamalar

Tamsayı aritmetiği gösterimi:


```bash
$(())
```

Temel aritmetik operatörler:

| Sembol | İşlem                   |
| ------ | ------------------------- |
| `+`  | addition – toplama       |
| `-`  | subtraction – çıkarma  |
| `*`  | multiplication – çarpma |
| `/`  | division – bölme        |

3 ile 2’yi toplamanın sonucunu göster:


```bash
echo $((3+2))
```

Bir sayıyı işaretçe tersine çevir (negate):


```bash
echo $((-1*-2))
```

---

## 📚 Diziler (Arrays)

1, 2, `"three"`, `"four"` ve 5 öğelerini içeren bir dizi tanımla:


```bash
my_array=(1 2 "three" "four" 5)
```

Dizine bir öğe ekle:


```bash
my_array+="six"
my_array+=7
```

Bir dizi bildir ve onu bir dosyadaki metin satırlarıyla doldur:


```bash
my_array=($(echo $(cat column.txt)))
```

---

## 🔁 `for` Döngüleri

1’den 5’e kadar olan değerler üzerinde yineleme yapmak için bir `for` döngüsü kullan:

```bash
for i in {0..5}; do
    echo "this is iteration number $i"
done
```

Bir dizideki tüm öğeleri yazdırmak için `for` döngüsü kullan:

```bash
for item in ${my_array[@]}; do
  echo $item
done
```

Yedi öğeli bir dizi varsayarak, `for` döngüsü içinde dizi indekslemesi kullan:

```bash
for i in {0..6}; do
    echo ${my_array[$i]}
done
```
