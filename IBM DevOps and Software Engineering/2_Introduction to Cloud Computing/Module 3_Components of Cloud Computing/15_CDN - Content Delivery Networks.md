# 🌐 CDN - İçerik Dağıtım Ağları

Bir **içerik dağıtım ağı** ( *Content Delivery Network* ), ya da  **CDN** , kullanıcının **coğrafi konumuna** bağlı olarak web sitesi içeriğinin geçici olarak depolanmış ( *cached* ), yani **önbelleğe alınmış** kopyalarını kullanıcılara teslim eden  **dağıtık bir sunucu ağıdır** . Bir CDN bu içeriği dağıtık konumlarda saklar ve web sitenizin ziyaretçileri ile web sitesi sunucunuz arasındaki mesafeyi azaltır. Videonun geri kalanında, İçerik Dağıtım Ağları hakkında daha fazlasını öğreneceğiz.

Merhaba. Ben Ryan Sumner, IBM Cloud’da **Baş Ağ Mimarıyım** ve bugün şu soruyu yanıtlamanıza yardımcı olacağım: bir içerik dağıtım ağı nedir?

Kısacası, bir içerik dağıtım ağı ya da CDN, **internet içerik teslimatını hızlandıran** bir hizmettir. Başka bir deyişle, bir CDN’nin temel faydası web sitenizi **daha hızlı** hale getirmesidir.

## 🧭 Küresel Kullanıcılar ve Sınırlı Sunucu Konumları

Bunu nasıl başardığını ve diğer bazı faydalarını anlatmaya başlamadan önce, dünyanın her yerinde kullanıcılarımız varken ama dünyanın her yerinde sunucularımız olmadığında karşılaştığımız bazı zorluklardan ve bu dinamik nedeniyle bu kullanıcıların yaşadığı deneyimden bahsetmek istiyorum.

Burada Dallas’ta barındırılan bir sunucuyu gösteren basit bir diyagramım var. Bu benim web sitem. Sonra dünyanın her yerinde kullanıcılarım var. Yani Sidney’de beş tane olabilir. Londra’da beş tane var. New York’ta on tane olabilir. LA’de on tane olabilir. Dallas’taki sunucuma ve web siteme erişen dünyada toplam 30 kullanıcım var.

## ⏱️ Mesafe ve Gidiş-Dönüş Süresi

Bu kullanıcıların bir kısmını yolculuklarında takip edelim. Sidney’deki kullanıcılarımıza bakalım. Web sitesine bir istek yapıyorlar. Dallas’a **8.600 mil** gidişleri var ve sonra **8.600 mil** de geri dönüşleri var. Bunun aldığı süre genellikle **milisaniye** cinsinden ölçülür ve sadece bu gidiş-dönüş yaklaşık **170 milisaniye** olabilir.

Londra’daki kullanıcılarımız için bu yaklaşık **100 milisaniye** olabilir. New York City’deki kullanıcılarımız muhtemelen yaklaşık **40 milisaniyelik** bir gidiş-dönüş süresi deneyimler. LA’de ise yaklaşık  **30** .

Gördüğünüz gibi, ne kadar uzaktaysanız, sonuçta o kadar uzun sürer; sizin için web sitesi o kadar yavaş olur.

## 🚀 CDN’nin Devreye Girmesi: Mesafeyi Azaltmak

İşte burada CDN devreye girer ve hız artışını gerçekten şu şekilde sağlar: kullanıcı ile içerik (veya içeriği sağlayan sunucu) arasındaki mesafeyi azaltarak.

Bunu yaparken, bu içerik dağıtım ağı uç noktalarını ( *endpoints* ) mümkün olduğunca dünyanın birçok konumuna yerleştirir. Bizim durumumuzda, kullanıcılarımızın bulunduğu hemen her konumda bir tane olduğunu varsayacağız.

## 📦 İçeriğin Dağıtılması ve Yakından Sunulması

Artık Sidney’deki, Londra’daki, New York City’deki veya LA’deki kullanıcı içeriklere erişmeye çalıştığında, içerik önce içerik dağıtım ağı hizmeti tarafından alınır ve sonra dünyanın dört bir yanına dağıtılır.

Böylece Dallas’taki sunucuya tek bir istek yapılır. Sonra bu istek dünyanın her yerine dağıtılır ve Londra’daki kullanıcılarımız artık Dallas’a kadar gitmek yerine, bu içeriği en yakın coğrafi konumlarından doğrudan alabilir; bu da içeriği almak için gereken süreyi dramatik biçimde azaltır.

Gördüğünüz gibi, bir CDN’nin mesafeyi azaltarak son kullanıcıya faydaları sağlaması oldukça temeldir; bu da hizmeti teslim etmek için gereken süreyi azaltır.

## 📉 Dolaylı Faydalar: Daha Az Yük, Daha Yüksek Uptime, Daha Fazla Güvenlik

Ancak burada görmediğiniz şey dolaylı bir faydadır: Dallas’taki sunucuya gerçekten ulaşan trafiğin miktarındaki azalma. Yani dolaylı fayda, Dallas’ta bu kadar kullanıcıya hizmet etmek için ihtiyaç duyduğunuz yükte veya kapasitede bir azalma görmenizdir.

Bir diğer dolaylı fayda da, Dallas’ta çok daha az geçerlilik ( *validity* ) ve çok daha az şey gerçekleştiği için; çünkü tüm bu kullanıcılar bu yolculukları yapmak zorunda kalmıyor.

Ayrıca çok uzaktaki kullanıcılarla iletişim kurmak zorunda da değilim. Dallas ortamı da  **uptime** ’da bir artış görebilir.

Ve son olarak, kullanıcılar Dallas’taki sunucularla gerçekten doğrudan iletişim kurmadığı için, belirsizlik yoluyla güvenlik ( *security through obscurity* ) şeklinde dolaylı bir faydanız olur.

Bir CDN’nin sonunda son kullanıcıya daha iyi bir fayda sağlamak için nasıl çalıştığını anlamak oldukça temel.
