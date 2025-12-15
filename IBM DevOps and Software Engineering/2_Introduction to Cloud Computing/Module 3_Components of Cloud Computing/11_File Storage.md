# 📁 File Storage

Bu videoda,  **File Storage** ’ı daha ayrıntılı şekilde ele alacağız. **Direct Attached Storage** gibi, *file storage* da erişilebilmesi ve üzerinde veri depolanabilmesi için önce bir  **compute node** ’a bağlanmalıdır. Ancak  *File Storage* ,  *direct attached storage* ’a kıyasla daha ucuz olabilir, arızalara karşı daha dayanıklı olabilir ve kullanıcı olarak sizin için daha az disk yönetimi ve bakım gerektirebilir.

Ayrıca çok daha büyük miktarlarda *File Storage* sağlayabilir ve bunu bir sunucuya disk olarak sunabilirsiniz.

 *File storage* , uzak depolama cihazlarından ( **remote storage appliances** ) bağlanır. Yani fiziksel diskler ayrı, özel bir donanım parçasının içinde bulunur ve ardından veri merkezindeki altyapı üzerinden  **compute node** ’a bağlanırlar. Bu depolama cihazları yalnızca arızalara karşı son derece dayanıklı olmakla kalmaz; aynı zamanda bu cihazlar *encryption in transit* gibi hizmetler sağladığından, veriler bunlarda çok daha güvenlidir.

Bu cihazların tamamı servis sağlayıcı tarafından yönetilir.

 *File Storage* , compute node’lara bir **ethernet network** üzerinden bağlanır — yani e-posta alırken veya internette gezinirken kullanabileceğiniz türden aynı ağ, ancak bu ethernet ağı normalde bu işe özel olarak tahsis edilir. Bu nedenle bazen  **‘Network Attached Storage’** , **‘Network File Storage’** ya da sadece **‘NFS’** olarak adlandırılabilir.

Ethernet ağlarıyla ilgili sorunlardan biri, hızlarının değişken olabilmesidir — ethernet ağı ne kadar yük altındaysa, hızının veya bant genişliğinin etkilenme olasılığı o kadar artar. Elbette bulut sağlayıcıları depolama ağlarını çok yüksek trafik hacimlerini kaldıracak şekilde inşa eder; ancak buna rağmen tutarlı hız garanti edilemez. Bu nedenle  *File storage* , tutarlı şekilde yüksek ağ hızlarının gereklilik olmadığı iş yüklerinde kullanılma eğilimindedir.

İş yükleri açısından, *File Storage* genellikle aynı anda birden fazla compute node’a bağlanabilir; burada bağlanan disk veya volume, compute node üzerinde başka bir sürücü gibi görünür.

---

## 🗂️ Çoklu Compute Node Bağlama ve Kullanım Senaryoları

 *File Storage* ’ın aynı anda birden fazla compute node’a bağlanabilmesi, ortak bir depolama ihtiyacının olduğu durumlar için onu ideal bir çözüm haline getirir — örneğin departman dosya paylaşımı, bir uygulama tarafından işlenmesi gereken gelen dosyalar için bir  **‘landing zone’** , veya bir web servisinin erişebileceği bir dosya deposu ( **repository** ).

Bu uygulamalarda, bağlayıcı ağın hızındaki potansiyel değişkenlik genellikle bir sorun değildir.

Elbette maliyetin kritik olduğu durumlarda, veritabanları gibi başka uygulamalar için de *file storage* kullanabilirsiniz; ancak bunun karşılığı hızdır ( *trade-off is speed* ).

---

## ⚙️ IOPS Kapasitesi

*File storage* sağlarken dikkate almanız gereken unsurlardan biri, depolamanın **IOPS** kapasitesidir.  **IOPS** , *Input/Output Operations Per Second* ifadesinin kısaltmasıdır ve disklerin veri yazma ve okuma hızını ifade eder ( **not** : bu, depolama ile compute node arasındaki ağın hızı değildir).

IOPS değeri ne kadar yüksekse, alttaki diskin hızı o kadar yüksektir. Daha yüksek bir IOPS genellikle daha fazla maliyet anlamına da gelir.

IOPS’i anlamak önemlidir; çünkü IOPS değeri uygulamanız için çok düşükse, depolama bir darboğaz haline gelebilir ve uygulamanızın yavaş çalışmasına neden olabilir. Alternatif olarak, IOPS çok yüksekse, muhtemelen depolamanız için ihtiyaç duyduğunuzdan daha fazla ödeme yapıyor olursunuz.

Örneğin, bir dosya paylaşımı 30 farklı compute node’a bağlanmış olabilir ve bir uygulama bu paylaşıma dakikada 60 kez veri yazar ve ister. Bunu ortalamaya vurursanız saniyede 1 işleme denk gelir. Bu basit örnekle, her uygulamanın farklı IOPS gereksinimleri olduğunu görebilirsiniz.

---

## 🧱 Sonraki Video

Bir sonraki videoda **Block Storage** hakkında daha fazla konuşacağız, bunun *File Storage* ile nasıl karşılaştırıldığını ve tipik olarak birini diğerine göre ne zaman kullanacağınızı ele alacağız.
