# ☁️ Cloud Native Uygulamalar

Basitçe söylemek gerekirse, *cloud native* (bulut yerel) uygulama; en baştan yalnızca bulut ortamında çalışacak şekilde geliştirilen bir uygulama ya da mevcut bir uygulamanın *cloud native* prensipleriyle yeniden düzenlenip (refactor) yeniden yapılandırıldığı (reconfigure) bir uygulamadır. Bir *cloud native* uygulama, bir uygulamayı bir bütün olarak oluşturmak üzere birlikte çalışan  *microservice* ’lerden oluşur; ancak her biri otomasyon ve orkestrasyon süreçleriyle bağımsız olarak ölçeklenebilir ve yinelemeli biçimde geliştirilebilir.

Bu  *microservice* ’ler çoğu zaman  *container* ’lar içinde paketlenir;  *container* ’lar, uygulama kodunun kütüphaneleri ve bağımlılıklarıyla birlikte paketlendiği, böylece her yerden çalıştırılabilen yürütülebilir yazılım birimleridir. Bu bağımsızlık, son kullanıcıların deneyimini aksatmadan *cloud native* uygulamaların sık ve yinelemeli (iterative) şekilde iyileştirilmesini sağlar.

*Cloud native* uygulamalar, kullanıcı arayüzünü, iş mantığı katmanını ( *business-logic layer* ) ve veri katmanını ( *data-layer* ) sıkı şekilde birbirine bağlayan, tek dev bir yazılım parçasından oluşan geleneksel ya da *monolithic* uygulamalardan farklıdır.

Bir *cloud native* uygulamanın bir seyahat sitesinde nasıl kullanılabileceğine dair örneği ele alalım. Sitenin kapsadığı her konu—uçuşlar, oteller, araçlar, kampanyalar—kendi başına bir  *microservice* ’tir.

Her  *microservice* , diğer  *microservice* ’lerden bağımsız olarak yeni özellikleri devreye alabilir. Kampanyalar ve indirimler de bağımsız şekilde ölçeklenebilir. Seyahat sitesi müşterilere bir bütün olarak sunulsa da, her *microservice* bağımsız kalır ve diğer servisleri etkilemeden gerektiğinde ölçeklenebilir veya güncellenebilir.

İster yeni bir *cloud native* uygulama oluşturuluyor olsun ister mevcut bir uygulama modernize ediliyor olsun, geliştiriciler tutarlı bir geliştirme prensipleri setine uyar: Uygulamaları tek işlevli  *microservice* ’lere bölerek *microservices* mimari yaklaşımını izlemek. Maksimum esneklik, ölçeklenebilirlik ve taşınabilirlik için  *container* ’lara dayanmak. Kullanıcı geri bildirimine dayalı hızlı, yinelemeli güncellemelerle oluşturma ve iyileştirme sürecini hızlandıran *Agile* yöntemleri benimsemek.

Bu videoda,  *cloud native* ’in temel kavramlarına, faydalarına ve kullanım senaryolarına daha yakından bakacağız.

---

## 🎙️ Andrea Crawford ile Cloud Native Uygulamalar

Merhaba. Ben Andrea Crawford ve IBM Cloud’dayım. Bugün *cloud native* uygulamalar hakkında konuşacağız.

Miras dünyasında, hantal ( *lumpy* ), *monolithic* uygulamalarımız var. Yeni dünyada ise bulutta yaşayan  *microservice* ’lerimiz var.

Bu diyagrama baktığımızda, bulut altyapısını görüyoruz. Bu; sizin  *private* , *public* ve *enterprise* altyapınızdır.

*Cloud native* uygulamalar, *hybrid* ve *multicloud* durumlarına uygulanır. Ayrıca zamanlama ( *scheduling* ) ve orkestrasyon ( *orchestration* ) katmanımız var. Bu katman,  *control plane* ’lerle ilgilidir; örneğin  *kubernetes(K8s)* .

Ayrıca uygulama ve veri servisleri katmanımız var. Bu katman, *backing services* ile ilgilidir ve uygulama kodumuzu diğer bulutlarda ya da hatta *on-premise* ortamda mevcut olabilecek mevcut servislerle entegre edebilmemizi sağlar.

Uygulama çalışma zamanlarımız ( *application runtimes* ) var: bunlar geleneksel ya da konvansiyonel olarak *middleware* diye bilinen şeylerdir. Ve burada, işte, *cloud native* uygulamalarımızın olduğu yer var.

Bu, tam burada yukarıdaki tatlı nokta. Yani uygulama kodumuz aslında *cloud native* için, geleneksel,  *monolithic* , hantal uygulamalarda olacağından çok farklı şekilde tasarlanır, inşa edilir ve teslim edilir.

Şimdi *cloud native* uygulamaların neden şu faydaları gerçekten kullanabildiğinden biraz bahsedelim: inovasyonu mümkün kılmak, iş çevikliğini ( *business agility* ) sağlamak ve teknoloji perspektifinden en önemlisi, şu çözüm yığınının ( *solution stack* ) metalaştırılması ( *commoditization* ).

Zaman ilerledikçe ve teknolojiler olgunlaşıp ortaya çıktıkça, servislerin çoğu aslında bu yığının daha alt katmanlarına doğru yeniden düzenleniyor ( *refactored* ). Bu, çekirdek servislerin daha düşük bir ağırlık merkezine sahip olmaya başladığı anlamına gelir; bu da inovasyonu, işte burada bu seviyede serbest bırakır.

Peki, ne zaman bir *cloud native* uygulama inşa etmeliyiz? *Her şey* Bulutta yaşayan her şey, bir *cloud native* uygulama tasarımına ve yaklaşımına sahip olmalıdır.

Bu, uygulama kodumuzun şu tür şeylerle enstrümante edilmesi gerektiği anlamına gelir: standartlaştırılmış loglama ( *standardized logging* ), standartlaştırılmış olaylar ( *standardized events* ) ve bu loglama ile olayları, birden fazla *microservice* ve *cloud native* uygulamanın kullanabileceği standart bir kataloğa eşleyebilmek.

İsteyeceğimiz son şey, geliştirme ekiplerimizin ( *development squads* ) log ve olay mesajlarının ne olması gerektiğini kendilerinin çözmek zorunda kalmasıdır. Bunu standartlaştıralım; çünkü bunu da metalaştırabilmek istiyoruz.

Ayrıca *distributed tracing* gibi şeylere ihtiyacımız var. *Microservices* dünyasına geçtiğimizde, çok sayıda hareketli parça olur. Bu da sistemin çekirdeğine ait servislerden yararlanmamız gerektiği anlamına gelir; örneğin:  *load balancing* , *service discovery* ve  *routing* .

Bunlar, burada bu katmanda, *Istio* gibi şeylerle ve daha yeni projelerin ortaya çıkmasıyla, örneğin *Knative* ile metalaştırılan türden şeylerdir.

Ve böylece, *cloud native* uygulamaların faydalarını tanıyıp bunu özetleyecek olursak, biz tamamen kurumsal ölçekte ( *enterprise* ) ve ölçekli mühendislik ( *engineering at scale* ) odaklıyız.

Bir sonraki videoda  *DevOps* ’a bakacağız.
