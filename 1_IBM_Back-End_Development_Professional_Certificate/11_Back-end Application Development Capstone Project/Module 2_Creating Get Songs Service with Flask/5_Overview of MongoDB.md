# 🍃 MongoDB’ye Genel Bakış

“MongoDB’ye Genel Bakış”a hoş geldiniz. Bu videoyu izledikten sonra şunları yapabileceksiniz: MongoDB’nin ne olduğunu açıklamak, MongoDB’nin farklı bileşenlerini listelemek ve MongoDB’yi neden ve nerede kullanacağınızı tanımlamak.

MongoDB, doküman tabanlı ve bir NoSQL veritabanıdır. SQL veritabanları gibi verileri satır ve sütunlardan oluşan tablolar halinde saklamak yerine, MongoDB veritabanındaki her kayıt bir dokümandır ve veriyi ilişkisel olmayan ( *non-relational* ) bir şekilde saklarsınız.

Dokümanlar, JSON nesneleri veya Python sözlükleri gibi ilişkisel ( *associative* ) dizilerdir. Örneğin, bir öğrencinin adını, soyadını, e-posta adresini ve kimliğini temsil eden bir öğrenci dokümanı.

Benzer türde MongoDB dokümanları bir *collection* içinde gruplanır. Kampüs yönetim sistemimiz tüm öğrenci kayıtlarını veya dokümanlarını `Students` koleksiyonunda saklar.

Benzer şekilde, tüm personel dokümanları `Employees` koleksiyonunda saklanır.

---

## 🗄️ Veritabanı Nedir?

Önceki örneğimizi takip edersek, kampüs yönetim sistemi kendisiyle ilgili farklı türdeki tüm verileri `Campus Management DB` adlı bir MongoDB veritabanında saklar.

---

## 🧾 Dokümanı Parçalara Ayıralım

Aşağıdaki dokümanda `firstName`, `lastName`, `email` ve `studentId`, John Doe adlı bir öğrenciyi temsil eden değerleriyle birlikte alanlar ( *fields* ) veya özellikler ( *properties* )’tir ve her alan adı o doküman içinde benzersizdir.

MongoDB çeşitli veri türlerini destekler; bu sayede bilginizi saklamak için doğru veri türünü kullanma konusunda tam yeteneğe sahip olursunuz. Örneğin, tarihler **ISODate** veya Unix tarzı **epoch** tarihler olarak saklanmalıdır; bu da “15 Ocak ile 15 Şubat arasında doğan tüm öğrencileri bana ver” gibi sorgularda size yardımcı olur.

Sayılar tam sayı ( *whole numbers* ) veya ondalık ( *decimals* ) olarak saklanabilir.

Doküman veritabanı olması nedeniyle MongoDB, ikincil bilgileri birlikte gruplamak için alt-dokümanları ( *sub-documents* ) saklamanıza da olanak tanır. Ayrıca değer listelerini de destekler. Sadece metin değil, hatta farklı türlerin karışık biçimde birlikte bulunmasını da destekler.

---

## 🛠️ MongoDB ile Çalışmanın Kolaylığı

MongoDB ile çalışmak kolaydır çünkü yazdığınız veriye ve onu nasıl okuyacağınıza odaklanabilirsiniz. Geleneksel ilişkisel veritabanları, önce şemayı oluşturmanızı, ardından verinizi tutacak tablo yapılarını yaratmanızı gerektirirdi. Dolayısıyla ek bir alan saklamaya karar verirseniz, tablolarınızı değiştirmeniz ( *alter* ) gerekir.

MongoDB’de ise, ilerledikçe değiştirirsiniz.

MongoDB ayrıca hem yapılandırılmış ( *structured* ) hem de yapılandırılmamış ( *unstructured* ) veriyi içeri almanız için size güç verir.

MongoDB, verilerinizin birden fazla kopyasını tutarak yüksek erişilebilirlik ( *high availability* ) de sağlar; bunu sonraki konularda ele alacağız.

MongoDB’de, nasıl saklandığı ve nasıl bağlanması gerektiğinin karmaşıklığı hakkında endişelenmeden karmaşık veri yapılarını kolayca tasarlayabilirsiniz. Örneğin, Kampüs Yönetimi uygulamanız ABD’de de yayına alınır; orada posta kodu ( *postcode* ) yerine *zip code* kullanılır.

---

## 📈 Ölçeklenebilirlik

MongoDB’nin sağladığı ölçeklenebilirlik, veri ihtiyaçlarınız büyüdükçe kolayca ölçekleme yapabileceğiniz anlamına gelir:

* Dikey ölçekleme ( *vertically* ): Daha büyük, daha hızlı, daha iyi donanım ekleyerek
* Yatay ölçekleme ( *horizontally* ): Verinizi bölümlere ayırarak ( *partitioning* )

Bunların tümü; ister kendi yönettiğiniz şirket içi ( *self-managed on-premises* ) MongoDB üzerinde çalıştırıyor olun, ister hibrit ya da bulutta barındırılan ve tam yönetilen servisler olan **IBM Cloud Databases for MongoDB** veya **AWS, Azure ve Google Cloud üzerindeki MongoDB Atlas** gibi çözümleri kullanıyor olun, gerçekleştirilebilir.

---

## 📝 Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* MongoDB’nin doküman tabanlı ve bir NoSQL veritabanı olduğu
* MongoDB’nin çeşitli veri türlerini desteklediği
* Dokümanların veriyi saklamak için esnek bir yol sunduğu
* Benzer türde MongoDB dokümanlarının *collections* içinde gruplandığı
* MongoDB’nin veriyi okuma/yazma şeklinize göre modellediği, yapılandırılmış veya yapılandırılmamış veriyi içeri alabildiği ve yüksek erişilebilirlik sağladığı
* MongoDB’nin, yapılandırılmış veya yapılandırılmamış veriyi esnek şekilde saklayabilmesi nedeniyle çeşitli amaçlarla kullanılabildiği
