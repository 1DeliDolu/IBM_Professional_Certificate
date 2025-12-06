# 🧩 Uygulama Programlama Arayüzü (API)

## 🧠 API’ye Genel Bakış

Bu videoda Uygulama Programlama Arayüzlerini ( *Application Program Interface* , kısaca  *API* ) ele alacağız.

Özel olarak, bir API’nin ne olduğunu, API kütüphanelerini ve REST API’lerini; bunlara ek olarak İstek ( *Request* ) ve Yanıt ( *Response* ) kavramlarını ve PyCoinGecko ile bir örneği tartışacağız.

Bir API, iki yazılım parçasının birbiriyle konuşmasını sağlar. Örneğin, elinizde programınız, bazı verileriniz ve başka yazılım bileşenleriniz vardır. Girdiler ve çıktılar aracılığıyla diğer yazılımlarla iletişim kurmak için API’yi kullanırsınız.

Tıpkı bir fonksiyonda olduğu gibi, API’nin nasıl çalıştığını bilmek zorunda değilsiniz; sadece aldığı girdileri ve ürettiği çıktıları bilmeniz yeterlidir. `pandas` aslında, çoğu Python ile bile yazılmamış olan bir yazılım bileşenleri kümesidir.

---

## 🐼 Pandas API’si ile Çalışmak

Elinizde bazı veriler vardır. Bir dizi yazılım bileşeniniz vardır. Diğer yazılım bileşenleriyle iletişim kurarak veriyi işlemek için `pandas` API’sini kullanırız.

Şimdi diyagramı sadeleştirelim. Bir sözlük ( *dictionary* ) oluşturup ardından `DataFrame` kurucusunu ( *constructor* ) kullanarak bir `pandas` nesnesi oluşturduğunuzda, API jargonunda buna bir “örnek” ( *instance* ) denir.

Sözlüğün içindeki veriler `pandas` API’sine aktarılır. Daha sonra API ile iletişim kurmak için bu  *dataframe* ’i kullanırsınız.

---

## 🌐 REST API’leri ve İstemci Kavramı

`head` metodunu çağırdığınızda, *dataframe* API ile iletişim kurar ve  *dataframe* ’in ilk birkaç satırını görüntüler. `mean` metodunu çağırdığınızda, API ortalamayı hesaplar ve değerleri döndürür.

REST API’leri, başka bir popüler API türüdür; internet üzerinden iletişim kurmanıza olanak tanıyarak depolama gibi kaynaklardan yararlanmanızı, daha fazla veriye erişmenizi, yapay zeka algoritmalarını ve çok daha fazlasını kullanmanızı sağlar.

Buradaki *RE* “ *Representational* ”ı, *S* “ *State* ”i, *T* ise “ *Transfer* ”i ifade eder. REST API’lerinde programınıza *istemci* ( *client* ) denir.

API, internet üzerinden çağırdığınız bir web hizmetiyle iletişim kurar. İletişim, girdi veya istek ( *request* ) ve çıktı veya yanıt ( *response* ) ile ilgili bir dizi kural içerir. Şimdi bazı yaygın terimlere bakalım.

---

## 🔗 İstemci, Kaynak, Uç Noktalar ve HTTP Yöntemleri

Siz ya da kodunuz bir *istemci* olarak düşünülebilir. Web hizmetine ise bir *kaynak* ( *resource* ) denir.

İstemci, hizmeti bir *uç nokta* ( *endpoint* ) aracılığıyla bulur. Bunu bir sonraki bölümde daha ayrıntılı olarak inceleyeceğiz.

İstemci, kaynağa istekler gönderir ve yanıt da istemciye geri döner.  *HTTP yöntemleri* , internet üzerinden veri iletmenin bir yoludur.

REST API’lerine ne yapmaları gerektiğini bir istek ( *request* ) göndererek söyleriz. Bu istek genellikle bir HTTP mesajı aracılığıyla iletilir. HTTP mesajı genellikle bir JSON dosyası içerir.

---

## 🪙 Kripto Para Verileri ve PyCoinGecko API’si

Bu dosya, hizmetin hangi işlemi gerçekleştirmesini istediğimize dair talimatları içerir. Bu işlem, internet aracılığıyla web hizmetine iletilir. Hizmet bu işlemi gerçekleştirir.

Benzer bir şekilde, web hizmeti bir HTTP mesajı aracılığıyla bir yanıt döndürür ve bilgiler genellikle bir JSON dosyası aracılığıyla gönderilir. Bu bilgiler tekrar istemciye iletilir.

Kripto para verileri, sürekli güncellendiği ve kripto para alım satımı için hayati önem taşıdığı için API’lerde kullanılmak üzere mükemmeldir.

CoinGecko API’si için, CoinGecko tarafından her dakika güncellenen `PyCoinGecko` adlı Python istemci/sarmalayıcısını ( *client/wrapper* ) kullanacağız.

Bu sarmalayıcıyı/istemciyi kullanıyoruz, çünkü kullanımı kolay olduğundan siz verileri toplama görevine odaklanabilirsiniz; ayrıca zaman serisi verileriyle çalışmak için `pandas` zaman serisi fonksiyonlarını da tanıtacağız.

`PyCoinGecko` kullanarak veri toplamak basittir. Tek yapmamız gereken, kütüphaneyi kurup içe aktarmak ( *import etmek* ), ardından bir istemci nesnesi oluşturmak ve son olarak verilerimizi talep etmek için bir fonksiyon kullanmaktır.

Bu fonksiyonda, son 30 güne ait, ABD doları cinsinden *bitcoin* verilerini alıyoruz.

Bu durumda yanıtımız, fiyat, piyasa değeri ( *market cap* ) ve toplam hacimleri içeren, her birinde UNIX zaman damgası ( *timestamp* ) ve o andaki fiyat bulunan iç içe geçmiş listelerden oluşan bir Python sözlüğü şeklinde ifade edilen bir JSON’dur.

Biz yalnızca fiyata ilgi duyduğumuz için, `price` anahtarını kullanarak sadece bunu seçeceğiz.

İşleri basitleştirmek için, iç içe geçmiş listemizi `timestamp` ve `price` sütunlarına sahip bir  *DataFrame* ’e dönüştürebiliriz; ancak `timestamp` sütununu anlamak zordur.

---

## 📈 Zaman Serisi Dönüşümü ve Mum Grafik

Bunu, `pandas` içindeki `to_datetime` fonksiyonunu kullanarak daha okunabilir bir formata dönüştüreceğiz.

`to_datetime` fonksiyonunu kullanarak okunabilir zaman verileri oluştururuz; girdi `timestamp` sütunudur ve zaman birimi milisaniye olarak ayarlanır. Çıktıyı `date` adlı yeni bir sütuna ekleriz.

Şimdi bir *mum grafiği* ( *candlestick plot* ) oluşturmak istiyoruz. Günlük mumlar için verileri elde etmek üzere, her günün minimum, maksimum, ilk ve son fiyatını bulmak için `date` sütununa göre gruplayacağız.

Son olarak, mum grafik oluşturmak ve çizdirmek için `plotly` kütüphanesini kullanacağız.

Artık HTML dosyasını açıp sekmenin sol üst köşesindeki `Trust HTML` seçeneğine tıklayarak mum grafiğini görüntüleyebiliriz. Grafik aşağı yukarı şöyle görünmelidir.
