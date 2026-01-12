# 🧪 BDD Örneği

Bu videoyu izledikten sonra, BDD spesifikasyonlarında *feature* ve *scenario* kavramlarının ne olduğunu açıklayabilecek ve bir BDD spesifikasyonunun nasıl oluşturulacağını özetleyebileceksiniz.

## 🧾 BDD Spesifikasyonunun Bölümleri: Feature ve Scenario

Bir spesifikasyon, kullanıcı hikâyelerini temsil eden bir veya daha fazla  *feature* ’dan oluşur. İhtiyacınız olduğu kadar feature oluşturabilirsiniz. Ben her feature’ı kendi spesifikasyon dosyasına koymayı severim, ancak elbette hepsini tek bir dosyaya koyabilir ya da nasıl isterseniz o şekilde gruplayabilirsiniz.

Bir Gherkin dokümanında ilk anahtar kelime genellikle  **Feature** ’dır; ardından iki nokta üst üste ve başlık gelir. Buradan itibaren feature’lar standart kullanıcı hikâyesi sözdizimini kullanır:

> “Bir rol olarak, bir işlevsellik istiyorum, Böylece bir fayda elde ediyorum.”

Bu, çevik ( *agile* ) ekiplerin kullanıcı hikâyelerini tanımlarken kullandığı bir sözdizimidir; dolayısıyla çevik pratikleri takip ediyorsanız bunu tanımalısınız. Hikâyelerinizi Kanban panonuzda bu şekilde yazıyorsanız, onları BDD spesifikasyonunuza kolayca kopyalayıp yapıştırabilirsiniz.

## 🎬 Her Feature İçin Somut Örnekler: Senaryolar

Her feature, bir veya daha fazla somut örnek ya da *scenario* içerir. Bir scenario, bir feature’ın tek bir davranışını tanımlayan bir durumdur ve bu tanımı yazmak için **Given, When, Then** sözdizimini kullanırsınız.

Her scenario, ilgili davranış için tam bir test vakası oluşturur. Laboratuvarlarda **Behave** test aracını kullandığınızda bu scenario’lara karşı testler çalıştırırsınız. Feature’ın farklı davranışlarını tanımlamak için ihtiyacınız olduğu kadar scenario yazın.

## 🛍️ Feature ve Scenario Yazımına Bir Örnek

Feature ve scenario’ların nasıl yazılacağını göstermek için bir örneğe bakalım. Çoğu insan alışverişin nasıl çalıştığını bildiği için perakende sektöründen bir örnek kullanacağız.

Dokümana **Feature** anahtar kelimesiyle başlarsınız; ardından iki nokta ve başlık gelir. Başlık, bu feature’ın ne hakkında olduğunu ifade etmelidir. Test vakalarını çalıştırdığınızda araç tarafından görüntülenir; böylece testlerin hangi feature hakkında rapor verdiğini bilirsiniz.

Bu feature’ın başlığı  **“Returns go to stock”** ’tur; böylece bu feature’ın kapsamını bilirsiniz. İadeleri ele alır; özellikle iade edilen ürünlerin stoğa geri dönmesine ilişkin beklenen davranışı.

Feature satırının altında kullanıcı hikâyesi yer alır:

> “As a store owner, I want to add items back to stock when they’re returned, So that I can keep track of the stock.”

BDD araçları bu kullanıcı hikâyesini herhangi bir şekilde ayrıştırmaz. Testleri yürütürken yalnızca bu satırları görüntüler; böylece bu feature’ın kullanıcı hikâyesini bilirsiniz.

## 💸 Scenario 1: İade Edilen Ürün Stoğa Geri Dönmeli

Sonra ilk scenario gelir. Bunun da, bu scenario’yu çalıştırdığınızda görünen bir başlığı vardır:

**“Refunded items should be returned to stock.”**

Bu başlık, bu scenario’nun para iadesi ( *refund* ) ile ilgili olduğunu söyler. Para iadesi, müşterinin bir ürünü iade edip parasını geri istemesidir.

BDD aracı, bu scenario’nun geri kalanını ayrıştıracaktır. Unutmayın: bu scenario yalnızca insanların okuması için değil, bilgisayarın işlemesi içindir de. Her satır, bir test vakasının bir bölümünü çalıştıran bir adımı tetikler. “Test vakasının bir bölümü” diyorum çünkü test vakasının tamamı scenario’nun kendisidir. Üzerinden geçtikçe ne demek istediğimi göreceksiniz.

İlk adım bir önkoşul belirtir:

> “Given that a customer previously bought a black sweater from me.”

Bu, bağlamı kurar; yani testin başlangıç durumunu. Testi çalıştırmadan önce bir müşteriye ihtiyacınız olduğunu ve o müşterinin siyah bir kazak için bir siparişe sahip olması gerektiğini söyler.

İkinci adım başka bir önkoşul belirtir:

> “And I have three black sweaters in stock.”

**And** anahtar kelimesinin bir önceki anahtar kelimenin anlamını üstlendiğini unutmayın. Burada önceki anahtar kelime **Given** olduğu için bu adım, “Given I have three black sweaters in stock.” ile eşdeğerdir. Yani testi değerlendirebilmeniz için stokta üç siyah kazak olduğundan emin olmanız gerektiğini söyler.

Üçüncü adım şudur:

> “When they return the black sweater for a refund.”

Bu, bir şeyin olmasına neden olan olaydır. Bu adım, test edilen sistemde siyah kazağın iadesini başlatır ve para iadesi talep eder.

Son olarak, son adım şudur:

> “Then I should have four black sweaters in stock.”

Bu, gözlemlenen sonucun ne olması gerektiğine dair test doğrulamasıdır. Bu adımda BDD aracı, stokta gerçekten dört siyah kazak olup olmadığını kontrol eder. Eğer varsa scenario geçer; yoksa scenario başarısız olur.

## 🔁 Scenario 2: Değişim Yapılan Ürün Stoğa Geri Dönmeli

Bu feature’ın ikinci bir scenario’su var; ona da bakalım.

İkinci scenario şudur:

**“Exchanged items should be returned to stock.”**

İlk scenario’dan farklı olarak bu, para iadesi ile ilgili değildir; müşterilerin satın aldıkları ürünü başka bir ürünle değiştirmesiyle ilgilidir.

Adımları konuşalım:

> “Given that a customer previously bought a blue shirt from me.”

Given’in testi çalıştırmadan önceki başlangıç durumunu ifade ettiğini bilirsiniz. BDD aracı bunu gördüğünde, bir müşteriniz olduğunu ve müşterinin içinde mavi bir gömlek bulunan bir siparişe sahip olduğunu garanti eden bir adımı çalıştırır.

> “And I have two blue shirts in stock.”

Given’den sonra gelen And, başka bir Given gibidir; dolayısıyla araç stokta iki mavi gömlek olduğundan emin olacak bir adımı çalıştırır.

> “And I have three black shirts in stock.”

Yine And bir Given’dir; bu yüzden araç stokta üç siyah gömlek olduğundan emin olan bir adımı çalıştırır.

Bu noktada başlangıç durumunda stokta iki mavi gömlek ve üç siyah gömlek vardır.

> “When they return a blue shirt for a replacement in black.”

When anahtar kelimesi olayı belirtir. Bu, iade fonksiyonunu beklenildiği gibi davranıp davranmadığını görmek için test eder.

> “Then I should have three blue shirts in stock.”

Then anahtar kelimesi, davranış doğrulamasını belirtir. Bu adım bir test doğrulamasıdır; önceki değişimden sonra stokta üç mavi gömlek olması gerektiğini belirtir çünkü iade edilen mavi gömlek stoğa geri dönmüştür.

> “And I should have two black shirts in stock.”

And yine bir önceki anahtar kelimenin anlamını üstlenir; bu adım “Then I should have two black shirts in stock.” ile aynıdır. Then adımı sonucu ölçtüğü için, değişim yapmak üzere stoktan bir siyah gömlek çıkarıldığından dolayı stokta iki siyah gömlek kaldığını kontrol eder.

BDD spesifikasyonunun harika yanı, bu dokümanın paydaşlarınızla birlikte tam olarak oluşturduğunuz doküman olması ve BDD testlerinizi çalıştırmak için **Behave** gibi bir BDD aracıyla kullandığınız doküman olmasıdır. Test araçlarınız da dahil olmak üzere herkesin anlayabileceği tek bir dokümana sahip olursunuz.

## 📌 Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* Bir  *feature* , bir kullanıcı hikâyesinin yüksek seviyeli tanımıdır.
* Bir  *scenario* , bir feature’ın tek bir davranışını tanımlayan bir durumdur.
* Her scenario, davranış için tam bir test vakası oluşturur.
* BDD spesifikasyonunu oluşturmak için bir feature yazarsınız ve ardından **Given, When, Then** sözdizimini kullanarak scenario’lar yazarsınız.
