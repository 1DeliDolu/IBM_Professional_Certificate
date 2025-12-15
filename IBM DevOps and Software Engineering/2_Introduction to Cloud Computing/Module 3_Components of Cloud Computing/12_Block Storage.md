# 🧱 Block Storage

Bu videoda  *Block Storage* ’ı ve bulutta *File Storage* ile nasıl karşılaştırıldığını ele alacağız.

 *Block storage* , dosyaları veri parçalarına (veya bloklara) böler ve her bloğu benzersiz bir adres altında ayrı ayrı depolar. *Direct attached storage* ve *file storage* gibi, *block storage* da iş yükleriniz için kullanılmadan önce bir  *compute node* ’a bağlanmalıdır.

 *Block storage* , *file storage* gibi uzak depolama cihazlarından ( *remote storage appliances* ) bağlanabilir; bu da onu arızalara karşı son derece dayanıklı hale getirir ve bu cihazlarda sunulan *encryption in transit* ve *encryption at rest* hizmetleri sayesinde veriyi çok daha güvenli tutar.

 *Block storage* , compute node’lara bir *volume* olarak, sinyallerin ışık hızında hareket ettiği özel bir fiber ağ üzerinden bağlanır. Bu fiber optik ağlar,  *File Storage* ’ı sağlayan ethernet ağlara göre daha pahalıdır; bu da  *Block Storage* ’ın genellikle daha yüksek bir fiyat noktasına sahip olmasının nedenlerinden biridir. Ancak trafik daha hızlı ve hız tutarlılığıyla aktığı için, düşük gecikmeli ( *low-latency* ) depolamaya ihtiyaç duyan iş yükleri için idealdir.

## 🧩 İş Yükleri Açısından Farklar

İş yükleri açısından,  *File Storage* ’ın 80 veya daha fazla compute node’a bağlanabilmesine karşın,  *Block Storage* ’ın normalde aynı anda yalnızca bir compute node’a bağlandığını belirtmek önemlidir. Bu diskler tutarlı biçimde yüksek hızda çalıştığından, veritabanları ve posta sunucuları gibi sürekli hızlı depolama gerektiren iş yükleri için mükemmeldir.

 *Block storage* , compute node’lar arasında belirli bir düzeyde disk paylaşımı gereken iş yükleri için uygun değildir.

## 📈 IOPS Gereksinimleri

*Block storage* için de *file storage* için de, depolamanın *IOPS* kapasitesini dikkate almanız gerekir. Çoğu bulut sağlayıcısı, depolama sağlarken *IOPS* özelliklerini belirtmenize ve bazı durumlarda ihtiyaç duydukça depolamanızın *IOPS* değerlerini ayarlamanıza izin verir; dolayısıyla bir uygulamanın gereksinimleri veya kullanım davranışı değişirse buna göre uyarlayabilirsiniz.

## 🧾 Özet: Benzerlikler ve Farklar

Bu iki depolama türünün ortak yönlerini ve farklılıklarını özetlemek gerekirse: *Block* ve  *File Storage* , hizmet sağlayıcı tarafından bakımı yapılan cihazlardan alınır. Her ikisi de normalde yüksek erişilebilirlik ( *highly available* ) ve dayanıklılığa sahiptir ve çoğu zaman *data encryption at rest* ve *in transit* içerir.

 *File storage* , bir compute node’a ethernet ağı üzerinden bağlanır; bu nedenle bazen *Network attached* veya *NFS Storage* olarak adlandırılır. *File storage* çok güvenilirdir; ancak bağlayıcı ağın hızı yüke bağlı olarak değişebilir.

 *Block storage* , yüksek hızlı fiber ağ üzerinden bağlanır; bu çok güvenilir ve tutarlıdır. *File storage* aynı anda birden fazla compute node’a bağlanabilir. *Block storage* ise aynı anda yalnızca bir node’a bağlanabilir.

 *File storage* , dosya paylaşımlarının gerektiği, iş yüklerinin depolamaya “şimşek hızında” bağlantı gerektirmediği veya maliyetin önemli olduğu durumlarda iyi bir seçimdir. *Block storage* ise veritabanları gibi diske tutarlı ve hızlı erişim gerektiren bir uygulamayı desteklerken iyi bir seçimdir.

Her iki depolama türünü sağlarken de uygulamanın *IOPS* gereksinimlerini göz önünde bulundurmayı unutmayın.

---

# 🎙️ IBM Cloud’dan Gelen Anlatım

Hey arkadaşlar, benim adım Amy Blea. IBM Cloud’da offering ekibindeyim ve bugün sizinle bazı geleneksel depolama türleri hakkında konuşmak istiyorum: *file* ve  *block storage* . Ne olduklarına dair genel bir bakış sunup, birini diğerine tercih etmeye ne zaman karar vereceğinize dair bazı ipuçları vereceğim.

O halde başlayalım:  *block storage* .

 *Block storage* , verilerin depolama üzerinde ham bloklar halinde yazıldığı ve sahip olduğunuz sunucular tarafından bir *storage area network* üzerinden erişildiği depolamadır. Yani tüm sunucularınız vardır; birbirleriyle aynı ağda ya da farklı bir ağda olabilirler, ancak hepsi depolamaya bu *storage area network* üzerinden bağlanır.

## ✅ Block Storage’ın Avantajları

*Block storage* kullanmanın bazı avantajları şunlardır:  *block storage* , uygulamalarınız için mümkün olan en düşük gecikmeyi sağlar ve ayrıca yüksek performans veya çok sayıda *IOPS* gerektiren uygulamalar için kullanılabilir.

*Block storage* ile ilgili bir diğer şey de, genel olarak yüksek derecede yedekli ( *highly redundant* ) olmasıdır. Çoğu *block storage* hizmeti, verinizin hacim ( *volume* ) genelinde yedekli olmasını sağlayan yerleşik bir yetenek sunar; böylece, örneğin bir volume devre dışı kalırsa veya bir disk kaybolursa, uygulamanıza herhangi bir etki olmadan verinizi başka bir yerden geri alabilirsiniz.

## 🔌 File Storage’ın Bağlanma Şekli

 *File storage* , hizmetinize  *block storage* ’dan biraz daha farklı şekilde bağlanır. Her şey aynı ağ üzerinde bağlıdır; yani tüm dosyalarınız veya dosya paylaşımınız ( *file share* ) burada bulunur. Bunların hepsine, o ağ üzerindeki herhangi bir sunucu tarafından erişilebilir. Yani bu,  *network attached storage* ’dır.

*File storage* son derece ölçeklenebilirdir; ağınızda birden çok  *file share* ’iniz olabilir ve tüm sunucularınızı aynı anda buna bağlı tutabilirsiniz. Birden çok çalışma zamanı ( *multiple runtimes* ) tarafından erişilebilirdir.

Bu görsel anlatımda, birden fazla sunucunun aynı anda eriştiği tek bir *file share* görüyoruz; ayrıca tek seferde birden çok eşzamanlı okuma ve yazma işlemi ( *simultaneous reads and writes* ) da gerçekleştirebilirsiniz ve verinizin üzerine yazılması konusunda endişelenmenize gerek kalmaz.

## 🧠 Hangisini Ne Zaman Seçmelisiniz?

Peki uygulamanız için *block storage* mı yoksa *file storage* mı seçmenin doğru zamanı ne zaman? Öncelikle, bunu ne için kullandığınızı düşünmeniz gerekir.

Örneğin, bir *VMware* yapılandırmanız olduğunu ve üzerinde *VMware* bulunan birden çok sanal sunucunuz olduğunu ve  *boot volumes* ’a ihtiyaç duyduğunuzu varsayalım. Bu durumda *block storage* kullanırsınız.

*Transactional databases* veya çok düşük gecikme ve yüksek performans gerektiren *relational databases* gibi iş yükleriniz varsa, *block storage* seçersiniz.

Yapılandırılmış ( *structured* ) ve yapılandırılmamış ( *unstructured* ) verinin bir karışımı olan durumlarda, örneğin hem metin dosyaları hem de medya dosyaları bulunan bir web hosting sunucusunda, *file storage* seçersiniz.

Ayrıca birden çok kullanıcının aynı anda erişmesi, birlikte çalışması, aynı anda okuma ve yazma yapması gereken bir işbirliği alanınız ( *collaborative space* ) varsa, *file storage* seçersiniz.

## 🏁 Kapanış

Başta da belirttiğim gibi, *block* ve *file storage* oldukça geleneksel depolama türleridir. Pazara giren yeni depolama hizmetleri kadar gösterişli, parlak veya “heyecan verici” olmayabilirler; ancak ister kurum içi ( *on premise* ) ister bulutta olsun, sahip olduğunuz farklı iş yükleri için hâlâ çok ilgili ve kullanışlıdırlar.

Bugün benimle birlikte *file* ve *block storage* arasındaki farklar videosunu izlediğiniz için teşekkürler. Sorularınız, yorumlarınız veya diğer videolar için fikirleriniz varsa yorumlara bir şeyler yazın; gelecekte buna benzer daha fazla video görmek isterseniz abone olun.

Bir sonraki videoda  *Object Storage* ’a bakmaya başlayacağız.
