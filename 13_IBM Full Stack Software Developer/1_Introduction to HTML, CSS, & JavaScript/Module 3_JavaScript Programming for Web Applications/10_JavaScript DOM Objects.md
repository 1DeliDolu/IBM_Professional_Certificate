## 🎵 JavaScript DOM Objects

(Music) JavaScript DOM Objects konusuna hoş geldiniz. Bu videoyu izledikten sonra, ilgili *node* türlerini listeleyebilecek, doküman elemanlarına nasıl erişileceğini gösterebilecek ve nesne adlandırmayı açıklayabileceksiniz. W3C DOM Level 2, 12 farklı *node* türü tanımlar; bunların yedisi HTML dokümanlarında doğrudan uygulanabilir. HTML için uygulanabilir olmayan *node* türleri tablodan çıkarılmıştır. Bu tablo, bir DOM ağacını görüntülediğinizde sayısal *node* türlerinin anlamını kavrayabilmeniz için önemlidir. Her *node* türü, bir tamsayı değer ile de temsil edilen adlandırılmış bir sabittir. Örneğin, bir **ELEMENT_NODE** türü tamsayı olarak  **1** , bir **ATTRIBUTE_NODE** türü tamsayı olarak  **2** , bir **TEXT_NODE** türü tamsayı olarak **3** ve bir **COMMENT_NODE** tamsayı olarak **8** ile temsil edilir.

---

## 🧷 Node Name ve Node Value

DOM ağacında **ELEMENT_NODE** türü için  *node name* , elemanın veya etiketin adıdır. Örneğin bir **DIV** elemanına bakıyorsanız, *node name*  **DIV** ’dir. Eğer **DIV** elemanının **id=div123** gibi bir özniteliği ( *attribute* ) varsa, öznitelik adı **“id”** ve öznitelik değeri **“div123”** olur; bu bir ad-değer ( *name-value* ) çiftidir. Başka bir örnek: Bir paragraf elemanını bazı metin takip ediyorsa, bu metin dizesinin  *node name* ’i **hash-sign-text** olur ve *node value* metin dizesinin kendisidir. Tablo, bazı DOM Level 2 *node object* özelliklerini ve karşılık gelen veri türlerini listeler. Bu özellikleri, Chrome DevTools gibi bir tarayıcının geliştirici araçlarında bir HTML sayfasının DOM ağacını görüntülerken görürsünüz. DOM API ile bir HTML sayfasındaki elemanlara nasıl erişirsiniz?

---

## 🗃️ Browser Arrays ile Elemanlara Erişim

Doküman yüklendiğinde, tarayıcı  **forms** ,  **images** ,  **anchors** ,  **links** , **applets** ve **embeds** için diziler ( *arrays* ) oluşturur. Ardından her türdeki tüm nesneleri bu dizilerin içine yerleştirir. Diziler, kaynak dokümanda göründükleri sıraya göre indekslenir. Her dizinin ilk indeksi  **0** ’dan başlar. **forms[ ]** gibi her bir dizi türü, bir eleman dizisi içerir; her bir indeks elemanı  **element[ ]** , o formda bulunan alanlar veya düğmelerdir. Şekilde **field1** adlı elemana, göreli konumuyla şu şekilde referans verebilirsiniz:

```javascript
document.forms[0].elements[0]
```

Aynı alana, adlandırılmış elemanlarla da referans verebilirsiniz; örneğin:

```javascript
document.forms["form1"].elements["field1"]
```

Hatta kısaltılmış biçimiyle:

```javascript
document.form1.field1
```

Şekilde kesikli çizgi ile gösterildiği üzere, bir pencere ( *window* ) içinde yalnızca bir doküman bulunabildiği için **window** önekini yazmayabilirsiniz. Ancak, referans verilen nesnede **document** önekini çıkaramazsınız.

---

## 🆔 id Attribute ve Adlandırma Kuralları

**id** özniteliği, bir dokümandaki bir elemanı tanımlar. Bir elemanın **id** özniteliği, script’lerin **id** özniteliğinin değerine uyan bir isimle elemana referans vermesi için kullanılır. **id** özniteliği ile bir HTML elemanına script ile erişilebilir bir referans adı atamak için aşağıdaki kuralları kullanın:

* **id** , doküman içinde benzersiz ( *unique* ) bir ad olmalıdır.
* **id** özniteliğine atanırken ad tırnak işaretleri içinde olmalıdır.
* Ad, sayısal bir rakamla başlamamalıdır.

**id** değeriyle eşleşen bir *node object* döndürmek için kullanılan fonksiyon, parametre argümanı olarak **id** adını alan **document.getElementById** fonksiyonudur. Her ikisi de kullanıldığında (daha önce görüldüğü gibi) **id** ve **name** öznitelikleri için aynı değerin kullanılması önerilir.

---

## ✅ Özet

Bu videoda, ilgili *node* türlerini nasıl listeleyeceğinizi, nokta gösterimi ( *dot notation* ) kullanarak iç içe nesnelere nasıl erişeceğinizi ve script’ten erişimi kolaylaştırmak için nesneleri nasıl adlandıracağınızı öğrendiniz.
