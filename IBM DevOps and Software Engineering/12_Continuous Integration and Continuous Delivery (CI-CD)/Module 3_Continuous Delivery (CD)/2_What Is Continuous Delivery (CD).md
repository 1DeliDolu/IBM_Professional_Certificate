# 🚚 Sürekli Teslimat (CD) Nedir?

‘Sürekli Teslimat nedir?’ videosuna hoş geldiniz. Bu videoyu izledikten sonra şunları yapabileceksiniz: Sürekli Entegrasyon ile Sürekli Teslimat arasındaki farkı ayırt etmek, Sürekli Teslimatın hedeflerini açıklamak ve Sürekli Teslimatın faydalarını açıklamak.

![1766140039411](image/2_WhatIsContinuousDelivery(CD)/1766140039411.png)

İlk olarak, Sürekli Teslimat ile Sürekli Entegrasyon arasındaki farkı anlamak önemlidir; çünkü çoğu zaman insanlar ‘CI/CD’yi tek bir şeymiş gibi söyler, ama öyle değildir. Bunlar, birbirinden sonra gerçekleşen iki ayrı ve farklı şeydir.

Sürekli Entegrasyon, kodunuzu ana (main) veya master ya da trunk dalına sürekli olarak entegre etmektir; böylece ana dala geri birleştirmeden önce kodunuz çok fazla uzaklaşmaz ve çalıştığından emin olmak için ana dala geri birleştirme yaparsınız. Kodunuzu ana kodla sürekli olarak entegre edersiniz.

Buna karşılık Sürekli Teslimat, entegre edilmiş kodu alıp bir yere dağıtmaktır (deploy etmektir).

![1766140073267](image/2_WhatIsContinuousDelivery(CD)/1766140073267.png)

---

## 🔁 CI ve CD Süreci Nasıl Ayrışır?

Her entegre ettiğinizde dağıtım yapabilirsiniz, her entegre ettiğinizde dağıtım yapmayabilirsiniz — bir döngüde sürekli entegrasyon yapıyor olabilirsiniz. Ardından ana dalınıza birleştirdiğinizde, Sürekli Teslimat kısmını başlatırsınız.

Sürekli Teslimat terimi, her değişikliği *üretim benzeri (production-like)* bir ortama teslim ederek kodun üretime hızlı ve güvenli bir şekilde dağıtılabilmesini sağlamaya yönelik bir dizi uygulama olarak tanımlanabilir. Dikkat edin, “ *üretim benzeri* ” diyor. Bunun üretim ortamı olması gerekmez ve çoğu zaman da değildir.

Aslında, üretime dağıtmak genellikle “Sürekli Dağıtım (Continuous Deployment)” olarak adlandırılır. Sürekli Teslimat yalnızca, kodu dağıtılabildiğinden emin olmak için bir geliştirme, test veya staging ortamına dağıttığınız anlamına gelir.

Bu ayrıca, herkesin kodun çalıştığını görmesine fırsat verir. Buradaki kilit çıkarım şudur: Bu süreç otomatikleştirilmiştir. Kodu dağıtmak için kimse herhangi bir manuel adım gerçekleştirmemiştir. Kod, sürekli olarak otomatik şekilde dağıtılır.

![1766140150326](image/2_WhatIsContinuousDelivery(CD)/1766140150326.png)

---

## 🎯 Sürekli Teslimatın Hedefleri Nelerdir?

Peki Sürekli Teslimatın hedefleri nelerdir? Martin Fowler’a göre: “Sürekli Teslimat, yazılımı, yazılımın herhangi bir zamanda üretime yayımlanabilecek şekilde inşa ettiğiniz bir yazılım geliştirme disiplinidir.”

![1766140173762](image/2_WhatIsContinuousDelivery(CD)/1766140173762.png)

Bunun ne anlama geldiğine daha derinlemesine bakalım.

Herhangi bir zamanda üretime yayınlayabilmek, ana (main) ya da master dalın her zaman dağıtılabilir (deployable) olması gerektiği anlamına gelir. Bu da, ürününüzü bozabilecek kötü kodun ana ya da master dala girmemesini sağlamak için yerinde bir kontrol setine sahip olmanız gerektiği anlamına gelir.

Bu kesinlikle kritik bir noktadır. Ve bu yüzden her pull request olduğunda testleri çalıştırmak için Sürekli Entegrasyonu kullanırsınız. Ayrı feature branch’lerde çalışmak ve pull request’leri kullanmak, yazdığınız herhangi bir kodun ana dala geri birleştirmeden önce doğru çalıştığından emin olmanızı sağlar.

![1766140222058](image/2_WhatIsContinuousDelivery(CD)/1766140222058.png)

---

## ✅ Sürekli Teslimatın Faydaları

Sürekli Teslimatın faydaları çoktur ve çeşitlidir; bunlar şunları içerir:

Geliştirme ekiplerinizin, yazılımı yazılım geliştirme yaşam döngüsünün (SDLC) çeşitli aşamalarından taşıyan adımları otomatikleştirmesini sağlamak.

Otomasyon; durmaksızın test ve dağıtım döngüleriyle dağıtım süresini azaltmaya yol açar.

Ne kadar çok dağıtım yaparsanız, bir sonraki dağıtımınızın çalışacağına dair o kadar fazla güvene sahip olursunuz ve dağıtımlarda hata ayıklamaya o kadar az zaman harcarsınız.

Standart dağıtım stratejileriyle normalde yaygın olan maliyetleri azaltmak. Bu, insan maliyetleri, altyapı maliyetleri ve manuel hatalar nedeniyle kaybedilen zamanın maliyeti olabilir.

Sürekli Teslimat, geliştirme ekibinizin yazılım dağıtımlarını projenin büyüklüğüne göre ölçeklendirmesini sağlar.

Ve yazılım geliştirme yaşam döngüsünün çeşitli aşamalarına kodu otomatik olarak dağıtmanızı sağlar. Geliştirme ortamına sorunsuz şekilde dağıttıktan sonra, test ortamına ve ardından staging ortamına da sorunsuz şekilde dağıttıysanız, üretime dağıttığınızda bunun da sorunsuz olma ihtimali oldukça yüksektir.

![1766140264628](image/2_WhatIsContinuousDelivery(CD)/1766140264628.png)

---

## 📌 Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

CI/CD tek bir şey değildir; birbirinden sonra gerçekleşen iki ayrı ve farklı şeydir.

Sürekli Teslimat, entegre edilmiş kodu alıp bir yere dağıtmaktır.

Sürekli Teslimat, yazılımı herhangi bir zamanda üretime yayımlanabilecek şekilde inşa ettiğiniz bir yazılım geliştirme disiplinidir.

Pull request’lerin ve feature branch’lerin olmasının sebebi, ana dala geri birleştirmeden önce kod değişikliklerinin çalıştığından emin olabilmenizdir.

Ve kodunuzun üretime teslim edeceğiniz şeyin hatasız ve amaca uygun olmasını sağlamak için genellikle birkaç Kalite Güvence (Quality Assurance) aşamasından ve Staging ya da Test aşamalarından geçmesi gerekir.

![1766140317468](image/2_WhatIsContinuousDelivery(CD)/1766140317468.png)
