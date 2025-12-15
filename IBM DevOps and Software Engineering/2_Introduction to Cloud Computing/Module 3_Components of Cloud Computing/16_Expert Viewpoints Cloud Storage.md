# 🧠 Uzman Görüşleri: Bulut Depolama

Bulut depolama uzman görüşlerine hoş geldiniz. Bu videoda, birkaç bulut uygulaması profesyonelinin bulut depolama seçimi için faktörleri tartıştığını dinleyeceğiz.

## 💬 İhtiyaçlara En Uygun Bulut Depolamayı Seçerken Hangi Faktörleri Dikkate Alıyorsunuz?

> Bu nedenle projelerim için bulut depolama almayı düşündüğümde, üç ana şeye bakıyorum. Birincisi, bana ne kadara mal olacak? İkincisi, depolamaya veri giriş/çıkış hızı nedir? Ve üçüncüsü, ne kadar süre boyunca benim için erişilebilir olacak?

Depolama aslında oldukça karmaşık olabilir. Çoğu zaman farklı depolama türlerini kullanmanız gerekir; ancak sormanız gereken ilk soru şudur: *Bu depolama ne için kullanılıyor?* Ne kadar hızlı olması gerekiyor? Kaç kişi kullanıyor, ne sıklıkla?

Ne kadara mal olacağını dikkate almak çok önemlidir. Ve maliyet aslında zor olabilir; çünkü sadece kullandığınız depolama miktarı değil, çoğu zaman ona ne sıklıkla ve ne kadar eriştiğiniz de önemlidir. Bu nedenle, bu depolamayı ne için kullanmanız gerektiğini gerçekten anlayın ve ardından tüm bu farklı şeyleri cevabınıza dahil edin; bu da umarım sizi doğru depolamaya veya probleminizi çözmek için kullanmanız gereken birden fazla depolamaya yönlendirmeye yardımcı olur.

> Bulut depolama ihtiyaçlarınıza karar verirken dikkate alınacak faktörler; maliyet, performans, güvenlik ve operasyonel kullanım kolaylığını içerir.

## 🗂️ Dosya, Blok ve Nesne Depolama Arasında Karar Vermek

Bulut depolamaya karar verirken genellikle  *dosya (file)* , *blok (block)* ve *nesne (object)* depolama arasında karar verirsiniz.

 *Dosya depolama* , çoğu kişiye en tanıdık gelen arayüze sahiptir. Temelde yerel bilgisayarınızdaki gibi bir dosya sistemidir. Birden fazla istemcinin eşzamanlı erişim için mount etmesini destekler ve bu, onu kullandığım zamanlarda tipik olarak tercih etme sebebim olmuştur.

*Blok depolama* eşzamanlı erişimi desteklemez, ancak çok düşük gecikmeye sahiptir ve genellikle veritabanları gibi performans yoğun uygulamalar için tercih edilen depolama türüdür.

*Nesne depolama* ise genellikle sık değiştirilmediği büyük, yapılandırılmamış veriler için tercih edilir. Örneğin; büyük veri setleri, video dosyaları, veritabanı yedekleri, bu tür şeyler.

> Depolama, depolama türüne bağlı olarak birçok şekilde karakterize edilebilir. Bir tür nesne depolamadır. İkinci tür blok depolamadır; NFS gibi dosya depolama ya da veritabanı depolama, SQL veya NoSQL servisleridir.

## 🏷️ Bulutta Depolama Sınıfları ve Kullanım Senaryoları

Şimdi, bulut bilişimde edinebileceğiniz farklı depolama sınıfları veya depolama kategorileri vardır.

Bir uygulama üzerinde çalışıyorsam ve son kullanıcı verisini ya da bir tür yapılandırmayı depolamak istiyorsam, *bulut nesne depolamaya* bakarım. Bulut nesne depolama yavaş olsa da, bulut nesne deposu içinde oluşturabileceğim bu *sınırsız alanı* veya  *bucket* ’ları bana sağlar.

Biraz daha hızlı bir şeye ihtiyacım varsa; örneğin hızın önemli olduğu bir veritabanı depolaması gibi, o zaman *blok seviyesinde depolamaya* bakabilirim. Bu depolama fiber ağlarda çalışır ve bu nedenle bulut nesne depolamada olduğu gibi İnternet üzerinden çalışmaya kıyasla biraz daha hızlıdır.

Üçüncü kategori ise  *dosya depolamadır* . Dosya depolamanın dezavantajı, blok depolamadan biraz daha yavaş olmasıdır. Ancak dosya depolama belirli bir sunucuya mount edildiğinden, onu benim tarafımda birden fazla uygulama ve birden fazla sunucu için ortak depolama olarak kullanabilirim.

## ⏱️ Gecikme, Güncelleme Maliyeti ve Erişim Desenleri

> Nesne depolamada güzel ve düşük maliyet elde edebilirsiniz, ancak en yüksek ya da en düşük gecikmeyi elde edemeyebilirsiniz. Çünkü nesne depolamada, bir dosyanın çok küçük bir kısmını güncellediğinizde bile, diyelim ki bir dosyanın bir harfini güncelliyorsunuz, tüm nesneyi güncellemeniz gerekir.

Böylece tüm o güncellemenin bedelini ödersiniz ve ayrıca tüm nesnenin güncellenmesini beklemek zorunda kalırsınız. Oysa *dosya depolamanız* varsa, veriye eklemeler yapabilirsiniz. Ve genellikle bu dosya depolama, gerçek hesaplama (compute) kaynaklarınıza daha yakın şekilde bağlıdır ve bu yolla çok daha düşük gecikme elde edebilirsiniz.

Bir diğer depolama türü de  *blok depolamadır* . Bulutta, blok depolama ile optimize edilmiş sanal makineleri seçebilirsiniz; bunlar blok depolama ile sunucu arasında son derece düşük gecikmeye sahiptir. Bu nedenle aşırı düşük gecikme için bu harika bir çözüm olabilir.

## 🔐 Güvenlik, Şifreleme, Yaşam Döngüsü ve Maliyet

> Buradaki bazı değerlendirmeler güvenlik ve şifrelemedir. Yani ideal olarak, verinin hem *beklemede (at rest)* hem de *aktarım sırasında (in flight)* şifrelenmesini istersiniz.

Dikkate alınacak diğer faktörler arasında veri erişim sıklığı bulunur; düşük gecikme ile çok aktif erişimden, daha seyrek erişime, seyrek ya da  *cold storage* ’a veya uzun vadeli depolama için  *archive* ’a kadar.

Bir diğer faktör maliyettir. Yani daha sık erişim ve daha düşük gecikme genellikle daha pahalı olacaktır. Bu servisler ve iş gereksinimleri. Veri belki *değiştirilemez (immutable)* ya da korunmuştur; öyle ki değiştirilemez veya silinemez. Bir diğeri de veri yaşam döngüsü ve eski verileri tutmak, taşımak, arşivlemek veya silmek için politikaları nasıl otomatikleştireceğinizdir.

## 🌐 Depolama Alan Ağı ve İçerik Dağıtım Ağı

> Ve bazı bulut sağlayıcıları, bulut sanal makinelerinizden erişebileceğiniz, bir sürü blok depolamayı tek bir depolama alan ağı (storage area network) gibi kullanabilmeniz için şu anda bir *storage area network* çıkarıyor.

Dikkate alınacak bir diğer şey de şifreleme seçenekleridir. Neyse ki şu anda buluttaki çoğu depolama çözümü depolamanızı şifreleme yeteneğine sahiptir. Ancak bunun bir özellik olduğundan emin olmak istersiniz.

Ve sonra bir başka seçenek de *content delivery network* olarak adlandırılır. İçerik dağıtım ağları için bu, örneğin medyanın son kullanıcıya mümkün olduğunca yakın depolanmasını istiyorsanız bir seçenektir; böylece web sitenizi yüklediklerinde ve görüntülere baktıklarında, medya tüm bölgelere kopyalandığı için bunlar anında yüklenir.
