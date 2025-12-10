# 🕸️ Service Mesh ve Istio

## 🎯 Öğrenme Hedefleri

“Service Mesh ve Istio”ya hoş geldiniz.

Bu videoyu izledikten sonra şunları yapabiliyor olacaksınız:

* Mikroservislerin faydalarını sıralamak,
* Mikroservislerle birlikte gelen zorlukları açıklamak,
* Bir  *service mesh* 'in ne olduğunu açıklamak,
* Bir  *service mesh* 'in neden faydalı olduğunu açıklamak,
* Bir  *service mesh* 'in yaygın mikroservis zorluklarını nasıl hafifletebileceğini açıklamak.

---

## ✅ Mikroservislerin Faydaları

Bulut yerel uygulamalar ( *cloud-native applications* ) geliştirmek için bir mikroservis mimarisi kullanmak birçok fayda sağlar.

Mikroservislerle kodu güncellemek daha yönetilebilirdir — yalnızca ilgili servisleri güncellemeniz gerekir.

Mikroservislerle, farklı uygulama bileşenlerini geliştiren ekipler kendi özel ihtiyaçlarını karşılayan farklı teknoloji yığınlarını kullanmakta serbesttir.

Ayrıca, bir uygulama çalışırken daha fazla yük alan bileşenler bağımsız olarak ölçeklenebilir; böylece yalnızca tek bir bileşenin daha fazla kaynağa ihtiyaç duyduğu durumlarda tüm uygulamanın ölçeklenmesi gerekmez.

---

## ⚠️ Mikroservislerin Beraberinde Getirdiği Zorluklar

Mikroservis kullanımı bazı zorlukları da beraberinde getirir.

Mikroservislerin, iletişimi güvence altına almak ve şifrelemeyi kurmak için yapılandırılması gerekir.

Geliştirme ekipleri, yeni özellikleri kullanıcıların bir alt kümesine sunmak ya da yeni bir özelliğin iki sürümünü karşılaştırarak hangi sürümün kullanıcıları daha çok etkilediğini görmek isteyebilir.

Bu durumlarda ekiplerin  *canary deployments* 'a ve  *A/B testing* 'e ihtiyaçları vardır.

Mikroservisler arasındaki iletişim, bir servis erişilemez veya özellikle yavaş olduğunda zincirleme hatalar olasılığını da beraberinde getirir.

İletişim hatalarının birden çok mikroservise zincirleme şekilde yayılmasını önlemek için geliştiricilerin *retries* ve *circuit breaking* mekanizmalarını uygulaması gerekir.

---

## 🧩 Service Mesh’e Giriş

Şimdi  *service mesh* 'lerden bahsedelim.

Bir  *service mesh* , servisler arası iletişimi güvenli ve güvenilir hale getirmek için ayrılmış bir katmandır.

Diğer yeteneklerinin yanı sıra,  *service mesh* 'ler servisler arasındaki trafik akışını kontrol etmek için trafik yönetimi, servisler arasındaki trafiği şifrelemek için güvenlik ve uygulamaları sorun gidermek ve optimize etmek için servis davranışının gözlemlenebilirliğini sağlar.

*Service mesh* yetenekleri ve özellikle de Istio *service mesh* hakkında daha fazla bilgi edinmek için, şimdi IBM Cloud ekibinden Ram Vennam'i dinleyelim.

---

## 🧪 Örnek Uygulama ve Service Mesh Kullanım Nedenleri

Bu örnek uygulamayı kullanalım.

Kullanıcı arayüzü ( *UI* ) mikroservisim, *catalog* servisinin iki sürümüyle konuşuyor ve bunlar da *inventory* ile konuşuyor. Bunların hepsi bir *Kubernetes* kümesi içinde dağıtılmış servislerdir.

Birinin bir *service mesh* kullanmasının bir numaralı nedeni, iş yüklerini güvence altına almak istemeleridir. Bu nedenle, bir servis başka bir servisle konuşurken *mutual TLS* kullanılmasını isterler.

İkinci olarak, servislerin birbirine nasıl bağlandığını dinamik olarak yapılandırmak isterler.

Örneğin bu senaryoda birinci sürüm ve ikinci sürüm vardır. Dolayısıyla, testler ve artımlı yayınlar yaparken trafiğin yüzde 90'ını sürüm 1'e ve trafiğin yüzde 10'unu da sürüm 2'ye göndermek isteyebilirim.

Sistemimi daha sağlamlaştırmak için *retry policies* ve *circuit breaking* eklemeyi de denemek isteyebilirim.

Üçüncü olarak, uygulamamın uçtan uca nasıl çalıştığını gözlemlemek isterim; yalnızca bir servisin çalışıp çalışmadığını görmek değil, sistemdeki darboğazların nerede olduğunu ve trafiğin nasıl aktığını görmek isterim.

Ve dördüncü olarak, kimin neyle konuşma erişimine sahip olduğunu kontrol etmek isterim.

Bu örnekte  *UI* 'ın *catalog* ile konuşmasına izin verilir ve  *catalog* 'un *inventory* ile konuşmasına izin verilir, ancak  *UI* 'ın doğrudan *inventory* ile konuşmasına izin verilmez ve yetkisiz konteynerlerin *inventory* servisiyle konuşmasına izin verilmez.

Bundan daha da ayrıntılı hale gelip,  *UI* 'ın  *inventory* 'ye bir HTTP GET isteği yapmasına,  *catalog* 'un ise  *inventory* 'ye bir POST isteği yapmasına izin verildiğini söyleyebilirsiniz.

---

## ⚙️ Istio ve Proxy Mimarisi

Geçmişte, tüm bu özellikleri doğrudan uygulama kodlarının içine programlamaları için geliştiricilerimizi görevlendirirdik.

Bu durum, geliştirme döngüsünü yavaşlattı, bu mikroservisleri büyüttü ve genel olarak her şeyi daha az esnek hale getirdi; ancak artık daha iyi bir yol var ve bu da  *service mesh* 'tir.

Uygulamanızı küçük ve iş odaklı tutar, bunun yerine zekayı ağa dinamik olarak programlarsınız ve Istio'nun yaptığı tam olarak budur.

Dolayısıyla, Istio kurulu olduğunda olan ilk şey, her bir konteynerinizin yanına proxy'lerin otomatik olarak enjekte edilmesidir; bu proxy'ler  *envoy proxies* 'dir ve proxy'nin kendisi, uygulama konteynerinizin yanında bir konteyner içinde çalışır, ancak aynı Kubernetes pod'u içinde çalışır.

Artık *UI* *catalog* ile konuşmak istediğinde, proxy bu isteği gerçekten yakalar, ilgili tüm ilkeleri uygular ve trafiği diğer taraftaki proxy'ye yönlendirir; ardından *catalog* proxy'si bu isteği alır ve  *catalog* 'a iletir.

Istio, bu proxy'lerin her birini istediğiniz yapılandırmayla yapılandırır.

---

## 🧠 Istio Kontrol Düzlemi Bileşenleri

Istio, Kubernetes'i  *CRD* 'ler kullanarak genişletir.

Dolayısıyla, Istio yapılandırmasını uygulamak için YAML dosyanızı yazıp Kubernetes'e uygularsınız.

Istio'nun *galley* bileşeni bu YAML'ı alır, doğrular ve ardından Istio *pilot* bileşenine iletir.

 *Pilot* , bu yapılandırmayı *envoy* yapılandırmasına dönüştürür ve her bir proxy'ye dağıtır.

Proxy'lerin ek ilkeler ve kurallar uygulamasını istiyorsanız, bir *policy* bileşeni vardır.

Daha sonra bu proxy'ler, sisteminizde neler olup bittiğine ilişkin telemetri bilgisini sürekli olarak Istio *telemetry* bileşenine raporlar.

Ve son olarak, ama en az diğerleri kadar önemli olan *citadel* bileşeni vardır.

 *Citadel* , sisteminizdeki her bir servise güçlü bir kimlik sağlamaktan sorumludur.

Ayrıca sertifikalar üretir ve her bir proxy'ye dağıtır; böylece bu proxy'ler birbirleriyle konuşurken *mutual TLS* kullanılabilir.

---

## 🌐 Istio Kaynakları: Gateway, Virtual Service, Destination Rules

Istio ile çalışmaya başlamak ve Istio'yu yapılandırmak için öğrenmeniz gereken üç temel kaynak vardır.

İlk olarak bir *gateway* vardır.

 *Gateway* , ağınızın kenarında oturan ve gelen ve giden HTTP ve TCP bağlantılarını kabul eden bir yük dengeleyici gibidir.

Daha sonra, trafiği gateway'den servislerinize yönlendirmek için bir *virtual service* oluşturursunuz.

Bir  *virtual service* , bir gateway'e bağlanarak trafiği  *UI* 'a yönlendirebilir ya da bir servise bağlanarak trafiği diğer servislerinize yönlendirebilir; burada yüzde 90'a yüzde 10 trafik bölme gibi ilkeler uygulayabilirsiniz.

Trafik yönlendirildikten sonra, bu trafik üzerinde TLS ayarları veya *circuit breaking* gibi kurallar uygulayabilirsiniz ve bunlar *destination rules* kullanılarak yapılır.

İşte Istio hakkında bilmeniz gereken üç temel kaynak bunlardır.

---

## 🔁 Policy ve Telemetry Bileşenlerindeki Yeniden Düzenleme

Aslında, bu bileşenlerde bazı yeniden düzenlemeler ( *refactoring* ) yapıldığı için *policy* ve *telemetry* bileşenlerini yıldız içine alacağım.

Ek bir  *network hop* 'tan kaçınmak için mantık bu  *control plane* 'in dışına ve doğrudan proxy'lerin içine taşınmaktadır.

Bu da daha iyi performansa dönüşür.

---

## 📚 Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* Mikroservis mimarilerinin, servisler arasında güvenliğe ve servisleri yönetmek ve test etmek için yöntemlere ihtiyaç duyduğu,
* Bir  *service mesh* 'in, ortamdaki iletişimi koordine ederek güvenlik ve daha fazlasını sağlayan özel bir katman olduğu,
* Istio'nun, mikroservislerle birlikte dağıtıldığında  *traffic shifting* , *mutual transport layer security* ve *telemetry* sağladığı.
