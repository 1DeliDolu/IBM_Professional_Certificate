# 🧰 Sürekli Teslimat (CD) Araçları

Sürekli Teslimat Araçları’na hoş geldiniz. Bu videoyu izledikten sonra, Sürekli Teslimat’ı (Continuous Delivery – CD) mümkün kılan farklı araçları tanımlayabilecek, bir CD aracı seçerken nelere bakmanız gerektiğini açıklayabilecek ve CD için *Argo CD* ile *Tekton* araçlarını tanımlayabileceksiniz.

![1766141089220](image/5_ToolsofContinuousDelivery(CD)/1766141089220.png)

Ortalama bir geliştiricinin Sürekli Teslimat uygulaması için kullanabileceği birçok araç vardır.  *Jenkins* , pazardaki daha eski CI/CD araçlarından biridir ve en popüler olanlardan biridir. Çok büyük bir topluluğa sahiptir ve sayısız eklentiyi destekler, ancak CD için ideal değildir. *Jenkins* pipeline sürecine görünürlük sağlamaz ve çok fazla kurulum ve bakım gerektirir; bu da onu diğer CD araçlarına kıyasla rekabetçi olmaktan uzaklaştırır.

*Spinnaker* ise Netflix tarafından kurum içinde geliştirilmiş, buluttan bağımsız (cloud-agnostic) adanmış bir CD aracıdır. CD pipeline’larını yönetmenize olanak tanır ve sürüm geri alma (release rollback) süreçlerini basitleştirir. Load balancer oluşturmayı ve cluster ölçeklemeyi yerel olarak (natively) destekler.

*Concourse CI* de CD yetenekleri içeren bir araçtır ve başlangıçta container’lar düşünülerek geliştirilmiştir; ancak yine de işleri sanal makineler üzerinde çalıştırabilirsiniz. Container’lar yüksek ölçeklenebilirliğe sahiptir ve *container-first* yaklaşımı sayesinde build’in her adımı çok esnektir; yalnızca build almak için bir Docker imajını işaret etmeniz yeterlidir.

Son olarak  *GitLab* , hem CI hem de CD uygulayabilir. GitLab aynı zamanda bir kaynak kod yöneticisi olduğundan, kodu production’a dağıtma sürecini otomatikleştirmek kolaydır. Tüm büyük bulut platformlarını destekler; bu da CI/CD pipeline’ını inşa etmeyi oldukça esnek hâle getirir.

![1766141160570](image/5_ToolsofContinuousDelivery(CD)/1766141160570.png)

 *Travis CI* , CD yetenekleri içeren bir başka CI aracıdır. Diğer CD uygulamaları kadar zengin özellikli değildir, ancak minimum bakım gerektirir.

 *Tekton* , Kubernetes üzerinde uygulamaları build etmek, test etmek ve deploy etmek için açık kaynaklı, üreticiden bağımsız (vendor-neutral) bir çerçeve kullanmanızı sağlar. En büyük gücü modülerliğidir; VM’ler, serverless, Kubernetes ve bulut sağlayıcıları gibi birden fazla ortamda dağıtım yapmanıza olanak tanır.

 *Go CD* , yerel Docker ve Kubernetes desteğiyle kolay pipeline kurulumu sunduğunu iddia eden bir araçtır. Commit ile deployment arasındaki tüm aşamalarda her pipeline’ı izlemenize yardımcı olan kendi *Value Stream Map* aracını içerir. Pipeline’ları YAML veya JSON dosyalarıyla ya da görsel bir UI içinde oluşturabilirsiniz.

Ve son olarak  *Argo CD* , Intuit tarafından başlangıçta geliştirilmiştir; çünkü Spinnaker’dan daha hafif bir araç arıyorlardı ve build ile deployment sürelerini iyileştirip GitOps iş akışlarını sadeleştirmek istiyorlardı. UI iyi tasarlanmıştır ve kullanımı kolaydır;  *Jenkins* ,  *GitHub Actions* , *CircleCI* ve daha fazlası gibi çeşitli CI araçlarıyla iyi entegre olur.

![1766141225925](image/5_ToolsofContinuousDelivery(CD)/1766141225925.png)

## 🔍 Bir CD Aracı Seçerken Nelere Bakılmalı?

İş akışınızda kullanmak üzere bir CD aracı ararken, aşağıdaki temel değerlendirmeler öncelikli olmalıdır. CD ile birlikte tam denetim izleri (full audit trails), tescilli entegre gizli bilgi yönetimi (proprietary integrated secrets) ve ince ayrıntılı rol tabanlı erişim kontrolü (fine-grained, role-based access control) isteyebilirsiniz. Bu özellikler CD araçlarında kısmen mevcut olabilir ve her yerde bulunmaz; çünkü bazı araçlar çok yeni ve aşırı basit olabilir.

Zengin özellikli bir CD aracı, uygulamalarınız daha karmaşık hâle gelip daha fazla hareketli parçaya sahip olduğunda, gerekli özelliklerin hâlihazırda elinizin altında olmasını sağlar. CI pipeline’ınıza bağlı olarak bazı CD araçları mevcut sürecinizle uyumlu olmayabilir. Uyumlu olan ve mevcut araç setinizle kolay entegre olan bir araç seçmek, CD kurulumunu hızlandırır ve olası sorunları azaltır.

CD araçları, nasıl uygulandıkları ve geliştiricilerin projelerinde CD’yi kurmasının ne kadar kolay olduğu açısından büyük ölçüde farklılık gösterebilir. *Tekton* gibi araçlar kurulumu kolaydır ve pipeline’larınıza dair net içgörüler sağlar. Kurulumun ötesinde bakım da çok zaman alabilir. *Argo CD* gibi araçlar kurması ve bakımını yapması kolayken, *Jenkins* hem kurulum hem de bakım açısından zahmetlidir.

![1766141262125](image/5_ToolsofContinuousDelivery(CD)/1766141262125.png)

## 🛡️ CD Pipeline İçinde Gereken Ek Araçlar

Bir pipeline’ı bir CD aracıyla inşa etmek yalnızca ilk adımdır. CD pipeline’ınız içinde aşağıdaki görevleri gerçekleştirmek için hangi araçlara ihtiyaç duyduğunuzu da düşünmelisiniz:

Pipeline içinde, uygulama güvenliği taraması ve genel uygulama sağlığını güvenceye almak için araçlara ihtiyacınız vardır. Güvenlik çoğu zaman sonradan akla gelir ve uygulama yayına alınmadan hemen önce eklenir. Pipeline’ınıza güvenlik kontrolleri ekleyerek, yol boyunca yaptığınız her değişikliğin güvenli olduğu test edilir.

Güvenlik açığı taraması (vulnerability scanning), bağımlılıkları ve bileşen zafiyetlerini belirlemeye yardımcı olur. Bir gün zafiyeti olmayan uygulamalar, mevcut kodda veya kütüphanelerde bulunan istismarlar (exploit) nedeniyle bir anda zafiyetli hâle gelebilir. Bilinen zafiyetlere sahip kodu sevk etmediğinizden emin olmak için CD pipeline’ınıza güvenlik açığı taramasını eklemek kritik derecede önemlidir.

API anahtarları ve kimlik bilgileri için secret taraması (secret scanning), hassas bilgilerin yanlışlıkla açığa çıkmasını önler. Çoğu zaman geliştiriciler, şifreleri ve diğer kimlik bilgilerini yanlışlıkla kaynak kontrole eklenmiş dosyalara koyar. Secret taraması, kimlik bilgilerinin sızdırılmamasını sağlar.

*Static Application Security Testing* (SAST) taraması, SQL injection ve cross-site scripting gibi tüm kod tabanındaki zafiyetleri tespit eder. Bu hataların bazıları code review sırasında yakalanabilse de, geliştiriciler unuttuğunda CD pipeline’ınızın bunları kontrol ettiğinden emin olmak önemlidir.

*Dynamic Application Security Testing* (DAST), kaynak kodda gizli olabilecek yanlış güvenlik varsayımlarını tarar. Dinamik tarama, çalışan uygulamada zayıf noktaları kontrol eder. Bunları production’da kötü niyetli kullanıcıların bulmasındansa CD pipeline’ınızda yakalamak daha iyidir.

Son olarak, bir CD pipeline’ı ayrıca kod dağıtımını (deployment) kolaylaştıran bir araca ihtiyaç duyar. Dağıtımların otomasyonu, tekrar edilebilir olmalarını sağlar; böylece geliştirme, test, staging veya production’a deploy ederken aynı sonuçları elde edersiniz.

![1766141295414](image/5_ToolsofContinuousDelivery(CD)/1766141295414.png)

## 🌱 Argo CD ve Tekton’a Kısa Bakış

Popülerliği artan nispeten yeni bir araç  *Argo CD* ’dir.  *Argo CD* , CD’yi otomatikleştirmeyi, denetlemeyi ve anlamayı kolaylaştıran bildirimsel (declarative) bir Sürekli Teslimat aracıdır. İstenen uygulama durumunu tanımlamak için Git repository’lerini tek doğruluk kaynağı (single source of truth) olarak kullanan GitOps desenini izler.

Argo CD, bir Kubernetes controller olarak, mevcut uygulama durumunu istenen durumla karşılaştırır, farklılıkları görselleştirir ve otomatik senkronizasyonla eşitliği (parity) sağlar.

![1766141320795](image/5_ToolsofContinuousDelivery(CD)/1766141320795.png)

Bu kursta *Tekton* kullanacağımız için, ona da kısaca bakalım.  *Tekton* , uygulama detaylarını soyutlayan esnek, açık kaynaklı bir çerçevedir; böylece projelerinizin gereksinimlerine göre build, test ve deploy etmeye odaklanabilirsiniz. CI/CD araçlarını ve sürecini standartlaştırarak Tekton,  *Jenkins* , *Skaffold* ve *Knative* gibi diğer CI/CD araçlarıyla iyi çalışır.

*Tekton* pipeline’ları tamamen taşınabilirdir (fully portable); oluşturulduktan veya tanımlandıktan sonra, kurum içindeki bir geliştirici pipeline’ı alıp bileşenlerini yeniden kullanabilir.

![1766141339251](image/5_ToolsofContinuousDelivery(CD)/1766141339251.png)

## ✅ Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz: Seçebileceğiniz birçok Sürekli Teslimat aracı vardır, iyi bir CD aracı zengin özellikli, kullanımı kolay, yüksek uyumluluğa sahip ve düşük bakım gerektiren bir araç olmalıdır, tarama ve deployment görevleri CD pipeline içindeki araçlar tarafından ele alınmalıdır, *Argo CD* bir Kubernetes controller olarak uygulanan bildirimsel (declarative) bir Sürekli Teslimat aracıdır ve *Tekton* pipeline’ları tamamen taşınabilirdir; geliştiriciler bileşenlerini yeniden kullanabilir.

![1766141372577](image/5_ToolsofContinuousDelivery(CD)/1766141372577.png)
