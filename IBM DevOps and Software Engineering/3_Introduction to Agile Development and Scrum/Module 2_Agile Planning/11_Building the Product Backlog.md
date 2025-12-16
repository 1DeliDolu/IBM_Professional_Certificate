# 🧩 Ürün Backlog’unu Oluşturma

Bu videoyu izledikten sonra şunları yapabileceksiniz: Bir ürün backlog’unu tanımlamak, bir ürün backlog’unu nasıl bir araya getireceğinini açıklamak ve gereksinimleri hikâyelere dönüştürmek.

Scrum sürecindeki adımlara geri dönüp bakarsak, bu modülde yalnızca ürün backlog’u ile ilgileneceğiz. Ürün backlog’unu nasıl oluştururuz?

## 🗂️ Ürün Backlog’u Nedir?

Ürün backlog’u, uygulanmamış tüm hikâyelerdir, değil mi? Sprint’te olmayan, üzerinde çalışılmayan, çalışılmayı bekleyen hikâyeler. Genellikle bunu sıralı bir şekilde derecelendiririz; yani öncelik sırasına koyarız.

Eğer uzun bir ürün backlog’u varsa, en üsttekiler alttakilere göre daha doğru bir şekilde sıralanmış olur ve bu sorun değildir.

Yalnızca bir ya da iki sonraki sprint’i sıralamanız gerekir; geri kalanlar nispeten sıralanmamış olabilir, ancak backlog’un en üstü iş açısından önem sırasına göre sıralanmalıdır. Bir sonraki sprint’e almamız gereken bir sonraki en önemli şey nedir?

Ayrıca, en üstteki hikâyeler, alttaki hikâyelerden daha fazla detaya sahip olmalıdır, değil mi? Yani bu backlog üzerinde çalışırken ve hikâyeler üzerinde çalışırken, en üsttekileri sprint’e hazır hâle getirmek isteriz; ihtiyaç duydukları tüm detaylara sahip olmalarını isteriz. Alttakiler ise yine biraz daha belirsizdir. Onlar üzerinde daha sonra çalışacağız, daha sonra daha fazla detay ekleyeceğiz.

## 🧮 Örnek: Sayaç (Hit Counter) Servisi Gereksinimleri

Bir örnek üzerinden gideceğiz ve bu örnekte, geliştirdiğimiz servis için size bazı örnek gereksinimler vereceğiz. Peki ne inşa ediyoruz?

Bir hit counter (ziyaret/sayaç) oluşturacağız; yani bir şeyleri sayan bir servis olacağız. Böylece sayaca bir isim verebilirim ve her artırdığımda 1, 2, 3, 4… ve sonra “Bunlardan kaç tane var?” derim ve bana 4 sayısını geri verir. Yani sadece bir şeyleri saymak için kullandığımız küçük bir sayma servisi; bir sayfadaki hit’leri saymak, istediğiniz herhangi bir şeyi saymak gibi. Yani bir sayma servisi.

Şimdi, bunun ileride birden fazla sayaca izin vermesini istiyoruz; dolayısıyla birden fazla sayaç ile birden fazla şeyi sayabilmek gereksinimlerimizden biri.

Ayrıca sayaçların yeniden başlatmalar arasında kalıcı olması gerekiyor. Yani bu yalnızca bellek içi bir sayaç olamaz. Sistemin yeniden başlatılıp tekrar ayağa kalktığında tüm sayaçları hatırlaması için bir tür kalıcılığa, bir tür veritabanına ihtiyacı olacak.

Sonra bir gereksinim daha var: “Biliyor musun, muhtemelen ara sıra bir sayacı sıfıra geri resetleyebilmem gerekir.” Böylece o şeyleri yeniden saymaya başlayabilirim; yani bir sayacı sıfırlamak da müşterinin bize verdiği başka bir gereksinim.

## 🧱 ZenHub Kanban Board ve Pipeline’lar

ZenHub’daki kanban board’a bakarsak bu sütunları görürsünüz; bunlara pipeline denir:  **New Issues** ,  **Icebox** ,  **Product Backlog** ,  **Sprint Backlog** ,  **In Progress** ,  **Q&A** , **Review/Q&A** ve  **Done** .

Bu alıştırma için **New Issues** dışında hiçbir şeyle ilgilenmemize gerek yok. Yeni hikâyeler oluşturmaktan bahsedelim. New Issues var ve boş; bu yüzden ilk hikâyeyi oluşturmaya başlayacağız:  **Bir şeyleri saymak için gerekli servis** .

## 🧾 Hikâye Şablonunu Uygulama

Hikâye şablonumuza geri dönelim; hatırlayın:  **Bir rol olarak** ,  **bir fonksiyona ihtiyacım var** ,  **böylece bir fayda kazanırım** .

Bunu ilk hikâyeye uygulayalım: bir şeyleri saymak için servise ihtiyaç var. Peki bu kimin için? Muhtemelen kullanıcı için, değil mi?

Bir kullanıcı olarak, bir sayacı olan bir servise ihtiyacım var, böylece bir şeyin kaç kez yapıldığını takip edebilirim.

Artık bunun kimin için olduğunu biliyoruz, ne olduğunu biliyoruz ve bundan sonra elde edecekleri değerin ne olduğunu biliyoruz. Bu aşamada hikâye hakkında bildiğim neredeyse sadece bu kadar.

Bu hikâyeyi New Issues içine koyacağım, bu hikâye için yeni bir issue oluşturacağım ve böylece artık normal bir hikâyeye dönüşecek.

## 🧩 Gereksinimleri Hikâyelere Çevirme

Şimdi bir sonraki gereksinime bakalım:  **Birden fazla sayaca izin vermeli** . Yine gidip “Bu kimin için?” diye bakıyoruz. Muhtemelen hâlâ kullanıcı için.

Bir kullanıcı olarak, birden fazla sayaca sahip olmaya ihtiyacım var, böylece aynı anda birkaç sayımı takip edebilirim.

Yine bunun kimin için olduğunu biliyoruz, neye ihtiyaç duyduklarını biliyoruz ve onlar için ne kadar değerli olduğunu biliyoruz; dolayısıyla backlog’u sıralarken şunu söyleyebiliriz: “Aynı anda birkaç şeyi takip edebilmenin değeri ne kadar?” Belki başlangıçta değil; belki önce bir tane çalıştırırız, değil mi?

Dolayısıyla daha sonra bu backlog’u sıralamak için bilmeniz gereken tüm bilgi budur. Bu da New Issues içinde bir hikâyeye dönüşür.

Şimdi bir sonraki gereksinime bakalım:  **Sayaçları yeniden başlatmalar arasında kalıcı kılmak** . Bu kimin için? Belki bu, servis sağlayıcı içindir, değil mi? Belki servis sağlayıcı, servis yeniden başlatıldığında tüm sayaçlar kaybolursa mahcup olur.

Dolayısıyla belki bu servis sağlayıcı içindir: Kullanıcıların servis yeniden başlatıldıktan sonra sayımlarını kaybetmemesi için son bilinen sayımı kalıcı kılan bir servise ihtiyacım var ve bunun ne kadar önemli olduğunu değerlendirebiliriz. Bu bizim üçüncü hikâyemiz.

Şimdi dördüncü gereksinime bakalım:  **Sayaçlar sıfırlanabilir** . Yine aynı şekilde gideriz; bu bir sistem yöneticisi için olabilir. Belki şöyle deriz: “Hey, yalnızca sysadmin bir sayacı resetleyebilir.” Belki kullanıcıların sayaçları resetlemesine izin vermeyiz.

Bir sistem yöneticisi olarak, sayacı sıfırlayabilme yeteneğine ihtiyacım var, böylece baştan yeniden sayım yapabilirim.

Buradaki önemli kısım, bunun kimin için olduğunu söylemenizdir. Rolü belirtmek, bunun kimlerin faydasına olacağını herkes için netleştirir.

 **“İhtiyacım var”** , gerçekten neye ihtiyaç duyduklarını söyler ve  **“böylece”** , “Bundan elde edecekleri iş değeri nedir?” sorusunu yanıtlar.

Artık backlog’da dördüncü hikâyemi de oluşturdum.

## 🥇 Backlog’u Önceliklendirme

Şimdi backlog’u önceliklendirmeye geçelim. New Issues içine aldıklarıma göre, bunları Icebox’a mı koymalıyım yoksa Product Backlog’a mı? Bunlarla ne yapacağım?

Hatırlayın, New Issues’i gelen kutum gibi kullanmayı sevdiğimi söylemiştim; dolayısıyla şimdi bu dört şey gelen kutusunda olduğuna göre gidip onlarla bir şey yapayım.

Backlog’u önceliklendireyim.

İlkini alırım ve derim ki: “Biliyorsun, bu temel bir şey.” Servisi çalıştırmamız gerekiyor; bu yüzden bu, Product Backlog’un en tepesine gider.

Sonra bir sonraki hikâyeye bakarım ve okurum: birden fazla sayaca sahip olmam gerekiyor. Ve şöyle diyebilirim: “Biliyorsun, birden fazla sayaç, bunu sonra ele alırız. Bu gelecekte yapacağımız bir şey; şu anda üstlenmeyeceğim.”

Sonra servisin yeniden başlatmalar arasında kalıcı olması gerektiğine bakarım. Derim ki: “Muhtemelen çalıştırdıktan hemen sonra gelecek bir şey. Muhtemelen arkasına bir veritabanı koymak isterim.”

Dolayısıyla minimum uygulanabilir ürünümü (minimum viable product) yaptığımda, arkasında herhangi bir kalıcılık olmayabilir. Sonrasında kalıcılık eklenir.

Sonra New Issues’deki son hikâyeye yönetici olarak bakarım ve derim ki: “Evet, muhtemelen veritabanında kalıcı hâle getirdikten hemen sonra sayacı sıfırlayabilmek isterim. Böylece baştan yeniden sayabilirim.”

## 🔄 Tek Satırlık Gereksinimlerden Hikâye Söz Dizimine

Ve yaptığım şey şu: Müşteriden gelen, tek satırlık olan bu yeni gereksinimleri aldım ve onları hikâye söz dizimine yazdım.

Hikâye şablonunu kullandım ve dedim ki: “Bir kullanıcı olarak ihtiyacım var…” değil mi; “Bir rol olarak ‘İhtiyacım var’ böylece bir değer elde ederim” ve sonra bunları, uygulamak isteyebileceğimi düşündüğüm bir öncelik sırasıyla backlog içine taşıdım.

## ✅ Öğrenilenler

Bu videoda şunu öğrendiniz: Ürün backlog’u, uygulanmamış tüm hikâyelerin önceliklendirilmiş (ranked) bir listesidir. Backlog’da üst sıralarda yer alan hikâyeler, daha alt sıralarda yer alanlardan daha fazla detaya sahip olmalıdır ve **“Bir … olarak, …’e ihtiyacım var, böylece …”** şablonunu kullanarak hikâyeler oluşturmak, herkesin kime fayda sağladığını ve sunduğu iş değerini anlamasını sağlar.
