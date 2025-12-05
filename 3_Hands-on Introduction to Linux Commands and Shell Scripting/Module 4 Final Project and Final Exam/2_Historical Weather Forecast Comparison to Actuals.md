# 🌦️ Uygulama Projesi: Tarihsel Hava Tahmini ile Gerçeklerin Karşılaştırılması

## 🎯 Öğrenme Hedefleri

Bu uygulama projesinde şunları yapacaksın:

* Günlük log dosyanı başlatmak
* Ham veriyi indirmek, çıkarmak ve bir rapora yüklemek için bir Bash betiği yazmak
* Raporuna bazı temel analizler eklemek
* Raporunun günlük olarak güncellenmesini zamanlamak
* Tarihsel tahmin doğruluğunu ölçmek ve raporlamak

Bu projeyi yönetilebilir adımlara böldük. Bunların herhangi birini veya tamamını kendi başına denemekte özgürsün; ancak, yine de sağlanan detaylarla çalışmanı kontrol etmeni öneririz.

---

## 📝 Alıştırma 1 - Hava durumu raporu log dosyanı başlat

### 📄 1.1 rx_poc.log adlı bir metin dosyası oluştur

`rx_poc.log`, POC hava durumu raporu log dosyan olacak; yani kazıyacağın günlük hava durumu verilerinin giderek büyüyen geçmişini içeren bir metin dosyası. Log dosyasındaki her bir giriş, Tablo 1’deki bir satıra karşılık gelir.

**İpucu için buraya tıkla**

`touch` komutunu kullan ya da GUI üzerinden yeni bir metin dosyası aç.

**Çözüm için buraya tıkla**

Terminaline aşağıdakini girerek `rx_poc.log` dosyasını oluştur:

```bash
1
touch rx_poc.log
```

---

### 🧾 1.2 Hava durumu raporuna bir başlık ekle

Başlığın, Tablo 1’deki sütun adlarından oluşmalı ve sekmelerle ayrılmalı.

Başlığı hava durumu raporuna yaz.

**İpucu için buraya tıkla**

`echo` komutunu `-e` seçeneği ile kullan ve isimleri içeren dizgede sekme ayraçları `\t` ekle.

Neden `-e` seçeneğine ihtiyaç duyulduğunu düşün.

**Çözüm için buraya tıkla**

Bir kabuk değişkeni ve komut ikamesi ( *command substitution* ) kullan:

```bash

header=$(echo -e "year\tmonth\tday\tobs_temp\tfc_temp")
echo $header>rx_poc.log
```

VEYA daha doğrudan, `echo` ve yönlendirme kullan:

```bash
1
echo -e "year\tmonth\tday\tobs_temp\tfc_temp">rx_poc.log
```

İpucu: Gereksiz gibi görünse de, bu tür durumlarda değişken kullanmak daha iyi bir pratiktir. Değişkenler, daha anlaşılır ve başkaları ya da senin tarafından daha sonra değiştirilmesi daha güvenli, çok daha temiz bir kod sağlar. Değişkenlerin için anlamlı isimler kullanmak, kodu aynı zamanda “kendini belgeleyen” hale getirir.

---

## 🌐 Alıştırma 2 - Ham hava durumu verilerini indir

### 🛠️ 2.1 rx_poc.sh adlı bir metin dosyası oluştur ve onu çalıştırılabilir bir Bash betiği yap

**İpucu 1 için buraya tıkla**

Bir *shebang* ekle.

**İpucu 2 için buraya tıkla**

`chmod` komutunu kullan.

**Çözüm 1 için buraya tıkla**

`rx_poc.sh` dosyasını oluştur:

```bash
1 touch rx_poc.sh
```

`rx_poc.sh` dosyasının ilk satırına Bash *shebang* satırını ekle:

```bash
1 #! /bin/bash
```

**Çözüm 2 için buraya tıkla**

Betini çalıştırılabilir yapmak için terminalde şunu çalıştır:

```bash
1 chmod u+x rx_poc.sh
```

Değişikliklerini `ls` komutunu `-l` seçeneği ile kullanarak doğrula.

---

### 🏙️ 2.2 Hava durumu raporuna erişmek için şehir adını Casablanca olarak ata

**İpucu için buraya tıkla**

Atama operatörünü kullan.

**Çözüm için buraya tıkla**

```bash
1 city=Casablanca
```

---

### ☁️ 2.3 Casablanca için hava durumu bilgisini elde et

**İpucu için buraya tıkla**

`curl` komutunu `--output` seçeneği ile kullan. Çıktıyı `weather_report` adlı bir dosyaya kaydet.

**Çözüm için buraya tıkla**

`rx_poc.sh` dosyasını aşağıdakini içerecek şekilde düzenle:

```bash
1 curl -s wttr.in/$city?T --output weather_report
```

---

## 🔍 Alıştırma 3 - Gerekli verileri çıkar ve yükle

### 📤 3.1 Ham veri dosyasından gerekli verileri çıkarmak ve bunları obs_temp ve fc_temp değişkenlerine atamak için rx_poc.sh dosyasını düzenle

Gerekli verilerin çıkarılması, doğru sonucu elde edene kadar biraz deneme yanılma gerektiren bir süreç olacaktır. 2.3. Adımda elde ettiğin hava durumu raporunu incele, neyi çıkarman gerektiğini belirle ve kalıplara bak.

Şunları yapmanın yollarını arıyorsun:

* Kabuk komutlarını kullanarak yalnızca ihtiyacın olan verileri ( *sinyal* ) çıkarmak
* Geri kalan her şeyi ( *gürültü* ) filtrelemek
* Filtrelerini bir boru hattında birleştirmek (komutları zincirlemek için *pipes* kullanımını hatırla)

**Başlamak için İpucuya buradan tıkla**

Hava durumu raporundan yalnızca sıcaklık içeren satırları çıkar ve sonucu sıcaklık çıktısını temsil eden değişkenlere kaydet.

---

### 🌡️ 3.1.1 Anlık sıcaklığı çıkar ve bunu obs_temp adlı bir kabuk değişkeninde sakla

Sonuçlarını doğrulamayı unutma.

Şu ana kadar fark etmiş olabileceğin gibi, wttr.in’den çıkarılan sıcaklık değerleri, etrafları özel biçimlendirme karakterleriyle çevrili halde gelir. Bu “gizli” karakterler, sayıları belirli bir renkte görüntülemeye neden olur – örneğin, log dosyanı görüntülemek için `cat` komutunu kullandığında.

Ne yazık ki, bu tür biçimlendirilmiş metinler üzerinde aritmetik işlem yapamazsın; bu yüzden, bu laboratuvarda daha sonra kullanabilmek için, değerleri çevreleyen biçimlendirmeden ayıklaman gerekir.

**İpucu 1 için buraya tıkla**

Anlık sıcaklık hangi satırda?

**İpucu 2 için buraya tıkla**

Satırı uygun şekilde alanlara ayırmak için sınırlayıcı ( *delimiter* ) olarak kullanabileceğin herhangi bir karakter var mı?

**Çözüm için buraya tıkla**

`rx_poc.sh` dosyasına aşağıdaki satırları eklerken, boru hattındaki her filtrenin ne yaptığını komut satırında kullanarak anladığından emin ol. Boru hattını geliştirirken, sonucu görmek için filtreleri birer birer eklemeyi dene.

```bash
#To extract Current Temperature
obs_temp=$(curl -s wttr.in/$city?T | grep -m 1 '°.' | grep -Eo -e '-?[[:digit:]].*')
echo "The current Temperature of $city: $obs_temp"
```

İlk satır, belirtilen şehir ($city) için wttr.in’den hava durumu bilgisini getirmek için `curl` komutunu kullanır. Ardından, geçerli sıcaklığı santigrat derece cinsinden çıkarmak için `grep` ve `grep -Eo` kombinasyonunu kullanır ve bunu `obs_temp` değişkenine atar.

İkinci satır (`echo $obs_temp`), anlık sıcaklığı konsola yazdırır.

---

### 🌤️ 3.1.2 Yarın öğlen için sıcaklık tahminini çıkar ve bunu fc_temp adlı bir kabuk değişkeninde sakla

**İpucu için buraya tıkla**

Önceki boru hattını anladıysan, deneme yoluyla bu problemi çözebileceksin.

**Çözüm için buraya tıkla**

`rx_poc.sh` dosyasına şunları ekle:

```bash

# To extract the forecast tempearature for noon tomorrow
fc_temp=$(curl -s wttr.in/$city?T | head -23 | tail -1 | grep '°.' | cut -d 'C' -f2 | grep -Eo -e '-?[[:digit:]].*')
echo "The forecasted temperature for noon tomorrow for $city : $fc_temp C"
```

İlk satır, yarının öğle tahmin sıcaklığını içeren satıra daraltmak için `head` ve `tail` kombinasyonunu kullanır. `grep` ve `cut`, sıcaklık bilgisini ayıklamak ve biçimlendirmek için kullanılır ve sıcaklığın sayısal kısmı `grep -Eo` ile yakalanır.

İkinci satır (`echo $fc_temp`), yarın öğlen için tahmin edilen sıcaklığı konsola yazdırır.

---

### 📆 3.2 Gün, ay ve yılı uygun kabuk değişkenlerinde sakla

**İpucu için buraya tıkla**

Komut ikamesi ( *command substitution* ) ve `date` komutunu doğru biçimlendirme seçenekleriyle kullan.

Casablanca için saat dilimi UTC+1’dir. Casablanca yerel saatini almak için, `TZ` isimli saat dilimi ortam değişkenini aşağıdaki gibi ayarlayabilirsin:

```bash
1
TZ='Morocco/Casablanca'
```

**Çözüm için buraya tıkla**

`rx_poc.sh` dosyasına şunları ekle:

```bash

#Assign Country and City to variable TZ
TZ='Morocco/Casablanca'
# Use command substitution to store the current day, month, and year in corresponding shell variables:
day=$(TZ='Morocco/Casablanca' date -u +%d) 
month=$(TZ='Morocco/Casablanca' date +%m)
year=$(TZ='Morocco/Casablanca' date +%Y)
```

Not: Neden, öğlen saatini almak istiyorsak, sadece `hour`’ı 12 değerine ayarlamadığımızı merak ediyor olabilirsin.

Ancak, eğer bunu yapsaydık, kodu gerçekten doğru yerel saatte çalıştırdığımızı doğrulama yeteneğimizi kaybederdik. Yerel zamanı sabit bir sayıdan ziyade bir ölçüm olarak düşünmelisin.

---

### 🔗 3.3 Alanları Tablo 1’deki tek bir satıra karşılık gelen, sekmeyle ayrılmış bir kayıtta birleştir

Ortaya çıkan kaydı, hava durumu log dosyana bir veri satırı olarak ekle.

**İpucu için buraya tıkla**

Log dosyanı başlatmak için başlığı nasıl oluşturmuştun?

**Çözüm için buraya tıkla**

`rx_poc.sh` dosyasına şunları ekle:

```bash

record=$(echo -e "$year\t$month\t$day\t$obs_temp\t$fc_temp C")
echo $record>>rx_poc.log
```


## ⏰ Alıştırma 4 - Bash betiğin `rx_poc.sh`’i her gün yerel saatle öğlen çalıştırmayı zamanla

### 🕒 4.1. Betiğini günün hangi saatinde çalıştıracağını belirle

Her gün, Kazablanka’da yerel saatle öğlen vakti hava durumu verisini yüklemek istediğini hatırla.

Önce, sisteminin varsayılan saat dilimi ile UTC arasındaki zaman farkını kontrol et.

**İpucu 1 için buraya tıkla**

Sistem saatini almak için bir kez, UTC’yi almak için bir kez olmak üzere, uygun seçeneklerle `date` komutunu iki kez kullan.

**Çözüm için buraya tıkla**

Aşağıdaki komutları çalıştırmak, sistemin ile UTC arasındaki zaman farkını elde etmek için ihtiyacın olan bilgiyi verir.

```bash
$ date
Mon Feb 13 11:28:12 EST 2023
$ date -u
Mon Feb 13 16:28:16 UTC 2023
```

Artık sisteminin yerel saati ile Kazablanka’nın saati arasında kaç saat fark olduğunu belirleyebilirsin.

Bu örnekte yerel saat (11:28), UTC’den (16:28) 5 saat geridedir. Bu nedenle, sistemin saat dilimi (EST), UTC-5 ofsetine sahiptir.

Şimdi, sistemin ile Kazablanka arasındaki zaman farkını hesapla:

Kazablanka UTC+1’dedir.

Sistemin UTC-5’tedir.

Zaman farkı şu şekilde hesaplanır: (Kazablanka UTC ofseti) – (Sisteminin UTC ofseti).

Bu da: `(+1) - (-5) = 6` saattir.

Bu, Kazablanka saatinin, sisteminin saatinden 6 saat ileride olduğu anlamına gelir.

Dolayısıyla, betiğini Kazablanka’da öğlen (12:00 UTC+1) çalıştırmak için, onu sistem saatine göre sabah 6:00’da (EST) çalıştırman gerekir.

Kazablanka’da 12:00’den 6 saat geri gidersen, sisteminde 06:00 (sabah 6) elde edilir.

---

### 🧾 4.2. Betiğini çalıştıran bir cron görevi oluştur

**İpucu için buraya tıkla**

`crontab` dosyasını düzenle ve dosyada yer alan `crontab` sözdizimi açıklamasını incele.

**Çözüm için buraya tıkla**

`crontab` dosyasını düzenle:

```bash
1
crontab -e
```

Dosyanın sonuna aşağıdaki satırı ekle:

```bash
1
0 6 * * * /home/project/rx_poc.sh
```

Dosyayı kaydet ve editörden çık.

---

### ✅ 4.3. Tam çözüm

Referans olması için, ham hava durumu raporunu oluşturan bir Bash betiği aşağıdadır. Bakmadan önce tüm adımları kendi başına takip etmeyi dene!

**Tam Çözüm için buraya tıkla**

```bash
#! /bin/bash
 
#Assign city name as Casablanca
city=Casablanca

#Obtain the weather report for Casablanca
curl -s wttr.in/$city?T --output weather_report

#To extract Current Temperature
obs_temp=$(curl -s wttr.in/$city?T | grep -m 1 '°.' | grep -Eo -e '-?[[:digit:]].*')
echo "The current Temperature of $city: $obs_temp"

# To extract the forecast tempearature for noon tomorrow
fc_temp=$(curl -s wttr.in/$city?T | head -23 | tail -1 | grep '°.' | cut -d 'C' -f2 | grep -Eo -e '-?[[:digit:]].*')
echo "The forecasted temperature for noon tomorrow for $city : $fc_temp C"

#Assign Country and City to variable TZ
TZ='Morocco/Casablanca'


# Use command substitution to store the current day, month, and year in corresponding shell variables:
day=$(TZ='Morocco/Casablanca' date -u +%d)
month=$(TZ='Morocco/Casablanca' date +%m)
year=$(TZ='Morocco/Casablanca' date +%Y)


# Log the weather
record=$(echo -e "$year\t$month\t$day\t$obs_temp\t$fc_temp C")
echo $record>>rx_poc.log
```

---

## 📊 Alıştırma 5 - Gerçek değerlere göre tarihsel tahmin doğruluğunu raporlayan bir betik oluştur

Artık hava durumu verilerini bir rapora toplamak için bir ETL kabuk betiği oluşturduğuna göre, tahmin edilen sıcaklıkların doğruluğunu gerçek değerlere göre ölçmek ve raporlamak için başka bir betik oluşturalım.

Başlamak için, `historical_fc_accuracy.tsv` adında sekmeyle ayrılmış bir dosya oluştur.

Aşağıdaki kodu dosyaya ekleyerek sütun adları içeren bir başlık satırı ekle:

```bash
1
echo -e "year\tmonth\tday\tobs_temp\tfc_temp\taccuracy\taccuracy_range" > historical_fc_accuracy.tsv
```

Kopyalandı!

Wrap Toggled!

Bu rapor ile daha önce oluşturduğun rapor arasındaki temel farklardan biri, tahmin sıcaklığının artık tahminin yapıldığı gün yerine, tahminin ait olduğu tarihle hizalanacak olmasıdır. Sonuç olarak, tarih, tahminin yapıldığı gün bir önceki satırda değil, o tarihe ait gözlemlenen sıcaklık ile aynı satırda yer alacaktır.

Ayrıca, `fc_accuracy.sh` adlı çalıştırılabilir bir Bash betiği de oluştur.

Yeni betiğini periyodik olarak çalışacak şekilde zamanlamak yerine, onu, istek üzerine tarihsel tahmin doğruluğunu üretmek için kullanabileceğin bir araç olarak düşün.

---

### 🌡️ 5.1. Bugünün tahmin edilen ve gerçek sıcaklıkları arasındaki farkı belirle

Betik tüm veriyi tek seferde işleyecek şekilde yazmak yerine, sadece tek bir örnek için problemi çözerek işe başlayalım. Daha sonra betiği birden fazla günün genel durumunu ele alacak şekilde değiştirebilirsin.

#### 📥 5.1.1. Bugünün tahmin edilen ve gözlemlenen sıcaklıklarını çıkar ve değişkenlerde sakla

**İpucu 1 için buraya tıkla**

Dünkü kayda bak.

**İpucu 2 için buraya tıkla**

Tahmini uygun alandan çıkar.

**Çözüm için buraya tıkla**

```bash
1
yesterday_fc=$(tail -2 rx_poc.log | head -1 | cut -d " " -f5)
```

Kopyalandı!

Wrap Toggled!

---

#### 📏 5.1.2. Tahmin doğruluğunu hesapla

**İpucu için buraya tıkla**

Önce bugünün gözlemlenen sıcaklığını çıkar. Sonra tahmin edilen ve gözlemlenen sıcaklıklar arasındaki farkı hesapla.

**Çözüm için buraya tıkla**

```bash
1
2
3
today_temp=$(tail -1 rx_poc.log | cut -d " " -f4)
accuracy=$(($yesterday_fc-$today_temp))
echo "accuracy is $accuracy"
```

Kopyalandı!

Wrap Toggled!

İpucu: Bu hesabın anlamlı olabilmesi için hava durumu raporunun en az iki günlük veriye sahip olması gerekir.

Kodunu test etmek için, basitçe, hava durumu raporun `rx_poc.log` dosyasına yapay veriler ekleyebilirsin.

---

### 🏷️ 5.2. Her tahmine, doğruluğuna göre bir etiket ata

Her tahmine, doğruluk aralığının en sıkı şekilde uyduğu aralığa göre aşağıdaki tabloya göre bir doğruluk etiketi atayalım. Sonucunu doğrula.

| doğruluk aralığı | doğruluk etiketi |
| -------------------- | ----------------- |
| +/- 1 deg            | excellent         |
| +/- 2 deg            | good              |
| +/- 3 deg            | fair              |
| +/- 4 deg            | poor              |

**İpucu 1 için buraya tıkla**

Doğruluk değerini, her pozitif ve negatif tam sayı aralığı ile ayrı ayrı karşılaştırmak için iki koşul kullan.

**Çözüm için buraya tıkla**

```bash
if [ -1 -le $accuracy ] && [ $accuracy -le 1 ]
then
   accuracy_range=excellent
elif [ -2 -le $accuracy ] && [ $accuracy -le 2 ]
then
    accuracy_range=good
elif [ -3 -le $accuracy ] && [ $accuracy -le 3 ]
then
    accuracy_range=fair
else
    accuracy_range=poor
fi

echo "Forecast accuracy is $accuracy"
```

---

### 📁 5.3. Tarihsel tahmin doğruluk dosyana bir kayıt ekle

**İpucu için buraya tıkla**

Tüm alanları doldurmak için ihtiyacın olan doğru satırı ve kalan verileri çıkar.

**Çözüm için buraya tıkla**

```bash
row=$(tail -1 rx_poc.log)
year=$( echo $row | cut -d " " -f1)
month=$( echo $row | cut -d " " -f2)
day=$( echo $row | cut -d " " -f3)
echo -e "$year\t$month\t$day\t$today_temp\t$yesterday_fc\t$accuracy\t$accuracy_range" >> historical_fc_accuracy.tsv
```

---

### 🧮 5.4. Tek bir günü ele almak için tam çözüm

Aşağıda, yalnızca tek bir örnek ya da güne dayalı doğruluk hesaplamalarını ele alan `fc_accuracy.sh` betiğinin son hali verilmiştir.

**Çözüm için buraya tıkla**

```bash
#! /bin/bash

yesterday_fc=$(tail -2 rx_poc.log | head -1 | cut -d " " -f5)
today_temp=$(tail -1 rx_poc.log | cut -d " " -f4)
accuracy=$(($yesterday_fc-$today_temp))

echo "accuracy is $accuracy"

if [ -1 -le $accuracy ] && [ $accuracy -le 1 ]
then
           accuracy_range=excellent
elif [ -2 -le $accuracy ] && [ $accuracy -le 2 ]
   then
               accuracy_range=good
       elif [ -3 -le $accuracy ] && [ $accuracy -le 3 ]
       then
                   accuracy_range=fair
           else
                       accuracy_range=poor
fi

echo "Forecast accuracy is $accuracy_range"

row=$(tail -1 rx_poc.log)
year=$( echo $row | cut -d " " -f1)
month=$( echo $row | cut -d " " -f2)
day=$( echo $row | cut -d " " -f3)
echo -e "$year\t$month\t$day\t$today_temp\t$yesterday_fc\t$accuracy\t$accuracy_range" >> historical_fc_accuracy.tsv
```

---

### 🔁 5.5. Tüm günler için genelleme

Kodunu, tüm hava durumu doğruluk geçmişini oluşturacak şekilde genelleştirmek, sana bırakılmış bir alıştırma olarak kalmıştır. Bir sonraki alıştırmada, bu hava durumu doğruluk geçmişi raporunun sentetik bir versiyonunu indirip onunla çalışacaksın.

Hava durumu doğruluğu geçmişini kendin oluşturmak istersen, aşağıdaki öneriler sana rehberlik edebilir:

* Hava durumu log dosyanı bir `for` döngüsü kullanarak yinele. Her yinelemede:
  * Her yinelemede arka arkaya gelen satır çiftlerini çıkarmak için `head` ve `tail` kullan
  * Bu, sana geçerli günün ve bir önceki günün verilerini sağlar
* Bu satır çiftini, kodunda dünkü ve bugünkü verilerle yaptığın gibi ele al
* Doğruluk hesaplamalarını eskisi gibi gerçekleştir
* Tarih bilgisini çıkarmak için doğru satırı kullan
* Ortaya çıkan verini tarihsel tahmin doğruluğu raporuna ekle

---

## 📈 Alıştırma 6 - Tarihsel tahmin doğruluğunun haftalık istatistiklerini raporlayan bir betik oluştur

Bu alıştırmada, sentetik bir tarihsel tahmin doğruluğu raporu indirecek ve en son haftalık veriye dayalı bazı temel istatistikler hesaplayacaksın.

Önce, `weekly_stats.sh` adlı çalıştırılabilir bir Bash betiği oluştur.

---

### ⬇️ 6.1. Sentetik tarihsel tahmin doğruluğu veri setini indir

Veri setini geçerli çalışma dizinine indirmek için terminalde aşağıdaki komutu çalıştır.

```bash
1
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-LX0117EN-Coursera/labs/synthetic_historical_fc_accuracy.tsv
```

Kopyalandı!

Wrap Toggled!

---

### 📚 6.2. Tarihsel doğrulukları, son haftalık veriyi kapsayan bir diziye yükle

Betik dosyanı çalıştırılabilir yapmayı unutma. Ayrıca, diziyi terminale yazarak sonucunu doğrula.

**İpucu 1 için buraya tıkla**

Önce, verinin son haftasını çıkar.

**İpucu 2 için buraya tıkla**

Değerleri `scratch.txt` adlı geçici bir dosyada sakla. `scratch.txt` içeriğini `week_fc` adlı bir diziye yaz.

**Çözüm için buraya tıkla**

Kabuk betiğin aşağıdakine benzer görünmelidir. Bu görevi yerine getirmenin birçok yolu vardır, bu yüzden sağlanan çözüm tek değildir.

```bash
#!/bin/bash

echo $(tail -7 synthetic_historical_fc_accuracy.tsv  | cut -f6) > scratch.txt

week_fc=($(echo $(cat scratch.txt)))

# validate result:
for i in {0..6}; do
    echo ${week_fc[$i]}
done
```

---

### 📉 6.3. Hafta için minimum ve maksimum mutlak tahmin hatalarını göster

Şimdi dizini kullanarak, son hafta için minimum ve maksimum mutlak hataları hesapla. Örneğin, -1 gibi bir değerin varsa, bunu 1 olarak değiştir. Minimum ve maksimum mutlak hataları terminale yaz.

**İpucu 1 için buraya tıkla**

Dizinde negatif değer olup olmadığını kontrol et ve bu dizi girdilerini pozitif karşılıklarıyla yeniden ata.

**İpucu 2 için buraya tıkla**

`minimum` ve `maximum` adında iki değişken başlat. Dizi değerleri üzerinde döngü kur ve gerektiği gibi bu iki değişkeni güncelle.

**Çözüm için buraya tıkla**

`weekly_stats.sh` için son kabuk betiğin artık aşağıdakine benzer görünmelidir.

```bash
#!/bin/bash

echo $(tail -7 synthetic_historical_fc_accuracy.tsv  | cut -f6) > scratch.txt

week_fc=($(echo $(cat scratch.txt)))

# validate result:
for i in {0..6}; do
    echo ${week_fc[$i]}
done

for i in {0..6}; do
  if [[ ${week_fc[$i]} < 0 ]]
  then
    week_fc[$i]=$(((-1)*week_fc[$i]))
  fi
  # validate result:
  echo ${week_fc[$i]}
done

minimum=${week_fc[1]}
maximum=${week_fc[1]}
for item in ${week_fc[@]}; do
   if [[ $minimum > $item ]]
   then
     minimum=$item
   fi
   if [[ $maximum < $item ]]
   then
     maximum=$item
   fi
done

echo "minimum ebsolute error = $minimum"
echo "maximum absolute error = $maximum"
```

---

## 🏁 Özet

Tebrikler! Bu derste öğrendiğin birçok kavramı kullanarak, gerçek dünya koşullarına oldukça yakın, zorlu bir uygulama projesini yeni tamamladın.

Edindiğin bilgi, pek çok pratik gerçek dünya problemini çözmen için seni hazırlamış durumda. Bu dersin neredeyse sonuna geldin ve yolculuğunun son adımı, akran değerlendirmeli Final Projeyi tamamlamak olacak.

Bu laboratuvarda şunları öğrendin:

* Hava durumu raporu log dosyanı başlatmayı
* Ham hava durumu verisini indiren ve gerekli verileri çıkarıp yükleyen bir Bash betiği yazmayı
* Bash betiğin `rx_poc.sh`’yi her gün yerel saatle öğlen çalışacak şekilde zamanlamayı
* Raporlama metrikleri üretmek için gelişmiş Bash betikleme uygulamayı
* Tarihsel tahmin doğruluğunu raporlayan bir betik oluşturmayı
* Hafta için minimum ve maksimum mutlak hataları raporlayan bir betik oluşturmayı
