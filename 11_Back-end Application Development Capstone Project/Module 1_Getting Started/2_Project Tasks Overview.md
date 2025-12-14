# 🎸 Proje Görevlerine Genel Bakış

Bir popüler müzik grubu için bir web sitesi geliştireceksiniz. Grubun hayranları ve diğer kullanıcılar sitede aşağıdaki işlemleri gerçekleştirebilecek:

* Geçmiş etkinliklerden fotoğrafları görmek
* Şarkıların popüler sözlerini görmek
* Yaklaşan etkinliklerin listesini görmek
* Hesap oluşturmak
* Giriş yapıp bir etkinliğe kayıt olmak
* Giriş yapıp geçmiş kayıtlarını görmek

---

# 🧩 Capstone Adımları

Projeyi başarıyla tamamlamak için aşağıdaki adımları izleyeceksiniz:

## 🖼️ Flask ile Get Pictures mikroservisini oluşturma

* Fotoğrafı bir kaynak (resource) olarak ele alıp CRUD endpoint’lerini oluşturun.
* Mikroservis için health endpoint’i oluşturun.

## 🎶 Flask ile Get Songs mikroservisini oluşturma

* MongoDB veritabanını kurun.
* Veritabanından şarkı sözlerini (song lyrics) getiren servisi uygulayın.
* Mikroservis için health endpoint’i oluşturun.

## 🕸️ Django ile Ana Uygulamayı oluşturma

* Concert model’ini oluşturun.
* Django’nun *built-in* user model’ini kullanın.
* SQLite veritabanında tabloları oluşturmak için model’i migrate edin.
* Önceden tanımlanmış template’lere veri göndermek için controller’ları uygulayın.

## 🚀 Servisleri ve uygulamayı deploy etme

* Get Pictures’ı IBM Code Engine’e deploy edin.
* Get Songs ve MongoDB’yi Redhat OpenShift’e deploy edin.
* Ana uygulamayı IBM Kubernetes Service’e deploy edin.

---

# 📸 Ekran Görüntüsü Gereksinimleri

Capstone boyunca, *peer review* için göndermek üzere sizden belirli noktalarda ekran görüntüsü almanız istenecek. Ayrıca, diğer katılımcıların gönderimlerini de değerlendirmeniz istenecek.

---

# 🏗️ Capstone Mimarisi

![1765570771781](image/2_ProjectTasksOverview/1765570771781.png)

1. Kullanıcı Django web sitesinin ana sayfasını ziyaret eder.

## 👤 Anonymous kullanım senaryoları

2. Şarkı sayfası şarkıları ve şarkı sözlerini gösterir.
3. Fotoğraflar sayfası geçmiş konserlerden fotoğrafları gösterir.

## 🛠️ Admin kullanım senaryoları

4. Admin kullanıcının konser tarihini değiştirmesine izin verin.

## 🔐 Signed in kullanım senaryoları

* Kullanıcı uygulamaya giriş yapar.
* Kullanıcı konserlerini görebilir.
* Kullanıcı bir konsere rezervasyon yapabilir.
* Kullanıcı rezervasyonunu silebilir.

---

# 🧮 Değerlendirme Kriterleri

* Dört modüle bölünmüş tüm notlandırılan quiz’ler için toplam **40 puan** mümkündür.
* Final proje için toplam **60 puan** mümkündür.

## 📚 Modül puan dağılımı

* **Module 1: Getting Started (10 pts)**
* **Module 2: Creating Get Songs Service with Flask (10 pts)**
* **Module 3: Main Django Application (10 pts)**
* **Module 4: Deploy your application and services (30 pts)**
