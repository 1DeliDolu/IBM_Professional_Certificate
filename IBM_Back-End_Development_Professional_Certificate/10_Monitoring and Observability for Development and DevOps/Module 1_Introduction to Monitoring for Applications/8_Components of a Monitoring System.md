
# 🧩 İzleme Sisteminin Bileşenleri

İzleme Sisteminin Bileşenleri’ne hoş geldiniz! Bu videoyu izledikten sonra şunları yapabileceksiniz: İzleme sistemlerinin bileşenlerini açıklamak ve bir izleme sisteminin önemli niteliklerini belirlemek.

Bir izleme sisteminin temelini oluşturan üç temel bileşen vardır:  *metrikler* , *gözlemlenebilirlik* ve  *uyarı verme (alerting)* .

Bu  *metrikler* , sistemlerinizin sağlığına ilişkin görünürlük, kullanım veya davranıştaki eğilimlerin anlaşılması ve yaptığınız değişikliklerin etkisine dair farkındalık sağlayabilir. Metrikler beklenen aralıklarınızın dışına çıkarsa, bu sistemler bir operatöre inceleme yapmasını bildirmek için bildirimler gönderebilir ve olası nedenlerin belirlenmesine yardımcı olabilir.

 *Metrikler* , sistemleriniz boyunca gözlemlenebilen ve toplanabilen kaynak kullanımı veya davranışı temsil eder. Bunlar, işletim sistemi tarafından sağlanan düşük seviyeli kullanım özetleri olabileceği gibi, bir bileşenin belirli işlevselliğine veya yaptığı işe bağlı daha üst seviye veri türleri de olabilir; örneğin saniye başına karşılanan istekler veya bir web sunucuları havuzuna üyelik gibi.

Bazı metrikler toplam kapasite olarak sunulurken, diğerleri bir bileşenin ne kadar meşgul olduğunu gösteren bir oran ( *rate* ) olarak temsil edilir. Metrikler yararlıdır çünkü özellikle toplu halde analiz edildiklerinde sistemlerinizin davranışı ve sağlığı hakkında içgörü sağlarlar.

Metrikler, geçmiş eğilimleri anlamada kullanılan temel değerlerdir, [.5 saniye duraklama] farklı faktörleri ilişkilendirmek için, [.5 saniye duraklama] ve performansınızdaki, tüketiminizdeki veya hata oranlarınızdaki değişiklikleri ölçmek için kullanılır.

İzleme; farklı servisleri toplama, bir araya getirme ( *aggregating* ) ve izleme ( *watching* ) süreciyken, gözlemleme ( *observing* ) ise bu değerleri analiz ederek bileşenlerinizin özellikleri ve davranışları hakkında farkındalığı artırmaktır.

*Gözlemlenebilirlik* ayrıca toplanan veriler, bir araya getirilmiş bilgiler ve servisler genelindeki kaynaklar ve değerler arasındaki örüntüleri tanımayı ve anlamayı da içerir. Örneğin, bir uygulama hata oranlarında ani bir artış yaşarsa, izleme sistemini gözlemleyen bir yönetici bu artışa hangi olayın katkıda bulunduğunu keşfedebilir.

 *Uyarı verme (alerting)* , metrik değerlerindeki değişikliklere dayanarak eylemler gerçekleştiren bir izleme sisteminin tepkisel ( *responsive* ) bileşenidir.

Uyarı tanımları iki bölümden oluşur: metriğe dayalı bir koşul veya eşik değeri ve değer kabul edilebilir koşulların dışına çıktığında gerçekleştirilecek bir eylem.

Uyarılar, yöneticilerin sistemden ayrışmasına olanak tanır; böylece uygulamaları sürekli izlemeleri gerekmez. Yöneticiler aktif olarak yönetmenin mantıklı olduğu durumları tanımlayabilirken, değişen koşulları aramak için yazılımın pasif izlenmesine güvenebilir.

Bazı programatik yanıtlar da eşik ihlallerine dayanarak tetiklenebilir. Uyarı vermenin temel amacı, herhangi bir sorun veya problem varsa insan dikkatini sistemlerin durumuna çekmektir.

## ✅ İdeal Bir İzleme Sisteminin Önemli Nitelikleri

* Kendi altyapısı üzerinde bağımsız olarak çalışır.
* Güvenilir bir sistemdir.
* Kullanımı kolay pano ( *dashboard* ) görünümleri mevcuttur.
* Uzun zaman çizelgeleri boyunca eğilimler, örüntüler ve tutarlılıkları belirlemeye yardımcı olmak için geçmiş verilerin etkili şekilde tutulması.
* Farklı kaynaklardan korelasyon yapabilme yeteneği.
* Yeni metrikleri veya yeni bir altyapıyı izlemeye başlamak kolaydır.
* Esnek ve güçlü uyarı verme ( *alerting* ) mevcuttur.

## 📌 Bu Videoda Şunları Öğrendiniz

 *Metrikler* , *gözlemleme (observability)* ve  *uyarı verme (alerting)* , birlikte bir izleme sisteminin temelini oluşturan temel bileşenlerdir.

 *Metrikler* , sistemleriniz boyunca gözlemlenebilen ve toplanabilen kaynak kullanımı veya davranışı temsil eder.  *Gözlemlenebilirlik* , izleme yoluyla toplanan verileri analiz ederek bileşenlerinizin özellikleri ve davranışları hakkında farkındalığı artırma sürecidir.  *Uyarı verme* , metrik değerlerindeki değişikliklere göre eylemler gerçekleştiren izleme sisteminin tepkisel bileşenidir ve ideal izleme sistemleri bağımsız bir altyapıya, kullanımı kolay ve güvenilir sistemlere, korunmuş geçmiş verilere ve farklı kaynaklardan gelen verilerin etkili korelasyonuna sahiptir.
