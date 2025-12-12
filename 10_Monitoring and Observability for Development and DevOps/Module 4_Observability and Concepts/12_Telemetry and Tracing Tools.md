# 📡 Telemetri ve İzleme Araçları

Telemetry and Tracing Tools’a hoş geldiniz. Bu videoyu izledikten sonra, dağıtık izleme ile telemetri arasındaki farkı ayırt edebilecek ve popüler telemetri ile dağıtık izleme araçlarını listeleyebileceksiniz. Web servisleri, mobil uygulamalar, Cloud platformları veya IoT cihazları olsun, günümüzün dijital ekosistemi daha bağımlı ve daha birbirine bağlı hale gelmiştir. Bu tür bir karmaşıklık, sistem performansınızın verimli şekilde izlenmesi ve analiz edilmesi için kritik bir ihtiyaç doğurur. Telemetri ve izleme araçları böyle bir senaryoda yardımınıza koşar. Telemetri ve dağıtık izleme, yazılım mühendisliğinde, özellikle dağıtık sistemlerin geliştirilmesinde kullanılan, birbiriyle ilişkili kavramlardır. İki terim arasındaki farkı anlayalım.

## 🔍 Dağıtık İzleme ve Telemetri Arasındaki Fark

Dağıtık izleme, dağıtık Cloud ortamlarında iletilen istekleri gözlemleme tekniğidir. Diğer yandan telemetri, izleme ve analizi desteklemek için uzak veya erişilemeyen kaynaklardan verilerin otomatik olarak toplanması ve iletilmesi sürecidir.

Dağıtık izlemede, *correlation ID* adı verilen benzersiz tanımlayıcılar her isteğe kaynağında eklenir ve ardından sistem içindeki çeşitli servisler boyunca yayılır. Buna karşılık telemetri, sistem performans metrikleri ve kullanıcı davranışı gibi geniş bir veri yelpazesini içerir; örneğin tıklamalar, sayfa görüntülemeleri veya hata oranları.

Dağıtık izleme ile geliştiriciler, bir isteğin yolunu gerçek zamanlı olarak birden fazla düğüm ve servis üzerinden takip edebilir. Öte yandan telemetri, uygulama performansını artırabilir, sorunları kritik hale gelmeden önce belirleyebilir ve kullanıcıların sistemle nasıl etkileşim kurduğunu anlamaya yardımcı olabilir.

## 🧰 Popüler Telemetri Araçları

Şimdi bazı popüler telemetri araçlarını inceleyelim.

Datadog, öncelikle altyapı ve güvenlik izleme özellikleriyle bilinir. Ancak, uçtan uca tek bir platforma entegre edilmiş tüm bir gözlemlenebilirlik araçları paketini sunar. Datadog, uygulama performansınızı izlemenizi, gerçek kullanıcılardan veri toplamanızı, logları yönetmenizi ve olayları bildirmeyi ve çözmeyi mümkün kılar.

Bir sonraki araç Dynatrace, log yönetimi, altyapı izleme ve uygulama performans izleme ( *APM* ) dahil olmak üzere uçtan uca bir gözlemlenebilirlik platformudur ve kapsamlı bir gözlemlenebilirlik araç seti sağlar. Bu aracın uygulama izleme özelliği, Cloud uygulamalarının performansını ve güvenliğini izlemenizi sağladığı için mevcut en iyi seçeneklerden biridir.

Bir diğer popüler araç New Relic, loglama, altyapı izleme, uygulama performans izleme ( *APM* ), gerçek kullanıcı izleme ( *RUM* ) ve güvenlik izleme dahil 16 ana araca bölünmüş bir araç setine sahip bir gözlemlenebilirlik platformudur. En bilinen platformlardan biridir; özellikle üst düzey *APM* özelliklerinin gözlemlenebilirlik yığınına iyi entegre olması ve nispeten kolay bakımı nedeniyle övülür.

Sumo Logic, karmaşık Cloud mimarilerini gözlemlenebilir ve güvenli hale getirmede kilit rol oynayan analitik bir platformdur. Modern Cloud altyapıları ile uygulama gözlemlenebilirliği ve izleme için birkaç özellik açısından zengin ürün sağlar. Bununla da kalmaz. Sumo Logic ayrıca tüm bir güvenlik izleme ve yönetim paketi de sunar.

Bir diğer önerilen ve popüler araç Instana’dır; bu, Cloud tabanlı bir *APM* çözümüdür. Instana, mikroservis tabanlı uygulamaların performansı ve sağlığı hakkında gerçek zamanlı görünürlük sunar. Bu araç, servisler, konteynerler, hostlar ve altyapı dahil uygulamanızın tüm bileşenlerini otomatik olarak tanımlamak ve izlemek için gelişmiş telemetri teknolojisini kullanır.

Instana ile performans darboğazlarını kolayca keşfedebilir ve kullanıcılarınızı etkilemeden önce olası sorunları hızlıca giderebilirsiniz.

## 🧵 Popüler Dağıtık İzleme Araçları

Şimdi geliştiricilerin uygulamalarını izlemek, sorun gidermek ve optimize etmek için kullanabileceği bazı popüler dağıtık izleme araçlarına bakalım.

İlki Atatus’tur; dağıtık bir sistemde isteklerin nasıl aktığına dair ayrıntılı içgörüler sağlar. Bir isteğin istemciden sunucuya ve sunucudan sunucuya yolculuğunu izleyerek geliştiriciler, yol boyunca darboğazları ve performans sorunlarını belirleyebilir. Atatus, gerçek zamanlı veri görselleştirme ve analitik sunar; geliştiricilerin kullanıcı deneyimini etkileyebilecek sorunları hızlıca çözmesini sağlar.

Jaeger, Uber Technologies tarafından dağıtık sistemlerde mikroservisleri izlemek için geliştirilmiş bir dağıtık izleme teknolojisidir. Jaeger’in mikroservisler arasındaki istek akışına görünürlük sağlaması, geliştiricilerin uygulamalarının performansını ve davranışını analiz etmelerine olanak tanır.

Darboğazları ve problemleri bulmaya yardımcı olmak için, birden fazla servisten zamanlama verilerini ve logları toplar ve bunları tek bir görünümde sunar.

Bir diğer iyi bilinen dağıtık izleme aracı Zipkin’dir; dağıtık sistemlerde mikroservislerin nasıl etkileşime girdiğine dair bilgileri toplar. Zipkin ile isteklerin servisler arasında nasıl hareket ettiğini ve her isteğin gecikme ( *latency* ) ve yanıt süreleri açısından nasıl performans gösterdiğini görebilirsiniz.

Bir sonraki popüler dağıtık izleme aracı Dynatrace’tir; gözlemlenebilirlik, otomasyon, yapay zekâ ve uygulama güvenliği için hepsi bir arada bir platformdur. Bir ajan kurmak, ortamınızda gerçekleşen her şeyi otomatik olarak algılar ve dağıtımı kolaylaştırır. Dynatrace, uygulama ortamınızda olan biten her şeyin eksiksiz bir resmini sunar.

## ✅ Video Özeti

Bu videoda, dağıtık izlemenin dağıtık Cloud ortamlarında iletilen istekleri gözlemleme tekniği olduğunu öğrendiniz.

Öte yandan telemetri, izleme ve analizi desteklemek için herhangi bir uzak veya erişilemeyen kaynaktan verilerin otomatik olarak toplanması ve iletilmesi sürecini ifade eder.

Bazı popüler telemetri araçları Datadog, Dynatrace, New Relic, Sumo Logic ve Instana’dır. Bazı popüler dağıtık izleme araçları ise Atatus, Jaeger, Zipkin ve Dynatrace’tir.
