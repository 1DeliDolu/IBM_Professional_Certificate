# 🧩 Django Model-View-Template (MVT) Deseni

Standart *Model-View-Controller (MVC)* deseninin Django’daki uygulaması olan *Django Model View Template (MVT)* desenine hoş geldiniz.

Bu videoyu izledikten sonra şunları yapabileceksiniz:

* *Model-View-Controller (MVC)* desenini açıklamak
* *Django Model View Template (MVT)* desenini açıklamak

![1765195897088](image/1_DjangoModel-View-Template(MVT)Pattern/1765195897088.png)

---

## 🧱 Model-View-Controller (MVC) Tasarım Deseni

*MVC* tasarım deseni, uygulama mantığını üç bileşene ayırır.

 *Model* , verilere erişir ve onları işler, ancak veriyi sunmaz.

 *Model* , `SQL` veya *ORM* gibi veritabanı arayüzlerine sahip olabilir ya da ham veriyi işlemek için iş mantığını kullanabilir.

 *View* , veriyi bir web sayfasındaki görsel öğeler, bir mobil uygulama kullanıcı arayüzü ya da `JSON`/`XML` formatı gibi çeşitli biçimlerde sunar.

 *Controller* , *Model* ve *View* arasında koordinasyonu sağlar.

İstekleri yönlendirir, girdiyi işler,  *Model* ’den veri üzerinde `CRUD` işlemleri ister ve  *View* ’i günceller.

![1765195932421](image/1_DjangoModel-View-Template(MVT)Pattern/1765195932421.png)

---

## 🔁 İstek Akışı ve Controller’ın Rolü

Bir istemci uygulaması girdilerle birlikte  *Controller* ’a bir istek gönderdiğinde, *Controller* isteği yönlendirir, girdiyi doğrular ve işler,  *Model* ’e `CRUD` istekleri gönderir ve sunulmak üzere veriyi  *View* ’e iletir.

---

## 🧠 Django’da Controller ve MVT Deseni

Django framework’ünün uygulamasında, açıkça tanımlanmış bir *Controller* yoktur.

Bunun yerine, bu işlevi doğrudan Django sunucusunun kendisi yerine getirir.

 *Django Model* , veri modellemesini ve veritabanı eşlemesini, ayrıca veriyi işlemek için kullanılan iş mantığını yönetir.

 *Django View* , hangi verinin sunulacağını tanımlar, ancak nasıl sunulacağını tanımlamaz.

Genellikle  *View* , verinin nasıl sunulacağını tanımlayan bir şablona ( *template* ) işi devreder.

Bir istemci bir istek gönderdiğinde, Django sunucusu bu isteği Django URL yapılandırmasına göre uygun  *view* ’a yönlendirir.

Dolayısıyla Django, *Model-View-Template (MVT)* adı verilen bir tasarım desenini izler.

Öğrendiğimiz gibi, Django modelleri veritabanı tablolarına eşlenen sınıflardır.

![1765195991435](image/1_DjangoModel-View-Template(MVT)Pattern/1765195991435.png)

---

## 🗄️ Django Model ve Model API’leri

 *Django Model API’leri* , geliştiricilerin nesneler üzerinde `CRUD` işlemleri yapmasına olanak tanır ve geliştiriciler ayrıca Django model sınıflarına fonksiyonlar şeklinde iş mantığı da yazabilirler.

![1765196015179](image/1_DjangoModel-View-Template(MVT)Pattern/1765196015179.png)

---

## 👀 Django View ve Web Yanıtları

Django’da bir *View* esasen bir Python fonksiyonudur.

Bu fonksiyon, bir web isteğini alır ve bir web yanıtı üretmek için gerekli mantığı uygular; bu yanıt bir web sayfasının `HTML` içeriği, bir yönlendirme ( *redirect* ), bir `404` hatası, bir `XML` dokümanı, bir resim ya da başka herhangi bir web yanıtı olabilir.

![1765196046341](image/1_DjangoModel-View-Template(MVT)Pattern/1765196046341.png)

---

## 🧬 Django Template ve Dinamik İçerik

Çoğu zaman  *View* , bir web yanıtı üretmek için gereken veriyi `QuerySet` ya da nesneler biçiminde almak üzere *Django Model* ile etkileşime girer.

Django, kullanıcıya geri gönderilen ve tarayıcıda işlenen dinamik web sayfalarını üretmek için bir şablon ( *template* ) kullanır.

 *Django template* , statik `HTML` öğelerini ve `HTML` sayfalarının dinamik içeriğinin nasıl üretileceğini tanımlayan özel Python kodunu içerir.

![1765196070281](image/1_DjangoModel-View-Template(MVT)Pattern/1765196070281.png)

---

## 📝 Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* Django modeli, geleneksel *MVC* deseninden farklıdır.
* *Django Model-View-Template (MVT)* deseninde:
  * Django framework *Controller* rolünü üstlenir.
  * *Django View* , hangi verinin sunulacağını tanımlar.
  * *Django Template* , verinin tam olarak nasıl sunulacağını tanımlar.

![1765196093383](image/1_DjangoModel-View-Template(MVT)Pattern/1765196093383.png)
