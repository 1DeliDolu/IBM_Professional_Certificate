# 💠 Bootstrap

## 📘 Bootstrap’e Hoş Geldiniz

Bootstrap’e hoş geldiniz!

Bootstrap, web uygulaması geliştirmeyi kolaylaştırmak için tasarlanmış, ücretsiz bir web ön yüz ( *front-end* ) çatısıdır; Django şablon geliştirmesini basitleştirmek için iyi tasarlanmış ve yaygın olarak kullanılan birçok HTML ve CSS şablonu sağlar.

Bootstrap’in yardımıyla, geliştiriciler kolayca stillendirilmiş ve etkileşimli web sayfaları oluşturabilir. Django şablonlarımıza Bootstrap çatısını nasıl hızlı bir şekilde ekleyebileceğimize bakalım.

---

## ⚙️ Bootstrap’i Django Şablonlarına Entegre Etmek

Bootstrap’i entegre etmek basittir.

Bootstrap’i indirmeden Bootstrap CSS stil sınıflarını kullanmak istiyorsanız, içerik dağıtım ağları ( *content delivery networks* ) olan MaxCDN gibi servislerde barındırılan en son Bootstrap sürümüne ait bir bağlantıyı HTML şablonunuzun *head* öğesine ekleyebilirsiniz.

Hepsi bu; Bootstrap eklemenin en basit yolu budur.

---

## 🧱 Sayfa Düzeni ve Kurs İndeksi Tasarımı

Artık Bootstrap’in sağladığı CSS sınıflarını kullanmaya başlayabilirsiniz. Web sayfası geliştirme genellikle düzen ( *layout* ) tasarımıyla başlar.

Bir çevrimiçi kurs uygulamasındaki dersleri temsil etmek için basit bir kurs indeks düzeni tasarlayalım.

Birçok başka web sayfasında olduğu gibi, kurs indeks sayfamızın en üstünde, site içinde gezinmek için bağlantılar ve öğeler içeren bir gezinme çubuğu ( *navigation bar* ) bulunur. Gezinti çubuğumuzda ayrıca, kullanıcıların oturum açma veya kaydolma gibi kimlik doğrulamayla ilgili verileri gönderebilecekleri bir form da vardır.

Sonraki kısım, bir liste, tablo veya resim galerisi gibi ana öğeleri içeren web sayfasının ana içeriğidir. Burada, içerik öğelerini sarmak için bir *container* kullanacağız.

Her kursu bir *card* olarak sunmayı planlıyoruz;  *card* , içeriğinin etrafında kenarlık ve iç boşluk ( *padding* ) bulunan kutudur. Bu kartların bir başlığı ( *header* ), altlığı ( *footer* ), içeriği, görselleri, renkleri vb. olabilir.

Birden fazla kurs kartını yönetmek için onları bir *card deck* içine saracağız; bu, kartlardan oluşan ve kartların eşit yükseklik ve genişliğe sahip olduğu bir ızgara oluşturur.

---

## 🧭 Navigasyon Çubuğu (Navbar) Oluşturma

Bootstrap’te, bir gezinme çubuğunu (`navbar`) arka plan rengi gibi ek sınıflarla ve ekran boyutuna uyum sağlamak için gezinme çubuğunun nasıl genişleyip daralacağını belirleyen sınıflarla birlikte `navbar` sınıfını kullanarak oluştururuz.

Gezinti çubuğuna bağlantı veya buton gibi öğeler eklemek için, `navbar-nav` sınıfına sahip bir `ul` elementi kullanır, ardından `nav-item` sınıfına sahip `li` öğeleri ekleriz. Burada, `nav-link` sınıfına sahip basit bir *Home* bağlantısını gezinme çubuğuna ekledik.

Sonucu önizleyelim. Açık arka plan temasına sahip bir gezinme çubuğunun oluşturulduğunu görürsünüz. Şu anda yalnızca bir bağlantı öğesi vardır.

---

## 🔐 Navigasyon Çubuğuna Oturum Açma Formu Ekleme

Sonraki adımda, kimlik doğrulamayla ilgili verileri göndermek için gezinme çubuğuna bir form ekleriz. Tüm öğelerin aynı satırda ve sola hizalı olacağı satır içi ( *inline* ) bir form oluşturmamız gerekir.

Bu satır içi formun içinde, kullanıcı adı ve parola almak için iki adet girdi ( *input* ) öğesi ekleyebiliriz. Burada metinsel öğeleri stillendirmek için standart bir Django sınıfı olan `form-control` sınıfını kullanıyoruz.

Ardından, `btn` ve `btn-primary` sınıflarıyla stillendirilen bir gönderme butonu ekleriz; bu sınıflar standart bir Bootstrap mavi butonu oluşturur.

Son olarak, `btn` ve `btn-link` sınıflarıyla stillendirilmiş ve kayıt sayfasına giden bir *Sign up* bağlantısı ekleriz.

Sonuçta, gezinme çubuğuna eklenmiş bir oturum açma formu görebilirsiniz. Böylece, kurs indeks sayfamızın üstbilgi ( *header* ) bölümünü tamamlamış olduk.

---

## 🧩 İçerik Alanı: Container, Card ve Card Deck

Şimdi, sayfanın ana içeriğini oluşturmaya başlayacağız. Sayfayı, `container` sınıfıyla stillendirilmiş bir `div` elemanının içine dahil etmek istiyoruz.

Bootstrap’te iki tür *container* vardır. İlk `container` sınıfı sabit genişliğe sahiptir; diğeri ise üst öğenin tüm genişliğine yayılan `container-fluid` sınıfıdır.

`container` sınıfının içinde, `card-deck` sınıfıyla stillendirilmiş bir `div` oluştururuz. `card-deck` sınıfı, kurs kartlarımızı düzenlemek için kartlardan oluşan bir ızgara oluşturur.

Daha sonra bir kurs kartını temsil etmek için bir `card` `div`i oluştururuz. Her kurs kartında, kurs görselini göstermek için bir resim ( *image* ) öğesi, kurs adını göstermek için `card-title` içeren bir `card-body` ve kurs açıklamasını göstermek için `card-text` bulunur.

Sonuç, her kursun bir kart olarak sunulduğu, hoş bir kurs kart destesi ( *course card deck* ) olur.

---

## 📊 Tablo Şablonu ile Öğrenci Listesi

Yaygın olarak kullanılan bir diğer içerik şablonu ise, öğrenci listesi gibi tablosal verileri gösteren tablodur ( *table* ).

Bir Bootstrap tablosu oluşturmak için, `table` sınıfıyla stillendirilmiş bir `table` elementi oluştururuz. Ardından,  *first name* , *last name* ve *email* gibi tablo başlıklarını tanımlamak için bir `thead` elemanı ile tablo başlığını ( *table head* ) oluştururuz.

Sonra da, her tablo satırının (`tr`) bir kullanıcıyı, her tablo sütununun (`td`) ise  *first name* , *last name* veya *email* gibi bir kullanıcı özelliğini temsil ettiği bir tablo gövdesi ( *table body* ) ekleyerek, bir derse ait kullanıcı nesnelerini gösteririz.

Sonuçta, bir derse kayıtlı öğrencilerin listesini gösteren bir öğrenci tablosu elde ederiz.

---

## ✅ Neler Öğrendik?

Bu videoda, Bootstrap’in ne olduğunu ve Bootstrap’i Django şablonunuza nasıl entegre edeceğinizi öğrendiniz.

Ayrıca, oturum açma formuna sahip bir gezinme çubuğu,  *container* ,  *card* , *card deck* ve tablo ( *table* ) gibi bazı yaygın Bootstrap şablonlarını da öğrendiniz.
