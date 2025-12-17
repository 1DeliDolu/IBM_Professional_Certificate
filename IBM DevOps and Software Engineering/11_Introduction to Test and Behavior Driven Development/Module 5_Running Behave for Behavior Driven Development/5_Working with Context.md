# 🧠 Working with Context

Bu videoyu izledikten sonra, *context* değişkenini tanımlayabilecek ve  *context* ’i Python adımları arasında bilgi aktarmak için nasıl kullanacağınızı açıklayabileceksiniz.

 *Context* ’in ne olduğuna ve nasıl kullanabileceğinize yakından bakalım. *Context* değişkeni her adım tanımına ( *step definition* ) aktarılır; bu nedenle yazdığınız tüm adım fonksiyonlarının ilk argümanı olarak *context* adlı bir değişken bulunur.

Onu, içine bir şeyler koyup çıkarabileceğiniz ve etrafta taşıyabileceğiniz bir kap ya da çanta gibi düşünebilirsiniz. Tüm özellik dosyası ( *feature file* ) ve tüm adımlar boyunca varlığını sürdürür. Özellik dosyasından çağrılan her adım aynı  *context* ’i paylaşır. Bu yaşam süresi,  *context* ’i bir adımdan diğerine—ya da bu bilgiye ihtiyaç duyabilecek herhangi bir sonraki adıma—bilgi aktarmak için kullanışlı hale getirir.

---

## 🧪 Context Kullanım Alanları

Şimdi *context* için bazı kullanım örneklerini konuşalım. Bu örnek, Selenium yerine Python Flask test istemcisini ( *test client* ) kullanır; ancak adımlar arasında değişkenleri *context* ile nasıl gezdirebileceğinizi gösterir.

İlk adım dosyadaki **“Given the server is started.”** adımıdır. Bu tek satırlık kod, Flask uygulamasından bir test istemcisi alır ve bunu `context.client` adlı bir *context* değişkeninde saklar.

Artık herhangi bir sonraki adım, test istemcisini yalnızca `context.client`’a referans vererek alabilir. Bir sonraki adım da tam olarak bunu yapar. `context.client` üzerinde `get()` metodunu çağırarak test edilen uygulamanın kök URL’ini ( *root URL* ) alır.

Bu çağrının sonuçlarını başka bir *context* değişkeninde `context.response` olarak saklar. Böylece bu `get()` isteğinin yanıtını incelemesi gereken başka herhangi bir adım, onu `context.response` içinde bulabilir.

Tahmin edeceğiniz gibi, bir sonraki adım fonksiyonu tam da bunu yapar. `context.response`’un `data` özelliğine referans verir ve fonksiyona geçirilen mesaj dizesinin ( *message string* ) verinin herhangi bir yerinde bulunabildiğini doğrular ( *assert* ).

Bu, veriyi bir adımdan diğerine *context* içinde saklayarak nasıl aktarabileceğinize dair bir örnektir.

---

## 📋 Panoyu Simüle Etme

Bir sonraki örnek, bir panoyu ( *clipboard* ) simüle eder. Bazen bir alandan bilgiyi kopyalayıp başka bir alana yapıştırmanız gerekir, ancak maalesef Selenium panoları desteklemez.

Bu yüzden, kopyala-yapıştır işlemini pano kullanarak simüle etmek için kullandığım küçük bir numara var.

İlk adım **“I copy the element_name field”** adımıdır. Bu adım, bir değişken yer değiştirme ( *variable substitution* ) kullanır; bu, kopyanın kaynağı olarak kullanılacak bir öğe adını ( *element name* ) içeri aktarmanın bir yoludur.

Bu adımın ilk satırı, o ad için öğe kimliğini ( *element ID* ) hesaplar. İkinci satır, öğe kimliğini ileterek gerçek öğeyi almak için `context.driver.find_element_by_ID` çağrısını yapar.

Üçüncü satır, öğe üzerinde `get attribute` çağrısı yaparak değeri ister ve kopyalama burada gerçekleşir. Bu değeri `context.clipboard` adlı bir değişkende saklar.

Bu ismi ben uydurdum. Herhangi bir şey de diyebilirdim, ama “clipboard” uygun geldi. Artık herhangi bir sonraki adım `context.clipboard`’ı inceleyebilir ve oraya bir şey kopyalanıp kopyalanmadığını görebilir.

Sonra, yapıştırma işlevini yapan bir adımımız var:  **“I paste the ‘element_name’ field”** . Yine alanın adını hesaplar ve ardından öğeyi almak için `context.driver.find_element_by_ID` çağrısını yapar.

Adım öğeyi aldıktan sonra, yapıştırmaya hazırlık için onu temizler ( *clear* ). Bu son satır, yapıştırmanın gerçekleştiği yerdir.

Öğe üzerinde `send_keys()` çağrısı yapar ve kopyalama adımı tarafından oraya kaydedilen her ne ise onu içeren `context.clipboard` değişkenini geçirir. Dikkat edin; bu iki adım oldukça geneldir. Herhangi bir öğenin değerini alıp simüle edilen panoya kaydedebilir ve ardından bu değeri herhangi bir öğeye tuş vuruşları olarak gönderebilir.

Bu örnek, kopyala-yapıştır işlevselliği için basit ama etkili bir pano uygulamasıdır.

---

## ✅ Özet

 *Context* ’i anlamak için gerekenler bu kadar. Onu verileriniz için bir kap olarak düşünebilirsiniz. İhtiyaç duyduğunuz veriyi saklamak için kullanın; böylece özellik dosyasının süresi boyunca tüm adımlarınız için kullanılabilir olacaktır.

Bu videoda şunları öğrendiniz:  *context* , her adım tanımına aktarılan bir değişkendir; adımlar arasında bilgi aktarmak için, bir adımın *context* değişkeninde saklayın ve başka bir adımda o değişkeni kullanın.
