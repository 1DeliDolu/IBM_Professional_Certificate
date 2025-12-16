# 🧪 Testin Önemi

Bu videoyu izledikten sonra testin önemini açıklayabileceksiniz. AgileData.org’da, Agile geliştirme konusunda otorite olan yazılım mühendisi ve yazar Scott Ambler’a ait bir alıntı okudum. Şöyle dedi: *Eğer inşa etmeye değerse, test etmeye değerdir. Test etmeye değmiyorsa, onun üzerinde çalışarak neden zamanınızı boşa harcıyorsunuz?* Bunu düşündüğünüzde, bir şeyi test etmezseniz çalıştığını nasıl bilirsiniz?

Test etmek önemlidir ve otomatik test, *DevOps* için kritiktir. Bu, *continuous integration* ve *continuous delivery* hatlarınızı ( *pipelines* ) kurmakla ve üretime otomatik olarak dağıtmak üzere olduğumuz kodu test edebildiğimizden emin olmakla ilgilidir.

*Test-driven development* ve *behavior-driven development* gibi metodolojiler, sizi istemci deneyimine odaklı tutar. Yani kodunuzu çağıracak kişi; sahip oldukları gereksinimler, onu çağırmak için kullanacakları araçlar ve onlara geri verdiğiniz şeyden beklentileri. Tek bir satır kod bile yazmadan önce tüm bu yönlere odaklanırsınız. Ama kendimden önce gidiyorum.

---

## 🎯 Ne Test Edileceğini Nasıl Bilirsiniz?

Şuna odaklanmak istiyorum: Ne test edeceğinizi nasıl bilirsiniz?

Bu kadının kim olduğunu ve yanında durduğu kâğıt yığınının ne olduğunu biliyor musunuz? Eğer tahmin ettiyseniz, bu NASA’daki o kadın.

Haklısınız, bu  **Margaret Hamilton** . O kâğıt yığınları, **1969’daki NASA Apollo 11 görevinin Apollo guidance software’ının** kod çıktısıdır. Aslında o kâğıt yığını birkaç kopyadır. Çünkü 1969’da internet yoktu, *stack overflow* yoktu, GitHub yoktu. Ekipteki herkesin masasının yanında kodun bir çıktısı vardı ve fotoğraf daha etkileyici görünsün diye ekip, herkesin kopyalarını üst üste yığdı. Bu inanılmaz yazılımın sadece tek bir kopyası olsaydı bile etkilenirdim. Bu kadar müthiş.

---

## 👩‍💻 Margaret Hamilton ve Yazılım Mühendisliği

Margaret; Amerikalı bir bilgisayar bilimci, sistem mühendisi ve işletme sahibidir. NASA Apollo programı için gemideki yönlendirme yazılımını geliştirdikleri dönemde MIT Instrumentation Laboratory’de yazılım mühendisliği bölümünün direktörüydü.

1969’da insanları ilk kez Ay’a indiren yazılımdan sorumlu ekibe liderlik etti. Daha da önemlisi, *software engineering* terimini ortaya atan ve kavramı popülerleştiren kişilerden biri olarak anılır. Üzgünüm arkadaşlar, ilk yazılım mühendisi bir kadındı ve aynı zamanda son derece parlak bir kadındı.

Ondan önce, yazılım mühendisliği diye bir alan yoktu. Bilgisayarlar ve bilgisayarlaştırma çağında, bilgisayarlar için yazılım yazarken, kendisi ve ekibi çok temel bazı yazılım mühendisliği tasarım prensiplerini geliştirmek zorundaydı; çünkü bunlar mevcut değildi.

Apollo guidance system yazılımı için kendisinin ve ekibinin oluşturduğu tasarım prensiplerini sizinle paylaşmak istiyorum; çünkü bugün hâlâ geçerliler. Tahmin edebileceğiniz gibi, bir insanı Ay’a indirebilecek kadar sağlam bir yazılım üretmek için her ihtimali test etmeleri gerekiyordu.

---

## 🧱 Apollo Guidance System Tasarım Prensipleri

### 🗣️ Yüksek Seviyeli Dil Kullanın

İlk prensip? Yüksek seviyeli bir dil kullanın. O dönemde programlama çoğunlukla *machine language* ile yapılıyordu ve bu hem çok düşük seviyeliydi hem de bilgisayar mimarisine özeldi.

Margaret’in ekibi, cebirsel formülleri ifade edebilen daha yüksek seviyeli bir dil kullanmanın, yörünge hesaplamalarını daha kolay ve daha az hataya açık hâle getirdiğini fark etti.

### 🧩 İşlere Bölün

Sonraki prensip, işleri bölmektir. Apollo bilgisayarının belleği sınırlıydı ve tüm yazılım komutları aynı anda belleğe yüklenemiyordu; bu yüzden yazılımı daha küçük işlere böldüler.

Astronotlar, görevin farklı aşamalarında bilgisayarın tuş takımından bir *verb* ve bir *noun* girerek birçok küçük işi yüklemek zorundaydı.

Biz de bugün yazılımı hâlâ böleriz; kodumuzu ana rutinler ( *main routines* ), alt rutinler ( *subroutines* ) ve makrolara ( *macros* ) ayırırız.

### 🔄 Hata Durumunda Yeniden Başlatın

Ekip şunu öğrendi: Bir iş ( *job* ) başarısız olduğunda, işin içinde bulunduğu duruma artık güvenemezlerdi. Bu yüzden bir sonraki prensibi geliştirdiler: Hata durumunda yeniden başlatın.

Bir iş başarısız olursa, neyin yanlış gittiğini bulmaya çalışmazlardı. Sadece işi en baştan yeniden başlatırlardı. Biz de bunu bugün Kubernetes gibi modern sistemlerde yapıyoruz; bir container başarısız olursa, onu basitçe yeniden başlatıyoruz.

Bunun yeni bir şey olduğunu sanıyoruz ama Apollo guidance system bunu 1969’da yapıyordu.

### 📍 İyi Durumu Checkpoint Edin

Bir işi başlatmak pahalı olabilir ve o ana kadar yapılan tüm hesaplamaları kaybedersiniz; bu yüzden bir sonraki prensip bu sorunu çözer: İyi durumu checkpoint edin.

Bu, iyi bir hesaplama elde ettiğinizde onu checkpoint etmek veya bir yere kaydetmek demektir. Böylece iş yeniden başlamak zorunda kalırsa, son checkpoint’ten başlar ve tüm telemetry’yi yeniden hesaplamak zorunda kalmaz. Son checkpoint’ten devam eder.

Bugün container’larla çalışırken onların *stateless* olmasını ve tüm durumun ( *state* ) harici depolamada saklanmasını öneririz. Böylece bir container yeniden başlatılmak zorunda kalırsa, kaldığı yerden devam edebilir. Ve tüm bunlar Apollo’dan geldi.

### 🧷 Donanım Yazılımı İzler

Bir sonraki tasarım prensibi: Donanım yazılımı izler. O dönem *cooperative multitasking* kullanıyorlardı; yani yazılımın bir sonraki iş için CPU kontrolünü bırakması gerekiyordu.

Tahmin edebileceğiniz gibi, takılı kalan bir iş ( *hung job* ) tüm sistemi kilitleyebilirdi; bu sorunu önlemek için donanımı yazılımı izleyecek şekilde tasarladılar.

Bugün *preemptive multitasking* sistemlerimiz var; bu da bu sorunun büyük kısmını çözüyor; büyük ölçüde aynı şekilde.

### 📡 Telemetry Gönderin

Son prensip telemetry göndermektir. Belki ünlü  **1202 program restart alarm** ’ını duymuşsunuzdur. Bu alarm, Ay modülünün Ay’a inişini iptal ettirecek kadar ciddi bir riske yol açmıştı.

Houston’daki Mission Control bu alarmın neden olduğundan emin değildi; ancak telemetry verisi Houston’a akmaya devam ettiği için, Ay modülünün hâlâ doğru uçuş yörüngesinde olduğunu belirleyebildiler ve inişe devam etmenin güvenli olduğuna karar verdiler.

Bugün de yazılımlarımızdan log’ları akıtıyor, gerçek zamanlı metrikler topluyor ve çalışma zamanında neler olduğunu anlıyoruz; tıpkı Apollo programında yıllar önce yaptıkları gibi. Her şeyin eskisi yenidir.

Bu tasarım prensipleri zamanın testinden geçti ve Apollo guidance computer’ın her görevde kusursuz çalışmasını sağladı.

---

## 🚨 1202 Alarmı ve “Sadece Bildiğini Test Edebilirsin”

Şimdi kendinize soruyor olabilirsiniz: Apollo guidance system’dan ve elbette test-driven development’tan neden bahsediyoruz?

Dünyadaki tüm tasarım prensipleri, sadece bildiğiniz şeyleri test edebileceğiniz gerçeğini asla telafi edemez.

Astronotların Ay inişini iptal etmelerine neredeyse neden olan 1202 program restart alarmını hatırlıyor musunuz? Bu alarm, bir değil, iki öngörülemez olayın sonucuydu.

Ekranda bilgisayar arayüzünün bir sanatçı çizimi var. Buna *diskie* deniyordu ve astronotlar komutları bilgisayara girmek için tuşlayarak giriyorlardı.

Apollo bilgisayarı aynı anda sadece yedi iş çalıştırabiliyordu ve bu bellek kapasitesinin yaklaşık %80’ini kullanıyordu.

İlk öngörülemez olay, Ay’dan ayrılana kadar çalışması gereken  *rendezvous radar* ’ının arızalanmasıydı. Radarı yanlış zamanda etkinleştiren bir donanım hatası vardı; bu da sisteme ekstra %15 yük bindirdi. Sistem yükü artık %95’ti ve hâlâ çalışıyordu.

İkinci öngörülemez olay, Buzz Aldrin’in sistem durumunu almak için ekstra bir iş çalıştırmasıydı. *Verb 16, noun 68* girdi; bu sekizinci işi ekledi ve bilgisayara %10 daha yük bindirdi; bu da sistemi, tahmin ettiğiniz gibi,  *restart on failure* ’a zorladı.

İlk seferinde oldu ve bilgisayar toparlandı. Buzz tekrar çalıştırdı çünkü bilgisini istiyordu. 1202 alarmı tekrar oldu. Üçüncü kez çalıştırdıktan sonra, her *verb 16, noun 68* girdiğinde 1202 alarmının çıktığını ve sistemin yeniden başladığını fark etti. Böylece jeton düştü ve Ay’a iniş yapana kadar onu çalıştırmayı bıraktı.

---

## 🧷 Test Etmenin Kritik Dersi

Yazılımı debug etmek ve test etmek böyledir. Kimse, bir donanım hatasının rendezvous radar’ını erken başlatacağını ya da Buzz’ın Ay’a iniş sırasında ekstra bir iş çalıştıracağını asla öngöremezdi.

Ama ikisi birden oldu; bu yüzden karmaşık sistemlerin etkileşimlerini tahmin etmek zordur.

Testle ilgili önemli ders şudur: Yazılımı sadece düzeltmezsiniz. Hatayı yeniden üreten bir test senaryosu yazarsınız ve sonra yazılımı düzeltirsiniz.

Zamanla, daha fazla ve daha fazla test senaryosu bildikçe, sistem hatalara karşı daha dayanıklı hâle gelir.

Bu videoda şunu öğrendiniz: Bir yazılımın çalıştığını bilmek için onu test etmeniz gerekir. Test etmek, hatalara karşı daha sağlam ve daha dirençli bir sisteme götürür. Sadece bildiğiniz şeyleri test edebilirsiniz.
