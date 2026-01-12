## 🔁 GitHub Projelerini Klonlama ve Forklama

GitHub projelerini klonlama ve fork’lama konusuna hoş geldiniz.

Bu videoyu izledikten sonra şunları yapabileceksiniz:

* Depoları klonlamak ve senkronize etmek
* Yeni bir projeye temel olması için bir projeyi *fork* etmek
* Diğer geliştiricilerle iletişim kurmak için `git` komutlarını kullanmak

GitHub’da, bazıları çok faydalı projeler olan 100 milyondan fazla depo vardır.

Bir ekibe katılıyor olun ya da kendi projenizi mevcut bir çalışmaya dayandırıyor olun, en güçlü araçlardan bazıları bir depoyu *fork* etmek ve klonlamaktır.

*Klonlama* genel olarak, bir deponun yerel makinenizde bir kopyasını oluşturmayı ifade eder.

Klonlanan kopyalar iki konum arasında senkronize tutulabilir.

*Forklama* ise, orijinal projeyi etkilemeden bir projeyi değiştirmeye veya genişletmeye olanak tanır.

Bu yöntem çoğunlukla mevcut bir projeyi alıp onu yeni projeniz için başlangıç noktası yapmak için kullanılır.

### 📥 GitHub Deposunu Klonlama

Bir GitHub deposunu klonlamak için, klonlamak istediğiniz depoya gidin.

Depo adının altında **Code** düğmesine tıklayın.

**Clone with HTTPS** bölümünde, URL’yi kopyalamak için **Clipboard** düğmesine tıklayın.

Yalnızca kaynak kodu indirmek için **Download ZIP** seçeneğine tıklayabilirsiniz, fakat bu yöntem sürüm kontrol bilgilerini içermez.

### 🧑‍💻 Terminalde Klonlama İşlemi

Yerel makinenizde bir terminal penceresi açın ve klonun kopyalanmasını istediğiniz dizine geçin.

Aşağıdaki komutu yazın:

```bash
git clone <yukarıda-kopyaladığınız-URL>
```

Ardından Enter tuşuna basarak klonlama işlemini gerçekleştirin.

### 🔄 Değişiklikleri GitHub ile Senkronize Etme

Değişikliklerinizi yaptıktan ve kodunuzu yeniden GitHub ile senkronize etmeye hazır olduğunuzda, önce aşağıdaki komutu çalıştırmanız gerekir:

```bash
git add files
```

Bu, değiştirilen dosyaları GitHub deposundaki bir  *staging area* ’ya taşır.

 *Staging area* , commit’lerin tamamlanmadan önce biçimlendirilebildiği ve gözden geçirilebildiği bir alandır.

Hazır olduğunuzda şu komutu çalıştırın:

```bash
git commit -m "message"
```

Bu,  *staging area* ’daki değişiklikleri commit eder.

Değişikliklerinizi tamamen GitHub deposuna aktarmaya hazır olduğunuzda şu komutu kullanın:

```bash
git push
```

Bu komut, commit edilmiş tüm değişiklikleri depoya gönderir.

### 🌐 Uzak (Remote) Depolar ve İş Birliği

*Remote* depolar, başka bir yerde — internette, ağınızda hatta yerel bilgisayarınızda — saklanan depolardır.

Sizin için genellikle salt-okunur veya okuma-yazma olan birkaç uzak depo bulunabilir.

Başka kişilerle iş birliği yapmak, bu uzak depoları yönetmeyi ve onlara ihtiyaç duyduğunuzda iş paylaşımı için  *push* , *pull* ve *fetch* işlemleri yapmayı içerir.

* Değişikliklerinizi uzak depoya aktarmak için `git push` komutunu kullanın.
* Uzak depodaki tüm değişiklikleri yerel deponuza aktarmak için `git fetch` komutunu kullanın. Bu komut, bu değişiklikleri üzerinde çalıştığınız dal ile birleştirmez.
* İsterseniz birleştirme ( *merge* ) işlemini manuel olarak gerçekleştirebilirsiniz.

Uzak depodan yerel deponuza değişiklikleri aktarmak ve bunları bir dala birleştirmek için `git pull` komutunu kullanın.

### 🌱 Origin ve Upstream Kavramları

Geliştiriciler uzak depolardan bahsederken *upstream* ve *origin* terimlerini kullanırlar.

* *Origin* genellikle sizin fork’unuzu ifade eder.
* *Upstream* ise orijinal çalışmayı ifade eder.

Bunlar yaygın adlandırma biçimleridir; elbette bu uzak depolara dilediğiniz isimleri verebilirsiniz.

### 🍴 Forklama: Yeni Proje Tabanı ve Katkı

 *Forklama* , bir GitHub deposunun kopyasını alıp yeni bir proje için temel olarak kullanmak için uygulanır.

Forklama, orijinal depoya değişiklikleri geri göndermek için de kullanılabilir.

Bu yöntem aynı projede bağımsız değişiklikler yapmak için de kullanılır.

Bu durumda, değişikliklerinizden memnun kaldığınızda, orijinal proje sahibine bir *pull request* gönderirsiniz.

Proje sahibi, değişikliklerinizi kabul edip etmeyeceğine karar verebilir.

### 📄 Lisans Dosyası ve Fork İşlemi

Bir lisans dosyasının bir kopyasını tutmak çoğu zaman yasal bir zorunluluktur.

Herhangi bir yasal zorunluluk olmasa bile bu iyi bir pratiktir.

Forklamak istediğiniz depoya gidin.

Sağ üst köşede **Fork** düğmesine tıklayın.

### 🔁 Fork’u Upstream ile Senkronize Etme

Yerel bir klon üzerinden bir fork’u orijinal çalışma ile senkronize tutmak için önce projenin yerel bir klonunu oluşturun.

Git’i fork’unuzu senkronize edecek şekilde yapılandırmak için, bir terminal açın ve klonu içeren dizine geçin.

Aşağıdaki komutu yazın:

```bash
git remote -v
```

Bu komut size uzak depoları gösterir.

Ardından, klonunuzu oluştururken kullandığınız dizini yapıştırarak şu komutu yazın:

```bash
git remote add upstream <orijinal-deponun-URL’si>
```

`upstream` eklemek, orijinal depoyu *upstream* etiketiyle yeni bir uzak depo olarak ekler.

Tekrar aşağıdaki komutu yazarsanız:

```bash
git remote -v
```

yaptığınız değişikliğin yansıtıldığını görürsünüz.

### 🔃 Upstream’den Değişiklikleri Alma ve Birleştirme

İlgili diğer komutlar şunlardır:

```bash
git fetch upstream
```

Bu komut, *upstream* dallarını alır.

```bash
git merge upstream main
```

Bu komut ise değişiklikleri `main` dalına birleştirir.

Ayrıca, uzak dalı tek adımda almak ve birleştirmek için şu komutu da göreceksiniz:

```bash
git pull upstream
```

`git pull upstream`, uzak bir dal ile senkronize olma adımlarının sayısını azaltır, fakat otomatik birleştirmeler her zaman istenmeyebilir.

### ✅ Öğrendiklerinizin Özeti

Bu videoda şunları öğrendiniz:

* GitHub’da kullanabileceğiniz 100 milyondan fazla depo bulunmaktadır.
* Bir depoyu, yerel makinenize kopyalamak ve değişiklikleri orijinal depoyla senkronize etmek için klonlayabilirsiniz.
* Bir depoyu, yeni bir proje için temel olarak kullanmak veya bir projede bağımsız çalışmak için *fork* edebilirsiniz.
