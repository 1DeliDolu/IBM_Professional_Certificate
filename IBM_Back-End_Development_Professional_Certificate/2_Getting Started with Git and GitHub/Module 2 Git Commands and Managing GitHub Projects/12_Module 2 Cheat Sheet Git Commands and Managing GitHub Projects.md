# 🚀 Git ve GitHub ile Başlarken

## 📌 Modül 2 Hızlı Başvuru: Git Komutları ve GitHub Projelerini Yönetme

### 📋 Paket/Yöntem – Açıklama – Kod Örneği

---

### 💻 `git add`

**Açıklama:** Çalışma dizinindeki değişiklikleri  *staging area* ’a taşımak için kullanılır.

**Kod örneği:**

```bash
1
git add sample.md
```


---

### 💻 `git add .`

**Açıklama:** GitHub depolarında değişmiş dosyaları  *staging area* ’a taşımaya olanak tanır.

**Kod örneği:**

```bash
1
git add .
```


---

### 💻 `git am`

**Açıklama:** Depoya e-postayla gönderilen yamaları uygulamak için kullanılır.

**Kod örneği:**

```bash
1
git am < patchfile.patch
```


---

### 🌿 `git branch`

**Açıklama:** Depo içinde değişiklik yapabilmek için yalıtılmış bir ortam oluşturmaya olanak tanır.

**Kod örneği:**

```bash
1
git branch <new-branch>
```


---

### 🌿 `git checkout`

**Açıklama:** Mevcut branch’leri görmeye ve değiştirmeye olanak tanır.

**Kod örneği:**

```bash
1
git checkout <existing-branch>
```


---

### 🌿 `git checkout main`

**Açıklama:** *main* branch’ine geçiş yapmaya olanak tanır.

**Kod örneği:**

```bash
1
git checkout main
```


---

### 📥 `git clone`

**Açıklama:** Uzak ( *remote* ) depodan bir kopya oluşturmaya olanak tanır.

**Kod örneği:**

```bash
1
git clone <repository-url>
```


---

### 💾 `git commit`

**Açıklama:** *Staged* hâlde bulunan değişikliklerin anlık görüntülerini almanıza ve bunları projeye commit etmenize olanak tanır.

**Kod örneği:**

```bash
1
git commit -m "Your commit message here"
```


---

### ⚙️ `git config --global user.email`

**Açıklama:**

Örnek 1: Git için genel ( *global* ) e-posta yapılandırmasını ayarlar.

Örnek 2: Git için genel kullanıcı adı yapılandırmasını ayarlar.

**Örnek 1 – Kod örneği:**

```bash
1
git config --global user.email "your.email@example.com"
```


**Örnek 2 – Kod örneği:**

```bash
1
git config --global user.name "Your Name"
```


---

### 📡 `git daemon`

**Açıklama:** Depodan anonim indirmeye izin vermek için kullanılır.

**Kod örneği:**

```bash
1
git daemon --reuseaddr --verbose
```


---

### 🔍 `git diff`

**Açıklama:** Başkalarının kodunuzu gözden geçirerek değişiklikleri belirlemesine ve karşılaştırmasına yardımcı olur.

**Kod örneği:**

```bash
1
git diff example.txt
```


---

### 🔄 `git fetch`

**Açıklama:** Değişiklikleri uzak depodan yerel depoya aktarmak için kullanılır.

**Kod örneği:**

```bash
1
git fetch <options> <remote name> <branch name>
```


---

### 🔄 `git fetch upstream/main`

**Açıklama:** *Upstream* branch’leri almak için kullanılır.

**Kod örneği:**

```bash
1
git fetch upstream main:upstream-main
```


---

### 📤 `git format-patch`

**Açıklama:** Linux çekirdeği tarzı genel forum iş akışını benimsiyorsanız e-posta gönderimini üretir veya hazırlar.

**Kod örneği:**

```bash
1
git format-patch -n <number_of_commits>
```


---

### 🌐 `git http-backend`

**Açıklama:** Git-over-HTTP için sunucu tarafı bir uygulama sağlar; hem *fetch* hem de *push* servislerine izin verir.

**Kod örneği:**

```bash
1
2
3
git clone --bare /path/to/repos/myrepo.git
cd myrepo.git
git update-server-info
```


---

### 📂 `git init`

**Açıklama:** Mevcut bir depoyu klonlamak için kullanılır.

**Kod örneği:**

```bash
1
git init <directory>
```


---

### 🌐 `git instaweb`

**Açıklama:** Git depolarına web ön yüzü kurmaya olanak tanır.

**Kod örneği:**

```bash
1
git instaweb -p 8080
```


---

### 📜 `git log`

**Açıklama:** Bir projedeki önceki değişiklikleri incelemeye olanak tanır.

**Kod örneği:**

```bash
1
git log -p filename
```


---

### 🔀 `git merge`

**Açıklama:** Etkin branch’teki değişiklikleri başka bir branch’e birleştirmek için kullanılır.

**Kod örneği:**

```bash
1
git merge feature_branch
```


---

### 🔀 `git merge upstream/main`

**Açıklama:** `upstream/main` branch’inden gelen değişiklikleri mevcut branch’e birleştirir.

**Kod örneği:**

```bash
1
git merge upstream/main
```


---

### 📥 `git pull`

**Açıklama:** Değişiklikleri uzak depodan yerel depoya aktarmak ve bunları bir branch’e birleştirmek için kullanılır.

**Kod örneği:**

```bash
1
git pull origin main
```


---

### 📥 `git pull downstream`

**Açıklama:** *Downstream* bir depodan, özellikle o deponun *main* branch’inden değişiklikleri çeker.

**Kod örneği:**

```bash
1
git pull downstream main
```


---

### 📥 `git pull upstream`

**Açıklama:** “upstream” deposundan mevcut branch’e değişiklik çeker.

**Kod örneği:**

```bash
1
git pull upstream main
```


---

### 📤 `git push`

**Açıklama:** Tüm commit’lenmiş değişiklikleri depoya *push* etmek için kullanılır.

**Kod örneği:**

```bash
1
git push origin your_branch_name
```


---

### 🌍 `git remote`

**Açıklama:** İzlenen depolar kümesini yönetmek için kullanılan bir komuttur.

**Kod örneği:**

```bash
1
git remote add upstream https://github.com/original/repo.git
```


---

### 🌍 `git remote add origin <URL>`

**Açıklama:** Belirtilen URL ile “origin” adlı uzak depo ekler.

**Kod örneği:**

```bash
1
git remote add origin https://github.com/yourusername/your-repo.git
```


---

### 🌍 `git remote add upstream`

**Açıklama:** Özgün depoyu *upstream* etiketiyle yeni bir uzak depo olarak ekler.

**Kod örneği:**

```bash
1
git remote add upstream https://github.com/original/repo.git
```


---

### 🌍 `git remote rename`

**Açıklama:** `git remote rename` komutunu, yeniden adlandırmak istediğiniz uzak deponun adı ( *origin* ) ve vermek istediğiniz yeni ad ( *upstream* ) takip eder.

**Kod örneği:**

```bash
1
git remote rename origin new-origin
```


---

### 🌍 `git remote -v`

**Açıklama:** Yerel depo ile ilişkili uzak depoları görüntülemeye olanak tanır.

**Kod örneği:**

```bash
1
git remote -v
```


---

### ✉️ `git request-pull`

**Açıklama:**

Örnek 1: *Upstream* tarafının alabilmesi için değişikliklerin özetini oluşturur.

Örnek 2: E-posta isteği için bekleyen değişikliklerin bir özetini üretir.

**Örnek 1 – Kod örneği:**

```bash
1
git request-pull origin/main your-branch
```


**Örnek 2 – Kod örneği:**

```bash
1
git request-pull <base> <head> <repository>
```


---

### 🧠 `git rerere`

**Açıklama:** Daha önce çözülmüş merge çatışmalarının kaydedilmiş çözümlerini yeniden kullanır.

**Kod örneği:**

```bash
1
2
git rerere
git rerere diff
```


---

### ⏪ `git reset`

**Açıklama:** Çalışma dizinindeki dosyalara yapılan değişiklikleri geri alır.

**Kod örneği:**

```bash
1
git reset HEAD~1
```


---

### ⏮️ `git revert`

**Açıklama:** Hatalı commit’leri geri almak için kullanılır.

**Kod örneği:**

```bash
1
git revert HEAD
```


---

### ✉️ `git send-email`

**Açıklama:**

Örnek 1: E-posta gönderiminizin MUA’nız ( *Mail User Agent* ) tarafından bozulmadan gönderilmesini sağlar.

Örnek 2: Bir dizi yamayı e-postalar olarak gönderir.

**Örnek 1 – Kod örneği:**

```bash
1
2
git send-email --to=recipient@example.com
path/to/patchfile.patch
```

**Örnek 2 – Kod örneği:**

```bash
1
2
git send-email --to recipient@example.com
patches/*.patch
```


---

### 🔐 `git-shell`

**Açıklama:** Paylaşılan merkezi depo kullanıcıları için kısıtlı bir giriş shell’i olarak kullanılır.

**Kod örneği:**

```bash
1
sudo usermod -s /usr/bin/git-shell gituser
```


---

### 📊 `git status`

**Açıklama:** Çalışma dizininizin durumunu ve staged hâlde bulunan değişikliklerin anlık görüntüsünü görmeye olanak tanır.

**Kod örneği:**

```bash
1
git status
```


---

### 🧾 `git version`

**Açıklama:** Sisteminize yüklü olan geçerli Git sürümünü görüntüler.

**Kod örneği:**

```bash
1
git --version
```
