## 🧠 Expert Viewpoints: JSON ve JavaScript Kullanımı

Expert Viewpoints: Using JSON and JavaScript’e hoş geldiniz. Bu videoda, JSON ve JavaScript bilmenin kendilerine nasıl yardımcı olduğuna ve bu yöntemlerin yeni bulut uygulaması geliştiricilerine nasıl fayda sağlayabileceğine dair, birkaç uygulama geliştirme uzmanının görüşlerini dinleyeceğiz.

JavaScript ve JSON’a aşinalık, web geliştiricileri için az çok bir gerekliliktir. Eğer ön yüzle ( *front end* ) hiç çalışmıyorsanız, JavaScript’e dokunmadan idare edebilirsiniz; ancak JSON, veri serileştirme ( *data serialization* ) için fiili ( *de facto* ) standarttır. Başkaları tarafından yazılmış API’leri tüketebilmek ve ayrıca kendi API’lerinizin de JSON döndürmesini sağlayarak başkalarının onları kolayca kullanabilmesini mümkün kılmak için JSON’u nasıl kullanacağınızı öğrenmek isteyeceksiniz.

JSON’u çok sık göreceğiniz bir başka yer de, bir şeyi bilgisayarın kolayca anlayacağı şekilde belirtmeniz gereken durumlardır. Örneğin, muhtemelen bunu ilk kez bir Node.js projesi için gereksinimleri belirtirken göreceksiniz; ancak bunu daha sonra *platform as a service* teklifleri veya Kubernetes iş yükleri için dağıtımları ( *deployments* ) belirtirken de tekrar görebilirsiniz.

---

## 🧩 JSON’un JavaScript ile Doğal İlişkisi

JSON ya da  *JavaScript Object Notation* , JavaScript’in içine gömülüdür, değil mi? Bu yüzden JavaScript’te nesnelerle çalıştığınızda, aslında JSON ile çalışıyorsunuz. Bununla birlikte, RESTful web servislerinde iletişim veya veri için yaygın bir format da JSON’dur. Dolayısıyla Node.js geliştiricileri ve JavaScript geliştiricileri olarak JSON’dan kaçamazsınız. Aslında üzerinde çalışması oldukça dostça bir formattır.

JSON, bir JavaScript geliştiricisiyseniz, bir Node.js geliştiricisiyseniz, anlamanız ve JSON nesneleriyle çalışmanız gereken şeylerden biridir. Bu yüzden, onu ne kadar erken öğrenirseniz o kadar iyi.

---

## 🔁 Serileştirme ve Deserileştirme

JSON, nesneleri bir string içinde kodlamak ( *encode* ) için baskın formatlardan biridir. Ve JSON, JavaScript’te yerel ( *native* ) bir veri tipidir. Dolayısıyla serileştirme ( *serialization* ), JSON nesnesini bir bayt string’ine ( *byte string* ) dönüştürür; deserileştirme ( *deserialization* ) ise bayt string’ini tekrar JSON nesnesine dönüştürür.

JSON konusunda rahat olmanın büyük bir faydası, bulut ( *cloud* ) ve REST API’lerdeki istek ( *request* ) ve yanıt ( *response* ) nesnelerinin çoğu zaman JSON olmasıdır; en azından `curl` seviyesinde veya shell script seviyesinde çalıştığınızda.

---

## 🗄️ JSON Odaklı Veritabanları ve Gündelik Kullanım

JavaScript ve JSON bilmenin bir diğer faydası, JSON odaklı doküman veritabanlarıyla ( *JSON oriented document databases* ) çalışmaktır. JavaScript yazmak ve JSON kullanmak bana sürekli yardımcı oluyor; çünkü JavaScript, internetin dilidir. Bu yüzden onu birçok uygulamada görürsünüz.

Ve mevcut bir projeye yalnızca biraz kod ekleyebilmek ya da sıfırdan JavaScript yazabilmek gerçekten kullanışlıdır. Çok popüler bir dili konuşmak gibidir.

JSON, Python ve Node.js dahil olmak üzere modern dillerin birçoğu tarafından kullanılır. Bu yüzden ben her gün Python kullanıyorum; çünkü verinizi yapılandırmak ve onu ileri geri taşımak için gerçekten faydalı bir yoldur. Ve biliyorsunuz, çoğu API’den yanıt almanın yolu da budur.
