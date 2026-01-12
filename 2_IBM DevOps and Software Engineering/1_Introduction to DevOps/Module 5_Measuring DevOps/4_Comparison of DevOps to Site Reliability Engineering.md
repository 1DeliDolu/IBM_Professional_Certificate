# 🧩 DevOps ile Site Reliability Engineering Karşılaştırması

Bu videoyu izledikten sonra şunları yapabileceksiniz:
*Site Reliability Engineering’in* (SRE) *DevOps’tan* nasıl farklılaştığını fark etmek
*Site Reliability Engineering* ile *DevOps* arasındaki ortak noktaları fark etmek
*Site Reliability Engineering* ve *DevOps’un* birlikte nasıl kullanılabileceğini açıklamak

*DevOps’un* *Site Reliability Engineering* (SRE) ile nasıl karşılaştırıldığını merak ediyor olabilirsiniz. Bu konuyu incelemeden önce, muhtemelen *SRE’nin* ne olduğunu, *DevOps’tan* nasıl farklılaştığını ve bir *DevOps* ortamında *SRE’yi* nasıl kullanabileceğinizi açıklamalıyız.

Benjamin Treynor Sloss’a göre, *SRE* “…bir yazılım mühendisinin, eskiden operasyonlar olarak adlandırılan işle görevli kılınmasıyla ortaya çıkan şeydir.” Çoğu sistem yöneticisi, aynı manuel görevleri gün be gün yapmaktan mutludur; belki de bunun, bu manuel görevleri yapmak onların işi olduğunu düşündükleri içindir.

Ancak bir yazılım mühendisinden bir sunucu kurmasını isterseniz, muhtemelen ilk seferinde bunu manuel olarak yapacaktır. Birkaç gün sonra ondan ilkine tıpatıp benzeyen bir başka sunucu kurmasını isterseniz, onu da manuel olarak yapabilir. Fakat üçüncü sunucu istendiğinde, bir yazılım mühendisi muhtemelen sunucuyu otomatik olarak kuran bir program yazmaya başlayacaktır.

## 🧠 Yazılım Mühendislerinin Düşünme Biçimi ve Otomasyon

Bu, yazılım mühendislerinin düşünme biçimidir. Onlar programcıdır; program yazarlar. *Site reliability engineer’ların* amacı, kendilerini işsiz bırakacak kadar otomasyon yapmaktır. Elbette bu asla gerçekleşmez; çünkü her zaman otomatikleştirilecek daha fazla şey vardır.

*SRE’nin* ilkelerinden biri, yalnızca yazılım mühendislerini işe almaktır. Tekrarlayan görevleri *Infrastructure as Code* kullanarak otomatikleştirebilmeleri için kod yazmayı bilen insanlara ihtiyacınız vardır.  *Site reliability engineer’lar* , *toil’i* azaltmaya odaklanır; yani tekrarlayan, manuel görevleri.

## 🛠️ Toil Azaltma ve Zaman Dağılımı

Bunu otomasyon yoluyla yapabilmek için zamanlarının yaklaşık %50’sini *toil’i* azaltmaya ayırmaları önerilir. Fikir şudur: tekrar tekrar yaptığınız her şey otomatikleştirilmelidir. Aynı manuel görevi her gün yapmamalısınız.

## 🧱 Takım Yapısı: SRE ve DevOps Arasındaki Büyük Fark

*SRE* ekipleri, geliştirme ekiplerinden ayrıdır. Bu, *DevOps* ile *SRE* arasındaki büyük bir farktır.  *DevOps* , ayrı *silo* ekiplerde çalışmanın verimsiz olduğunun kabulüdür. Ancak  *SRE* , diğer yandan, bu *silo’ları* yerinde tutar.

Geliştirme ekibi, operasyon ekibinden ayrı ve farklı bir ekiptir. *SRE’de* stabilite, *error budgets* olarak bilinen bir şeyle kontrol edilir. Geliştiricilerin, üretimde çok fazla kesinti yaratmadıkları sürece uygulamalarını üretime dağıtmalarına izin verilir. Hataların neden olduğu izin verilen kesintilerin üst sınırı  *error budget’tır* .

## 📉 Error Budget ve Uptime Örneği

Örneğin, %99,9 çalışma süresi ( *uptime* ) olan bir  *service level agreement* ’ınız olsun. Bu, ayda yaklaşık 44 saniye kesinti anlamına gelir. Kesintiler ayda 44 saniyenin altında kaldığı sürece geliştiriciler sürümlerini üretime dağıtmaya devam etmekte özgürdür.

Geliştiriciler, *error budget’ı* aşacak kadar kesintiye neden olduktan sonra artık üretime dağıtım yapmalarına izin verilmez. Bu aslında oldukça iyi çalışır. Geliştiricilerin operasyonları beklemesi sorununu çözerken, üretim ortamının stabilitesi üzerinde operasyonlara kontrol sağlar.

## 🔄 Operasyon Rotasyonu ve Denge Mekanizması

*SRE* ile ilgili son bir şey: geliştiriciler, *SRE* ekibinin günlük olarak ne yaptığını anlamaları için zamanlarının yaklaşık %5’ini operasyon ekibinde rotasyonla geçirir. Ayrıca çok fazla kesintiye neden olurlarsa veya  *toil* , *site reliability engineer’ın* zamanının %50’sini aşarsa, işleri tekrar dengeye getirmeye yardımcı olmak için daha fazla geliştirici operasyonlara kaydırılır.

## 👥 Personel Havuzu ve Organizasyonel Denge

*SRE* ve *DevOps* arasında ekip oluşturma açısından büyük bir fark vardır. Öğrendiğimiz gibi, *SRE* ayrı geliştirme ve operasyon ekiplerini sürdürür, ancak tek bir personel havuzuna sahiptir.

Bu, bir *site reliability engineer* daha gerekiyorsa geliştiricilerden birini almanız anlamına gelir. Bir geliştirici daha istiyorsanız, *site reliability engineer’lardan* birini alırsınız. Bu, dengeyi sağlama çabasıdır.

Buna karşılık  *DevOps* , yazılımı üretime hızlı ve güvenli şekilde dağıtmak gibi ortak bir iş hedefi olan tek bir takımda *silo’ları* yıkar.

## 🧯 Üretim Stabilitesini Sağlama Yaklaşımı

*DevOps* ile *SRE* arasındaki diğer büyük fark, üretim stabilitesini nasıl sağladıklarıdır. Söylediğimiz gibi,  *SRE* , geliştirme ekibinin uyması gereken ve  *service-level objectives* ’a dayanan *error budgets* kullanır. Bir geliştirici *error budget’ı* aşıp üretimi istikrarsız hale getirdiğinde artık üretime dağıtım yapamaz.

Buna karşılık  *DevOps* , stabiliteyi *Continuous Delivery* boru hatları ( *pipelines* ) üzerinden otomasyon kullanarak ve üretimde çalışan koddan herkesin sorumlu olmasını sağlayarak korur. *DevOps’un* “ *you build it, you run it* ” şeklinde bir mantrası vardır. *SRE’den* farklı olarak, geliştiriciler uygulamalarından üretimde de sorumludur.

## 🤝 Ortak Noktalar: Görünürlük, Suçlamasız Kültür ve Hedefler

İki uygulama arasında ortak noktalar vardır. Her ikisi de geliştirme ve operasyonların birbirine görünür olmasını sağlamaya çalışır. İster *SRE’de* olduğu gibi geliştiriciler operasyonlarda rotasyonla çalışsın, ister *DevOps’ta* olduğu gibi geliştirme ve operasyon aynı takımda olsun, herkes üretimi stabil tutmanın ne gerektirdiğini anlar.

Her ikisi de suçlamasız ( *blameless* ) bir kültür gerektirir. Kimse işe üretimi çökertmek için gelmez. Genellikle insanlardan ziyade sistemi insanlar için başarısız olur. Bu nedenle suçlamasız bir kültür, her iki uygulamada da önemlidir.

İnsanlar, işlerin nasıl gittiği ve nasıl iyileştirileceği konusunda açık ve dürüst şekilde konuşabilir. İkisinin de hedefi aynıdır—stabiliteyle birlikte yazılımı daha hızlı dağıtmak. Dolayısıyla *DevOps* ve *SRE* ortak hedeflere sahiptir; sadece bunlara tamamen farklı yollarla ulaşırlar.

## 🧩 Birlikte Kullanım: Altyapıyı SRE, Uygulamayı DevOps Yönetir

*DevOps* ve *SRE’nin* birbirini nasıl tamamlayabileceğine ve birlikte nasıl kullanılabileceğine baktığımızda, *SRE’yi* altyapıyı sürdüren ekip olarak ve *DevOps’u* bu altyapıyı uygulamalarını sürdürmek için kullanan ekip olarak düşünmeyi seviyorum.

Bir bulut ortamındaysanız,  *SRE* , bulutu işleten insanları içerir ve  *DevOps* , bulutu tüketen insanları içerir. Bu nedenle *platform as a service* gibi şeyleri kullanmak *DevOps* için çok önemlidir. *SRE* ekipleri bir platform sağlar. *DevOps* ekipleri, uygulamalarını dağıtmak için platformu kullanır.

## ✅ Video Özeti

Bu videoda şunları öğrendiniz:
*SRE* *DevOps’tan* farklı bir yaklaşım benimser,
*SRE* ve *DevOps* bazı ortak hedeflere sahiptir,
*SRE* ve  *DevOps* , bilgisayar altyapısını hem sürdürmek hem de kullanmak için birlikte kullanılabilir.
