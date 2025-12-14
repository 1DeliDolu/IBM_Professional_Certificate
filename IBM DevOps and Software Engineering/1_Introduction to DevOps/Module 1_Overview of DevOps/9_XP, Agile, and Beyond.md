# 🚀 XP, Agile ve Ötesi

Bu videoyu izledikten sonra şunları yapabileceksiniz: **Extreme Programming’in Agile’ın başlangıcı olduğunu açıklamak** ve  **Agile’ı ve DevOps’un bir parçası hâline nasıl geldiğini açıklamak** .

## 🧩 Extreme Programming’in Doğuşu ve Geri Bildirim Döngüleri

1996’da Kent Beck, *Extreme Programming (XP)* ile ortaya çıktı. Kent bunu yinelemeli ( *iterative* ) bir yaklaşıma dayandırdı. Bu geri bildirim döngülerini tanımladı. Yayın ( *release* ) planları aylar sürer, yineleme ( *iteration* ) planları haftalar sürer, kabul ( *acceptance* ) planları günler sürer ve *stand-up* toplantıları her gün yapılır. Ve *pair negotiations* her saat yapılır; *unit testing* dakikalar içinde yapılır ve programlama saniyeler içinde yapılır. Bu gittikçe sıkılaşan döngüler yaklaşımı temsil eder.

Fikir, yazılım kalitesini artırmak ve hızlı geri bildirim almaktı: müşteriye bir şey sunmak, hızlıca geri bildirim almak ve sonra bunun üzerinde yineleme yapmak. Extreme programming, yazılım kalitesini ve değişen müşteri gereksinimlerine yanıt verebilirliği artırmayı amaçlıyordu.

## 👥 Eşli Programlama ve Takım İçinde Yetenek Harmanlama

*Pair programming* gibi kavramları vurguladı. Sizi *pair programming* denemeye teşvik ediyorum. Her kod satırında iki çift göz olmasını sağlar ve ekibinizi becerilerle çapraz eğitmeye yardımcı olur. Örneğin, Python’u gerçekten iyi bilen bir kişi, Python’u yeni öğrenen biriyle eşleşir. Birlikte çalışırlar ve junior programcı, senior programcının probleme nasıl yaklaştığını görür.

 *Pair programming* , ekibinizdeki becerileri harmanlamanın ve herkesin aynı kodu aynı anda anlayacak şekilde onun içinde olmasının harika bir yoludur.

Kent Beck’in *Extreme Programming* yaklaşımı, ilk Agile yöntemlerinden biriydi.

## 🏔️ Agile Manifesto’nun Ortaya Çıkışı

2001’de on yedi yazılım geliştirici, Utah’taki Snowbird’de bir tatil beldesinde bu hafif ( *lightweight* ) geliştirme yöntemlerini tartışmak için bir araya geldi. Ortaya çıkan şeye *Agile Manifesto* denir.

Agile Manifesto şunları vurguladı:  **süreçler ve araçlar yerine bireyler ve etkileşimler** ;  **kapsamlı dokümantasyon yerine çalışan yazılım** ;  **sözleşme pazarlığı yerine müşteri iş birliği** ; ve  **bir plana bağlı kalmak yerine değişime yanıt verme** . Yani, sağdaki öğelerde değer olsa da, soldaki öğelere daha fazla değer veririz.

Bu büyük bir atılımdı. İnsanlar organizasyonlarını Agile olacak şekilde değiştirmeye başladı.

## 🔁 Agile Geliştirme, Sprint’ler ve Sürekli İyileştirme

Agile geliştirmede, gereksinimler ve çözümler, kendi kendini organize eden çapraz fonksiyonlu ekipler ve müşterilerinin iş birliğine dayalı çabasıyla evrilir. Uyarlanabilir planlamayı ( *adaptive planning* ), evrimsel geliştirmeyi ( *evolutionary development* ), erken teslimatı ( *early delivery* ) ve sürekli iyileştirmeyi ( *continual improvement* ) savunur.

Ayrıca değişime hızlı ve esnek yanıtı teşvik eder. İş, *sprint* adı verilen artışlarla yapılır. Planlama uyarlanabilirdir. Önümüzdeki iki haftayı planlarız, sonra ondan sonraki iki haftayı ve sonra ondan sonraki iki haftayı. Agile, sürekli iyileştirmeyi içerir; yani ne öğrendiğinizi ve değişmek için ne yapacağınızı sormaktır.

Geliştiriciler buna sarılıyordu ve ben o zamanlar birkaç Agile ekibindeydim ve gerçekten, gerçekten çok iyi işliyordu.

## 🧱 Agile Tek Başına Yeterli Değil: Ops Gerçeği

Ama Agile olmak tüm sorunları çözmez. Hâlâ  *Ops* ’u düşünmek gerekir ve Agile, operasyonların nasıl ölçüldüğüyle doğrudan karşıt durumdaydı.

Bu kavramı gösteren bir projedeydim. Projeye Ocak’ta başladık. Şubat sonuna doğru, gerçekten deploy etmek istediğimiz kodumuz vardı. Deploy için Ops ekibine gittik ve “ticket açın” dediler. Biz de üç VM almak için ticket açtık. Birkaç gün sonra VM’leri sorduk. Bilirsiniz, VM oluşturmak yaklaşık 20 dakika sürer. Ops ekibi, “VM’yi oluşturacak 20 dakikası olan birini bulmak iki hafta sürüyor” dedi. Ticket bekledi, bekledi, bekledi ve sonra geri çevrildi. Proje Eylül’de deploy edildi ve ben projeden Aralık’ta ayrıldım. Katlanamadım.

Geliştiricilerin Agile olup sprint’lerle çalışması, sprint’lerle çalışması ve sonra Ops ekibinin bir şeyi deploy etmesini beklemesi, beklemesi, beklemesi çılgıncaydı. Agile, tek başına, yeterince iyi değildir.

## 🏎️🐢 İki Hızlı IT ve Shadow IT’nin Başlaması

Patrick Debois, Ops çalışanlarını da Agile yapmamız gerektiğini fark etti. Bu durumun sonucu *two-speed IT* olarak adlandırılır. Şöyle işler (ya da daha doğrusu... işlemez!): Bir geliştirici bazı kaynaklara ihtiyaç duyar. Ops, ona bir ticket göndermesini söyler.

Geliştirici şöyle der: “Boş ver. Buluta gideceğim.” Ve geliştirici buluta gider ve şirket içinden günlerce ticket’ı beklemek yerine kaynağı hemen alır. Bu, şirket kaynakları üzerinden gitmenin yavaş hızı ve şirket dışından kaynak almanın hızlı hızıdır.

Böylece *Shadow IT* başlar. İş biriminin bilmediği kaynaklar vardır çünkü insanlar IT biriminin etrafından dolaşır; çünkü IT onların ihtiyaçlarını karşılamıyordur. Sonra bulut bunu yapmayı çok kolaylaştırır ve her organizasyonda IT’nin hiç bilmediği bulut hesapları olan kullanıcılar bulunduğuna bahse girerim.

Bu probleme bir çözüm gerekir ve DevOps bunun bir cevabıdır.

## ✅ Video Özeti

Bu videoda şunları öğrendiniz:  *Extreme Programming* , Agile geliştirmeye giden yolu açtı ve Agile;  **bireylere değer vermeyi** ,  **iş birliğini** ,  **değişime yanıt vermeyi** ,  **uyarlanabilir planlamayı** , **erken teslimatı** ve **sürekli iyileştirmeyi** vurgular.
