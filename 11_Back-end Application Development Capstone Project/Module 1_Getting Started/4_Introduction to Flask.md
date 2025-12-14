# 🚀 Introduction to Flask

“Introduction to Flask”e hoş geldiniz. Bu videoyu izledikten sonra şunları yapabileceksiniz: Flask web framework’ünü tanımlamak ve ana özelliklerini açıklamak. Flask’ı makinelerinize nasıl kuracağınızı açıklamak. Flask’ın ana bağımlılıklarını tanımlamak. Flask ile Django adlı başka bir Python web framework’ü arasındaki temel farkları açıklamak.

Flask, web uygulamaları oluşturabilen bir mikro framework’tür. Diğer bazı daha büyük framework’ler gibi *katı görüşlere sahip (opinionated)* değildir ve kullanıcıyı belirli bir araç setine bağlamaz.

Flask’ın karmaşık bağımlılıklarından biri Python’dur. Flask 2.2.2 çalıştıracaksınız; bu sürüm minimum *Python 3.7* sürümünü gerektirir. 2004 yılında Armin Ronacher bu framework’ü bir *1 Nisan şakası* olarak oluşturdu. Kullanım kolaylığı ve genişletilebilirliği sayesinde hızla popülerlik kazandı. Flask, bir web uygulaması oluşturmak için ihtiyaç duyabileceğiniz minimum bağımlılıkları sağlar. Bununla birlikte genişletilebilirdir ve birçok topluluk eklentisi (community extension) Flask’a ek özellikler kazandırır.

## 🧩 Flask’ın Ana Özellikleri

Flask’ın ana özellikleri şunları içerir:

Flask, uygulamaları geliştirme modunda çalıştıran bir web sunucusuna sahiptir.

Flask ayrıca uygulamaları hata ayıklamaya yardımcı olan bir debugger ile gelir. Debugger, tarayıcıda etkileşimli traceback ve stack trace gösterir.

Flask, uygulama log’ları için standart Python logging’i kullanır. Uygulamanız hakkında özel mesajlar log’lamak için aynı logger’ı kullanabilirsiniz.

Flask, uygulamanızın farklı bölümlerini test etmenin bir yolunu sağlar. Test özelliği, geliştiricilerin test odaklı (test-driven) bir yaklaşım izlemesini mümkün kılar. Kodunuzun istendiği gibi çalıştığından emin olmak için *pytest* ve *coverage* gibi framework’leri kullanabilirsiniz.

Geliştiriciler, argümanları çekmek ve yanıtları özelleştirmek için request ve response nesnelerine erişebilir.

## 🧰 Flask’ın Ek Özellikleri

Flask’ın ek özellikleri şunlardır:

Framework, CSS dosyaları, JavaScript dosyaları ve görseller gibi statik varlıkları destekler. Flask, template’lerde statik dosyaları yüklemek için etiketler sağlar.

Ayrıca *Jinja* templating framework’ünü kullanarak dinamik sayfalar geliştirebilirsiniz. Bu dinamik sayfalar, her istek için değişebilecek bilgileri gösterebilir veya kullanıcının giriş yapıp yapmadığını kontrol edebilir.

Flask routing sağlar ve RESTful servisler için son derece kullanışlı olan dinamik URL’leri destekler. Farklı HTTP method’ları için route’lar oluşturabilir ve uygulamanızda yönlendirme (redirection) sağlayabilirsiniz.

Flask’ta uygulama seviyesinde çalışan global error handler’lar yazabilirsiniz. Son olarak, kullanıcı oturum (session) yönetimini destekler.

## 🧩 Popüler Topluluk Eklentileri

Uygulamanıza eklenebilecek bazı popüler topluluk eklentileri şunlardır:

 *Flask-SQL Alchemy* , SQL Alchemy adlı bir ORM için Flask’a destek ekler ve geliştiricilere Python’da veritabanı nesneleriyle çalışma imkânı verir.

 *Flask-Mail* , bir SMTP mail sunucusu kurma yeteneği sağlar.

 *Flask-Admin* , Flask uygulamalarına kolayca admin arayüzleri eklemenizi sağlar.

 *Flask-Uploads* , uygulamanıza özelleştirilmiş dosya yükleme eklemenizi sağlar.

İşte bazı diğer eklentiler:

 *Flask-CORS* , uygulamanızın Cross-Origin Resource Sharing’i işlemesini sağlayarak cross-origin JavaScript isteklerini mümkün kılar.

 *Flask-Migrate* , SQL Alchemy ORM’e veritabanı migration’ları ekler.

 *Flask-User* , kullanıcı kimlik doğrulama (authentication), yetkilendirme (authorization) ve diğer kullanıcı yönetimi aktivitelerini ekler.

 *Marshmallow* , kodunuza kapsamlı nesne serileştirme/serileştirme geri alma (serialization/deserialization) desteği ekler.

Son olarak, *Celery* basit arka plan görevleri ve karmaşık çok aşamalı programlar ile zamanlamalar için kullanılabilen güçlü bir task queue’dur.

## 📦 Flask Kurulumu

Flask, *pip* adlı Python paket yöneticisinde mevcuttur. Pip, lab ortamında kullanılabilir. Kendi makinelerinize kurulum yapıyorsanız, önce *venv* veya *pipenv* modülünü kullanarak bir virtual environment oluşturmanız önerilir.

Flask 2.2.2 sürümünü kurabilirsiniz. Uygulamanızdaki bağımlılıkların sürüm numarasını sabitlemeniz (pin) önerilir. Bu, uygulamanın geliştirme (development), staging ve production gibi farklı ortamlarda sıfırdan yeniden üretilebilmesini sağlar. Ayrıca paketler sürüm numarası olmadan otomatik güncellendiğinde yeni sorunların ve bug’ların yanlışlıkla sisteme girmesini engeller.

## 🧱 Flask’ın Yerleşik Bağımlılıkları

Flask, çeşitli özellikleri etkinleştiren bazı yerleşik bağımlılıklarla gelir.

 *Werkzeug* , WSGI (Web Server Gateway Interface)’yi uygular. Bu, uygulamalar ile sunucular arasındaki standart Python arayüzüdür.

 *Jinja* , uygulamanızdaki sayfaları render eden bir template dilidir.

 *MarkupSafe* , Jinja ile birlikte gelir. Template’leri render ederken güvenilmeyen girdiyi escape ederek injection saldırılarını önlemeye yardımcı olur.

 *ItsDangerous* , veriyi güvenli şekilde imzalamak için kullanılır. Bu, verinin kurcalanıp kurcalanmadığını belirlemeye yardımcı olur ve Flask’ın session cookie’sini korumak için kullanılır.

 *Click* , komut satırı uygulamaları yazmak için bir framework’tür. *flask* komutunu sağlar ve özel yönetim komutları eklemeye izin verir.

Yerleşik bağımlılıkları görmek için, sanal ortamda kurulu paketleri listelemek üzere *pip freeze* komutunu kullanabilirsiniz. Tüm yerleşik paketlerin varsayılan olarak kurulduğunu görebilirsiniz.

```bash
pip freeze
```

## 🆚 Flask ve Django Arasındaki Farklar

Şimdi başka bir Python geliştirici framework’ü olan Django’ya geçelim. Flask ve Django arasındaki bazı temel farklar şunlardır:

Flask, çok hafif (very light) bir framework olmayı hedefler. Django ise tam kapsamlı (full-stack) bir framework’tür. Sonuç olarak Flask, web uygulaması oluşturmak için gerekli olan temel bağımlılıkları sağlar. Bununla birlikte çok genişletilebilirdir ve geliştiricinin ek özellikler sağlayan eklentileri seçmesine izin verir.

Django ise tam kapsamlı bir uygulama oluşturmak için gereken her şeyi içerir.

Flask çok esnektir. Parçaları tak-çalıştır (plug-and-play) şeklinde ekleyip çıkarabilirsiniz. Öte yandan Django oldukça opinionated’tır ve çoğu kararı geliştirici adına verir; böylece geliştirici uygulamanın mantığına odaklanabilir.

## ✅ Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

Flask, minimum bağımlılıklarla gelen bir mikroframework’tür.

Web siteleri oluşturmak için Flask; debugging server’lar, routing, template’ler ve error handling gibi özelliklere sahiptir.

Flask, topluluk eklentileri kullanılarak genişletilebilir.

Flask, bir Python paketi olarak kurulabilir.

Django, Flask’a kıyasla full-stack bir framework’tür.
