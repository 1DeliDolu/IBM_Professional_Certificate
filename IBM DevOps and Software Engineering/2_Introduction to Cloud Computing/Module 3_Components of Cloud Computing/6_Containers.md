# 🔐 Bulutta Güvenli Ağ Oluşturma

## 📈 Güvenli Ağların Önemi

Bulut ortamları daha fazla benimsenirken ve dijital veriler hızla artan siber güvenlik tehditlerini davet ederken, Bulutta güvenli ağlar inşa etmek kritik önemdedir. Güvenli bir Bulut ağ varlığını nasıl oluşturabileceğimize bakalım.

## 🏢 Şirket İçi Ağlarla Benzerlikler

Beklenebileceği gibi, bir Bulut ağı oluşturma kavramı, şirket içi bir veri merkezinde bir ağ dağıtmaktan çok da farklı değildir.

## 🧩 Mantıksal Ağ Bileşenleri ve Hizmet Olarak Ağ

Ana fark, Bulutta fiziksel cihazlar yerine ağ öğelerinin mantıksal örneklerini kullanmamızdan kaynaklanır. Örneğin, ağ arayüz denetleyicileri veya  *NIC* ’ler, bulut ortamlarında  *vNIC* ’ler olarak temsil edilir. Bulutta, ağ işlevleri raf montajlı cihazlar biçiminde değil, bir hizmet olarak sunulur. Bulutta bir ağ oluşturmak için, kişi ağın boyutunu veya Bulut ağının sınırlarını belirleyen  *IP address range* ’i tanımlayarak başlar.

## 🌐 VPC ve Alt Ağlar

Bulut ağları, *Virtual, Private Cloud* veya *VPC* dahil seçenekler kullanılarak ağların mantıksal olarak ayrılmış segmentleri olan ağ alanlarında dağıtılır; bunlar da kendi içinde *subnets* adı verilen daha küçük segmentlere bölünebilir. Mantıksal olarak segmentlere ayrılmış bulut ağları, müşterilere özel bulutların güvenliğini ve genel bulutların ölçeklenebilirliğini sunan, bulutun özel bir ayrılmış bölümüdür.  *VM* ’ler veya *Virtual Server Instances* ( *VSI* ’ler), depolama,
