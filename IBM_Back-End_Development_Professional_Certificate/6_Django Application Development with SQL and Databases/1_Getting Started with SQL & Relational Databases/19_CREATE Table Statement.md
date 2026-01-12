# 🧱 CREATE TABLE İfadesi

Bu videoda, ilişkisel bir veritabanı tablosu oluşturmayı öğreneceğiz.

`CREATE` ifadesinin `CREATE TABLE` söz dizimi burada gösterilmektedir:

Tablo oluştururken, **“`CREATE TABLE`”** ifadesiyle başlar ve hemen ardından oluşturmak istediğiniz tablonun adını yazarsınız.

Sonra ifadenin geri kalanını bir çift parantez (yuvarlak parantez) içine alırsınız.

Parantez içindeki her satır, bir sütunun adını, ardından veri türünü ve daha sonra göreceğimiz bazı ek isteğe bağlı değerleri belirtir.

Her bir öznitelik ya da sütun tanımı **virgülle** ayrılır.

Örneğin, Kanada’daki eyaletler için bir tablo oluşturmak istersek şu şekilde belirtirsiniz:

```sql
CREATE TABLE provinces (
    id CHAR(2) PRIMARY KEY NOT NULL,
    name VARCHAR(24)
);
```

Bu örnekte kullanılan veri türleri şunlardır:

* `CHAR`: Sabit uzunlukta bir karakter dizisidir, bu örnekte uzunluk  **2** ’dir.
* `VARCHAR`: Değişken uzunlukta bir karakter dizisidir. Bu örnekte bu değişken karakter alanı en fazla **24** karakter uzunluğunda olabilir.

---

## 🗺️ Kanada Eyaletleri Tablosu

Bu ifadeyi çalıştırmak, veritabanında **2 sütunlu** bir tablo oluşturur.

* Birinci sütun olan `id`,  **AB** , **BC** vb. gibi eyaletlerin kısaltılmış 2 harfli kısa kodlarını saklamak için kullanılır.
* İkinci sütun olan `name` ise  **ALBERTA** , **BRITISH COLUMBIA** vb. gibi eyaletlerin tam adlarını saklamak için kullanılır.

---

## 📚 Kütüphane Veritabanı Örneği

Şimdi, **Library** (kütüphane) veritabanına dayanan daha ayrıntılı bir örneğe bakalım.

Bu veritabanı,  **AUTHOR** ,  **BOOK** , **BORROWER** gibi birkaç varlık (entity) içerir.

Önce **AUTHOR** varlığı için tabloyu oluşturarak başlayalım.

Tablonun adı `AUTHOR` olacak ve `AUTHOR_ID`, `FIRSTNAME`, `LASTNAME` vb. gibi öznitelikleri tablonun sütunları olacaktır.

Bu tabloda ayrıca `Author_ID` özniteliğini **Primary Key** olarak atayacağız; böylece tablodaki değerlerin yinelenmesi engellenir.

Unutmayın, ilişkisel bir tablonun  **Primary Key** ’i, tablodaki her bir  *tuple* ’ı (veya satırı) benzersiz şekilde tanımlar.

---

## ✍️ AUTHOR Tablosunu Oluşturma

Author tablosunu oluşturmak için aşağıdaki komutu çalıştırın:

```sql
CREATE TABLE author (
    author_id CHAR(2) PRIMARY KEY NOT NULL,
    lastname VARCHAR(15) NOT NULL,
    firstname VARCHAR(15) NOT NULL,
    email VARCHAR(40),
    city VARCHAR(15),
    country CHAR(2)
);
```

Burada `Author_ID`’nin **Primary Key** olduğuna dikkat edin.

Bu kısıtlama, tabloda yinelenen değerlerin oluşmasını engeller.

Ayrıca, `lastname` (Last Name) ve `firstname` (First Name) sütunlarının **`NOT NULL`** kısıtına sahip olduğunu da unutmayın.

Bu, bir yazarın mutlaka bir ismi olması gerektiğinden, bu alanların **NULL değer içeremeyeceğini** garanti eder.

---

## 🧾 Özet

Artık şunları biliyorsunuz:

* `CREATE`, veritabanında varlıklar (Entities) veya tablolar oluşturmak için kullanılan bir **DDL** ifadesidir.
* `CREATE TABLE` ifadesi, tablodaki sütunların özniteliklerinin tanımını içerir; buna sütun adları, sütunların veri türleri ve gerekirse **Primary Key** kısıtı gibi diğer **isteğe bağlı değerler** dahildir.

Bu videoyu izlediğiniz için teşekkürler.
