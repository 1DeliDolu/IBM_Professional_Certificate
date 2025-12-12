# 🚨 Alerting in Monitoring

Alerting in Monitoring’e hoş geldiniz! Bu videoyu izledikten sonra şunları yapabileceksiniz: Uyarılamayı ( *alerting* ) ve uyarılama kavramlarını tanımlamak, farklı uyarı türlerini açıklamak, popüler açık kaynak uyarılama araçlarını incelemek ve uyarılamanın faydalarını özetlemek.

Uyarılama, izlemenin ( *monitoring* ) kritik bir parçasıdır. Birlikte çalıştıklarında izleme ve uyarılama, uygulamalarınızın ve altyapınızın nasıl performans gösterdiğine dair içgörü sağlar. Uyarılama, bir izleme sisteminin tepkisel ( *responsive* ) unsurudur. Kullanıcıları etkilemeden önce sorunları hızlıca tespit edip ele almanıza yardımcı olur.

Ayrıca uyarılama, izlenen veriler altyapınızda veya uygulamalarınızda potansiyel problemler olduğunu gösterdiğinde sizi proaktif olarak bilgilendirir. Ve bir kuruluşun iş sistemleri içinde tespit edilen değişikliklere dayanarak kullanıcı tanımlı eylemleri tetikleyebilir.

Uyarılamanın en yaygın nedeni, o sistemden, servisten veya uygulamadan sorumlu olanları bilgilendirmektir. İki standart uyarı çıktısı vardır: Bildirimler ( *notifications* ), bazı koşulların tespit edildiğini söyler. Otomatik eylemler ( *automated actions* ), tespit edilen bir sorunu hafifletmek için betiklenmiş ( *scripted* ) veya programatik bir eylemi çalıştırır.

Uyarılama şu şekilde çalışır: İzleme sistemi, sistemlerden, uygulamalardan ve süreçlerden veri ve metrikleri toplar. İzleme sistemi, toplanan veriyi analiz eder. Arızalar veya anormallikler tespit edilirse bir alarm yükseltilir ve bir uyarı gönderilir. Uygun personel tarafından inceleme ve iyileştirme ( *mitigation* ) gerçekleştirilir ve sorun çözülür.

Ve ardından izleme süreci devam eder.

---

## 🧭 Uyarılama Süreci Nasıl Çalışır?

İşte genel bir bakış: Bir alarm tetiklendiğinde bir uyarı gönderilir. Ardından bir yönetici ( *admin* ) sorunu araştırır; bu araştırma, uyarının tetiklenmesine neden olan metrik ile başlar.

Yönetici, neden arayışıyla geriye doğru ilerleyerek kendi akıl yürütmesini yapar. İyileştirme, tatmin edici bir açıklama bulunduğunda başarılı olur. İyileştirme, sistemi yeniden dengeye ( *balance* ) getirir.

Metrikler bunu gösterecektir ve alarm “ *clear* ” durumuna geri geçer. İyileştirme, metrikler iyileşmeyi yansıtmadığında başarısız olur. Bu durumda, iyileştirme stratejisinin etkinliği sorgulanmalıdır ve sorunu tamamen çözmek için alternatif bir çözüm gerekebilir.

---

## 🧩 Dört Uyarı Türü

Dört tür uyarı vardır:  **Metrik uyarıları** ,  **Log uyarıları** , **Etkinlik log’u uyarıları** ve  **Akıllı tespit ( *smart detection* )** . Daha yakından bakalım.

### 📈 Metrik Uyarıları

Metrik uyarıları, izleme sisteminiz tarafından toplanan ham verilere dayanır. Sistemler, uygulamalar, veritabanları ve web sunucularındaki kaynakların kullanılabilirliği hakkında bilgi sağlarlar.

Metrikler, tüm altyapınızın ve uygulamalarınızın mevcut sağlığını anlamanıza yardımcı olur. Uygulamalarınızda veya altyapınızda yapılan değişikliklerin etkilerini anlamanıza yardımcı olacak şekilde kullanım ve davranış trendlerini ortaya çıkarabilirler.

### 📜 Log Uyarıları

Bir diğer uyarı türü log uyarısıdır. Metrik uyarılarından farklıdır. Log uyarıları, belirlenmiş aralıklarla kaynak log’larını değerlendirmek için log analitiği sorgularını kullanır; uygulamalarınızın veya servislerinizin nasıl performans gösterdiğini ve göstermekte olduğunu incelemek için çalışır.

Log uyarıları, ne olduğuna ve ne zaman olduğuna dair bir olay izi sağlar ve sorun giderme için son derece önemlidir.

### 🗂️ Etkinlik Log’u Uyarıları

Etkinlik log’u uyarıları, log inceleme sürecini otomatikleştirir; bu da sizi bu görevden uzaklaştırıp zamanınızı serbest bırakmaya yardımcı olur. İzleme sisteminizin bu koşullar gerçekleştiğinde sizi uyarması için kurallar ve koşullar belirlersiniz.

Etkinlik log’u uyarıları, yeni bir olay tanımlanmış kurallar veya koşullarla eşleştiğinde tetiklenir.

### 🧠 Akıllı Tespit

Akıllı tespit, bulut sağlayıcınızın sunabileceği Application Insights ile çalışır. Web uygulamanızda tespit edilen potansiyel performans ve hata anormalliklerine karşı uyarmak için uygulamanızın gönderdiği telemetriyi proaktif olarak analiz eder.

Ani değişiklikler tespit edilirse uyarılar otomatik olarak gönderilir.

---

## ⚠️ Uyarı Eşiklerinde Dikkat Edilmesi Gerekenler

Uyarılar çok faydalıdır; ancak çok geniş veya çok hassas ayarlanmış uyarılara dikkat edin.

Eşikler çok geniş ayarlandığında: İzleme sistemi gerçek problemleri yeterince hızlı tespit edemeyebilir ve etkilenen sistem veya uygulama daha yüksek derecede performans bozulaması yaşayabilir; bu da kesintiye ( *downtime* ) yol açabilir.

Sorunlar nihayet tespit edilip iyileştirildiğinde, pahalı kesintilerin tekrarını önlemek için uyarılama yapılandırması değiştirilmelidir veya ayarlanmalıdır.

Alarm izleyicileri ( *alarm monitors* ) gereksiz derecede hassas eşiklerle oluşturulduğunda: Normal sistem operasyonlarının bir alarm tetiklemesi oldukça olasıdır. Böyle senaryolarda, hiçbir zarar yokken alarmlar uyarılar üretecektir.

Bu sorunu gidermek için temel çizgi ( *baseline* ) yeniden değerlendirilmelidir ve gerçek sorunların tespit edilebilirliğini iyileştirmek için ilgili izleyiciler ( *monitors* ) ayarlanmalıdır.

Çoğu alarm ise geçerli bir sebepten ötürü çalar ve bu alarmlar genellikle iyileştirilebilecek sorunları belirler.

---

## 🛠️ Popüler Açık Kaynak Uyarılama Araçları

Bazı önemli açık kaynak uyarılama araçlarını bilmek önemlidir.

### 🧮 Bosun

Bosun, basit grafikleri gösterebilen ve uyarı kuralları ile koşulları için güçlü bir ifade dili ( *expression language* ) kullanarak uyarılar oluşturabilen düzenli özelliklere sahiptir. Yalnızca e-posta ve HTTP bildirim yapılandırmaları ile sınırlıdır; bu da Slack ve diğer araçlara bağlanmanın ek özelleştirme gerektirdiği anlamına gelir.

Bosun, bildirimler için şablonlar ( *templates* ) kullanabilir; bu da onları dilediğiniz kadar göz alıcı yapabileceğiniz anlamına gelir.

### 🕷️ Cabot

Bir diğer açık kaynak uyarılama aracı Cabot’tur. Arachnys adlı bir şirket tarafından oluşturulmuştur ve kendi başına herhangi bir veri toplamaz. Veriye erişmek için, uyarılama araçlarının API’lerine kancalanarak ( *hooking into* ) başka bir yöntem kullanır.

Uyarı kararları almak için ihtiyaç duyduğu verilerde bir çekme ( *pull* ), itme ( *push* ) değil, modeli kullanır. Cabot, uyarılama verisini bir Postgres veritabanında saklar ve bir Redis önbelleği ( *cache* ) kullanır. Google Calendar ile, Rota adlı bir özellik kullanarak nöbet ( *on-call* ) rotasyonları için entegre olabilir.

### 📊 StatsAgg

Son olarak, StatsAgg başka bir popüler açık kaynak uyarılama aracıdır. Diğer sistemler için bir proxy olarak hareket edebilen bir uyarılama ve metrik birleştirme ( *metrics aggregation* ) platformudur.

Graphite, StatsD, InfluxDB ve Open TSDB’yi giriş ( *inputs* ) olarak destekler. Ayrıca düzenli ifade ( *regular expression* ) eşleştirmesine dayalı uyarılar gönderebilir ve host veya instance yerine servis bazında uyarılamaya odaklanır.

---

## ✅ Uyarılamanın Faydaları

Uyarılama, altyapınızın ve uygulamalarınızın herhangi bir yerindeki problemleri fark etmenizi sağlar. Gözlem, inceleme veya müdahale gerektiren cihazlara, uygulamalara ya da sistemlere dikkatinizi çeker.

İzleme ve otomatik uyarılar, log’ları, sistem olaylarını ve diğer metrikleri manuel olarak incelemekten uzaklaşmanıza olanak tanır; böylece başka yerlerde kullanabileceğiniz değerli zamanı serbest bırakır.

Aktif olarak yönetmenin anlamlı olduğu durumları tanımlayabilir ve değişen koşulları izlemek için pasif izlemeye güvenebilirsiniz.

Altyapınız boyunca otomatik uyarılar uygulamak, sorunlara hızlı yanıt vermenizi, kesintiyi en aza indirmenizi ve daha iyi hizmet sağlamanızı mümkün kılar.

---

## 🧾 Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz: Uyarılama, izleme sisteminin tepkisel parçasıdır ve sorunlar hakkında uyarılmanızı sağlar. İzleme sisteminin izlemesi için eşikler ve koşullar yapılandırabilirsiniz; bu da zamanınızı serbest bırakır.

Uyarılar pasif bildirimler olabilir ya da belirli sorunları iyileştirmek için otomatik eylemleri tetikleyebilir. Dört uyarı türü vardır:  **metrik** ,  **log** , **etkinlik log’u** ve  **akıllı tespit** .

Uyarı eşiklerini çok gevşek ( *liberally* ) veya çok hassas ( *sensitively* ) yapılandırmak ek sorunlara yol açabilir ve  **Bosun** , **Cabot** ve **StatsAgg** üç popüler açık kaynak uyarılama sistemidir.
