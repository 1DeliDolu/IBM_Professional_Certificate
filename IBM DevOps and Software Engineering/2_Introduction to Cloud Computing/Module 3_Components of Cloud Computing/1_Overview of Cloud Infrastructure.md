# ☁️ Bulut Altyapısına Genel Bakış

Bulut hizmet modeli ve satıcıların sunduğu bulut türü seçildikten sonra, müşterilerin altyapı mimarisini planlaması gerekir. Altyapı katmanı bulutun temelidir. Bu katman,  *Bölgeler (Regions)* , *Alanlar (Zones)* ve *Veri Merkezleri (Data Centers)* içinde barındırılan fiziksel kaynaklardan oluşur. Bir bulut sağlayıcısının BT ortamı genellikle dünya genelinde birçok *Bölgeye* dağıtılmıştır.

Bir bulut  *Bölgesi (Region)* , bir bulut sağlayıcısının altyapısının kümelendiği coğrafi bir alan veya konumdur ve *NA South* ya da *US East* gibi isimlere sahip olabilir. Bulut bölgeleri birbirinden izoledir; böylece bir Bölge bir *Deprem* gibi doğal bir felaketten etkilenirse, diğer Bölgelerdeki bulut operasyonları çalışmaya devam eder.

Her Bulut Bölgesinin birden fazla *Alanı (Zone)* (veya kısaca  *Availability Zones / AZ* ) olabilir; bunlar genellikle kendi güç, soğutma ve ağ kaynaklarına sahip, birbirinden ayrı Veri Merkezleridir. Bu Alanlar *DAL-09* veya *us-east-1* gibi isimlere sahip olabilir. Alanların izolasyonu, bulutun genel *hata toleransını* artırır, *gecikmeyi (latency)* azaltır ve tek bir ortak *hata noktası* oluşmasını engeller. *Availability Zone’lar* (ve içlerindeki  *Data Center’lar* ), diğer AZ’lara ve bölgelere, özel veri merkezlerine ve internete çok yüksek bant genişlikli ağ bağlantıları ile bağlıdır.

Bir bulut  *Veri Merkezi (Data Center)* , bulut altyapısını barındıran büyük bir oda veya depodur. Bu veri merkezleri; sunucular gibi standartlaştırılmış bilişim kaynaklarını içeren pod’lar ve rack’ler (veya standart konteynerler) ile birlikte depolama ve ağ ekipmanlarını — yani fiziksel bir BT ortamında bulunan neredeyse her şeyi — içerir.

---

## 🖥️ Hesaplama Kaynakları

Bulut sağlayıcıları birkaç hesaplama seçeneği sunar:  *Sanal Sunucular (Virtual Servers)* , *Çıplak Metal Sunucular (Bare Metal Servers)* ve *“Sunucusuz” (Serverless)* hesaplama kaynakları.

Bir bulut veri merkezindeki sunucuların çoğu, sanallaştırma teknolojilerine dayalı yazılım tabanlı bilgisayarlar olan sanal sunucular veya sanal makineler (kısaca *Virtual Machines* ya da  *VMs* ) oluşturmak için *hypervisor* çalıştırır.

Rack’lerdeki diğer sunucular ise sanallaştırılmamış fiziksel sunucular olan  *bare metal server* ’lardır. Müşteriler ihtiyaç duyduklarında VM’leri ve Bare Metal sunucuları sağlayabilir ve iş yüklerini bunların üzerinde çalıştırabilirler.

Bulut kullanıcıları ayrıca iş yüklerini *sunucusuz (serverless)* hesaplama kaynaklarında da çalıştırabilir; bu, sanal makinelerin üzerinde bir soyutlama katmanıdır. Bu üç hesaplama seçeneğinin her birini sonraki videolarda daha ayrıntılı şekilde ele alacağız.

---

## 💾 Depolama

Bilgi ve veriler; dosyalar, kod, belgeler, görseller, videolar, yedekler, snapshot’lar ve veritabanlarından oluşabilir ve bulutta birçok farklı depolama seçeneğinde saklanabilir.  *Bare Metal Server* ’lar ve  *Virtual Server* ’lar, yerel sürücülerde varsayılan depolama ile sağlanır.

---

## 🌐 Ağ (Networking)

Bir bulut veri merkezindeki ağ altyapısı; router ve switch gibi geleneksel ağ donanımlarını içerir, ancak bulut kullanıcıları için daha da önemlisi, bulut sağlayıcılarının belirli ağ kaynaklarının sanallaştırıldığı veya API’ler aracılığıyla programatik olarak erişilebilir hâle getirildiği *Software Defined Networking (SDN)* seçenekleridir.

Bu, bulutta ağın sağlanmasını (provisioning), yapılandırılmasını ve yönetimini kolaylaştırır. Bulutta sunucular sağlandığında, onların *public* ve *private* ağ arayüzlerini kurmanız gerekir. *Public* ağ arayüzleri, adından da anlaşılacağı üzere, sunucuları genel internete bağlar; *private* olanlar ise diğer bulut kaynaklarınıza bağlantı sağlar ve onları güvende tutmaya yardımcı olur.

Fiziksel BT dünyasında olduğu gibi, buluttaki ağ arayüzlerinin IP adresleri ve subnet’lere otomatik olarak atanması veya yapılandırılması gerekir. Bir bulut ortamında, hangi ağ trafiğinin ve kullanıcıların kaynaklarınıza erişebileceğini yapılandırmak daha da önemlidir; bu da *Security Groups* ve *Access Control Lists (ACLs)* kurarak yapılabilir.

Kaynaklarınız için bulutta daha fazla güvenlik ve izolasyon sağlamak amacıyla, çoğu bulut sağlayıcısı  *Virtual Local Area Networks (VLANs)* , *Virtual Private Clouds (VPCs)* ve *Virtual Private Networks (VPNs)* sağlar. Firewall’lar, load balancer’lar, gateway’ler ve trafik analizörleri gibi bazı geleneksel donanım cihazları da sanallaştırılabilir ve bulutta hizmet olarak sunulabilir.

Bulut sağlayıcılarının sunduğu bir diğer ağ yeteneği ise, içeriği dünya genelinde birçok noktaya dağıtan  *Content Delivery Networks (CDNs)* ’dir; böylece içeriğe erişen kullanıcılar, kendilerine en yakın noktadan içeriği alarak daha hızlı erişebilir.

Bu bulut ağ seçenekleri ve terminolojilerinden bazılarını sonraki videolarda daha ayrıntılı öğreneceğiz. Bulut altyapısı sürekli gelişmekte ve iyileşmektedir. Bir sonraki videoda sanallaştırmayı ve sanal makineleri açıklıyoruz.
