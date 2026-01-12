# 🧪 Synthetic İzlemeye Giriş

Introduction to Synthetic Monitoring’e hoş geldiniz. Bu videoyu izledikten sonra,  *synthetic monitoring* ’i tanımlayabilecek ve  *synthetic monitoring* ’in önemini tartışabileceksiniz.

Bir alışveriş web sitesi sahibi olarak, müşterilerinizin sorunsuz ve keyifli bir alışveriş deneyimi yaşamasını istersiniz. Herhangi bir teknik sorun veya yavaş performansın kullanıcıları hayal kırıklığına uğratabileceğini ve satış kaybına yol açabileceğini bilirsiniz. Bu tür sorunları önlemek için *synthetic monitoring* uygularsınız.

*Synthetic monitoring* (aynı zamanda *synthetic testing* veya *proactive monitoring* olarak da adlandırılır), bir uygulamanın veya web sitesinin ne kadar iyi performans gösterdiğini takip etmek için kullanılan bir yöntemdir. Web sitesinde veya uygulamada bir kullanıcının tipik olarak gerçekleştireceği önceden tanımlanmış bir dizi eylem veya isteğin oluşturulmasını içerir.

Bu eylemler daha sonra kaydedilir ve gerçek kullanıcı etkileşimlerini simüle etmek için periyodik olarak yeniden oynatılır. Kısacası, kullanıcı deneyiminizi anlamanıza ve web sitesi performansını iyileştirmenize yardımcı olmak için öngörücü davranış kullanır.

Aktif bir yaklaşım olarak, *synthetic performance* sürekli test yoluyla gerçekleştirilir ve temel iş operasyonları, uygulama kullanılabilirliği, web sitesi hızı ve diğer faktörler hakkında bilgi sağlar.

 *Synthetic monitor* ’lar, web sitelerine, web servislerine,  *API* ’lere ve sunuculara bağlanan botlar gibi çalışır. Monitörler, web sitesinin iyi çalışıp çalışmadığını ve doğru performans gösterip göstermediğini, web sitesinin kendi sunucularının dışındaki bir kontrol noktaları ağı kullanarak kontrol eder. Bu kontrol noktaları, ağın veya dünyanın farklı bölgelerinde bulunur.

Yüzeyde, aktif  *synthetic monitoring* ’in amacı; örneğin bir web sayfası veya *DNS* gibi bir uygulama ya da servisin çalışır durumda olmasını ve gerçek son kullanıcılara hızlı şekilde yanıt vermesini sağlamaktır.

---

## 🤖 Synthetic Monitoring ile Yanıtlanabilecek Sorular

*Synthetic monitoring* araçlarını şu tür soruları yanıtlamak için kullanabilirsiniz:

* Web siteleri ve uygulamalar çalışır durumda mı, yoksa kapalı mı?
* Şu anda web sitesi ne kadar hızlı yükleniyor veya çalışıyor?
* Çalışmaya devam eden herhangi bir üçüncü taraf *API* var mı?
* *CPU* veya bellek kullanımı nasıl görünüyor?
* Sunucunun donanım bileşenleriyle ilgili herhangi bir problem oldu mu?

Bu tür soruları yanıtlamak için, *synthetic transaction monitor* genellikle iki şeyi ölçer:

* Kaynağın zaman içindeki kullanılabilirliği (örneğin,  **%99.99 uptime** )
* Kaynağın zaman içindeki yanıt verebilirliği (milisaniye cinsinden)

---

## 🌐 Synthetic Monitoring Nasıl Çalışır?

Tipik bir kullanıcı etkileşiminin nasıl görüneceğini modellemek için, *synthetic monitoring* sanal bir istemci ile uygulamanız veya web siteniz arasında bir web işlemini simüle ederek çalışır. Kullanılabilirlik, yanıt süresi, kesinti süresi ( *downtime* ) ve hatalar hakkında test yapmak ve bilgi toplamak için kullanılır.

Bu simüle edilmiş işlemler, dünya genelindeki çeşitli işletim sistemleri ve konumlardan başlatılır. Her işlem, bir kullanıcının web sitesiyle etkileşimini doğru şekilde simüle etme hedefiyle önceden belirlenmiş bir testi gerçekleştirir.

 *Synthetic monitoring* , düzenli olarak zamanlanmış bir şekilde bir web veya ağ varlığıyla etkileşime geçmeye çalışan diğer bilgisayarları veya kontrol noktalarını içerir.

Süreç, test sırasında bir hata oluşup oluşmamasına bağlı olarak dört veya beş adım gerektirir. Bu sürece bakalım:

1. İzleme sistemi kontrolü yapmak için bir kontrol noktası seçer ve talimatları kontrol noktasına gönderir.
2. Kontrol noktası bağlantıyı başlatır, yanıtı kontrol eder ve monitörün gerektirdiği kontrol türüne göre devam eder.
3. Kontrol noktası sonuçlarını ve bulgularını izleme sistemine geri bildirir.
4. Sistem, raporlama için bilgileri kaydeder.
5. Eğer kontrol bir hatayla sonuçlanırsa, servis hemen başka bir kontrol noktasından yeni bir test ister. Kontrol noktası aynı hatayı bildirirse sistem hatanın doğrulandığını ilan eder. Sistem, yükseltme ayarlarına ve görev çizelgelerine göre doğrulanan hata için bir uyarı gönderir.

Test türüne bağlı olarak bu süreç, her dakika kadar sık veya saatte bir kez olacak şekilde gerçekleşebilir.

---

## 🏢 Synthetic Monitoring Neden Önemlidir?

 *Synthetic monitoring* ’in önemi, bir şirketin veya markanın ağ veya internet üzerinden içerik ya da hizmet sağlıyor olması gerçeğine dayanır. Üretkenliği, geliri ve itibarı korumak için  *synthetic monitoring* ’e ihtiyaç vardır.

Kullanılabilirlik ve performans görev açısından kritik olduğunda, bir marka kullanıcıların bir problem olduğunu bildirmesini bekleyemez.

Peki *synthetic monitoring* ne yapar?

* Hızlı problem çözümü sunar. *Synthetic monitoring* kullanıldığında, düşük performans ve kesintiler hızlıca ortaya çıkar.
* Bir hata hakkında ayrıntılı raporlara anında erişim sağlar; bu da ekiplerin hızlı yanıt vermesine olanak tanır.
* Çoğu zaman ekipler kök nedeni bulabilir ve kullanıcı fark etmeden önce bir düzeltme uygulayabilir.
* Uyarılar, kullanıcılar web sitesi veya hizmetle ilgili bir sorun yaşamadan önce tetiklenmelidir.
* Proaktif yaklaşımı, ekipleri sorunlar oluşmadan önce uyarmada çok etkilidir.
* Bir veritabanı sunucusundan kaynaklanan performans düşüşü gibi, sorunlara dönüşmeden önce durumları kontrol edip doğrulayabilir ve tespit edebilir.

Üçüncü taraf içerik; reklamcılık, ödeme yönetim sistemleri, içerik dağıtım ağları ( *CDN* ’ler) ve analitik çözümler gibi biçimlerde gelir. *Synthetic monitoring* kullanımı, bu tür üçüncü taraf hizmetleri kullananların  *service level objective* ’leri izlemesine olanak tanır.

Performans bozulmaları ve kullanılabilir olmama olayları izlenerek tedarikçilerin sorumlu tutulması sağlanır.

Bir şirket işletiyorsanız, performans ve fonksiyona odaklanmanın yanı sıra  *synthetic monitoring* ’i  *service level agreement* ’ları ( *SLA* ’lar) doğrulamak için de kullanabilirsiniz.

Ayrıntılı raporlar, web sitelerinin veya uygulamaların herhangi bir dönem için tam kullanılabilirlik yüzdesini göstermesini sağlar. Yüksek kaliteli bir uygulama performansı sunmaya çalışırken  *API* ’lerinizin ve uygulamalarınızın kullanılabilirliğini ve çalışma süresini ( *uptime* ) kontrol etmeniz gerekir.

 *Synthetic monitoring* , çeşitli coğrafyalardan iş süreçlerini veya kullanıcı işlemlerini simüle etmenizi ve performanslarını izlemenizi sağlar; buna oturum açma, arama, form doldurma, sepete ürün ekleme ve ödeme işlemi ( *checkout* ) dahildir.

---

## 📊 RUM ve Synthetic Monitoring Karşılaştırması

Bir web sitesi veya uygulama izleme çözümü aradığınızda, iki farklı türle karşılaşırsınız:

* *Real User Monitoring (RUM)* : pasif izleme
* *Synthetic monitoring* : aktif izleme

 *RUM* , kullanıcı yolları veya işlemleri üzerindeki performans verilerini toplamak için gerçek kullanıcılara dayanır. Öte yandan, *synthetic monitoring* sorunları hızlı bir şekilde çözmek için simüle edilmiş kullanıcı işlemlerini izler.

Ekiplerin uygulamaların ve sayfaların duyarlı olduğunu ve amaçlandığı gibi çalıştığını izlemesine ve sağlamasına yardımcı olmak için, *RUM* çözümleri genellikle tekil kullanıcıları takip eden bir *JavaScript* kod parçacığı kullanır ve yanıt süreleri, yükleme süreleri, hatalar, tarayıcılar, konumlar ve diğerleri dahil olmak üzere çeşitli performans metrikleri ve verileri raporlar. Bu veriler daha sonra tek bir gösterge paneline ( *dashboard* ) sağlanır.

 *Synthetic monitoring* , değişkenleri ortadan kaldırarak tutarlı bir test ortamı oluşturmamıza olanak tanır. Test için kullanılan değişkenler kullanıcı segmentleriyle ilişkilendirilmiştir ancak bir sayfayı gerçekten ziyaret eden kullanıcıların çeşitliliğini yakalayamaz; işte burada *RUM* devreye girer.

Uzun vadeli performans eğilimleri *real user monitoring* kullanılarak izlenebilir ve bulunabilir. Öte yandan  *synthetic monitoring* , herhangi bir acil problemi belirlemenize ve çözmenize yardımcı olur. *Synthetic monitoring* ile izlediğiniz metrikler, *RUM* sonuçlarından da etkilenebilir.

*Real user monitoring* ve  *synthetic monitoring* ’in son derece önemli bilgiler sağladığı ve birlikte kullanıldıklarında en iyi şekilde çalıştıkları açıktır.

---

## ✅ Videodan Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* *Synthetic monitoring* , bir uygulamanın veya web sitesinin ne kadar iyi performans gösterdiğini takip etmek için kullanılır.
* Aktif  *synthetic monitoring* ’in amacı, bir uygulama veya servisin çalışır durumda olmasını ve gerçek kullanıcılara hızlı şekilde yanıt vermesini sağlamaktır.
* *Synthetic monitoring* önemlidir; çünkü daha hızlı problem çözümü sağlar, uyarı verir, diğer içerikleri izler.
* *SLA* uyumluluğunu sağlar ve karmaşık işlem ve iş süreçlerini izler.
