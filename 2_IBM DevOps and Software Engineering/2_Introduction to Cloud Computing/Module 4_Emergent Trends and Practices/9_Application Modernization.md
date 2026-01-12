# 🚀 Application Modernization

Birçok kuruluş, genellikle eski sistemlerde *izole* edilmiş ve güncellenmesi ile bakımı çok zor ve pahalı olan mevcut uygulamalara büyük yatırımlar yapmıştır. Bu uygulamaları modernleştirmek, bu kuruluşlar için büyük faydalar sağlayabilir; örneğin dijital dönüşümlerini hızlandırmak, yeni teknolojilerden ve hizmetlerden yararlanmalarını sağlamak ve müşterilerinin ihtiyaçlarına ve değişen pazar dinamiklerine daha hızlı yanıt verebilmelerini mümkün kılmak.

Bulut bilişim, Uygulama Modernizasyonu’nun üç ana bileşeninden biridir. Bu videonun geri kalanında bunun nasıl olduğunu ve Uygulama Modernizasyonu’nun başka neleri içerdiğini göreceğiz.

Ben IBM Cloud’dan Eric Minick ve uygulama modernizasyonu ile birlikte gerçekleşen üç büyük dönüşüm hakkında konuşmak istiyorum. Üç şey aynı anda oluyor; bunlar birbiriyle ilişkili ve mimariyi, altyapıyı ve çalışma biçimlerimizi — yani teslim etme şeklimizi — nasıl yaptığımızdaki bu değişimi görüyoruz.

## 🏗️ Geçmişten Bugüne Mimari ve Teslimat Yaklaşımı

Biraz geçmişe gidersek, çok *monolitik* olan uygulamalar görürdük; bunlar fiziksel sunucularda çalışırdı ve *waterfall* tarzı geliştirme kullanırdık. Uzun planlarımız olurdu ve “tamam, bu bizim planlama aşamamız, geliştirme aşamamız, test aşamamız” derdik ve bir yılı proje olarak planlayabilirdik.

Ve aslında artık uzaklaştığımız şey de bu.

## 🧩 Bugünün Durumu

Bugün çoğu kuruluşun nasıl çalıştığına bakarsak, mimari olarak bir tür *dağıtık mimari*ye sahipler. Bu genellikle *service-oriented architecture (SOA)* ile ilişkilidir; birkaç yıl önceki büyük popüler terimlerdi, ama bir tür dağıtık mimari: birbirleriyle konuşan bir sürü web servisi var, arka uçta bazı veritabanları var ve sonra bütün bunların üzerinden geçen bazı ön uçlar var.

Altyapı seviyesinde ise bir tür *virtual machine* üzerinde çalışıyorlar, tamam mı? Yani dedik ki: her yeni servisimiz olduğunda yeni bir sunucu sipariş etmek zorunda kalmaktan daha iyisini yapabiliriz. Bu işleri sanallaştıralım ve yol boyunca biraz daha fazla yoğunluk elde edelim.

Çalışma biçimi açısından; biliyorsunuz, *Agile development* oldukça normal — ve sonra aşağı akışta neler olduğuna dair birazını anlamaya çalışmak.

Bu bizi birçok ekibin bugün bulunduğu noktaya getiriyor, ama aslında gittikleri yere değil.

## 🔬 Sonraki Aşama: Microservices + Cloud + DevOps

O yüzden bir sonraki faza bakarsak: bu  *service-oriented architecture* ’a bir kez daha dönüyoruz ve sahip olduğumuz daha dinamik altyapıdan yararlanarak servislerin boyutlarını gerçekten küçültüyoruz. Ve bunlara şimdi *microservices* diyoruz, değil mi? *Microservices.*

Yani bir  *microservice architecture* ’ımız var: çok küçük, çok odaklı servisler; SOA’da gördüğümüz ağır *XML-based* iletişimden uzaklaşıp daha çok *REST-based* iletişime ve buna benzer şeylere yöneliyoruz.

Ama fikir aynı: parçaları daha küçük ve daha küçük hale getirmeye devam edelim.

## 🧱 Bağımsızlık ve Teslimat Disiplini

Gönderdiğimiz şeylerde daha fazla bağımsızlığımız var. “Bu servis başka bir servisten bağımsız olmak zorunda” demekte daha fazla disiplin; böylece bu şeyleri tek başlarına değiştirebilirim.

## ☁️ Altyapı: Cloud

Altyapı tarafında: *Cloud.* Bulut oldukça popüler. Bu *public cloud* da olabilir, *private cloud* da olabilir. Burada “cloud” derken çok geniş bir çerçeveden bahsediyorum.

## 🛠️ Çalışma Biçimi: DevOps ve SRE

Teslimat, yani çalışma biçimi açısından:  *DevOps* ’un gerçekten kilit olduğunu söyleyebiliriz.

Ve bunun içine *site reliability engineering (SRE)* gibi yaklaşımları da dahil ederim. Daha çok bugün sahip olduğumuz çalışma biçimleri.

## 🔗 Bu Üçü Birbirine Nasıl Bağlanıyor?

Şimdi bunlar tamam, ilginç. Peki bunların birbirleriyle ne ilgisi var?

Ben şunu iddia ediyorum: aslında gördüğümüz şey, uygulamaların nasıl teslim edildiğinde ve nasıl inşa edildiğinde — ve ne olduklarında — bir modernizasyondur.

Bugün herhangi bir büyük kuruluşa giderseniz “Biz bir bulut dönüşümünden geçiyoruz” diyen birini bulursunuz. Sık sık “Evet, DevOps dönüşümüne liderlik etmekten ben sorumluyum” diyen birini de bulursunuz.

Kurumsal mimariye gidersiniz, “Evet, microservice mimarilerini zorluyoruz” derler.

Bireyler üç ayrı dönüşümden geçtiklerini düşünürler. Ama bunlar gerçekten birbirine bağlı. Değil mi?

## ⛔ Ayrı Ayrı Yapılırsa Neden İşe Yaramıyor?

Eğer microservices yapıyorsam ve sürekli yeni microservice’lerim oluyorsa… ve yeni bir microservice’i ayağa kaldırmak için burada şunu yapmak zorundaysam: yeni bir fiziksel sunucu sipariş etmek ve sonra onu birkaç ay sonra rack and stack yapmak…

Hiçbir *time-to-market* faydası elde edemem.

Microservices’lardan normalde bekleyeceğim dayanıklılık ( *resilience* ) faydaları da en iyi ihtimalle mütevazı olur.

 *Microservices* , bulut altyapısı ister. Yeni bir microservice’im var; onu bir container’a koyayım ve o container’ı hemen şimdi çalıştırıp dinamik olarak ölçekleyeyim diyebilmek istersiniz.

Benzer şekilde, *cloud* da microservices çalıştırmayı sever.

## 📈 Ölçeklenebilirlik Faydası Nerede Parlıyor?

Dinamik ölçekleyebilmenin faydaları, az sayıda ya da çok sayıda gerekebilecek birçok küçük şeyiniz olduğunda gerçekten harika. Dağıtık bile olmayan bir monolitiniz olduğunda ise o kadar ilginç değil. Onu nasıl ölçeklerim? Daha büyük bir bulut sunucusu alırım?

## ⚙️ DevOps’un Birleştirici Rolü

Ve bütün bunlar, hız ve dayanıklılık fikrini yerleştiriyor; *DevOps* da bunu bir araya getiriyor.

Her zaman hız isteyen geliştiriciler, her zaman dayanıklılık isteyen operasyon ekipleri… Bulutu programlıyor olacaklar. Değil mi?

Bulutun sağladığı  *programmable infrastructure* , dayanıklılığı anlayan operasyon insanlarına ihtiyaç duyar — ama biraz da geliştirme becerisi getirmelerini ister.

Ve bu yeni altyapılardan, yeni mimarilerden gerçekten yararlanmak için bu yeni çalışma biçimlerine ihtiyacınız var.

## 🧭 Planlama ve İzleme: Eski Yöntemle Olmaz

Ayrıca şunu da söyleyeceksiniz: “Eğer bu bana *time-to-market* faydası verecekse, burada geride kalıp ‘Evet, bir yıllık bir proje planımız var ve bunu sadece uygulayacağız’ diyemem.”

Planlamada ve işin gereksinimlerine yanıt verme biçimimde daha çevik olmam, daha adapte olabilmem gerekiyor.

Uygulamalarımı daha kolay izlenebilir ve daha dayanıklı olacak şekilde daha iyi birbirine bağlamam gerekiyor. Uygulamanın, bu servislerden birinin arızalandığını bildiği ve bir yenisini ayağa kaldırabildiği bir yapıda olması gerekiyor.

## 🔄 Üç Dönüşüm Birlikte Yapılır

Bu bana gerçekten büyüleyici geliyor: bu kuruluşlara gittiğinizde her yerde, bu üç farklı dönüşümü aynı anda yaşıyorlar. Ama onları her zaman birlikte yapıyorlar. Ve yapmadıklarında — pek çalışmıyor.

Yani aynı anda üç dönüşüm var. Ve bizi sık sık *application modernization* hakkında konuşurken duyarsınız. Burada en üstte yazdığını görüyor musunuz?

Ben uygulama modernizasyonunu düşündüğümde, bunun sadece bu olduğunu düşünüyorum. Tam olarak bu dönüşüm: bu tür monolitlerden ya da  *service-oriented architectures* ’tan  *microservices* ’a geçmek;  *Cloud* ’u benimsemek; çalışma biçimlerimizi *DevOps* ve  *SRE* ’ye doğru modernleştirmek.

Bu *AppMod.* Gerçekten heyecan verici bir zaman.

Ve ona bütüncül bir şekilde yaklaşabildiğinizde gerçekten harika oluyor.
