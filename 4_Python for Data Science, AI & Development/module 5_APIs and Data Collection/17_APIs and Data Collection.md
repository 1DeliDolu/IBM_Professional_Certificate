# 📦 Modül 5 Özeti: API'ler ve Veri Toplama

Tebrikler! Bu modülü tamamladınız. Bu noktada şunları biliyorsunuz:

---

## 🔌 API'lerin Temelleri ve Pandas API'si

* Python'daki basit API'ler, hizmetler, kütüphaneler veya verilerle etkileşim için genellikle minimum yapılandırma veya karmaşıklık gerektiren, doğrudan ve kullanımı kolay yöntemler sağlayan uygulama programlama arayüzleridir.
* Bir API, iki yazılım bileşeninin birbiriyle iletişim kurmasını sağlar.
* Python'da bir API kütüphanesini kullanmak; kütüphaneyi içe aktarmayı, HTTP istekleri yapmak için fonksiyon veya metotlarını çağırmayı ve API tarafından sağlanan veri ya da servislere erişmek için yanıtları ayrıştırmayı gerektirir.
* Pandas API, diğer yazılım bileşenleriyle iletişim kurarak veriyi işler.
* Bir sözlük oluşturup ardından bir Pandas nesnesi oluşturmak için `DataFrames` kurucusunu kullandığınızda bir *instance* oluşur.
* `head()` metodu, bir `DataFrame`'in üst kısmından belirtilen sayıda satırı (varsayılan 5) görüntülerken, `mean()` metodu ortalamayı hesaplayıp değerleri döndürür.

---

## 🌍 REST API'ler, HTTP ve Zaman Serileri

* REST API'ler, depolama, daha fazla veriye erişim, yapay zeka algoritmaları vb. gibi kaynaklardan yararlanarak internet üzerinden iletişim kurmanıza imkân tanır.
* HTTP yöntemleri, internet üzerinden veri iletir.
* Bir HTTP mesajı genellikle işlemlere ilişkin talimatlar içeren bir JSON dosyası içerir.
* JSON dosyaları içeren HTTP mesajları, web servislerinden istemciye yanıt olarak geri döndürülür.
* Zaman serisi verileriyle çalışmak, Pandas zaman serisi fonksiyonunu kullanmayı içerir.
* Günlük mum çubukları ( *candlestick* ) için verileri alabilir ve grafiği `Plotly` kullanarak *candlestick* çizimiyle çizebilirsiniz.
* HTTP (HyperText Transfer Protocol), web sayfaları ve kaynaklar dâhil veriyi, Dünya Çapında Ağ üzerindeki bir istemci (web tarayıcısı) ile bir sunucu arasında aktarır.
* HTTP protokolü, farklı türde REST API'lerini uygulamak için yaygın olarak kullanılır.
* Bir HTTP yanıtı, kaynak türü, kaynağın uzunluğu vb. bilgiler içerir.
* Uniform Resource Locator (URL), web'de kaynak bulmanın en yaygın yoludur.
* Bir URL üç parçaya ayrılır: şema ( *scheme* ), internet adresi veya temel URL ( *base URL* ) ve rota ( *route* ).
* `GET` yöntemi, bilgi talep etmek için yaygın yöntemlerden biridir. Diğer bazı yöntemler ayrıca gövdeyi ( *body* ) de içerebilir.
* Response yöntemi, yanıtın sürümünü ve gövdesini içerir.
* `POST` veriyi sunucuya gönderir, `PUT` sunucuda hâlihazırda bulunan veriyi günceller, `DELETE` ise veriyi sunucudan siler.
* `Requests`, HTTP/1.1 isteklerini kolayca göndermenizi sağlayan bir Python kütüphanesidir.
* `GET` yöntemiyle sorgunuzun sonuçlarını değiştirebilirsiniz.
* Bir *query string* ile, bir URL'den ad, kimlik (ID) vb. gibi birden fazla isteğe ilişkin bilgiyi elde edebilirsiniz.

---

## 🕸️ Web Scraping ve HTML Yapısı

* Python'da web scraping; Beautiful Soup ve `requests` gibi kütüphaneleri kullanarak web sitelerinden veri çıkarmayı ve ayrıştırmayı, böylece çeşitli uygulamalar için bilgi toplamayı içerir.
* HTML, açı ayraçlar içinde yer alan ve *tag* olarak adlandırılan mavi metin öğeleriyle çevrili metinden oluşur.
* Bir web sayfasındaki bir HTML öğesini seçerek sayfayı inceleyebilirsiniz.
* Web sayfaları, HTML öğelerine ek olarak CSS ve JavaScript de içerebilir.
* Her HTML dokümanı, içinde dizgeler ve diğer  *tag* 'ler barındırabilen bir HTML ağacına benzer.
* Her HTML tablosu, tablo  *tag* 'lerinden oluşur ve satırlar, başlıklar, gövde vb. öğelerle yapılandırılır.
* Tablo biçimindeki veriler, Pandas içindeki `read_html` metodu kullanılarak web sayfalarından da çıkarılabilir.
* Python'daki Beautiful Soup, HTML ve XML dokümanlarını ayrıştırmak ve içinde gezinmek için kullanılan; web sayfalarından veri çıkarmayı ve veriyi değiştirmeyi daha erişilebilir hâle getiren bir kütüphanedir.
* Bir dokümanı ayrıştırmak için, onu Beautiful Soup kurucusuna geçirerek dokümanı iç içe geçmiş bir veri yapısı olarak temsil eden bir Beautiful Soup nesnesi elde edersiniz.
* Beautiful Soup, HTML'yi, HTML'yi ayrıştırmak için metotlara sahip ağaç benzeri nesneler kümesi olarak temsil eder.
* `NavigableString`, Beautiful Soup işlevselliğini destekleyen bir Python dizgesine benzer.
* `find_all`, *tag* adlarına, özniteliklerine (attribute'larına), bir dizgenin metnine veya bunların bazı kombinasyonlarına göre içerik çıkarmak için kullanılan bir metottur.
* `find_all` metodu, bir  *tag* 'in alt öğeleri arasında gezinir ve filtrelerinize uyan tüm alt öğeleri getirir.
* Sonuç, liste gibi bir Python yineleyicisi ( *iterable* ) olur.

---

## 📁 Dosya Biçimleri ve Veri Okuma

* Dosya biçimleri, düz metin için `.txt` veya virgülle ayrılmış değerler için `.csv` gibi, veriyi dosyalarda saklamak ve temsil etmek için kullanılan belirli yapı ve kodlama kurallarını ifade eder.
* Python, CSV, XML, JSON, `xlsx` vb. gibi farklı dosya biçimleriyle çalışır.
* Bir dosya adının uzantısı, bunun hangi türde bir dosya olduğunu ve hangi yazılımla açılması gerektiğini anlamanızı sağlar.
* CSV dosyalarındaki verilere erişmek için, Pandas gibi Python kütüphanelerini kullanabiliriz.
* Benzer şekilde, JSON, XML ve diğer dosyaları ayrıştırmaya yardımcı olan farklı metotlar vardır.

---

## 📚 Temel Kavramların Sözlüğü

* **Pandas:** Pandas, veriyi işleme ve analiz etme için kullanılan; `DataFrame` gibi veri yapılarını sağlayarak tabular veriyi işleme imkânı veren bir Python kütüphanesidir.
* **Web Scraping:** Web scraping, genellikle Beautiful Soup ve `requests` gibi kütüphanelerden yararlanarak programlama teknikleriyle web sitelerinden veri çıkarmayı içerir.
* **API:** Uygulama Programlama Arayüzleri (API'ler), farklı yazılım uygulamalarının birbirleriyle iletişim kurmasını sağlayarak veri alışverişi için yöntemler sunar.
* **HTTP Yöntemleri:** `GET`, `POST`, `PUT` ve `DELETE` gibi HTTP yöntemleri, web üzerindeki kaynaklar üzerinde işlemler gerçekleştirmek ve istemcilerle sunucular arasındaki veri transferini kolaylaştırmak için kullanılır.
* **Beautiful Soup:** Beautiful Soup, HTML ve XML dokümanlarını ayrıştırmak için kullanılan; web sayfalarından veri çıkarmayı ve veriyi değiştirmeyi kolaylaştıran bir Python kütüphanesidir.
