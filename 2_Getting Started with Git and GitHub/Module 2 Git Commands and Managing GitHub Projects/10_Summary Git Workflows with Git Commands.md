# 🧾 Git Komutlarıyla Git İş Akışları Özeti

### 📚 Bu modülde şunları öğrendiniz:

GitHub'da 100 milyondan fazla depo vardır. Bir depoyu klonlayabilir ve yapılan değişiklikleri özgün depoyla tekrar senkronize edebilirsiniz. Ayrıca bir depoyu *fork* edebilir ve onu yeni bir proje için temel olarak kullanabilir ya da o proje üzerinde bağımsız olarak çalışabilirsiniz.

---

### 🔁 Bir GitHub iş akışına dahil olan adımlar şunlardır:

* Uzak depoyu klonlamak ya da bir Git deposu başlatmak.
* Dosyaları  *staging area* 'a taşımak.
* İlk commit'i gerçekleştirmek.
* Bir dal ( *branch* ) oluşturmak ve onun üzerinde çalışmak.
* Dosyaları  *staging area* 'a eklemek ve commit etmek.
* Yerel commit’leri uzak depoya ( *remote repository* ) göndermek ( *push* ).
* Gözden geçirme ve birleştirme için bir *pull request* oluşturmak.
* Yerel depoyu güncellemek için *pull* işlemini kullanmak.

---

### 👥 Proje yönetiminde yer alan roller

Bir projeyi yönetirken birden çok rol görev alır:  *Developer* , *Integrator* ve  *Repository Administrator* .

#### 👨‍💻 Developer

Bir grup projesinde çalışan bir  *Developer* , tek başına çalışan bir geliştiricinin ihtiyaç duyduğu komutlara ek olarak `git clone`, `git pull`, `git fetch`, `git push` ve `git request-pull` gibi komutları kullanır.

#### 🧩 Integrator

Bir grup projesindeki bir  *Integrator* , başkaları tarafından yapılan değişiklikleri gözden geçirir ve entegre eder.  *Integrator* 'lar, katılımcıların ihtiyaç duyduğu komutlara ek olarak `git pull`, `git revert` ve `git push` gibi komutları kullanır.

#### 🗂️ Repository Administrator

 *Repository Administrator* 'lar, deponun nasıl organize edildiğini ve kullanıcıların depoyla nasıl etkileşim kurduğunu yapılandırırlar. Ayrıca web servislerine ve dokümantasyona erişim için gereken sunucuları yapılandırırlar, e-posta ve indeks ayarlarını tanımlar ve uygulamanın görünümünü ve hissini yönetirler.

---

### 🧮 Çeşitli Git komutları

Aşağıdaki tablo çeşitli Git komutlarını göstermektedir:


### 🧮 Git Komutları – Kısa Açıklamalar

| Komut                              | Açıklama                                                                 |
| ---------------------------------- | -------------------------------------------------------------------------- |
| `git init`                       | Yeni bir Git deposu başlatır.                                            |
| `git checkout`                   | Dal (branch) veya commit'e geçiş yapar.                                  |
| `git revert`                     | Belirli bir commit'i geri alır (yeni bir ters commit oluşturur).         |
| `git-format-patch`               | Commit'leri e-posta ile gönderim için patch dosyasına dönüştürür.  |
| `git fetch upstream`             | Uzak upstream depodaki değişiklikleri yerel olarak çeker (merge etmez). |
| `git status`                     | Çalışma dizinindeki ve staging alanındaki dosya durumunu gösterir.    |
| `git merge`                      | Belirtilen dalı mevcut dala birleştirir.                                 |
| `git config --global user.email` | Global e-posta bilgisini ayarlar.                                          |
| `git-request-pull`               | Pull request için özet oluşturur (CLI tabanlı).                        |
| `git merge upstream/main`        | Upstream ana dalını mevcut dala birleştirir.                            |
| `git add .`                      | Tüm değişiklikleri staging alanına ekler.                              |
| `git clone`                      | Uzak bir depoyu yerel olarak kopyalar.                                     |
| `git config --global user.name`  | Global kullanıcı adını ayarlar.                                        |
| `git-send-email`                 | Patch dosyalarını e-posta ile gönderir.                                 |
| `git pull upstream`              | Upstream'den değişiklikleri çeker ve birleştirir.                      |
| `git commit`                     | Staging alanındaki değişiklikleri kaydeder.                             |
| `git pull`                       | Uzak depodan değişiklikleri çeker ve birleştirir.                      |
| `git remote -v`                  | Uzak depo bağlantılarını listeler.                                     |
| `git-am`                         | E-posta ile gelen patch'leri uygular.                                      |
| `git web`                        | Web arayüzü başlatır (bazı özel konfigürasyonlarda).                |
| `git log`                        | Commit geçmişini listeler.                                               |
| `git push`                       | Yerel commit'leri uzak depoya gönderir.                                   |
| `git remote rename`              | Uzak depo adını değiştirir.                                            |
| `git-daemon`                     | Git sunucusu olarak çalışır (ağ üzerinden erişim için).            |
| `git-instaweb`                   | Depoyu tarayıcıda görüntülemek için geçici web sunucusu başlatır. |
| `git reset`                      | Staging alanını veya commit geçmişini geri alır.                      |
| `git version`                    | Yüklü Git sürümünü gösterir.                                        |
| `git remote add origin`          | Uzak depo bağlantısı ekler (genellikle ilk push için).                 |
| `git-pull downstream`            | Downstream'den değişiklikleri çeker (özelleştirilmiş senaryolarda).  |
| `git branch`                     | Yeni dal oluşturur veya mevcut dalları listeler.                         |
| `git diff`                       | Değişiklikleri satır satır gösterir.                                  |
| `git-remote`                     | Uzak depo işlemlerini yönetir.                                           |
| `git remote add upstream`        | Upstream uzak depo bağlantısı ekler.                                    |
| `git-rerere`                     | Tekrarlayan merge çatışmalarını otomatik olarak çözer.              |
