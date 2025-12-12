# 🔐 OWASP Top 4-6

## 🎯 Giriş ve Öğrenme Hedefleri

OWASP Top 4-6'ya hoş geldiniz! Bu videoyu izledikten sonra, *Insecure Design* (Güvensiz Tasarım), *security misconfiguration* (güvenlik yanlış yapılandırması) ve *vulnerable and outdated components* (zafiyet içeren ve güncel olmayan bileşenler) kavramlarını açıklayabileceksiniz.

Ayrıca güvensiz tasarım, güvenlik yanlış yapılandırması ve zafiyet içeren, güncel olmayan bileşenler için önleme stratejilerini de açıklayabileceksiniz.

---

## 🧩 Güvensiz Tasarımın Tanımı

Güvensiz tasarım, genel olarak bir uygulamanın tasarım aşamasında etkili güvenlik kontrollerinin bulunmamasına karşılık gelir.

Bu durum çoğu zaman saldırılara açık, zafiyet barındıran bir uygulamayla sonuçlanır. Güçlü parola deneme saldırılarını ( *brute force attacks* ), OTP (One Time Password) atlatmayı ( *OTP Bypass* ) ve diğer siber tehditleri önleyecek güvenlik duvarları ya da mekanizmalar uygulanmamıştır.

Güvensiz tasarım, web uygulamasının tasarımına dayalı riskleri vurgular ve mevcut olabilecek tüm mimari kusurları kapsar.

---

## 🛡️ Tasarım Aşamasında Güvenlik Önlemleri

Kusursuz uygulamalar bile güvensiz bir tasarımı telafi edemez. Saldırganlar, uygulamanızdaki zafiyetleri sömürmek için sürekli olarak arayış içindedir.

Belirli saldırılara karşı korunmak için güvenlik önlemlerine ihtiyaç vardır ve bunlar tasarım aşamasının bir parçası olarak değerlendirilip uygulanmalıdır. Uygulamanızın tasarım aşamasında güvenlik duvarları ve diğer güvenlik önlemlerinin tasarlanıp uygulanması, saldırıların önlenmesine yardımcı olur.

Uygun güvenlik stratejilerinin kullanılması, güvensiz tasarımdan kaçınmak için kritik öneme sahiptir. Güvenliği gözeterek tasarlamak, uygulamanızın en baştan itibaren mümkün olduğunca güvenli olmasını sağlar.

---

## ⚠️ Hata Mesajları ve Güvenli Hata Yönetimi

Hata mesajları, uygulama geliştirme ve sorun giderme sürecinin önemli bir parçasıdır. Uygulamanızda bir şeyler ters gittiğinde, hata mesajları sorunları düzeltmenize yardımcı olur ve bunun sonucunda kullanıcı deneyimi iyileşir.

Ancak hatalar güvenli bir şekilde ele alınmazsa, hassas bilgileri açığa çıkarabilir ve bir saldırganın istismar edebileceği zafiyetlere yol açabilir. Kodunuzda uygunsuz hata yönetimi, sunucu yazılımının sürüm detaylarını, kimlik bilgilerini barındıran yapılandırma dosyalarının nerede bulunduğunu, dizin yapısını, sistem yapısını ve daha fazlasını ortaya çıkarabilir.

Bu durum kuruluşunuz için ciddi sonuçlar doğurabilir; veri ihlallerine, finansal kayıplara, cezalara ve itibarın zedelenmesine neden olabilir. Hata ayrıntılarını bir log dosyasına yazmak ve kullanıcılara hassas verileri açığa çıkarmayan, anlaşılır ve güvenli mesajlar göstermek için güvenli bir hata yöneticisi kullanın.

---

## 🔐 Örnek: Kullanıcı Adı / Parola Hataları

Diyelim ki uygulamanızda kullanıcı adı veya parola giriş alanlarında bir hata oluştu.

Parolanın yanlış olduğunu ya da kullanıcı kimliğinin hatalı olduğunu açıkça belirten gerçekçi bir hata mesajı göstermek zararlıdır; çünkü eleme yöntemiyle saldırgan, girdilerden birinin doğru olduğunu anlayabilir ve bunu kendi avantajına kullanabilir.

Bunun yerine girilen kullanıcı adı ve parolanın hatalı olduğunu belirtmek daha iyidir. Bu ifade, saldırgana, gerçek kullanıcı kimlik bilgilerinin tamamına ya da bir kısmına sahip olduğu yönünde belirli bir bilgi vermez.

---

## 💾 Örnek: Veritabanı Hata Mesajları ve SQL Injection

Bir uygulama fonksiyonu başarısız olduğunda uygunsuz hata yönetimine ilişkin bir başka örnek de şudur:

Eğer bir hata mesajı, uygulama tarafından kullanılan bir veritabanı tablosunun yapısına ilişkin bilgiler içeriyorsa, bu durum saldırganlara SQL injection saldırısı gerçekleştirmek için ihtiyaç duydukları her şeyi sağlar; parolalar, hesap numaraları ve kredi kartları gibi değerli verileri açığa çıkarabilir.

Bu durumu ele almanın daha iyi bir yolu, uygulamanın kullanıcı arayüzüne (UI) kullanıcı dostu bir hata mesajı yazması, aynı zamanda daha ayrıntılı bir hatayı sorun giderme amacıyla kullanılmak üzere bir log dosyasına kaydetmesidir.

---

## 🧱 Güvenlik Yanlış Yapılandırmaları ( *Security Misconfiguration* )

Uygulama güvenliği yanlış yapılandırması, bir uygulamada gözden kaçmış yapılandırma zafiyetlerinin bulunduğu durumdur. Saldırganlar bu zafiyetlerden yararlanır.

Buna, üretim ortamına dağıtım yapılmadan önce devre dışı bırakılmadığı takdirde son derece tehlikeli olan hata ayıklama modu ( *debug mode* ) ve Q/A özellikleri gibi, geliştiriciler için gerekli özellikler de dahildir.

Saldırganlar bu özellikleri istismar ederek hassas bilgilere yetkisiz erişim sağlayabilir, hatta ayrıcalıklarını yükseltebilir. Gereksiz özellikler içeren uygulamalar, farkında olmadan kullanıcılara ihtiyaç duyduklarından daha fazla izin tanıyabilir.

Kullanıcıların, bir görevi yerine getirebilmek için ihtiyaç duydukları asgari izinlere sahip olmaları gerekir. Her zaman En Az Ayrıcalık İlkesi'ni ( *Principle of Least Privilege – PoLP* ) uygulayın.

---

## 🧩 Yanlış Yapılandırmaları Önleme Yaklaşımları

Peki bu güvenlik yanlış yapılandırmalarından nasıl kaçınabilirsiniz?

Gereksiz parçalardan, özelliklerden ve dokümantasyondan arındırılmış bir uygulama geliştirmeye çalışın. Gerek duyulmayan tüm frameworkleri ve özellikleri kaldırın ve varsayılan izinleri asla herkese açık olarak paylaşmayın; çevrimdışı ve özel tutun.

Tasarım aşamasında varsayılan kullanıcı adlarını, varsayılan ayarları ve izinleri kontrol edin. Ayrıca arka kapı hesaplarını, açık metin (şifrelenmemiş) yapılandırma dosyalarını ve diğer olası zafiyetleri de kontrol edin.

Güvenlik yanlış yapılandırmasının, uygulama yığınının herhangi bir kısmında ortaya çıkabileceğini unutmayın. Platform, web sunucusu, uygulama sunucusu, veritabanı ve kullandığınız özel kodlar dahil olmak üzere tüm katmanlarda güvenliği göz önünde bulundurun.

Güvenlik yanlış yapılandırmalarının önlenmesi bir ekip işidir ve stratejinizin bir parçası olarak sistem yöneticilerini de dahil etmelisiniz. Geliştiricilerin ve Sistem Yöneticilerinin uzmanlığını birleştirerek, tüm yığının doğru şekilde yapılandırıldığından ve güncel tutulduğundan emin olabilirsiniz.

---

## 🧬 Güncel Olmayan ve Zafiyet İçeren Bileşenler

Yazılım uygulamaları, işletim sistemleri, platformlar ve donanım sürekli olarak evrilir.

Uygulamaların güncel kalmasını ve değişen teknolojiyle uyumlu çalışmasını sağlamak için hata düzeltmeleri ( *bugfixes* ), yeni özellikler, ürün yazılımı güncellemeleri ( *firmware updates* ) ve yamalar sürekli olarak yayınlanır.

Hem istemci tarafında hem sunucu tarafında, uygulamanızda kullanılan her bir bileşenin ve iç içe geçmiş bağımlılığın sürümleri hakkında bilgi sahibi olmalısınız.

Çekirdek platform, destekleyici framework, bağımlılıklar ve doğrudan kullanılan bileşenler düzenli olarak ve zamanında güncellenip yükseltilmezse, bunlar güncelliğini yitirir ve uygulamanızı saldırılara karşı savunmasız bırakır. Mevcut düzeltmeler, uygulamanıza dâhil edilmediği takdirde, uygulamanız yamalar uygulanana kadar günlerce hatta aylarca zafiyetli durumda kalabilir.

---

## 🧹 Bağımlılık ve Bileşen Yönetimi

Uygulamanızı kullanılmayan bağımlılıklar ve özelliklerden arındırın. Bunlar uygulamanıza herhangi bir işlevsellik katmaz ve güncelliğini yitirdiğinde veya istismar edildiğinde risk oluşturabilir.

Yüklü bileşenlerin, iç içe geçmiş bağımlılıkların bir listesini oluşturun ve güvenlik farkındalığı için güncellenen bileşenleri takip edin.

*OWASP* ve *CISA* tarafından yayımlanan en güncel güvenlik riskleri ve zafiyetleri hakkında bilgi sahibi olun.

---

## 📌 Özet: Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* Güvensiz tasarım, uygulama geliştirme sürecinin tasarım aşamasında güvenlik kontrollerinin eksikliği anlamına gelir.
* Belirli türdeki saldırılardan korunmak için güvenlik duvarlarının ve diğer güvenlik önlemlerinin uygulanması hayati öneme sahiptir.
* Uygulamalarınızdaki tehlikeli yapılandırma zafiyetlerini tespit edin ve devre dışı bırakın.
* Varsayılan kullanıcı adları ve parolalar, varsayılan ayarlar ve izinler, arka kapı hesapları ve açık metin yapılandırma dosyaları devre dışı bırakılmalıdır.
* Güvenlik, platform, web sunucusu, uygulama sunucusu, veritabanı ve kullandığınız özel kodlar dâhil olmak üzere yığının tüm katmanlarında dikkate alınmalıdır.
* Güvenli uygulamalar tasarlama ve geliştirme planınızın bir parçası olarak sistem yöneticilerini de dahil edin. Onların uzmanlığı paha biçilmezdir.
* Uygulamanızın içerisinde nelerin bulunduğunu bilin.
* Kullanılan bileşenlerin ve hangi sürümlerin yüklü olduğunun yer aldığı bir kontrol listesi tutun.
* Uygulamanızı, zafiyete dönüşebilecek kullanılmayan bağımlılıklardan veya özelliklerden arındırın ve OWASP ile CISA tarafından yayımlanan en güncel güvenlik riskleri ve zafiyetleri hakkında bilgi sahibi olmaya devam edin.
