# 🎥 Demo Videosu: Snyk (SAST) Ücretsiz Araç

## 🎯 Snyk Demo Videosuna Giriş ve Öğrenme Hedefleri

Snyk Demo Videosuna hoş geldiniz. Bu videoyu izledikten sonra, açık kaynaklı bir statik uygulama güvenlik testi (SAST) aracı olan Snyk’i tanımlayabilecek ve onu kullanarak bir yazılım projesini güvenlik açıkları için nasıl tarayabileceğinizi açıklayabileceksiniz.

Ayrıca, Snyk kullanarak gerçekleştirilen bir güvenlik açığı taramasının sonuçlarını yorumlamayı da öğreneceksiniz.

Snyk, geliştiriciler için bir güvenlik platformu sağlayan, açık kaynaklı bir statik uygulama güvenlik testi (SAST) aracıdır. Snyk, doğrudan geliştirme araçlarına, iş akışlarına ve otomasyon hatlarına entegre olarak ekiplerin kod, bağımlılıklar, container’lar ve altyapıdaki güvenlik açıklarını belirlemesini, önceliklendirmesini ve gidermesini kolaylaştırır.

Her geliştiricinin araç setine güvenlik bilgisini ekler ve pazara liderlik eden uygulamalar ile güvenlik istihbaratı tarafından desteklenir. Yaparak öğrenme yaklaşımıyla, Snyk kullanarak bir yazılım projesini güvenlik açıkları için taramayı gösteren bir demoyu izleyelim.

---

## 📝 Adım 1: Snyk Hesabı Oluşturma

İlk adım olarak, GitHub üzerinde bir yazılım projesini taramak için bir Snyk hesabı oluşturmanız gerekir. Bu yüzden, web siteleri olan `snyk.io`ya giriş yaparak ücretsiz bir Snyk hesabı oluşturalım.

`Login`e tıklayın. Snyk hesabımızı GitHub hesabımızla entegre edelim; `GitHub`ı seçin ve ardından `Next step`e tıklayın.

Tekrar `Next step`e tıklayın. Üçüncü adım altındaki tüm kutucukları işaretlediğinizden emin olun; yani `Configure`, `Automation Settings` ve `Authenticate`.

---

## 🔗 Adım 2: GitHub ile Entegrasyon ve Depo Seçimi

`Authenticate GitHub`a tıklayın. Artık Snyk ve GitHub başarıyla bağlanmıştır.

Snyk, GitHub depoları içinde güvenlik açıklarını tarar. Taranmış bir deponuz yoksa, güvenlik açıklarını analiz etmek için bir depo içe aktarabilirsiniz.

`Monitor a public repository`ye tıklayın. `GitHub teacher/GitHub-slideshow` yazın ve ardından `Add repo`ya tıklayın.

İçe aktarma işlemini başlatmak için `Import One repository`ye tıklayın.

---

## 📂 Adım 3: Depoyu İçe Aktarma ve Tarama Sonuçlarını Açma

Snyk içe aktarma işlemine başlayacaktır ve bu biraz zaman alabilir, bu nedenle lütfen sabırlı olun.

Bu görev tamamlandığında, taranan projenin önündeki `>` (büyüktür işareti) simgesine tıklayın.

Herhangi bir sorun varsa, daha fazlasını görmek için dosya bağlantısına tıklayabilirsiniz.

Bu örnekte, `gemfile.lock` dosyası içinde 27 güvenlik açığı sorunu keşfedilmiştir. Bir Ruby projesinde `Gemfile.lock` dosyası, bir Python projesindeki `requirements.txt` dosyasına denktir.

Bu dosya, projenin bağımlı olduğu tüm paketlerin adlarını içerir; bu da bu paketlerin bazılarında bilinen güvenlik açıkları olduğu ve uygulamanızın da bu nedenle savunmasız olduğu anlamına gelir.

Genel bakışı görmek için projenin `Gemfile.lock` dosyasına tıklayın.

---

## 📈 Adım 4: Güvenlik Açıklarını ve Bağımlılıkları İnceleme

Aşağı kaydırdığınızda, sorunların bir kısmının listesini görebilirsiniz.

Sağ taraftaki panelde güvenlik açıklarının şiddet derecelerini, düzeltilebilirlik durumunu, istismarın olgunluk seviyesini ve durumunu görebilirsiniz.

`Retest Now` bağlantısına tıklamak, Snyk’in aynı güvenlik açıklarını yeniden test etmesini sağlar. Snyk’in ücretli sürümünde, bu güvenlik açıklarını tıklayarak giderebilirsiniz.

`Dependencies`e tıkladığınızda, proje için yazılım bağımlılıklarının bir listesini görebilirsiniz.

Profil sayfanıza dönmek için `Projects`e tıklayın. İşiniz bittiğinde oturumu kapatın veya tarayıcınızı kapatın.

---

## ✅ Özet: Snyk ile Neler Öğrendiniz?

Bu videoda, Snyk’in geliştirici güvenliği için açık kaynaklı bir statik uygulama güvenliği testi (SAST) aracı platformu olduğunu öğrendiniz.

Bu araç, ekiplerin güvenlik açıklarını belirlemesine, önceliklendirmesine ve gidermesine yardımcı olur. Snyk, GitHub gibi depolarda bulunan kodu tarar.

Son olarak, Snyk’i kullanarak güvenlik açıklarını gözden geçirebilir, kodu test edebilir ve güvenlik açıklarını giderebilirsiniz.
