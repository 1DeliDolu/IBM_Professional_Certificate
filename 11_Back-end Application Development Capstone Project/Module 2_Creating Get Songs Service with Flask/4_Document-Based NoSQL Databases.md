# 📄 Doküman Tabanlı NoSQL Veritabanları

“Doküman Tabanlı NoSQL Veritabanları”na hoş geldiniz. Bu video, doküman tabanlı NoSQL veritabanı kategorisini; mimarisini ve temel kullanım senaryolarını da kapsayacak şekilde açıklar.

Doküman veritabanları, *Key-Value* modelinin üzerine inşa edilir; değeri ( *value* ) görünür hale getirir ve sorgulanabilir kılar. Her bir veri parçası bir doküman ( *document* ) olarak kabul edilir ve tipik olarak **JSON** veya **XML** formatında saklanır.

Doküman veritabanlarının faydalarından biri, her dokümanın gerçekten esnek bir şema ( *flexible schema* ) sunmasıdır; yani iki dokümanın aynı olması veya aynı bilgileri içermesi gerekmez.

Doküman veritabanları genellikle dokümanların içeriğini indeksleme ve sorgulama yeteneği sunar; anahtar ve değer aralığı ( *key and value range* ) aramaları ve arama kabiliyeti sağlar ya da *MapReduce* gibi paradigmalar aracılığıyla analitik sorgulara imkan tanıyabilir.

Doküman veritabanları yatay olarak ölçeklenebilir ( *horizontally scalable* ) ve birden fazla node üzerinde  *sharding* ’e izin verir; tipik olarak dokümandaki bazı benzersiz anahtar ( *unique key* ) ile shard edilir. Doküman depoları ayrıca genellikle yalnızca tek doküman operasyonlarında atomik işlemleri ( *atomic transactions* ) garanti eder.

---

## 🧩 Doküman Tipi NoSQL Veritabanları İçin Kullanım Senaryoları

Doküman tipi bir NoSQL veritabanı için bazı kullanım senaryoları nelerdir?

İlk örnek, bir uygulama veya süreç için olay kaydı ( *event logging* ) olacaktır. Her bir örnek yeni bir doküman veya aggregate oluşturur ve olaya karşılık gelen tüm bilgileri içerir.

Bir diğer kullanım senaryosu çevrimiçi blog yazarlığıdır. Her kullanıcı bir doküman olarak temsil edilir; her gönderi bir dokümandır; ve her yorum, beğeni veya aksiyon bir doküman olur. Tüm dokümanlar, veri türüne ilişkin bilgileri içerir; örneğin kullanıcı adı ( *username* ), gönderi içeriği ( *post content* ) veya dokümanın oluşturulduğu zaman damgası ( *timestamp* ).

Daha genel olarak doküman depoları, web ve mobil uygulamalar için operasyonel veri kümeleri ( *operational datasets* ) ile iyi çalışır. İnternet düşünülerek tasarlanmışlardır –  **JSON** , **RESTful API** ve yapılandırılmamış veri ( *unstructured data* ) odaklı.

---

## ⚠️ Ne Zaman Uygun Değildir?

Doküman tipi NoSQL veritabanları, **ACID** işlemleri ( *ACID transactions* ) gerektiren kullanım senaryoları için uygun değildir. Bir doküman deposunun, birden fazla doküman üzerinde çalışan bir işlemi ( *transaction* ) ele alması mümkün değildir ve bu durumda ilişkisel bir veritabanı daha iyi bir seçim olabilir.

İkinci olarak, verinizi aggregate odaklı bir tasarıma zorladığınızı fark ediyorsanız, doküman veritabanları doğru seçim olmayabilir. Veri doğal olarak normalize/tablosal ( *normalized/tabular* ) bir modele oturuyorsa, bu da ilişkisel veritabanlarını araştırmanız gereken bir başka durumdur.

---

## 🗂️ Popüler Doküman NoSQL Veritabanı Örnekleri

Doküman veritabanları günümüzde kullanımda olan NoSQL veritabanı kategorileri arasında şu anda en yaygın olanıdır. Daha popüler doküman NoSQL veritabanı uygulamalarından bazıları şunlardır:

* IBM Cloudant
* MongoDB
* Apache CouchDB
* Terrastore
* OrientDB
* Couchbase
* RavenDB

---

## 📝 Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* Doküman tabanlı NoSQL veritabanlarının, değerleri görünür ve sorgulanabilir yapmak için dokümanları kullandığını.
* Her bir veri parçasının bir doküman olarak kabul edildiğini ve genellikle **JSON** veya **XML** formatında saklandığını.
* Her dokümanın esnek bir şema sunduğunu.
* Doküman tabanlı NoSQL veritabanlarının temel kullanım senaryolarının; uygulamalar ve süreçler için olay kaydı ( *event logging* ), çevrimiçi blog yazarlığı ve web/mobil uygulamalar için operasyonel veri kümeleri veya metadata olduğunu.
