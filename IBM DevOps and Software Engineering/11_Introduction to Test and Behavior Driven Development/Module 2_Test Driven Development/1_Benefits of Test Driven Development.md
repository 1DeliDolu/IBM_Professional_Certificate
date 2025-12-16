# 🧪 Test Güdümlü Geliştirmenin Faydaları

Bu videoyu izledikten sonra **test güdümlü geliştirmeyi (TDD)** tanımlayabilecek, **Kırmızı/Yeşil/Yeniden Düzenle (Red/Green/Refactor)** iş akışının her adımını açıklayabilecek ve **DevOps için TDD’nin faydalarını** anlatabileceksiniz.

## 🧩 Test Güdümlü Geliştirmeyi Tanımlama

Test güdümlü geliştirme, geliştirdiğiniz kodun tasarımını **birim test vakalarının** yönlendirmesi anlamına gelir. Bu, kodun nasıl çağrılacağına ve çağıranın karşılığında ne beklediğine odaklanmanızı sağlar.

Ben TDD’ye ilk kez bir **API** oluştururken ikna oldum. API’nin derinlerinde çalışıyordum ve bazı verilere ihtiyacım vardı, bu yüzden çağrıya bir parametre olarak ekledim. Sonra başka bir veriye ihtiyacım oldu ve onu da parametre olarak ekledim. Sonunda işim bittiğinde, harika bir API oluşturduğumu düşünüyordum; ancak bunun için test vakasını yazmaya gittiğimde, çağıran kişi olarak kodumu çağırmak için gereken verilerin yarısına sahip olmadığımı fark ettim. Bu korkunç bir API’ydi ama ben bunu, koduma tüketici gözünden bakıp onu çağırmaya çalışana kadar bilmiyordum.

## 🧠 TDD’nin Temel Mantığı

Bu yüzden test güdümlü geliştirmede, önce sahip olmayı istediğiniz kod için test vakasını yazarsınız. Sonra test vakasının geçmesini sağlayacak kodu yazarsınız. TDD, tüketici API’nin neyi içeri geçirmek isteyeceğini, dışarıda hangi sonuçları bekleyeceğini düşünmenizi gerektirir ve sizi müşteri odaklı tutar.

“Henüz yazmadığım bir kod için nasıl test vakası yazarım?” diye düşünebilirsiniz. Ben ilk kez bir TDD kursu aldığımda, profesör bize bir test vakası verdi ve “Bir program yazmanız gerekiyor ama programın ne yaptığını söylemeyeceğim. İşte test vakaları. Programı yazın ve gönderin.” dedi. Bu adamın deli olduğunu düşünmüştüm.

Sonra test vakalarını okumaya ve onların koddan ne beklediğini anlamaya başladım. Ardından kodu yazıp bu beklentileri karşılamaya başladım. Bu süreç, bir tasarım dokümanını takip etmeye çok benziyordu. Sonra fark ettim:  **test güdümlü tasarım** . Bu test vakaları tasarımdı.

## 📄 TDD’yi Tasarım Dokümanı Gibi Düşünmek

Dolayısıyla TDD’yi bir tasarım dokümanınız olarak düşünebilirsiniz. Yalnızca test vakalarını takip ederek gerçekten bir program yazabilmem inanılmazdı; ama yıllar önce o ödevi almış olmasaydım buna inanmazdım.

TDD sizi kodun amacına odaklar:

* Ne yapması gerekiyor?
* Hangi girdilere ihtiyaç duyuyor?
* Hangi çıktılar üretilmeli?

Bu davranışı belgeleyen test vakasını yazarsınız ve ardından bu davranışı sergileyecek kodu yazar, testin geçmesini sağlarsınız.

## 🔁 Kırmızı/Yeşil/Yeniden Düzenle İş Akışı

Bu, test güdümlü geliştirmenin temel iş akışıdır:

1. Sahip olmayı istediğiniz kod için **başarısız olan bir test vakası** yazın. Bu, kodun nasıl çağrılacağını ve karşılığında ne beklediğinizi ifade eder.
2. Sonra bu test vakasının geçmesini sağlayacak **yeterli kadar kod** yazın. Mükemmel olmak zorunda değildir. Güzel olmak zorunda değildir. Testin geçmesini sağlamak zorundadır.
3. Ardından kaliteyi artırmak için kodu  **yeniden düzenleyin (refactor)** . Belki başlangıçta sabit bir değer döndürdünüz ve artık gerçek değeri hesaplama zamanı gelmiştir.
4. Son olarak süreci  **tekrarlayın** .

Bu iş akışının tamamı **Kırmızı/Yeşil/Yeniden Düzenle (Red/Green/Refactor)** olarak bilinir. Birçok test aracı bu şemayı izler. Bu araçlar başarısız test vakalarını  **kırmızı** , geçen test vakalarını **yeşil** renkte gösterir. Red/Green/Refactor adı buradan gelir.

## ⚙️ DevOps İçin TDD Neden Önemlidir?

Öncelikle geliştiriciler için  **zaman kazandırır** . Kodun özelliklerini yazarken veya mevcut özellikleri değiştirirken, test vakalarınız bir şeyin bozulup bozulmadığını hızlıca bildirir.

Bu, daha güvenli hissettiğiniz için **daha hızlı kod yazmanıza** olanak tanır. Artık bir şeyi değiştirdiğinizde bir şeyi bozmuş olma ihtimali konusunda endişelenmeniz gerekmez; çünkü kodu yeniden düzenlerken çok daha hızlı hareket edebilirsiniz ve test vakaları davranıştaki değişiklikleri yakalar.

Testler, kodun beklediğiniz gibi çalıştığını garanti eder. İstediğiniz davranışı tanımlamak için önce test vakasını yazarsanız, test geçtiğinde bu davranışı başardığınızı bilirsiniz.

Test vakaları ayrıca gelecekteki değişikliklerin kodu bozmamasını sağlar. Başarısız test vakaları, bir şeyin kodu bozduğunu anında size bildirir.

Ve son olarak,  **en önemlisi** , bir DevOps hattı oluşturmak için tüm testleri otomatikleştirmeniz gerekir; aksi halde hataları üretime daha hızlı itmiş olursunuz. Birçok şirket bunu anlamıyor. Sürekli entegrasyon ve sürekli teslimatı otomatikleştirmek istiyorlar, ama testleri otomatikleştirmeden. Ne yazık ki, testleri otomatikleştirmeden bir **CI/CD hattına** sahip olamazsınız.

## ✅ Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* TDD’de  **test vakası kod tasarımını yönlendirir** .
* Red/Green/Refactor iş akışı üç adımdan oluşur:
  * Başarısız bir **birim test vakası** yazmak
  * Geçmesi için **yeterli kadar kod** yazmak
  * Kodu **yeniden düzenlemek (refactor)**
* TDD geliştirme zamanından tasarruf sağlar ve kodun beklendiği gibi çalıştığını garanti eder.
