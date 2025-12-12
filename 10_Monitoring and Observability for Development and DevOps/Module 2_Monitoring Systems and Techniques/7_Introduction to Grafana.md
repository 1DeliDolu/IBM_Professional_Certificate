# 📊 Grafana’ya Giriş

Grafana’ya Giriş’e hoş geldiniz! Bu videoyu izledikten sonra şunları yapabileceksiniz: Grafana’yı ve kullanım alanlarını tanımlamak, Grafana’nın temel mimarisini ve nasıl çalıştığını açıklamak ve Grafana kullanmanın faydalarını özetlemek.

## 🧩 Grafana Nedir?

Grafana, profesyonel, çapraz platformlu, açık kaynaklı bir veri görselleştirme ve metrik analiz aracıdır. Zaman serisi analitiği sağlar; bu da zaman içinde veri metriklerini incelemenize, analiz etmenize ve izlemenize yardımcı olabilir. Grafana’yı, verileriniz nerede saklanırsa saklansın metrikleri sorgulamak, görselleştirmek, uyarı oluşturmak ve anlamak için de kullanabilirsiniz.

Grafana, zaman serisi veritabanınızı (veya  *TSDB* ) grafiklere ve görselleştirmelere dönüştürerek, izlenen büyük miktardaki veriyi anlamlandırmanıza yardımcı olur.

## 🔗 Grafana ve Prometheus

Grafana, Prometheus ile de yaygın olarak kullanılır.

## ⚙️ Grafana Nasıl Çalışır?

Grafana’yı şirket içinde ( *on-premises* ) veya bulutta dağıttıktan ve veri kaynağınıza (bir veritabanı gibi) bir bağlantı oluşturduktan sonra, uyarılarınızı ve bildirimlerinizi ayarlayıp yapılandırırsınız. Ardından Grafana, istenen metrikleri veritabanından alır. Bu metrikleri kullanarak verilerinizi görselleştirebilir ve analiz edebilirsiniz.

Ayrıca, Grafana’nın ücretli, kurumsal ( *enterprise* ) sürümünü kullanıyorsanız, *Reporting* (Raporlama) özelliğini de kurabilirsiniz.

Grafana, tarayıcı tabanlı bir uygulamadır. On-premises olarak ya da seçtiğiniz herhangi bir bulut platformuna kolayca kurabilirsiniz.

## 🗄️ Veri Toplama ve Veri Kaynakları

Ancak Grafana yalnızca veritabanlarında depolanan veriler üzerinde çalışır. Veri toplama işlemi yapmaz. Bir veri kaynağına bağlanır ve metrikleri alır.

Grafana’nın özelleştirilebilir panoları ( *dashboard* ), büyük miktardaki verinin yorumlanmasını kolaylaştırır. Grafana, aşağıdakiler dahil düzinelerce veritabanı için yerel destek sağlar: Microsoft SQL Server, AWS CloudWatch, Graphite, Prometheus, ElasticSearch, MySQL, PostgreSQL ve diğerleri.

## ✅ Grafana Kullanmanın Faydaları

Grafana kullanmanın bazı faydaları şunlardır:

* Tüm veri kaynaklarınızı tek bir, düzenli görünümde entegre eder.
* Güçlü analitiği ile iş kararlarınızı yönlendirmenize yardımcı olur.

Ek olarak, kullanıcı ve uygulama davranışını, hata sıklıklarını ve kuruluşunuzda meydana gelen hata türlerini izlemenize yardımcı olur. Ayrıca, uygulamalarınızın ve altyapınızın nasıl performans gösterdiğini daha derinlemesine anlamak için Grafana’yı kullanabilirsiniz.

Grafana’nın kullanıcı arayüzü ( *UI* ) tarayıcı tabanlı olduğu için tüm veriler ekibinizin tamamı tarafından erişilebilir. Erişilebilir veriler, kuruluşunuzda veri odaklı bir kültür oluşmasına yardımcı olabilir.

## 🧰 Grafana’nın Özellikleri

Grafana’nın özellikleri şunlardır:

### 📈 Görselleştirme

Grafana; grafikler, histogramlar, tek istatistik tabloları ( *single stat tables* ), ısı haritaları ( *heatmaps* ) ve serbest metin panellerini ( *free text panels* ) destekler; bunlar işletmelerin genellikle verileri incelemek için ihtiyaç duyduğu bileşenlerdir.

### 🎛️ Özelleştirilebilirlik

Grafana özelleştirilebilir: Panellerinizi renk ve şeffaflık ile tamamen özelleştirebilir veya kullanım senaryonuza daha özel bir şey istiyorsanız kendi görselleştirme eklentilerinizi ( *visualization plugins* ) oluşturabilirsiniz.

Grafana uygulaması açık kaynaktır ve yeniden kullanılabilir panolar paylaşan, canlı bir meraklı topluluğu içerir.

### 🚨 Uyarılar

Grafana’yı, eşikleri görsel olarak tanımlamak ve bildirim göndermek için uyarılarda da kullanabilirsiniz.

### 🔎 Log Keşfi

Grafana; etiket filtreleri ( *label filters* ), filtreleme ve arama kullanarak logları daha verimli şekilde keşfetmenizi sağlar.

### 🧑‍💼 Yönetilebilirlik

Yönetilebilirlik de Grafana’nın temel bir özelliğidir. Şirketiniz için organizasyonlar ve ekipler oluşturmak üzere panellere ve panolara roller ve izinler ekleyebilirsiniz.

## 📝 Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* Grafana, profesyonel, çapraz platformlu, açık kaynaklı bir veri görselleştirme ve metrik analiz aracıdır.
* Grafana, bir veri kaynağına (bir veritabanı gibi) bağlanan ve uyarılar ile bildirimler gönderecek şekilde yapılandırılabilen, on-premises veya bulutta çalışan bir çözümdür.
* Kullanıcı ve uygulama davranışını, hata sıklıklarını ve kuruluşunuzda meydana gelen hata türlerini görselleştirmenize yardımcı olmak için tüm veri kaynaklarınızı tek bir, düzenli görünümde entegre eder.
* Grafana, veri görselleştirme sağlar, özelleştirilebilir, ayrıca logları ve verileri daha etkili şekilde yönetmenize ve keşfetmenize olanak tanır.
