# 🧩 CRUD İşlemleri

CRUD İşlemlerine hoş geldiniz. Bu videoyu izledikten sonra şunları yapabileceksiniz: *Mongo shell* kullanarak MongoDB veritabanınıza bağlanmak ve temel CRUD işlemlerini gerçekleştirmek.

 *Mongo shell* , MongoDB tarafından veritabanlarınızla etkileşim kurmak için sağlanan bir komut satırı aracıdır. Etkileşimli bir JavaScript arayüzüdür ve MongoDB üzerinde veri ve yönetim işlemleri gerçekleştirmek için kullanılabilir.

Öncelikle bir bağlantı dizesi sağlayarak kümenize bağlanırız. Bağlandıktan sonra tüm veritabanlarımızın listesini görüntüleyebiliriz. Basitlik açısından, kabuğun (shell) zaten MongoDB örneğimize bağlı olduğunu varsayacağız.

---

## 🔌 Veritabanına Bağlanma ve Koleksiyonları Görüntüleme

Kampüs yönetimi veritabanında çalışmaya başlamak için aşağıdaki ifadeyi çalıştırırız:

```cli
use campusManagementDB
```

Ardından kampüs yönetimi veritabanında hangi koleksiyonların bulunduğunu şu komutla görebiliriz:

```cli
show collections
```

İki koleksiyon gösterir: **Staff** ve  **Students** .

---

## 🧱 CRUD Nedir?

CRUD işlemleri  **Create** ,  **Read** , **Update** ve **Delete** işlemleridir; bu nedenle kısaltması  **CRUD** ’dur.

---

## 🟢 Create İşlemi

Bir **Create** işlemiyle başlayalım.

**Students** koleksiyonuna yeni bir doküman ekleyeceğiz. Şu biçimdedir: `db.`, yani *campusManagementDB* veritabanı. Sonra koleksiyon adı, yani `students.` Ve ardından `insertOne` fonksiyonu gelir; bu fonksiyon, **Students** koleksiyonunda oluşturmak istediğimiz dokümanı argüman olarak alır.

İşlemin sonucu, işlemin başarılı olduğunu belirten bir onaydır. Ve bu bir ekleme işlemi olduğu için `insertedId` gösterir.

`_id` ( *“underscore id”* olarak telaffuz edilir) MongoDB’de her dokümanda zorunlu bir alandır. John Doe’nun dokümanında kendimiz sağlamadığımız için, Mongo shell sürücüsü `_id` alanını ekler ve bizim için `ObjectId` üretir.

*Mongo shell* bir JavaScript yorumlayıcısıdır; yani içinde değişkenler tanımlayabilir ve başka fonksiyonlar da gerçekleştirebilirsiniz.

Burada `students_list` içinde iki doküman olacak şekilde oluşturulur ve bunu `insertMany` fonksiyonuna argüman olarak geçebiliriz.

---

## 🔎 Read İşlemleri

Şimdi bazı **Read** işlemleri yapalım.

İlkinde, herhangi bir filtre kriteri olmadan `findOne` fonksiyonunu çağırırız. Bu, doğal sıradaki ilk dokümanı döndürür; bu sıra, veritabanının disk üzerindeki dokümanlara başvurma sırasıdır.

İkinci **Read** işleminde, belirli bir e-posta adresine sahip ilk öğrenciyi bulmak istiyoruz. Kriteri birden fazla doküman karşılıyorsa bile, `findOne` fonksiyonunu kullandığımız için yalnızca ilki okunur.

Sonra soyadı `Doe` olan tüm öğrencileri almak istiyoruz. Ve son olarak, yalnızca `Doe` soyadına sahip kaç öğrenci olduğunu saymak istiyorsak `count` fonksiyonunu çağırırız.

Bu sayma işlemi MongoDB üzerinde gerçekleşir ve yalnızca sayı değeri döndürülür.

---

## ♻️ Replace İşlemi

Şimdi bir **Replace** işlemi gerçekleştireceğiz.

Bir öğrenci kaydını alıp dokümanda bazı değişiklikler yapalım. Hangi öğrencilerin kampüste olduğunu veya yalnızca çevrimiçi olduğunu belirlemek için yeni bir alan oluşturuyoruz. Ayrıca e-postayı kampüsün e-postasıyla güncelliyoruz.

Tüm değişiklikler yapıldıktan sonra `replaceOne` fonksiyonunu çağırırız. Bu fonksiyonun ilk argümanı, soyadı Doe olan bir dokümanı bulmak için filtre kriteridir. İkinci argüman güncellenmiş öğrenci nesnesidir.

Bu ifadenin çıktıları şunlardır: Bir onay, filtre kriterimizle eşleşen kaç doküman olduğu bilgisi ve gerçekte kaçının değiştirildiğinin sayısı.

Replace örneğinde, yeni değişikliklerle birlikte tüm dokümanı geri gönderiyorduk. Daha büyük dokümanlarda bu, istemci ile veritabanı arasında çok fazla aktarım süresi gerektirir. Bunun yerine, küçük değişiklikler için MongoDB’nin yerinde (in-place) güncellemelerini kullanabiliriz.

Bunu, yalnızca iki atama içeren bir `changes` dokümanı oluşturarak yaparız; bizim durumumuzda bunlar `$set` altında yer alır. Ardından `updateOne` fonksiyonunu çağırırız.

Kilitlenme (lockdown) nedeniyle tüm öğrencileri yalnızca çevrimiçi olacak şekilde güncellemek için, herhangi bir filtre kriteri olmadan `updateMany` fonksiyonunu ve bir değişiklik dokümanını çalıştırabiliriz.

---

## 🗑️ Delete İşlemi

Bir silme işlemi çalıştırmak için, güncelleme ve bulma işlemlerinde olduğu gibi, `deleteOne` fonksiyonu ilk argüman olarak filtre kriteri alır.

Bu silme ifadesini çalıştırmak size bir onay ve kaç dokümanın silindiğini temsil eden bir sayı verir.

Benzer şekilde, kriteri karşılayan birden fazla dokümanı silmek için `deleteMany` fonksiyonunu kullanabilirsiniz.

---

## ✅ Video Özeti

Bu videoda şunları öğrendiniz:

* *Mongo shell* ’in, MongoDB tarafından veritabanlarınızla etkileşim kurmak için sağlanan etkileşimli bir komut satırı aracı olduğunu.
* *Mongo shell* kullanmak için önce bir bağlantı dizesiyle kümenize bağlanmanız gerektiğini.
* Veritabanlarını listelemek için `show dbs`, bir veritabanı seçmek için `use databasename`, ve bir veritabanındaki koleksiyonları listelemek için `show collections` kullandığınızı.
* CRUD işlemlerinin  **Create** ,  **Read** , **Update** ve  **Delete** ’ten oluştuğunu.
* Kullanışlı fonksiyonların `insertOne`, `insertMany`, `findOne`, `find`, `count`, `replace`, `updateOne`, `updateMany`, `deleteOne` ve `deleteMany` olduğunu.
* Çalıştırılan işleme bağlı olarak farklı türde onayların (acknowledgement) döndürüldüğünü.
