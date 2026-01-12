# 🧭 Methodolojilere Genel Bakış

Bu videoyu izledikten sonra, yazılım geliştirmeye yönelik *Waterfall* yaklaşımını açıklayabilecek, *Waterfall* yaklaşımındaki sorunları izah edebilecek, *Extreme Programming* yaklaşımını tanımlayabilecek, *XP* yaklaşımının değerlerini listeleyebilecek, ayrıca  *Kanban* ’ı tanımlayıp temel prensiplerini sıralayabileceksiniz.

---

## 🌊 Geleneksel Waterfall Geliştirme

Geleneksel *Waterfall* geliştirmeye bakalım. Her şey bir **gereksinimler (requirements)** fazıyla başlar. İnsanlar gereksinimleri toplar, müşterinin ne istediğini anlamaya çalışır ve en azından o an için müşterinin isteyeceği bir şeyi teslim edeceğimizden emin olmaya çalışırlar. Bu fazda yaptığınız şey, müşterinin sistemde isteyebileceği tüm gereksinimleri belgelemektir.

Ardından **tasarım (design)** fazına geçersiniz.

Dikkat edin, burada “fazlar” (phases) terimini kullanıyorum. Bu çok önemli, çünkü bir fazdan diğerine geçmek için **çıkış kriterleri** ve **giriş kriterleri** vardır. Tüm gereksinimleri aldıktan sonra tasarıma geçeriz; umudumuz, gerçekten ihtiyaç duyduğumuz tüm gereksinimlere sahip olmaktır. Tasarım fazında mimarlar tasarım yapar. Bu gereksinimleri nasıl çalışan yazılıma dönüştüreceğimizi belirlerler ve tüm sistemi tasarlarlar.

Bu faz bittiğinde **kodlama (coding)** fazına geçeriz. Burası geliştiricilerin “hackety hack” kod yazdığı yerdir.

Şimdi, bunun *Waterfall* olarak adlandırıldığını ve okların aşağı doğru aktığını fark edeceksiniz; çünkü bir şelalede yukarı yüzmek gerçekten zordur. Bu yüzden uygun bir isim. Kodlama fazındayken “Bu kötü bir tasarım, çalışmıyor” diye fark ettiğinizde, geri dönüp yeniden tasarlamak çok zordur. Hatta yazılım geliştirmeyi sivil mühendislik projeleri gibi ele aldığımız için bazen o tasarımcılar bir sonraki projeye geçmiş olur ve gidip onları bulmanız gerekir. Yani şelalede yukarı yüzmek çok ama çok zordur.

Kodlamadan sonra nihayet **entegrasyon (integrate)** aşamasına geliriz. Tüm bu süre boyunca izole şekilde kod yazarız; kendi modülümü bir başkasının modülüyle entegre etmeyiz. Modüllerin bir araya geldiği bir zaman vardır. İlk kez o zaman “Bu kod parçaları birlikte çalışıyor mu?” diye anlarız.

Sonra **test (testing)** aşamasına geçeriz; çünkü artık insanların test edebileceği bir sistem vardır. Hata bulduklarında, şelalede yukarı yüzmeleri gerekir; kodlama fazında hata kaydı açıp yeniden kod yazarlar. Ve test ettikleri hatalardan biri, aslında tasarımın değişmesi gerektiğini ortaya çıkarırsa (bileşenler iyi etkileşmiyorsa), şelalenin çok ama çok yukarısındaki tasarım fazına geri dönmek gerekir; bu da çok pahalıdır.

Son olarak tüm testler bittikten sonra yazılımı **dağıtır (deploy)**ız.

---

## ⚠️ Waterfall Yaklaşımında Ne Yanlış?

Bu yaklaşımda  **değişime yer yoktur** . Her fazın giriş ve çıkış kriterleri vardır.

Biri bittiğinde, bir sonraki başlar. Tasarımı değiştirmeye, gereksinimleri değiştirmeye veya buna benzer şeylere geri dönmeye dair bir düzenleme yoktur.

Diğer sorun:  **En sona kadar çalışıp çalışmadığını bilemezsiniz** , değil mi? Ara teslimat yoktur. Son adıma kadar hiçbir şey teslim edilmez; en sonda operasyon ekibine verir ve “Bunu üretime alıp teslim edin” dersiniz.

Bir diğer konu: her adım, bir sonraki başladığında biter; bu yüzden adı şelaledir, işler aşağı doğru devredilir. Ve tabii ki her devrin kendisi, bilgi kaybetmek için bir fırsattır; kazaların yaşanması ya da insanların tıkanması (önceki fazdan gelen işi kabul edememeleri) mümkündür. Böylece bir sonraki fazın başlamasını beklemek zorunda kalırsınız.

Ayrıca hataların geç bulunması  **çok ama çok maliyetlidir** ; testte tasarımın yanlış olduğunu bulmak ve geri dönüp yeniden tasarlamak çok pahalıdır.

Son olarak, **uzun teslim süreleri** vardır. Yazılımı ilk istediğiniz andan itibaren; tasarım, kodlama, test ve nihai teslimata gelene kadar çok uzun, çok uzun, çok uzun süreler geçer.

Buradaki problem şudur: ekipler ayrı ayrı çalışır; birbirlerine etkilerinin farkında değildir. Tasarımcılar kodun etkisinin farkında değildir, kod yazanlar entegrasyonun etkisinin farkında değildir. Herkes kendi fazının “silosu” içinde çalışır.

Ve bu korkutucu bir düşünce olmalı: koda en uzak olan kişiler, zavallı operasyon ekibi, bunu üretimde çalıştırmak ve yönetmek zorundadır, değil mi? Kod hakkında en az bilgiye sahip olanlar, bunu çalıştırması beklenenlerdir. Pek verimli değil.

---

## ⚡ Extreme Programming

Başka bir metodolojiye geçelim:  *Extreme Programming* . Bu 96 yılında tanıtıldı. *Kent Beck* bunu ortaya koydu ve sağ taraftaki grafiğe bakarsanız çok iteratif olduğunu ve döngülerden bahsettiğini görürsünüz.

Dış döngüde büyük bir **release planı** vardır. Sonra bir **iteration planı** vardır. Release aylar sürebilir, iterasyonlar haftalar sürebilir, kabul (acceptance) günler sürebilir, stand-up toplantıları günde bir kez olur, pair negotiation saatler içinde, unit testing dakikalar içinde, pair programming saniyeler içinde gerçekleşir. Yani iş yapma ve hızlı geri bildirim alma döngüleri gittikçe sıkılaşır.

Bu, yazılım geliştirmeye yönelik iteratif bir yaklaşıma dayanır. Hatta Agile’ın bunu buradan aldığı söylenebilir. Amaç yazılım kalitesini artırmaktır, değil mi? Değişime duyarlı olmak, müşteri gereksinimlerine duyarlı olmak, işleri küçük artışlarla yapmak.

Bu nedenle birçok kişi  *Extreme Programming* ’i ilk Agile yöntemlerinden biri olarak kabul eder.

---

## 🧩 Extreme Programming Değerleri

İlki  **sadelik (simplicity)** . Yalnızca ihtiyacınız olanı yapın ve fazlasını yapmayın; aşırı mühendislik yapmayın, fazla kod yazmayın, müşterinin istemediği ekstra kod teslim etmeyin. Basit tutun, çok önemli.

İkincisi  **iletişim (communication)** . Ekipteki herkes iletişim kurmalıdır; herkesin ne yaptığını bilmelidir. Çok fazla iletişimi ve etkileşimi teşvik eder. Bu da çok önemlidir.

Üçüncüsü  **geri bildirim (feedback)** . Geri bildirim almıyorsanız nasıl gittiğinizi bilemezsiniz. Bu yüzden geri bildirim döngüleri *Extreme Programming* için kritik olduğu gibi, genel olarak Agile için de kritiktir.

Sonra  **saygı (respect)** . Herkes ekipte saygı gördüğünü hisseder; tavsiye verebilir, öneride bulunabilir ve önerileri ekipteki herhangi birinin önerisi kadar değerlidir. Hiyerarşi yoktur; herkes eş seviyededir ve fikirleri için saygı görür.

Son olarak  **cesaret (courage)** . Tahminlerimizi şişirmeyiz; dürüstçe “Bunu yapabiliriz, şunu yapamayız” deriz. Size şu kadar zamanda bitireceğiz diye yalan söylemeyiz.  *Extreme Programming* ’de çok açık ve dürüst olunur: bunlar tahminlerdir, bunlara taahhüt ederiz.

---

## 🧷 Kanban

Sonraki:  *Kanban* . Bu, Japon üretim sistemlerinden gelir. Kanban kelimesi “billboard sign” anlamına gelir ve üretim hattında sürekli akışla ilgilidir; kartlar veya notlar ürünle birlikte istasyondan istasyona akar.

Kanban’ın temel prensipleri şunlardır:

* **İş akışını görselleştirin (visualize the workflow).** Eğer işi göremiyorsanız, işi yönetemezsiniz. Bu, Agile’a da taşıdığımız bir şeydir. Agile’da Kanban panoları kullanacağımızı göreceksiniz.
* **Devam eden işi sınırlayın (limit the work in progress).** Üretim hattında işin bir istasyonda birikmesini istemezsiniz. Yazılım geliştirirken de insanların aynı anda çok fazla şey üzerinde çalışmasını istemezsiniz. Çünkü %100 çalışan tek bir şeyi sevk edebilirsiniz; iki şeyin %50’sini sevk edemezsiniz. Bir kişi iki şey üzerinde çalışıyorsa bu iyi değildir. Bu anlayış Kanban’dan gelir: devam eden işi sınırlamak.
* **Akışı yönetin ve geliştirin (managing and enhancing the flow).** Kanban’da sürekli iyileştirme aranır. Akışı nasıl daha iyi ve daha hızlı hale getirebiliriz, diye bakılır.
* **Politikaları açık hale getirin (making policies explicit).** Herkes süreçlerin nasıl işlediğini ve “done” tanımının ne olduğunu anlamalıdır. Bir şeyin “done” olması ne demektir? Bunu Kanban’dan alıp Agile planlamada da kullanırız.
* **Sürekli iyileştirin (continuously improving).** Geri bildirim almak ve yaptığınız işi sürekli geliştirmek çok önemlidir. Kanban; akışları daha iyi çalışır hale getirmek, onları anlamak, görmek, ölçebilmek ve daha hızlı akmak için sürekli iyileştirmekle ilgilidir.

---

## ✅ Video Özeti

Bu videoda, geleneksel *Waterfall* yaklaşımının yazılım geliştirmede yapılandırılmış, adım adım ilerleyen bir süreç olduğunu ve sorunların geliştirme sürecinin ilerleyen aşamalarına kadar ortaya çıkmayabileceğini öğrendiniz.  *Extreme Programming* , yazılım kalitesini ve değişen gereksinimlere yanıt verebilirliği artırmak için geliştirilmiştir. *XP* değerleri;  **sadelik** ,  **iletişim** ,  **geri bildirim** , **saygı** ve **cesaret**tir. *Kanban* ise iş akışını görselleştirme, devam eden işi sınırlama, akışı yönetme ve geliştirme, süreç politikalarını açık hale getirme ve süreci sürekli iyileştirme ile karakterize edilen bir sistemdir.
