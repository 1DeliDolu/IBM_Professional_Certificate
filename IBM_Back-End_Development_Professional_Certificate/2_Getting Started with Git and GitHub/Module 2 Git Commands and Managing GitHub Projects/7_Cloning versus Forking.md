## 🔀 Klonlama ve Forklama

Klonlama ve fork’lamaya hoş geldiniz.

Şimdiye kadar klonlama ve fork’lama kavramlarına daldınız, ancak aralarındaki farkları hiç düşünmek için durakladınız mı?

Bu videoda, depoları klonlama ve fork’lama arasındaki farkı ve bunları ne zaman kullanmanız gerektiğini öğreneceksiniz. Ayrıca, klonlama ve fork’lama iş akışını da açıklayacaksınız.

GitHub, birden fazla geliştiricinin kod tabanları üzerinde paralel olarak iş birliği yapmasına olanak tanır. GitHub.com’daki bir proje, *public* (herkese açık) veya *private* (özel) bir depo olarak bulunur.

Bu projede çalışan her geliştiricinin, bilgisayarında kendi depo kopyası olabilir; buna *local repo* derler. Ayrıca GitHub.com üzerinde bulunan bir kopya daha vardır; buna da *remote repo* denir.

### 🧬 Örnek Senaryo: Grand Messaging ve Grand Messaging Plus

Diyelim ki elinizde **Grand Messaging** adlı mevcut bir proje var ve bunun üzerine, orijinaline göre ek özellikler ve geliştirmeler sunan yeni ya da türetilmiş bir proje olan  **Grand Messaging Plus** ’ı oluşturmak istiyorsunuz.

Kod tabanınızı en baştan yazmaya başlamanıza gerek yoktur; mevcut **Grand Messaging** projesini basitçe *fork* edebilir,  **Grand Messaging Plus** ’ı oluşturabilir ve mevcut kod tabanı üzerinde geliştirerek yeni ve geliştirilmiş özellikler sunabilirsiniz.

Public bir projeyi fork’lamak için, projenin GitHub proje sayfasına gidebilir ve sayfanın üst kısmındaki **Fork** seçeneğini seçebilirsiniz.

Bu fork seçeneği yalnızca web arayüzünü kullanırken mevcuttur. Bir fork oluşturmak için yerel ( *native* ) bir `git` komutu yoktur.

Fork’u oluşturduğunuz depo, **orijinal upstream deposu** olarak adlandırılır.

Orijinal upstream’i fork’ladıktan sonra, deponun fork’lanan kopyası **origin** olur ve origin’e erişimi olan geliştiriciler, bunun yerel makinelerinde klonlarını oluşturabilirler.

### 🌿 Klonlama Sonrası: Branch’ler ve Değişiklikler

Klonlamadan sonra, branch’ler oluşturabilir ve kod tabanında yeni özellikler eklemek, iyileştirmeler yapmak veya hataları düzeltmek gibi değişiklikleri kolayca yapabilirsiniz.

Son olarak, değişikliklerinizi branch’e ekleyebilir, commit’leyebilir ve origin’deki main branch ile birleştirilmesini ( *merge* ) talep edebilirsiniz.

Ancak şunu unutmamak önemlidir: `push` ve `merge` kullanarak değişikliklerin senkronizasyonu, yalnızca geliştiricilerin *yazma erişimine* sahip olduğu depolarla yapılabilir.

Peki, fork’un alındığı, yazma erişiminizin olmadığı orijinal  **upstream** ’e değişikliklerinizi geri katkıda bulunmak isterseniz ne olur?

Bu durumda, önerdiğiniz değişiklikler için **Pull requests** sekmesinden **New pull request** seçeneğini seçerek bir *pull request* gönderebilirsiniz.

Upstream projenin bakımını yapanlar, pull request içindeki değişiklikleri inceleyebilir, geri bildirim sağlayabilir ve çözümlenmesi gereken herhangi bir çatışma ( *conflict* ) yoksa buna göre merge edebilirler.

Şimdi, branch’leri nasıl oluşturabileceğinize ve değişiklikleri nasıl senkronize edebileceğinize bakalım.

### 🌱 Branch Oluşturma ve Değişiklikleri Senkronize Etme

Bir branch oluşturmak için `git branch` komutunu kullanabilir ve ardından `git checkout` komutunu kullanarak branch’i aktif hale getirebilirsiniz.

```bash
git branch
git checkout <branch-adı>
```

Değişiklikler yapıldıktan sonra, bunları `git add` ve `git commit` komutlarını kullanarak kaydedip  *staging* ’e alırsınız.

```bash
git add <dosyalar>
git commit -m "mesaj"
```

İstenen değişiklikler tamamlandıktan sonra, yeni oluşturulan branch için bir **upstream branch** ayarlamalı ve değişiklikleri yeni branch’e *push* etmelisiniz.

Sonrasında, değişikliklerin yeni branch’ten main branch’e, incelemenin ardından merge edilmesi için maintainer’a bir istekte bulunursunuz.

### 🔁 Forklama İş Akışını Yeniden Gözden Geçirme

Fork’lama iş akışını tekrar hatırlayalım:

Önce bir upstream projenin fork’unu oluşturursunuz; bu fork daha sonra **origin** olur.

Geliştirici, yerel makinelerde klonlar oluşturabilir, değişiklikler yapabilir ve ardından `git push` komutunu kullanarak güncellenmiş main branch’i, pull request’ler oluşturarak origin’e geri gönderebilir.

```bash
git push
```

Upstream projenin bakımını yapanlar (maintainer’lar), değişiklikleri inceler ve herhangi bir çatışma yoksa merge ederler.

### 🔀 `git merge` Hakkında Önemli Bir Nokta

`git merge` komutu hakkında dikkat edilmesi gereken bir nokta, git branch’lerindeki bağımsız geliştirme hatlarını alıp bunları tek bir branch içinde entegre etmenize olanak tanımasıdır.

### 🤝 Yeni Geliştirici ve Klonlama ile İş Birliği

Şimdi, projeye yeni bir geliştiricinin katıldığını ve  **Grand Messaging** ’i  **Grand Messaging Plus** ’a yükseltmek için çalıştığını varsayalım.

Projede iş birliği yapabilmesi için uzak depoyu bu yeni geliştiriciyle nasıl paylaşacaksınız?

İşte tam burada klonlama imdadınıza yetişir.

GitHub’daki herhangi bir public repo’yu ya da erişiminizin olduğu bir private repo’yu, o repoya gidip **Code** düğmesini seçerek klonlayabilirsiniz.

Bu noktada, uzak deponun tüm kod tabanını çeşitli yollarla alabilirsiniz.

GitHub ayrıca HTTPS URL’sini kopyalayabilmenizi ve ardından yerel makinenizden `git clone URL` komutunu çalıştırabilmenizi sağlar:

```bash
git clone <HTTPS-URL>
```

### 🧭 Klonlama İş Akışı

Klonlama işin içine, repo’yu fork’ladıktan ve repo artık origin olduktan sonra girer.

Daha sonra, geliştiricinin kendi bilgisayarında kullanabileceği, uzak deponun birebir kopyasını oluşturmak için `git clone` komutunu kullanarak origin’i kullanırsınız.

```bash
git clone <origin-URL>
```

Ardından yeni geliştirici yeni bir branch oluşturur, değişiklikler yapar ve bunları `add` ve `commit` işlemlerini kullanarak kaydeder.

```bash
git branch <yeni-branch>
git checkout <yeni-branch>
git add <dosyalar>
git commit -m "mesaj"
```

Bundan sonra, değişikliklerinin gözden geçirilmesi için yeni branch’i origin’e *push* eder:

```bash
git push -u origin <yeni-branch>
```

Bir reviewer ya da maintainer, deponun en güncel kopyasını almak için `git fetch` veya `git pull` komutunu ve branch’teki değişiklikleri belirleyip karşılaştırmaya yardımcı olması için `git diff` komutunu kullanır.

```bash
git fetch
git pull
git diff
```

### 🔀 İnceleme Sonrası: Merge ve Upstream’e PR

İnceleme tamamlandıktan sonra, reviewer `git checkout` komutunu kullanarak ilgili branch’e geçebilir ve branch’i main ile merge edebilir.

```bash
git checkout main
git merge <yeni-branch>
```

Son olarak, maintainer erişimi olan herhangi biri, orijinal repoda değişiklikleri başlatmak için orijinal upstream’e bir pull request oluşturabilir.

### 📝 Özet

Hızla tekrar edelim:

Bu videoda şunları öğrendiniz:

* Başlangıç noktası olarak başka bir projeden türetilmiş bir proje oluşturmak istiyorsanız, bir projeyi fork etmeyi tercih edebilirsiniz.
* Fork ettiğiniz depo, **upstream repo** olarak adlandırılır.
* Yazma erişiminizin olmadığı upstream projeye değişikliklerinizi geri katkıda bulunmak için, yaygın olarak **PR** (Pull Request) olarak adlandırılan bir *pull request* gönderebilirsiniz.
* Upstream projenin bakımını yapanlar, pull request içindeki değişiklikleri inceleyebilir, geri bildirim verebilir ve çözümlenmesi gereken herhangi bir çatışma yoksa buna göre merge edebilirler.
* Uzak deponun birebir kopyasını `git clone` işlemini kullanarak oluşturabilirsiniz.
* Projenin klonlandığı uzak depo, aynı zamanda **origin** olarak da adlandırılır.

Branch’ler oluşturmak ve değişiklikleri senkronize etmek için kullanılan `git` komutları şunlardır:

* `git branch` → bir branch oluşturmak için
* `git checkout` → branch’i aktifleştirmek için
* `git add` ve `git commit` → değişiklikleri kaydetmek için
* `git push` → branch’i uzak depoya göndermek için
* `git merge` → değişiklikleri main branch ile birleştirmek için
