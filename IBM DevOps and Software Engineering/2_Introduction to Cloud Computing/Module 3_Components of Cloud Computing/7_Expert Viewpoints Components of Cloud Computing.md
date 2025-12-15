# 🧠 Expert Görüşleri: Bulut Bilişimin Bileşenleri

Bulut bilişimin bileşenleri uzman görüşlerine hoş geldiniz. Bu videoda, bulutta bilişim kaynakları arasında karar verirken dikkate alınan bazı faktörleri tartışan birkaç bulut uygulaması profesyonelini dinleyeceğiz. Örneğin, *Bare Metal* sunucuya karşı sanal sunucuya karşı *container*lar.

---

## 🖥️ Sanal Sunucular ve Sanal Makineler

Sanal sunucular, temel olarak başka bir işletim sisteminin içinde farklı bir işletim sistemi çalıştırır. Örnek olarak, Linux’un üzerinde Windows çalıştırmak verilebilir ve bu nedenle kendi tam işletim sistemlerini içerirler.

Dolayısıyla  *VM* ’ler (Virtual Machines) görünüm ve davranış olarak fiziksel sunuculara çok benzer. Ve tüm işletim sistemini içerdukleri için genellikle gigabaytlar boyutundadırlar, oldukça büyüktürler.

 *VM* ’ler, işletim sistemine, uygulamaya ve kütüphane sürümlerine bağımlılıkları nedeniyle çok daha az taşınabilirdir. Bu, sanal makinelerle ilgili bir değerlendirme unsurudur.

---

## 📦 Container, Sanal Sunucu ve Bare Metal Arasında Seçim

*Container*lar, sanal sunucular ve *bare metal* sunucular arasında karar verirken, ölçeklenebilirlikleri ve maliyet verimlilikleri nedeniyle neredeyse her zaman başlangıç noktası olarak *container*lara yöneliyorum.

Ancak bu, her zaman en iyi seçenek oldukları anlamına gelmez. Örneğin, güvenlik gerekçeleriyle *container*larınızın başka bir müşterininkiyle aynı *VM* üzerinde çalışmasına tahammül edemeyebilirsiniz.

Bu durumda kendi sanal sunucunuzu sağlamayı tercih edebilirsiniz. Ya da belki sürekli olarak mümkün olan en iyi performansa ihtiyacınız vardır ve *hypervisor tax* veya *noisy neighbor* etkileriyle uğraşmak istemezsiniz.

Bu durumda *bare metal* seçersiniz.

---

## 🐳 Container Teknolojisinin Avantajları ve Orkestrasyon

*Container*lar, Dev, QA ve production ortamları arasında paylaşılabilen Linux tabanlı ortak bir paylaşımlı imaja dayanır. Bu, *container*ların çok büyük bir avantajıdır.

Ayrıca  *VM* ’ler için saniyeler yerine, milisaniyeler gibi çok hızlı sürelerde *container* başlatmak da mümkündür. Hafiftirler; genellikle megabaytlar boyutundadırlar ve buradaki temel teknolojiler, *container* orkestrasyonu için  **Docker** , **Kubernetes** ve  **OpenShift** ’tir.

---

## 🧩 Kullanım Senaryoları: Mikroservisler ve Bulut-Native

Buradaki bazı çekici kullanım senaryoları, iş yüklerinin hizmet verilebilir en küçük birimlere bölünebildiği durumlardır. Burada örneğin mikroservisleri düşünebilirsiniz ve bu, “cloud native architecture” olarak adlandırılan şey için belki de temel bir teknolojidir.

---

## ⚡ Serverless Fonksiyonlar

Daha az maliyetli ve yalnızca gerektiğinde çalışan bir şey istiyorsanız, bu serverless fonksiyonlar için mükemmel bir kullanım senaryosudur.

Çünkü bazı bulut sağlayıcılarında yalnızca milisaniye kullanım kadar az birimlerde ücretlendirebilirler ve serverless fonksiyonlar, işletim sistemini yamalama gibi işlerde zaman harcamamanıza yardımcı olur.

---

## 🌐 Cloud Agnostic ve Hibrit Bulut için Container

Bulut agnostik olmak istiyorsanız; yani aynı anda farklı bulut sağlayıcılarında bulunmak istiyorsanız (hibrit bulut kurulumuna sahip olmak gibi), *container*lar iyi bir seçim olabilir çünkü **Docker** her yerde aynı şekilde çalışır.

Son birkaç yılda, özellikle kurumsal alanda Kubernetes ve OpenShift ve diğer şeylerle *container*ların oldukça yol kat ettiğini gördüm. Açıkçası, *container*lar neredeyse atmak isteyeceğiniz her iş yükünü çalıştırabilir.

---

## 🚫 Container İstisnaları

Bazı istisnalar vardır; bazen bir *bare metal* makinede özel bir ekran kartına ihtiyaç duyarsınız veya çekirdek seviyesinde ayarlara erişmeniz gerekir; bunları bir *container*da yapamazsınız.

Ancak çoğunlukla şunu söyleyebilirim: belirli bir sebepten dolayı kullanmamak için özel bir ihtiyacınız yoksa *container*ları veya  *serverless* ’ı kullanacaksınız.

---

## 🧱 Bare Metal Sunucular

*Bare Metal* sunucular, temelde tek kiracılı ( *single tenant* ) adanmış donanım sunucusudur. Bu, bizim eski (legacy) donanım yaklaşımımızdır.

Avantajları: performans, güvenlik ve güvenilirlik için sunucuyu belirli ihtiyaçlara göre optimize edebilirsiniz.

Dezavantajları ise talep üzerine ölçeklenebilirlikte sınırlardır; donanım sabit bir kapasiteye sahiptir ve *bare metal* sunucular için aylık sabit fiyatlandırma vardır.

---

## 🎯 Bare Metal Kullanım Alanları

*Bare metal* sunucuların anlamlı olduğu kullanım alanları vardır. Bunlardan bazıları çok yüksek performans gerektiren şeyler olabilir. Oyun ya da gerçek zamanlı analitik gibi durumları düşünün; ya da düzenleyici veya uyumluluk gereksinimlerinin adanmış bir hesaplama ortamını zorunlu kıldığı durumlar.

Veya sürekli ve devamlı hesaplama kaynakları kullanan uygulamalar.

---

## 🚀 Örnek: Aşırı İşlem Gücü Gerektiren Senaryolar

Aşırı hız ve çok fazla işlem gücüne ihtiyacınız varsa; diyelim ki süpersonik bir jet için bir tasarım üzerinde iterasyon yapıyorsunuz ve bir rüzgar tünelinde nasıl davranacağını modellemeniz gerekiyor ve bunu 500 kez yapmanız gerekiyor.

Bu, işlenecek çok büyük miktarda veri demektir. Ve bir kümedeki en güçlü makineleri kullanmak istersiniz ve onların birbirine mümkün olduğunca yakın olmasını istersiniz; yani bu *bare metal* makinelerdir.
