# 🧰 Bir IDE ile Çalışmak

## 👋 Cloud IDE’ye Giriş

Herkese merhaba ve IBM Skills Network ekibi tarafından sağlanan Cloud IDE (veya *Integrated Development Environment* – Entegre Geliştirme Ortamı) demosuna hoş geldiniz.

Cloud IDE, öğrenme amaçlı bir programlama ortamıdır. Kendi kişisel cihazınızda herhangi bir yazılım veya araç yüklemenize ya da yapılandırmanıza gerek kalmadan, doğrudan bir tarayıcı içinde kod yazmak, çalıştırmak, hata ayıklamak ve komutları yürütmek için kullanabilirsiniz.

Bu demoda şunları öğreneceksiniz:

* Cloud IDE’nin farklı bileşenlerinde gezinebilmek
* Gerekli Python paketlerini veya kütüphanelerini kurmak
* Kod yazmak
* Kod çalıştırmak

![1765099460261](image/7_WorkingwithanIDE/1765099460261.png)

---

## 🪟 Cloud IDE Panelleri

Cloud IDE’yi açtığınızda iki ana panel görüntülenir.

Sol panel, **instructional pane** (yönerge paneli) olarak adlandırılır.

Projenizi tamamlamak için izlemeniz gereken talimatları bu panelde görürsünüz.

Sağ panel ise bir **programlama arayüzü** görüntüler; burada kodunuzu yazabilir ve çalıştırabilirsiniz.

Lütfen dikkat: Sağ panel, kod yönetimi için yaygın olarak kullanılan popüler bir IDE olan **VS Code** arayüzüne benzer.

---

## 📑 Yönerge ve Kod Panellerini Özelleştirme

Yönerge panelinin ve kod panelinin boyutlarını yeniden ayarlayabilirsiniz.

Örneğin, yönerge panelinin boyutunu, panelin kenarını sola doğru sürükleyerek küçültebilirsiniz.

Aynı şekilde, paneli sağa doğru sürükleyerek boyutunu büyütebilirsiniz.

Tercihinize göre yazı tipini ve yazı tipi boyutunu değiştirmeniz de mümkündür.

Eğer yönerge panelinde birden fazla sayfa varsa, **Next** ve **Previous** düğmelerini görürsünüz.

Bu düğmeler, sayfalar arasında gezinmenizi sağlar.

Ayrıca bir yönerge sayfasını önizleyebilirsiniz.

Yönerge panelinin sol üst köşesinde bir **Table of contents** düğmesi bulunduğuna dikkat edin.

Bu düğmeyi, talimatların farklı bölümleri arasında gezinmek için kullanabilirsiniz.

---

## 🤖 Yapay Zekâ Destekli Chatbot: Tai

Şimdi Cloud IDE’de bulunan yapay zekâ destekli bir chatbota bakalım.

IBM Skills Network ekibi, laboratuvar ortamını ve kodlama ödevlerini kullanmanız konusunda size yardım sağlayan, **Tai** adlı yapay zekâ destekli bir Teaching Assistant (öğretim asistanı) chatbot sunmaktadır.

Tai’nin simgesi, yönerge panelinin sol tarafında bulunur.

Chatbot’a erişmek için simgeye tıklamanız yeterlidir.

Örneğin şu şekilde bir soru soralım:

“ *Please provide me with simple Python code.* ”

Gördüğünüz gibi, kod ekranda görüntülenir.

Bu kodu kopyalayabilir veya çalıştırabilirsiniz.

---

## 🧮 Programlama Arayüzü ve Temel Sekmeler

Şimdi IDE’nin programlama arayüzüne bakalım.

Programlama arayüzünde birkaç bileşen bulunur; ancak en sık kullanacağınız iki sekme şunlardır:

* **Editor** sekmesi: Kodu yazdığınız yer
* **Terminal** sekmesi: Kodu çalıştırdığınız yer

Programlama panelinde ayrıca bir **Skills Network Toolbox** bulunur.

Bu araç kutusu, çeşitli veritabanı yönetim ortamları, büyük veri araçları, bulut araçları, gömülü yapay zekâ kütüphaneleri ile çalışmanızı ve geliştirdiğiniz uygulamaları başlatmanızı sağlar.

---

## 📦 Terminal Üzerinden Python Paketleri Kurma

Kodu yazmaya başlamadan önce, bu bulut tabanlı ortamda gerekli Python kütüphanelerini veya paketlerini kurmanız gerekir.

Bu işlemi **Terminal** sekmesinde gerçekleştirmeniz gerekir.

Yeni bir terminal açmak için:

1. Menüden  **Terminal** ’e tıklayın.
2. Ardından  **New Terminal** ’ı seçin.

Demo amacıyla, yönerge panelinden bir komut bloğunu kopyalayalım ve terminale yapıştıralım.

Sonra komutu çalıştırmak için **Enter** tuşuna basın.

`numpy` kütüphanesinin başarıyla yüklendiğine dikkat edin.

Artık bu kütüphaneyi kodunuzda içe aktarabilirsiniz.

---

## 📝 Yeni Bir Python Programı Oluşturma

Şimdi basit bir Python programı oluşturalım.

Programlama panelinde  **File** ’a tıklayın.

Ardından **New File** seçeneğini seçin.

Yeni dosya, **Editor** sekmesinde açılır.

Koda başlamadan önce dosyayı kaydetmek, en iyi uygulamalardan ( *best practice* ) biridir.

Bir Python kodu yazdığımız için dosyayı `.py` uzantısıyla kaydedin.

**File** menüsünden  **Save** ’e tıklayın (veya `Ctrl+S` kısayolunu kullanın).

Sistem sizden bir dosya adı girmenizi istediğinde adı yazın.

Bu örnekte dosyayı `Hello.py` olarak kaydedelim.

---

## ✍️ Kodu Eklemek

Sıradaki adım, kodu eklemektir.

Kodu **Editor** sekmesinde elle yazabilirsiniz veya yönerge panelinden (varsa) kodu kopyalayıp dosyanıza yapıştırabilirsiniz.

Bu demo için, kodu yönerge panelinden kopyalayıp dosyaya yapıştıralım.

Dosyayı kaydetmeyi unutmayın!

Artık kodu çalıştırma zamanı.

---

## ▶️ Kodu Çalıştırma

Şimdi **Terminal** sekmesine geri dönelim.

Program dosyasının kayıtlı olduğu klasörde bulunduğunuzdan emin olun.

Dosyayı çalıştırmak için şu şekilde yazabilirsiniz:

```bash
python3 Hello.py
```

Yani, `python3` komutundan sonra dosya adını yazarsınız.

Bu örnek için komut: `python3 Hello.py`’dir.

Çıktının herhangi bir hata olmadan görüntülendiğine dikkat edin.

---

## 📚 Özet

Bu noktada Cloud IDE demosunun sonuna geldik.

Özetlemek gerekirse:

* **Cloud IDE** , VS Code’a benzer bir programlama ortamıdır

  [öğrenme ve uygulamalı beceriler geliştirme amacıyla IBM Skills Network tarafından sağlanmaktadır].

* Cloud IDE’de iki panel vardır: **instructional** (yönerge) ve **programming** (programlama) paneli.
* Yönerge panelinde, talimat sayfaları arasında gezinmek için **Table of contents** düğmesini kullanabilirsiniz.
* Programlama paneli, kod yazmak için **Editor** sekmesini, kod çalıştırmak için **Terminal** sekmesini sunar.
* Gerekli kütüphaneleri **Terminal** üzerinden kurmanız gerekir.
* Laboratuvarlar sırasında, dilediğiniz zaman yönerge panelindeki kod bloklarını kopyalayarak **Editor** veya **Terminal** sekmelerine yapıştırabilirsiniz.
