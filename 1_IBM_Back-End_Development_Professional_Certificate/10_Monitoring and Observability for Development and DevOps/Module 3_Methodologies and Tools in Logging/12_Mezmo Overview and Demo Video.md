# 🔭 Mezmo Genel Bakış ve Demo Videosu

Mezmo Genel Bakış ve Demo Videosu’na hoş geldiniz. Bu videoyu izledikten sonra Mezmo’yu ve özelliklerini açıklayabilecek, platformda Mezmo ile çalışmayı gösterebilecek ve log verisini içeri aktarma yöntemlerini sergileyebileceksiniz. Mezmo, daha önce *LogDNA* olarak bilinen, telemetri verilerinizi yönetmek ve üzerinde aksiyon almak için kullanılan güçlü bir *gözlemlenebilirlik (observability)* platformudur. Mezmo log analizi, operasyon ekiplerine veri akışı üzerinde kontrol sağlar ve geliştiricilerin loglardan hızlıca değer elde etmesini mümkün kılar.

Mezmo  *agent* ’ları, kod kütüphaneleri veya  *API* ’leri kullanarak minimal kurulum ve onboarding ile birden fazla kaynaktan loglarınızı kolayca merkezileştirebilirsiniz.

---

## 🛠️ Mezmo’nun Özellikleri

Mezmo ile çalışmak çeşitli özellikler sunar. Mezmo, tüm *DevOps* ekibi düşünülerek geliştirilmiştir.

Özellikleri, operasyon ekiplerinin doğru veriyi doğru geliştirme ekibine daha hızlı ulaştırabilecek şekilde yapılandırabilirsiniz. Bu, iş birliğini artırırken daha güvenli uygulamalar elde edilmesine de katkı sağlar.

Mezmo, otomatik ve özel ( *custom* ) ayrıştırma ( *parsing* ) için kullanılabilir. Geliştiricilerin loglarından ihtiyaç duydukları veriyi kolayca ortaya çıkarmasına olanak tanır.

Mezmo’nun *alert* (uyarı) özelliğini kullanarak sistem etkinliğinizle ilgili bildirimler alabilirsiniz. Ayrıca üretimde meydana gelen sorunlar hakkında ekibinizi bilgilendirecek uyarılar kurabilirsiniz. Uyarılar,  *PagerDuty* , *Slack* ve daha fazlası gibi çeşitli entegrasyonlarla yapılandırılabilir.

Mezmo, kritik *Cloud* ve *Kubernetes* olaylarını görmenizi sağlar. Log verinizi belirli bir zaman aralığında görselleştirerek sistem etkinliğinizi daha iyi analiz edebilir ve trendleri belirleyebilirsiniz.

*Spike protection* özellikleri ile dinamik eşikler ve veri hacmi limitlerine ulaşıldığında tetiklenen uyarılar ayarlayabilirsiniz.

Mezmo;  *Payment Card Industry (PCI)* ,  *Service Organization Control type 2 (SOC 2)* , *Health Insurance Portability and Accountability Act (HIPAA)* ve *General Data Protection Regulation (GDPR)* gibi endüstri regülasyonlarına uygundur.

---

## 🧪 Mezmo Platformu Demonstrasyonu

Şimdi Mezmo platformunda neler yapabileceğinizi gösteren demoyu izleyin. Mezmo’nun log analiz platformu; logları toplamanıza, izlemenize, ayrıştırmanıza, *live tail* yapmanıza, grafiğini çizmenize ve net görselleştirmeler ile daha akıllı uyarılarla analiz etmenize olanak tanır; hem de birkaç dakika içinde.

*mezmo.com* adresini ziyaret ettiğinizde, sağ üstteki **"Start Free Log Analysis"** seçeneğine tıklayarak kayıt olabilirsiniz. E-posta adresinizle 14 günlük deneme sürümüne kaydolduktan sonra hesabınızı kurabilir ve yeni bir organizasyon oluşturabilirsiniz.

Organizasyonunuz; loglarınıza erişip yapılandırabildiğiniz, üye ekleyebildiğiniz, faturalandırma planlarını değiştirebildiğiniz ve hesabınızın diğer yönlerini yönetebildiğiniz bağımsız bir çalışma alanıdır.

Bir organizasyon oluşturduğunuzda, log göndermek için kullanabileceğiniz otomatik oluşturulmuş bir *ingestion key* verilir.

---

## 📊 Enterprise Dashboard

 *Enterprise dashboard* , organizasyonunuzun ne kadar veri içeri aktardığına dair bir genel bakış sağlar. Günlük log satırı saklama ( *retention* ) bilgisini ve saklama süreleri kategorileriyle bir *stack graph* gösterir; ayrıca günlük restore edilen veri, içeri aktarılan veri, günlük saklanan veri ve en çok kullanılan uygulamalar, kaynaklar ve etiketlerdeki kullanım trendlerini sunar.

Bu kurs için 14 günlük Mezmo ücretsiz denemesini kullanabilirsiniz. 14 gün sonra Mezmo’yu kullanmaya devam edebilirsiniz; ancak loglar saklanmaz.

Daha fazla bilgi için Mezmo web sitesindeki fiyatlandırma seçeneklerini kontrol edebilirsiniz. Orada, Mezmo’yu öğrenmek için mükemmel olan  *community version* ’ı göreceksiniz.

---

## 🔎 Log Arama (Search)

Mezmo’nun güçlü arama yeteneğini kullanarak loglarınızı arayabilirsiniz. Bir arama terimi, tek bir kelimeden veya tırnak içine alınmış bir ifadeden oluşan bir string’dir. Girdi terimleriniz, tüm log boyunca aranır. Alan ( *field* ) belirtilirse, belirli bir alanda da aranabilir.

Operatörleri kullanmak, arama süreci üzerinde daha fazla kontrol sağlar ve daha ilgili sonuçlar sunar. Burada loglarımızda *invalid user* string’ini arıyoruz ve bu string’in nerede bulunduğuna dair ayrıntılı sonuçlar elde ediyoruz. Satır öğelerini genişleterek bu öğeyle ilişkili metadata ve alanları keşfedebilirsiniz.

---

## 🧭 Views (Görünümler)

 *Views* , log satırları için belirli filtreler ve arama sorgularına ait kısayollara kaydedilir.

Views’e ilk kez girdiğinizde, tüm log satırlarını gösteren varsayılan  **everything view** ’u görürsünüz. Örneğin *connection close* sonuçlarını gösteren bir view oluşturmanız gerekiyorsa, sorguyu arama fonksiyonuyla arayın. Bu, *connection close* sonuçlarını döndürecektir.

Tüm yeni sorgular varsayılan olarak kaydedilmemiş ( *unsaved view* ) durumdadır. Artık bunu benzersiz bir ad vererek yeni bir view olarak kaydetmeyi seçebilirsiniz; kategori ve uyarı isteğe bağlıdır.

View oluşturulduktan sonra, saklanan view’ların adlarını genişletebilir ve tercih ettiğiniz view’a tıklayarak sonuçları doğrudan görebilirsiniz. Bu, sonuçları görüntülemek için kolay ve hızlı bir yol sağlar.

---

## 🚨 Views Üzerinden Alert (Uyarı) Ekleme

Belirli koşullar sağlandığında sizi bilgilendirmek için view’lara uyarılar ekleyebilirsiniz. Mezmo;  *Slack* ,  *PagerDuty* , *Datadog* gibi çeşitli mesajlaşma ve bildirim platformları için uyarı entegrasyonları ve farklı log veri türleri için view, board ve screen şablonları sağlar.

Tek bir view’a uyarı ekleyebilir veya birden fazla view’a uygulayabileceğiniz bir uyarı şablonu ( *alert template* ) oluşturabilirsiniz.

Bu örnekte, daha önce oluşturulan *connection close* view’u için bir e-posta uyarısı oluşturacağız. Views, birden fazla uyarıya ve birden fazla uyarı tipine sahip olabilir.

*Presence* (varlık) veya *absence* (yokluk) uyarılarını yapılandırabilirsiniz. Uyarıyı *presence* olarak ayarlayın. Bu örnek için, **15 dakikada 100 log satırı** olacak şekilde ayarlayın. Her 15 dakikanın sonunda, log kriterleri karşılandığında seçtiğiniz e-postaya bu uyarı gönderilecektir.

---

## 📥 Log Verisi İçeri Aktarma (Ingestion) Yöntemleri

Mezmo, log verisini içeri aktarmak için çeşitli yöntemler sağlar.

Loglarınızın üretildiği host üzerine Mezmo log agent’ını doğrudan kurabilirsiniz. Mezmo agent’ını  *Linux* ,  *Windows* ,  *MacOS* , *Kubernetes* ve *OpenShift* sistemlerinde dağıtabilirsiniz.

Mezmo *CLI* ile log satırı verisini *live tail* yapabilir ve filtreleyebilirsiniz.

Mezmo istemci tarafı logger’ı, istemci tarafı JavaScript uygulamanızdan logları Mezmo’nun ingestion sunucularına gönderir.

Mezmo, çeşitli popüler loglama platformlarından ve *Syslog* çeşitlerinden logları doğrudan göndermek için entegrasyonlar geliştirmiştir.

Go, Python, Ruby, Rust, Android ve iOS ile geliştirilen uygulamalardan logları doğrudan göndermek için hem Mezmo tarafından desteklenen hem de topluluk tarafından sağlanan kod kütüphaneleri mevcuttur.

Mezmo  *API* ’sini kullanarak Mezmo’ya log satırları gönderebilir, ayrıca ingestion’ı programatik olarak yöneterek başlatıp durdurabilirsiniz.

---

## ✅ Video Özeti

Bu videoda Mezmo’nun, telemetri verilerinizi yönetmek ve üzerinde aksiyon almak için kullanılan bir gözlemlenebilirlik platformu olduğunu öğrendiniz. Mezmo’nun özellikleri arasında otomatik ve özel ayrıştırma, uyarılar, spike protection ve logları görselleştirme yer alır.

Mezmo’nun log analiz platformu; arama, uyarı oluşturma, log verisi içeri aktarma ve çok daha fazlası için kullanılabilir.
