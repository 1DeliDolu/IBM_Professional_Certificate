# 📝 Metin Dosyaları Oluşturma ve Düzenleme

Metin Dosyaları Oluşturma ve Düzenleme’ye hoş geldiniz.

Bu videoyu izledikten sonra şunları yapabileceksiniz:

* Linux için popüler metin düzenleyicilerini listelemek
* Popüler bir GUI tabanlı metin düzenleyiciyi tanımlamak
* Bir dosyayla çalışmak için komut satırı düzenleyicilerini kullanmak

Linux ortamınızda kod yazmak için metin düzenleyicileri kullanırsınız.

Aralarından seçim yapabileceğiniz birçok düzenleyici vardır ve bunlar iki ana kategoriye ayrılabilir:

* **Komut satırı metin düzenleyicileri**
* **GUI (grafik arayüzlü) metin düzenleyiciler**

Komut satırı metin düzenleyicilerine örnekler şunlardır:

* **GNU nano** , küçük ve kullanımı kolay, mod’suz bir metin düzenleyicisidir.
* **vi** , aslen Unix için oluşturulmuş, geleneksel bir komut satırı düzenleyicisidir.
* **vim** , vi tabanlı, güçlü, mod’lu bir komut satırı düzenleyicisidir.

Popüler GUI tabanlı bir düzenleyici  **gedit** ’tir; GNOME ortamının varsayılan düzenleyicisidir.

Ve **emacs** (e’-max), hâlâ geliştirilmeye devam eden en eski özgür, açık kaynak projelerden biri olan bir başka metin düzenleyicisidir.

Emacs’i GUI modunda veya bir komut satırı içinde kullanabilirsiniz.

 **Gedit** , çoğu Linux dağıtımında önceden kurulu gelen, popüler ve modern bir metin düzenleyicisidir.


---

## 🖱️ gedit’e Genel Bakış

Gedit, genel amaçlı bir metin düzenleyici olarak tasarlanmıştır ve GNOME projesinin felsefesiyle uyumlu olarak, basitlik ve kullanım kolaylığını vurgular; sade ve basit bir GUI’ye sahiptir.

Gedit, metin düzenleme deneyiminizi geliştirmek için pek çok özellik sunar, bunlar arasında:

* Entegre bir **dosya tarayıcı**
* **Geri al (undo)** ve **yeniden yap (redo)** işlevleri
* Arama dizesinde **düzenli ifadeleri (regular expressions)** destekleyen arama ve değiştirme işlevleri
* **gedit-plugins** paketinden gelen eklentilerle genişletilebilirlik (extensibility)

Metin düzenleyici, kodunuzun farklı yönlerini yorumlamanıza ve odaklanmanıza yardımcı olmak için **sözdizimi renklendirmesi (syntax color coding)** kullanır.

---

## 📟 GNU nano’ya Genel Bakış

 **GNU nano** , şu özellikleri sağlayan bir komut satırı metin düzenleyicisidir:

* **Geri al (undo)** ve **yeniden yap (redo)** özellikleri
* Arama dizesinde **düzenli ifadeleri** destekleyen arama ve değiştirme
* **Sözdizimi vurgulama (syntax highlighting)**
* Kodun **otomatik girintilenmesi**
* **Satır numaralandırma**
* **Satır satır kaydırma (line-by-line scrolling)**
* Aynı anda birçok dosyayla çalışabilmeniz için **birden fazla arabellek (multiple buffers)**

Bir metin dosyasını nano’da açmak için, açmak istediğiniz dosyanın adını takip eden `nano` komutunu yazarsınız.

Bu işlem, dosyayı düzenleyebileceğiniz yeni bir metin düzenleyici penceresi açar.

Nano uygulamasının görünümü şu şekildedir:

Ana alan, açık dosyanın metnini görüntüler; bu örnekte, nano’nun Wikipedia sayfasındaki kaynak metindir.


---

## ⌨️ nano’da Gezinme ve Temel Düzenleme

İmleç şu anda dosyanın başında bulunuyor, ancak metin içinde  **ok tuşları** , **Page Up** ve **Page Down** tuşları ya da **Home** ve **End** tuşlarını kullanarak gezinebilirsiniz.

Yazdığınız herhangi bir metin, imlecin bulunduğu konuma girilir.

Ayrıca **Delete** ve **Backspace** tuşlarını kullanarak metni silebilirsiniz.

**Enter** tuşuna basmak yeni bir satır başlatır.

Nano penceresinin altında, düzenleyicide kullanabileceğiniz komutların bir listesi yer alır.

Bu komutlara erişmek için aynı anda `control` (Ctrl) tuşuna ve komut için belirtilen harfe basarsınız.

Örneğin, **Yardım (Get Help)** almak için `control` ve `G` tuşlarına (`Ctrl` + `G`) basarsınız.


---

## 🔍 nano’da Arama (Where Is) Özelliği

Şimdi birkaç düzenleme seçeneğinin nasıl kullanılacağına bakalım.

Bir metin dizesini aramak için `control W` tuşlarına (`Ctrl` + `W`) basarak **Where Is** seçeneğini kullanabilirsiniz.

Bu, uygulama penceresinin altında yeni bir panel açar.

Bu yeni panelin daha yakından görünümü şöyledir:

Köşeli parantezler içinde, en son aranan dizeyi görebilirsiniz; burada bu dize  **1999** ’dur.

Bulmak istediğiniz dizeyi yazın; örneğin **‘https’** ve **Enter** tuşuna basın.

İmleç, arama dizesinin, imlecin mevcut konumundan sonra bulunan ilk örneğine taşınır.

Nano, bu kurstaki laboratuvarlardan (lab) birinde keşfedeceğiniz daha birçok düzenleme özelliğini destekler.

---

## 🧠 Vim’e Kısa Bir Giriş

 **Vim** , geleneksel ve çok güçlü bir komut satırı düzenleyicisidir.

Nasıl çalıştığına alışmak biraz zaman alır, ancak biraz pratikle, parmaklarınız tüm metin düzenleme görevlerinizi hızla yerine getirecek **kas hafızasını (muscle memory)** geliştirir.

Komut istemine `vim` yazarak vim uygulamasını başlatırsınız.

Yeni bir dosya oluşturmak veya var olan bir dosyayı düzenlemek için bir dosya adı da belirtebilirsiniz.

Vim’in iki temel modu vardır:

* **Insert mode (Ekleme modu)** : Metin girdiğiniz mod
* **Command mode (Komut modu)** : Diğer tüm işlemleri yaptığınız mod

Bir vim oturumu başlattıktan sonra,  **Insert mode** ’a geçmek için `i` tuşuna basın.

Örneğin **“some text”** gibi biraz metin yazın ve sonra **Escape** tuşuna basarak Insert mode’dan çıkıp Command mode’a geçin.

Metin, imlecin geçerli konumunda arabelleğe (buffer) yazılmış olur.

---

## 💾 Vim’de Kaydetme ve Çıkma Komutları

Artık tekrar  **Command mode** ’dasınız ve dosyanızı bir dosya adıyla kaydetmek için **‘colon save’** komutunu bir dosya adıyla birlikte kullanabilirsiniz; örneğin  **‘example dot txt’** .

Arabellek dosyaya yazılır ve şu bilgileri gösteren bir mesaj görüntülenir:

* Dosya adı
* Bunun yeni bir dosya olduğu
* Bir satır ve 10 sütun içerdiği
* Ve dosyanın başarıyla yazıldığı

Artık dosyanız zaten mevcut olduğuna göre, dosyadaki değişiklikleri yazmak için daha yaygın olan **‘colon w’** komutunu kullanabilirsiniz.

Vim oturumundan çıkmak için **‘colon q’** komutunu girin.

Ve son yazma işleminden beri yapılan değişiklikleri kaydetmeden çıkmak için,  **‘bang’** , yani ünlem işaretini ekleyerek **‘colon q bang’** komutunu kullanın.

Bu, vim’e çok kısa bir girişti.

Metin arabelleğinde gezinmek ve arama, kopyalama, yapıştırma ve metni başka yerlere taşıma gibi işlemleri gerçekleştirmek için kullanabileceğiniz birçok komut vardır.

Bu komutlardan bazılarını yaklaşan bir laboratuvarda (lab) uygulama fırsatı bulacaksınız.

---

## 📚 Özet: Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* Linux kodunuzla çalışmak için çeşitli **komut satırı** veya **GUI tabanlı metin düzenleyiciler** kullanabilirsiniz.
* **gedit** , çalışmanızı basitleştirmek için birçok özellik sunan GUI tabanlı bir düzenleyicidir.
* **GNU nano** , benzer işlevleri komut satırı formatında sağlayan bir komut satırı düzenleyicisidir.
* Ve  **vim** , veriyi girmek için  **Insert mode** ’u, dosyayla çalışmak için ise  **Command mode** ’u kullanan başka bir komut satırı düzenleyicisidir.

Bir metin düzenleyiciyi kullanarak mevcut dosyalarla nasıl çalışacağınızı gördünüz.

Bu, Linux komutlarını kullanarak dosyalar oluşturmayı ve bu dosyalara metin eklemeyi (append) öğrenirken size yardımcı olacaktır.
