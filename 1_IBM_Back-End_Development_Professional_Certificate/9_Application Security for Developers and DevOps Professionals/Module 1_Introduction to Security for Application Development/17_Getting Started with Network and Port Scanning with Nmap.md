# 🚀 Nmap ile Ağ ve Port Taramasına Başlangıç

Bu okumada, **Nmap** hakkında genel bir bakış edineceksiniz.

---

## 🎯 Hedefler

Bu okumayı tamamladıktan sonra şunları yapabileceksiniz:

* **Nmap’in (Network Mapper) önemini açıklamak**
* **Nmap’in çeşitli kullanım alanlarını açıklamak**
* **Nmap’in tarihsel arka planını tanımak**
* **Nmap’in farklı kullanıcı kitlesini belirlemek**

---

## 🛰️ Nmap’e Giriş

Nmap, *Network Mapper* ifadesinin kısaltması olan, açık kaynaklı bir ağ tarama ve güvenlik denetimi aracıdır.

Ağ cihazlarını, servisleri ve işletim sistemlerini tespit etmek ve parmak izini çıkarmak, ayrıca güvenlik açıklarını belirlemek için kullanılır.

Ağda açık portları taramak, işletim sistemlerini tespit etmek ve  *buffer overflow* , saldırı girişimleri ( *intrusions* ) ve hizmet engelleme ( *denial-of-service* ) saldırıları gibi zafiyetleri tespit etmek için kullanılabilir.

Nmap, güvenlik denetimlerinde, sızma testlerinde ve sistem yönetiminde yaygın olarak kullanılır.

Gordon Lyon (takma adıyla  **Fyodor** ) tarafından geliştirilmiş ve ilk kez Eylül 1997’de yayımlanmıştır.

Nmap, bir bilgisayar ağındaki ana bilgisayarları ( *hosts* ) ve servisleri keşfetmek ve böylece ağın yapısının bir haritasını çıkarmak için tasarlanmıştır.

Bu araç, çok yönlülüğü ve kapsamlı yetenekleri nedeniyle ağ güvenliği alanında büyük bir popülerlik kazanmıştır.

---

## 👥 Nmap’i Kimler Kullanır?

Nmap, ağ yöneticileri, güvenlik uzmanları, sızma testi uzmanları, sistem yöneticileri ve meraklı kullanıcılar dahil olmak üzere geniş bir kullanıcı kitlesi tarafından kullanılır.

Esnekliği ve çeşitli özellikleri, onu rutin ağ izleme işlemlerinden gelişmiş güvenlik değerlendirmelerine kadar pek çok uygulama için uygun hale getirir.

---

## 🧩 Nmap’in Hedef Kullanıcıları

Nmap, siber güvenlik ve BT toplulukları içinde farklı roller ve amaçlar için kullanılan çok yönlü ve yaygın bir araçtır.

Nmap’in başlıca hedef kullanıcı gruplarından bazıları şunlardır:

### 🛠️ Ağ Yöneticileri

Ağ yöneticileri, Nmap’i:

* Ağ varlıklarını keşfetmek ve haritalamak,
* Ağ sağlığını izlemek,
* Yanlış yapılandırmaları belirlemek,
* Yalnızca yetkili servislerin dışarıya açıldığından emin olmak

için kullanırlar.

### 🛡️ Güvenlik Profesyonelleri

Güvenlik analistleri, sızma testi uzmanları ve etik hacker’lar Nmap’i:

* Ağların güvenlik durumunu değerlendirmek,
* Açık portları, servisleri ve potansiyel zafiyetleri tespit etmek,
* Olası saldırı vektörlerini ortaya çıkarmak için sızma testleri gerçekleştirmek

amacıyla kullanırlar.

### 🖥️ Sistem Yöneticileri

Sistem yöneticileri Nmap’i:

* Ağ bağlantısı sorunlarını gidermek,
* Ağla ilgili problemleri teşhis etmek,
* Servislerin ve portların doğru yapılandırıldığından emin olmak

için kullanırlar.

### 📊 BT Yöneticileri

BT yöneticileri, Nmap’i:

* Ağ altyapısı hakkında içgörü elde etmek,
* Güvenlik önlemleriyle ilgili bilinçli kararlar almak,
* Mevcut güvenlik kontrollerinin etkinliğini değerlendirmek

için kullanırlar.

### 🎯 Sızma Testi Uzmanları

Sızma testi uzmanları Nmap’i, bir ağ savunmasındaki:

* Olası giriş noktalarını,
* Güvenlik açıklarını,
* Zayıf yönleri

belirlemek için kullanırlar.

Nmap’in kapsamlı tarama yetenekleri, gerçek dünyadaki saldırıları simüle etmek için değerlidir.

### 🧭 Güvenlik Danışmanları

Güvenlik danışmanları, kuruluşlara:

* Ağ güvenliğini iyileştirme,
* Riskleri azaltma

konularında uzman tavsiyesi ve öneriler sunmak için Nmap’ten yararlanırlar.

### ✅ Uyum ve Denetim Uzmanları

Uyum ve denetimden sorumlu profesyoneller Nmap’i:

* Ağ yapılandırmalarını değerlendirmek,
* Güvenlik standartlarına uygunluğu doğrulamak,
* Regülasyon gerekliliklerini etkileyebilecek potansiyel zafiyetleri belirlemek

için kullanırlar.

### 🔬 Araştırmacılar

Araştırmacılar ve akademisyenler Nmap’i:

* Çalışmalar yürütmek,
* Veri toplamak,
* Ağ güvenliği ve siber güvenlik tehditlerine ilişkin anlayışa katkıda bulunmak

amacıyla kullanırlar.

### 🎓 Eğitmenler

Siber güvenlik eğitmenleri, müfredatlarının bir parçası olarak öğrencilere:

* Ağ taraması,
* Güvenlik değerlendirmesi,
* Zafiyet analizi

konularını öğretmek için Nmap kullanırlar.

### 💻 Açık Kaynak Meraklıları

Nmap açık kaynaklı bir yazılımdır ve:

* Ağ,
* Güvenlik,
* Teknoloji

ile ilgilenen meraklı kullanıcılar, pratik deneyim kazanmak ve Nmap’in geliştirilmesine katkıda bulunmak için bu aracı kullanabilirler.

Nmap’in çok yönlülüğü ve yetenekleri, onu ağ ortamlarını güvence altına alma, yönetme ve analiz etme süreçlerine dahil olan geniş bir profesyonel yelpazesi için değerli bir araç haline getirir.

Nmap’in güçlü bir araç olduğunu ve kullanımının her zaman etik ilkelere ve yasal sınırlara uygun olması gerektiğini unutmamak önemlidir.

---

## 🎯 Nmap’in Amacı

Nmap’in birincil amacı, **ağ keşfi** ve  **güvenlik denetimidir** .

Nmap, kullanıcıların:

* Bir ağ üzerindeki aktif ana makineleri ( *hosts* ) belirlemesine,
* Açık portları ve servisleri keşfetmesine,
* Bu ana makinelerde çalışan işletim sistemlerini tespit etmesine

yardımcı olur.

Nmap ayrıca, bir ağ altyapısı içindeki potansiyel güvenlik risklerini ve zayıf noktaları belirleyerek zafiyet değerlendirmesine de destek olur.

---

## 🔍 Nmap Tarama Türleri ve Örnekleri

### 🔗 TCP Connect Tarama (Varsayılan Tarama)

Temel tarama türüdür ve her hedef portla tam bir TCP bağlantısı kurar.

* Örnek komut:
  ```bash
  nmap -sT target
  ```

---

### 🕵️ SYN Stealth Tarama

Yarı açık ( *half-open* ) tarama olarak da bilinir; **SYN** paketleri gönderir ve yanıtları analiz eder.

* Örnek komut:
  ```bash
  nmap -sS target
  ```

---

### 📡 UDP Tarama

Hedef portlara **UDP** paketleri göndererek açık UDP servislerini belirlemeye çalışır.

* Örnek komut:
  ```bash
  nmap -sU target
  ```

---

### 🚧 ACK Tarama

Güvenlik duvarı yapılandırmalarını belirlemek için **TCP ACK** paketleri gönderir.

* Örnek komut:
  ```bash
  nmap -sA target
  ```

---

### 🧬 Sürüm Tespiti (`-sV`)

Açık portlarda çalışan servislerin **sürüm bilgilerini** tespit etmeye çalışır.

* Örnek komut:
  ```bash
  nmap -sV target
  ```

---

### 💻 İşletim Sistemi Tespiti (`-O`)

Hedefin işletim sistemini belirlemeye çalışır.

* Örnek komut:
  ```bash
  nmap -O target
  ```

---

### 📜 Betik Taraması (`-sC`)

Önceden tanımlanmış betikleri çalıştırarak ek bilgi toplar.

* Örnek komut:
  ```bash
  nmap -sC target
  ```

---

### 📶 Ping Taramaları

Hedefin erişilebilirliğini kontrol etmek için çeşitli ping tekniklerini kullanır.

* Örnek komut (ICMP Echo Request):
  ```bash
  nmap -PE target
  ```

---

### 🧭 Traceroute (`--traceroute`)

Paketlerin izlediği yolu belirlemek için **traceroute** işlemi gerçekleştirir.

* Örnek komut:
  ```bash
  nmap --traceroute target
  ```

---

### 🕳️ TCP Null Tarama

Hiçbir TCP bayrağı ( *flag* ) ayarlanmamış paketler gönderir ve yanıtları gözlemler.

* Örnek komut:
  ```bash
  nmap -sN target
  ```

---

### 🧨 TCP FIN Tarama

Yalnızca **FIN** bayrağı ayarlı paketler gönderir ve yanıtları gözlemler.

* Örnek komut:
  ```bash
  nmap -sF target
  ```

---

### 🎄 TCP Xmas Tarama

Birden fazla TCP bayrağı ayarlı (Xmas ağacı gibi “yakılmış”) paketler gönderir ve yanıtları gözlemler.

* Örnek komut:
  ```bash
  nmap -sX target
  ```

---

### 🧠 Tarama Türlerinin Amacı

Her tarama türü, hedef ağ hakkında bilgi toplamada belirli bir amaca hizmet eder.

Hangi bilgiyi edinmek istediğinize ve ne kadar görünürlük (veya gizlilik) istediğinize bağlı olarak kullanılacak tarama türü seçilir.

> Not: Nmap’i her zaman sorumlu bir şekilde kullanın ve hedef ağı taramak için gerekli izinlere sahip olduğunuzdan emin olun.

---

## 📈 Nmap’in Evrimi ve Tarihi

Nmap, başlangıçta Fyodor tarafından basit bir ağ tarama aracı olarak geliştirilmiştir.

Yıllar içinde güçlü ve kapsamlı bir ağ haritalama ve güvenlik değerlendirme aracına dönüşmüştür.

Fyodor’un sürekli özverisi ve aktif bir katkıcı topluluğu sayesinde Nmap’in yetenekleri düzenli olarak geliştirilmiş ve genişletilmiştir.

Nmap’in geliştirme geçmişi, aşağıdaki gelişmiş özelliklerin eklenmesini içerir:

* İşletim sistemi tespiti ( *OS detection* ),
* Sürüm tespiti ( *version detection* ),
* Betik motoru ( **Nmap Scripting Engine – NSE** ),
* Performans iyileştirmeleri.

Nmap’in benimsenmesi hızla artmış ve dünya çapında ağ yöneticileri ve güvenlik uzmanları için vazgeçilmez bir araç haline gelmiştir.

---

## 🧪 Piyasadaki Benzer Ürünler

Nmap, tanınmış ve yaygın olarak kullanılan bir ağ tarama aracı olmakla birlikte, piyasada bulunan birkaç benzer ürün de mevcuttur.

Bunlardan bazıları şunlardır:

### ⚡ Zmap

 **Zmap** , büyük ölçekli, tüm interneti kapsayan ağ araştırmaları için tasarlanmış, hızlı ve açık kaynaklı bir ağ tarayıcıdır.

Ağ keşfi ve veri toplama üzerine odaklanır.

### 🚀 Masscan

 **Masscan** , internet ölçeğinde tarama için tasarlanmış bir diğer yüksek hızlı ağ tarayıcıdır.

Tüm IPv4 adres uzayını birkaç dakika içinde tarayabilecek kapasiteye sahiptir.

### 🛡️ OpenVAS

 **Open Vulnerability Assessment System (OpenVAS)** , ağlarda güvenlik denetimleri gerçekleştiren ve tespit edilen zafiyetlere ilişkin ayrıntılı raporlar sunan kapsamlı bir zafiyet tarayıcısıdır.

### 🖼️ Zenmap

 **Zenmap** , Nmap’in grafik kullanıcı arayüzü (GUI) sürümüdür.

Nmap taramalarının görsel bir gösterimini sağlar ve taramaları yapılandırmak ve başlatmak için daha kolay bir yol sunar.

### 📡 Wireshark

 **Wireshark** , öncelikle bir ağ protokol analizörü olmakla birlikte, ağ keşfi ve güvenlik analizi için de kullanılabilir.

Ağ üzerinden geçen paketleri yakalar ve analiz eder.

---

## ✅ Sonuç

Sonuç olarak, Nmap zengin bir geçmişe ve sürekli bir evrime sahip, güçlü ve yaygın olarak kullanılan bir ağ tarama aracıdır.

Uyarlanabilirliği, sağlamlığı ve kapsamlı özellik seti, onu ağ yöneticileri ve güvenlik uzmanları için vazgeçilmez bir varlık haline getirmektedir.

Nmap hakkında daha fazla bilgi edinmek için **Nmap Network Scanning sitesi**ni inceleyebilirsiniz.

---

## ✍️ Yazar

**Anita Verma**

---

## 📅 Değişiklik Günlüğü (Changelog)

| Date       | Version | Changed by   | Change Description            |
| ---------- | ------- | ------------ | ----------------------------- |
| 16-08-2023 | 0.3     | Steve Hord   | QA pass with edits            |
| 15-08-2023 | 0.2     | Rashi Kapoor | ID review, LO, grammar review |
| 09-08-2023 | 0.1     | Anita Verma  | Initial version created       |

---

## 📌 Öne Çıkan Maddeler

* **Etik Kullanım:** Nmap güçlü bir araç olmakla birlikte, yetkisiz erişim ve izinsiz taramaları önlemek için kullanımı etik ilkelere ve yasal sınırlara uygun olmalıdır.
* **Nmap:**  *Network Mapper* ’ın kısaltması olan Nmap, ağ taraması ve güvenlik denetimi için kullanılan, cihazları, servisleri ve zafiyetleri tespit edebilen açık kaynaklı bir araçtır.
* **Kullanıcı Tabanı:** Nmap; ağ yöneticileri, güvenlik uzmanları, sızma testi uzmanları ve eğitmenler gibi pek çok kişi tarafından çeşitli ağ yönetimi ve güvenlik görevleri için kullanılmaktadır.
* **Nmap Tarama Türleri:** Nmap; TCP Connect Tarama, SYN Stealth Tarama ve İşletim Sistemi Tespiti gibi, her biri ağ hakkında belirli türde bilgi toplama amacına hizmet eden çeşitli tarama türlerini destekler.
* **Ağ Keşfi:** Nmap’in temel amacı, bir ağ üzerindeki aktif ana makineleri belirlemek, açık portları ve servisleri keşfetmek ve bu ana makinelerde çalışan işletim sistemlerini tespit etmektir.
