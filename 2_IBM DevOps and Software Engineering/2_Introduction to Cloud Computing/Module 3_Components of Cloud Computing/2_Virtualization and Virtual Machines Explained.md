# 🧩 Virtualization ve Sanal Makineler Açıklaması

Merhaba. Ben IBM Cloud ekibinden Kaleigh Bovey ve bugün sanallaştırma hakkında konuşacağız. Bildiğiniz gibi *sanallaştırma* oldukça eski bir teknolojidir, ancak bugün bulut bilişim stratejimizi oluşturmak için hâlâ son derece önemlidir.

Öncelikle, sanallaştırma nedir? Basitçe söylemek gerekirse, sanallaştırma; ister işlem gücü ( *compute* ), depolama ( *storage* ), ağ ( *networking* ), sunucular ( *servers* ) veya uygulamalar ( *applications* ) olsun, bir şeyin yazılım tabanlı ya da “sanal” bir sürümünü oluşturma sürecidir. Sanallaştırmayı mümkün kılan şey ise *hypervisor* adı verilen bir bileşendir. Bunu buraya yazacağız.

Bir  *hypervisor* , fiziksel sunucunun (ya da  *host* ’un) üzerinde çalışan bir yazılımdır.

---

## 🧠 Hypervisor Türleri

Piyasada birkaç farklı *hypervisor* türü vardır. Bunların yaptığı şey temelde, fiziksel sunucudaki kaynakları toplayıp sanal ortamlarınıza tahsis etmektir.

İki ana *hypervisor* türü vardır:

* **Type 1**
* **Type 2**

Şimdi **Type 1** ile başlayalım.

---

## 🏗️ Type 1 Hypervisor

 **Type 1 hypervisor** , doğrudan fiziksel sunucunun üstüne kurulan bir *hypervisor* türüdür. Bunlara **bare-metal hypervisor** da denir. Hatırlamanız için bunu buraya yazacağız.

Bunlar en sık kullanılan *hypervisor* türleridir ve en güvenli olanlardır, gecikmeyi ( *latency* ) düşürürler ve piyasada en çok göreceğiniz türdür.

Örnekler:

* VMware **ESXi**
* Microsoft **Hyper-V**
* Açık kaynak **KVM**

---

## 🧱 Type 2 Hypervisor

Diğer *hypervisor* türü ise burada,  **Type 2 hypervisor** .

Bunları farklı yapan şey, fiziksel sunucu ile *hypervisor* arasında bir **host işletim sistemi (host OS)** katmanının bulunmasıdır. Bu nedenle bunlara **Hosted** de denir.

Bunlar çok daha az yaygındır. Genellikle son kullanıcı sanallaştırması ( *end-user virtualization* ) için kullanılır ve piyasada şu isimlerle görebilirsiniz:

* Oracle **VirtualBox**
* VMware **Workstation**

Yine, çok daha az yaygındırlar.  **Type 1 hypervisor** ’a göre gecikmeleri ( *latency* ) daha yüksektir.

---

## 💻 Sanal Makineler ve Sanal Ortamlar

Hypervisor’unuzu kurduktan sonra sanal ortamlar ya da sanal makineler, yani kısaca  **VM** ’ler oluşturabilirsiniz. Haydi birkaç ortam kuralım.

Peki bir VM’i VM yapan nedir?  **VM** , basitçe yazılım tabanlı bir bilgisayardır. Fiziksel bir bilgisayar gibi çalışır. Bir işletim sistemi ve uygulamalara sahiptir ve birbirlerinden tamamen bağımsızdırlar.

Ancak bir *hypervisor* üzerinde birden fazla VM çalıştırabilirsiniz ve  *hypervisor* , fiziksel sunucudan alınan kaynakların bu sanal ortamlara nasıl tahsis edildiğini yönetir.

Bağımsız oldukları için, farklı sanal makinelerde farklı işletim sistemleri çalıştırabilirsiniz. Örneğin:

* Burada **Windows**
* Burada **Linux**
* Burada **UNIX**

---

## 🚚 Taşınabilirlik ve Esneklik

Bağımsız oldukları için ayrıca son derece taşınabilirdirler. Bir sanal makineyi, tamamen farklı bir makinedeki başka bir  *hypervisor* ’a neredeyse anında taşıyabilirsiniz. Bu da ortamınız içinde size çok fazla esneklik ve taşınabilirlik sağlar.

Bütün bunlara baktığınızda, bu sanallaştırmanın süreç olarak özüdür.

---

## ✅ Sanallaştırmanın Temel Faydaları

Buradan almanız gereken birkaç temel faydadan bahsedelim:

### 1) 💰 Maliyet Tasarrufu

Bunu düşündüğünüzde, tek bir altyapı parçası üzerinden birden fazla sanal ortam çalıştırabilmeniz, fiziksel altyapı ayak izinizi ciddi şekilde azaltabileceğiniz anlamına gelir.

Bu, özünde konsolidasyondur ve çok daha az sayıda sunucu bakımına ihtiyaç duymanız, daha az elektrik tüketmeniz, bakım maliyetlerinden tasarruf etmeniz demektir. Sonuç olarak günün sonunda kârlılığınıza katkı sağlar.

### 2) ⚡ Çeviklik ve Hız

Dediğim gibi, bir sanal makineyi ayağa kaldırmak nispeten kolay ve hızlıdır. Geliştiricileriniz yeni bir ortam istediklerinde, örneğin bir *dev test* senaryosu çalıştırmak için yeni bir ortam kurmak istediklerinde, tamamen yeni bir ortam sağlamak ( *provisioning* ) çok daha zahmetlidir. Sanallaştırma bu süreci çok daha basit ve hızlı hâle getirir.

### 3) 🛠️ Kesinti Süresini Azaltma

Diyelim ki bu *host* beklenmedik şekilde devre dışı kaldı. Sanal makineleri bir  *hypervisor* ’dan başka bir  *hypervisor* ’a (farklı bir fiziksel sunucu üzerinde) taşıyabildiğiniz için, iyi bir yedek planınız olur, değil mi?

Yani bu *host* çökerse, VM’lerinizi çok hızlı biçimde çalışan başka bir makinedeki başka bir  *hypervisor* ’a taşıyabilirsiniz.

---

## ☁️ Kapanış

Sanallaştırma ve VM’ler, bulut bilişimin merkezindedir ve birçok fayda sağlar. Bir sonraki videoda sanal makine türlerini ele alacağız.
