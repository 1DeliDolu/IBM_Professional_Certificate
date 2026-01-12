
# 📊 İzleme Sisteminde Metrik Türleri

İzleme Sisteminde Metrik Türlerine hoş geldiniz! Bu videoyu izledikten sonra şunları yapabileceksiniz: İzleme sistemlerinde takip edilecek önemli metrikleri belirlemek ve Hangi metrikleri izlemeniz gerektiğini belirleyen faktörleri açıklamak. İzleme sisteminin ana bileşenlerinden biri  *metriklerdir* . Metrikleri takip etmek neden önemlidir? Metrikler, uygulamalarınızın kaynakları nasıl kullandığını temsil eder ve sistemlerinizin davranışı ile sağlığı hakkında içgörü sağlar.

Takip etmeniz gereken önemli metrikler:  **host tabanlı** ,  **uygulama** ,  **ağ ve bağlantı** , ve **sunucu havuzu** metrikleridir. Metrik takibi, izleme stratejinizi planlamanıza ve analiz etmenize yardımcı olabilir; çünkü sistemler genellikle hiyerarşik şekilde çalışır ve daha karmaşık katmanlar daha ilkel altyapının üzerine inşa edilir.

---

## 🖥️ Host Tabanlı Metrikler

Host tabanlı metrikler şunları ölçer:  **CPU** ,  **Bellek** ,  **Disk alanı** ,  **Süreçler** . Göstergeler, bir uygulama yığını ve servislerini şimdilik göz ardı ederek, tek bir makinenin sağlığını ve performansını değerlendirmeye dahil olan her şeydir.

Host tabanlı metrikler çoğunlukla işletim sistemi veya donanımın kullanım ya da performansından oluşur.

---

## 🧩 Uygulama Metrikleri

Uygulama metrikleri, servisler veya uygulamalar gibi kaynaklara bağlı işlem ya da iş birimlerine odaklanır. Bakılacak metrik türlerinin spesifik çeşitleri, servisin ne sağladığına, hangi bağımlılıklarının olduğuna ve hangi diğer bileşenlerle etkileşime girdiğine bağlıdır.

Bu seviyedeki metrikler, bir uygulamanın sağlığını, performansını veya yükünü gösterir. Dikkat edilmesi gereken göstergeler şunlardır:  **Hata ve başarı oranları** ,  **Servis arızaları ve yeniden başlatmalar** ,  **Yanıtların performansı ve gecikmesi** , ve  **Kaynak kullanımı** .

Bu göstergeler, bir uygulamanın doğru ve verimli şekilde çalışıp çalışmadığını belirlemeye yardımcı olur.

---

## 🌐 Ağ ve Bağlantı Metrikleri

Altyapının çoğu türü için, ağ ve bağlantı göstergeleri dışa dönük erişilebilirlik için önemli ölçütlerdir; ancak birden fazla makineye yayılan sistemlerde servislerin diğer makineler tarafından erişilebilir olduğuna dair temel işaretlerdir.

Diğer metriklerde olduğu gibi, ağların genel işlevsel doğruluğu ve gerekli performansı sağlama yeteneği şu alanlara bakılarak kontrol edilmelidir:  **Bağlantı** ,  **Hata oranları ve paket kaybı** ,  **Gecikme** , ve  **Bant genişliği kullanımı** .

Ağ katmanınızı izlemek, hem iç hem de dış servislerinizin erişilebilirliğini ve yanıt verebilirliğini iyileştirmenize yardımcı olabilir.

---

## 🧱 Sunucu Havuzu Metrikleri

Yatay ölçeklenen altyapılarla uğraşırken, sunucu havuzları metrik eklemeniz gereken başka bir altyapı katmanıdır. Tek tek sunucular hakkındaki metrikler faydalı olsa da, servis daha iyi şekilde, bir makine koleksiyonunun iş yapabilme ve isteklere yeterince yanıt verebilme kapasitesi olarak ölçek düzeyinde temsil edilir.

Bu metrik türü birçok yönden uygulama ve sunucu metriklerinin daha üst seviye bir çıkarımıdır; ancak bu durumda kaynaklar makine düzeyi bileşenler yerine homojen sunuculardır.

Sunucu koleksiyonlarının sağlığını özetleyen verileri toplamak, sisteminizin yükü taşıma ve değişikliklere yanıt verme konusundaki gerçek kabiliyetlerini anlamak için önemlidir.

---

## 🔗 Harici Bağımlılık Metrikleri

Eklemek isteyebileceğiniz diğer metrikler, harici bağımlılıklar ile ilgili olanlardır. Bunlar, sisteminizin uygulamanızın kullandığı harici sistemlerle etkileşimlerini izlemenize olanak tanır. Bazı bağımlı servisler kesintiler hakkında durum sayfaları sağlayabilir. Ancak bunları kendi sistemleriniz içinde takip ederseniz, sağlayıcılarınızdaki ve operasyonlarınızı etkileyebilecek problemleri belirleyebilirsiniz.

Bu seviyede takip edilecek bazı öğeler şunlardır: **Servis durumu ve erişilebilirliği** **Başarı ve hata oranları**  **Çalışma hızı ve operasyonel maliyetler** , ve  **Kaynak tükenmesi** .

Elbette, toplanması faydalı olabilecek daha birçok metrik türü vardır.

---

## 🧠 Hangi Metriklerin İzleneceğini Belirleyen Faktörler

En önemli bilgiyi farklı odak seviyelerinde kavramsallaştırmak, problemlerin tahmin edilmesi veya tespit edilmesi için en faydalı göstergeleri belirlemenize yardımcı olabilir. Toplayacaklarınızı ve aksiyon alacaklarınızı etkileyebilecek bazı faktörler şunlardır:

* Takip için mevcut kaynaklar: İnsan kaynağınız, altyapınız ve bütçenize bağlı olarak, takip edeceğiniz kapsamı uygulayabileceğiniz ve makul şekilde yönetebileceğiniz ölçüde sınırlamanız gerekir.
* Uygulamanızın karmaşıklığı ve amacı: Uygulamanızın veya sistemlerinizin karmaşıklığı, neyi izleyeceğinizi büyük ölçüde etkileyebilir. Bazı yazılımlar için kritik olan öğeler, diğerleri için önemli olmayabilir.
* Dağıtım ortamı: Sağlam izleme üretim sistemleri için en önemli olsa da, hazırlık ve test sistemleri de izlemeden fayda görür; ancak ciddiyet, ayrıntı düzeyi ve ölçülen metrikler açısından farklılıklar olabilir.
* Metriğin potansiyel faydası: Bir şeyin ölçülüp ölçülmemesini etkileyen en önemli faktörlerden biri, gelecekte yardımcı olma potansiyelidir. Takip edilen her ek metrik sistemin karmaşıklığını artırır ve kaynak tüketir.

Veri gereksinimi zaman içinde değişebilir; bu da düzenli aralıklarla yeniden değerlendirmeyi gerektirir.

* Kararlılığın ne kadar gerekli olduğu: Bazı kişisel ya da erken aşama projelerde kararlılık ve çalışma süresi öncelik olmayabilir. Unutmayın, kararlarınızı etkileyen faktörler; mevcut kaynaklarınıza, projenizin olgunluğuna ve ihtiyaç duyduğunuz servis seviyesine bağlı olacaktır.

---

## ✅ Video Özeti

Bu videoda şunları öğrendiniz: Takip etmeniz gereken önemli metrikler  **host tabanlı** ,  **uygulama** ,  **ağ ve bağlantı** , ve **sunucu havuzu** metrikleridir. Uygulama metrikleri, servisler veya uygulamalar gibi host düzeyi kaynaklara bağlı işlem veya iş birimlerine odaklanır.

İsteğe bağlı olarak izlemeyi seçebileceğiniz bir bileşen **harici bağımlılık metrikleri**dir; bunlar, operasyonlarınızı etkileyebilecek problemleri tahmin etme ve belirleme konusunda yardımcı olur.

Hangi metrikleri izlemeniz gerektiğini belirlemenize yardımcı olan faktörler; takip için mevcut kaynaklar, uygulamanızın karmaşıklığı ve dağıtım ortamınızın ne kadar karmaşık olduğudur.
