# 🔐 Güvenli Bulut Ağları

Bulut ortamları daha fazla benimsendikçe ve dijital veriler hızla artan siber güvenlik tehditlerini davet ettikçe, Bulut üzerinde güvenli ağlar inşa etmek kritik hale gelir. Güvenli bir Bulut ağ varlığını nasıl oluşturabileceğimize bakalım.

## 🏢 Bulutta Ağ Kurma Mantığı

Beklenebileceği gibi, bir Bulut ağı oluşturma fikri, şirket içi (on-premises) bir veri merkezinde ağ dağıtmaktan çok da farklı değildir. Temel fark, Bulut’ta fiziksel cihazlar yerine ağ bileşenlerinin mantıksal örneklerini kullanmamızdan kaynaklanır.

Örneğin, *network interface controllers* veya  **NIC** ’ler, bulut ortamlarında  **vNIC** ’ler olarak temsil edilir.

## 🧩 Ağ Fonksiyonlarının Hizmet Olarak Sunulması

Bulut’ta ağ işlevleri, raf tipi (rack-mounted) cihazlar biçiminde değil, **hizmet olarak** sunulur. Bulut’ta bir ağ oluşturmak için, işe ağın boyutunu veya Bulut ağını tanımlayan sınırları belirleyen IP adres aralığını tanımlayarak başlanır.

## 🧱 VPC ve Alt Ağlar

Bulut ağları, **Virtual Private Cloud** veya **VPC** gibi seçenekler kullanılarak ağların mantıksal olarak ayrılmış segmentleri olan ağ alanlarında dağıtılır ve bunlar da *subnet* adı verilen daha küçük segmentlere bölünebilir.

Mantıksal olarak segmentlere ayrılmış bulut ağları, müşterilere özel bulutların güvenliğini ve genel bulutların ölçeklenebilirliğini sunan, bulutun özel bir ayrılmış bölümüdür.

## 🖥️ Kaynakların Subnet’lere Dağıtılması

 **VM** ’ler veya  **Virtual Server Instances (VSI)** ’ler, depolama, ağ bağlantısı ve yük dengeleyiciler gibi Bulut kaynakları subnet’lere dağıtılır. Subnet’ler kullanmak, kullanıcıların şirket içi ortamlarda kullanılan aynı çok katmanlı ( *multi-tier* ) konseptlerle kurumsal uygulamalar dağıtmasına olanak tanır.

Subnet’ler ayrıca Bulut’ta güvenliğin uygulandığı ana alandır. Her subnet, subnet seviyesinde bir güvenlik duvarı görevi gören **access control lists (ACLs)** tarafından korunur. Subnet içinde ise **security groups** oluşturulabilir; bunlar **VSI** gibi örnek (instance) seviyesinde güvenlik sağlar.

## 🏗️ Üç Katmanlı Uygulama Örneği

Bir subnet oluşturduktan sonra, uygulamalarınızı çalıştırabilmek için içine bazı  **VSI** ’lar ve depolama ekleme zamanı gelir.

Diyelim ki Web erişimi gerektiren VSI’lar, uygulama katmanı VSI’ları ve arka uç veritabanı VSI’ları gerektiren üç katmanlı bir uygulamanız var. Bu durumda, web’e bakan VSI’ları birinci bir security group’a, uygulama VSI’larını ikinci bir security group’a, veritabanı VSI’larını ise üçüncü bir security group’a yerleştiririz.

Web’e bakan VSI’ların İnternet erişimine ihtiyaç duyduğu açıktır. Kullanıcıların İnternet katmanındaki uygulamaya erişimini sağlamak için ağa bir **public gateway instance** eklenir.

## 🛡️ VPN ile Güvenli Bağlantı

Public gateway’ler Bulut’a İnternet erişimi için harika olsa da, kurumlar kendi şirket içi kaynaklarını **Virtual Private Networks (VPNs)** kullanarak güvenli biçimde bağlayıp Bulut’a genişletmekle ilgilenir.

## ⚖️ Yük Dengeleyiciler ve Uygulama Yanıt Verebilirliği

Birçok subnet oluşturup çeşitli iş yükleri dağıtırken, uygulamaların yanıt verebilir kalmasını sağlamak gerekli hale gelir. Bu, farklı uygulamalar için bant genişliği kullanılabilirliğini sağlayan **load balancers** ile gerçekleştirilir.

## 🔗 Hibrit Bulutta Özel Yüksek Hızlı Bağlantılar

Hibrit Bulut ortamına sahip kurumlar, bulutlar ile şirket içi kaynaklar arasında özel yüksek hızlı bağlantılar kullanmanın, genel bağlantı çözümlerine göre daha güvenli ve daha verimli bir yöntem olduğunu görür.

Bazı bulut hizmet sağlayıcıları bu tür bağlantı sunar; örneğin **IBM Cloud** ve şirket içi kaynakların gerektiğinde Bulut’a genişletilmesini sağlayan **Direct Link** çözümü.

## 🧠 Sonuç: Bulut Ağı Kurmanın Özeti

Bir Bulut Ağı oluşturmak; BT profesyonellerinin ortamlarını güvence altına almak ve yüksek performanslı iş uygulamalarını sağlamak için uzun süredir güvendikleri veri merkezi ağlarına benzer ağ işlevselliği sunan bir dizi mantıksal yapı ( *logical constructs* ) oluşturmayı içerir.
