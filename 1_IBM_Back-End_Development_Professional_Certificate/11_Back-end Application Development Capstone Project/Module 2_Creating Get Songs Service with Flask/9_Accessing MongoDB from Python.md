# 🗄️ MongoDB’ye Python ile Erişim

MongoDB’ye Python ile Erişim’e hoş geldiniz. Bu videoyu izledikten sonra şunları yapabileceksiniz: *MongoClient’ın* ne olduğunu açıklamak ve Campus Management veritabanımız için Python kullanarak temel CRUD işlemlerini gerçekleştirmek.

 *MongoClient* , MongoDB ile etkileşime girmenize yardımcı olan bir sınıftır. Önce, MongoDB’nin Python için resmi sürücüsü olan `pymongo` içinden  *MongoClient* ’ı içe aktarırız. `'uri'`, MongoDB’nin bulunduğu adresi söyler. Ardından *MongoClient* oluştururuz; bunu kodumuzda yalnızca bir kez yapmamız gerekir.

Sonraki kısım, campus management veritabanını işaret eden nesneyi alır ve son olarak campus management veritabanı nesnesinden `'students'` koleksiyonunu işaret ederiz.

---

## 🧩 MongoClient ile Bağlantı ve Koleksiyona Erişim

Artık `'students'` koleksiyonuna bir referansımız olduğuna göre, bir öğrenci dokümanı oluşturalım. Bunun için, eklemeye çalıştığımız dokümanı girdi olarak alan `'insert_one'` fonksiyonunu çağırırız.

Toplu ekleme işlemini ise `'insert_many'` fonksiyonunu çağırarak yapabiliriz. Bu fonksiyon girdi olarak bunun yerine bir liste alır.

---

## 🔎 Okuma İşlemleri

Şimdi bazı Okuma ( *Read* ) işlemleri yapalım. İlkinde, herhangi bir filtre ölçütü olmadan `'find_one'` çağırırız. Bu, doğal sıradaki ilk dokümanı döndürür; bu sıra, veritabanının disk üzerindeki dokümanlara başvurduğu sıradır.

Ardından bir e-postaya sahip ilk öğrenciyi buluruz. Ölçütlerle eşleşen birden fazla doküman varsa, yalnızca ilki okunacaktır; çünkü `'find_one'` fonksiyonunu kullanıyoruz. Tüm dokümanları almak için `'find'` yaparız.

Şimdi soyadı Doe olan tüm öğrencileri alıyoruz. Ve son olarak, sadece soyadı Doe olan kaç öğrenci olduğunu saymak istersek, `'count'` fonksiyonunu çağırırız. Bu sayım MongoDB üzerinde gerçekleşir ve yalnızca sayı değeri istemciye döndürülür.

---

## 🧭 Cursor ve Sonuçları Alma

MongoDB’de bir koleksiyon üzerinde `'find'` yaptığımızda, geriye bir *cursor* döner. Bu  *cursor* , MongoDB’deki dokümanlarımızı işaret eder.

Bunu mongo shell kullanarak çalıştırdıysanız, shell bu dokümanları perde arkasında sizin için alır. Cursor’ımızdan dokümanları almak için python `'dumps'` çağırırız; bu, cursor’ımızı tüketerek tüm dokümanları alır.

---

## 🧱 Dokümanı Değiştirerek Güncelleme

Bir öğrenciyi alıp dokümanda bazı değişiklikler yapalım. Öğrencilerin kampüste mi yoksa sadece çevrimiçi mi olduklarını belirlemek için yeni bir alan oluşturuyoruz. Ayrıca e-postayı kampüs e-posta adresiyle güncelleyeceğiz.

Tüm değişiklikler yapıldıktan sonra `'replace'` fonksiyonunu çağırırız. Bu fonksiyonun ilk argümanı, soyadı Doe olan bir dokümanı bulmak için filtre ölçütüdür; ikinci argüman ise güncellenmiş Python nesnesidir.

Replace örneğinde, yeni değişikliklerle birlikte tüm dokümanı geri gönderiyorduk. Daha büyük dokümanlar için bu, istemci ile veritabanı arasında çok fazla aktarım süresi alır.

---

## 🛠️ Yerinde Güncelleme

Küçük değişiklikler için MongoDB’nin yerinde ( *in-place* ) güncellemelerini kullanabiliriz. Bunu, bizim durumumuzda yalnızca iki atama içeren bir değişiklik dokümanı oluşturarak yaparız; bunlar `'$set'` altında yer alır.

Bu yerinde güncelleme ile öğrenci dokümanını almamız bile gerekmez. Kilitlenme ( *lockdown* ) nedeniyle tüm öğrencileri sadece çevrimiçi olacak şekilde güncellemek için, herhangi bir filtre ölçütü olmadan `'update_many'` fonksiyonunu çalıştırıp tüm dokümanları değiştirebiliriz.

---

## 🗑️ Silme İşlemleri

Tıpkı update ve find gibi, `'delete_one'` ve `'delete_many'` fonksiyonları da ilk argüman olarak filtre ölçütü alır. Bu fonksiyonlar, verilen koleksiyonda ölçütlerle eşleşen bir veya birçok dokümanı silecektir.

---

## ✅ Video Özeti

Bu videoda şunları öğrendiniz:

* *MongoClient* ’ın MongoDB ile etkileşime girmenize yardımcı olan bir sınıf olduğunu.
* *MongoClient* ’ın, MongoDB’nin Python için resmi sürücüsü olan `pymongo` içinden içe aktarıldığını.
* Tekil veya toplu eklemeler yapabileceğinizi.
* Tüm dokümanları değiştirebileceğinizi ( *replace whole documents* ).
* Yerinde güncelleme yapabileceğinizi; bunun tercih edilen seçenek olduğunu.
* Koleksiyonunuzdan bir veya daha fazla dokümanı silebileceğinizi.
