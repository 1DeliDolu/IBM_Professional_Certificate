# 🔽 Sonuç Kümelerini Sıralama

## 🎬 Giriş

Merhaba, **SELECT** ifadesi sonuç kümelerinin sıralanmasına hoş geldiniz.

Bu videoda, ilişkisel bir veritabanı tablosundan veri almaya yönelik bazı ileri teknikleri ve sonuç kümesinin nasıl sıralanacağını öğreneceğiz.

## 🎯 Dersin Hedefleri

Bu dersin sonunda, sonuç kümesini artan veya azalan düzende nasıl sıralayabileceğinizi tanımlayabilecek ve sıralama düzeni için hangi sütunun kullanılacağını nasıl belirteceğinizi açıklayabileceksiniz.

---

## 💾 Veritabanı Yönetim Sisteminin Amacı

Bir veritabanı yönetim sisteminin temel amacı yalnızca verileri depolamak değil, aynı zamanda verilerin alınmasını da kolaylaştırmaktır.

En basit hâliyle bir **SELECT** ifadesi şu şekildedir:

```sql
SELECT * FROM TableName;
```

Basitleştirilmiş kütüphane veritabanı modelimiz ve **Book** tablosuna dayanarak:

```sql
SELECT * FROM Book;
```

ifadeleri, dört satırlık bir sonuç kümesi verir.

**Book** tablosundaki tüm sütunlar için tüm veri satırları görüntülenir.

---

## 📚 Belirli Sütunları Listeleme

Sadece kitap başlıklarını listelemeyi de tercih edebiliriz. Aşağıdaki örnekte gösterildiği gibi:

```sql
SELECT Title FROM Book;
```

Ancak, sıralama herhangi bir düzende görünmemektedir.

---

## 🔤 Sonuç Kümesini Alfabetik Olarak Sıralama

Sonuç kümesini alfabetik sırada görüntülemek, sonuç kümesini daha kullanışlı hâle getirir.

Bunu yapmak için **ORDER BY** ifadesini kullanırız.

Sonuç kümesini alfabetik sırada görüntülemek için, **ORDER BY** ifadesini **SELECT** ifadesine ekleriz.

**ORDER BY** ifadesi, bir sorguda sonuç kümesini belirtilen bir sütuna göre sıralamak için kullanılır.

Bu örnekte, sonuç kümesini sıralamak için **Title** sütunu üzerinde `ORDER BY` kullanılmıştır.

Varsayılan olarak, sonuç kümesi **artan** düzende sıralanır.

Bu örnekte, sonuç kümesi kitap başlığına göre alfabetik sırada sıralanmıştır.

---

## 🔁 DESC ile Azalan Sıralama

Azalan düzende sıralama yapmak için `DESC` anahtar sözcüğünü kullanırız.

Artık sonuç kümesi, belirtilen sütuna göre (bu örnekte  **Title** ) sıralanmış ve **azalan** düzende düzenlenmiştir.

İlk üç satırın sırasına dikkat edin; başlığın ilk üç kelimesi aynıdır. Bu nedenle sıralama, karakterlerin farklılaştığı noktadan itibaren başlar.

---

## 🔢 Sıralama için Sütun Numarasını Kullanma

Sıralama sütununu belirtmenin bir diğer yolu, sütun sıra numarasını kullanmaktır.

Bu örnekte:

```sql
SELECT title, pages FROM Book ORDER BY 2;
```

ifadesi, sorgudaki sütun sıra numarasını, sıralama düzeni için belirtir.

**Pages** sütun adını belirtmek yerine, **2** sayısı kullanılmıştır.

**SELECT** ifadesinde, sütun listesindeki ikinci sütun  **Pages** ’tir. Bu nedenle sıralama düzeni, **Pages** sütunundaki değerlere göre yapılır.

Bu durumda, **Pages** sütunu kitabın sayfa sayısını göstermektedir.

Görüldüğü gibi, sonuç kümesi sayfa sayısına göre artan düzende sıralanmıştır.

---

## ✅ Ders Özeti

Artık sonuç kümesini hem artan hem de azalan düzende nasıl sıralayabileceğinizi ve sıralama düzeni için hangi sütunun kullanılacağını nasıl belirteceğinizi açıklayabilirsiniz.

Bu videoyu izlediğiniz için teşekkürler.
