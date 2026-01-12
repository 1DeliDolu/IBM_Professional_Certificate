# ⚙️ Serverless Computing

Serverless, ölçeklendirme, zamanlama, yamalama ve uygulama yığınlarını sağlama gibi yaygın altyapı yönetimi görevlerinin sorumluluğunu bulut sağlayıcılarına devreden; geliştiricilerin zaman ve emeklerini uygulamalarına veya süreçlerine özgü kod ve iş mantığına odaklamalarına olanak tanıyan bir bilişim yaklaşımıdır.

Serverless, sunucu olmadığı anlamına gelmez; yalnızca altta yatan fiziksel veya sanal sunucuların yönetiminin kullanıcılarından kaldırıldığı anlamına gelir. Serverless bilişim ortamı, uygulamalar için gerektiği kadar kaynak tahsis eder.

## 🧩 Serverless’i Diğer Modellerden Ayıran Temel Özellikler

Serverless modeli, geliştiricinin sunucu sağlamasını, uygulama yığınlarını ve yazılımı kurmasını veya altyapıyı işletmesini gerektirmez.

Serverless bilişim, kodu yalnızca talep üzerine, istek başına çalıştırır; sunulan istek sayısıyla şeffaf biçimde ölçeklenir.

Serverless, son kullanıcıların yalnızca kullanılan kaynaklar için ödeme yapmasını sağlar; boşta kapasite için asla ödeme yapılmaz. Bu durum, bulutta sanal sunuculardan farklıdır; sanal sunucularda son kullanıcılar, V’ler çalıştığı sürece (boşta olsalar bile) ödeme yapar.

## 🧠 Çalışma Mantığı

Etkili biçimde serverless, altyapıyı geliştiricilerden soyutlar; kod, tekil fonksiyonlar olarak yürütülür ve her fonksiyon, *durumsuz (stateless)* bir konteyner içinde çalışır.

Bir isteğe hizmet etmek için önceden bir yürütme bağlamı gerekmez ve her yeni istekle birlikte fonksiyonun yeni bir örneği çağrılır.

## 🧪 Örnek Senaryo

Örneğin, web sitenizin ön ucu ile depolama katmanınız arasında, tekil fonksiyonlar çalıştıran bir serverless platformunuz olabilir; serverless uygulama, metin dosyalarını çeviriyor ve bunları bulut tabanlı bir depolama hizmetinde saklıyor olabilir.

Web sitenizin ön yüzünü kullanarak serverless uygulamaya metin dosyaları gönderirsiniz. Uygulama, farklı dillerde çeviriler üretir ve ardından bu çevrilmiş dosyaları bir Bulut Depolama’ya kaydeder ve bağlantılarını size geri gönderir.

## 🛠️ Günümüzde Bazı Önemli Serverless Hizmetleri

Günümüzdeki bazı temel serverless bilişim hizmetleri şunlardır:

* IBM Cloud Functions (Apache OpenWhisk tabanlı)
* AWS Lambda
* Microsoft Azure Functions

Serverless’in tüm uygulamalar veya senaryolar için en iyi uyum olmayabileceğini belirtmek önemlidir.

## 🧷 Serverless İçin Uygun Uygulama Özellikleri

Uygulama özelliklerini değerlendirmeniz ve uygulamanın serverless mimari kalıplarıyla uyumlu olduğundan emin olmanız gerekir.

Serverless mimarisi için uygun uygulamalar, aşağıdaki özelliklerden bazılarına sahip olabilir:

* kısa süre çalışan *durumsuz (stateless)* fonksiyonlar (saniyeler veya dakikalar)
* yoğun olmayan ve yoğun dönemleri değişken olan mevsimsel iş yükleri
* çok fazla boşta zaman gösteren üretimsel hacimsel veriler
* olay tabanlı işleme veya kullanım senaryolarını uygulamak için eşzamansız istek işleme
* *durumsuz (stateless)* fonksiyonlar olarak inşa edilebilecek mikroservisler

## 📌 Uygun Kullanım Alanları

Serverless mimarileri; veri ve olay işleme, IoT, mikroservisler ve mobil arka uçlar etrafındaki kullanım senaryoları için çok uygundur.

Doğasında bulunan ve otomatik ölçeklenmesi, hızlı sağlama ve boşta zaman için değişmeyen bir fiyatlandırma modeli nedeniyle, mikroservis mimarisini desteklemek günümüzde serverless bilişimin en yaygın kullanım alanlarından biri hâline gelmiştir.

Serverless; veri zenginleştirme, dönüştürme, doğrulama ve temizleme gibi görevler etrafında yapılandırılmış metin, ses, görüntü ve video verileriyle çalışmak için çok uygundur; PDF işleme, ses normalizasyonu, küçük resim (thumbnail) üretimi ve video dönüştürme (transcoding) gibi.

Veri arama ve işleme ile genom işleme gibi paralel görevler de serverless çalışma zamanında çalıştırılmaya çok uygundur.

Serverless ayrıca; iş verisi akışları, IoT sensör verileri, günlük (log) verileri ve finansal piyasa verileri dâhil olmak üzere her tür veri akışı alımıyla çalışmak için de uygundur.

## ⚠️ Dikkate Değer Zorluklar

Son olarak, serverless hakkında dikkate değer bazı zorluklara bakalım.

Serverless iş yükleri, iş yüküne yanıt olarak yukarı ve aşağı ölçeklenecek şekilde tasarlanır. Ancak uzun süren süreçlerle karakterize edilen iş yükleri için geleneksel bir sunucu ortamını yönetmek daha basit ve daha maliyet etkin olabilir.

Serverless uygulama mimarisi sağlayıcıya bağımlı olabilir; bu nedenle özellikle kimlik doğrulama, ölçekleme, izleme veya yapılandırma yönetimi gibi platform yeteneklerini içeren konularda *sağlayıcıya kilitlenme (vendor lock-in)* potansiyeli vardır.

Serverless mimariler iş yüküne yanıt olarak yukarı ve aşağı ölçeklendiğinden, bazen yeni bir isteğe hizmet etmek için sıfırdan başlatılmaları gerekebilir. Bazı uygulamalar için bu gecikme fazla etkili değildir; ancak düşük gecikmeli bir finansal uygulama gibi bir şey için bu gecikme kabul edilemez.
