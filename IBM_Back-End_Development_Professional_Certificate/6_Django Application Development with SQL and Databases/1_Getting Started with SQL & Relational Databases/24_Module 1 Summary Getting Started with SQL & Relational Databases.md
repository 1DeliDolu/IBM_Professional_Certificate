# 📚 Bölüm 1 Özeti: SQL ve İlişkisel Veritabanlarına Giriş

Tebrikler! Bu modülü tamamladınız.

Kursun bu noktasında aşağıdakileri biliyorsunuz:

---

## 💻 SQL ve Yapılandırılmış Veri

* *Structured Query Language* yani  **SQL** , ilişkisel veritabanlarındaki verileri yönetmek için tasarlanmıştır ve yapılandırılmış verilerle çalışmak için kullanışlıdır.
* **Veri** , kelimeler, sayılar ve resimler hâlindeki olguların bir koleksiyonudur.

---

## 🗄️ Veritabanı Nedir?

* Bir  **veritabanı** , verilerin eklendiği, değiştirildiği ve sorgulandığı işlevleri sağlayan bir veri deposudur.
* **İlişkisel veritabanları** , sütunların öğelerin özelliklerini içerdiği, birbiriyle ilişkili öğe koleksiyonları olarak tablolar hâlinde verileri saklar.

---

## 🧱 Temel SQL İfadeleri ve Veritabanı Türleri

* Temel SQL ifadeleri: `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE` ve `DELETE`’tir.
* **İlişkisel olmayan (non-relational) veritabanları** , verileri saklama ve geri getirme konusunda esnek ve ölçeklenebilir bir yaklaşım sunar.
* İlişkisel veritabanları, büyük hacimli verilerin optimize edilmiş biçimde saklanması, geri getirilmesi ve işlenmesi için idealdir.

---

## ⚙️ RDBMS ve Özellikleri

* **RDBMS** , esneklik, azaltılmış fazlalık (redundancy), yedekleme ve felaket kurtarma kolaylığı ve **ACID uyumluluğu** sağlayan, olgun ve iyi belgelenmiş bir teknolojidir.

---

## 🧩 Varlık-İlişki (ER) Modeli

* Bir  **Varlık-İlişki (Entity-Relationship) modeli** , ilişkisel veritabanlarını tasarlamak için kullanılan bir araçtır.
* **Varlıklar (entities)** tablolara dönüşür ve **öznitelikler (attributes)** sütunlara çevrilir.

---

## 🛠️ DDL Komutları ve `CREATE TABLE` İfadesi

* `CREATE`, `ALTER`, `TRUNCATE` ve `DROP`, tablolar gibi veritabanı nesnelerini tanımlayan, değiştiren veya silen ifadelerdir.
* `CREATE TABLE` ifadesi, tablodaki sütunların özniteliklerinin tanımını içerir; bunlara şunlar dahildir:
  * Sütun adları
  * Sütunların veri tipleri
  * Gerekliyse **Primary Key (Birincil Anahtar)** kısıtı gibi isteğe bağlı değerler

---

## 📊 Sonuç Kümelerini Sıralama: `ORDER BY`

* `ORDER BY` ifadesi, bir SQL sorgusunda sonuç kümesini belirtilen bir sütuna göre sıralamak için kullanılır.

  Örneğin, `"ORDER BY title"` ifadesi, sonuç kümesini **`title`** adlı sütuna göre sıralar.
* Sıralanacak sütunu, sütun sıra numarasını belirterek de ifade edebilirsiniz.

  Örneğin:

  ```sql
  select title, pages from book ORDER BY 2
  ```

  ifadesi, sıralama düzeninin ikinci sütundaki değerlere göre belirlendiğini gösterir.

---

## 🔗 `JOIN` Operatörü ve Anahtarlar

* `JOIN` operatörü, iki veya daha fazla tablodaki satırları, bu tablolardaki belirli sütunlar arasındaki ilişkiye göre birleştirir.
* Birleştirilen tablolar, genellikle bir tablonun **primary key (birincil anahtar)** sütunu olup diğer tabloda **foreign key (yabancı anahtar)** olarak görünen ortak bir sütunla ilişkilidir.
* Bir ilişkisel tablonun  **Primary Key (Birincil Anahtarı)** , tablodaki her satırı benzersiz şekilde tanımlar.
* Bir  **Foreign Key (Yabancı Anahtar)** , başka bir varlığın birincil anahtarına referans veren sütunlar kümesidir.

---

## 🧬 Birden Fazla Tabloyu Birleştirmek

* Üç veya daha fazla farklı tablodan veri birleştirmeniz gerektiğinde, `JOIN` ifadesine yeni tablolar eklersiniz.
* Önce, tablo **A** ve tablo **B** bilgilerini, paylaştıkları öznitelikleri eşleştirerek birleştirirsiniz.

  Ardından, tablo **B** ve tablo **C** bilgilerinin, yine paylaşılan öznitelikleri eşleştirerek join işlemini gerçekleştirirsiniz.

---

## 🔄 Farklı `JOIN` Türleri

* SQL, `INNER JOIN` ve `OUTER JOIN` gibi çeşitli `JOIN` türleri sunar.
* İki tabloyun kesişimine karşılık gelen bir veri kümesini çıkarabilir veya daha büyük bir veri kümesini seçebilirsiniz.
