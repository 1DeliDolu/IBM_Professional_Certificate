# 🏢 Organizasyonel Yapının DevOps’a Etkisi

Bu videoyu izledikten sonra, organizasyon yapısının DevOps’u nasıl etkilediğini belirleyebilecek, Conway Yasası’nı açıklayabilecek ve DevOps ekipleri için en uygun organizasyonu tanımlayabileceksiniz. Organizasyon yapınızın DevOps’a dönüşme yeteneğinizi nasıl etkilediğine bakalım. Bir DevOps organizasyonu olmanın bir parçası da önce Agile olmaktır çünkü Agile, DevOps’un temel bir ilkesidir. Kendinize şunu sormalısınız: “Organizasyonumun kültürü gerçekten Agile zihniyetini benimsiyor mu?” Agile ekiplerin küçük olması gerektiğini hatırlamak önemlidir. Büyük ekipleriniz varsa ve DevOps’u başarıyla uygulamak istiyorsanız, ekiplerinizi küçük hale getirmeniz gerekir. Agile ekipler adanmış olmalıdır.

Birden fazla projeye aynı anda bağlı kişileriniz olup, tüm bu projelerin aynı hızda ilerlemesini ya da insanların tek bir projeye uzun süre odaklı kalmasını bekleyemezsiniz. Agile ekipler çapraz fonksiyonlu olmalıdır. “Geliştirme ekibi” dediğimiz şey, ürünü geliştirmekten sorumlu olan tüm insanları içerir. Bu; yazılım mühendisleri, test mühendisleri, operasyon mühendisleri, iş analistleri, ne gerekiyorsa demektir. Bu insanların aynı ekipte olması ve biletleme sistemleri üzerinden birbirlerinin dikkatini çekmeye çalışarak silo şeklinde çalışmaması gerekir. Bu ekiplerin kendi kendini organize edebilen yapıda olması gerekir. Bir sprintte bir seferde bir işe taahhüt verirler.

# 📐 Conway Yasası

Organizasyonun neden önemli olduğuna Conway Yasası ile başlayarak bakalım. 1968’de Melvin Conway şunu ifade etti: “Bir sistemi tasarlayan herhangi bir organizasyon (geniş anlamda tanımlanmıştır), yapısı organizasyonun iletişim yapısının bir kopyası olan bir tasarım üretecektir.” Örneğin, dört takımdan bir derleyici yapmalarını isterseniz, dört geçişli bir derleyici elde edersiniz. Dört geçişli bir derleyici elde etmenize şaşırmamalısınız; onu yapması için dört takım istediniz. Bir kullanıcı arayüzü ekibiniz, bir uygulama ekibiniz ve bir veritabanı ekibiniz varsa, üç katmanlı bir mimari elde edersiniz. Üç katmanlı bir mimari elde etmenize şaşırmamalısınız; onu yapması için üç takım istediniz. Bu, Conway Yasası’nın iş başındaki halidir.

# 🧩 Mikroservislere Geçiş İçin Organizasyonu Yeniden Kurgulamak

Yazılımı inşa etme biçiminizi değiştirmek ve bir mikroservis uygulama mimarisini benimsemek istiyorsanız, insanları onların inşa etmesini beklediğiniz mimari etrafında yeniden organize etmeniz gerekir. Teknoloji etrafında organize olan geleneksel bir organizasyonda, tüm kullanıcı arayüzü işlerini yapan ayrı bir kullanıcı arayüzü ekibiniz olabilir. Hangi özelliği geliştiriyor olursanız olun; özelliğiniz için bir kullanıcı arayüzü öğesi eklemek amacıyla bu ekipteki birinin dikkatini ve zamanını almanız gerekir. Buna bazen ön yüz ekibi denir.

Sonra uygulama ekibiniz ya da arka uç ekibiniz vardır ve uygulama mantığını eklerler. Ön yüzle ya da veritabanı şemaları gibi şeylerle uğraşmazlar çünkü tüm bunları yöneten bir veritabanı yöneticileri ekibiniz vardır. Bir veritabanı yöneticisinin (DBA) işi yapması için bir talep açmadıkça kimse veritabanına dokunmaz.

# 🧱 Üç Katmanlı Mimari ve Silolar

Bu şekilde organize olduğunuzda, üç katmanlı bir mimari elde edersiniz. Dediğim gibi, üç katmanlı bir mimariye sahip olmanıza şaşırmamalısınız; onu yapması için üç takım istediniz. Conway Yasası bize, bir organizasyonun iletişim yapısını yansıtan bir yapıya sahip bir tasarım üreteceğini söyler. Burada sürpriz yok. Organize olduğumuz şeyi elde ettik. Bu nedenle nasıl organize olduğunuza özellikle dikkat etmek çok önemlidir. Ekiplerinizi iş alanları etrafında organize etmek daha iyidir.

# 🧭 İş Alanlarına Göre Ekip Organizasyonu

Giriş, kayıt ve kullanıcı verilerini yöneten bir hesap ekibiniz olabilir. Bu ekip, çapraz fonksiyonlu bir ekip içinde kullanıcı arayüzü becerilerine, uygulama becerilerine ve veritabanı becerilerine sahiptir. Ardından kişiselleştirme ekibi vardır. Yapay zekâ (AI) kullanarak kişiselleştirme algoritmaları oluştururlar. Kendi kullanıcı arayüzlerini, kendi uygulama mantıklarını ve kendi veritabanlarını kontrol ederler. Son olarak, gönderim, kabul ve envanter etrafında yetenekler inşa eden bir depo ekibiniz olabilir. Bunlar, onların uçtan uca yönettiği mikroservislerdir.

Depo ekibinin özelliklerini geliştirmek için başka ekiplerle koordinasyon kurmasına gerek yoktur. Özelliklerini tamamlamak için diğer ekiplerin dikkatini almak adına talep açmalarına gerek yoktur. Küçük, adanmış, çapraz fonksiyonlu, kendi kendini organize eden bir ekip olarak çalışırlar. İş alanları etrafında organize olmazsanız, DevOps’un tüm faydasını elde edemezsiniz. Ekiplerinizi iş ile hizalamak istersiniz. Her ekibin bir iş alanıyla hizalanmış kendi misyonu olmalıdır. Gerekli özerkliğe sahip olduklarından emin olun ki bu, bir “mini start-up” gibi hissettirsin.

# 🚀 Yüksek Performanslı DevOps Ekipleri İçin Optimal Yapı

Ekipler kendi kendini organize edebilen ve çapraz fonksiyonlu olmalı; 5-7 mühendisle, 10’dan fazla olmayacak şekilde kurulmalıdır. Ardından, ürettikleri şey için uçtan uca sorumluluk vererek ekiplerinizi güçlendirmek istersiniz. Taahhüt ederler, inşa ederler, dağıtırlar, bakımını yaparlar ve hizmetlerini işletirler. Her şeyi kontrol ederler. Ve onlardan uzun vadeli bir misyon üstlenmelerini istersiniz; bu genellikle tek bir iş alanı etrafında olur. Yüksek performanslı ekipler oluştururken bunun ne kadar önemli olduğunu yeterince vurgulayamam. İnsanlar sürekli ekibe girip çıkıyorsa, sahiplenme ve işlerinden gurur duyma duygusu oluşturan uzun vadeli bir misyona sahip adanmış bir ekibin faydalarını asla elde edemezsiniz.

# ✅ Özet

Bu videoda, DevOps’u başarıyla uygulamak için organizasyonların küçük, adanmış, çapraz fonksiyonlu, kendi kendini organize eden ekiplere sahip olması gerektiğini öğrendiniz. Conway Yasası, bir şirketin tasarım sonuçlarının şirketin iletişim yapılarının doğrudan bir yansıması olduğunu ima eder. Başarılı DevOps ekipleri iş alanları etrafında organize edilmelidir. Her ekibin bir iş alanıyla hizalanan bir misyonu olmalıdır.
