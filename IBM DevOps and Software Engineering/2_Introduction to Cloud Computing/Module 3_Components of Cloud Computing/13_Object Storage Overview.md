# 🧺 Object Storage Genel Bakış

Bu videoda *nesne depolamanın (object storage)* ne olduğunu, verilerin nesne depolamada nasıl saklandığını ve bunun *dosya (file)* ve *blok (block) depolama* gibi daha geleneksel depolama türlerinden nasıl farklılaştığını anlamaya başlayacağız.

## 🧩 Nesne Depolamanın Temel Farkı: Compute Node’a Bağlanmaz

*Nesne depolama* ile ilgili ilk dikkat edilmesi gereken şey, onu kullanmak için belirli bir  *compute node* ’a bağlamamanızdır.

Bunun yerine bir *object storage service instance* sağlarsınız ve verilerinizi yüklemek, indirmek ve yönetmek için bir *API (application programming interface)* kullanırsınız.

Bu, API çağırabildiğiniz her şeyle nesne depolamayı doğrudan kullanabileceğiniz anlamına gelir ve altta yatan bir  *compute node* ’a ihtiyacınız yoktur.

## 💰 Maliyet Avantajı

*Nesne depolama* ile ilgili ikinci dikkat edilmesi gereken şey, diğer *Cloud storage* seçeneklerine kıyasla daha ucuz olmasıdır.

Gigabayt başına maliyeti genellikle ayda birkaç ABD senti seviyesindedir ve bazı durumlarda kullanılan  *storage tier* ’a bağlı olarak daha da düşük olabilir—*storage tiers* konusuna daha sonra değineceğiz.

## ♾️ Pratikte Sınırsız Kapasite

*Nesne depolama* ile ilgili üçüncü ve muhtemelen en önemli dikkat edilmesi gereken nokta, pratikte sınırsız olmasıdır.

*Dosya* ve  *blok depolamada* , istediğiniz depolama boyutunu gigabayt veya terabayt cinsinden belirlersiniz ve sağladığınız boyuta göre bir ücret ödersiniz.

*Nesne depolamada* ise yalnızca ihtiyaç duyduğunuz depolamayı tüketirsiniz ve kullandığınız kadarını gigabayt bazında ödersiniz.

Dosya yüklemeye devam edebilirsiniz ve depolama asla tükenmez.

## 🗂️ Ne Zaman Kullanılır: Yapılandırılmamış Veriler

Peki, *nesne depolamayı* ne zaman kullanırsınız?

 *Nesne depolama* , büyük miktarda *yapılandırılmamış (unstructured) veri* saklamak için harikadır.

*Yapılandırılmamış* demek, verinin herhangi bir hiyerarşik klasör veya dizin yapısında saklanmadığı anlamına gelir.

*Nesne depolama* *bucket* kullanır ve  *object* ’ler bu  *bucket* ’lar içinde yapısal olarak düz ( *structurally flat* ) bir şekilde saklanır.

## 🪣 Bucket Mantığı ve Sınırlamalar

Bir  *bucket* , anlamlı isimler verebilmeniz ve elbette farklı nesne türleri için farklı  *bucket* ’lara sahip olabilmeniz açısından bir klasöre biraz benzer.

Ancak bir  *bucket* ’ı başka bir *bucket* içine yerleştiremezsiniz.

## 🏷️ Metadata ve Nesne Kimliği

Bir nesne ( *object* ) bir *bucket* içine yerleştirildiğinde, onunla birlikte bazı  *metadata* ’lar da bulunur.

Yani veriye eklenmiş veriler; örneğin bir *object ID* gibi.

Bu  *metadata* , uygulamaların nesneyi bulmasına ve erişmesine yardımcı olur; ayrıca verinin ne zaman saklandığı ya da en son ne zaman erişildiği gibi bilgiler de sağlar.

## 📦 Bucket Boyutu Tanımlanmaz

Bir *bucket* oluşturduğunuzda, herhangi bir boyutlandırma bilgisi sağlamanız veya tanımlamanız gerekmez.

*Bucket* yalnızca içine koyduğunuz veriyi tutar.

Ve servis sağlayıcı yeterli depolama kapasitesinin mevcut olmasını sağlar.

 *Bucket* ’lar birkaç bayttan başlayıp birden çok petabayta kadar veri tutabilir; depolanan veri miktarını istediğiniz kadar yavaş veya hızlı büyütebilir, ayrıca tekrar küçültebilirsiniz.

## 🛡️ Dayanıklılık ve Yüksek Erişilebilirlik Seçenekleri

Servis sağlayıcı, aynı zamanda dayanıklılığı ( *resilience* ) ve nesne depolama çözümünün yüksek erişilebilir ( *highly available* ) olmasını da sağlar.

Bazı  *Cloud provider* ’lar, farklı dayanıklılık seviyelerinde farklı *bucket* türleri sunar.

Örneğin, dayanıklı olan ama verinin yalnızca tek bir veri merkezinde saklandığı  *bucket* ’lar sunarlar.

Bu, verinin belirli bir coğrafi konumda kalması gereken durumlarda veya yüksek erişilebilirliğin daha az önemli olduğu senaryolarda iyi bir seçenektir.

Ardından, verinin aynı bölgede farklı veri merkezleri veya  *zone* ’lar içinde birden çok kez saklandığı ya da hatta birden çok bölgede saklandığı, bölgeler arası ( *across regions* ) yüksek erişilebilir  *bucket* ’lar sunarlar.

Bu seçenekler genellikle daha pahalıdır, ancak veriniz için hem en yüksek dayanıklılık hem de erişilebilirlik seviyesini sağlar.

## 🧱 Düz Depolama Yapısı ve Uygun Veri Türleri

*Nesne depolama* çok düz ( *very flat* ) bir depolama yapısına sahiptir; bunu bir sonraki derste açıklayacağız.

Bu veri; metin dosyalarından ses dosyalarına ve video dosyalarına, IoT verilerinden sanal makine imajlarına, yedekleme dosyalarından veri arşivlerine kadar her şey olabilir.

Hemen hemen statik olan ve hızlı okuma/yazma hızlarının gerekli olmadığı her veri, *object storage* için iyi bir uyum sağlar.

## 🚫 Uygun Olmadığı Yerler

 *Nesne depolama* ; işletim sistemlerini çalıştırmak için uygun değildir; ayrıca veritabanları gibi uygulamalar veya dosya içeriklerinin değiştiği herhangi bir şey için de uygun değildir.

## 🧾 Özet

Bu derste öğrendiklerimizi özetlemek gerekirse, *object storage* statik olan dosyaları veya nesneleri saklamak için kullanılır.

*Nesne depolama* kullanarak saklayabileceğiniz veri; metin dosyalarından ses ve video dosyalarına, IoT verilerinden sanal makine imajlarına, yedekleme dosyalarından veri arşivlerine kadar her şey olabilir.

*Nesne depolama* kullanarak işletim sistemlerini veya veritabanları gibi diğer uygulamaları çalıştıramazsınız.

*Nesneler*  *bucket* ’lar içinde saklanır.

Birden fazla  *bucket* ’a sahip olabilirsiniz ancak  *bucket* ’ları  *bucket* ’ların içine koyamazsınız.

Bir *bucket* için boyut belirtmeniz gerekmez.

İhtiyacınız kadar az veya çok alan kullanabilirsiniz.

Birçok sağlayıcı, her biri için farklı ücretlendirmelerle farklı türde  *bucket* ’lar sunar.

Bazıları dayanıklılık ve erişilebilirliğe göre, diğerleri ise içindeki nesnelere ne sıklıkla erişildiğine göre belirlenir.

## ⏭️ Sonraki Video

Bir sonraki videoda, *object storage data tiers* ve  *object storage API* ’lerine dalacağız.
