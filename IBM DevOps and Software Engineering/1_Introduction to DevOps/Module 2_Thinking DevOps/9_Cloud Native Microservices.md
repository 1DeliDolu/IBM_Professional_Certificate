# ☁️ Bulut Yerel Mikroservisler

Bu videoyu izledikten sonra şunları yapabileceksiniz: Bulut yerel mikroservislerin uygulama tasarımı üzerindeki etkisini fark etmek, stateless (durumsuz) mikroservisleri açıklamak ve monolitik ile mikroservis mimarilerini karşılaştırmak.

DevOps’tan tam anlamıyla yararlanmak için uygulama tasarımı hakkında farklı düşünmeniz gerekir. Bulut yerel mikroservisleri düşünmeniz gerekir.

Bu görsel, küçük mikroservislerden oluşan bir koleksiyon olarak tasarlanmış bir uygulamayı gösteriyor. Bu servislerin her biri diğerlerinden bağımsızdır. Her servis, uygulamanın belirli bir alanını (domain) kapsar. Servis adlarından bunun bir araç çağırma (ride-sharing) servisi örneği olduğunu anlamış olabilirsiniz.

Sürücüler, ödemeler, yolculuk yönetimi ve bildirimler vardır. Bunların hepsi, bir iş alanı etrafında tek amaçlı olacak şekilde tasarlanmış küçük servislerdir.

Bir servisten diğerine giden çizgilere dikkat edin. Bunlar REST API’leri (representational state transfer architectural style Application Programming Interface) işaret eder. Hiçbir servis başka bir servisin veritabanına erişmiyor. Hatta görselde veritabanları bile yer almıyor. Bu, mikroservis kullanan bulut yerel bir tasarımdır.

---

## 🧱 Stateless Servisler ve Bulut Yerel Tasarım

Bu, durumsuz (stateless) servislerin bir koleksiyonudur. Bulut yerel (cloud native), “bulutta doğmuş” anlamına gelir; bulutun sunduğu yatay ölçeklenebilirlikten yararlanır.

Bu servisler, bulut yerel uygulamaların nasıl davranması gerektiğini açıklayan **“The Twelve-Factor App”** içinde belirtilen yönergeleri izler. Bu, 2011’de Heroku ekibi tarafından ilk kez oluşturulmuştur. Heroku, ilk platform-as-a-service uygulamalarından biriydi ve bugün sahip olduğumuz bulut yerel platformlara giden yolu açtı.

Uygulamalar, durumsuz mikroservislerin bir koleksiyonu olarak tasarlanır. Durumsuz, uygulamanın durumu olmadığı anlamına gelmez.

Bu, servislerin (gizli) durumu tutmadığı anlamına gelir. Durum bir veritabanında kalıcı hale getirilir; her servis kendi durumunu ayrı bir veritabanında veya kalıcı bir nesne deposunda (persistent object-store) tutar.

Durumun ayrılması önemlidir. Servisler durumu paylaşsaydı mikroservisleriniz olmazdı. Sadece dağıtık bir monolitiniz olurdu.

Dayanıklılık (resilience) ve yatay ölçekleme, birden fazla instance dağıtarak elde edilir. Uygulamanızı birden fazla bağımsız servise böldüğünüzde, ihtiyaç oldukça onları bağımsız şekilde ölçekleyebilirsiniz.

Örneğin, diğer servisleri ölçeklemeden sadece bildirim (notification) servisini büyütebilirim. Bu, bulut platformunun sorunsuz ve “sonsuz” yatay ölçeklenebilirliğinden yararlanır.

Hata ayıklamak ve yama yapmak yerine, arızalı instance’lar öldürülür ve yeniden ayağa kaldırılır (respawn). Sıkça “instance’lar evcil hayvan değil, sığırdır (cattle not pets)” ifadesini kullanırız. Instance’larınıza fazla bağlanmayın. İhtiyaç oldukça scale out yaparız, ihtiyaç kalmadığında da geri scale ederiz.

Uygulamayı çok sayıda küçük mikroservise böldüğünüzde, bu servislerin sürekli teslimini (continuous delivery) yönetmeye yardımcı olması için DevOps pipeline’larını kullanmanız gerekir.

---

## 🧠 Mikroservis Tanımı

*Mikroservis* terimi Martin Fowler ve James Lewis tarafından ortaya atılmıştır. Şöyle dediler: “mikroservis mimari stili, tek bir uygulamayı küçük servislerden oluşan bir takım (suite) olarak geliştirme yaklaşımıdır; her biri kendi sürecinde (process) çalışır...”

Bunlar sadece thread değildir. Bunlar bağımsız çalışan tam süreçlerdir, “...ve hafif mekanizmalarla, çoğunlukla bir HTTP kaynağıyla iletişim kurar.” Günümüzde bu hafif mekanizmalar olarak REST API’leri kullanıyoruz.

Fowler ve Lewis devam ederek şunu söyler: “Bu servisler iş kabiliyetleri etrafında inşa edilir ve tamamen otomatik dağıtım mekanizmasıyla bağımsız olarak deploy edilebilir.”

Araç çağırma uygulamasında her servisin sürücü servisi, yolcu servisi ve bildirim servisi gibi bir iş kabiliyeti etrafında inşa edildiğini gördünüz.

Bu servisler bağımsız deploy edilebilir. Örneğin, her şeyi yeniden deploy etmeden bildirim servisini yükseltebilirim. Mikroservislerin her şeyin bağımsız deploy edilmesini mümkün kılması özellikle önemlidir.

---

## 🏗️ Monolit ve Mikroservis Karşılaştırması

Bu, monolit ile mikroservislerle çalışmaya kıyasla nasıl işler?

Hesaplamalar, kopyalama yetenekleri ve yapılacaklar (to-dos) içeren bir monolitiniz olduğunu varsayalım. Bu uygulamayı deploy ettiğinizde, tüm bileşenleri birlikte deploy etmek zorundasınız.

Bunları bağımsız mikroservislerden oluşan birden fazla instance’a ayırabiliriz.

Eğer hesaplama kapasitesini artırmam gerekirse, bu üç instance’ı ölçekleyip belki ona çıkarabilirim. To-dos’u veya kopyalama yeteneklerini ölçeklemem gerekmez. Bulut kaynaklarını en iyi şekilde kullanmak için bunları bağımsız ölçekleyebilmek çok önemlidir.

Her mikroservisin, kendi durumunu takip ettiği kendi veritabanı olur. Bunları bağımsız deploy edebilirim ve veritabanını da bağımsız değiştirebilirim. Bunu yapmak için sadece kendi ekibimle değişimi koordine etmem yeterlidir; çünkü diğer servisler iletişim için REST API’leri kullanır. Veritabanında birbirlerinin tabloları üzerinde select atmazlar.

Bir e-ticaret sitesinde çalıştığınızı düşünün; bu bir monolit olsun ve müşteri tablosunu değiştirmek istiyor olun. Muhtemelen müşteri tablosunu değiştirmek için sipariş ekibi ve kargo ekibindeki kişilerle koordine olmanız gerekir; çünkü sipariş ve kargo için ona bağımlıdırlar.

Bir mikroserviste, diğer ekiplerle koordine olmaya gerek yoktur; çünkü siz sadece benim REST API’mi çağırıyorsunuz. Benim tablomun nasıl göründüğüyle ilgilenmezsiniz. API üzerinden gelirsiniz.

SQL veritabanından NoSQL veritabanına geçebilirim ve siz bunu asla bilmezsiniz. Siz müşteri verisini istersiniz, ben size müşteri verisini veririm.

Monolit ile mikroservis mimarisi arasındaki fark budur. Mikroservislerde her servis gevşek bağlıdır (loosely coupled) ve bir REST API aracılığıyla iletişim kurar.

---

## 🧾 Özet

Bu videoda şunları öğrendiniz:

Bulut yerel mimari, bağımsız deploy edilebilen mikroservislerin bir koleksiyonudur.

Durumsuz mikroservisler, kendi durumlarını ayrı bir veritabanında veya kalıcı bir nesne deposunda tutar.

Mikroservisler ölçeklenebilirlik için tasarlanmış, gevşek bağlı servislerdir ve API’ler üzerinden iletişim kurar.
