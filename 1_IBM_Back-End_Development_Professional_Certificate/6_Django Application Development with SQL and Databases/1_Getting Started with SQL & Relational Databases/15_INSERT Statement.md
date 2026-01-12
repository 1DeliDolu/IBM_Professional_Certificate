# 📥 INSERT Statement

## 👋 Giriş

Merhaba ve  *Insert Statement* 'a hoş geldiniz.

Bu videoda, ilişkisel bir veritabanı tablosunun nasıl doldurulacağını öğreneceğiz.

Bu videonun sonunda, *Insert Statement* sözdizimini ( *syntax* ) tanımlayabilecek ve bir tabloya satır eklemenin iki yöntemini açıklayabileceksiniz.

---

## 🗃️ Tablonun Veri ile Doldurulması

Bir tablo oluşturulduktan sonra, tablonun verilerle doldurulması gerekir.

Bir tabloya veri eklemek için *Insert Statement* kullanılır.

 *Insert Statement* , bir tabloya yeni satırlar eklemek için kullanılır.

 *Insert Statement* ,  *Data Manipulation Language Statements* ’tan biridir.

*Data Manipulation Language Statements* veya kısaca  *DML Statements* , veriyi okumak ve değiştirmek için kullanılır.

---

## 📚 Author Varlığı ( *Entity* ) Üzerinden Örnek

*Author* varlık ( *entity* ) örneğine dayanarak, tabloyu varlık adı olan *Author* kullanarak ve varlığın özniteliklerini tablonun sütunları olacak şekilde oluşturmuştuk.

Şimdi, *Author* tablosuna satırlar ekleyerek bu tabloya veri ekleyeceğiz.

*Author* tablosuna veri eklemek için *Insert Statement* kullanırız.

---

## 🧩 INSERT Statement Sözdizimi

 *Insert Statement* ’ın sözdizimi şu şekildedir:

```sql
Insert into TableName, ColumnName, Values
```

Bu ifadede:

* `TableName`, tabloyu tanımlar.
* `ColumnName` listesi, tablodaki her sütunu tanımlar.
* `Values` ifadesi ( *clause* ), tablodaki sütunlara eklenecek veri değerlerini belirtir.

---

## 🧑‍💻 Raul Chong Satırının Eklenmesi

Raul Chong için verilerin bulunduğu bir satır eklemek için, şu bilgileri içeren bir satır ekleriz:

* `Author` alt çizgi `ID` değeri: **A1**
* Soyadı: **Chong**
* Adı: **Raul**
* E-posta: **rfc at ibm.com**
* Şehir: **Toronto**
* Ülke: **CA** (*Canada* için)

*Author* tablosunda altı sütun vardır, bu nedenle  *Insert Statement* , virgülle ayrılmış altı sütun adını listeler ve ardından yine virgülle ayrılmış olarak her sütun için bir değer belirtir.

*Values* ifadesinde sağlanan değer sayısının, *ColumnName* listesinde belirtilen sütun adlarının sayısına eşit olması önemlidir.

Bu, her sütunun bir değere sahip olmasını sağlar.

---

## ➕ Birden Fazla Satır Eklemek

Bazı veritabanları, *Values* ifadesinde satırları virgülle ayırarak tek bir `Insert Into` ifadesiyle birden fazla satır eklemeye izin verir.

Örneğin, *Insert Statement* içinde, biri Raul Chong için, diğeri Rav Ahuja için olmak üzere iki satır ekliyor olabiliriz.

Ancak SQLite bu özelliği desteklemez, bu nedenle satır ekleme işlemi tek tek yapılmalıdır.

---

## ✅ Özet ve Kapanış

Artık *Insert Statement* sözdizimini tanımlayabiliyor ve bir tabloya satır eklemenin iki yöntemini açıklayabiliyorsunuz:

* Satırları **birer birer** eklemek
* Satırları **çoklu** şekilde eklemek

Bu videoyu izlediğiniz için teşekkürler.
