
# 🧪 Uygulamalı Laboratuvar: İleri Düzey Bash Betikleme

Bash betikleme becerilerinizi bir üst seviyeye taşıyacağınız bu uygulamalı laboratuvara hoş geldiniz. Burada çalışacağınız beceriler, sayısız betikleme uygulaması için mantıksal yapı taşları görevi görecektir.

Bu kavramlar, aynı zamanda bu dersin Final Projesinde yeni becerilerinizi sergilerken de gerekli olacaktır.

Bash betiklerinizi geliştirirken, her aşamada sonuçları test etmeniz ve mantığınızın beklendiği gibi çalıştığından emin olmanız her zaman tavsiye edilir. Her aşamayı, kolayca kavranabilir bir alt görevi yerine getiren ve nihai betiğinizin bir yapı taşı olan bir adım olarak düşünün.

---

## 🎯 Öğrenme Hedefleri

Bu laboratuvarı tamamladıktan sonra şunları yapabileceksiniz:

* Koşullu ifadeleri kullanarak komut kümelerini çalıştırmak
* Mantıksal operatörlerle doğru/yanlış karşılaştırmaları oluşturmak
* Aritmetik operatörleri kullanarak temel matematiksel hesaplamalar yapmak
* Liste benzeri dizilerde veri saklamak ve bu verilere erişmek
* `for` döngüleriyle tekrarlayan görevleri yürütmek

---

## 💻 Skills Network Cloud IDE Hakkında

*Skills Network Cloud IDE* (Theia ve Docker tabanlı), kurs ve proje ile ilgili uygulamalı laboratuvarlar için bir ortam sağlar.  *Theia* , masaüstünde veya bulutta çalıştırılabilen açık kaynaklı bir IDE’dir ( *Integrated Development Environment* ).

Bu laboratuvarı tamamlamak için, Docker konteynerinde çalışan Theia tabanlı Cloud IDE’yi kullanacağız.

---

## ⚠️ Önemli Not: Laboratuvar Ortamı Hakkında

Bu laboratuvar ortamındaki oturumların kalıcı olmadığını lütfen unutmayın.

Her bağlandığınızda sizin için yeni bir ortam oluşturulur. Önceki oturumda kaydetmiş olabileceğiniz tüm veriler kaybolur. Verilerinizi kaybetmemek için, bu laboratuvarları tek bir oturumda tamamlamayı planlayın.

---

## 1️⃣ Alıştırma 1 – Koşullu ifadeler ve mantıksal operatörler kullanma

Bu alıştırmada, aşağıdaki görevleri yerine getirmek için koşullu ifade içeren basit bir Bash betiği oluşturacaksınız:

* Kullanıcıya bir soruya Evet veya Hayır yanıtı vermesini istemek
* Kullanıcının yanıtına göre bir çıktı yazdırmak

---

### 1.1 📝 Yeni bir Bash betiği oluşturma

Bir Bash betik dosyası oluşturun ve onu çalıştırılabilir hale getirin.

**İpucu için buraya tıklayın**

`echo` komutunu kullanarak yeni bir Bash betiğine bir *shebang* yönlendirin.

Alternatif olarak, favori metin düzenleyicinizi kullanarak yeni bir metin dosyası açın ve içine bir *shebang* ekleyin. Yeni betiğinizi çalıştırılabilir hale getirmeyi unutmayın.

**Çözüm için buraya tıklayın**

Yalnızca komut satırı kullanarak bir çözüm:

```bash
1 echo '#!/bin/bash' > conditional_script.sh 
2 chmod u+x conditional_script.sh 
```

---

### 1.2 💬 Kullanıcıyı sorgulama ve yanıtı saklama

Şimdi betiğinizin:

* Kullanıcıya seçtiğiniz ikili (evet veya hayır) bir soru sormasını
* Kullanıcının yanıtını bir değişkende saklamasını

sağlayın.

**İpucu için buraya tıklayın**

`echo` ve `read` komutlarını kullanın.

**Çözüm için buraya tıklayın**

Bash betiğinizin artık aşağıdakine benzer görünmesi gerekir:

```bash
1 #!/bin/bash 
2 echo 'Are you enjoying this course so far?' 
3 echo -n "Enter \"y\" for yes, \"n\" for no." 
4 read response
```

---

### 1.3 🔁 Koşullu blok kullanarak kullanıcıya yanıt seçme

Son olarak, yaptığınız sorguya kullanıcının verdiği yanıta göre kullanıcıya bir mesaj yazdırmak için bir koşullu blok kullanın.

**İpucu:** Yanıtın izin verilen yanıtlardan hiçbirine uymadığı durumu da ele almak en iyi uygulamadır.

**İpucu için buraya tıklayın**

Kullanıcının yanıtını mevcut yanıt seçenekleriyle karşılaştırmak ve her durumda uygun bir mesaj yazdırmak için mantıksal bir operatör kullanan `if elif else fi` yapısında bir koşullu blok kullanın.

**Çözüm için buraya tıklayın**

Artık Bash betiğinizin aşağıdakine benzer olması gerekir:

```bash
#!/bin/bash

echo 'Are you enjoying this course so far?'
echo -n "Enter \"y\" for yes, \"n\" for no"
read response
if [ "$response" = "y" ]
then
    echo "I'm pleased to hear you are enjoying the course!"
    echo "Your feedback regarding what you have been enjoying would be most welcome!"
elif [ "$response" = "n" ]
then
   echo "I'm sorry to hear you are not enjoying the course."
   echo "Your feedback regarding what we can do to improve the learning experience"
   echo "for this course would be greatly appreciated!"
else
   echo "Your response must be either 'y' or 'n'."
   echo "Please re-run the script to try again."
fi
```

---

## 2️⃣ Alıştırma 2 – Temel matematiksel hesaplamalar ve sayısal mantıksal karşılaştırmalar yapma

Bu alıştırmada, kullanıcı tarafından girilen iki tamsayı üzerinde temel aritmetik hesaplamalar yapan bir Bash betiği oluşturacaksınız. Ayrıca, hangi hesaplamanın en büyük sonuca yol açtığını belirlemek için mantıksal karşılaştırmalar kullanacaksınız.

---

### 2.1 ➕ Bash betiği oluşturma

Kullanıcıdan iki tamsayı girmesini isteyen ve ardından bu iki tamsayının hem toplamını hem de çarpımını saklayıp yazdıran çalıştırılabilir bir Bash betiği oluşturun.

**İpucu için buraya tıklayın**

Önceki alıştırmadaki gibi `echo` ve `read` komutlarını kullanın.

Aritmetik hesaplamalar için kullanılan gösterimi hatırlayın.

**Çözüm için buraya tıklayın**

```bash
#!/bin/bash

echo -n "Enter an integer: "
read n1
echo -n "Enter another integer: "
read n2

sum=$(($n1+$n2))
product=$(($n1*$n2))

echo "The sum of $n1 and $n2 is $sum"
echo "The product of $n1 and $n2 is $product."
```

---

### 2.2 🧠 Betiğinize mantık ekleme

Betiğinize, toplamın çarpımdan büyük mü, küçük mü yoksa çarpıma eşit mi olduğunu belirleyen bir mantık ekleyin. Her olası sonuç için uygun bir ifade yazdırın.

Kullanıcının iki tamsayı girdiğini varsayın. Kullanıcının yanlışlıkla tamsayı olmayan bir dize girdiği durumu ele alma konusunda endişelenmeyin.

**İpucu için buraya tıklayın**

Bir koşul bloğu kullanın. Mantıksal operatörlerin gösterimini hatırlayın.

**Çözüm için buraya tıklayın**

```bash
#!/bin/bash

echo -n "Enter an integer: "
read n1
echo -n "Enter another integer: "
read n2

sum=$(($n1+$n2))
product=$(($n1*$n2))

echo "The sum of $n1 and $n2 is $sum"
echo "The product of $n1 and $n2 is $product."

if [ $sum -lt $product ]
then
   echo "The sum is less than the product."
elif [ $sum -eq $product ]
then
   echo "The sum is equal to the product."
elif [ $sum -gt $product ]
then
   echo "The sum is greater than the product."
fi
```

---

## 3️⃣ Alıştırma 3 – `for` döngüleri içinde veri saklamak ve erişmek için dizileri kullanma

Bu alıştırmada, CSV biçiminde sağlanan bir veri kümesine dayanarak bir rapor oluşturacaksınız. Veri kümesindeki sütunları ayrı dizilere ayıklayacak, aritmetik ve dizi mantığı kullanarak yeni bir sütun oluşturacaksınız. Son olarak, bu yeni sütunu veri kümesiyle birleştirerek ortaya çıkan raporu CSV dosyası olarak kaydedeceksiniz.

---

### 3.1 📥 Geçerli çalışma dizininize bir CSV dosyası indirme

`arrays_table.csv` dosyası aşağıdaki URL’de bulunmaktadır:

```text
1
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/M3/L2/arrays_table.csv
```

*Kopyalandı!*

*Satır kaydırma değiştirildi!*

**İpucu için buraya tıklayın**

`wget` komutunu kullanın.

**Çözüm için buraya tıklayın**

```bash
csv_file="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/M3/L2/arrays_table.csv"
wget $csv_file
```

---

### 3.2 👀 CSV dosyasını görüntüleyerek yapısını anlama

**İpucu için buraya tıklayın**

Komut satırında `cat` komutunu kullanın veya dosyayı GUI ile açın.

**Çözüm için buraya tıklayın**

```bash
cat arrays_table.csv
```

---

### 3.3 🧱 Tablo sütunlarını 3 diziye ayrıştıran bir Bash betiği oluşturma

**İpucu için buraya tıklayın**

Komut yerine koyma ( *command substitution* ), `cut` komutu ve bir öğe listesinden dizi oluşturma gösterimini kullanın.

Ayrıca, mantığınızı doğrulamak için ilk diziyi yazdırın.

**Çözüm için buraya tıklayın**

```bash
#!/bin/bash

csv_file="./arrays_table.csv"

# parse table columns into 3 arrays
column_0=($(cut -d "," -f 1 $csv_file))
column_1=($(cut -d "," -f 2 $csv_file))
column_2=($(cut -d "," -f 3 $csv_file))

# print first array
echo "Displaying the first column:"
echo "${column_0[@]}"
```

---

### 3.4 ➖ Üçüncü ve ikinci sütunların farkı olacak yeni bir dizi oluşturma

Yeni dizinizi bir başlıkla (bir sütun adıyla) başlatın ve sonuçlarınızı doğrulamayı unutmayın.

**İpucu 1 için buraya tıklayın**

Diziyi doldurmak için bir döngü kullanın.

Gereken eleman sayısını belirleyin ve bunu döngü ifadenize dahil edin.

Mantığınızı doğrulamak için hem eleman sayısını hem de yeni dizinizin içeriğini yazdırın.

**İpucu 2 için buraya tıklayın**

Kaç yinelemeye ihtiyaç duyduğunuzu bildiğinizde `for` döngüsü gösterimini ve dizi indekslemesinin 0’dan başladığını hatırlayın.

Satır sayısını almak için, `cat` ve `wc` komutlarını filtre olarak kullanan bir *pipe* üzerinde komut yerine koyma kullanın ve sonucu bir değişkende saklayın.

**Çözüm için buraya tıklayın**

```bash
#!/bin/bash

csv_file="./arrays_table.csv"

# parse table columns into 3 arrays
column_0=($(cut -d "," -f 1 $csv_file))
column_1=($(cut -d "," -f 2 $csv_file))
column_2=($(cut -d "," -f 3 $csv_file))

# print first array
echo "Displaying the first column:"
echo "${column_0[@]}"

## Create a new array as the difference of columns 1 and 2
# initialize array with header
column_3=("column_3")
# get the number of lines in each column
nlines=$(cat $csv_file | wc -l)
echo "There are $nlines lines in the file"
# populate the array
for ((i=1; i<$nlines; i++)); do
  column_3[$i]=$((column_2[$i] - column_1[$i]))
done
echo "${column_3[@]}"
```

---

### 3.5 📊 Yeni sütunu kaynak tabloyla birleştirerek bir rapor oluşturma

Raporunuzu CSV dosyası olarak kaydedin.

Sonuçlarınızı doğrulamayı unutmayın.

**İpucu 1 için buraya tıklayın**

Yeni diziyi dosyaya satır satır yazın.

Dosyayı bir başlıkla başlatın.

**İpucu 2 için buraya tıklayın**

Yeniden yönlendirmeyi kullanın ve iki dosyayı yan yana birleştirmeyi ( *merge* ) nasıl yapacağınızı hatırlayın.

Nihai raporunuzun doğru CSV biçimine sahip olduğundan emin olun.

**Çözüm için buraya tıklayın**

```bash
#!/bin/bash

csv_file="./arrays_table.csv"

# parse table columns into 3 arrays
column_0=($(cut -d "," -f 1 $csv_file))
column_1=($(cut -d "," -f 2 $csv_file))
column_2=($(cut -d "," -f 3 $csv_file))

# print first array
echo "Displaying the first column:"
echo "${column_0[@]}"

## Create a new array as the difference of columns 1 and 2
# initialize array with header
column_3=("column_3")
# get the number of lines in each column
nlines=$(cat $csv_file | wc -l)
echo "There are $nlines lines in the file"
# populate the array
for ((i=1; i<$nlines; i++)); do
  column_3[$i]=$((column_2[$i] - column_1[$i]))
done
echo "${column_3[@]}"

## Combine the new array with the csv file
# first write the new array to file
# initialize the file with a header
echo "${column_3[0]}" > column_3.txt
for ((i=1; i<nlines; i++)); do
  echo "${column_3[$i]}" >> column_3.txt
done
paste -d "," $csv_file column_3.txt > report.csv
```

---

## ✅ Sonuç

Tebrikler! İleri düzey Bash betikleme mantığı kullandığınız bir uygulamalı laboratuvarı az önce tamamladınız.

Bu laboratuvarda şunları öğrendiniz:

* Belirli bir koşulun doğru veya yanlış olmasına göre komutları çalıştırmak için koşullu ifadeleri kullanabileceğinizi
* Doğru/yanlış işlemleri yapmak için mantıksal operatörleri
* Temel matematiksel hesaplamaları gerçekleştirmek için aritmetik operatörleri
* Verileri saklamak ve bunlara erişmek için liste benzeri dizileri
* Tekrarlayan görevleri yürütmek için `for` döngülerini

Burada ileride çok faydalı olacak pek çok konuyu ele aldınız. Benzer sorunlarla, alıştırmalarınızda ve final projelerinizde ve en güzeli kariyerinizde karşılaşacaksınız! Laboratuvarlarınızı her zaman tekrar gözden geçirebileceğinizi unutmayın.

**İpucu:** Yalnızca verimlilikle ilgilenmiş olsaydık, adımlardan biri atlanabilirdi. Özellikle, hesaplamalarınızı bir dizide saklayıp daha sonra diziyi dosyaya yazmak yerine, hesaplamalarınızı satır satır bir metin dosyasına yönlendirebilirdiniz.

Son olarak, bu kurs için dilediğiniz zaman bir değerlendirme ve puanlama yapmanızı teşvik ediyoruz!
