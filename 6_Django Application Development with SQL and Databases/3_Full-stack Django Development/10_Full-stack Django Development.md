# 📚 Modül 3 Özeti: Full-stack Django Geliştirme

Bu modülü tamamladığınız için tebrikler. Kursun bu noktasında artık şunları biliyorsunuz:

---

### 🧩 Model-View-Controller (MVC) Tasarım Deseni

`Model-View-Controller` tasarım deseni, uygulama mantığını üç bileşene ayırır:

* **Model** veriye erişir ve veriyi işler.
* **View** veriyi çeşitli biçimlerde sunar.
* **Controller** Model ve View arasında koordinasyonu sağlar.

---

### 🧱 Django Model-View-Template Deseni

Django `Model-View-Template` deseni, MVC'ye benzer; ancak bir Controller yoktur ve denetleyici işlevini Django sunucusu yerine getirir.

---

### 🖼️ Django View

Django'da bir View, bir Web isteğini alan ve gerekli mantığı uygulayarak bir Web yanıtı üreten bir Python fonksiyonudur.

Django, statik HTML öğelerini ve özel Python kodunu içeren bir şablon kullanarak dinamik Web sayfaları üretir.

---

### 📁 Django Projesinin Çekirdek Dosyaları

Bir Django projesi oluşturduğunuzda, Django bazı çekirdek dosyalar oluşturur:

* `manage.py`, Django projesiyle etkileşime geçmek için kullanılan bir komut satırı arayüzüdür.
* `settings.py`, Django projenizin ayarlarını ve yapılandırmalarını içerir.
* `urls.py`, Django uygulamanızın URL ve yönlendirme tanımlarını içerir.

---

### 🛠️ Django Admin Sitesi

Bir Django admin sitesi oluşturmaya, bir admin kullanıcısı yaratarak başlarsınız.

Ardından süper kullanıcı olarak oturum açabilir ve modellerinizi yönetebilmek için admin sitesine kaydedebilirsiniz.

Admin formunu özelleştirebilir ve arama ile filtreler ekleyebilirsiniz.

---

### 🌐 Django View Yanıtları ve Şablonlar

Bir Django View, HTTP `GET`, `POST`, `DELETE` veya `UPDATE` gibi bir Web isteğini alır ve bir Web yanıtı döndürür. Web yanıtı, bir string, JSON/XML dosyası, HTML sayfası ya da istemci veya sunucu tarafındaki hataları belirten bir hata durumu olabilir.

Verilerinizin nasıl sunulacağını belirtmek için Django'da şablonlar oluşturursunuz. Bir Django şablonu, dinamik kısımların nasıl ekleneceğini tanımlamak için statik HTML öğelerini Django şablon etiketleri ve değişkenleriyle birleştirir. Bunlar birlikte çalışarak, kullanıcının Web tarayıcısında görüntülenen bir HTML sayfası üretir.
