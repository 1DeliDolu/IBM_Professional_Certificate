## 🧩 JavaScript APIs

JavaScript API’lerine hoş geldiniz. Bu videoyu izledikten sonra,  *node* ’larla nasıl çalışılacağını açıklayabilecek, bir elemanın içeriğinin nasıl değiştirileceğini tanımlayabilecek, bir nesnenin  *inline style* ’ının ve özniteliklerinin ( *attributes* ) nasıl değiştirileceğini açıklayabilecek ve **Window** nesnesi metodları ile olaylarının ( *events* ) nasıl kullanılacağını tanımlayabileceksiniz. **DOM Level 1 core** ve **Level 1 HTML** spesifikasyonları tek bir ünite için fazla ayrıntı içerir. Bunun yerine, ünitenin geri kalanı HTML sayfalarıyla çalışırken yaygın olarak kullanılan script fonksiyonları ve özelliklerine odaklanır. Web sayfalarında HTML DOM elemanlarına erişirken kullanılan bazı yaygın API’ler slaytta görülmektedir; DOM elemanları bir sonraki bölümde incelenir.

---

## 🧷 Node Referansı Alma

Bir dokümandaki bir eleman için, verilen bir  **id** ’ye göre bir *node reference* almak için **document.getElementById** fonksiyonunu kullanın ve **id** değerini argüman olarak geçin. Bu, web sayfasında eşleşen benzersiz bir **id** bulunursa, belirli bir HTML veya XML elemanını döndürür.

---

## 🏷️ getElementsByTagName ile NodeList

**getElementsByTagName** fonksiyonu, belirli bir etiket adına ( *tag name* ) sahip elemanların bir  **NodeList** ’ini getirir.  **NodeList** , dokümanınızdaki elemanlardan oluşan bir dizi içerir. İlgilendiğiniz elemanın adını verirsiniz ve dokümanda bu adla bulunan tüm elemanların bir dizisi döndürülür. HTML elemanları için **tagName** parametresi, HTML etiketinin literal adıdır. Eğer **getElementsByTagName** fonksiyonunu parametre olarak **“p”** ile çalıştırırsanız, dokümandaki tüm paragraf elemanlarının bir  **NodeList** ’i döndürülür. Bu örnek, **getElementsByTagName** fonksiyonunu kullanarak ve parametre argümanı olarak **“img”** geçirerek bir web sayfasındaki tüm görsel elemanlarını nasıl alabileceğinizi gösterir. Sonuç, **imgSet** değişkenine atanan bir  **NodeList** ’tir.

Kodun bir sonraki kısmında, **nodeList** üzerinde döngü kurar ve sonuçları bir DOM çıktı akışına birleştirirsiniz. **src** özniteliği, **img** etiketi için yaygın bir özelliktir. **src** özniteliği, görsel kaynağının konumunu belirtir. **document.write()** fonksiyonu, script tarafından oluşturulan HTML’i dokümana ekler.

---

## 🏗️ Eleman Oluşturma ve Dokümana Ekleme

Mevcut dokümanda bir eleman oluşturmak için DOM API fonksiyonu **document.createElement(TagName)** kullanılabilir. Elemanı oluşturduktan sonra, elemanı dokümanda uygun konuma yerleştirmek için çeşitli fonksiyonlar kullanabilirsiniz. Bu fonksiyonlara örnek olarak, yeni oluşturulan elemanı dokümana eklemek için kullanılabilen  **insertBefore** , **appendChild** veya **replaceChild** fonksiyonları verilebilir.

Bu örnek, bir dokümana *node* ekleme kaynak kodunu gösterir. **“Hello world!”** dizesini içeren bir *text node* ile birlikte yeni bir paragraf elemanı oluşturulmaktadır. Ardından  *text node* , paragraf elemanının bir çocuğu ( *child* ) olarak eklenir. Son olarak, metin içeren paragrafın tamamı, HTML sayfasının **body** düğümünün sonunda bir *child node* olarak eklenir.

---

## 📝 innerHTML ile İçerik Değiştirme

**element.innerHTML** fonksiyonu, bir HTML elemanının içeriğini getirir veya ayarlar. **innerHTML** özelliği, tüm alt elemanları ( *child elements* ) bir metin dizesi olarak döndürür. **element.innerHTML** ile, HTML etiketleri içerebilen bir metin dizesine ayarlayarak bir HTML elemanının içeriğini değiştirebilirsiniz.

Bir elemanın **innerHTML** değerini bir dizeye ayarlamak, mevcut tüm alt elemanları kaldırır. Ardından tarayıcı bu dizeyi ayrıştırır ve HTML elemanının içeriğini ayarlar.

---

## 🎨 Inline CSS Style Değiştirme

Belirli bir eleman için *inline* CSS stilini almak veya ayarlamak için **element.style** metodunu kullanabilirsiniz. Eğer bir elemanın stilini ayarlamak için **element.style** kullanırsanız, bir CSS stil sayfasından gelen ayarı, tek bir spesifik stil ile geçersiz kılar. JavaScript’te stili ayarlama yolu şu formattadır:

```javascript
element.style.propertyName = value
```

Örneğin, **div style="color:blue"** olan bir elemanınız olduğunu varsayalım. Burada etiketi, blok elemanlarını renk stiliyle biçimlendirmek için gruplamak amacıyla kullanılır.

Bu **div** etiketinin stilini şu JavaScript ifadesiyle değiştirebilirsiniz:

```javascript
div.style.color = 'red';
```

Buna karşılık, **element.setAttribute('style', …)** daha önce ayarlanmış tüm *inline* CSS stillerini siler.

---

## 🧷 Attribute Değiştirme

Parametreleri **(attrName, attrValue)** olan **element.setAttribute** fonksiyonu, bir elemanın özniteliğini ( *attribute* ) dinamik olarak değiştirir. Örnekte, **id** değeri **theImage** olan bir elemanın **src** özniteliği farklı bir hedef görsele ayarlanır.

**element.removeAttribute(attrName)** fonksiyonu, bir elemandan bir özniteliği kaldırır.

**element.getAttribute(attrName)** fonksiyonu, varsa, elemandaki belirtilen özniteliğin değerini getirir.

---

## 🪟 Window Object Metodları ve Olayları

İşte bazı **window object** fonksiyonları ve olayları. Yeni bir tarayıcı penceresi açmak için **window.open()** fonksiyonunu kullanın. Bu metod, yeni **window object** için bir referans döndürür. Bu referansı daha sonra, **reference_name** ifadesini takiben **close()** fonksiyonunu kullanarak pencereyi kapatmak için kullanabilirsiniz.

**window.open** fonksiyonunun parametreleri şunlardır:

* **URL** – Yeni pencerede görüntülenecek web sayfasının konumunu belirten bir dize. Eğer mevcut URL bağlamında yeni pencereye script ile oluşturulmuş içerik yazacaksanız boş bir dize geçebilirsiniz.
* **Name** – Pencerenin adını belirten bir dize.
* **Features** – Pencerenin konumu ve boyutları gibi özelliklerini belirten isteğe bağlı bir dize. *Features* dizesi, virgülle ayrılmış ad-değer çiftlerinden oluşan bir listedir.
* **Replace** – İsteğe bağlı bir boolean değer. **true** ise, yeni konum tarayıcı geçmişinde mevcut sayfanın yerini alır.

**window.onload** fonksiyonu, sayfa yüklendikten sonra bir fonksiyonu başlatmak için kullanılabilir.

**window.dump("message")** fonksiyonu, web tarayıcısının konsoluna bir dize yazar. **dump()** fonksiyonu, tanılama ( *diagnostic* ) bilgilerini göstermek için **alert()** metoduna göre daha az rahatsız edici bir yoldur.

Son olarak, **window.scrollTo(x-value, y-value)** web tarayıcısını bir sayfadaki belirli koordinatlara kaydırır.

**onload** olay işleyicisi ( *event handler* ), doküman web sayfasını yükledikten sonra mevcut pencerede çalışır. Örnekte, **onload** olayı anonim bir fonksiyonun çalışmasına neden olur. Bu fonksiyon da sırayla **addPara()** fonksiyonunu çalıştırır.

---

## ✅ Özet

Bu videoda, bir  *node* ’a referansı şu şekilde alabileceğinizi öğrendiniz:

* **document.getElementById(id)** – **id** özniteliğine göre tek bir belirli elemanı döndürür.
* **document.getElementsByTagName(tagName)** – belirtilen etikete sahip elemanların bir listesini getirir.

Bir elemanı şu şekilde oluşturabilirsiniz:

* **document.createElement(TagName)**

Ve şu şekilde yerleştirebilirsiniz:

* **insertBefore** , **appendChild** veya **replaceChild**

Elemanları şu yöntemlerle değiştirebilirsiniz:

* **element.innerHTML** ile bir HTML elemanının içeriğini almak veya ayarlamak
* **element.style** ile *inline* CSS stilini almak veya ayarlamak
* **element.setAttribute** ile bir elemanın özniteliklerini değiştirmek

Bir  **window object** ’i şu fonksiyonlar dahil olmak üzere yönetebilirsiniz:

* **window.open** – web tarayıcısı için yeni bir **window object** referansı döndürür
* **window.dump("message")** – web tarayıcısı konsoluna bir dize yazar

Bu kapsamlı bir liste değildir – HTML elemanları ve  *node* ’larla çalışmanızı sağlayan çok daha fazla fonksiyon vardır.
