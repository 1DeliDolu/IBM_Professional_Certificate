# 🎓 Kursa Giriş

Merhaba. Ben John Rofrano; IBM Research’te *DevOps Champion* ve  *Senior Technical Staff Member* ’ım ve sizi *Test Odaklı Geliştirmeye (Test-Driven Development)* ve *Davranış Odaklı Geliştirmeye (Behavior-Driven Development)* ya da **TDD** ve  **BDD** ’ye giriş kursuna hoş geldiniz demek istiyorum.

Bu kurs, kodunuzun beklendiği gibi davrandığından emin olmak için test senaryoları yazmanız adına ihtiyaç duyduğunuz becerileri size kazandıracak. Bir yazılım mühendisi olarak her gün kullandığım iş akışlarını ve teknikleri size öğreteceğim; ama bunu sadece benden duymayın. North Carolina State University Bilgisayar Bilimleri Bölümü’ndeki araştırmacılar geliştiricileri test odaklı geliştirmeyle tanıştırdı ve sonra yaklaşımla ilgili ne düşündüklerini sordu.

Sonuçlar şunlardı: **%92** TDD’nin daha yüksek kaliteli kod ürettiğine inanıyordu, **%79** TDD’nin daha basit tasarımı teşvik ettiğini düşünüyordu ve **%71** yaklaşımın gözle görülür biçimde etkili olduğunu düşünüyordu.

*Behavior-driven development* ya da  **BDD** , Cucumber’ın  *state of behavior-driven developments report* ’una göre ekip iş birliğini yeniden tanımlıyor; ekiplerin  **%74** ’ünde BDD senaryoları yazımına birden fazla rol katılıyor ve bunun sonucunda yalnızca iş birliğinde iyileşmeler değil, aynı zamanda artan yazılım kalitesi de elde ediliyor.

## 🧪 Testlerin Otomasyonu ve Paylaşılan Anlayış

Test senaryolarının  **%80** ’i otomatikleştiriliyor; tüm bunlar yapılırken kodlamadan önce ortak bir anlayış oluşturuluyor ve iş bilgisi yakalanıyor.

Bu kursta *test first* yaklaşımını benimseyeceğiz: sahip olmayı dilediğiniz kod için önce test senaryolarını yazmayı ve sonra onların geçmesini sağlayacak kodu yazmayı öğreneceğiz.

Kendi kendinize şöyle soruyor olabilirsiniz: Henüz yazmadığım kod için nasıl test senaryoları yazabilirim? O zaman ben de size şunu sormalıyım: Henüz yazmadığınız kod için nasıl tasarım dokümanı yazarsınız? Tasarım dokümanı kodun davranışını tanımlar. Benzer şekilde test senaryoları da kodun davranışını tanımlar. Hiçbir farkı yok.

## 🧭 TDD’nin Tasarımı Yönlendirmesi

TDD’yi takip etmek, testlerin tasarımı yönlendirdiği anlamına gelir.  *Extreme programming* ’in babası Kent Beck bir keresinde şöyle demişti: **TDD basit tasarımları teşvik eder ve güven ilham eder.** Buna kesinlikle katılıyorum.

Bu kurs boyunca, test odaklı geliştirme ve davranış odaklı geliştirmenin daha hızlı kod yazma konusunda size nasıl güven verebileceğine bakacağız. Kodun davranışını bozduysanız bunu hemen anlarsınız; çünkü TDD ve BDD test senaryoları bunu yakalayacaktır.

## ✅ TDD Bölümünde Öğrenecekleriniz

Kursun TDD bölümünde, kodunuzun beklendiği gibi davrandığından emin olmak için test doğrulamalarını ( *test assertions* ) nasıl yazacağınızı öğreneceksiniz.

Ayrıca, her testin diğerlerinden izole şekilde çalışması için tutarlı bir başlangıç durumu oluşturmayı sağlayan test fikstürlerini ( *test fixtures* ) nasıl kullanacağınızı öğreneceksiniz.

*Test verisini nereden bulacağım?* diye hiç merak ettiniz mi? Kendi test verinizi kolayca üretmek için *factories* ve *fakes* kullanmayı ve üretim sistemlerinden örnek test verisi kullanmayı öğreneceksiniz.

Kod kapsamı ( *code coverage* ) araçlarını nasıl kullanacağınızı öğreneceksiniz. Bu araçlar, kodun yüzde kaçının test senaryolarıyla kapsandığını keşfetmenizi ve kodun hangi satırlarında test senaryosu olmadığını belirlemenizi sağlar.

Ardından laboratuvarlarda, o ele avuca sığmaz kod satırlarının peşine birlikte düşeceğiz ve amaçlandığı gibi çalıştıklarını kanıtlamak için test senaryoları yazacağız.

Dış etkilerden bağımsız kalmaları için test senaryolarında *mocking* kullanmayı; odağınızı kendi kodunuzu test etmeye, başkasının servisini test etmemeye yönlendirmeyi öğreneceksiniz. Ayrıca hata taklitleri yaparak ( *mimic failures* ) hata yakalayıcılarınızın ( *error handlers* ) doğru çalıştığını test edebilmek için de *mocking* kullanacaksınız.

## 🧩 BDD’nin Faydaları ve İş Akışları

Sonraki adımda, daha üst seviye otomatik testler için davranış odaklı geliştirmenin ( **BDD** ) faydalarını ve iş akışlarını öğreneceksiniz.

Hem paydaşların hem de geliştirme ekiplerinin sistemin davranışını tek bir sözdiziminde tanımlamasına olanak veren *Gherkin* dilinin temellerini keşfedeceksiniz.

Sistemi, son kullanıcı perspektifinden bir dizi senaryo olarak tanımlayan *feature files* yazacaksınız.

Feature’ınızın senaryoları yazıldıktan sonra, `behave` aracıyla başlangıç Python adımlarını ( *initial Python steps* ) nasıl üreteceğinizi, iş akışını ve bu adımları nasıl uygulayacağınızı keşfedeceksiniz.

Bu kurs ayrıca  *context variable* ’ı ve Python adımlarında `behave` ile çalışırken değişken ikamesinin ( *variable substitution* ) faydalarını da kapsayacak.

## 🏗️ Final Modülü Projesi

Final modülünde, tıpkı endüstride yaptığımız gibi bir proje üzerinde çalışacaksınız. Bir e-ticaret uygulamasının ürün kataloğu arka ucu için bir mikroservis oluşturacaksınız.

Proje iki bölüme ayrılmıştır.

### 🧱 Bölüm 1: TDD ile REST API

Projenin ilk bölümünde, iyi test odaklı pratikleri kullanarak kullanıcıların ürünleri çeşitli özniteliklere göre  **oluşturmasına** ,  **okumasına** ,  **güncellemesine** , **silmesine** ve **listelemesine** olanak tanıyan bir REST API oluşturacaksınız.

### 🧪 Bölüm 2: BDD ile Yönetim Arayüzünü Test Etme

İkinci bölümde ise, sizin için sağlanan yönetici kullanıcı arayüzünün beklendiği gibi davrandığını test etmek üzere davranış odaklı geliştirme senaryoları yazacaksınız.

## 📉 Hata Sayısındaki Azalma ve Kalite Artışı

TDD ve BDD ile daha güvenilir kod inşa edersiniz. Microsoft ve IBM’i içeren bir çalışma, TDD uygulayan ürün ekiplerinde hata sayısının, TDD pratiklerini kullanmayan benzer projelere kıyasla **%40–%90** arasında azaldığı sonucuna varmıştır.

Hatalarda **%90** düşüş; bu gerçekten oldukça iyi. Daha az hatayla daha iyi kalite ve daha iyi sürdürülebilirlik.

Bundan ben de isterim. Nereye kayıt oluyoruz? Tam burada bu kursa kayıt oluyorsunuz.

Öyleyse bana katılın ve test odaklı ve davranış odaklı geliştirme hakkında her şeyi öğrenin. TDD ve BDD ile yazılım mühendisliği deneyiminizi dönüştürebilir ve kodunuzun davranışı konusunda daha fazla güven kazanabilirsiniz.

## 🧑‍🤝‍🧑 Öğrenme Süreci ve İş Birliği

Bu yüzden videoları izleyin, demoları görüntüleyin, laboratuvarlarda deneyler yapın ve bilginizi test etmek için quiz’leri çözün.

Ayrıca forumlarda akranlarınızla etkileşim kurmayı unutmayın; çünkü yazılım mühendisliği bir takım sporudur ve iş birliği teşvik edilir.

Benim söylemeyi sevdiğim bir şey var: Geliştirmenize, sahip olmayı dilediğiniz kod için test senaryoları yazarak başlarsanız, o dilek mutlaka gerçek olur.

Sınıfta görüşürüz.
