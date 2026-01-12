## 🎵 Client-Side JavaScript: with DOM

(Music) DOM ile Client-side JavaScript konusuna hoş geldiniz. Bu videoyu izledikten sonra, *document object model* (DOM) hiyerarşisini tanımlayabilecek, **window** ve **document** nesnelerini açıklayabilecek, HTML dokümanlarıyla çalışmak için JavaScript uygulamalarında yaygın olarak kullanılan DOM nesnelerini belirleyebileceksiniz.  *Document object model* , HTML veya XHTML ile JavaScript arasındaki programlama arayüzüdür.  *Document Object Model (DOM)* , uygulamaların ve script’lerin dokümanların içeriğine, yapısına ve stiline dinamik olarak erişip güncellemesi için tarayıcı tabanlı bir arayüzdür. JavaScript, web tarayıcısında web sayfası elemanlarına erişmek ve onları değiştirmek için DOM’u kullanır. *World Wide Web Consortium* (W3C), *Document Object Model* spesifikasyonlarının dört seviyesini yayınladı. Her bir sonraki seviye, yapılandırılmış dokümanları tanımlamak için daha ayrıntılı bir özellik seti sağlar.

Farklı tarayıcıların, DOM standardıyla çeşitli uyumluluk seviyeleri vardır. Bu ünitedeki DOM tartışması, DOM ile HTML elemanlarına erişmek için **DOM Level 1 Core** ve **DOM Level 1 HTML** API’lerine odaklanır. Çoğu web tarayıcısındaki JavaScript motoru, DOM Level 1’i tamamen destekler. İşte tarayıcılar için temel DOM modelinin bir temsili. **window** nesnesi, DOM hiyerarşisinin en üstündedir ve dokümanı içeren ortamı kontrol eder. **history** nesnesi, tarayıcıdaki sayfaların yakın geçmişi hakkında dahili ayrıntıları tutar. **history** nesnesi, tarayıcıda geri veya ileri düğmelerine tıklamayı simüle etmenize imkân veren metodlara sahiptir.

---

## 🪟 DOM Hiyerarşisindeki Temel Nesneler

**location** nesnesi, bir sayfanın URL’i hakkında bilgi içerir.  **navigator** , istemci internet tarayıcısının veya  *user agent* ’ın nesne temsildir. **navigator** nesnesi için geçerli bir standart yoktur; bu yüzden **navigator** nesnesi üzerinde sorgular çalıştırıldığında dönen özellik değerleri tarayıcılar arasında tutarlı değildir. **screen** nesnesi, ekranın boyutları gibi kullanıcının ekranı hakkında bilgi türetmek için kullanılır. **screen** nesnesi, mobil cihazlarda çalışan tarayıcı pencerelerinin ekran boyutunu belirlemek için faydalıdır. **document** nesnesi, bir sayfa içindeki tüm HTML elemanlarına erişim sağlar. Bir pencereye yüklenen her HTML dokümanı, bir **document** nesnesi haline gelir.

---

## 🌍 Window Object ve Global Kapsam

**window** nesnesi, DOM hiyerarşisindeki tüm nesnelerin en dıştaki global kapsayıcısıdır. Tarayıcı bir sayfayı yüklediğinde, sizin için otomatik olarak bir **window** nesnesi oluşturulur. Daha sonra JavaScript kodunuzdan **window** nesnesinin özelliklerine ve fonksiyonlarına erişebilirsiniz. İstemci taraflı JavaScript’te **Window** nesnesi global nesne olarak görev yapar ve DOM’daki her şey bir **window** içinde gerçekleşir. **window** nesnesi için birçok önceden tanımlı metod vardır. Web sayfalarında kullanılan  **window.alert** , **window.confirm** ve **window.prompt** diyalogları global **window** nesnesinden gelir. DOM API’sindeki metodlar için **window** önekini yazmadan da kullanabilirsiniz. Bu nedenle **window.alert** metodu, mesaj argümanı ile daha basit şekilde **alert** olarak kodlanabilir.

---

## 🌳 DOM Ağaç Yapısı ve Node Türleri

Bu şekil, basit bir HTML dokümanı için nesne modelini gösterir. Soldaki HTML kapsama ( *containment* ) hiyerarşisinin, nesne hiyerarşisiyle eşleştiğine dikkat edin. Nesne diyagramı, HTML dokümanının yapısına karşılık gelen bir ağaç yapısı olarak da temsil edilebilir. Ağaç yapısının dalları **node** olarak adlandırılır. W3C DOM’da iki tür **node** vardır: **element nodes** ve  **text nodes** . Tüm HTML etiketleri ( **html** ,  **head** ,  **meta** , **title** ve  **body** )  **element node** ’lardır. Bir elemanın başlangıç ( *start tag* ) ve bitiş ( *end tag* ) etiketi arasında yer alan gerçek metni içeren node’lar ise  **text node** ’lardır.

---

## 🧾 DOM Level 2 ve White Space

Şekil, dokümanın **FORM** bölümünün DOM Level 2 ağacını gösterir. Elemanlar arasındaki satır sonları ( *line feeds* )  **text node** ’lardır ve DOM Level 2 ağacının bir parçasıdır. DOM Level 2 ağacı, paragraf ve input elemanlarından önce bir satır sonu *text node* içerir. **input** elemanı, input etiketini takip eden tüm metni içeren bir **text node** içerir. **input** elemanını takip eden ek bir satır sonu *text node* daha vardır. Dokümanın form bölümünün DOM Level 0’ı ise yalnızca  **form** , **p** ve **input** kutularına sahip olurdu. DOM Level 2, bazen **"white space"** olarak adlandırılan satır başları ( *carriage returns* ), tablar ve boşlukları ekler.

---

## ✅ Özet

Bu videoda şunları öğrendiniz:  *Document object model (DOM)* , HTML veya XHTML ile JavaScript arasındaki programlama arayüzüdür. DOM’un her bir sonraki seviyesi, yapılandırılmış dokümanları tanımlamak için daha ayrıntılı bir özellik seti sağlar. Farklı tarayıcıların DOM standardıyla farklı uyumluluk seviyeleri vardır. Tarayıcılar için temel DOM, farklı fonksiyonlar yerine getiren nesneleri içeren bir hiyerarşidir. Örneğin **window** nesnesi dokümanın ortamını kontrol eder, **location** nesnesi sayfanın URL’i hakkında bilgi içerir, **screen** nesnesi kullanıcının ekranı hakkında bilgi türetir ve **document** nesnesi sayfa içindeki tüm HTML elemanlarına erişim sağlar. DOM seviyeleri, geliştiricilerin web sayfaları için düz HTML dokümanlarından daha karmaşık formlara kadar çeşitli dokümanlar inşa edebileceği nesne türlerini tanımlar.
