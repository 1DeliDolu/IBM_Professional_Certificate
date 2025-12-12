# 🎛️ Prometheus’a Giriş

Prometheus’a Giriş’e hoş geldiniz! Bu videoyu izledikten sonra şunları yapabileceksiniz: Prometheus’un ne için kullanıldığını açıklamak, Prometheus mimarisini ve nasıl çalıştığını açıklamak ve Prometheus’un faydalarını ve özelliklerini özetlemek.

## 🧩 Prometheus Nedir?

Prometheus, SoundCloud adlı bir şirket tarafından geliştirilmiş açık kaynaklı bir izleme ( *monitoring* ) ve uyarı ( *alerting* ) çözümüdür. Prometheus ile sunucularınızı, sanal makinelerinizi ( *VMs* ) ve veritabanlarınızı izlemek için kullanabilirsiniz. Prometheus; sistem sağlığını, uygulama davranışını ve tahmini ( *prediction* ) ile performansı analiz eder, izler ve raporlar. Ayrıca sağlam bir veri modeli ve sorgu dili kullanarak ayrıntılı, uygulanabilir metrikler sağlar.

## 🏥 Güvenilir Tanılama ve İzleme

Prometheus güvenilir, başvurulan bir sistemdir; böylece bir kesinti sırasında veya uygulamaların düzenli izlenmesinde sorunları hızlıca teşhis edebilirsiniz.

## 🏗️ Prometheus Mimarisi ve Nasıl Çalışır?

Yapılandırıldıktan sonra Prometheus şu şekilde çalışır:

* Altyapınızda çalışan servisleri  **otomatik olarak keşfeder** .
* Ya da metriklerin çekilmesini ( *pulled* ) istediğiniz servisleri  **manuel olarak tanımlayabilirsiniz** .

Prometheus, HTTP/HTTPS uç noktalarından istekler göndererek metrikleri HTTP uç noktaları üzerinden düz metin formatında açığa çıkarır. Ardından, tanımlı aralıklarla uygulamalarınızdan ve ana makinelerinizden ( *hosts* ) gerçek zamanlı metrikleri, benzersiz tanımlayıcıları ve zaman damgalarını ( *timestamps* ) *scrape* eder (yani *pull* eder). Sonra Prometheus toplanan verileri zaman serisi veritabanında düzenler, sıkıştırır ve depolar.

Daha sonra verileri Prometheus Sorgu Dili ( *PromQL* ) ile panoda ( *dashboard* ) görüntüleyebilir ve e-posta veya diğer bildirim yöntemleriyle Alertmanager’a uyarı göndermek için kullanabilirsiniz.

## 🧪 Enstrümantasyon ve İstemci Kütüphaneleri

Metrikler uygulamalardan otomatik olarak ortaya çıkmadığı için geliştiricilerin onları üreten enstrümantasyonu ( *instrumentation* ) eklemesi gerekir. Uygulama enstrümantasyonu istemci kütüphaneleri ( *client libraries* ) gerektirir.

Ya da iki ya da üç satır kod ile bir metrik tanımlayabilir ve enstrümantasyonunuzu kontrol ettiğiniz kaynak kodunun içine ekleyebilirsiniz. Bu yönteme **doğrudan enstrümantasyon ( *direct instrumentation* )** denir.

Ayrıca istemci kütüphanelerini kullanarak da enstrümantasyon yapabilirsiniz. İstemci kütüphanelerinde Prometheus; Go, Python ve Ruby için resmi kütüphaneler ve C+, .Net, Node.js ve Haskell, Erlang, Rust, Java ve Scala gibi diğerlerini destekleyen üçüncü taraf kütüphaneler içerir.

## 🔌 Exporter ile Metrik Alma

Bir uygulamadan metrik elde etmenin başka bir yolu da bir **exporter** üzerinden olur. Exporter, metrik almak istediğiniz uygulamanın yanına dağıttığınız ( *deploy* ) bir yazılım parçasıdır. Bir exporter’ı, bir uygulamanın metrik arayüzü ile Prometheus’un *exposition* (veya metin) formatı arasında veri dönüştüren bire bir bir proxy olarak düşünün.

Prometheus’tan gelen istekleri alır. Uygulamadan metrikleri toplar ve sonra bu veriyi doğru Prometheus formatına dönüştürür. Son olarak veriyi Prometheus sunucusuna bir yanıt ( *response* ) ile geri döndürür.

Prometheus sunucuları otonomdur ve dağıtık veya ağ üzerinden depolamaya ya da diğer uzak servislere dayanmaz.

## ☁️ Dağıtım ve Veri Depolama

Bulutta veya şirket içinde ( *on-premises* ) dağıtılabilirler. Prometheus, kurumsal uygulamaların kalıcılık katmanından ( *persistence layer* ) metrikleri *scrape* eder. Kalıcılık katmanı, uygulamanızın iş fonksiyonları ile ilişkisel bir veritabanında sakladığı veriler arasında bir aracı ( *intermediary* ) olarak hareket eder.

Bazı Prometheus uygulamaları, veriyi Prometheus sunucusunun kendisine dayanmak yerine Prometheus verisini depolamak için adanmış bir zaman serisi veritabanı ( *time-series database* ) kullanabilir. Prometheus, izleme verilerinin artımlı yedeklerini ( *incremental backups* ) almayı basitleştiren bir zaman serisi veritabanı kullanır.

Prometheus bazı servislere yerel destek sağlar; bu, izleme ajanlarının ( *monitoring agents* ) gerekmediği anlamına gelir. Birkaç örnek: Kubernetes, etcd, SkyDNS ve diğer veritabanı yönetim sistemleri ve uygulama sistemleri.

## 🚨 Alertmanager ve Uyarı Yönetimi

Alertmanager, Prometheus ile birleştirilebilen esnek bir metrik toplama ve uyarı aracıdır. Bir uyarı koşulu algılandığında, Prometheus sunucusu uyarıyı üretir ve Alertmanager’a gönderir. Alertmanager bu uyarıları işler ve e-posta, nöbet ( *on-call* ) bildirim sistemleri ve sohbet platformları kullanarak uyarı bildirimlerini gönderir.

## 📈 Ne Zaman Prometheus Kullanmalısınız?

Birincil hedeflerinizden biri metrikleri toplamak ve değerlendirmekse, özellikle yalnızca sayısal zaman serisi verilerini ( *purely numeric time-series data* ) kaydetmek için Prometheus kullanmaktan fayda sağlarsınız.

Prometheus çok boyutlu veri toplama ve sorgulama sağlar. Ayrıca hem makine merkezli izleme ( *machine-centric monitoring* ) hem de son derece dinamik servis odaklı mimarilerin izlenmesi için iyi bir uyum sağlar. Doğru ayarlanmış ve dağıtılmış bir Prometheus kümesi saniyede milyonlarca metriği toplayabilir; bu da onu karmaşık iş yükleri için çok uygun hale getirir.

Prometheus genellikle Grafana ile birlikte kullanılır.

## 🧾 Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* Prometheus, yerelde veya bulutta dağıtılan açık kaynaklı ve ücretli sürümler sunan güçlü bir analitik araçtır.
* Enstrümantasyon, istemci kütüphaneleri ve exporter’lar veri kaynaklarından metrik yakalamak için kullanılır.
* Prometheus, Prometheus verisini depolamak için adanmış bir zaman serisi veritabanı kullanabilir.
* Sayısal zaman serisi verisini toplar ve değerlendirir ve tipik olarak Grafana ile kullanılır.
