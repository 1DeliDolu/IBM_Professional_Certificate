# 🌥️ Hybrid Çoklu Bulut

Hibrit bulut, önceki derste ele aldığımız gibi, bir kuruluşun şirket içi (on-premise) özel bulutunu ve üçüncü taraf genel bulutunu, kuruluşun uygulamalarını çalıştırmak için tek bir altyapıda birleştiren bir bilişim ortamıdır. *Multi-cloud* (çoklu bulut) ise; altyapı, platform veya yazılım hizmetleri düzeyinde, farklı hizmet sağlayıcılardan (genel, özel ve yönetilen) birden fazla bulut modelinin birlikte benimsendiği bir bulut kullanım stratejisidir. Örneğin bir işletme, e-postayı bir sağlayıcıdan hizmet olarak alabilir, bir CRM uygulamasını başka bir sağlayıcıdan kullanabilir ve altyapıyı da farklı bir sağlayıcıdan temin edebilir.

Özetle,  *hibrit çoklu bulut* ; farklı hizmet sağlayıcılarındaki bulut modelleri ve hizmetlerinin en iyi yönlerinden yararlanabildiğiniz ve uygulamalarınız ile iş yüklerinizin birden fazla bulut üzerinde sorunsuz şekilde birlikte çalışabildiği bir yaklaşımı ifade eder.

Bu videoda, bir işletmenin neden hibrit çoklu bulut yaklaşımını tercih edebileceğine dair bazı kullanım senaryolarına bakacağız.

---

## 📈 Bulut Ölçekleme

Bu videoda, bir işletmenin neden hibrit veya çoklu bulutu kullanmak isteyebileceğine dair birkaç kullanım durumuna değinmek istiyorum. En temel olanla başlayalım:  *bulut ölçekleme* .

Çoğumuz bununla muhtemelen aşinayız. Bulutu benimsemenin ana nedenlerinden biridir. Diyelim ki belirli bir kullanıcı tabanına ulaşabilen bir çiçek teslimat servisimiz var. Şirket içi altyapıları var ve belirli bir kullanıcı yükünü karşılayabiliyorlar. Bunu burada görselleştirirsek; bir takvim yılı boyunca yüklerinin artıp azalabileceğini ve belirli tatil günlerine göre değişebileceğini hayal edebilirsiniz.

Bu zirve dönemleri karşılamak için şirket içi mimarilerini büyütebilirler, ancak bu yaklaşım peşin maliyetler ve bakım maliyetleriyle gelir.

Bunun yerine yapacakları şey, yük arttığında ölçeklenmelerine izin veren buluttan yararlanmak ve artık ihtiyaç kalmadığında kaynakları otomatik olarak kaldırmaktır ( *deprovision* ).

Bu kavram aslında sadece hibrit veya çoklu buluta özgü değil; genel olarak bulut bilişimin bir parçasıdır. Ancak bu beni bir sonraki konuya getiriyor.

---

## 🧩 Bileşik Bulut

Burada, *bileşik bulut*un nasıl oluşturulabileceğinden bahsedeceğiz. Bu, temelde birden fazla bulut ortamına yayılmış uygulamalar anlamına gelir.

Çiçek teslimat servisine geri dönelim. Diyelim ki şirket içi mimarileri, uygulamalarının üç ana bileşenini çalıştırmalarını sağlıyor: Web UI, bazı faturalandırma API’leri ve bir ödül (rewards) çerçevesi.

Şimdi diyelim ki bu servis aslında AB merkezli ve Avrupalı müşterileri memnun. Ancak Kuzey Amerika’daki veya Amerikalı müşteriler için, özellikle Veterans Day veya Thanksgiving civarında sistemin yavaşladığını fark ediyorlar. Bunun üzerine, uygulamalarını birden fazla bulut ortamına yayarak hibrit bulut veya çoklu bulut mimarisinden yararlanmaya karar veriyorlar.

Amerika’daki veri merkezlerinden yararlanacaklar ve aslında şunu belirlemişler: Ödül çerçevesi Avrupa tarafında şirket içinde kalabilir; ancak faturalandırma ve UI yeteneklerini taşımak istiyorlar. Dolayısıyla sadece bu iki bileşeni, Kuzey Amerika veya Amerika’daki bir veri merkezinde seçtikleri bir bulut platformuna taşıyacaklar.

Bu, Amerikan tatillerine yanıt olarak belirli bölümleri ölçeklemelerine olanak tanırken, AB tarafındaki bölümlerin de ayrı ayrı ölçekli kalmasını sağlar. Bu örnekte çiçek teslimat servisi, hibrit veya çoklu bulut mimarisi kullanarak küresel ölçekte ölçeklemeden yararlanabilir.

---

## ✈️ Havayolu ve Seyahat Sektörü

Şimdi havayolu veya seyahat sektöründen bahsedelim. Önce *modernizasyon* örneğiyle başlayabiliriz.

Geçmişte rezervasyon sistemleriyle çalışmak zor olabiliyordu veya arayıp konuşmanız gerekebiliyordu. Ancak artık neredeyse tüm havayolu şirketlerinin bir mobil uygulaması var. Çoğu zaman, ve aslında sadece seyahat sektöründe değil genel olarak, kurumsal uygulamaların yaklaşık %80’i hâlâ şirket içinde (on-prem) çalışıyor. Bu sektör için de muhtemelen durum böyledir.

Bu örnekte, diyelim ki şirket içinde çalışan bir rezervasyon sistemleri var; ancak son kullanıcılar için yeni deneyimler üretmek amacıyla bir mobil uygulama geliştirmişler.

Bu mobil uygulama elbette bir mobil backend’e sahip ve bu backend muhtemelen bir genel bulutta çalışıyor; o da rezervasyon servisiyle birlikte çalışıyor. Yani mobil uygulama mobil backend’e istek atıyor, mobil backend de rezervasyon yetenekleriyle çalışıyor.

Bu sayede modernleşmiş oluyorlar ve yeni kullanıcı deneyimleri mümkün hale geliyor. Ancak bunu bir adım daha ileri götürelim.

---

## 🕒 Gecikmeler İçin Öneri Özelliği

Kullanıcı memnuniyetsizliğinin önemli bir kaynağı, uçuşların gecikmesi durumudur. Uçuş geciktiğinde, yolcuların yeni uçuşlar için yeniden rezervasyon yapması gerekebilir. Çözüm neredeyse her zaman aynıdır: Yolcu, mümkün olan en kolay şekilde varış noktasına ulaşmak ister.

Bu nedenle havayolu şirketleri, buluttan yararlanarak bir öneri (recommendation) özelliği oluşturuyor. Bu özellik, bir gecikme önerildiği anda ya da gecikme gerçekleştiği anda yeni uçuşların rezerve edilebilmesini sağlar.

Bu da mobil backend servisine bağlanır ve kullanıcıların uçuş gecikir gecikmez telefonlarından yeni uçuş rezervasyonu yapabilmesine imkân tanır. Bu yalnızca havayolu şirketlerinin kârlılığını artırmakla kalmaz, aynı zamanda daha mutlu kullanıcılar yaratır. Modernizasyonun yapıldığı yöntemlerden biri budur.

Şimdi bunu bir adım daha ileri götürüp veri ve yapay zekâdan bahsedelim.

---

## 📊 Veri ve Yapay Zekâ

Veri ve yapay zekâ için, havayolu sektörü çok miktarda tarihsel veriden yararlanıyor. Bir şirketin on yıllar boyunca var olduğu düşünüldüğünde, plansız bakımın ne zaman gerçekleştiğine dair tarihsel verileri olduğunu varsayalım. Aslında havayolu sektöründeki toplam gecikme süresinin %30’u plansız bakım gerçekleştiğinde ortaya çıkar.

Makine öğrenmesi veya yapay zekâ yeteneklerinden yararlanarak; sahip oldukları tüm eski (legacy) veriye, büyük hacimlere bağlanabilir ve bunları makine öğrenmesi ve yapay zekâ yetenekleriyle birleştirebilirler.

Bu, havayolu şirketlerinin kestirimsel analitikten yararlanmasını ve hatalar oluşmadan ya da plansız bakım gerçekleşmeden önce içgörüler elde etmesini sağlar. Bu da yine kârlılığı artırır, kullanıcıları daha mutlu eder ve daha verimli bir havayolu sektörü yaratır.

Bugün hibrit ve çoklu bulut platformları için dört ana kullanım senaryosunu konuştuk: çiçek teslimat servisinde *bulut ölçekleme* ve  *bileşik bulut* ; havayolu sektöründe ise *modernizasyon* ve  *veri ile yapay zekâ* .

---

## 🔒 Vendor Lock-in’i Önleme

Hibrit çoklu bulut stratejisini benimsemenin bir diğer nedeni de belirli bir satıcının bulut platformuna bağımlı kalmayı ( *lock-in* ) önlemek ve ihtiyaç ortaya çıktığında iş yüklerini bir bulut platformundan diğerine taşıyabilme esnekliğine sahip olmaktır.

Bir sonraki videoda, mikroservis mimarisinin ne olduğunu, özelliklerini, faydalarını ve kullanım senaryolarını anlayacağız.
