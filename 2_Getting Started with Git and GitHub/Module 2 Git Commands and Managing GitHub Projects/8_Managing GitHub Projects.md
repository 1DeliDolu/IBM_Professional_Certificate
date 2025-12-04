## 🧩 GitHub Projelerini Yönetme

GitHub projelerini yönetmeye hoş geldiniz.

Bu videoda, bir projede sürüm kontrolünün yani Git’in yaygın rollerini belirleyecek ve diğer geliştiricilerle iletişim kurmak için kullanılan Git komutlarını listeleyeceksiniz.

---

### 👥 Projedeki Roller ve Git’in Kullanımı

GitHub’ın, sürüm kontrolü ve proje yönetimi için popüler bir platform olduğunu zaten biliyorsunuz.

Etkili iş birliği ve proje organizasyonu için GitHub projelerinizi yönetmeniz gerekir.

Bir projeyi yönetirken birden fazla rol söz konusudur:

* geliştirici,
* entegratör,
* depo yöneticisi ( *repository administrator* ).

Bir grup projesinde katılımcı olarak çalışan bir geliştiricinin, diğerleriyle nasıl iletişim kuracağını öğrenmesi ve tek başına çalışan bir geliştiricinin ihtiyaç duyduğu komutlara ek olarak bu komutları da kullanması gerekir.

Git ile çalışırken, Git komutlarını veya **GitHub Desktop** gibi masaüstü araçlarını kullanabilirsiniz.

---

### 🧑‍💻 Geliştirici Rolü ve Temel Git Komutları

`git clone`, geliştiricinin üzerinde çalışmak istediği, uzak ve paylaşılan bir depo olan  *upstream* ’den bir kopya oluşturmak için kullanılır.

`git pull` ve `git fetch`,  *origin* ’den depoyu çekmek veya almak ve *upstream* ile güncel tutmak için kullanılır.

`git push`, depo iş akışı için eşzamanlı ( *concurrent* ) bir sürümleme sistemi benimsediyseniz commit’leri paylaşılan depoya göndermek için kullanılır ve `git request pull` ise  *upstream* ’in çekebilmesi için değişikliklerin bir özetini oluşturur.

---

### 🤝 Entegratörün Görevleri ve Ek Komutlar

Bir grup projesindeki entegratör, başkaları tarafından yapılan değişiklikleri alır, bunları inceler ve entegre eder, pull request’lere yanıt verir ve ortaya çıkan sonucu başkalarının kullanması için yayımlar.

Entegratörler, katılımcıların ihtiyaç duyduğu komutlara ek olarak aşağıdaki komutları kullanırlar:

* `git pull`, güvendiğiniz yardımcılarınızla yaptığınız çalışmaları birleştirmenize yardımcı olur.
* `git revert`, berbat olmuş ya da hatalı herhangi bir commit’i geri alır.
* `git push`, projeyi yerel repodan uzak repoya yayımlamaya yardımcı olacaktır.

---

### 🛠️ Depo Yöneticisinin (Repository Administrator) Görevleri

Depo yöneticisi, deponun nasıl organize edildiğini ve kullanıcıların depo ile nasıl etkileşime girdiğini yapılandırır.

Ayrıca toplulukları, varlık türlerini, ilişkileri, kategorileri ve öznitelikleri yönetir.

Bir depo yöneticisi, geliştiriciler için depoya erişimi kurar ve sürdürür.

Ayrıca web servislerine ve dokümantasyona erişmek için gereken sunucuları yapılandırır, e-posta ve indeks ayarlarını tanımlar ve uygulamanın görünüm ve hissini yönetir.

Depo yöneticileri, sürekli entegrasyon ve sürekli teslim (*continuous integration* ve *continuous delivery* ya da  *CI/CD* ) dâhil yazılım iş akışlarını otomatikleştirmek için  **GitHub Actions** ’ı kullanabilir.

---

### 🔁 Özet

Haydi, kısaca tekrar edelim.

Bu videoda, bir projeyi yönetmede birden fazla rolün yer aldığını öğrendiniz: geliştirici, entegratör ve depo yöneticisi.

Her rol, iş birliği yaptığı kişilerle iletişim kurmak için farklı Git komutları kullanır.

Bir grup projesinde çalışan geliştirici, tek başına çalışan bir geliştiricinin ihtiyaç duyduğu komutlara ek olarak şu komutları kullanır:

* `git clone`
* `git pull`
* `git fetch`
* `git push`
* `git request pull`

Bir grup projesindeki entegratör, başkaları tarafından yapılan değişiklikleri inceler ve entegre eder.

Entegratörler, katılımcıların ihtiyaç duyduğu komutlara ek olarak `git pull`, `git revert` ve `git push` gibi komutlar kullanırlar.

Depo yöneticileri, deponun nasıl organize edildiğini ve kullanıcıların depo ile nasıl etkileşime girdiğini yapılandırırlar.

Ayrıca web servislerine ve dokümantasyona erişmek için gereken sunucuları yapılandırır, e-posta ve indeks ayarlarını tanımlar ve uygulamanın görünüm ve hissini yönetirler.
