# 🖥️ Bare Metal Sunucular

Bir *bare metal* sunucu, tek kiracılı ( *single tenant* ), adanmış bir fiziksel sunucudur. Başka bir deyişle, tek bir müşteriye tahsis edilmiştir. Bulut sağlayıcısı, fiziksel sunucuyu alıp müşteriler için bir veri merkezindeki rafa yerleştirir. Bulut sağlayıcısı sunucuyu işletim sistemine ( *OS* ) kadar yönetir; bu da donanımda veya raf bağlantısında bir sorun olursa bunu düzeltecek veya değiştirecekleri ve ardından sunucuyu yeniden başlatacakları anlamına gelir. Müşteri, sunucuda bunun dışındaki her şeyi yönetmekten ve idare etmekten sorumludur.

*Bare metal* sunucular, ya bulut sağlayıcısı tarafından iş yükü paketlerine uygun olacak şekilde önceden yapılandırılır ya da müşteri gereksinimlerine göre özel olarak yapılandırılabilir. Buna işlemciler, RAM, sabit diskler, özel bileşenler ve işletim sistemi dahildir.

Müşteriler ayrıca kendi işletim sistemlerini kurabilir ve bulut sağlayıcısında bulunmayan belirli  *hypervisor* ’ları kurarak kendi sanal makinelerini ve çiftliklerini oluşturabilir. *Bare metal* sunucularla birlikte, bilimsel hesaplamayı hızlandırmak, veri analitiği yapmak ve profesyonel düzeyde sanallaştırılmış grafikler işlemek için tasarlanmış  *GPU* ’lar da ekleyebilirsiniz.

*Bare metal* sunucular fiziksel makineler olduğu için, sanal sunuculara göre sağlanmaları ( *provision* ) daha uzun sürer. Önceden yapılandırılmış *bare metal* kurulumlarının sağlanması 20–40 dakika sürebilir ve özel kurulumlar yaklaşık üç veya dört saat sürebilir. Ancak bu sağlama süreleri bulut sağlayıcısına göre değişebilir. *Bare metal* sunucular, herhangi bir zamanda tek bir istemciye adanmış olduğundan, benzer boyuttaki sanal makinelerden daha pahalı olma eğilimindedir. Ayrıca, sanal sunucuların aksine, tüm bulut sağlayıcıları *bare metal* sunucu sunmaz.

## ⚙️ Özelleştirilebilirlik ve Kullanım Amaçları

*Bare metal* sunucular tamamen özelleştirilebilir olduğundan, en zorlu ortamlarda müşterinin istediğini yapabilir. *Bare metal* sunucular adanmıştır ve yüksek güvenlikli ve izole ortamlarda uzun vadeli yüksek performanslı kullanım için tasarlanmıştır.

İstemciler *bare metal* sunuculara tam erişim ve kontrol sahibidir çünkü bir *hypervisor* gerekli değildir. Alttaki sunucu donanımı diğer müşterilerle paylaşılmadığından, *bare metal* sunucular yüksek performanslı hesaplama ( *HPC* ) ve minimum gecikmeye bağlı gecikme ( *latency* ) gerektiren veri yoğun uygulamaların zorlu ihtiyaçlarını karşılar. Bu sunucular ayrıca büyük veri analitiği uygulamalarında ve *GPU* yoğun çözümlerde de öne çıkar.

*Bare metal* sunucuların karşıladığı bazı iş yükü örnekleri şunlardır:  *ERP* ,  *CRM* ,  *AI* , *deep learning* ve sanallaştırma. Yüksek düzeyde güvenlik kontrolü gerektiren ya da genellikle şirket içi ( *on-premises* ) bir ortamda çalıştırdığınız uygulamaları kullanıyorsanız, *bare metal* sunucu bulutta iyi bir alternatiftir.

## ⚖️ Bare Metal Sunucular ve Sanal Sunucular Karşılaştırması

*Bare metal* sunucuları sanal sunucularla karşılaştırırken, en önemli değerlendirmelerden bazıları müşteri ihtiyacında bulunur.

*Bare metal* sunucular, *CPU* ve *I/O* yoğun iş yükleri için en iyi sonucu verir, en yüksek performans ve güvenlikte öne çıkar, sıkı uyumluluk ( *compliance* ) gereksinimlerini karşılar ve tam esneklik, kontrol ve şeffaflık sunar; ancak ek yönetim ve operasyonel yük getirir.

Buna karşılık, sanal sunucular hızlıca sağlanır, esnek ( *elastic* ) ve ölçeklenebilir bir ortam sağlar ve kullanımı düşük maliyetlidir. Ancak alttaki donanımı diğer sanal sunucularla paylaştıkları için, aktarım kapasitesi ( *throughput* ) ve performans açısından sınırlı olabilirler.
