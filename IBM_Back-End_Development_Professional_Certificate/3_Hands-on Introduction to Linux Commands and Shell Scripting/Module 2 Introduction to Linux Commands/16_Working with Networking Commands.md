# 🌐 Ağ Komutları ile Çalışmak

## 🎯 Öğrenme Hedefleri

Bu laboratuvarı tamamladıktan sonra şunları yapabileceksiniz:

* `hostname` ve `ip` komutlarını kullanarak ağ yapılandırmanızı görüntülemek
* `ping` komutunu kullanarak bir ağ bağlantısını test etmek
* `curl` ve `wget` komutları ile veri aktarmak

---

## 🧰 Skills Network Cloud IDE Hakkında

**Skills Network Cloud IDE** (Theia ve Docker tabanlı), kurs ve proje ile ilgili uygulamalı laboratuvarlar için bir ortam sağlar.

 **Theia** , masaüstünde veya bulutta çalıştırılabilen, açık kaynaklı bir  **IDE** ’dir ( *Integrated Development Environment – Tümleşik Geliştirme Ortamı* ).

Bu laboratuvarı tamamlamak için, Theia tabanlı  **Cloud IDE** ’yi kullanacaksınız.

---

## ⚠️ Laboratuvar Ortamı Hakkında Önemli Uyarı

Lütfen bu laboratuvar ortamındaki oturumların **kalıcı olmadığını** unutmayın.

Bu nedenle, her bağlandığınızda sizin için **yeni bir ortam** oluşturulur ve önceki oturumda kaydetmiş olabileceğiniz tüm veri veya dosyalar kaybolur.

Verilerinizi kaybetmemek için, bu laboratuvarları **tek bir oturumda** tamamlamayı planlayın.

---

## 🧪 Alıştırma 1 – Ağınız Hakkında Yapılandırma Bilgilerini Görüntüleme

### 🔹 1.1. Sisteminizin hostname’ini ve IP adresini görüntüleme

#### 🏷️ `hostname`

 **Hostname** , bir ağa bağlı bilgisayar veya cihaza atanan isimdir ve bu cihazı tanımlamak ve onunla iletişim kurmak için kullanılır.

Geçerli hostname’i görüntülemek için aşağıdaki komutu çalıştırın:

```bash
hostname
```

**IP adresi** ( *Internet Protocol address* ), İnternet Protokolü’nü iletişim için kullanan bir bilgisayar ağına bağlı her cihaza atanan sayısal etikettir.

Host’unuzun IP adresini görüntülemek için `-i` seçeneğini kullanabilirsiniz:

```bash
hostname -i
```

---

### 🔹 1.2. Ağ arabirimi yapılandırmasını görüntüleme

Aşağıdaki komutları çalıştırarak `iproute2` paketini kurun:

```bash
sudo apt update
sudo apt install iproute2
```

#### 🧰 `iproute2`

`ip` komutu, bir ağ için ağ arabirimi parametrelerini yapılandırmak veya görüntülemek amacıyla kullanılır.

Sisteminizdeki tüm ağ arabirimlerinin yapılandırmasını görüntülemek için şunu girin:

```bash
ip a
```

Belirli bir aygıtın (örneğin `eth0` adlı ethernet adaptörü gibi) yapılandırmasını görüntülemek için şunu girin:

```bash
ip addr show eth0
```

`eth0` genellikle sunucunuzu ağa bağlayan  **birincil ağ arabirimidir** .

Sunucunuzun IP adresini, **2. satırda** `inet` kelimesinden sonra görebilirsiniz.

---

## 🧪 Alıştırma 2 – Ağ Bağlantısını Test Etme

### 🔹 2.1. Bir hosta bağlantıyı test etme

#### 📡 `ping`

`ping` komutunu kullanarak `www.google.com` adresinin ulaşılabilir olup olmadığını kontrol edin.

Bu komut, `www.google.com` sunucusuna veri paketleri göndermeye devam eder ve geri aldığı yanıtı yazdırır.

(Ping işlemini durdurmak için **Ctrl + C** tuşlarına basın.)

```bash
ping www.google.com
```

Sadece sınırlı sayıda ping atmak isterseniz `-c` seçeneğini kullanın:

```bash
ping -c 5 www.google.com
```

---

## 🧪 Alıştırma 3 – Bir Sunucudan Veri Görüntüleme veya İndirme

### 🔹 3.1. Bir sunucudan veri aktarma

#### 🌐 `curl`

Aşağıdaki URL’deki dosyaya `curl` kullanarak erişebilir ve dosyanın içeriğini ekranınızda görüntüleyebilirsiniz:

```bash
curl https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt
```

Verilen URL’deki dosyaya erişmek ve aynı zamanda dosyayı bulunduğunuz çalışma dizinine kaydetmek için `-O` seçeneğini kullanın:

```bash
curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt
```

Eğer URL’sini biliyorsanız, herhangi bir web sayfasının **HTML kodunu görüntülemek** için de `curl` kullanabilirsiniz.

---

### 🔹 3.2. Bir URL’den dosya(lar) indirme

#### 📥 `wget`

`wget` komutu, `curl` komutuna benzerdir, ancak  **birincil kullanımı dosya indirmektir** .

`wget`’in benzersiz özelliklerinden biri, bir URL’deki dosyaları **özyinelemeli (recursive)** olarak indirebilmesidir.

`wget` komutunu iş başında görmek için önce geçerli dizininizden `usdoi.txt` dosyasını silin:

```bash
rm usdoi.txt
```

Ardından, dosyayı `wget` kullanarak tekrar indirin:

```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/usdoi.txt
```

---

## 🧑‍💻 Uygulama Alıştırmaları

Başlamadan önce, aşağıdaki komutları girerek `/home/project` dizininde olduğunuzdan emin olun:

```bash
cd /home/project
pwd
```

---

### 📝 1. Host’unuzun IP adresini görüntüleyin.

**İpucu için tıklayın**

Doğru seçenekle birlikte `hostname` komutunu kullanın.

Not: IP adresinizi `ping` veya `ip` komutlarını kullanarak elde etmenin başka yolları da vardır.

Her ikisi de IP adresinizi gösterecektir, ancak aynı zamanda fazladan birçok bilgi de içerirler.

**Çözüm için tıklayın**

```bash
hostname -i
```

---

### 📝 2. `www.google.com` bağlantınızla ilgili istatistikleri alın.

**İpucu için tıklayın**

`ping` komutunu kullanın.

**Çözüm için tıklayın**

```bash
ping www.google.com
```

---

### 📝 3. `eth0` ethernet adaptörünüz hakkında bilgi görüntüleyin.

**İpucu için tıklayın**

Doğru argümanla `ip` komutunu kullanın.

**Çözüm için tıklayın**

```bash
ip addr show eth0
```

---

### 📝 4. `www.google.com` ana sayfasının HTML kodunu görüntüleyin.

**İpucu için tıklayın**

Doğru argümanla `curl` komutunu kullanın.

**Çözüm için tıklayın**

```bash
curl www.google.com
```

---

### 📝 5. `www.google.com` ana sayfasının HTML kodunu indirin.

**İpucu için tıklayın**

Doğru argümanla `wget` komutunu kullanın.

**Çözüm için tıklayın**

```bash
wget www.google.com
```

Not: `wget`, HTML kodunu `index.html` olarak kaydeder. Bunu aşağıdaki komutla kontrol edebilirsiniz:

```bash
ls -l
```

---

## ✅ Özet

Bu laboratuvarda şunları öğrendiniz:

* `hostname` ve `ip` komutlarını kullanarak ağ yapılandırmanızı görüntülemek
* `ping` komutunu kullanarak bir ağ bağlantısını test etmek
* `curl` ve `wget` komutları ile veri aktarmak
