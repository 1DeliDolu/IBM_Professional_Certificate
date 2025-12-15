# 🪣 Object Storage - Katmanlar ve API’ler

Bu videoda  *Object Storage* , *Data Tiers* ve *Object Storage API’lerine* daha yakından bakacağız.  *Object Storage bucket* ’larının ayrıca  *storage tier* ’ları (veya  *class* ’ları) bulunur ve bu katmanlar, veriye ne sıklıkla erişildiğine göre belirlenir.

*Standard tier* bucket, sık erişilen nesneleri saklayacağınız yerdir. Bu katman genellikle en yüksek *gigabyte başına maliyete* sahiptir.

*Vault* veya  *archive tier* , belgelere ayda yalnızca bir ya da iki kez (veya daha az) erişildiği durumlarda kullanılabilir ve daha düşük bir depolama maliyetiyle sunulur. Ayrıca *cold vault tier* da olabilir; burada genellikle yalnızca yılda bir ya da iki kez erişilen veriler saklanır. Bu depolama çoğu zaman ayda gigabyte başına ABD’de bir sentin çok küçük bir kısmı kadar maliyete sahiptir.

Çoğu zaman veriniz için otomatik arşivleme kuralları da ayarlayabilirsiniz; yani bir nesne belirli bir süre erişilmezse otomatik olarak daha ucuz bir depolama katmanına taşınır. Bu kural, nesnenin ne zaman arşivlenmesi gerektiğini belirlemek için nesnenin  *metadata* ’sının bir kısmını kullanır.

 *Object Storage* ’ın *IOPS* seçenekleriyle gelmediğini unutmayın.  *Object Storage* , dosya veya blok depolamaya kıyasla genellikle çok yavaştır; indirmelerin tamamlanması çoğunlukla saniyeler sürer, hatta daha uzun da sürebilir. Sağlayıcılar *cold vault* bucket’ları sunduğunda, bu katmanlardan veri geri getirme bazen saatler bile sürebilir çünkü depolama çevrimdışı tutulur. Uygulamanızın dosyalara hızlı erişmesi gerekiyorsa, *object storage* iyi bir seçenek olmayabilir.

 *Object storage* ’ın kullanılan gigabyte başına fiyatlandırıldığından bahsetmiştik, ancak verinin geri alınmasıyla ilgili başka maliyetler de olabilir. Bu maliyetler benzer şekilde düşük olsa da, veriler *vault* veya  *cold vault tier* ’larında olduğunda erişim ücretleri daha yüksek olabilir. Bu nedenle, verinin erişim sıklığına göre doğru katmanda olduğundan emin olmak önemlidir.

 *Object Storage* ’a erişmek için bir  *compute node* ’a bağlanması gerekmez; bunun yerine *application program interface* ya da *API* üzerinden erişirsiniz. *Object Storage* için en yaygın API, AWS tarafından sunulan S3  *object storage* ’a dayanan bir standart olan  *S3 API* ’dir. Birçok sağlayıcı, *S3 compatible* olan API’ler sunar; bu faydalıdır çünkü geliştiricilerin birden fazla satıcının  *object storage* ’ına erişebilen kod yazabilmesi anlamına gelir.

API’nin kendisi *HTTP based RESTful API* ya da  *RESTful web service* ’tir. API çağrısı, uygulamaların *object storage* ve  *bucket* ’ları yönetmesine; ayrıca nesneleri buralara *put* (yükleme) veya buralardan *get* (indirme) işlemleriyle almasına olanak tanır.

*Object Storage* yalnızca yeni uygulamalar için değildir; mevcut uygulamaların gereksinimlerini karşılamak için de kullanılabilir. Ayrıca,  *off-site tape based solutions* ’ın yerine geçerek yedekleme ve felaket kurtarma için etkili bir çözüm olarak kullanılabilir ve veriyi geri yükleme süresini azaltır. Günümüzde birçok yedekleme paketi, veriyi *object storage* kullanarak buluta yedekleme yeteneğini içerir.

 *Object Storage* , fiziksel olarak teyp sürücülerine yüklenmesi ve çıkarılması gereken; ardından coğrafi yedeklilik için saha dışına taşınması gereken teyp tabanlı yedekleme çözümlerinden daha verimlidir.

## 🧾 Ders Özeti

Bu derste öğrendiklerimizi özetlemek gerekirse:

* *Object storage* ’ın her biri farklı ücretlere sahip farklı katmanları vardır. Bazıları, içindeki nesnelere erişim sıklığına göre belirlenir.
* *Object Storage* , ayda kullanılan depolama gigabyte’ı başına fiyatlandırılır ve ayrıca veri geri alma için bazı ücretler vardır.
* *Object Storage* , dosya veya blok depolamadan çok daha ucuzdur.
* *Object Storage* , dosya ve blok depolamaya kıyasla çok yavaştır.
* Nesneler sık erişilmediğinde daha ucuz katmanlara otomatik arşivlenmesine izin veren kurallar çoğu zaman oluşturulabilir.
* *Object Storage* ’a bir *API* kullanılarak erişilir.
* Birçok *Object Storage* sağlayıcısı  *S3 compatible API* ’ye sahiptir; bu, geliştiricilerin birden fazla satıcının *Object Storage* çözümüne karşı çalışacak kod oluşturabilmesi anlamına gelir.
* Buluttaki  *Object Storage* , etkili bir *Backup and Disaster Recovery Solution* sunar.

Bir sonraki videoda, *Object Storage* tarafından yönlendirilen *Content Delivery Network* ya da *CDN* konusunu ele alacağız.
