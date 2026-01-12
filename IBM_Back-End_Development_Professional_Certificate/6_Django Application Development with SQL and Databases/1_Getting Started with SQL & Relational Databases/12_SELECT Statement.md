# 📌 SELECT İfadesi

## 👋 Giriş: SELECT ifadesiyle veri alma

Merhaba ve *SELECT* ifadesiyle veri almaya hoş geldiniz.

Bu videoda, bir ilişkisel veritabanı tablosundan, bir tablonun sütunlarını seçerek nasıl veri alacağımızı öğreneceğiz.

Bu dersin sonunda şunları yapabileceksiniz:

* Bir ilişkisel veritabanı tablosundan veri almak
* Bir  *predicate* ’in kullanımını açıklamak
* *WHERE* ekiyle kullanılan *SELECT* ifadesinin sözdizimini ( *syntax* ) tanımlamak
* Bir ilişkisel veritabanı yönetim sistemi tarafından desteklenen karşılaştırma operatörlerini listelemek

Bir veritabanı yönetim sisteminin ( *Database Management System – DBMS* ) temel amacı yalnızca veriyi depolamak değil, aynı zamanda verinin alınmasını da kolaylaştırmaktır.

Bu yüzden, bir ilişkisel veritabanı tablosu oluşturup tabloya veri ekledikten sonra, bu veriyi görmek isteriz. Veriyi görmek için *SELECT* ifadesini kullanırız.

*SELECT* ifadesi, bir *Data Manipulation Language (DML)* ifadesidir.

---

## 🧰 DML ve SELECT: Sorgu ve sonuç kümesi

*Data Manipulation Language* ifadeleri ya da *DML* ifadeleri, veriyi okumak ve değiştirmek için kullanılır.

*SELECT* ifadesi bir sorgu ( *query* ) olarak adlandırılır ve bu sorguyu çalıştırdığımızda elde ettiğimiz çıktı, bir *sonuç kümesi* ( *result set* ) veya *sonuç tablosu* ( *result table* ) olarak adlandırılır.

En basit haliyle bir *SELECT* ifadesi şöyledir:

```sql
SELECT * FROM tablo_adı;
```

Kitap varlığı ( *book entity* ) örneğine dayanarak, tabloyu varlığın adı olan `book` ile ve varlık niteliklerini tablonun sütunları olacak şekilde oluştururduk.

Veri, `book` tablosuna, tabloya satırlar ekleyen `INSERT` ifadesi kullanılarak eklenirdi.

Kitap varlığı örneğinde:

```sql
SELECT * FROM book;
```

ifadesi dört satırlık bir sonuç kümesi verir. `book` tablosundaki tüm sütunlara ait tüm veri satırları görüntülenir.

---

## 🧱 Tüm sütunlar yerine belirli sütunları seçmek

Buna ek olarak, *SELECT* ifadesinde sütun adlarını tek tek belirterek de tüm sütunlar için tüm satırları alabilirsiniz.

Bir tabloda her zaman tüm sütunları almak zorunda değilsiniz. Yalnızca bir sütun alt kümesini ( *subset of columns* ) alabilirsiniz.

İsterseniz, `book` tablosundan yalnızca iki sütunu alabilirsiniz. Örneğin `book_id` ve `title`.

Bu durumda *SELECT* ifadesi şöyledir:

```sql
SELECT book_id, title FROM book;
```

Bu durumda, dört satırın her biri için yalnızca bu iki sütun görüntülenir.

---

## 📐 Sütun sırası, WHERE eki ve predicate

Görüntülenen sütunların sırasının, her zaman *SELECT* ifadesindeki sırayla eşleştiğine de dikkat edin.

Peki, `book_id` değeri `B1` olan kitabın başlığını ( *title* ) bilmek istersek ne olur?

İlişkisel işlem ( *relational operation* ), *WHERE* ekini kullanmamıza izin vererek, sonuç kümesini kısıtlamamıza yardımcı olur.

*WHERE* eki her zaman bir *predicate* gerektirir.

Bir  *predicate* , sonucu  *true* , *false* veya *unknown* olan bir koşuldur ( *condition* ).

 *Predicate* ’ler, *WHERE* ekinin arama koşulunda ( *search condition* ) kullanılır.

Dolayısıyla, `book_id` değeri `B1` olan kitabın başlığını bilmemiz gerekirse, *WHERE* ekini, `book_id` `B1`’e eşittir  *predicate* ’iyle kullanırız.

---

## ⚖️ Karşılaştırma operatörleri ve sonuç kümesini kısıtlama

```sql
SELECT book_id, title FROM book WHERE book_id = 'B1';
```

Sonuç kümesinin artık, koşulu *true* olarak değerlendirilen tek bir satırla sınırlandığına dikkat edin.

Önceki örnekte, *WHERE* ekinde karşılaştırma operatörü olarak “eşittir” ( *equal to* ) kullanıldı.

Bir ilişkisel veritabanı yönetim sistemi tarafından desteklenen başka karşılaştırma operatörleri de vardır:

* Eşittir ( *equal to* )
* Büyüktür ( *greater than* )
* Küçüktür ( *less than* )
* Büyük veya eşittir ( *greater than or equal to* )
* Küçük veya eşittir ( *less than or equal to* )
* Eşit değildir ( *not equal to* )

---

## 🎯 Dersin sonunda neler öğrendiniz?

Artık bir ilişkisel veritabanı tablosundan veri alabilir ve sütun seçimi yapabilirsiniz.

Bir  *predicate* ’in kullanımını tanımlayabilir, *WHERE* ekiyle kullanılan *SELECT* ifadesinin sözdizimini belirleyebilir ve bir ilişkisel veritabanı yönetim sistemi tarafından desteklenen karşılaştırma operatörlerini listeleyebilirsiniz.

Bu videoyu izlediğiniz için teşekkürler.
