# 🧩 NoSQL Veritabanlarının Özellikleri

“NoSQL Veritabanlarının Özellikleri”ne hoş geldiniz. Bu video, NoSQL veritabanlarının kavramlarını ve özelliklerini açıklar ve bir NoSQL veritabanını benimsemenin birincil faydalarını anlatır.

NoSQL veritabanları arasındaki en yaygın özelliğin, mimari olarak **ilişkisel olmayan** ( *non-relational* ) yapıda olmaları olduğunu zaten öğrendiniz. Peki hangi NoSQL veritabanı türleri vardır? Ve bunların ortak noktaları nelerdir?

NoSQL veritabanlarını sınıflandırmak için çeşitli çalışmalar yapılmıştır ve pazarda genel bir görüş birliği, bunların dört türe ayrıldığı yönündedir:  *Key-Value* ,  *Document* , *Column-based* ve *Graph* tarzı NoSQL veritabanları. Bu türler arasında bir miktar örtüşme vardır; bu nedenle tanım her zaman net olmayabilir. Ancak bu kursta daha sonra, farklı türler ve kullanım senaryoları hakkında daha fazla ayrıntı duyacaksınız.

---

## 🔗 NoSQL Veritabanlarını Bir Arada Tutan Nedir?

NoSQL veritabanlarını bir araya getiren ortak noktalardan biri, çoğunun köklerinin açık kaynak topluluğuna dayanması ve açık kaynaklı bir şekilde kullanılmış ve bundan yararlanılmış olmasıdır. Bu, sektörde büyümelerini sıçrama tahtası gibi desteklemede temel bir rol oynamıştır.

Aynı zamanda, veritabanının ticari sürümünü, teknolojiye yönelik hizmet ve desteği sunan; buna paralel olarak da açık kaynak karşılığının sponsorluğunu sağlayan şirketlerle sıkça karşılaşırsınız. Buna örnek olarak CouchDB için IBM Cloudant, Apache Cassandra için Datastax ve Mongo veritabanının kendi açık kaynak sürümüne sahip olan Mongo gösterilebilir.

Teknik olarak aralarında oldukça fark vardır; ancak bazı ortak noktalar ortaya çıkar. Çoğu NoSQL veritabanı **yatay ölçeklenmek** ( *horizontal scale* ) üzere tasarlanmıştır ve ilişkisel muadillerine kıyasla verilerini daha kolay paylaşırlar.

Bunu yapmak için çoğunlukla, bölümlemeyi ( *partitioning* ) veya “ *sharding* ”i basitleştirmek amacıyla, tüm veritabanı boyunca **global unique key** kullanımı gerekir. Ayrıca, geçmişte veri depolarının İsviçre çakısı ( *Swiss army knives* ) olarak görülen  *RDBMS* ’lere kıyasla, belirli kullanım senaryolarına daha fazla özelleşmişlerdir.

Geliştiriciler, veri modelleme ve kullanım kolaylığı nedeniyle NoSQL veritabanlarına yönelir. Son olarak, birçok NoSQL veritabanı, ilişkisel veritabanlarının sabit şemalarına kıyasla esnek şemalarıyla daha çevik ( *agile* ) geliştirmeye olanak tanır.

Şimdiye kadar NoSQL’in ne anlama geldiğini, veritabanı teknolojileri dünyasındaki tarihini ve NoSQL veritabanı özelliklerinin bazı temellerini, ayrıca ilişkisel veritabanlarıyla karşılaştırıldıklarında ortaya çıkan farkları ele aldık. Peki bir NoSQL veritabanını neden kullanırsınız? Ve bu veritabanlarının popülerliği neden bu kadar hızlı artıyor?

---

## 🚀 NoSQL Veritabanlarını Kullanma Nedenleri

Liste uzundur; bu yüzden burada daha yaygın olanlardan bazılarına yer verdik. Her konuya kısaca değinelim; tüm NoSQL veritabanlarının bu faydaların tamamını göstermeyebileceğini akılda tutarak.

### 📈 Ölçeklenebilirlik

Bir NoSQL veritabanı kullanmanın en yaygın nedeni ölçeklenebilirliktir; özellikle sunucu kümeleri ( *clusters* ), raflar ( *racks* ) ve hatta muhtemelen veri merkezleri boyunca **yatay ölçekleme** yeteneği. Uygulamaların değişen taleplerini karşılamak için hem yukarı hem aşağı ölçekleyebilmenin esnekliği ( *elasticity* ) kritiktir. NoSQL veritabanları, “ *Big Data* ” uygulamalarının sergilediği büyük veri boyutlarını ve çok sayıda eşzamanlı kullanıcıyı karşılamak için uygundur.

### ⚡ Performans

Performans konusu ölçeklenebilirlikle birlikte ilerler. Büyük veri kümeleri ve yüksek eşzamanlılık koşullarında bile hızlı yanıt süreleri sunma ihtiyacı modern uygulamalar için zorunludur. NoSQL veritabanlarının büyük sunucu kümelerinin kaynaklarından yararlanabilmesi, bu koşullarda onları hızlı performans için ideal hale getirir.

### 🛡️ Yüksek Erişilebilirlik

Yüksek erişilebilirlik ( *High Availability* ) bir veritabanı için açık bir gereksinimdir ve verilerin birden fazla kopyasıyla sunucu kümeleri üzerinde çalışan bir veritabanı, tek sunuculu bir çözüme kıyasla daha dayanıklı ( *resilient* ) bir çözüm sağlar.

### ☁️ Bulut Mimarileri ve Maliyet Azaltma

Tarihsel olarak büyük veritabanları pahalı makinelerde veya mainframe’lerde çalıştırılırdı. Modern işletmeler uygulamalarını desteklemek için bulut mimarilerini kullanmaktadır ve NoSQL veritabanlarının dağıtık veri doğası, onların bulut mimarilerinde sunucu kümeleri üzerinde dağıtılıp işletilmesini mümkün kılar; bu da maliyeti büyük ölçüde azaltır.

Maliyet, her teknoloji girişimi için önemlidir ve NoSQL benimseyenlerin, mevcut veritabanlarına kıyasla önemli ölçüde maliyet düşürürken aynı veya daha iyi performans ve işlevsellik elde ettiklerini duymak yaygındır.

### 🧱 Esnek Şema ve Sezgisel Veri Yapıları

Esnek şema ve sezgisel veri yapıları, geliştiricilerin uygulamaları verimli şekilde inşa etmek isterken sevdiği temel özelliklerdir. Çoğu NoSQL veritabanı esnek şemalara izin verir; bu da veritabanında kilitlenme ( *locking* ) veya kesinti ( *downtime* ) olmadan uygulamalara hızlıca yeni özellikler eklenebileceği anlamına gelir.

NoSQL veritabanlarının ayrıca, ilişkisel veri depolarının satır ve sütunlarına kıyasla geliştirme ihtiyaçlarını çözmede daha etkili olabilen çeşitli veri yapıları vardır. Örnekler:

* Hızlı lookup için *key-value* depoları
* De-normalized ve sezgisel bilgiyi saklamak için *document stores*
* İlişkisel/bağlantısal veri kümeleri için *graph databases*

### 🧠 Özel Yetenekler

Bazı NoSQL sağlayıcılarının son kullanıcıları cezbeden çeşitli özel yetenekleri de vardır. Örnekler arasında *geospatial search* gibi belirli indeksleme ve sorgulama yetenekleri, veri replikasyonunun sağlamlığı ( *data replication robustness* ) ve modern HTTP API’leri yer alır.

---

## ⚖️ Neden Her Zaman NoSQL Kullanılmıyor?

Bu faydaların tümüyle birlikte, neden herkesin NoSQL dışında başka bir şey kullandığını sorabilirsiniz. Günümüzde çoğu durum için bunun doğru olduğunu söyleyebilirsiniz; ancak yine de en iyi şekilde bir *RDBMS* ile karşılanan pek çok gereksinim kesinlikle vardır. Bunu kursta daha sonra ele alacağız.

---

## 📝 Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* NoSQL veritabanlarının ilişkisel olmayan ( *non-relational* ) yapıda olduğunu
* NoSQL veritabanlarının dört kategorisi bulunduğunu
* NoSQL veritabanlarının köklerinin açık kaynak topluluğuna dayandığını
* NoSQL veritabanı uygulamalarının teknik olarak birbirinden farklı olduğunu
* NoSQL veritabanlarını benimsemenin çeşitli faydaları olduğunu
