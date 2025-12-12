# 🛡️ OWASP İlk 1-3

## 🎯 Öğrenme hedefleri

OWASP İlk 1-3'e hoş geldiniz! Bu videoyu izledikten sonra,  *bozulmuş erişim kontrolü* , *kriptografik hatalar* ve *enjeksiyon* kavramlarını tanımlayabileceksiniz. Ayrıca bozulmuş erişim kontrolünü, kriptografik hataları ve enjeksiyonu önlemenin yollarını da açıklayabileceksiniz.

## 🔐 Erişim kontrolü

 *Erişim kontrolü* , kimliği doğrulanmış kullanıcılara belirli hakların (veya izinlerin) verilerek uygulamalara ve kaynaklara erişmelerinin sağlanmasıdır.

Erişim kontrolü, kullanıcılara kendilerine tanınmış erişim kapsamında kaynakları ve özellikleri kullanma hakkı veya ayrıcalığı verir.

Erişim kontrolü, kullanıcılara kendilerine tanınan haklar dışında başka haklar gerektirmeden kendi çalışma alanlarını sağlar.

Ve erişim kontrolü, kullanıcıların uygulamaları, sistemleri veya diğer kaynakları kullanırken kendileri için öngörülen izinlerin dışına çıkmamalarını sağlamak için güvenlik politikalarını uygular.

## 🚫 Bozulmuş erişim kontrolü

 *Bozulmuş erişim kontrolü* , saldırganların bir uygulama veya sistem için öngörülen izinlerin dışında erişim sağlaması, değişiklik yapması, silme işlemleri gerçekleştirmesi veya eylemler yapabilmesidir.

Erişim kontrolü zafiyetlerinden yararlanan saldırganlar, uygulamanızın güvenliğini tehlikeye atabilir, şirketinizin itibarına zarar verebilir ve hatta finansal kayıplara yol açabilir.

Saldırganlar, sömürülebilecek bir şey olup olmadığını görmek için URL'lerdeki bilgilerle oynarlar. Örneğin, bir kullanıcının kimliği (ID'si) URL'de görünüyorsa, saldırganlar bir şey olup olmadığını görmek için bunu değiştirmeyi deneyebilir. Eğer bir şey oluyorsa, gizlilik ihlal edilebilir ve uygulamanızın güvenliği risk altına girer.

Bozulmuş erişim kontrolü, 2022 OWASP Top 10 listesindeki bir numaralı zafiyettir. Bu, web uygulamalarında en sık karşılaşılan zafiyetlerden biridir.

Bozulmuş erişim kontrolünü önlemek için yapabileceğiniz bazı şeyler şunlardır: Kullanıcılara sınırlı ayrıcalıklar vermek, onların kendilerine ayrılmış ayrıcalıklı çalışma alanlarında kalmalarını sağlar.

Sınırlı erişim hakları, kullanıcıların izni olmayan bir ortamda gizlice dolaşmalarını veya yetkisiz değişiklikler yapmalarını engeller.

Düzenli erişim kontrolü kontrolleri güvenlik açısından faydalıdır. Bu, yöneticilerin kullanıcıların hem yatayda hem dikeyde hangi seviyede erişime ihtiyaç duyduklarının her zaman farkında olmalarını sağlar.

Uygulamanız hakkında sınırlı miktarda kamuya açık bilgi dağıtın. Çok fazla bilgiyi kamuya açık hale getirmek, saldırganların uygulamanızı istismar etmesine istemeden kapı aralayarak uygulamanızın güvenliğine zarar verebilir. Uygulamanızı güvende tutmak için kamuya açık bilgiyi gerekli olanlarla sınırlayın.

Bazen bir dosya yolunun URL içinde göründüğünü fark etmiş olabilirsiniz. Saldırganlar bunu, web sunucunuzun dizin listelemelerine yapılmış açık bir davet olarak görür.

Sayfaların web sunucunuzun dizininde nerede bulunduğunu dış dünyanın bilmesini engellemek için URL'lerde dizin listelemelerini devre dışı bırakın.

Sunucu günlüklerinde kaydedilmiş herhangi bir erişim kontrolü hatası fark ederseniz, önce sistem yöneticilerinizi uyarmalısınız. Günlüklerin erişim kontrolü hatalarını kaydedip bunlarla ilgili hiçbir şey yapılmamasını istemezsiniz.

## 🧬 Kriptografik hatalar

 *Kriptografi* , birden fazla şifreleme yönteminin kullanılmasıyla sağlanır. Uygulamanızda şifreleme kullanmayı planlıyorsanız, kriptografik hataların farkında olmalısınız.

Şu örneğe bakalım: HTTP isteğiniz, bir kullanıcı kimliği veya kredi kartı numarası gibi hassas bilgilerle ilişkili bazı bilgiler içerebilir.

Kullanıcı kimliği 123 ise ve siz bunu şifreleme kullanarak rastgele bir karakter dizisine dönüştürürseniz, bu bilgi yalnızca hedef alıcı tarafından çözüldüğünde okunabilir veya anlaşılabilir.

URL içinde iletilen HTTP isteğiniz zayıf veya iyi bilinen şifreleme yöntemleri kullanıyorsa, verileriniz muhtemelen hassas veri veya bilgilerinizi saldırganlara sızdıran ya da ifşa eden bir kriptografik hatayla karşılaşacaktır.

Saldırganlar geleneksel şifreleme yöntemlerini kolayca çözebilir. Kriptografik hataları önlemenin en iyi stratejisi, veritabanında saklanan tüm hassas verileri geleneksel şifreleme yöntemleri yerine *kimlik doğrulamalı şifreleme* kullanarak şifrelemektir.

Aktif olarak iletilen veya durağan (beklemede) olan tüm verileri şifreleyin.

Ayrıca HTTPS'in güvenli, HTTP'nin ise güvenli olmadığını anlamak önemlidir. HTTP kullanan web siteleri, güvenli olmadıkları için saldırıya uğrama olasılığı daha yüksek olan sitelerdir.

HTTPS, iletim sırasında bilgilerin şifrelenmesini sağlar; bu da verilerinizi güvende ve korunaklı tutar.

SMTP ve FTP gibi eski protokolleri kullanmaktan kaçının. Bu protokoller ortadaki adam ( *man-in-the-middle* ) saldırılarına daha yatkındır.

Şifreleme anahtarları kritik öneme sahiptir ve saldırganlar için birincil hedeflerdir. Ele geçirilmiş bir anahtar, onlara bir yığın kişisel bilgi ve fikri mülkiyete erişim sağlayabilir.

Bu anahtarları asla yazılım uygulamanıza gömülü ( *hard code* ) olarak yazmayın. Anahtarlar tek ve belirli bir amaçla sınırlı olmalıdır.

Bir anahtar yaşam döngüsü ve yönetim sürecini izleyin. Ve onları güvende tutmak için mutlaka yedekleyip güvenli bir şekilde saklayın.

## 💉 Enjeksiyon saldırıları

 *Enjeksiyon* , güvenilmeyen bilginin bir komut, sorgu veya kötü niyetli veriyle birlikte bir yorumlayıcıya iletilmesiyle ortaya çıkar.

Bu, yorumlayıcıyı istenmeyen komutları çalıştırması için kandırarak, saldırganlara verilere yetkisiz erişim imkânı sağlayarak çalışır.

Yaygın enjeksiyon saldırısı türleri şunlardır: SQL enjeksiyonu, işletim sistemi komut enjeksiyonu, HTTP Host header enjeksiyonu, LDAP enjeksiyonu, cross-site scripting kod enjeksiyonu ve kod enjeksiyonu.

Enjeksiyon saldırılarını ortadan kaldırmanın en iyi yolu, yorumlayıcının kullanılmasından kaçınan veya parametreli bir arayüz sunan güvenli bir API kullanmaktır.

Bir kaçış ( *escape* ) listesi kullanarak anahtar kelimeleri veya özel karakterleri engellemek yardımcı olabilir.

Anahtar kelime listenizi düzenli olarak güncel tutmak her zaman en iyi uygulamadır. Ve saldırganların select ifadelerini kullanıp kullanmadığını kontrol ederek ifadeleri temizleyin ( *sanitize edin* ).

## 📌 Özet

Bu videoda şunları öğrendiniz:

* Çevrimiçi uygulamalardaki en yaygın zafiyetlerden biri bozulmuş erişim kontrolüdür.
* Erişim kontrolü zafiyetlerinden yararlanan saldırganlar, uygulamanızın güvenliğini tehlikeye atabilir, şirketinizin itibarını zedeleyebilir ve hatta finansal kayıplara yol açabilir.
* Kriptografiyi sağlamak için kullanılabilecek birden fazla şifreleme yöntemi vardır.
* İyi bilinen bir şifreleme yöntemi, hassas verilerin kamuya sızmasına veya ifşa olmasına neden olabilir.
* Şifreleme hatalarını azaltmaya yönelik önemli stratejiler arasında, veritabanında saklanan tüm hassas veriler için kimlik doğrulamalı şifreleme kullanmak ve hem durağan hem de iletim halindeki tüm verileri şifrelemek yer alır.
* HTTP yerine HTTPS kullanın ve ortadaki adam saldırılarına yatkın olan SMTP ve FTP gibi eski protokollerden kaçının.
* Enjeksiyon saldırıları, güvenilmeyen bilgilerin bir komut, sorgu veya kötü niyetli veriyle birlikte bir yorumlayıcıya iletilmesiyle gerçekleşir.
* Enjeksiyon saldırılarına örnek olarak kod enjeksiyonu, SQL enjeksiyonu, işletim sistemi komut enjeksiyonu, cross-site scripting ve LDAP enjeksiyonu verilebilir.
