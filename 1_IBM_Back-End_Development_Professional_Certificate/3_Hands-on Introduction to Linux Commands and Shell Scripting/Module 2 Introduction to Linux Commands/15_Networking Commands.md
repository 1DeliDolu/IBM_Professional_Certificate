# 🌐 Ağ Komutları

Bu “Ağ Komutları”na hoş geldiniz. Bu videoyu izledikten sonra şunları yapabileceksiniz:

* Ağ yapılandırmanızı incelemek
* Bir URL bağlantısının kararlılığını değerlendirmek
* Bir URL’den veriyi tanımlamak ve almak

---

## 🏷️ `hostname` Komutu

`hostname` komutu, bilgisayarınızı benzersiz şekilde tanımlayan  **hostname** ’i ve diğer bilgileri almak veya ayarlamak için kullanılır.

Herhangi bir seçenek olmadan `hostname` komutunu girdiğinizde, makinenizin  **hostname** ’ini döndürür. Bu örnekte hostname, `mylinuxmachine.local` şeklindedir.

Eğer makinenizin yerel bir alan adı ( *local domain* ) ayarı varsa, hostname içinde `.local` son eki görünür.

Alan adı son ekini kaldırmak için, `-s` seçeneğini ekleyebilirsiniz.

`-i` seçeneğini kullanırsanız, `hostname` komutu hostname’e ait IP adresini sağlar.

---

## 📡 `ip` Komutu ile Ağ Arayüzlerini Görüntüleme

`ip` komutu, ağ arayüzü bilgilerini yapılandırmak ve görüntülemek için kullanılan güçlü bir yardımcı programdır.

Cihazınızın iletişim arayüzlerinin tüm ayrıntılarını görmek için aşağıdaki komutu kullanın:

```bash
ip a
```

Bu komut; IP adresleri, MAC adresleri ve diğer arayüze özgü ayrıntılar da dahil olmak üzere kapsamlı bilgiler sağlar.

Bu komut özellikle ağ yapılandırmalarını yöneten sistem yöneticileri için kullanışlıdır.

Belirli bir aygıtın, örneğin `eth0` adlı bir Ethernet adaptörünün ayrıntılarını görüntülemek için şu komutu kullanın:

```bash
ip address show eth0
```

Bu komut, adaptörle ilgili bilgileri gösterir; IP adresi, alınan ve gönderilen paket sayısı ve hatalar, düşen paketler, toplam gönderilen ve alınan veri miktarı gibi temel metrikleri içerir.

---

## 📶 Bağlantı Testi için `ping` Komutu

Bir ana bilgisayara veya IP adresine bağlantıyı test etmek için `ping` komutunu kullanabilirsiniz.

`ping`, **ICMP** (Internet Control Message Protocol) istekleri olarak bilinen paketler gönderir, sunucudan yanıt bekler ve sonucu yazdırır.

Örneğin:

```bash
ping google.com
```

yazarak, her başarılı **echo request** yanıtı için `ping` bir bilgi satırı döndürür ve siz `Ctrl + C` ile sonlandırana kadar devam eder.

`ping` sonlandırıldıktan sonra, ping sonuçlarına dair özet istatistikleri yazdırır.

Her echo isteği için `ping`, aşağıdakiler de dahil olmak üzere yararlı bilgiler raporlar:

* Verilen URL’nin IP adresi, örneğin `142.251.41.68`
* Toplam gidiş-dönüş süresi (round-trip time) – milisaniye cinsinden

Son kısımda verilen istatistikler arasında şunlar yer alır:

* Kaç paket gönderildi ve alındı
* Düşen paketlerin yüzdesi
* Gidiş-dönüş sürelerinin **en düşük, ortalama, en yüksek** değeri
* Ve milisaniye cinsinden standart sapma

Eğer `ping` komutunun belirli sayıda ping sonucu döndürmesini isterseniz, `-c` seçeneğini kullanabilirsiniz.

Örneğin:

```bash
ping -c 5 google.com
```

komutu, beş ping sonucu döndürür, ardından sonlanır ve `-c` seçeneği olmadan vereceğiyle aynı istatistikleri yazdırır.

---

## 🌍 `curl` Komutu ile URL’lerden Veri Aktarma

`curl` komutu, URL’lere veri gönderip URL’lerden veri almanızı sağlayan ve birçok farklı protokolü destekleyen güçlü bir araçtır.

Aşağıdaki komutu girdiğinizde:

```bash
curl www.google.com
```

`www.google.com` adresindeki açılış sayfasının HTML içeriğinin tamamı, varsayılan HTTP protokolü kullanılarak döndürülür.

Burada örneğin, Google G logosu için bir PNG dosyasının yolunu görebilirsiniz.

Bu logoyu, tarayıcınızda `google.com` adresine bu yolunu ekleyerek görüntüleyebilirsiniz.

`curl` komutuna, bir URL’nin içeriğini yerel bir dosyaya yazdırmasını da sağlayabilirsiniz. Bu, `-o` seçeneği kullanılarak yapılır.

Örneğin, şu komutu girebilirsiniz:

```bash
curl www.google.com -o google.txt
```

Daha sonra `google.txt` dosyasının içeriğini `head` komutunu kullanarak görüntüleyebilir ve dosya içeriğinin gerçekten önceki çıktıyla eşleştiğini doğrulayabilirsiniz.

---

## 📥 `wget` Komutu ile Dosya İndirme

`curl` komutuna benzer şekilde, `wget` komutu da bir URL’de bulunan dosyaları almak için kullanılır.

`wget`, bir URL’de bulunan bir dosyayı veya bir web sayfasının HTML kodunu alabilmesi bakımından `curl`’e benzer; ancak protokol desteği açısından daha özelleşmiştir ve **özyinelemeli (recursive)** indirme yeteneklerine sahiptir.

Bu, bir URL’nin birden çok dosya içeren bir klasöre işaret edebildiği durumlarda kullanışlıdır.

Burada, `wget` komutunu `w3.org` tarafından barındırılan `iso_8859-1.txt` adlı tek bir test dosyasını indirmek için kullanırsınız.

`wget`, indirirken aşağıdaki türden bilgiler döndürür:

* Hedef sunucunun ad çözümlemesi ve sunucuya bağlanma
* HTTP isteğinin gönderilmesi
* Yanıtın beklenmesi
* Ve dosyanın kaydedilmesi

Dosyayı, bulunduğunuz dizine otomatik olarak adlandırıp kaydeder.

Başvuru için, tarayıcınızda bu URL’deki veriye baktığınızda gördüğünüz şudur: basit bir metin dosyası.

Aşağıdaki komutu girerek:

```bash
head -12 iso_8859-1.txt
```

indirilen dosyanın içeriğinin ilk on iki satırını görürsünüz.

Beklendiği gibi, dosya az önceki slaytta gördüğünüzle tamamen aynı veriyi içerir.

---

## ✅ Özet

Bu videoda şunları öğrendiniz:

* `hostname` komutunun, hostname’i almak veya ayarlamak için kullanıldığını
* `ip` komutunun, cihazınızdaki tüm iletişim arayüzleri hakkında ayrıntılı bilgi görüntülediğini
* Bir ana bilgisayara veya IP adresine bağlantıyı test etmek için `ping` komutunu kullanabileceğinizi
* `curl` komutunun, URL’lere veri gönderip URL’lerden veri almanızı sağladığını
* `wget` komutunun, bir URL’de bulunan dosyaları almak için kullanıldığını
