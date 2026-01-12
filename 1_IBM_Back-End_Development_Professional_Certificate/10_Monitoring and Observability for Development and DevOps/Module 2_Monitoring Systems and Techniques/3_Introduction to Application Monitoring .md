# 🧭 Uygulama İzlemeye Giriş

Uygulama İzlemeye Giriş’e hoş geldiniz! Bu videoyu izledikten sonra, uygulama izlemeyi tanımlayabileceksiniz. Uygulama izlemenin önemini tartışabilecek ve izleme çözümlerini değerlendirmenin faydalarını ve sürecini özetleyebileceksiniz.

Uygulama izleme, geliştiricilerin yazılımlarının amaçlandığı şekilde performans gösterdiğinden emin olmak için kullandığı bir süreçtir. Geliştiriciler, bir uygulamanın nasıl çalıştığını değerlendirmek için performans metriklerini toplamak üzere izleme araçlarını kullanır. Bu, uygulama çalışırken gerçek zamanlı olarak meydana gelen herhangi bir sorunun, hatanın veya beklenmedik olayın hızlıca tespit edilmesini sağlar. Ayrıca uygulama izleme, uygulama kullanımına dair daha iyi bir anlayış sunar; bu da geliştiricilerin daha yüksek performans ve kullanıcı memnuniyeti için uygulamaları ince ayarlamasına ve sürdürmesine olanak tanır.

---

## 🧩 Uygulama İzleme Araçlarının İşlevleri

Uygulamanızın ve bağımlılıklarının sorunsuz ve amaçlandığı şekilde çalıştığından emin olmak için sunucular, veritabanları, mesaj kuyrukları ve önbellekler gibi bileşenlerin gözlemlenmesi gereklidir.

İzleme araçları ayrıca görselleştirme ve uyarılar sağlar. Panolar (dashboard’lar) genel bir görünüm sunar ve uyarılar belirli problemlere dikkat çeker. Buna ek olarak, izleme araçları anomalileri tespit edebilir; bu, basit eşik tespitinden gelişmiş *machine learning* desen tanımaya kadar değişebilir.

Dağıtık izleme ( *distributed tracing* ) ile geliştiriciler, hataların kaynağını tespit etmek için bir olayın birden fazla düğüm (node) boyunca nasıl bağlandığını izleyebilir. İzleme araçlarının bir diğer ana işlevi de, isteklerin servisler arasında nasıl ilerlediğini görsel olarak temsil eden bağımlılık eşlemedir ( *dependency mapping* ).

---

## 🏗️ Dağıtım Modelleri ve Yaklaşımlar

Uygulama izleme genellikle şirket içinde ( *on-premises* ) veya bulut tabanlı çözümler aracılığıyla sunulur. Ayrıca yazılım tabanlı veya donanım tabanlı bir çözüm de olabilir.

Donanım tabanlı çözümler, performans telemetrisini toplayan özel web aygıtlarını içerir; telemetri, sisteminiz tarafından toplanan ve kaydedilen veri ve metriklerdir.

Yazılım tabanlı ajan süreçleri bir web uygulamasının yanında dağıtılabilir. Bu ajanlar, telemetri verilerini toplamak için uygulama performans göstergesi (veya  *API* ) çalışma zamanlarına ( *runtimes* ) bağlanır. Bu, izlemeyi güçlendirmek için sentetik trafik ile birlikte çalışır.

Sentetik trafik, belirlenen aralıklarda uygulama verimini ( *throughput* ) ve performansını izlemek için kullanıcı etkileşimini simüle eder. Tipik olarak dünyanın herhangi bir yerinde bulunabilen çeşitli uç noktalara ( *endpoints* ) kurulan harici bir uygulama tarafından üretilir.

---

## 📡 Telemetri Nedir ve Neleri Kapsar?

Telemetri, izleme için otomatik olarak toplanan ve kaydedilen sistem verisidir. Telemetri; kaynak kullanımı, sunucu günlükleri, ağ trafiği ve performans metriklerini içerir.

Geliştiriciler ve ekipleri şunları izler:

* Uygulamalarınızı barındıran ve çalıştıran sunuculardan CPU ve diğer kaynak kullanım metrikleri
* Hedef uygulamalarda alınan kullanıcı isteklerinin sayısını yanıt süresiyle karşılaştırmak ve hata oranlarını izlemek için sunucu günlükleri
* Uygulama kesintisini ( *downtime* ) tespit etmek için ağ trafiği
* Programlama dilleri ve servisler üzerindeki uygulama bağımlılıklarına göre ölçülen ve analiz edilen temel performans metrikleri

---

## ✅ Uygulama İzlemenin Faydaları

Hızlı teşhis, temel faydalardan biridir. Uygulama izlemenin doğrudan faydası, proaktif sorun gidermedir — başka bir deyişle, son kullanıcıları etkilemeden önce gelecekteki sorunları hızlıca teşhis edip düzeltme yeteneğidir.

Ayrıca uygulama izleme şunları sağlayabilir: daha hızlı çözüm süreleri ve BT personeli verimliliğinde artış.

DevOps süreçlerinin bir parçası olarak tutarlı biçimde kullanıldığında, uygulama izleme; uygulama dağıtımını hızlandırmaya ve daha yüksek kaliteli kullanıcı deneyimleri sunmanıza yardımcı olabilir.

Etkili uygulama izleme, iş verimliliğini başka şekillerde de artırabilir. Proaktif problem çözme stratejileri kullanarak potansiyel problemleri ortaya çıkmadan önce öngörebilir ve çözebilirsiniz. Satışlarınızı ve gelirinizi artırabilirsiniz. İzleme, müşteri memnuniyetini mümkün kılmaya ve iş büyümesini yönlendirmeye yardımcı olan değerli içgörüler sağlar. İzleme ayrıca, müşteri şikayetleriyle sonuçlanabilecek problemleri öngörüp ortadan kaldırarak kullanıcı deneyimini geliştirmenize olanak tanır.

Ayrıca kesinti süresini ( *downtime* ) azaltırsınız; bu da üretkenlik kaybı, marka itibarına zarar, veri kaybı ve kaçırılan fırsatlarla sonuçlanır.

---

## 📈 İş Sonuçlarına Etkisi

Uygulama performansını izlemek şirketinizin üretkenliğini artırır. Sistemler ve uygulamalar sorunsuz çalıştığında üretkenlik problemlerinden kaçınılır. Kesinti, gecikme veya sorun yaşamayan müşteriler daha memnun müşterilerdir. Memnun müşteriler daha sağlıklı ve başarılı bir işletmeye katkıda bulunur.

---

## 🧾 Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz: Uygulama izleme, geliştiricilerin uygulama performansını proaktif olarak gözlemlemesine olanak tanır. Şirket içinde ( *on-premises* ) veya bulut üzerinden dağıtılan yazılım ya da donanım tabanlı bir çözüm olabilir. Panolar, geliştiricilerin sorunları hızla izole edip düzeltmesine yardımcı olmak için uygulama telemetrisi hakkında içgörü sağlar.

Uygulama izleme, uygulamanın kullanılabilirliğini ( *availability* ) ve performansını en üst düzeye çıkarmaya yardımcı olabilir. Uygulama geliştiricilerini daha verimli hale getirerek operasyon maliyetlerini düşürür ve veriye dayalı kararlar yoluyla müşteri deneyimini iyileştirip iş büyümesini yönlendirir.
