# 🚀 DevOps Benimsenmesi

Bu videoyu izledikten sonra şunları yapabileceksiniz: Büyük şirketlerin DevOps’u nasıl benimsediğini tanımlamak ve DevOps’un kültürel bir değişim gerektirdiğini fark etmek. DevOps tamamen farklı bir zihniyet gerektirir; bu yüzden önce öğrendiklerinizi unutmanız gerekir. DevOps kültürünü gerçekten benimsemek için mevcut kültürünüzü unutmanız gerekir. Bunu söylemesi yapmaktan daha kolaydır.

Kurumsal kültüre gömülü olmayan, startup olan şirketler için bu daha kolaydır. Yeni startup’lar yeni bir kültürle başlar, ancak büyük kurumsal işletmeler öğrendiklerini unutmak ve yollarını değiştirmek zorundadır. Bunu yapmak son derece zordur.

---

## 💥 Hızlı Başarısız Olma ve Hızlı Geri Alma

Ama şunu düşünün: Ya hızlı başarısız olabilseydiniz ve hızlıca geri alabilseydiniz? Bir değişikliğin  *blast radius* ’ünü (etki alanını) sınırlayabilirdiniz. Üretime bir şey çıkarabilir ve ters giderse, o değişikliğin etki alanını sınırlayarak tüm sistemi çökertmesini engelleyebilirdiniz.

Ya “ikinci kez düşünmek” ve analiz etmek yerine pazarda test edebilseydiniz? Şirketler bunu sürekli yapar. A/B testleri yaparlar ve siz arkadaşınıza şöyle dersiniz: “Hey, web sitesindeki o widget’ı gördün mü? Şuna tıklıyorsun ve o...”

Arkadaşınız da size şöyle bakar: “Neyden bahsediyorsun?” Arkadaşınız onu görmedi; hiçbir widget görmedi. Görmemesinin sebebi sitenin A/B test yapmasıdır. Siz A grubundaydınız, o B grubundaydı. O yeni widget’ı görmedi. Şirketler müşterilerinin bir alt kümesini alıp onlara yeni bir şey gösterir ve herkes üzerinde denemek yerine nasıl tepki verdiklerine bakar. Bu pazarda test etmektir ve çok ama çok güçlü olabilir.

---

## 🧩 Mikroservislerle Parça Parça Değişim

Ya uygulama tasarımınız tek tek bileşenleri değiştirip yer değiştirebileceğiniz bir yapıda olsaydı? Büyük “big bang” sürümleri olmazdı. Spotify gibi uygulamalar bu şekilde tasarlanmıştır. Spotify tek bir büyük monolitik uygulama değildir. Bir sürü küçük mikroservisten oluşur.

Bir öneri motorları vardır; uygulamada görünen bir mikroservistir. Yeni bir öneri algoritmasını devreye almak isterlerse, o ekip diğer uygulama parçalarını etkilemeden yeni öneriyi yayına alabilir. Tamamen saçma öneriler yapabilir ama tüm Spotify hizmetini çökertmez. Sadece biraz tuhaf görünen öneriler alırsınız; müziğinizi dinlemeye devam edersiniz. Ne önemi var? Bunlar pazarda hızlı hareket etmenizi sağlayan şeylerdir.

---

## 🎤 Flickr ve “Günde 10+ Dağıtım”

2009’da Velocity konferansında bu, pek çok kişinin gözünü açtı. John Allspaw ve Paul Hammond, Velocity 2009 konferansında artık meşhur olan “10+ Deploys per day – Dev and Ops Cooperation at Flickr” başlıklı sunumlarını yaptı. Allspaw o sırada Flickr’daydı ve günde 10 dağıtım yaptıklarını anlattı; insanların kafası yandı — günde 10 dağıtım!

İnsanlar altı ayda bir dağıtım çıkarabilseler bile mutlu oluyordu. Ama Flickr’ın tamamını günde 10 kez dağıtmıyorlardı. İnsanlar bunu ilk başta fark etmedi. Farklı bir uygulama tasarımları vardı. Küçük parçaları dağıtıyorlardı.

Bu, Dev ve Ops birlikte çalışırsa, Ops’un Dev için bir kapı bekçisi olması yerine birlikte hareket edip değişiklikleri dışarı çıkarabileceği ihtimaline insanların gözünü açtı. O konuşmada, son bir haftada Flickr’da 18 kişi tarafından 496 değişiklikten 67 dağıtım yapıldığını söylediler.

Ve bu, Aralık 2008’deydi.

---

## 🛍️ Etsy: Ayda 517 Dağıtım

Ocak 2011’de Etsy, o ay üretime 517 kez dağıtım yaptıklarından bahsetti. Aslında söyledikleri şuydu: Ocak 2011’de, bir ay içinde bir milyardan fazla görüntülenmeleri vardı, kodları 76 farklı kişi tarafından commit edildi ve üretime toplam 517 kez dağıtıldı.

Ben de basit bir “arka yüz hesap” hesabı yaptım ve yaklaşık her 25 dakikada bir dağıtım yaptıklarını tahmin ettim. İnsanlar buna bakıp “Bunu nasıl yapıyorlar?” diyordu. Chad Dickerson Etsy’nin Chief Technical Officer’ıydı. Etsy’nin dağıtım ortamının; ekipler arasında yüksek düzeyde güven, şeffaflık, iletişim ve disiplin gerektirdiğini söyledi.

Kendisi ve ekipleri ortak bir hedef için birlikte çalışıyordu; silo’larda birbirlerine karşı çalışmıyorlardı.

---

## 🦄 “Unicorn” Sanılan Şirketlerden Kurumsala

Bunların efsane şirketler olduğunu düşünebilirsiniz, değil mi? Bunlar parıl parıl “unicorn”lar. Büyük bir kurumsal yapıda bunu asla yapamazsınız. İmkânsız. Kurumsallar bu kadar hızlı değişemez, bu kadar hızlı hareket edemez. Yapamazlar.

Olmaz.

Sonra 2016’da, 1.300 katılımcılı DevOps Enterprise Summit’te IT Revolution’dan Gene Kim (The Phoenix Project yazarı), sektörün nerede durduğunu ve kurumsalda DevOps benimsenmesini neyin tetiklediğini anlatmaya başladı.

Ticketmaster, Nordstrom, Target, USAA, ING gibi büyük şirketler vardı. Büyük perakende şirketleri, sigorta şirketleri, bankalar… sahneye çıkıp DevOps’u övüyorlardı. Bu, diğer kurumsalların DevOps’un sadece startup’lara özel olmadığını fark etmeye başladığı andı. Büyük kurumsallarda da işe yarıyordu.

Ticketmaster, ortalama toparlanma süresinde %98 azalma olduğunu söyledi. Geleneksel IT, *mean time to failure* ile ölçülür; ama DevOps tamamen *mean time to recovery* ile ilgilidir. Bir şeyler bozulacak. Soru, ne kadar hızlı toparlanabildiğinizdir.

Nordstrom %20 daha kısa lead time’lar elde etmişti. Target’ta full stack deploy üç aydan dakikalara indi. Elbette çok fazla otomasyon yaptılar. Bazen o üç ayın tamamı iş değildir.

Bazen o üç ay, bir change review board’un önüne çıkmak zorunda olmanızdır ve onlar sadece her ayın ilk Salı günü toplanır; bugün de o Salı’dan sonraki Çarşamba ise, bir sonraki ayı beklemek zorunda kalırsınız. Büyük şirketler böyle çalışır. Daha hızlı hareket etmek istiyorsanız, o bariyerleri yıkmanız ve değişiklikleri daha hızlı itmeniz gerekir.

USAA sürümleri 28 günden 7 güne indi. Bu oldukça iyi: bir aydan bir haftaya. ING’de DevOps yapan 500 uygulama ekibi var. CSG, release başına 200 incident’tan 18’e indi.

Bu inanılmaz. Bunlar 2016’da DevOps Enterprise Summit’te DevOps’u öven büyük şirketlerdi. İnsanlar fark etmeye başlamıştı. Artık sadece unicorn’lar değildi.

---

## 🧠 “Sihirli Araç mı?” Hayır: Kültür

Peki bunu nasıl yapıyorlar? Sırları ne? Sihirli bir araç mı? ...ve onu nereden satın alabilirim?

Hayır! DevOps kültürünü benimsediler. Satın aldıkları bir araç değil. Takip ettikleri bir prosedür değil. Şirketlerinin kültürünü gerçekten değiştirdiler; bunu yapmak çok zor ama DevOps’un sunduğu avantajları elde etmek için gerekli.

Şirketinizin kültürünü değiştirmediğiniz sürece DevOps’u denemede başarısız olursunuz, çünkü DevOps araçlarla ilgili değildir. DevOps; güven, şeffaflık, iletişim, koordinasyon ve disiplinle ilgilidir.

“DevOps’u kutudan çıkarıp satın alamazsınız.”

---

## ✅ Bu Videoda Öğrendikleriniz

* 2009’da John Allspaw’ın “10+ Deploys per Day – DevOps at Flickr” konuşmasının etkisi.
* DevOps’un ekipler arasında güven, şeffaflık ve disiplin gerektiren bir kültürel değişim olduğu.
