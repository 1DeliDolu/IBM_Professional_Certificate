# 🌩️ Cloud Native Observability

Cloud Native Observability’e hoş geldiniz. Bu videoyu izledikten sonra, *cloud native observability* kavramını açıklayabileceksiniz.

Önde gelen bir e-ticaret şirketinde bir DevOps ekibinin parçası olduğunuzu varsayalım. Ekibiniz, kusursuz bir kullanıcı deneyimi sunmak için şirketin *cloud-native application* olarak oluşturulmuş çevrimiçi platformunu yönetmekten sorumludur. Ancak son zamanlarda platform, aralıklı yavaşlamalar ve zaman zaman kesintiler yaşamaktadır; bu da müşterilerin memnuniyetsiz olmasına ve gelir kaybına yol açmaktadır. Bir çözüme ihtiyaç olduğunu fark eden ekibiniz, *cloud native observability* uygulamaya karar verir.

---

## 🔍 Cloud Native Observability Nedir?

 *Cloud native observability* , dinamik ve dağıtık ortamlarda çalışan  *cloud-native application* ’ların davranışını izleme ve anlama uygulamasıdır.

Uygulamalar ve altyapı bileşenleri tarafından üretilen büyük miktarda verinin toplanmasını, işlenmesini, analiz edilmesini ve görselleştirilmesini içerir; böylece sistemlerin sağlık durumu, performansı ve güvenilirliği hakkında içgörüler elde edilir.

 *Cloud native observability* ; sistemin bütünsel bir görünümünü sağlamak için  *metrics* ,  *logs* ,  *traces* , *events* ve *alerts* gibi tekniklerden yararlanır. Amaç, DevOps ekiplerinin sorunları hızlıca tespit edip etkili şekilde gidermesini ve uygulama teslim sürecini sürekli iyileştirmesini sağlamaktır.

---

## ✅ Güçlü Bir Observability Çözümü Uygulamanın Avantajları

Güçlü bir *observability* çözümü uygulamanın birçok avantajı vardır. En bariz avantaj, sorunları verimli bir şekilde tespit edip çözebilme yeteneğidir.

Bir diğer önemli avantaj ise, olaylar arasındaki korelasyonları belirleyerek *mean time to repair* ya da  *MTTR* ’ı azaltmaya yardımcı olmasıdır. Sorun giderme, saatler ya da günler yerine yalnızca dakikalar içinde yapılabilir; bu da yanıt sürelerinde önemli ölçüde iyileşme sağlar.

Bir başka avantaj da *shift left* yapabilme yeteneğidir; bu sayede mühendisler ve geliştiriciler, sorunları geliştirme yaşam döngüsünün daha erken aşamalarında teşhis edebilir. Bu, sorun giderme yaklaşımında reaktif olmak yerine proaktif olmayı sağlar.

Son olarak, *observability* uygulamak daha sağlıklı sistemler, daha az hata ve daha verimli süreçler sağlar. Bu da, uygulama sorunları, kesinti olayları veya iş operasyonlarını aksatan yavaş yanıt süreleri nedeniyle müşterilerin churn etme olasılığını azaltarak müşteri memnuniyetini artırır.

---

## 🧠 Cloud Observability ile Bağlamsallaştırma ve Korelasyon

*Cloud observability* ile yalnızca tekil sistemleri izlemekten fazlasını yapabilirsiniz. Tüm BT ortamı boyunca, ayrık uygulamalar ve sistemler arasındaki etkileşimleri bağlamlandırabilir ve korele edebilirsiniz.

 *Cloud observability* ’nin temelleri  *automation* , *context* ve  *intelligent actions* ’tır.

---

## 🏢 Enterprise Observability’nin Temelleri

 *Enterprise observability* , yeni kod dağıtıldığında veya sistem değişiklikleri gerçekleştiğinde değişiklikleri otomatik ve sürekli olarak tespit eder ve hızlı geri bildirim sunar.

 *Enterprise observability* , uygulama bileşenleri ve servisleri arasındaki bağlantıları ortaya çıkararak kaynak performansını ve erişilebilirliğini optimize eder.

Değişiklikler meydana geldiğinde, *enterprise observability* bağlamla birlikte derin analizleri proaktif şekilde sağlar ve sistem optimizasyonu için adımlar önerir.

---

## 🧩 Modern Zorluklar ve Geleneksel İzlemenin Yetersizliği

Teknoloji ilerledikçe yeni zorluklar da ortaya çıkar. Modern dünyada, dağıtık *microservices* ortamları ve konteyner tabanlı uygulamalar giderek daha yaygındır. Ancak geleneksel izleme araçları bu sistemlerin karmaşıklığını yönetmekte zorlanır.

Bu ortamlar dinamik olabilir; servisler, farklı altyapılardan, platformlardan, dillerden ve teknolojilerden oluşan sunucu kümeleri üzerinde dağıtılabilir. Bu da geleneksel altyapı ve uygulama izleme araçlarının dil seviyesinde görünürlük sağlamasını zorlaştırır.

---

## 📦 Container’lar İçin Geleneksel İzlemeyi Yapılandırmanın Zorluğu

*Konteynerlar* farklı teknolojiler, mimariler ve konfigürasyonlar çalıştırabilir. Ayrıca her konteynerın benzersiz olması ve uygun eşik değerlerini önceden tanımlamanın zorluğu, süreci daha da karmaşık hale getirir.

Sonraki olarak, konteyner platformlarının genellikle yalnızca temel izleme işlevselliği sunduğunu ve bu nedenle gelişmiş izlemeye ihtiyaç duyulduğunu düşünelim.

Hatta gelişmiş *virtual machine* platformları bile uygulama katmanı verisi veya dağıtık izleme ( *distributed tracing* ) sağlayamaz.

---

## ☸️ Kubernetes ve Orkestrasyonun Sınırları

*Kubernetes* gibi konteyner orkestratörlerinin, başarısız konteynerları bulup yeniden başlatabilen mükemmel sağlama ( *provisioning* ) ve orkestrasyon araçları olduğunu düşünebilirsiniz. Ancak bunlar gelişmiş izleme için ne amaçlanmış ne de tasarlanmıştır.

Kullanıcı deneyimi ya da uygulama performans yönetimine odaklanmazlar ve kendi farkındalıklarının dışında kalan kaynak kullanımını izleyemezler.

---

## 🧾 Sonuç

İşletmeler *microservices* ve konteyner tabanlı  *cloud-native application* ’lar gibi daha karmaşık teknolojileri uygulamaya devam ettikçe, uygun *observability* ve izleme araçlarına sahip olmak kritik hale gelir. Geleneksel çözümler, bu yeni zorluklarla başa çıkmak için artık yeterli olmayabilir.

Bu videoda şunları öğrendiniz:  *Cloud native observability* , dinamik ve dağıtık ortamlarda çalışan  *cloud-native application* ’ların davranışını izleme ve anlama uygulamasıdır. Güçlü bir *observability* çözümü uygulamanın avantajları; sorunları verimli şekilde tespit edip çözmek,  *MTTR* ’ı azaltmak, *shift left* yapmak ve daha sağlıklı sistemler geliştirmektir.  *Cloud enterprise observability* ’nin sütunları  *automation* , *context* ve  *intelligent action* ’dır. Geleneksel çözümler, konteyner tabanlı  *cloud-native application* ’larda karmaşık *microservices* yapılarını yönetmek için artık yeterli olmayabilir. Bu nedenle uygun *observability* ve izleme araçlarına sahip olmak kritik önem taşır.
