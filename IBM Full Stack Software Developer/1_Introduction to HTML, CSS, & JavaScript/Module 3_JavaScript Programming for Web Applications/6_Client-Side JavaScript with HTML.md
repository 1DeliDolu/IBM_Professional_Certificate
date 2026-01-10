## 🖥️ Client-Side JavaScript: with HTML

Client-Side JavaScript with HTML konusuna hoş geldiniz. Bu videoyu izledikten sonra, istemci taraflı bir script’i tanımlayabilecek, istemci taraflı script’lerin ne zaman kullanılabileceğine örnekler verebilecek, **noscript** etiketinin nasıl kullanılacağını açıklayabilecek ve script’lerde  *Event Binding* ’i tanımlayabileceksiniz. İstemci taraflı bir script, bir HTML dokümanına eşlik eden veya doğrudan HTML dokümanının içine gömülebilen bir programdır. Script programı, doküman yüklendiğinde veya bir bağlantı etkinleştirildiğinde ya da bir düğmeye tıklandığında gibi başka bir zamanda istemci cihazda çalışır. JavaScript, HTML içinde bir *scripting* dili olarak yaygın biçimde kullanılsa da, bunun yerine başka *scripting* dilleri de kullanılabilir. Script’ler yazarlara, HTML dokümanlarını son derece etkileşimli biçimlerde değiştirme ve genişletme imkânı sunar. Script’ler bir HTML dokümanı yüklendikten sonra çalışabilir.

---

## 🧩 Client-Side Script Kullanım Örnekleri

Script’ler formları doğrulamak veya yazılırken girdiyi işlemek için kullanılabilir. Script’ler, bir düğmeye tıklanması gibi web sayfasında gerçekleşen olaylar ( *events* ) tarafından tetiklenebilir. Script’ler, bir HTML sayfasında doküman elemanlarını dinamik olarak oluşturmak için kullanılabilir.

---

## 🏷️ script Tag ile Script Ekleme Yöntemleri

Bu slayt, **script** etiketinin bir HTML dokümanına script eklemek için iki şekilde nasıl kullanıldığını gösterir. Örnek 1, bir script’i doğrudan HTML dokümanının içine nasıl ekleyebileceğinizi gösterir. Bu yöntem kısa script’ler için uygundur; ancak script uzun olduğunda, Örnek 2’de kullanılan yöntem tercih edilir. Örnek 2, harici bir script dosyasını işaret etmek için **SRC** özniteliğini kullanır.

Bu yöntemin çeşitli kullanım durumları vardır; örneğin karmaşık etkileşimler için JavaScript kütüphanelerini içe aktarmak veya aynı script’i birden fazla HTML dokümanında kullanmak.

---

## 🚫 noscript Tag Kullanımı

Web sitenizi ziyaret eden bazı kullanıcılar JavaScript’in çalışmasını devre dışı bırakmış olabilir veya  *scripting* ’i desteklemeyen bir tarayıcı kullanıyor olabilir. Bu durumlara imkân tanımak için alternatif yolun içeriğini **noscript** etiketi içine yerleştirin. Tarayıcı  *scripting* ’i desteklemiyorsa, tarayıcı **noscript** etiketi içinde bulunan kod bölümünü çalıştırır.

---

## 🔗 Event Binding

Script’ler, sayfa bir tarayıcı oturumunda çalışırken gerçekleşen belirli olayların algılanmasıyla çalışabilir. Bir olay meydana geldiğinde bir fonksiyonun çağrılmasına *event binding* denir. Örneğin **onload** olayı, tarayıcı bir sayfayı yüklemeyi bitirdiğinde bir script’in çalışmasını sağlayabilir.

Ya da **onclick** olayı gerçekleştiğinde bir fonksiyon çalıştırılabilir. Bu olay, işaretleme cihazı bir elemanın (örneğin bir düğme) üzerinde tıklandığında ve bu eleman olay için bir işleyici ( *handler* ) tanımladığında meydana gelir. Olay işleyicisi ( *event handler* ), düğmeye tıklandığında ne yapılacağını bildiren bir fonksiyondur. Diğer faydalı olaylar arasında, imleç bir elemanın üzerine taşındığında gerçekleşen **on-mouse-over** bulunur. Burada, **showAnswers** adlı  *inline event handler* , düğmeye tıklandığında çalışır.

---

## ✅ Özet

Bu videoda, istemci taraflı bir script’in bir HTML dokümanına eşlik eden bir program olduğunu öğrendiniz. Hatta HTML’in içine gömülü de olabilir.

Script’ler, özellikle daha etkileşimli elemanlar ekleyerek kullanıcı deneyimini geliştirmek için geliştiricilere HTML dokümanlarını genişletme yolları sunar. **script** etiketini kullanarak bir script’i HTML dokümanına dahil edebilir veya harici bir dosyadan bir script çağırabilirsiniz. *Scripting* devre dışı bırakıldığında alternatif sağlamak için **noscript** etiketini kullanın. Script’ler, otomatik olarak çalışmaları için olaylara bağlanabilir. Örneğin **onload** olayı, tarayıcı bir sayfayı yüklemeyi bitirdiğinde bir script’i çalıştırabilir.
