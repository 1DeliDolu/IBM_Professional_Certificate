# 🧾 Modül 1 Ek Ders 3 Özeti

Tebrikler! Bu dersi tamamladınız. Kursun bu noktasında artık şunları biliyorsunuz:

## 📚 Kursta bu noktada şunları biliyorsunuz

* `CREATE`, `ALTER`, `TRUNCATE` ve `DROP`, tablolar gibi veritabanı nesnelerini tanımlar, değiştirir veya siler.
* `CREATE TABLE` deyimi, tablodaki sütunların özniteliklerinin tanımını içerir; bunlar şunlardır:

  * Sütunların adları
  * Sütunların veri tipleri
  * Gerekirse Birincil Anahtar kısıtı gibi isteğe bağlı değerler
* `ORDER BY` ifadesi, bir SQL sorgusunda sonuç kümesini belirtilen bir sütuna göre sıralamak için kullanılır. Örneğin, `ORDER BY title` ifadesi, sonuç kümesini **“title”** adlı sütuna göre sıralar.
* Sıralanacak sütunu, sütun sıra numarasını belirterek de ifade edebilirsiniz. Örneğin,

  `select title, pages from book ORDER BY 2` ifadesi, sıralama düzeninin ikinci sütundaki değerlere göre belirlendiğini gösterir.
* `JOIN` işleci, bu tablolardaki belirli sütunlar arasındaki bir ilişkiye dayanarak, iki veya daha fazla tablodan satırları birleştirir.
* Birleştirilen tablolar, genellikle tablolardan birinin birincil anahtarı olup diğer tabloda yabancı anahtar olarak görünen ortak bir sütun ile ilişkilendirilir.
* İlişkisel bir tablonun Birincil Anahtarı, tablodaki her satırı benzersiz olarak tanımlar.
* Yabancı Anahtar, başka bir varlığın birincil anahtarına referans veren sütunlar kümesidir.
* Üç veya daha fazla farklı tablodan verileri birleştirmeniz gerekiyorsa, birleştirmelere yeni tablolar eklersiniz. Önce, paylaşılan özniteliklerini eşleştirerek tablo `A` ve tablo `B` bilgilerinin birleşimini elde edersiniz. Ardından, paylaşılan özniteliklerini eşleştirerek tablo `B` ve tablo `C` bilgilerini birleştirirsiniz.
* SQL, `INNER JOIN` ve `OUTER JOIN` gibi çeşitli JOIN türleri sunar. İlgili iki tablonun kesişimine karşılık gelen bir veri kümesini çıkarabilir veya daha büyük bir veri kümesi seçebilirsiniz.
