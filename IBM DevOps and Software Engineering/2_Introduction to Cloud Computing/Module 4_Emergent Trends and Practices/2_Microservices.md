# 🧩 Microservisler

Microservis mimarisi, tek bir uygulamanın birçok gevşek bağlı ve bağımsız olarak dağıtılabilir daha küçük bileşen ya da hizmetten oluştuğu bir yaklaşımdır. Bu hizmetlerin her biri genellikle kendi konteynerlarında çalışan kendi teknoloji yığınına sahiptir. Birbirleriyle  *API’ler* , *olay akışı (event streaming)* ve *mesaj aracılarının (message brokers)* bir kombinasyonu üzerinden iletişim kurarlar.

Bir işletme açısından bunun anlamı şudur: Uygulama bileşenleri, bağımsız çalışan birden fazla geliştirici tarafından daha verimli şekilde geliştirilebilir ve güncellenebilir. Ekipler, farklı bileşenler için farklı teknoloji yığınları ve çalışma zamanı ortamları kullanabilir. Çok fazla yük alan bileşenler bağımsız olarak ölçeklenebilir; böylece tüm uygulamayı ölçeklemek zorunda kalmanın getirdiği israf ve maliyet azalır.

Bu videoda, mikroservislerin uygulama geliştirmeyi nasıl şekillendirdiğine bakacağız ve ayrıca mikroservislerin kullanımını gösteren bir örnek senaryoyu inceleyeceğiz.

---

## 🏗️ Uygulama Geliştirmenin Değişen Yüzü

Geliştiricilerin uygulama oluşturma biçimi değişiyor. Geçmişte yazılım, büyük monolitik uygulamalar olarak inşa edilirdi; bir geliştirici ekibi, ortak bir kod tabanı üzerinde kurulu büyük bir uygulamayı oluşturmak için aylarca çalışırdı. Bu geliştiriciler, uygulamanın her bölümünü baştan sona yazardı.

Artık onlarca yıllık yazılım geliştirmeden sonra, geliştiricilerin bir uygulamanın temelini oluşturmak için kullanabileceği çok büyük miktarda kod zaten mevcut; bu da artık her satır kodu sıfırdan yazmak zorunda olmadıkları anlamına geliyor. Bulut geliştirme platformları, uygulamalara kolay ve güvenli biçimde entegre edilebilecek bir kod ekosistemi sunar.

Artık tek bir ekipte tek bir dev uygulama inşa etmek yerine, geliştiriciler küçük bağımsız ekiplere ayrılır ve *mikroservisler* denen daha küçük kod parçaları yazarlar. Mikroservisler, büyük uygulamaları temel işlevlerine ayırır.

---

## 🧱 Mikroservis Örnekleri

Örneğin:

* Arama ( *Search* )
* Öneriler ( *Recommendations* )
* Müşteri Puanları ( *Customer Ratings* )
* Ürün Katalogları ( *Product Catalogs* )

Her biri birbirinden bağımsız geliştirilir, ancak bulut geliştirme platformu üzerinde birlikte çalışarak işleyen bir uygulama oluştururlar.

Bir  *konteyner (container)* , her bir mikroservis için dağıtım yöntemidir; yani kodu gitmesi gereken yere taşır. Konteynerlar *tak-çalıştır (plug-and-play)* mantığındadır; dolayısıyla bir mikroservis uygulama için çalışmıyorsa, geliştiriciler diğer uygulama işlevlerinin nasıl çalıştığını bozmadan onu çıkarıp yerine başka birini koyabilir.

---

## 🎥 Kullanım Senaryosu: Ron ve Dream Game

Ron, Dream Game adında çevrim içi bir akış medya hizmetini kullanan bir futbol hayranıdır. Dün gece takımının kritik yarı final maçını izlemeyi kaçırdı. Neyse ki, maçı bu gece Dream Game üzerinden izleyebilir.

Giriş yaptığında, tüm Dream Game kullanıcıları arasında en popüler içerikleri görür. Biraz aradıktan sonra, aradığı maçı bulur. Aslında istediği şey, oyununu tek bir tıklamayla bulabilmektir.

Neyse ki Dream Game geliştirme ekibi, Ron gibi izleyiciler için daha iyi bir kullanıcı deneyimi geliştirmek üzere mikroservisleri kullanmaktadır.

---

## 🗂️ Mikroservisler Nasıl Çalışıyor?

### 🧾 1) İçerik Kataloğu ( *Content Catalog* )

İlk mikroservis, Dream Game’in sunduğu milyonlarca oyunu barındıran bir *İçerik Kataloğu*dur. Küçük bir geliştirici ekibi, her içerik parçasını onu tanımlayan *metadata* ile düzenler.

### 🔎 2) Arama Fonksiyonu ( *Search Function* )

Bu metadata, ikinci mikroservis olan *Arama Fonksiyonu*na beslenir; bu da Ron’un arama sonuçlarının yakalanmasını ve Dream Game kataloğuyla karşılaştırılmasını sağlar.

### ⭐ 3) Öneriler ( *Recommendations* )

Üçüncü mikroservis olan  *Öneriler* , tüm Dream Game kullanıcıları arasında en popüler içeriklere ilişkin verileri toplar. Ron’un ilk girişte gördüğü ana sayfayı üreten şey budur.

Bu üç mikroservisin her biri kendi ayrı konteynerındadır ve uygulamaya katılmaya hazırdır.

---

## 🧭 Servis Keşfi ve API ile İletişim

Ancak birlikte çalışabilmeleri için önce birbirlerini bulmaları gerekir. Bunu, bu ve diğer birçok mikroservisin iletişim kurması için bir yol haritası oluşturan *Service Discovery* denen bir şeyi kullanarak yaparlar.

Mikroservisler birbirlerini bulduklarında, *uygulama programlama arayüzü* yani *API* kullanarak iletişim kurarlar. Dolayısıyla Ron favori futbol takımını aradığında, *Arama* mikroservisi, Ron’un ne aradığı hakkında *İçerik Kataloğu* ile (bir *API* üzerinden) iletişim kurar.

---

## 🎯 Hedef: Tek Tıkla Maça Ulaşmak

Şimdi tekrar hedefe dönelim: Ron’un futbol maçına tek bir tıklamayla ulaşmasını sağlamak. *Öneriler* mikroservisi üzerinde çalışan geliştirme ekibi, koda bir *analitik algoritma* ekleyerek güncelleme yapmaktadır.

Analitik kullanarak *Öneriler* mikroservisi, Ron’un izleme geçmişini ve tercihlerini; diğer kullanıcılar arasındaki popüler içeriklerle karşılaştıracaktır. Buna futbol hayranları ve Ron’un coğrafi bölgesi ile demografisindeki izleyiciler de dahildir.

Geliştiricilerin kodu sıfırdan oluşturması gerekmediği için, bu yeni işlevselliği birkaç gün içinde dağıtabilirler. Bu güncellemeler, diğer mikroservis konteynerları normal şekilde çalışmaya devam ederken arka planda gerçekleşir.

Ron bir sonraki Dream Game kontrolünde, yalnızca en popüler ya da en yeni içerikleri görmek yerine, sistem izleme alışkanlıklarını ve tercihlerini daha fazla öğrendikçe kendini geliştirmeyi sürdürecek kişiselleştirilmiş bir oynatma listesi görür.

Sonuç: Ron, favori takımının son maçını hemen bulur.

---

## 🚀 Sonuç: Paralel İnovasyon ve Daha İyi Deneyim

Mikroservis yaklaşımı, geliştiricilerin uygulamalar üzerinde paralel biçimde hızlı inovasyon yapmasına ve Ron gibi kullanıcıların gerçekten ilgilendikleri şeylere odaklanmasına olanak tanır. Ve bu ilgi alanları her gün daha hızlı değişip büyürken, mikroservisler işletmelerin ayak uydurmasına ve müşterileriyle birlikte büyümesine yardımcı olur.
