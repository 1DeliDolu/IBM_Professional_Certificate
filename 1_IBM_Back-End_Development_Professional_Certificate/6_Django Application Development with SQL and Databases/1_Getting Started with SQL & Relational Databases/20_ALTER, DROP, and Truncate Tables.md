# 🧱 ALTER, DROP ve TRUNCATE Tabloları

## 🎬 Giriş

Merhaba ve *ALTER, DROP ve TRUNCATE tabloları* konusuna hoş geldiniz.

Bu videoyu izledikten sonra şunları yapabileceksiniz:

`ALTER TABLE`, `DROP TABLE` ve `TRUNCATE` deyimlerini açıklamak, sözdizimlerini açıklamak ve bu deyimleri sorgularda kullanmak.

## ⚙️ ALTER TABLE Deyiminin Kullanım Alanları

`ALTER TABLE` deyimini, bir tablodan sütun eklemek veya kaldırmak, sütunların veri tiplerini değiştirmek, anahtar ekleyip kaldırmak ve kısıtlamalar ekleyip kaldırmak için kullanırsınız.

`ALTER TABLE` deyiminin sözdizimi burada gösterilmektedir. Değiştirmek istediğiniz tablonun adını takip eden `ALTER TABLE` ifadesiyle başlarsınız.

`CREATE TABLE` deyiminden farklı olarak, `ALTER TABLE` deyiminde parametreleri parantez içinde belirtmezsiniz.

## 🧩 ALTER TABLE Deyiminde Satırlar ve Değişiklikler

`ALTER TABLE` deyimindeki her satır, tabloda yapmak istediğiniz tek bir değişikliği belirtir.

Örneğin, yazarın telefon numarasını saklamak için, Library veritabanındaki `AUTHOR` tablosuna bir telefon numarası sütunu eklemek üzere aşağıdaki deyimi kullanırsınız:

```sql
ALTER TABLE author ADD COLUMN telephone_number BIGINT;
```

Bu örnekte sütunun veri tipi `BIGINT`’tir ve 19 basamağa kadar bir sayı tutabilir.

## 🔧 Sütun Veri Tipini Değiştirmek (ALTER COLUMN)

Bir sütunun veri tipini değiştirmek için de `ALTER TABLE` deyimini kullanırsınız. Bunu yapmak için, sütun için yeni veri tipini belirten `ALTER COLUMN` ifadesini kullanırsınız.

Örneğin, telefon numarası için sayısal bir veri tipi kullanmak, numaranın bir parçası olarak parantez, artı işareti veya tire kullanamayacağınız anlamına gelir. Bunu aşmak için sütunu `CHAR` veri tipini kullanacak şekilde değiştirebilirsiniz.

Aşağıdaki kod, `author` tablosunu nasıl değiştireceğinizi gösterir:

```sql
ALTER TABLE author ALTER COLUMN telephone_number SET DATA TYPE CHAR(20);
```

Ancak, mevcut veriyi içeren bir sütunun veri tipini değiştirmek, eğer mevcut veriler yeni veri tipiyle uyumlu değilse sorunlara yol açabilir.

## ⚠️ Veri Tipi Uyumsuzluğu ve Hata Durumları

Örneğin, bir sütunu `CHAR` veri tipinden sayısal bir veri tipine dönüştürmek, sütun zaten sayısal olmayan veriler içeriyorsa çalışmayacaktır.

Bunu yapmaya çalışırsanız, bildirim günlüğünde bir hata mesajı görürsünüz ve deyim çalıştırılmaz.

## ➖ Sütun Silmek: DROP COLUMN

Eğer spesifikasyonunuz değişir ve artık bu ekstra sütuna ihtiyacınız kalmazsa, bu kez `DROP COLUMN` ifadesiyle `ALTER TABLE` deyimini tekrar kullanarak sütunu kaldırabilirsiniz. Aşağıda gösterildiği gibi:

```sql
ALTER TABLE author DROP COLUMN telephone_number;
```

## 🗃️ DROP TABLE ile Tablo Silmek

Bir tablodan bir sütunu silmek için `DROP COLUMN` kullanmaya benzer şekilde, bir tabloyu veritabanından silmek için `DROP TABLE` deyimini kullanırsınız.

Eğer veri içeren bir tabloyu silerseniz, varsayılan olarak tablodaki veriler de tabloyla birlikte silinir.

`DROP TABLE` deyiminin sözdizimi şöyledir:

```sql
DROP TABLE table_name;
```

Dolayısıyla, `author` tablosunu veritabanından kaldırmak için şu deyimi kullanırsınız:

```sql
DROP TABLE author;
```

## 🧹 Tabloyu Boşaltmak: TRUNCATE TABLE

Bazen tablonun kendisini silmek yerine sadece tablodaki verileri silmek isteyebilirsiniz. Bunu yapmak için `WHERE` koşulu olmadan `DELETE` deyimini kullanabilirsiniz, ancak genellikle tabloyu kesmek ( *truncate* ) daha hızlı ve verimli olacaktır.

Bir tablodaki tüm satırları silmek için `TRUNCATE TABLE` deyimini kullanırsınız. Deyimin sözdizimi şöyledir:

```sql
TRUNCATE TABLE table_name IMMEDIATE;
```

Buradaki `IMMEDIATE`, deyimin derhal işlenmesini ve geri alınamamasını belirtir.

Dolayısıyla, `author` tablosunu kesmek için şu deyimi kullanırsınız:

```sql
TRUNCATE TABLE author IMMEDIATE;
```

## ✅ Özet

Bu videoda şunları öğrendiniz:

* `ALTER TABLE` deyimi, örneğin sütun eklemek, değiştirmek veya silmek için, mevcut bir tablonun yapısını değiştirir.
* `DROP TABLE` deyimi, mevcut bir tabloyu siler.
* `TRUNCATE TABLE` deyimi, bir tablodaki tüm veri satırlarını siler.
