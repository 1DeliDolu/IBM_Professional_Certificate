# 🧭 NoSQL’a Genel Bakış

NoSQL’a Genel Bakış’a hoş geldiniz. Bu video, NoSQL terimini ve işaret ettiği teknolojiyi tanımlar ve NoSQL’in veritabanı ekosistemindeki tarihini açıklar.

İlk olarak, NoSQL adından bahsedelim. Bu ad, sahneye yeni çıkan açık kaynaklı dağıtık veritabanlarını tartışmak için düzenlenen bir etkinlikte ortaya atıldı ve o zamandan beri *NoSQL* adı kullanılmaya devam etti. Kulağa geldiğinin aksine, NoSQL aslında “NO SQL” değil, **“Not Only SQL”** anlamına gelir. NoSQL adı, aslında ne olmadığını tarif eder. Yani, stil ve teknoloji açısından oldukça farklılık gösteren, ancak ortak bir özelliği paylaşan bir veritabanı ailesine işaret eder: **ilişkisel olmayan** ( *non-relational* ) bir yapıya sahip olmaları. Bu da, standart satır-sütun tabanlı bir ilişkisel veritabanı yönetim sistemi ( *RDBMS* ) olmadıkları anlamına gelir. Bu nedenle, bu veritabanlarını tanımlamak için daha iyi bir isim **“ilişkisel olmayan”** olurdu.

---

## 🗄️ NoSQL Neyi Sağlar?

NoSQL veritabanları, modern uygulamalar için bir dizi sorunu ele alan yeni veri saklama ve sorgulama yöntemleri sunar. En önemlisi, NoSQL veritabanlarının çoğu, “ *big data* ” hareketiyle birlikte ortaya çıkan farklı türden ölçek ( *scale* ) problemlerini ele almak üzere tasarlanmıştır. Ölçek derken, hem verinin boyutunu hem de bu veri üzerinde eşzamanlı işlem yapan kullanıcı sayısını kastediyoruz.

NoSQL veritabanları, genellikle kullanım senaryolarında daha özelleşmiştir ve ilişkisel veritabanlarına kıyasla uygulama işlevselliği geliştirmek açısından çok daha basit olabilir. Bu kurstaki sonraki videolarda, farklı NoSQL veritabanlarının faydalarına daha ayrıntılı şekilde değineceğiz.

---

## 🕰️ NoSQL Hareketinin Kısa Tarihi

NoSQL hareketinin tarihine hızlıca bakalım. 1970 ile 2000 arasındaki döneme geri dönersek, bazı ilişkisel olmayan veritabanları (örneğin IBM’in IMS’i — ki Apollo uzay görevlerinde kullanılan hiyerarşik bir veritabanıydı) bulunsa da, pazar ilişkisel veritabanlarının hakimiyeti altındaydı. Bu yüzden uygulama mimarları ve geliştiriciler uygulamaları için bir veri deposuna ihtiyaç duyduklarında, temelde çeşitli yaygın ilişkisel veritabanları arasından seçim yapıyorlardı. Oracle, IBM DB2, Microsoft SQL Server ve MySQL, en popüler olanlardan bazılarıydı.

---

## 🌐 Dotcom Dönemi ve Yeni Ölçek Problemleri

90’ların sonu/2000’lerin başındaki dotcom patlaması sırasında internet uygulamaları ve şirketleri hızla büyümeye başladığında, uygulamalar ağırlıklı olarak şirket içindeki binlerce çalışanı desteklemekten, kamuya açık internet üzerinde milyonlarca kullanıcıya hizmet etmeye ihtiyaç duyar hale geldi.

Bu tür uygulamalar için erişilebilirlik ( *availability* ) ve performans hayatiydi ve bu yeni ölçek problemleri, onları desteklemek için yeni ölçeklenebilir teknolojiler oluşturma yönünde bir itici güç yarattı. Bu dönemde IBM, Google ve Facebook gibi büyük teknoloji şirketleri çok sayıda güçlü teknoloji geliştirdi ve bunları topluluğa whitepaper’lar aracılığıyla yayınladı ve/veya açık kaynak yaptı.

Özel örnekler şunları içerir:

* Google’ın **MapReduce** whitepaper’ı, dağıtık sistemlerde büyük veri kümelerinin nasıl işleneceğini anlatıyordu.
* Amazon’un **Dynamo** whitepaper’ı, quorum tarzı bir mimaride küme ( *cluster* ) içinde veri ve iş yükünün nasıl dengeli dağıtılacağını detaylandırıyordu.

---

## 🧩 2000’lerin Sonu: Yeni NoSQL Veritabanlarının Yükselişi

2000’lerin sonlarında, birçoğu açık kaynak topluluklarından çıkan çok sayıda yeni veritabanı ortaya çıktı.  **Apache CouchDB** , **Cassandra** ve **Hbase** gibi veritabanlarının yanı sıra  **Mongo** ,  **Redis** , **Riak** ve **Neo4j** gibi sistemler de daha yaygın kullanılmaya başlandı; özellikle ilişkisel veritabanlarının karşılamakta zorlandığı daha büyük ölçek gerektiren uygulamalarda.

Son 10 yıl civarında ise bazı NoSQL veritabanları, tam yönetilen servis modeli olan **database-as-a-service (DBaaS)** yaklaşımını benimsedi. Bu yaklaşım, yönetim ve bakım yükünü son kullanıcıdan alır ve geliştiricilerin bu modern veritabanlarıyla uygulama geliştirmeye odaklanmasını sağlar. Örnekler arasında **IBM Cloudant** ve **Amazon DynamoDB** bulunur.

---

## 📝 Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* “NoSQL” adının **Not Only SQL** anlamına geldiğini ve NoSQL teriminin mimari olarak **ilişkisel olmayan** bir veritabanı sınıfını ifade ettiğini.
* NoSQL veritabanı uygulamalarının teknik olarak birbirinden farklı olmasına rağmen, hepsinin bazı ortak özellikler paylaştığını.
* Tarihsel olarak ilişkisel veritabanlarının daha yaygın olduğunu, ancak **2000 yılından sonra** Big Data’nın ölçek talepleri nedeniyle NoSQL veritabanlarının veritabanı pazarında daha popüler hale geldiğini.
