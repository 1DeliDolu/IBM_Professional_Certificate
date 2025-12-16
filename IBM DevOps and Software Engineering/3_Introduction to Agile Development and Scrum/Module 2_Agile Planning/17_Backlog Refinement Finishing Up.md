# 🧾 Backlog Refinement: Son Dokunuşlar

## 🎯 Bu videoyu izledikten sonra yapabilecekleriniz

Bu videoyu izledikten sonra bir hikâyeyi *sprint-ready* hâle getirmek için ayrıntı ekleyebilecek, *technical debt* olan hikâyeleri belirleyebilecek ve *sprint planning* öncesinde ürün  *backlog* ’unuzu sıralayabileceksiniz.

## 🏷️ Etiketler: İşi görselleştirmek

Bir sonraki konuşmak istediğim şey *labels* (etiketler). Etiketler işi görselleştirmemize yardımcı olur. *Kanban* panosuna bakarsak, tüm bu güzel renkleri görürsünüz. Ben renklerde çok aşırıya kaçmam. Çok fazla renk olursa anlamsızlaşır; ama birkaç renk gözüme çarpıyorsa, panomda o renkten çok mu var diye görebilirim. Ve bu benim için ne anlama geliyor?

Bu etiketlere bakalım. Etiketler GitHub’da standart olarak gelir ve bunlar standart GitHub etiketleri ve renkleridir. *Bugs* var; hatalar kırmızıdır. Ben bunu severim. Kırmızı tehlike demektir. Çok fazla hata istemezsiniz. *Enhancements* camgöbeği rengindedir.

Fena değil. *Help wanted* yeşildir. Yani bunlar iyi şeyler gibi. *Questions* var, *won’t fix* var, *invalid* olan şeyler var ve bunlar her bir hikâye hakkında şeyleri görselleştirmeme yardımcı olur. Ama burada olmamasına şaşırdığım 1 etiketi eklemeyi severim ve o da en altta *technical debt*tir. *Technical debt* etiketini sarı yaparım çünkü sarı dikkat demektir. Çok fazla teknik borç istemezsiniz.

## 🧩 Hikâyeye etiket atama: “Enhancement” örneği

Hikâyeme geri dönerim ve derim ki: “Biliyor musun, bu gerçekten müşteriye değer katıyor. Bu, değer katan yaptığımız ilk şey ve bunun bir *enhancement* olduğunu düşünüyorum.” Bu yüzden bu hikâyeye *enhancement* etiketini atayacağım ve sonra kaydedeceğim.

Kaydettiğimde ürün  *backlog* ’uma geri dönerim ve görünümünün değiştiğini fark ederim; aracı kullandığınızda ZenHub’da da değişir. Küçük bir daire olduğunu fark edersiniz… Alt kısmında bir daire olan bir alan var. O daire içinde  *story point* ’ler olacak, yani yakında orada bir sayı olacak.

Ve sonra küçük *enhancement* etiketi var; açık mavi veya camgöbeği renkli *enhancement* etiketi. Böylece artık *kanban* panosunda renklerle nasıl gittiğimizi görmeye başlayabilirim.

## 🧽 İkinci hikâyeyi refine etmek: Kalıcılık ve Redis

Şimdi ürün  *backlog* ’unda öncelik sırasına göre bir sonraki hikâyeye geçelim ve onu *groom* edelim. Bu hikâye şöyle: “Bir servis sağlayıcı olarak, servisin kalıcı olmasına ihtiyacım var; böylece sayacı kaybetmem.”

Peki bazı varsayımlar neler? Belki şöyle deriz: “Biliyor musun, Redis veritabanı kullanacağız.” Bu güzel bir *MEM cache* veritabanı. Bir sayacı takip etmek için ilişkisel bir veritabanına gerçekten ihtiyacımız yok. Geliştiriciler bunu bilmiyor olabilir. Bu yüzden mimar veya lider geliştirici, “Bunu yazmalıyız; kim alırsa alsın bilsin: Redis kullanacağız ve sayacı bir *MEM cache* veritabanında bir *name value pair* olarak saklayacağız,” diyebilir.

Bildiğiniz her şey için—her zaman varsayımlar vardır—bunları hikâyelerde belgelendirin ve sonra kabul kriterlerimiz var: “Sayaçı ikiye artırdım ve servisi yeniden başlattım, o zaman sayaç hâlâ iki döndürmeli,” değil mi? Bu, arkasında gerçekten kalıcılık olduğunu kanıtlar.

Etiket konusuna gelince, şunu söyleyebilirim: “Bu bir  *enhancement* ,” değil mi? Artık daha iyi çünkü sayacı kaybetmiyorsunuz. O yüzden bunu da *enhancement* yapacağım.

## ☁️ New issue’dan gelen hikâyeyi refine etmek: Buluta dağıtım

Sonra bir sonraki hikâyeyi seçeriz: “deploy service to the cloud.” Bunu açtığımızda, “deploy service to the cloud” dışında bir şey olmadığını görürüz; çünkü bu  *new issues* ’dan geldi.

İlk hikâyeleri oluştururken şablonu kullandık; müşteriler ve paydaşlar daha fazla hikâye oluşturacak. Bunlar  *new issues* ’a düşecek. Çok fazla ayrıntıları olmayacak. O yüzden “deploy service to the cloud.” Şimdi bunu refine edelim:

“Bir servis sağlayıcı olarak, servisin buluta dağıtılmasına ihtiyacım var; böylece kullanıcı talebiyle kapasiteyi ölçekleyebilir,” değil mi? Böylece bunun ne kadar önemli olduğunu bilirim.

Ve bazı varsayımlar: IBM Cloud’a koyacağız ve belki bir *Cloud Foundry app* olarak dağıtacağız… ya da Kubernetes’e koyup bir konteyner olarak dağıtacağız. Geliştiriciye, buluta nasıl dağıtmak istediğinize dair bazı ipuçları verin.

Sonra kabul kriterleri: “Buluta dağıttım ve müşteri URL’ye gittiğinde, servisimiz erişilebilir olmalı,” değil mi? Bunun tamamı erişilebilirlikle ilgilidir.

Peki buna hangi etiketi verelim? Ben buna *technical debt* diyeceğim çünkü müşteriye gerçekten fark edilen bir değer eklemiyor. Her ne kadar daha yüksek erişilebilirliğin müşteri değeri olduğu savunulabilse de, müşteri zaten yüksek erişilebilirliği bekler. Yani bu, müşterinin fark edeceği bir *enhancement* değildir. (İsterseniz *enhancement* da diyebilirsiniz; ama tartışma adına ben bunu *technical debt* yapacağım.)

## 🟡 Technical debt nedir?

Bu da şu soruyu doğurur: *technical debt* nedir?

 *Technical debt* , müşterinin değer olarak algılamadığı her şeydir, değil mi? Ürüne gerçekten bir özellik eklemez; ama yapmanız gereken bir şeydir. Eğer yapmazsanız, belki her şey dağılır; bu yüzden “müşteri, bir şeylerin patlamamasından değer alıyor” diye argüman kurup *enhancement* diyebilirsiniz; ama genellikle, müşterinin değer elde ettiği bir müşteri hikâyesi olarak algılamadığı ve “arkada” kalan yapılması gereken şeylerdir.

Birçok insan teknik borcun zamanla biriktiğini bilir ve bunun kötü bir şey olduğunu düşünür; ama bazen doğal olarak oluşur, değil mi? Bazen koddaki güvenlik açıkları, yamalanması gereken harici kütüphanelerden gelir ve bu sizin hatanız değildir. Tamamen kontrolünüz dışındadır; yine de zamanla birikir ve bu borcu ödemek önemlidir.

## 🧰 Technical debt örnekleri

*Technical debt* örneklerine bakalım:

* Kod *refactoring* (yeniden düzenleme). Bazı kestirme yollar aldık ve şimdi kodu refactor etme zamanı. Müşteri refactoring’den doğrudan bir fayda görmez; ama geliştiriciler kod refactor edildiği için belki daha hızlı *enhancement* ekleyebilir. Sonuçta fayda argümanı kurulabilir; ama “yeni özellikler listesi”ne “kodumuzu refactor ediyoruz” yazmazsınız, bu muhtemelen teknik borçtur.
* Ortamları kurmak ve sürdürmek. Müşteriler bunu umursamaz. Test ortamı, herhangi bir ortam… teknik borç. Yapılmalı; ama müşteri bir fayda görmez.
* Veritabanı gibi teknolojiyi değiştirmek. SQL’den NoSQL’e geçmeye karar verdik. Müşteri bunu görmez; her şey perde arkasındadır. Teknik borçtur. Kötü bir şey değildir. Belki daha önce yapamadığınız şeyleri yapmanızı sağlar; ama o “yeni yapabildiğiniz şeyler” *enhancement* olur. Sadece veritabanı değiştirmek teknik borçtur.
* Kütüphanelerdeki güvenlik açıkları. Kütüphaneleri yükseltmeniz gerekir, kodu yeniden test etmeniz gerekir, bir şeylerin bozulmadığından emin olmanız gerekir. Teknik borç.

Teknik borçtan kaçmamak çok önemlidir. Ne olduğunu anlayın, bir etiket verin. Her  *sprint plan* ’e biraz teknik borç koyduğunuzdan emin olun; böylece onu ödüyorsunuz. Bu etikete sahip olarak, *kanban* panosunda kaç hikâyenin sarı ( *technical debt* ), kaç hikâyenin mavi ( *enhancement* ) olduğunu görebilirsiniz.

## 🔁 Sayaç sıfırlama hikâyesini refine etmek

Son olana bakalım: “Bir sistem yöneticisi olarak, bir sayacı sıfırlayabilme yeteneğine ihtiyacım var; böylece bir şeyi yeniden sayabilirim.”

Şimdi varsayımlar ekleyelim. Belki teknik lider şöyle dedi: “Geliştiriciye URL’nin nasıl olacağını söylemeliyiz çünkü biraz zor olabilir. *post* ile `counters`’a, sayaç adıyla, sonra `/reset` ile… bu sayacı sıfırlayacak.” Çünkü sayacı sıfırlamanın birden fazla yolu olabilir, değil mi? Sıfıra güncelleyebilirsiniz; birçok yol var. Ama belki bunu korumak ve sadece yöneticilerin yapmasını sağlamak için, yalnızca yöneticilerin erişebileceği ayrı bir endpoint yaparsınız.

Ve kabul kriterleri: “Sayaç beşe ilerlediyse, serviste reset’i çağırdığımda ve mevcut sayacı istediğimde, servis sıfır döndürmelidir.” Böylece davranışın nasıl olması gerektiğini iyi anlarız. *Definition of done* üzerinde anlaştık;  *sprint review* ’de bunu gösterdiklerinde artık soru kalmaz ve bunun tam olarak böyle yaptığı gösterilir. Kimse “Böyle olması gerekmiyordu” diye tartışamaz.

Şimdi etiket atayalım: Ben bunun bir *enhancement* olduğunu söylerim. Sayaçları sıfırlayabilmek yeni bir özelliktir; bu yüzden *enhancement* ile devam edeceğim.

## 📌 Panoya geri dönüş: Görsel durum

Şimdi *kanban* panomuza geri dönelim. Ürün  *backlog* ’umuz tamamen refine edilmiş durumda ve hızlıca görebileceğimiz etiketlerimiz var: “üç hikâye  *enhancement* , bir hikâye  *technical debt* .” Güzel bir görsel gösterge elde ettim.

 *Icebox* ’takiler sorun değil; onlar daha sonra. Onları sonra refine ederiz. Ama ürün  *backlog* ’unun en üstündekiler bu güzel etiketlere sahip ve belki bu turda *sprint planning* sırasında onlara *story point* de koyabiliriz.

## 🗓️ Backlog refinement için ipuçları

 *Backlog* ’u her  *sprint* ’te refine etmelisiniz. Benim  *sprint* ’lerim genelde Pazartesi’den sonraki Cuma’ya kadar sürer ve *sprint* bitmeden önceki Çarşamba günü bir *backlog refinement meeting* yapmayı severim.

Yani iki haftada bir,  *backlog* ’umu refine ederim ve onu, genelde *sprint* başında Pazartesi sabahı yaptığım *sprint plan* için hazırlarım. Çünkü *sprint retrospective* ve  *sprint review* ’u Cuma günü yaparsınız; herkes yorgundur, eve gider; sonra  *sprint planning* ’i Pazartesi sabah ilk iş yaparım. Bu yüzden bunu genelde Çarşamba yaparım.

Bazı insanlar bunu her hafta yapar ve çok fazla gereksinim geliyorsa her hafta yapmak isteyebilirsiniz. Ama en azından her  *sprint* ’te bir kez,  *backlog* ’u sağlıklı tutmak için refine etmek önemlidir.

Ben ürün  *backlog* ’unda en az iki  *sprint* ’lik refine edilmiş hikâye olmasını severim, değil mi? Eğer bir mucize olur da *sprint* içindeki tüm hikâyeler bitirse, daha fazlasını  *product backlog* ’tan çekebilirler.

Ama çoğunlukla, bir şey olursa kesintiye uğramamak için yeterli sayıda refine edilmiş hikâyem olduğundan emin olmak isterim. Belki bazı gecikmeler yüzünden bir hafta refinement toplantısını atlayabilirim. Bu yüzden ürün  *backlog* ’unda en az iki  *sprint* ’lik refine edilmiş içerik isterim.

## ⏱️ Refinement ne kadar iyi olursa planning o kadar hızlı olur

Bu hikâyeleri refine etmeye ne kadar çok zaman harcarsanız,  *sprint planning* ’de o kadar az zaman harcarsınız.

Eğer *story point* ekleyebilirseniz, güzel; bunu  *sprint plan* ’de yapacağız. Ama *backlog refinement meeting* sırasında bazı  *story point* ’ler ekleyemezseniz sorun değil; çünkü bu hikâyelerin ne kadar büyük olduğuna dair bir fikir verir.

Ama ne kadar çok detay eklerseniz, *sprint planning meeting* sırasında hikâyeleri yazıyor olmak istemezsiniz. Bu, planning toplantısını sonsuza kadar uzatır. Buna güvenin. Hepsini *backlog refinement meeting* sırasında halledin.

## ✅ Kapanış

Bu videoda,  *backlog refinement* ’ın ürün  *backlog* ’unu sıralamak ve hikâyeleri *sprint-ready* hâle getirmek için kullanıldığını öğrendiniz.  *Technical debt* , paydaşın değer olarak algılamadığı her hikâyedir ve hedef, *Sprint planning meeting* için  *backlog* ’u hazır hâle getirmektir.
