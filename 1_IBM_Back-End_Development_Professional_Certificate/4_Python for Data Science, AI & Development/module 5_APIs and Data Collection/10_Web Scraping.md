# 🕸️ Web Scraping

## 🎯 Video Hedefleri ve Giriş

Bu videoda **Web Scraping** konusunu ele alacağız.

Bu videoyu izledikten sonra:

* *web scraping* tanımlayabilecek,
* `BeautifulSoup` nesnelerinin rolünü anlayabilecek,
* `find_all` metodunu uygulayabilecek
* ve bir web sitesini *web scrape* edebileceksiniz.

Bir spor takımının en iyi oyuncularını bulmak için yüzlerce veri noktasını analiz etmek isteseydiniz ne yapardınız?

Farklı web sitelerinden bilgileri tek tek kopyalayıp bir **e-tabloya** mı yapıştırırdınız?

Doğru veriyi bulmak için saatler harcayıp, sonunda görev çok bunaltıcı olduğu için vaz mı geçerdiniz?

İşte burada **web scraping** yardımcı olabilir.

Web scraping, bir web sitesinden bilgileri otomatik olarak çıkarmak için kullanılabilen bir süreçtir ve saatler değil, birkaç dakika içinde kolayca gerçekleştirilebilir.

Başlamak için sadece biraz Python koduna ve **Requests** ile **Beautiful Soup** adında iki modülün yardımına ihtiyacımız var.

---

## 🏀 Ulusal Basketbol Ligi Örneği ve BeautifulSoup Nesnesi

Diyelim ki sizden, aşağıdaki web sayfasından **Ulusal Basketbol Ligi** oyuncularının adını ve maaşını bulmanız istendi.

Önce `BeautifulSoup`’u içe aktarırız.

Web sayfasının HTML’ini, `HTML` adlı değişkende bir **string** olarak saklayabiliriz.

Bir dokümanı *parse* etmek için, onu `BeautifulSoup` kurucusuna ( *constructor* ) geçiririz.

Böylece, belgeyi iç içe geçmiş bir veri yapısı olarak temsil eden `soup` adlı `BeautifulSoup` nesnesini elde ederiz.

`BeautifulSoup`, HTML’i, HTML’i *parse* etmek için kullanılan metotlara sahip, ağaç benzeri ( *Tree-like* ) nesneler kümesi olarak temsil eder.

Oluşturduğumuz `soup` adlı `BeautifulSoup` nesnesini kullanarak `BeautifulSoup` nesnesini gözden geçireceğiz.

---

## 🏷️ Tag Nesnesi ve Ağaç (Tree) Temsili

`tag` nesnesi, orijinal belgedeki bir HTML etiketine karşılık gelir.

Örneğin, `"title"` etiketi.

`h3` etiketini ele alalım.

Aynı ada sahip birden fazla `tag` varsa, bu etikete sahip ilk öğe seçilir.

Bu durumda, **Lebron James** için, ismin `"b"` (bold) niteliği içinde yer aldığını görürüz.

Bunu çıkarmak için **ağaç (Tree) temsili**ni kullanırız.

Haydi ağaç temsilini kullanalım.

---

## 🌿 Ağaçta Gezinme: child, parent ve sibling

`tag-object` değişkeni burada yer alır.

Etiketin *child* (çocuk) öğesine erişebilir veya dal boyunca aşağı doğru şu şekilde ilerleyebilirsiniz:

Ağaçta yukarı doğru gezinmek için `parent` niteliğini kullanabilirsiniz.

`tag child` değişkeni burada yer alır.

`parent`’a erişebiliriz.

Bu, orijinal `tag` nesnesidir.

`"tag object"`in *sibling* (kardeş) öğesini bulabiliriz.

Bunun için sadece `next-sibling` niteliğini kullanırız.

---

## 🧬 Özellikler, Navigable String ve `find_all` Metodu

Birinci kardeşin ( *sibling one* ) kardeşini bulabiliriz.

Yine `next sibling` niteliğini kullanırız.

`tag child` nesnesini ele alalım.

Özelliğin adını ( *name* ) ve değerini ( *value* ), bir sözlükte anahtar–değer çifti olarak şu şekilde erişebilirsiniz.

İçeriği, bir **Navigable string** olarak döndürebilirsiniz; bu, `BeautifulSoup` işlevselliğini destekleyen bir Python string’ine benzer.

Şimdi `find_all` metodunu gözden geçirelim.

Bu bir filtredir; bir etiketin adını, özelliklerini, bir string’in metnini veya bunların bazı kombinasyonlarını temel alarak filtreleme yapmak için filtreleri kullanabilirsiniz.

---

## 🍕 Pizza Listesi Örneği ve Satır/Sütunlara Erişim

Pizza yerlerinin listesini ele alalım.

Daha önce olduğu gibi bir `BeautifulSoup` nesnesi oluşturun.

Ancak bu sefer, ona `table` adını verin.

`find_all()` metodu bir etiketin alt öğeleri (descendants) arasında gezinir ve filtrelerinize uyan tüm alt öğeleri getirir.

Bunu, `table` üzerinde `tr` etiketi ile uygulayın.

Sonuç, bir listeye çok benzeyen Python  *iterable* ’ıdır; her öğe, `tr` için bir `tag` nesnesidir.

Bu, listedeki her bir satıra karşılık gelir – **tablo başlığı** dahil.

Her öğe bir `tag` nesnesidir.

İlk satırı ele alalım.

Örneğin, ilk tablo hücresini çıkarabiliriz.

Ayrıca her tablo hücresini dolaşabiliriz.

Önce, `"table rows"` listesini, `row` değişkeni aracılığıyla dolaşırız.

Her öğe tablodaki bir satıra karşılık gelir.

Tüm tablo hücrelerini bulmak için `find_all` metodunu uygulayabilir, ardından her satır için `cells` değişkeni üzerinden yineleme yapabiliriz.

Her yinelemede, `cell` değişkeni, ilgili satır için tablodaki bir öğeye karşılık gelir.

Her bir öğe üzerinde yinelemeye devam eder ve bu işlemi her satır için tekrarlarız.

---

## 🌐 Requests ile Bir Web Sayfasını Scrape Etme

Şimdi `BeautifulSoup`’u bir web sayfasına nasıl uygulayacağımızı görelim.

Bir web sayfasını *scrape* etmek için ayrıca `Requests` kütüphanesine de ihtiyaç duyarız.

İlk adım, ihtiyaç duyulan modülleri içe aktarmaktır.

Web sayfasını indirmek için `requests` kütüphanesinden `get` metodunu kullanın.

Girdi, URL’dir.

Metni almak için `text` niteliğini kullanın ve bunu `page` değişkenine atayın.

Ardından, `page` değişkeninden `soup` adlı bir `BeautifulSoup` nesnesi oluşturun.

Bu, HTML sayfasını *parse* etmenizi sağlar.

Artık sayfayı *scrape* edebilirsiniz.

Daha fazlası için laboratuvarlara ( *labs* ) göz atın.
