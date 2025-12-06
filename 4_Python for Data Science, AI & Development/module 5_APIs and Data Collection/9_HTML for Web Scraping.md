# 🌐 Web Kazıma için HTML

## 💡 Giriş: HTML ve Web Kazıma

Bu videoda, Web Kazıma ( *Web Scraping* ) için Hiper Metin İşaretleme Dili yani  *HTML* 'i gözden geçireceğiz.

Birçok faydalı veri, emlak fiyatları ve kodlama sorularına çözümler gibi, web sayfalarında mevcuttur. *Wikipedia* web sitesi, dünyanın bilgisinin bir deposudur.

 *HTML* 'i anladığınızda, bu bilgiyi çıkarmak için  *Python* 'u kullanabilirsiniz.

Bu videoda şunları yapacaksınız:

* Basit bir web sayfasının *HTML* yapısını gözden geçirmek,
* Bir *HTML* etiketinin bileşimini anlamak,
* *HTML* ağaçlarını ( *HTML Trees* ) anlamak,
* *HTML* tablolarını anlamak.

## 🎯 Örnek Senaryo: Oyuncu İsimleri ve Maaşları

Diyelim ki sizden, aşağıdaki sayfadan Ulusal Basketbol Ligi'ndeki oyuncuların adlarını ve maaşlarını bulmanız istendi.

Web sayfası  *HTML* 'den oluşur. Köşeli ayraçlar içinde yer alan ve *tag* (etiket) olarak adlandırılan bir dizi mavi metin unsuruyla çevrelenmiş metinden oluşur.

Bu etiketler, içeriğin tarayıcıda nasıl görüntüleneceğini belirtir. İhtiyacımız olan veri bu metnin içindedir.

## 🧱 Basit Bir HTML Sayfasının Yapısı

İlk kısımda, bu belgenin bir *HTML* belgesi olduğunu bildiren `DOCTYPE html` bulunur.

`html` elementi, bir *HTML* sayfasının kök ( *root* ) elementidir ve `head` elementi sayfa hakkında meta bilgileri içerir.

Sonrasında `body` kısmı gelir; bu, web sayfasında görüntülenen kısımdır. Genellikle ilgilendiğimiz veri buradadır; `h3` ile gösterilen elementleri görürüz, bu da 3. seviye başlık anlamına gelir ve metni daha büyük ve kalın yapar.

Bu etiketler oyuncuların isimlerini içerir; verinin elementlerin içine alındığına dikkat edin. Köşeli ayraç içinde bir `h3` ile başlar ve yine köşeli ayraç içinde `/h3` ile biter.

Ayrıca `p` adında farklı bir etiket vardır; bu, paragraf anlamına gelir ve her `p` etiketi bir oyuncunun maaşını içerir.

## 🏷️ Bir HTML Etiketinin Bileşimi

Bir *HTML* etiketinin bileşimine yakından bakalım.

Burada bir *HTML Anchor* (bağlantı) etiketinin örneği vardır. Bu etiket, *IBM* metnini görüntüler ve üzerine tıkladığınızda sizi *IBM.com* sitesine götürür.

Öncelikle etiket adımız vardır; bu örnekte `a`. Bu etiket, bir sayfayı başka bir sayfaya bağlamak için kullanılan bir köprü ( *hyperlink* ) tanımlar.

Her etiket adını  *Python* 'da bir sınıf, her bir etiketi de o sınıfın bir örneği ( *instance* ) olarak düşünmek faydalı olabilir.

Bir açılış ya da başlangıç etiketi ve bir de bitiş etiketi vardır. Bitiş etiketinde, etiket adının başında bir eğik çizgi (`/`) bulunur.

Bu etiketler içeriği barındırır; bu örnekte, web sayfasında görüntülenen metni.

Bir de özniteliğimiz ( *attribute* ) vardır; bu, Öznitelik Adı ( *Attribute Name* ) ve Öznitelik Değeri ( *Attribute Value* ) bileşenlerinden oluşur. Bu örnekte öznitelik, gidilecek web sayfasının URL'sidir.

Gerçek web sayfaları çok daha karmaşıktır; kullandığınız tarayıcıya bağlı olarak, bir *HTML* elementini seçip ardından *Inspect* (İncele) seçeneğine tıklayabilirsiniz.

Bunun sonucunda, *HTML* kodunu inceleyebilme olanağı elde edersiniz. Ayrıca bu derste ele almayacağımız *CSS* ve *JavaScript* gibi başka tür içerikler de vardır.

## 🌳 HTML Ağaçları ve Hiyerarşi

Asıl element burada gösterilmektedir. Her *HTML* belgesi, aslında bir belge ağacı ( *document tree* ) olarak adlandırılabilir. Basit bir örnek üzerinden gidelim.

Etiketler, metin dizeleri ( *string* ) ve başka etiketler içerebilir. Bu öğeler, etiketin çocukları ( *children* ) olarak adlandırılır. Bunu bir soy ağacı gibi de gösterebiliriz.

İç içe geçmiş her etiket, bu ağaçta ayrı bir seviyedir.

`html` etiketi, `head` ve `body` etiketlerini içerir. `head` ve `body` etiketleri, `html` etiketinin torunları ( *descendants* )dır. Daha özel olarak, `html` etiketinin doğrudan çocuklarıdır.

`html` etiketi ise onların ebeveynidir ( *parent* ). `head` ve `body` etiketleri, aynı seviyede oldukları için kardeş ( *siblings* ) olarak adlandırılır.

`title` etiketi, `head` etiketinin çocuğudur ve `head` etiketi onun ebeveynidir. `title` etiketi, `html` etiketinin bir torunudur ancak doğrudan çocuğu değildir.

Başlık ( *heading* ) ve paragraf ( *paragraph* ) etiketleri `body` etiketinin çocuklarıdır; ve hepsi `body` etiketinin çocukları olduğu için birbirlerinin kardeşidir.

Kalın yazı ( *bold* ) etiketi, başlık etiketinin bir çocuğudur; etiketin içeriği de ağacın bir parçasıdır, ancak bunu çizmek oldukça zahmetli olabilir.

## 📊 HTML Tabloları

Şimdi de *HTML* tablolarını gözden geçirelim.

Bir *HTML* tablosu tanımlamak için `table` etiketini kullanırız. Her tablo satırı `tr` etiketiyle tanımlanır; ilk satır için ayrıca bir tablo başlığı etiketi ( *table header tag* ) kullanabilirsiniz.

Tablo satırındaki hücreler, her biri bir tablo hücresi tanımlayan `td` etiketlerinden oluşur.

İlk satırın birinci hücresi için şuna sahibiz; ilk satırın ikinci hücresi için ise şuna sahibiz; ve bu böyle devam eder.

İkinci satır için şuna sahibiz; ikinci satırın birinci hücresi için şuna sahibiz; ikinci satırın ikinci hücresi için şuna sahibiz; ve benzeri biçimde devam eder.

## ✅ Sonuç: HTML Bilgisiyle Veriyi Çekmeye Hazırız

Artık *HTML* hakkında bazı temel bilgilere sahibiz. Şimdi bir web sayfasından biraz veri çıkarmayı deneyelim.
