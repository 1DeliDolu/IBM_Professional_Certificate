
# 🚀 Otomatik Ölçekleme

## 👋 Karşılama ve Öğrenme Hedefleri

Merhaba ve otomatik ölçeklemeye hoş geldiniz.

Bu videoyu izledikten sonra şunları yapabileceksiniz:

* Otomatik ölçeklemeyi tanımlamak.
* Üç tür otomatik ölçekleyiciyi açıklamak.
* Her bir otomatik ölçekleyicinin nasıl çalıştığını göstermek.

## 📈 Ölçeklemenin Temelleri ve Kubernetes’te Katmanlar

 *ReplicaSet* ’ler ölçekleme için iyi bir başlangıç sağlar, ancak kaynağınızın her zaman on örneğinin çalışmasını istemezsiniz. İhtiyaç oldukça ölçekleyebilmelisiniz.

Kubernetes otomatik ölçekleme, kümeyi talebe göre otomatik olarak ölçekleyerek kaynak kullanımını ve maliyetleri optimize etmeye yardımcı olur.

Kubernetes, iki farklı katmanda otomatik ölçeklemeyi etkinleştirir: küme veya *node* düzeyi ve *pod* düzeyi.

Kubernetes’te üç tür otomatik ölçekleyici mevcuttur: *Horizontal Pod Autoscaler* ( **HPA** ), *Vertical Pod Autoscaler* ( **VPA** ) ve *Cluster Autoscaler* ( **CA** ).

## ⚙️ `autoscale` Komutu ile Otomatik Ölçekleme Oluşturma

Otomatik ölçekleme oluşturmak için, mevcut *pod* sayısını ve durumunu listeleyin. Bu senaryoda elinizde bir adet *pod* vardır.

Bir *deployment* oluşturduğunuzda, otomatik olarak bir *ReplicaSet* oluşturulur.

Otomatik ölçekleme yapabilmek için, gerekli özniteliklerle birlikte yalnızca `autoscale` komutunu kullanırsınız.

`min`, en az *pod* sayısını ifade eder. Dikkat ederseniz `min` değerini ikiye olacak şekilde değiştirdik.

`max`, en fazla *pod* sayısını ifade eder; ve `CPU percent`, küme genelinde CPU kullanımı yüzde 50’ye ulaştığında sisteme yeni bir *pod* oluşturmasını söyleyen bir tetikleyici görevi görür.

Arka planda ise  *deployment* , yukarı ve aşağı ölçeklemek için hâlâ  *ReplicaSet* ’i kullanır.

Bu otomatik ölçeklenen *ReplicaSet* içindeki çoğaltma ( *replica* ) sayısının, önceki `autoscale` komutunda belirtilen asgari sayı ikiye ayarlandığı için ikiye değiştiğine dikkat edin.

## 🧩 Otomatik Ölçekleme Türlerine Genel Bakış

Şimdi, Kubernetes’te üç tür otomatik ölçekleme tipi vardır.

*Horizontal Pod Autoscaler* yani  **HPA** , *pod* sayısını artırıp azaltarak bir uygulamanın çoğaltma ( *replica* ) sayısını ayarlar.

*Vertical Pod Autoscaler* yani  **VPA** ,  *pod* ’ların kaynak boyutunu veya hızını artırıp azaltarak bir konteynerin kaynak isteklerini ve sınırlarını ayarlar.

*Cluster Autoscaler* yani  **CA** ,  *pod* ’lar zamanlanamadığında ya da talep,  *node* ’ların kapasitesine göre artıp azaldığında, kümedeki *node* sayısını ayarlar.

## 📊 Horizontal Pod Autoscaler (HPA)

Kubernetes’te bir  **HPA** , talebi karşılamak için iş yükünü yatay olarak ölçekleyerek, örneğin bir *deployment* gibi bir iş yükü kaynağını otomatik olarak günceller.

Yatay ölçekleme veya  *scaling out* , uygulama kullanımı değiştikçe çalışan *pod* sayısını otomatik olarak artırır ya da azaltır.

Bir  **HPA** , CPU veya bellek kullanımı gibi metrikler için hedefler ile istenen en fazla ve en az çoğaltma ( *replica* ) sayısını belirleyen bir küme operatörünü ( *cluster operator* ) kullanır.

Örneğin, sabah erken saatlerde sistem yükü düşüktür, bu nedenle bir *pod* yeterlidir.  **HPA** , kullanım taleplerini karşılamak için iş yükü kaynağını otomatik olarak ölçekler.

Saat 11:00’e gelindiğinde, tepe yük üç *pod* ihtiyacı doğurur.  **HPA** , iş yükü kaynağını kullanım talebini karşılayacak şekilde otomatik olarak ölçekler.

Öğleden sonra kullanım düştüğünde, üçüncü *pod* silinmek üzere işaretlenir ve kaldırılır; saat 17:00’ye gelindiğinde kullanım daha da azalır ve başka bir *pod* daha silinmek üzere işaretlenir ve kaldırılır.

## 📄 YAML ile HPA Nesnesi Oluşturma

Otomatik ölçeklemeyi etkinleştirmenin bir başka yolu da, bir YAML dosyasından **HPA** nesnesini elle oluşturmaktır.

`autoscale` komutuna benzer şekilde, en az ve en fazla *pod* sayısını ayarlayabilirsiniz.

`CPU percent` bayrağı, hedef CPU kullanımı yüzdesi ( *target CPU utilization percentage* ) olarak görünür ve sıfırdan bir **HPA** otomatik ölçekleyici oluşturabilseniz de, bunun yerine `autoscale` komutunu kullanmalısınız.

## 📈 Vertical Pod Autoscaler (VPA)

En iyi uygulama, yatay olarak ölçeklemektir; ancak kümede çalıştırmak isteyebileceğiniz ve yatay ölçeklemenin imkânsız olduğu ya da ideal olmadığı bazı hizmetler de vardır.

Dikey ölçekleme ya da  *scaling up* , mevcut bir makineye daha fazla kaynak eklemek anlamına gelir.

 **VPA** , bir hizmeti küme içinde dikey olarak ölçeklemenizi sağlar.

Küme operatörü, tıpkı  **HPA** ’de olduğu gibi CPU veya bellek kullanımı gibi metrikler için hedefler belirler.

Ardından küme, hizmetin bir ya da birden fazla  *pod* ’unun boyutunu mevcut kullanım ve hedeflenen değer temelinde yeniden ayarlar.

## 🧪 VPA Çalışma Örneği

Örneğin, sabah erken saatlerde sistem yükü düşüktür, dolayısıyla *pod* tarafından kullanılan sistem kaynakları da düşüktür.

Saat 11:00’e gelindiğinde, tepe yük daha fazla kapasite ihtiyacı doğurur.  **VPA** , talebi karşılamak için  *pod* ’a daha fazla sistem kaynağı, CPU ve bellek ekleyerek  *pod* ’u otomatik olarak ölçekler.

Öğleden sonra kullanım düştüğünde, *pod* daha az sistem kaynağı kullanacak şekilde otomatik olarak ölçeklenir; saat 17:00’ye gelindiğinde, kullanım daha da azalır ve  *pod* , saat 7:00’deki seviyelere uyacak şekilde daha da otomatik olarak ölçeklenir.

CPU veya bellek gibi kaynak metrikleri üzerinde,  **VPA** ’ları  **HPA** ’larla birlikte kullanmamalısınız. Ancak, özel ( *custom* ) veya harici ( *external* ) metriklerde onları birlikte kullanabilirsiniz.

## 🖥️ Cluster Autoscaler (CA)

 **CA** ,  *pod* ’ların üzerinde çalışabileceği mevcut *node* sayısını artırıp azaltarak, doğrudan kümenin kendisini otomatik olarak ölçekler.

 *Pod* ’lar, **HPA** veya **VPA** kullanılarak otomatik olarak ölçeklenir.

Ancak  *node* ’ların kendisi  *pod* ’larla aşırı yüklendiğinde,  *pod* ’ların küme genelinde kendilerini yeniden dengeleyebilmeleri için  *node* ’ları otomatik olarak ölçeklemek üzere **CA** kullanabilirsiniz.

## 🧪 CA Çalışma Örneği

Örneğin, sabah erken saatlerde sistem yükü düşüktür, bu nedenle mevcut  *node* ’lar bu yükü kaldırabilir.

Talep arttığında yeni *pod* istekleri gelir ve  **CA** , talebi karşılamak için kümeye yeni bir *node* ve *pod* ekleyerek kümeyi otomatik olarak ölçekler.

Saat 11:00’e gelindiğinde, tepe yük yeni  *node* ’u tam kapasiteye getirir.

Öğleden sonra kullanım düştüğünde, kullanılmayan  *pod* ’lar silinmek üzere işaretlenir ve kaldırılır.

Saat 17:00’ye gelindiğinde kullanım daha da düştüğünde, yeni *node* içindeki tüm  *pod* ’lar silinmek üzere işaretlenir ve kaldırılır. Ardından  *node* ’un kendisi de işaretlenir ve kaldırılır.

Bir  *cluster autoscaler* , görevlerinizi çalıştırmak için her zaman yeterli işlem gücü olmasını ve kullanılmayan  *node* ’lar için fazladan ödeme yapmamanızı sağlar.

Örneğin, geceler ve hafta sonları yalnızca geliştirme veya sürekli tümleştirme ( *continuous integration* ) test yüklerine sahip olabilir ve kümelerde, tüm toplu işleme ( *batch processing* ) görevlerinin tamamlandığı ve yeni partinin günün ilerleyen saatlerine kadar başlamadığı dönemler olabilir.

## ✅ Otomatik Ölçekleyici Türlerinin Seçimi ve Özet

Her otomatik ölçekleyici türü, belirli senaryolar için uygundur. En iyi seçeneği bulmak için her birinin artılarını ve eksilerini analiz etmelisiniz.

Üç türün tümünü birlikte kullanmak, hizmetlerin tepe yük zamanlarında kararlı bir şekilde çalışmasını ve talebin düşük olduğu dönemlerde maliyetlerin en aza indirilmesini sağlar.

Bu videoda şunları öğrendiniz:

* Otomatik ölçekleme, gerektiğinde küme veya *node* düzeyinde ve *pod* düzeyinde ölçeklemeye olanak tanır.
* Bir  *deployment* ’ı veya bir  *ReplicaSet* ’i otomatik olarak ölçekleyebilirsiniz.
* Otomatik ölçekleyici türleri arasında yatay *pod* ( **HPA** ), dikey *pod* ( **VPA** ) ve küme ( **CA** ) bulunur ve çoğu zaman üç otomatik ölçekleyici türünün birlikte kullanılması en iyi çözümü sunar.
