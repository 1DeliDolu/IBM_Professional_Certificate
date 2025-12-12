# 🧭 Tracing for Container-Based Applications

Tracing for Container-Based Applications’a hoş geldiniz. Bu videoyu izledikten sonra, container uygulamaları için iz sürmenin neden gerekli olduğunu açıklayabilecek, container tabanlı uygulamalar için iz sürmeyi uygulama adımlarını listeleyebilecek ve uygulama geliştirmede iz sürmeyi uygulamaya yönelik en iyi uygulamaları tartışabileceksiniz.

Container tabanlı uygulamalarla çalıştığınızda, bazen mikro servis uygulamanızın performansını optimize etmeniz gerekir. Ancak container’lar ve servisler arasındaki sofistike etkileşimleri anlamak zordur. Bu durum, darboğazları belirleme ve verimliliği artırma kapasitenizi engelleyebilir. İşte bu noktada iz sürme (tracing) yardımınıza koşabilir. Uygulamanızdaki bir isteğin, çeşitli container’lar ve servislerden geçerken ilerleyişini takip etmenizi sağlar.

Trace’ler, tüm işlem yolunun eksiksiz bir resmini sunar; bağımlılıkları incelemenize, gecikme (latency) problemlerini bulmanıza ve performans darboğazlarını tespit etmenize olanak tanır.

## 🧩 Neden Container Uygulamaları İçin Tracing Gerekli?

Peki container uygulamaları için iz sürme neden gereklidir? Container tabanlı uygulamalar için iz sürme, isteklerin farklı uygulama bileşenleri arasındaki akışını yakalamayı ve analiz etmeyi içerir. Tracing, container’laştırılmış bir ortamda mikro servis mimarisinin dağıtık doğası nedeniyle daha da büyük bir önem kazanır. Bir geliştirici olarak, istekleri birden fazla container ve servis üzerinden izleyerek hangi bileşenin gecikmeye veya hatalara neden olduğunu hızlıca belirleyebilir ve sorunları daha verimli şekilde çözebilirsiniz.

İsteklerin akışını yakalamak ve analiz etmek için  *OpenTracing* , *Zipkin* veya *Jaeger* gibi iz sürme araçlarını kullanabilirsiniz. Bu araçlar, uygulamada bir isteğin alındığı an veya harici bir servisle etkileşime girdiği an gibi kritik noktalarda trace verisi üretmek üzere kodunuzu enstrümante etmenize olanak tanır.

Ardından, uygulamanın performansı ve davranışı hakkında içgörü elde etmek için trace verisini toplayıp analiz edebilirsiniz.

## 🛠️ Container Tabanlı Uygulamalarda Tracing Uygulama Adımları

Container tabanlı bir uygulamayı izlemek çeşitli yöntemlerle gerçekleştirilebilir. Container tabanlı uygulamalar için iz sürmeyi uygulamak üzere izlenmesi gereken beş adım vardır.

İlk olarak, uygulama yığınınız (stack) ve *Kubernetes* gibi container orkestratörünüzle çalışabilen bir iz sürme aracı seçmelisiniz.

Sonra, trace’ler üretmek için kodunuzu enstrümante edeceksiniz. Enstrümantasyonun kesin yöntemi, uygulamanızda kullanılan dil ve framework’e bağlı olacaktır.

Ardından, seçilen iz sürme aracı için izleme ajanını (tracing agent) uygulamanızdan trace’leri alacak şekilde yapılandıracaksınız.

Araca bağlı olarak ortam değişkenleri (environment variables) ayarlamanız veya yapılandırma dosyalarını değiştirmeniz gerekebilir.

Şimdi, izleyiciyi (tracer) container’laştırılmış uygulamanızla birlikte dağıtacaksınız. Çalıştığından ve trace’leri alabildiğinden emin olmalısınız.

Son olarak, işlevselliği doğrulayacaksınız. Bu aşamada, logları inceleyerek veya seçilen aracın sağladığı panoları (dashboards) kullanarak trace verisinin üretildiğini ve tracer’a gönderildiğini doğrularsınız.

## 🌐 Distributed Tracing Nasıl Çalışır?

Dağıtık iz sürme (distributed tracing), uygulama isteklerinin akışını ön uç (front-end) bileşenlerden veya cihazlardan arka uç (back-end) servislerine, veritabanlarına ve diğer üçüncü taraf servislere kadar izler. Nasıl çalıştığını anlamak için dağıtık iz sürmeyi, kök veya ebeveyn (parent) span’a sahip, dallanarak çocuk span’lara uzanan ağaç benzeri bir yapı olarak düşünebilirsiniz.

İzleme, son kullanıcı uygulamayla etkileşime geçer geçmez başlar. Bir HTTP isteği gibi ilk istek gönderildiğinde ona özel bir *trace ID* verilir; bu belirli isteğin izlediği tüm yol, o trace içinde ayrıntılandırılır.

Sistem boyunca istek işlenirken operasyonlar veya span’lar bu ilk *trace ID* ile işaretlenir. Ayrıca kendisine özel bir ID de alır; mevcut isteğe ilk neden olan operasyon, yani *parent span* olarak da adlandırılan span’ın da kendine ait bir ID’si olur.

Bu span’ların her biri, isteğin yolculuğundaki belirli bir adımı temsil eder ve etiketler (tags), sorgular (queries), ayrıntılı stack trace’ler, loglar ve bağlam veren olaylar (context giving events) gibi kritik verilerle kodlanır. Bu, dağıtık bir sistem boyunca bir trace ilerlerken yol üzerinde gereken her ek operasyon için platformun çocuk span’lar oluşturacağı anlamına gelir.

Monitoring araçlarını kullanarak verileri daha iyi görselleştirebilir ve uçtan uca istekleri izleyebilirsiniz. Birden fazla adım söz konusudur; bunlara enstrümantasyon, trace bağlamı (trace context), metrikler ve metadata ile analiz ve görselleştirme dahildir.

## ✅ Uygulama Geliştirmede Tracing için En İyi Uygulamalar

Uygulama geliştirmede iz sürmeyi uygulamaya yönelik en iyi uygulamaların da farkında olmalısınız.

Enstrümantasyon servislerini benzersiz bir ID ile kullanmalısınız. Burada, her dış isteğe (external request) benzersiz bir dış istek ID’si atanır. Atanan dış istek ID’si, isteği işleyen tüm ilgili servislere iletilir. Ardından dış istek ID’si tüm log mesajlarına dahil edilir.

Son olarak, merkezi bir serviste dış istekleri işlerken, istekle ilgili başlangıç ve bitiş zamanları ile gerçekleştirilen operasyonlar gibi bilgiler kaydedilir.

Sisteminizde optimum performans ve güvenilirliği sağlamak için, uçtan uca enstrümantasyon uygulamanız ve tüm gelen (inbound) ve giden (outbound) servis çağrılarının trace’lerini kaydetmeniz önerilir. Bu, gecikme (latency), trafik (traffic), hatalar (errors) ve sistemin doygunluğu (saturation) veya kullanım oranı (utilization) gibi *Site Reliability Engineering (SRE)* golden signal’larını, ayrıca *RED* yani response, error ve duration metriklerini izlemenize olanak tanır.

Bu metriklere dayalı alarmlar kurarken aynı zamanda bazı trace’leri de kaydetmek, kullanıcılarınız etkilenmeden önce sorunları hızlıca tespit etmenizi ve çözmenizi sağlar.

Süre (duration) metriklerine dikkat etmek, sistem davranışını etkili biçimde ölçmek için kritik önemdedir. Bu, farklı bileşenlerin çeşitli senaryolarda nasıl çalıştığına dair önemli bilgiler verecektir.

Araçlarınızı seçerken uluslararası standartlarla uyumluluğu sağlamak için  *OpenTelemetry* , *OpenTracing* ve *OpenCensus* standardizasyonunu takip etmeniz önerilir.

Kullanılan özelleştirilmiş iş metrikleri ve tracing span’ları, gelecekteki optimizasyon ve sorun giderme çalışmalarına yardımcı olması için dokümante edilmelidir. Gelecek geliştirme döngüleri veya bakım girişimleri bu dokümantasyonu bir referans noktası olarak kullanabilir.

## 🧾 Video Özeti

Bu videoda, birden fazla container ve servis üzerinden istekleri izleyerek gecikmeye veya hatalara neden olan bileşeni hızlıca belirleyebileceğinizi ve sorunları daha verimli çözebileceğinizi öğrendiniz.

Container’laştırılmış uygulamalar için iz sürmeyi uygulamak üzere izlenmesi gereken beş adım vardır: bir iz sürme aracı seçmek, kodunuzu enstrümante etmek, izleme ajanını yapılandırmak, tracer’ı dağıtmak ve işlevselliği doğrulamak.

Platform, dağıtık bir sistem boyunca bir trace ilerlerken yol boyunca gereken her ek operasyon için çocuk span’lar oluşturur.

Sisteminizin optimum performansı ve güvenilirliği için uçtan uca enstrümantasyon uygulayın ve tüm gelen ve giden servis çağrıları için trace’leri kaydedin.
