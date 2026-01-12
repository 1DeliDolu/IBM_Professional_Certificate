# 📝 UPDATE ve DELETE İfadeleri

Merhaba, *UPDATE* ifadesi ve *DELETE* ifadesi konusuna hoş geldiniz. Bu videoda, ilişkisel bir veritabanı tablosundaki verileri değiştirmeyi ve silmeyi öğreneceğiz.

Bu dersin sonunda, *UPDATE* ve *DELETE* ifadelerinin sözdizimini tanımlayabilecek ve bu ifadelerdeki *WHERE* koşulunun önemini açıklayabileceksiniz.

Bir tablo oluşturulup verilerle doldurulduktan sonra, tablodaki veriler *UPDATE* ifadesiyle değiştirilebilir. *UPDATE* ifadesi, veri işleme dili yani *Data Manipulation Language (DML)* ifadelerinden biridir.

*DML* ifadeleri, verileri okumak ve değiştirmek için kullanılır. Yazar varlığı ( *author entity* ) örneğine dayanarak, tabloyu varlık adı olan  *author* 'ı ve varlık özniteliklerini tablonun sütunları olarak kullanarak oluşturduk.

---

Tabloyu doldurmak için *author* tablosuna satırlar eklendi. Bir süre sonra, tablodaki verileri değiştirmek isteyebilirsiniz.

*author* tablosundaki verileri değiştirmek veya güncellemek için *UPDATE* ifadesini kullanırız. *UPDATE* ifadesinin sözdizimi şu şekildedir:

```sql
UPDATE [TableName] SET [[ColumnName]=[Value]]
```

Bu ifadede, *TableName* değiştirilecek tablonun adını, *ColumnName* ise *WHERE* koşulunda belirtildiği şekilde değeri değiştirilecek sütunu tanımlar.

Bir örneğe bakalım. Bu örnekte, *Author_Id* değeri A2 olan yazarın adını ve soyadını  *Rav Ahuja* 'dan  *Lakshmi Katta* 'ya güncellemek istiyorsunuz.

Bu örnekte, *UPDATE* ifadesinin nasıl çalıştığını görmek için, değerleri görmek amacıyla önce *author* tablosundaki tüm satırları seçerek başlarız.

---

Yazar kimliği A2'ye eşit olan kayıt için adı ve soyadı *Lakshmi Katta* olarak değiştirmek üzere *UPDATE* ifadesini şu şekilde girersiniz:

```sql
UPDATE AUTHOR SET LASTNAME='KATTA' FIRSTNAME='LAKSHMI' WHERE AUTHOR_ID='A2'
```

Şimdi, güncellemenin sonucunu görmek için *author* tablosundaki tüm satırları tekrar seçin ve ikinci satırdaki ismin  *Rav Ahuja* 'dan  *Lakshmi Katta* 'ya değiştiğini göreceksiniz.

*WHERE* koşulunu belirtmezseniz, tablodaki tüm satırların güncelleneceğine dikkat edin. Bu örnekte, *WHERE* koşulu belirtilmemiş olsaydı, tablodaki tüm satırlar için ad ve soyad *Lakshmi Kata* olarak değişmiş olurdu.

Bir süre sonra, bir tablodan bir veya daha fazla satırı kaldırma ihtiyacı doğabilir. Satırlar *DELETE* ifadesiyle kaldırılır.

*DELETE* ifadesi, verileri okumak ve değiştirmek için kullanılan veri işleme dili ( *DML* ) ifadelerinden biridir. *DELETE* ifadesinin sözdizimi şu şekildedir:

```sql
DELETE FROM [TableName] <WHERE [Condition]>
```

Silinecek satırlar *WHERE* koşulunda belirtilir.

---

Yazar varlığı örneğine dayanarak, yazar kimliği A2 ve A3 olan satırları silmek istiyoruz. Bir örneğe bakalım:

```sql
DELETE FROM AUTHOR WHERE AUTHOR_ID ID IN ('A2', 'A3')
```

*WHERE* koşulunu belirtmezseniz, tablodaki tüm satırların silineceğine dikkat edin.

Artık *UPDATE* ve *DELETE* ifadelerinin sözdizimini tanımlayabilir ve bu ifadelerdeki *WHERE* koşulunun önemini açıklayabilirsiniz.

Bu videoyu izlediğiniz için teşekkür ederiz.
