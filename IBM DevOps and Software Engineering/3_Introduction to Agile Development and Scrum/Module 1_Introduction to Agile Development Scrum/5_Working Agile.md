# 🏃‍♀️ Working Agile

Bu videoyu izledikten sonra, *Agile* çalışmanın beş uygulamasını listeleyebilecek, küçük partilerle çalışmayı açıklayabilecek, *minimum viable product* (MVP) tanımlayabilecek, *behavior driven development* (BDD) anlayabilecek, *test driven development* (TDD) anlayabilecek ve  *pair programming* ’in nasıl çalıştığını açıklayabileceksiniz.

## 📦 Küçük Partilerle Çalışmak

Şimdi, *Agile* bir şekilde çalışmanın gerçekte ne anlama geldiğine bakalım. Öncelikle, küçük partilerle çalışmak istersiniz. Bunu *lean* üretimden alıyoruz. Büyük bir parti hâlinde bir şey üretmek istemezsiniz; çünkü sonra onu yanlış yaptığınızı fark ederseniz, geri dönüp değiştirmek zorunda kalmak çok fazla israf yaratır.

Şimdi, “küçük partilerle çalışma”ya bakalım—diyelim ki bin broşürü postalamam gerekiyor. Adımlar şunlar: broşürleri katlamak, broşürleri zarflara koymak, zarfları kapatmak ve son olarak zarfları pullamak.

Diyelim ki bunları 50’lik partiler hâlinde yapacağız, değil mi, büyük partiler, her seferinde 50 tane, ve her adımın tamamlanmasının yaklaşık altı saniye sürdüğünü varsayalım. Yani dakikada yaklaşık 10 adım yapabiliyorum. İlk adım olan katlamayı yapıyoruz, değil mi? Dakikada 10 olduğuna göre 50 tanesini katlamak yaklaşık beş dakika sürüyor. Sonra bir sonraki adıma geçiyorum. Bir sonraki adım hepsini zarflara yerleştirmek ve yine, dakikada yaklaşık 10 tane yapabiliyorsam, beş dakika daha sürüyor; önceki beş dakikayla birlikte. Şimdi 10 dakika içindeyim. Hepsi katlandı ve yerleştirildi; sonra üçüncü adım olan hepsini kapatmaya geçiyorum, değil mi? Yine dakikada yaklaşık 10; 50 taneyi beş dakika daha kapatabiliyorum. Böylece 15 dakikaya çıkıyorum, değil mi? Duvar saati zamanı. Ve sonra nihayet dördüncü adıma geliyorum ve ilk bitmiş ürünü elde etmem 16 dakika sürdü, değil mi?

Gerçekten inceleyebileceğim ve kalitesinin nasıl olduğuna bakabileceğim ilk ürün. Peki ya zarflarda tutkal yoksa, değil mi? Bir şeylerin ters gittiğini anlamam 11 dakika sürerdi. Broşürde bir yazım hatası varsa? En başa kadar geri dönmem gerekir, değil mi? Yani bu şekilde büyük partilerle çalışmak çok, çok israf edici.

Şimdi aynı örneğe *single piece flow* ile bakalım. Yine her adımın yaklaşık altı saniye sürdüğünü varsayalım.  *Single piece flow* ’da katlıyorum, değil mi? Zarfa koyuyorum, kapatıyorum ve pul yapıştırıyorum; ilk bitmiş ürün yaklaşık 24 saniyede ortaya çıkıyor. Artık onu inceleyebilirim, çalışıp çalışmadığına bakabilirim, düşündüğüm şey olup olmadığını görebilirim; sonra akışın geri kalanını serbest bırakırım.

Peki ya zarflarda tutkal yoksa? O zaman, uh, belki 18 saniye sonra anlardım, değil mi? Broşürde bir yazım hatası varsa, 24 saniye sonra. Dolayısıyla iki büyük partiler hâlinde çalışmamamız çok, çok önemlidir; böylece hızlı geri bildirim alabilir, yön değiştirebilir ve şunu anlayabiliriz: biliyorsunuz, farklı bir şey yapmamız gerekiyor mu—ve sonra yapmamız gereken değişiklikleri yapabiliriz.

## 🧪 Minimum Viable Product

Şimdi *minimum viable product* hakkında konuşalım. Önce ne olmadığını anlayalım; çünkü bir yanlış anlama var: *minimum viable product* sanki projenin birinci fazıymış ya da, biliyorsunuz, ilk beta gibi bir şeymiş gibi düşünülüyor. Ve değil. Bir *minimum viable product* bu değildir.

 *Minimum viable product* , bir hipotezi kanıtlamak ve öğrenme kazanmak ve anlayış kazanmak için yapabileceğiniz en asgari şeydir. Bu ikisi arasındaki fark, birincisinin tamamen teslimatla ilgili olmasıdır, değil mi? “Neyi teslim edeceğim?” Ama ikincisi tamamen öğrenmeyle ilgilidir. “Ne öğrenebilirim? Bu MVP’yi yayımlamaktan ne öğrenebilirim; geri bildirim alıp belki bir sonrakini daha da iyi yapabilir miyim?”

Bu yüzden her MVP’nin sonunda, yön değiştirip değiştirmeyeceğinize ( *pivot* ) ya da devam edip etmeyeceğinize ( *persevere* ) karar vermeniz önemlidir.

Bir örneğe bakalım. İşte araba isteyen bir müşteri için *minimum viable product* geliştiren bir ekip. İlk iterasyonda bir tekerlek teslim ediyorlar. Müşteri şöyle diyor: “Tekerlekle ne yapacağım? Bununla hiçbir şey yapamam?” “Yani, iterasyonlarla çalışıyoruz, burada çevik olmaya çalışıyoruz, değil mi? Bir sonraki iterasyonda sana biraz daha vereceğiz.” Ve ona bir şasi veriyorlar ve bu, “Tamam, bununla gerçekten hiçbir şey yapamıyorum.” Ve sonra nihayet, biliyorsunuz, ona direksiyonsuz bir araba veriyorlar ve en sonunda arabayı alıyor, değil mi? Böylece o kupeyi alıyor. O ekip,  *minimum viable product* ’ın nasıl oluşturulacağını anlamadı. Sadece iteratif geliştirme yapıyorlardı.

İkinci ekip, bir MVP oluşturmanın değerini anlıyor. İlk başta ona bir kaykay veriyorlar ve müşteri şöyle diyor: “Ben sizden araba istedim, siz bana kaykay veriyorsunuz.” “Durun, durun; biz rengi test ediyoruz. O kırmızı rengi nasıl buldunuz? İstediğiniz renk o mu?” “Evet, kırmızı fena değil ama biliyorsunuz, yönlendirmek çok zor.” “Bunu bir sonraki MVP’de düzelteceğiz.” Sonra ona yön verebilmesi için bir şey ekliyorlar ve müşteri şöyle diyor: “Tamam, yön verebilmemi sağladınız ama çok hızlı gidemiyorum. Daha iyi bir hareket ettirme şekline ihtiyacım var.” “Bunu da bir sonraki MVP’de ele alacağız.” Bir sonraki iterasyonda ona pedallar veriyorlar.

Bir noktada, müşteri o motosiklete binerken ve saçlarında rüzgârı hissederken, şöyle karar veriyor: “Ben bir üstü açık istiyorum.” İlk durumda, müşteri aylar önce tam olarak istediği şeyi aldı; çünkü sadece bir planı takip ediyorlardı. Ama ikinci durumda müşteri, tam olarak arzuladığı şeyi aldı; çünkü geliştirme ekibiyle etkileşimli şekilde çalışıyorlardı ve sonunda, biraz farklı bir şey geliştiriyorsunuz ama müşterinin gerçekten, gerçekten istediğine daha yakın oluyor.

## 🧩 Behavior Driven Development

 *Behavior driven development* , sistemi dışarıdan içeriye doğru tanımladığımız zamandır. Bu genellikle entegrasyon testi seviyesinde yapılır, değil mi? Yani BDD testi yaparken, genellikle sistemi müşteri arayüzüne karşı test edersiniz, değil mi? Müşterinin gördüğü şeye karşı test edersiniz; sistemin olması gerektiği gibi davranıp davranmadığını görmek için.

Eğer bu bir e-ticaret sistemiyse, sepetime bir şey koyduğumda istediğim gibi davranıyor mu? Sepeti bir siparişe dönüştürdüğümde istediğim gibi davranıyor mu? Gerçekten dışarıdan içeriye bir yaklaşım. Altta neler olup bittiğiyle çok fazla ilgilenmez.

Güzel olan tarafı, hem geliştiricilerin hem de paydaşların sistemi tanımlamak ve sistemin davranışı konusunda, sistemin ne yaptığı konusunda anlaşmak için kullanabileceği tek bir sözdizimi kullanmasıdır.

Şimdi o sözdizimine bakalım. Bu, BDD *feature scenarios* ile başlar. Burada şöyle derim: “Bir *role* olarak, yani bunun kim için olduğunu bilmek istiyorum. Bir fonksiyona ihtiyacım var, değil mi? Yani gerçekten ihtiyaç duyduğumuz işlevsellik nedir—böylece bir iş değeri elde edeyim?” Böylece bunun kim için olduğu bellidir. Müşteriler için mi? Sistem yöneticisi için mi, değil mi? Değeri kim alıyor, neye ihtiyaçları var ve neden ihtiyaçları var? Ve bu,  *feature file* ’ınızın başlangıcıdır.

Sonra senaryolar üzerinden geçmeye başlarsınız ve burada ortak bir sözdizimi kullanırız. *Gherkin syntax* olarak bilinir; Gherkin turşusundan gelir. Şuna benzer:

```gherkin
Given bir dizi önkoşul
When bir olay gerçekleştiğinde
Then gözlemlenebilir bir sonuç görmeliyim
```

Bu *given when-then* sözdizimini kullanarak geliştiriciler de anlayabilir, paydaşlar da anlayabilir; herkes bu ortak sözdizimini anlayabilir: Sepetimde bir şey varken ve sonra sepetimi temizlediğimde, biliyorsunuz, sepetimde hiçbir şey görmemeliyim. Dolayısıyla bu sözdiziminin bu BDD senaryolarında olması çok, çok önemlidir.

## ✅ Test Driven Development

 *Test-driven development* , sistemi içeriden dışarıya doğru test etmektir.  *Behavior-driven development* ’ın aksine. Sistemin iç kısımlarıyla, tekil modüllerle ilgilenir. Buna genellikle *unit testing* denir, değil mi? Ve bu, unit test senaryosu güdümlüdür; küçük bir modül seviyesinde “bu girdileri verdiğimde bu çıktıları alıyorum”dan emin olmak isteriz.

Hepsini bir araya koyduğumda istediğim davranışı elde edip etmeyeceğimi bilmiyorum. Bu, BDD’nin konusu. Ama TDD için, *test driven development* için, ben sadece sistemi en alttaki birim seviyesinde test ediyorum. Bu yüzden, sahip olmayı dilediğiniz kod için önce bir test senaryosu yazarsınız, sonra o test senaryosunun geçmesi için yeterli kod yazarsınız ve sonra baştan başlarsınız ve yeniden düzenlersiniz ( *refactor* ).

İş akışı şuna benzer: Bir test senaryosu yazarım. “Kodu yazmadan önce test senaryosu mu yazıyorsun?” diyebilirsiniz. Evet; bu beni, kodun ne yapması gerektiğine odaklı tutar. Bunu çağırdığımda, bunu nasıl çağırmak istiyorum? Hangi parametreleri geçmek istiyorum ve sonra bu bana ne yapıyor? Bu yüzden önce test senaryosunu yazarsınız, sonra o test senaryosunun geçmesi için yeterli kod yazarsınız, sonra geçince kodu yeniden düzenleyebilirsiniz; çünkü artık sizi dürüst tutacak test senaryolarınız vardır, bir şeyi bozup bozmadığınızı bilirsiniz.

Şimdi, test senaryosu çalıştığında ve başarısız olduğunda genellikle kırmızıya döndüğü ve doğru çalıştığında yeşile döndüğü için, buna *Red, Green, Refactor* demeye eğilimliyiz. Bir test senaryosunu izle: bir test senaryosu yaz, başarısız olduğunu izle, geçmesi için sadece yeterli kod yaz, sonra yeniden düzenle—geçmesi için belki çok zarif yapmamış olabilirsin—şimdi geri dönüp her türlü hata kontrolünü falan ekleyebilirsin, biraz daha, uh, sağlam yapabilirsin ve sonra test senaryolarını çalıştırırsın. Hiçbir şeyi bozmadığından emin olursun.

## 👥 Pair Programming

 *Pair programming* .  *Pair programming* , iki programcının birlikte aynı şey üzerinde çalışmasıdır, uh, ve ilk tepki şudur: “Bir işi yapmak için iki kişiye para mı ödüyorum?” Ama aslında gerçekten çok, çok iyi çalışır; çünkü yaptığınız şey şudur: bir kişi kod yazar, sonra başka bir kişi koda bakan ikinci bir göz olur.

Soru şudur: Hataları üretimde mi bulmak istersiniz? Hataları kodu yazarken mi bulmak istersiniz? Kodu yazarken bulmak çok daha ucuzdur; dolayısıyla iki göz, birbirlerini kontrol ederler ve gidip gelirler. Sadece biri ve sonra diğeri değildir.

Genellikle 20 dakikalık artışlarla, değil mi? Birisi kod yazıyor, diğeri izliyor ve sadece izlemiyor. Bazen bir şeylere bakıyorlar, bazen tartışıyorlar. “Sence bu değişkene ne ad vermeliyim? Sence bu fonksiyona ne ad vermeliyim?” Değil mi? Bu kodun etrafında çalışan iki zihin seti var ve olan şey şu: günün sonunda aslında daha yüksek kaliteli kod elde ediyorsunuz, değil mi? Kod kalitesi artıyor çünkü iki kişi onu zaten kontrol etmiş oluyor ve bu yüzden, “Bir parça kod yazmak için iki kişiye para ödeyemem” dediğinizde… İki kişiye bunun için para ödememeyi göze alamazsınız; çünkü kodu yazmak işin ucuz kısmıdır. Hata ayıklamak, üretimde bakımını yapmak, pahalı olan kısım odur ve bu yüzden pahalı kısmın ucuzlamasını istiyorsanız programcılarınızın *pair programming* yapmasını istersiniz.

Ayrıca kıdemli bir programcıyı genç bir programcıyla eşleştirmek de çok iyidir. Böylece genç programcılar şunu görebilir: Kıdemli programcı probleme nasıl yaklaşıyor? Ve böylece öğrenirler, mentorluk alırlar; kıdemli programcı da genç kişinin nasıl gittiğini görebilir.

Ya da koda aşina olmayan kişileri, koda aşina olan biriyle çalıştırırsınız. Şimdi daha fazla insan kodu öğreniyor; çünkü oradalar ve diğer kişiden adeta bir eğitim alıyorlar. Bu yüzden  *pair programming* , ekibinizdeki tüm insanları belirli bir seviyeye getirmenin gerçekten, gerçekten harika bir yoludur.

## 🧾 Video Özeti

Bu videoda, küçük partilerle çalışmanın hızlıca faydalı bir şey teslim etmek anlamına geldiğini, bir  *MVP* ’nin hipotezi test etmek ve öğrenmek için yapabileceğiniz en ucuz, en kolay şey olduğunu öğrendiniz.  *Behavior driven development* , doğru şeyi inşa ettiğinizden emin olur. Ve  *test driven development* , şeyi doğru şekilde inşa ettiğinizden emin olur.

*Pair programming* ise kusurları daha erken keşfetmenizi ve kod kalitenizi artırmanızı sağlar.
