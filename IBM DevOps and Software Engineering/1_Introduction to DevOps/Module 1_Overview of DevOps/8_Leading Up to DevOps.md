## 🚀 Leading Up to DevOps

Bu videoyu izledikten sonra şunları yapabileceksiniz: **Waterfall (Şelale) yönteminin sorunlarını açıklamak** ve  **DevOps öncesinde yazılım geliştirme ile operasyonlar arasındaki tipik ilişkiyi tanımlamak** .

DevOps’un çözdüğü problemi tam olarak anlayabilmek için bizi DevOps’a getiren süreci anlamak önemlidir.

---

### 🏗️ Waterfall Sürecinin Başlangıcı

Mimarlar aylarca, hatta aylar boyunca sistemi kâğıt üzerinde tasarlardı.
Gereksinim dokümanları, tasarım dokümanları,  **üst seviye tasarımlar** , **alt seviye tasarımlar** ve **sistem seviyesi tasarımlar** oluşturulurdu.

Ancak bundan sonra geliştirme aşamasına geçilirdi.
Geliştiriciler, izole edilmiş bir geliştirme ortamında aylarca özellikler üzerinde çalışırlardı.

Kod geliştirilirken, eğer tasarımlar yanlışsa mimarlara geri dönmek  **çok maliyetliydi** .

---

### 🧪 Test ve Dağıtım Aşamaları

Tüm kod geliştirildikten sonra test aşamasına geçilirdi.
Bu aşamada  **tüm kod bir kerede test edilirdi** .

Test sürecinde bulunan hatalar açılır ve **1. veya 2. seviye kritik hata kalmayana kadar** kod geliştirmeye geri gönderilirdi.

Bir noktada geliştirme ekibi kodu **dağıtım için operasyonlara** teslim ederdi.

Bu dağıtım, kod yazıldıktan  **aylar sonra** , hatta bazen **bir yıl sonra** gerçekleşirdi.
Bazı projeler **iki yıla kadar** sürebilirdi.

---

### ⚙️ Operasyonların Karşılaştığı Zorluklar

Operasyon ekibi, geliştiricilerin ne inşa ettiğine dair neredeyse hiçbir bilgiye sahip olmadığı için dağıtımı çok uzun sürede gerçekleştirirdi.

Dağıtımdan sonra sistemi  **çalışır halde tutma sorumluluğu tamamen operasyon ekibine ait olurdu** .

Bu çalışma biçimine **Waterfall (Şelale) yöntemi** denir.

---

### 🪜 Waterfall Yönteminin Aşamaları

Waterfall yaklaşımında her şey **fazlar halinde** gerçekleşir:

* Gereksinimler toplanır ve bir **gereksinim dokümanı** oluşturulur, faz biter.
* Bu çıktılar bir sonraki faza aktarılır.
* Tasarım fazında tüm tasarımlar yapılır ve belgelenir, faz biter.
* Tasarım çıktıları geliştirme fazına aktarılır.
* Geliştiriciler, alt seviye tasarım dokümanlarını alarak kodu yazar.

Her fazın **giriş ve çıkış kriterleri** vardır.

---

### 🔌 Entegrasyon ve Testte Ortaya Çıkan Sorunlar

Bu süreç boyunca herkes  **izole şekilde kod yazar** ; modüller birbirleriyle entegre edilmez.

Entegrasyon fazına gelindiğinde, tüm modüller ilk kez bir araya getirilir.
İşte bu noktada parçaların birlikte çalışıp çalışmadığı  **ilk kez anlaşılır** .

Ardından test fazına geçilir.
Hatalar bulunduğunda, ekiplerin tekrar  **şelalede yukarı doğru yüzmesi** , yani kodlama fazına geri dönmesi gerekir.

Bu nedenle bu yönteme *Waterfall* denir; çünkü geriye dönmek,  **bir şelaleye karşı yüzmeye çalışmak gibidir** .

---

### 🔄 Geri Dönüşlerin Zorluğu

Sorun yaşandığında tasarım fazına kadar geri dönmek gerekebilir.

Üstelik yazılım geliştirme, **inşaat mühendisliği projeleri gibi** ele alındığı için:

* Mimarlar başka projelere geçmiştir
* Tasarımcılar artık ekipte değildir

Onları tekrar bulup tasarımı değiştirmek gerekir.
Sonrasında geliştiriciler kodu değiştirir ve bu sefer entegre olmasını umut ederler.

Bu süreç  **çok hataya açık** , **yüksek riskli** ve  **geç değişikliklere kapalıdır** .

---

### ⚠️ Waterfall Yönteminin Temel Sorunları

Bu yaklaşımın başlıca sorunları şunlardır:

* **Değişime yer yoktur**
* Fazlar arası geri dönüş mümkün değildir
* **Ara teslimatlar yoktur**
* Yazılımın çalışıp çalışmadığı **ancak en sonda anlaşılır**
* Sorunlar fazlar arasında aşağı doğru aktarılır
* Bilgi kaybı ve hatalar sık yaşanır
* Geç bulunan hatalar **çok pahalıya mal olur**
* Uzun teslim süreleri oluşur

---

### 🧱 Silo Yapısı ve Operasyonların Yükü

Takımlar birbirlerinden habersiz çalışır:

* Tasarımcılar kod üzerindeki etkilerini bilmez
* Geliştiriciler test ve entegrasyonu düşünmez
* Herkes kendi fazının **silosunda** çalışır

En korkutucu olan ise,  **kodu en az bilen ekip olan operasyonların** ,
o kodu **dağıtması, çalıştırması ve üretimde yönetmesi** beklenir.

---

### 📌 Video Özeti

Bu videoda şunları öğrendiniz:

* Geleneksel  **Waterfall geliştirme modeli** , gecikmelere, hayal kırıklıklarına, uzun teslim sürelerine ve geç değişikliklerin yüksek maliyetli olmasına yol açar.
* Operasyon ekipleri,  **tanımadıkları kodları yönetmek zorunda kalır** .
* Geçmişte yazılım geliştiriciler ve operasyon ekipleri **birlikte değil, silo halinde** çalışmıştır.
