# 🧪 Introduction to Sampling

Introduction to Sampling’e hoş geldiniz. Bu videoyu izledikten sonra, *örnekleme (sampling)* ve *loglama (logging)* kavramını açıklayabileceksiniz.

Bulut ortamlarında ve yazılım sistemlerinde, birden fazla örnek (instance) üzerinde dağıtılmış büyük ölçekli uygulamalarınız olabilir. Bu uygulamalar yüksek hacimde log üretebilir ve bu logları verimli şekilde yönetmek zorlayıcı hale gelebilir. Örnekleme ve loglama altyapısı, log işlemeyi optimize etmeye ve maliyetleri azaltmaya yardımcı olabilir.

 *Örnekleme ve loglama (sampling and logging)* , analiz veya depolama için yalnızca log olaylarının bir alt kümesinin toplanması uygulamasıdır. Her bir olayı veya veri parçasını tek tek loglamak yerine, kayıt için rastgele ya da başka ölçütlere göre bir alt küme seçilir.

Bu yaklaşım, log verileri için gerekli depolama miktarını azaltmaya ve yönetim ile analiz süreçlerini kolaylaştırmaya yardımcı olabilir.

---

## 🧭 Örnekleme Stratejileri

Örnekleme stratejileri, analiz ve depolama için log kayıtlarının bir alt kümesinin seçilmesinde kullanılan teknikleri ifade eder. Loglamada yaygın olarak kullanılan birkaç örnekleme stratejisi vardır.

İlk olarak,  *zamana dayalı örnekleme (time-based sampling)* , log kayıtlarını sabit zaman aralıklarında seçer; örneğin her dakika veya her saat.

*Boyuta dayalı örnekleme (size-based sampling)* tekniği, log kayıtlarını boyutlarına göre seçer; örneğin yalnızca belirli bir eşiği aşan kayıtları seçmek gibi.

*Rastgele örnekleme (random sampling)* tekniği, analiz için daha büyük bir kümeden log kayıtlarını rastgele seçer.

*Olay tabanlı örnekleme (event-based sampling)* tekniği, hata veya uyarı gibi belirli olaylara göre log kayıtlarını seçer.

Son olarak, *ağırlıklı örnekleme (weighted sampling)* tekniği, log kayıtlarına önem veya ilgililik düzeylerine göre ağırlıklar atar ve ardından buna göre örnekleme yapar.

Bir loglama sisteminde uygulamadan önce, hangi stratejinin ihtiyaçlarınız için en uygun olduğunu dikkatle değerlendirmek önemlidir.

---

## 🔎 Gözlemlenebilirlikte Örnekleme Kullanımına Örnekler

Örneklemenin, sistem performansı hakkında içgörü elde etmek ve olası sorunları belirlemek için gözlemlenebilirlikte nasıl kullanılabileceğine dair birkaç örneği inceleyelim.

İlk örnek, performans özelliklerini belirlemek için bir uygulamanın CPU kullanımının düzenli aralıklarla örneklenmesiyle ilgilidir.

Ağ paket örneklemesi (network packet sampling), ağdan geçen paketlerin bir örneğinin toplanarak ağ trafiğiyle ilgili sorunların belirlenmesini ifade eder.

Dağıtık sistemlerden izleme (tracing) verilerinin örneklenmesi, darboğazların ve diğer sorunların belirlenmesine yardımcı olur.

Log örneklemesi (log sampling), sistem genelinde farklı kaynaklardan logların toplanması, bunların analiz için örneklenmesi ve olağandışı eğilimler veya kalıpların belirlenmesiyle ilgilidir.

Hata oranı örneklemesi (error rates sampling), bir uygulamanın ürettiği hataları belirleyip örnekleyerek acil müdahale gerektiren kritik sorunların izinin sürülmesiyle ilgilidir.

Kullanıcı davranışı örneklemesi (user behavior sampling), kullanıcı deneyimini geliştirmek için tıklama akışları (click streams), fare hareketleri (mouse movements) ve diğer kullanıcı etkileşimleri gibi verilerin örnekleme yoluyla analiz edilmesini ifade eder.

---

## ✅ Örnekleme ve Gözlemlenebilirlik Kullanmanın Avantajları

İlerleyelim ve örnekleme ile gözlemlenebilirlik kullanmanın avantajlarını belirleyelim.

İlk avantaj, azaltılmış ek yük (reduced overhead) sağlamasıdır. Örnekleme, toplanan veri miktarını azaltır; bu da hesaplama ek yükünü ve depolama gereksinimlerini düşürür.

Bir sonraki avantaj, gelişmiş performanstır (enhanced performance). İşlenecek daha az veri olduğunda analiz ve görselleştirme daha hızlı yapılabilir; bu da daha hızlı yanıt süreleriyle sonuçlanır.

Bir diğer avantaj, maliyet etkinliğidir (cost-effectiveness). Örnekleme kullanarak kuruluşlar, sistem davranışı hakkında değerli içgörüler elde etmeye devam ederken depolama maliyetlerini azaltabilir.

Son olarak, örnekleme; kuruluşların verinin küçük bir bölümünü analiz etmesine olanak tanıyarak ölçeklenebilirlik zorluklarına yardımcı olabilir ve gerektiğinde izleme (monitoring) yeteneklerini ölçeklendirmeyi kolaylaştırır.

---

## ⚠️ Gözlemlenebilirlikte Örneklemenin Dezavantajları

Gözlemlenebilirlikte örneklemenin dezavantajlarını da incelemek önemlidir.

İlk olarak, örneklemenin tüm ayrıntıları yakalamayabileceğini anlamalısınız. Verinin yalnızca bir kısmını analiz etmek, önemli bilgilerin gözden kaçmasına neden olabilir ve potansiyel olarak sistemi etkileyebilir.

İkinci olarak, örnekleme doğru olmayabilir ve her zaman gerçek veriyi temsil etmeyebilir. Örnek verinin doğruluğu, örneğin genel popülasyonu ne kadar iyi temsil ettiğine bağlıdır.

Bir diğer dezavantaj, sınırlı çözünürlüktür (limited resolution). Örnekleme ve izleme sistemleri çözünürlüğü sınırlar. Olayların yalnızca bir kısmı yakalandığında, sistem etkinliğine ilişkin ayrıntılı bir görünüm elde etmek zordur.

Örnekleme ayrıca aykırı değerleri (outliers) maskeleyebilir. Örneklemenin kaçırdığı nadir aykırı değerler, hayati sistem sorunu içgörüleri içerebilir ve fark edilmeyen problemler riskini artırır.

Son olarak, örnekleme; bir sistem içindeki birden fazla değişken ve bağımlılık arasındaki etkileşimlerden doğan karmaşık performans sorunlarını teşhis etmeyi zorlaştırabilir.

---

## 🧾 Video Özeti

Bu videoda, örnekleme ve loglamanın analiz ve depolama için yalnızca log olaylarının bir alt kümesinin toplanması uygulaması olduğunu öğrendiniz.

Loglamada yaygın olarak kullanılan örnekleme stratejileri;  *zamana dayalı örnekleme (time-based sampling)* ,  *boyuta dayalı örnekleme (size-based sampling)* ,  *rastgele örnekleme (random sampling)* , *olay tabanlı örnekleme (event-based sampling)* ve *ağırlıklı örnekleme (weighted sampling)* stratejileridir.

Örnekleme kullanmanın bazı avantajları; azaltılmış ek yük, gelişmiş performans, maliyet etkinliği ve geliştirilmiş doğruluktur.

Bazı dezavantajlar ise ayrıntıların kaçırılması, yanlış veri, sınırlı çözünürlük ve maskelenmiş aykırı değerlerdir.
