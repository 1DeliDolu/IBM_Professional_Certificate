# SQL Injection’lar

## SQL Injection’a Giriş ve Öğrenme Hedefleri

SQL Injection’a hoş geldiniz! Bu videoyu izledikten sonra şunları yapabileceksiniz:

Structured Query Language (veya SQL, “sequel” olarak telaffuz edilir) injection’larını açıklamak, dört tür SQL injection’ını tanımlamak ve saldırganların bir saldırıda hangi SQL ifadelerini (clauses) ve operatörlerini kullandığını açıklamak.

## SQL Injection Nedir?

SQL (veya “sequel”) injection, bir veritabanını istismar etmek için bir string girdi geçiren bir saldırıdır.

Örneğin, bir web sayfasındaki bir alanda kullanıcı girdisi istediğinizde SQL injection gerçekleşebilir. Bir SQL injection’da saldırgan, *set operations* kullanarak bir SQL ifadesini değiştirir.

Ya da farklı sonuçlar döndürmek için `WHERE` ifadesini değiştirir.

Yaygın görülen dört SQL injection saldırı türü şunlardır:  *SQL manipulation* ,  *code injection* , *function call injection* ve  *buffer overflow* ’lar.

## SQL Manipulation Saldırıları

 *SQL manipulation* , SQL injection türleri arasında en yaygın olanlardan biridir.

Bir  *SQL manipulation* , *set operations* içeren bir SQL ifadesini değiştiren bir saldırıdır.

SQL manipulation saldırılarının iki yaygın biçimi bir `WHERE` ifadesi ya da bir `UNION` ifadesi kullanır.

Çoğu zaman bir SQL manipulation saldırısı, kullanıcı kimlik doğrulamasındaki bir `WHERE` ifadesini her zaman `TRUE` sonucunu verecek şekilde değiştirir.

Örneğin, SQL ifadesinin

```sql
SELECT * FROM users WHERE username = ‘alice’ and PASSWORD = ‘mypassword’;
```

olduğunu varsayalım; saldırıdan sonra SQL ifadesi:

```sql
SELECT * FROM users WHERE username = ‘alice’ and PASSWORD = ‘mypassword’ or ‘a’ = ‘a’
```

hâline gelir.

Bu örnek her zaman `TRUE` sonucunu üretir, çünkü saldırgan tarafından eklenen `a` her zaman `a`’ya eşittir.

Ya da bir saldırgan, farklı tablolardan veri almak için bir `UNION SELECT` ifadesini değiştirebilir. Bu örnek, Python programlama dili ve string birleştirme (string concatenation) kullanır.

## Python ile String Birleştirme Örneği

Elinizde şu argümanlar vardır:

```python
username = request.args.get ("username")
```

Bu, iletilen argümanlardan kullanıcı adını alacaktır.

Ve ardından:

```python
password = request.args.get equals "password"
```

vardır; yani yine iletilen argümanlardan parolaları alıyor ve bunları bir değişkene atıyoruz.

Sonra ifade `'SELECT * FROM Users WHERE Name =` olur ve bununla, iki artı karakteri kullanarak `(+ username +)` kullanıcı adını birleştirir.

`AND Password =` ve yine parolayı iki artı karakteriyle `( + password + )` birleştirir ve bu string `sql` adlı bir değişkene atanır.

Sonraki satırda ise `db.execute` çağrılır, bu `sql` ifadesi parametre olarak geçirilir ve sonuç `results` adlı değişkene atanır.

Bu kod parçacığında neler olduğuna dikkat edin. İstekten (request) gelen değişkenlerle tüm bu string değerleri artı artı artı artı (plus plus plus plus) kullanarak birleştiriyorsunuz.

 *Happy path* ’te, kullanıcı adını `John Doe` ve parolasını `myPass` olarak girer.

Ve ortaya çıkan sorgu string’i:

```sql
SELECT * FROM Users WHERE Name ="John Doe" AND Password ="myPass"
```

olur.

Bu da tam olarak beklediğimiz şeydir.

## "OR 1=1" ile SQL Injection Senaryosu

Bu SQL, adı `John Doe` ve parolası `myPass` olan kullanıcıları döndürür.

Ancak bir SQL injection saldırısında, saldırganın kullanıcı adı alanına `" OR 1=1` ve parola alanına da `" OR 1=1` girdiğini varsayalım.

Artık ortaya çıkan sorgu string’i:

```sql
SELECT * FROM Users WHERE Name ="" OR 1=1 AND Pass ="" OR 1=1
```

olur.

Buradaki sorun, `OR` ifadesi ve `1`’in her zaman `1`’e eşit olması nedeniyle adın boş, parolanın boş olmasının hiçbir öneminin olmamasıdır.

Bu SQL ifadesi, `1=1` her zaman `True` olarak değerlendirileceği için tablonuzdaki tüm kullanıcıları her zaman döndürecektir!

Dolayısıyla, bir SQL ifadesi oluşturmak için string’leri birleştirmenin ne kadar tehlikeli olduğunu görebilirsiniz.

## Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* SQL injection, bir veritabanını istismar etmek için bir string girdi geçiren bir saldırıdır.
* SQL saldırıları, bir web sayfasında kullanıcı girdisi istendiğinde gerçekleşebilir.
* Bir SQL manipulation saldırısında saldırgan, *set operators* kullanarak ya da `WHERE` ifadelerini veya `UNION` operatörlerini değiştirerek bir SQL ifadesini değiştirir.
* Dört tür SQL injection saldırısı vardır:  *SQL manipulation* ,  *code injection* , *function call injection* ve  *buffer overflow* . Ve  *SQL manipulation* , injection saldırılarının en yaygın türüdür.
