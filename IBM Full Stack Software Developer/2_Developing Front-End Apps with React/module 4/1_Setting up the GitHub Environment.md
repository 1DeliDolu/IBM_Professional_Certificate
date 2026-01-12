# 🧪 Laboratuvar: GitHub Ortamını Kurma

**Tahmini gereken süre:** 15 dakika

---

## 📚 Ne öğreneceksiniz?

Bu laboratuvarda, proje için çevrimiçi bir depo oluşturacak ve *Skills Network Environment* içinde klasörler ve dosyalar oluşturmayı öğreneceksiniz. Ayrıca kodunuzun çıktısını nasıl görüntüleyeceğinizi anlayacaksınız.

---

## 🎯 Öğrenme hedefleri

Bu laboratuvarı tamamladıktan sonra şunları yapabileceksiniz:

* Çevrimiçi bir depo oluşturma.
* *Skills Network Environment* içinde klasörler ve dosyalar oluşturma.
* React uygulamasını oluşturma ve çalıştırma.
* Git işlemlerini gerçekleştirme.

---

## ✅ Ön koşullar

* Ön koşul derslerini, özellikle *Getting Started with Git and GitHub* kursunu tamamlamış olmalısınız.
* Bir *GitHub* hesabınız olmalıdır. Bir *GitHub* hesabı oluşturmak istiyorsanız, ayrıntılı adımlar için buraya tıklayın.

---

## 🔧 Git komutlarını çalıştırma ihtiyacı

Verilerinizin bir *GitHub* deposunda doğru şekilde yönetilmesini ve kalıcı olmasını sağlamak için birkaç temel adımı takip etmek kritik önemdedir:

* **Düzenli güncellemeler:** Projenizde değişiklik yaptığınızda veya yeni bileşenler eklediğinizde, güncellemeleri *GitHub* deponuza eklemek, commit etmek ve push etmek önemlidir. Bu süreç, en son çalışmanızın güvenli şekilde saklanmasını ve iş birliği yapanlar tarafından erişilebilir olmasını sağlar.
* **Oturum kalıcılığı:** Etkin bir oturum sırasında verileriniz erişilebilir durumda kalır. Ancak oturumunuzun süresi dolarsa veya çıkış yaparsanız, çalışmaya devam etmek için depoyu tekrar clone etmeniz gerekir.

---

## 🧩 Görev 1: Deponuzu oluşturun ve kişisel erişim belirteci üretin

1. *GitHub* hesabınızda, herhangi bir **README.md** dosyası oluşturmadan boş bir genel ( *public* ) *GitHub* deposu oluşturun. Deponuzu **public** olarak ayarladığınızdan ve uygun şekilde adlandırdığınızdan emin olun.
2. Daha fazla bilgi için *GitHub Sign Up and Create Repo* laboratuvarına bakabilirsiniz.
3. Dosyaları bir *GitHub* deposuna push etmek için, kimlik doğrulamanızın *GitHub* hesabınıza bağlı olduğundan emin olmak üzere bir *Personal Access Token* gereklidir.
4. Bir *Personal Access Token* oluşturmak için *GitHub* hesabınıza gidin ve sağ üst köşedeki profil simgenize tıklayın. Ardından **Settings** seçeneğine tıklayın.
5. Sonra **Developer settings** seçeneğini seçin. Bu seçenek genellikle pencerenin alt kısmında yer alır.
6. *Personal access tokens* altında **Tokens (classic)** bölümüne gidin.
7. Bir erişim belirteci oluşturmak için **Generate a personal access token** seçeneğine tıklayın.
8. *Generate token* sayfasında gerekli ayrıntıları doldurun ve git komutları için erişimi etkinleştirmek üzere **repo** onay kutusunu işaretleyin.
9. Ardından **Generate token** seçeneğine tıklayın.
10. Kişisel erişim belirteciniz oluşturulacaktır. Belirteç yalnızca **30 gün** geçerlidir. Mevcut belirtecin süresi dolduğunda yeni bir belirteç oluşturmanız gerekecektir.

**UNUTMAYIN:** Kişisel erişim belirtecinizi şimdi kopyaladığınızdan emin olun. Onu bir daha göremeyeceksiniz! Kaydetmeyi unuttuysanız veya kaybettiyseniz, daha önce oluşturulan belirteci silin ve yenisini oluşturun.

---

## 🗂️ Görev 2: Skills Network Environment içinde dosyalar oluşturun

1. *Skills Network Environment* içinde bir terminal açık değilse, pencerenin sağ üst kısmındaki **Terminal** sekmesini seçin ve açılır menüden **New Terminal** seçeneğine tıklayın.
2. React uygulaması oluşturmak için aşağıdaki adımları izleyin. Terminale şu komutu yazın:

```bash
npm create vite@latest
```

Terminal, verilen ekrana benzer görünmelidir. Ardından devam etmek isteyip istemediğiniz sorulacaktır; bunun için **Enter** tuşuna basmanız gerekir.

3. Sonraki adımda, aşağıdaki ekranda gösterildiği gibi proje adını girmeniz istenecektir. **learning_react** adlı projeyi yazın ve  **Enter** ’a basın. Proje adının küçük harflerle olması gerektiğinden emin olun. Referans için verilen ekran görüntüsüne bakabilirsiniz.
4. Gösterilecek listeden bir framework seçin. Ok tuşlarını kullanarak  **React** ’i seçin ve  **Enter** ’a basın.
5. Ok tuşlarını kullanarak **JavaScript** varyantını seçin ve ardından  **Enter** ’a basın.

Yukarıdaki adımlar tamamlandıktan sonra, uygulama adı **learning_react** olan bir klasör oluşturacaktır. Terminalde, aşağıdaki ekranda gösterildiği gibi belirli komutları çalıştırmanız istenecektir.

6. Şimdi terminali kullanarak oluşturduğunuz uygulama klasörünün içine girmeniz gerekir. Bunun için aşağıdaki komutu çalıştırın:

```bash
cd learning_react
```

7. Terminale yazarak **npm install** komutunu çalıştırın. Bu komut, React uygulamasını çalıştırmak için gerekli tüm dosyaları yükleyecektir.

```bash
npm install
```

8. Şimdi **learning_react** klasörü altındaki **package.json** dosyasına gidin. **script** nesnesi altında bulunan **preview** anahtarına aşağıdaki kodu ekleyin:

```json
"preview": "vite build; vite preview --host"
```

**script** nesnesinin, verilen ekran görüntüsündeki gibi göründüğünden emin olun.

9. Sonraki adımlar React uygulamanızı çalıştırmanıza olanak sağlayacaktır. Şimdi, verilen ekran görüntüsünde 1 numarada gösterilen **Explorer** simgesine tıklayın; ardından kıvrımlı oku ( *twisty arrow* ) tıklayarak proje klasörünü genişletin. React uygulamanızın tüm klasör yapısını göreceksiniz.
10. Bundan sonra, uygulamayı çalıştırmak için terminalde aşağıdaki komutu girin:

```bash
npm run preview
```

Terminaliniz, **Local** kelimesiyle başlayan bir satır ve ardından localhost yolu ile bir port numarası gösterecektir. Aşağıda örnek bir ekran görebilirsiniz; burada port numarası  **4173** ’tür. Bu port, React uygulamanızı çalıştıracaktır.

---

## 🖥️ Görev 3: Çıktınızı kontrol edin

Sonraki adımda, çıktınızı bir tarayıcıda görüntülemek için gerekli adımları uygulayacaksınız.

1. IDE ortamının sol alt kısmındaki *Skills Network* simgesini seçin (ekran görüntüsünde 1 numarada gösterilmiştir). Bu işlem  **“Skills Network Toolbox”** ’ı açacaktır.
2. Bu işlem  *Skills Network Toolbox* ’ı açacaktır. Ardından **Launch Application** seçeneğine tıklayın (2 numaraya bakın).
3. **Application Port** alanına **4173** port numarasını girin (3 numaraya bakın) ve **[↗]** simgesine tıklayın.
4. React uygulaması varsayılan tarayıcınızı açacak ve aşağıdaki gibi çıktıyı göreceksiniz.

---

## 🧰 Görev 4: Terminalde Git komutlarını gerçekleştirin

1. Şimdi, pencerenin sağ üst kısmındaki **Terminal** sekmesini seçin ve açılır menüden **New Terminal** seçeneğine tıklayın (ekran görüntüsünde belirtildiği gibi). Terminal yolunuzun **/home/project/** şeklinde okuduğundan emin olun. Ayrıca, **cd <learning_react>** kısmında **<learning_react>** ifadesini kendi proje adınızla değiştirmelisiniz.
2. Sonra, bu terminalde tüm Git komutlarını çalıştırabilmek için terminali başlatıp bir Git deposu oluşturun. Verilen komutu kullanın ve  **Enter** ’a basın:

```bash
git init
```

3. Ardından, *Skills Network Environment* içinde gerekli komutları çalıştırabilmek için terminali yapılandırmanız gerekir:

```bash
git config --global --add safe.directory /home/project
```

 **Enter** ’a basın.

**Önemli**
**git config** komutu, proje klasörü ortamınız içinde git komutlarını kullanarak çalışmanıza yardımcı olacaktır.

4. Sonrasında, git’i e-posta adresinizle yapılandırmanız gerekir. **[you@example.com](mailto:you@example.com)** ifadesini kendi e-posta adresinizle değiştirin. E-posta adresinizin çift tırnak içinde olduğundan emin olun:

```bash
git config --global user.email "you@example.com"
```

 **Enter** ’a basın.

Şimdi, kullanıcı adınızı ayarlamak için config komutunu kullanmalısınız. **Your Name** ifadesini kendi adınızla değiştirin ve çift tırnak kullandığınızdan emin olun:

```bash
git config --global user.name "Your Name"
```

5. Ardından, değişiklikleri *GitHub* deposu için kaydetmek üzere **git add** ve **git commit** komutlarını çalıştırın. Aşağıdaki komutları sırayla çalıştırın:

```bash
git add --a
```

```bash
git commit -m "initial commit"
```

6. Dosyaları *GitHub* deponuza push etmek için git push komutlarını uygulayın. *GitHub* deponuzda ana dalı ayarlamanız gerekir:

```bash
git branch -M main
```

7. *GitHub* depo URL’nizi bir **origin** değişkenine ekleyin. Ayrıca ifadesini kendi *GitHub* depo URL’nizle değiştirin. Örneğin:

```bash
git remote add origin https://github.com/<youraccountname>/<yourrepositoryname>
git remote add origin <git-repo-url>
```

 **Enter** ’a basın.

8. Sonra, dosyalarınızın içeriğini *GitHub* deponuza push edin:

```bash
git push -u origin main
```

 **Enter** ’a basın.

**Önemli**
Yukarıdaki komut, ilk push işleminizi tüm değişikliklerinizi doğrudan **main** dalına yükleyecek şekilde ayarlar. Bunu yalnızca bir kez yapmanız gerekir. Bundan sonra **git push** da aynı işlemi yapacaktır.

9. *GitHub* ’a **git push** komutunu kullanarak dosyaları push ederken, terminal sizden *GitHub* hesabınız için kullanıcı adınızı ve parolanızı girmenizi isteyecektir. Kullanıcı adınızı girin ve  **Enter** ’a basın. Parolanız için, 1. adımda oluşturduğunuz  *Personal Access Token* ’ı yapıştırmanız gerekir.

**Önemli**
 *Personal Access Token* ’ınızı terminale yapıştırdığınızda güvenlik nedeniyle görünmeyecektir, ancak oradadır. Sadece  **Enter** ’a basın; dosya ve klasörleriniz *GitHub* deposuna push edilecektir.

10. Tüm dosyalarınız *GitHub* dizininize push edilmiştir.

**Not:** Git komutları hakkında daha fazla ayrıntı için *Hands-on Lab: Getting Started with Branches using Git Commands* bölümüne de başvurabilirsiniz.

---

## 🚀 Görev 5: GitHub Pages kullanarak dağıtım yapın

1. React uygulamanızı  *GitHub* ’da dağıtmak için **gh-pages** yüklemeniz gerekir. Bu, projenizi  *GitHub Pages* ’a dağıtmak için bir araç olarak kullanmanıza olanak sağlar. Terminalde şu komutu çalıştırın:

```bash
npm install gh-pages --save-dev
```

2. **package.json** dosyasında, `"build": "vite build"` satırından önce aşağıdaki satırları ekleyin:

```json
"predeploy": "npm run build",
"deploy": "gh-pages -d dist",
```

3. Ardından **vite.config.js** dosyasında, `plugins: [react()]` satırından önce şu satırı ekleyin:

```js
base: "/YOUR_REPOSITORY_NAME",
```

**Not:** `<YOUR_REPOSITORY_NAME>` yerine kendi depo adınızı yazın. Örneğin *GitHub* deponuzun adı **learning_react** ise şu şekilde görünmelidir: `base: "/learning_react"`

4. Şimdi terminalde deploy komutunu çalıştırın. Bu komut, **package.json** dosyasında tanımlanan `"deploy"` betiğini çalıştırarak projeyi **gh-pages** aracıyla  *GitHub Pages* ’a dağıtır:

```bash
npm run deploy
```

**Not:** Kodunuzda herhangi bir değişiklik yaptığınızda tüm dosyalarınızı kaydetmeniz ve onlar için git komutlarını çalıştırmanız gerekir.

5. Kodunuzdaki değişiklikleri güncellemek için **git add** ve **git commit** komutlarını çalıştırın. Ardından, *GitHub* deponuzu uygun kod yönetimi için güncellemek amacıyla **git push** komutunu çalıştırın.
6. *GitHub* deponuza gidin. Ardından, oluşturduğunuz site deposuna gidin.
7. Depo adınızın altında  **Settings** ’e tıklayın.
8. Sol taraftaki gezinme çubuğunda, yan çubukta **Code and Automation** bölümünde  **Pages** ’e tıklayın.
9. Aşağıdaki sayfayı göreceksiniz. **None** yazan açılır menüye tıklayın, sonra  **gh-pages** ’i seçin ve ardından **Save** düğmesine tıklayın.
10. Sayfanızı tekrar yenileyin; aşağıdaki gibi bağlantıyı göreceksiniz. **shoppingreact** yerine kendi *GitHub* depo adınızı göreceksiniz.

**Not:** Bağlantıyı göremiyorsanız, lütfen **(1-2)** dakika bekleyin ve sayfayı tekrar yenileyin.

11. Canlı web sitenizi görmek için oluşturulan bağlantıya tıklayın.

---

## 📝 Not

1. Varsayılan React uygulamanızda herhangi bir değişiklik yapmadıysanız, görev 3, adım 6 için aşağıda gösterilene benzer bir çıktı görmelisiniz.
2. *GitHub Pages* üzerinde dağıtımdan sonra, tüm içeriklerin ve görsellerin düzgün görünmesi biraz zaman alabilir. Uygulamanın tamamen yüklenmesi için lütfen birkaç dakika daha bekleyin.

Bu yönergelere uyarak, iyi organize edilmiş ve verimli bir *GitHub* deposunu sürdürebilir; çalışmanızın güvenli şekilde saklanmasını ve sizinle iş birliği yapanlar için kolay erişilebilir olmasını sağlayabilirsiniz.

---

## 👤 Yazar(lar)

Richa Arora

© IBM Corporation. Tüm hakları saklıdır.
