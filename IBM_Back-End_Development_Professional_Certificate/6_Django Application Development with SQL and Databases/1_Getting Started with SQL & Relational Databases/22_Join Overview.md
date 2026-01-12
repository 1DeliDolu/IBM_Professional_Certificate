# 🔗 Join Genel Bakış

Merhaba, Join Genel Bakış’a hoş geldiniz. Bu videoyu izledikten sonra şunları yapabileceksiniz:

## 🎯 Öğrenme Hedefleri

* `JOIN` operatörünü tanımlamak
* Bir join işleminde *primary key* ve  *foreign key* ’lerin rolünü açıklamak
* Farklı join operatörü türlerini listelemek

---

## 📊 Basit `SELECT` İfadesinden Çok Tablolu Sorgulara

Basit bir `SELECT` ifadesi, tek bir tablodan bir veya daha fazla sütundan veri getirir.

Bir sonraki karmaşıklık düzeyi, verilerin iki veya daha fazla tablodan getirilmesidir. Bu da, sonuç kümesinin nasıl üretileceği konusunda birden çok olasılığa yol açar.

İki tablodan veri birleştirmek için `JOIN` operatörünü kullanırsınız. Bir `JOIN`, bu tablolardaki belirli sütunlar arasındaki bir ilişkiye dayanarak iki veya daha fazla tablodan satırları birleştirir.

Bu sadeleştirilmiş kütüphane veritabanı örneğinde, *author* ve *book* birer  *entity* ’dir (varlıktır).

---

## 🧱 Varlık-İlişki Diyagramı ve İlişkili Tablolar

Bu *entity relationship* diyagramı, *author* ve *book* varlıkları için, ayrıca  *borrower* ,  *loan* , *copy* ve *author list* gibi diğer varlıklar için ilişkisel veri modelini temsil eder.

Bilgiler, farklı tablolara bölünmüştür.

Eğer hangi  *borrower* ’ın ödünçte hangi kitap kopyasına ( *copy* ) sahip olduğunu bilmek isteseydiniz, üç tablodan veri toplamanız gerekirdi:  *borrower* , *loan* ve *copy* tabloları.

İşte tam bu noktada `JOIN` operatörünü kullanmanız gerekir.

Önce bu tablolar arasındaki ilişkiyi belirlemeniz gerekir. Yani, tablolar arasında bağlantı olarak kullanılacak sütunu veya sütunları bulmalısınız.

Bu *entity relationship* diyagramında,  *author ID* ,  *book ID* , *borrower ID* ve *copy ID* sütunlarının üzerinde *primary key* ikonunun bulunduğuna dikkat edin.

---

## 🔑 Primary Key ve Foreign Key Kavramları

Bir  *primary key* , bir tablodaki her satırı benzersiz şekilde tanımlar.

Ekranın alt yarısındaki varlıklarda, bazı özniteliklerin yanında parantez içinde `FK` bulunduğuna da dikkat edin. Bu, başka bir varlığın  *primary key* ’ine referans veren sütunlar kümesi olan bir  *foreign key* ’i gösterir.

Örneğin, *loan* varlığında, yanında `FK` olan *borrower ID* özniteliği vardır. Bu örnekte, *borrower ID* özniteliği, *loan* varlığındaki  *foreign key* ’dir ve *borrower* varlığının  *primary key* ’ine referans verir.

Dolayısıyla, hangi  *borrower* ’ın ödünçte bir kitabı olduğunu bilmek isterseniz, *borrower* ve *loan* tablolarından veri toplamanız gerekir. Her iki tablodan da  *borrower ID* ’ye ihtiyaç duyarsınız.

---

## 🔗 İki Tablodan Daha Fazla Tabloyu Join Etmek

Şimdiye kadar iki tabloyu birleştirme örneğini gördünüz. Peki, üç veya daha fazla farklı tablodan veri birleştirmeniz gerekse ne olur?

Yeni tabloları join’lere eklemeniz yeterlidir.

Örneğin, hangi  *borrower* ’ların ödünçte kitabı olduğunu ve kitabın hangi kopyasının onlarda olduğunu bilmek isterseniz:

* Önce, *borrower* tablosundaki bilgiler ile *loan* tablosundaki bilgileri,  *borrower ID* ’leri eşleştirerek join edersiniz.
* Sonra, *loan* tablosundaki bilgiler ile *copy* tablosundaki bilgileri,  *copy ID* ’leri eşleştirerek join edersiniz.

SQL, size birkaç farklı `JOIN` türü sunar. İlgili iki tablonun kesişimine karşılık gelen bir veri kümesini çıkarabilirsiniz ya da daha büyük bir veri kümesi seçebilirsiniz.

---

## ⚙️ Farklı `JOIN` Türleri

Bu iki tablodaki tüm verilerin kombinasyonunu seçme noktasına kadar gidebilirsiniz.

En yaygın join türü bir  *inner join* ’dir. `INNER JOIN`, ortak bir sütunda eşleşen değerleri olan iki tablodan yalnızca bu eşleşen satırları gösterir. Bu ortak sütun genellikle bir tablonun  *primary key* ’idir ve ikinci tabloda *foreign key* olarak bulunur.

Bunun yanında  *outer join* ’ler de vardır. `OUTER JOIN`, eşleşen satırları ve hatta iki tablodan eşleşmeyen satırları bile döndürebilir.

Sonuç kümenizi daha da hassaslaştırmak için kullanabileceğiniz pek çok *outer join* çeşidi vardır.

---

## ✅ Özet

Bu videoda şunları öğrendiniz:

* Satırları iki veya daha fazla tablodan birleştirmek için `JOIN` operatörünü kullanabilirsiniz.
* Join edilen tablolar, genellikle bir tablonun  *primary key* ’i ve diğer tabloda *foreign key* olarak görünen ortak bir sütun ile ilişkilidir.
* İki tür join vardır: *inner join* ve  *outer join* .
