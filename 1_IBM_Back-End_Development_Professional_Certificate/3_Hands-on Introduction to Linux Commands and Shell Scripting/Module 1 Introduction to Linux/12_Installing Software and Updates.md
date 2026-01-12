# 💿 Yazılım ve Güncellemelerin Kurulması

Yazılım ve Güncellemelerin Kurulması’na hoş geldiniz.

Bu videoyu izledikten sonra şunları yapabileceksiniz:

* Paketleri ve paket yöneticilerini açıklamak
* **deb** ve **RPM** tabanlı dağıtımlar için paketleri ayırt etmek
* Güncellemeleri yüklemek için bir paket yöneticisi kullanmak
* Yazılım kurmak için bir paket yöneticisi kullanmak

---

## 📦 Paketler ve Paket Yöneticileri

Hem yazılım güncellemeleri hem de Linux işletim sistemleri için yazılım kurulum dosyaları, **paketler** olarak bilinen dosyalar hâlinde dağıtılır.

Bu paketler, yeni yazılım kurmak veya mevcut yazılımları güncellemek için gereken bileşenleri içeren **arşiv (archive)** dosyalarıdır.

Paketlerin indirilmesini ve kurulmasını yönetmek için **paket yöneticilerini (package managers)** kullanırsınız.

Farklı Linux dağıtımları, farklı paket yöneticileri sağlar — bazıları  **GUI tabanlı** , bazıları ise **komut satırı aracı**dır.

---

## 📁 deb ve RPM Paket Türleri

Linux işletim sistemlerinde paket yöneticileri tarafından **Deb** ve **RPM** paketleri kullanılır.

Bunlar, farklı Linux işletim sistemleri için yazılım veya güncellemeler içeren  **farklı dosya türleridir** .

* `.deb` dosyaları;  **Debian** , **Ubuntu** ve **Mint** gibi Debian tabanlı dağıtımlarda kullanılır.

  **Deb** , *Debian* anlamına gelir.
* `.rpm` dosyaları;  **CentOS/RHEL** , **Fedora** ve **openSUSE** gibi Red Hat tabanlı dağıtımlarda kullanılır.

  **RPM** , *Red Hat Package Manager* ifadesinin kısaltmasıdır.

**Deb** ve **RPM** biçimleri eşdeğerdir, bu nedenle dosya içeriği diğer Linux işletim sistemi türlerinde de kullanılabilir.

---

## 🔁 Paket Dönüştürme: `alien` Aracı

Kullanmak istediğiniz bir paket yalnızca diğer biçimde mevcutsa, bunu **`alien`** aracıyla dönüştürebilirsiniz.

* Paketleri **RPM biçiminden deb biçimine** dönüştürmek için, `alien` komutunu kullanır ve dönüştürmek istediğiniz paketin adını belirtirsiniz.
* **RPM biçimine dönüştürmek** için, `alien` komutu ile birlikte `-r` anahtarını (switch) kullanırsınız.

---

## ✅ Paket Yöneticilerinin Sağladığı Faydalar

Paket yöneticileri çeşitli avantajlar sağlar:

* Paketler arasındaki **bağımlılıkları (dependencies)** otomatik olarak çözebilirler.
* Güncellemeler mevcut olduğunda sizi  **bildirimle haberdar edebilirler** .
* GUI tabanlı paket yöneticileri, güvenlik ve yazılım güncellemelerini düzenli aralıklarla  **otomatik olarak kontrol edebilir** .
* Güncellemeleri otomatik olarak kurabilir ya da yalnızca **istediğiniz güncellemeleri seçip kurmanıza** izin verebilirler.

---

## 🖼️ GUI Tabanlı Paket Yöneticileri: PackageKit ve Update Manager

GUI tabanlı Linux dağıtım paket yöneticilerine **PackageKit** ve **Update Manager** dahildir.

 **Update Manager** , deb tabanlı Linux sistemlerini güncellemek için kullanılan bir GUI aracıdır.

Varsayılan olarak Update Manager:

* Yazılım güncellemelerini **günlük** olarak kontrol eder,
* Her gün, mevcut  **güvenlik güncellemelerini otomatik olarak indirir ve kurar** ,
* Diğer tüm güncellemeleri ise **haftalık** olarak görüntüler.

Ayrıca, istediğiniz zaman  **manuel olarak güncellemeleri kontrol edebilirsiniz** .

---

## 🔔 Update Manager ile Güncelleme Adımları

Update Manager, yazılım güncellemeleri mevcut olduğunda sizi bilgilendirir:

1. Kurmak istediğiniz güncellemeleri seçin.
2. **“Install Updates”** (Güncellemeleri Kur) seçeneğine tıklayın.
3. İstenirse, kullanıcı parolanızı girin ve **OK** düğmesine tıklayın.

Update Manager, siz çalışmaya devam ederken güncellemeleri  **arka planda kurar** .

---

## 💻 Komut Satırında `apt` ile Güncelleme

 **`apt`** , deb tabanlı Linux sistemlerini güncellemek için kullanılan bir komut satırı aracıdır.

Dağıtımınız için mevcut paketleri bulmak üzere şu komutu kullanırsınız:

```bash
sudo apt update
```

Bu komutun çıktısı:

* Mevcut her paketi listeler,
* Bir **bağımlılık ağacı (dependency tree)** oluşturur,
* Kaç paketin yükseltilebileceğini (upgrade edilebileceğini) bildirir.

Sistemde yüklü tüm paketleri yükseltmek için şu komutu kullanırsınız:

```bash
sudo apt upgrade
```

Yalnızca belirli bir paketi kurmak isterseniz, aşağıdaki komutu kullanabilirsiniz:

```bash
sudo apt install package_name
```

---

## 🪟 RPM Tabanlı Sistemler için GUI: PackageKit

 **PackageKit** , RPM tabanlı Linux sistemlerini güncellemek için kullanılan bir GUI aracıdır.

Güncellemeler mevcut olduğunda, PackageKit bildirim alanında **“yıldız patlaması (starburst)” simgesi** gösterir.

* Yapılandırılabilir bir aralıkta güncellemeleri otomatik olarak kontrol eder.
* İstediğiniz zaman  **manuel olarak da güncellemeleri kontrol edebilirsiniz** .

Yıldız patlaması simgesine tıklamak, tüm mevcut yazılım güncellemelerini listeleyen **Software Update** penceresini açar:

1. Kurmak istediğiniz güncellemeleri seçin.
2. **Install Updates** düğmesine tıklayın.
3. İstenirse, kullanıcı parolanızı girin ve **OK** düğmesine tıklayın.

PackageKit, siz çalışmaya devam ederken güncellemeleri  **arka planda kurar** .

---

## 💻 Komut Satırında `yum` ile Güncelleme

 **`yum`** , RPM tabanlı sistemleri güncellemek için kullanılan bir komut satırı aracıdır.

`yum`, *Yellowdog Updater, Modified* ifadesinin kısaltmasıdır.

Sistemdeki tüm paketleri güncellemek için şu komutu yazarsınız:

```bash
sudo yum update
```

Parolanızı girdikten sonra `yum`:

* Mevcut tüm paket güncellemelerini getirir (fetch eder),
* Güncellemelerin özetini görüntüler ve sizden indirme işlemini  **onaylamanızı ister** .

Onaylarsanız, `yum`:

* Tüm paket güncellemelerini indirir,
* Sistemdeki paketleri günceller.

İşlem tamamlandığında, başarı mesajı olarak `"Complete!"` ifadesini görüntüler.

---

## 📥 Yeni Yazılım Kurmak: `apt` ve `yum` ile

Yeni yazılımlar kurmak için de komut satırı araçlarını kullanabilirsiniz.

* Deb tabanlı bir sistemde bir paketi kurmak için `apt` komutunu **install anahtarı** ile kullanırsınız.
* RPM tabanlı bir sistemde yazılım kurmak için `yum` komutunu **install anahtarı** ile kullanırsınız.

---

## 🐍 Python Paket Yöneticileri: `pip` ve `conda`

Birçok yazılım uygulaması, **Python ortamlarını yönetmek** için, popüler *pip* veya *conda* paketleri gibi **paket yöneticilerini** kullanır.

Örneğin, hâlihazırda bir Python ortamına ve ilgili `pip` paketine sahip olduğunuzu varsayarsak, Python’da veri düzenleme (data wrangling) için kullanılan popüler **“pandas”** kütüphanesini kolayca kurabilirsiniz.

Aşağıdaki komutu girerek:

```bash
pip install pandas
```

`pip` paket yöneticisine şunları yapmasını söylemiş olursunuz:

* En güncel **pandas** paketini aramak,
* **pandas** paketini indirmek,
* Bağımlılıkları kontrol etmek ve gerektiğinde güncellemek,
* Ve **pandas** paketini kurmak.

Kurulum tamamlandığında, paket yöneticisi yeni yazılımın **sürüm numarasını** görüntüler.

---

## 🧾 Özet

Bu videoda şunları öğrendiniz:

* `.deb` ve `.rpm`, Linux işletim sistemlerinde paket yöneticileri tarafından kullanılan  **farklı dosya türleridir** .
* **Deb** ve **RPM** biçimleri, birinden diğerine dönüştürülebilir.
* **Update Manager** ve  **PackageKit** , sırasıyla deb ve RPM tabanlı dağıtımlarda kullanılan popüler  **GUI tabanlı paket yöneticileridir** .
* **`apt`** ve  **`yum`** , sırasıyla deb ve RPM tabanlı dağıtımlarda kullanılan popüler  **komut satırı paket yöneticileridir** .
