## 💉 Diğer SQL Enjeksiyonu Saldırı Türleri

Welcome to Other Types of SQL Injection Attacks! After watching this video, you will be able to: Characterize the four types of SQL injection attacks and explain how to prevent SQL injection attacks.

Diğer SQL enjeksiyonu saldırı türlerine hoş geldiniz! Bu videoyu izledikten sonra, dört tür SQL enjeksiyonu saldırısını tanımlayabilecek ve SQL enjeksiyonu saldırılarının nasıl önleneceğini açıklayabileceksiniz.

---

## 🧩 Code Injection Nedir?

A common type of SQL injection to watch for is code injection. A code injection is an attack that inserts new SQL statements or database commands into another SQL statement. In code injection, typically the attacker will execute the two statements as one.

Dikkat edilmesi gereken yaygın bir SQL enjeksiyonu türü  *code injection* ’dır.  *Code injection* , mevcut bir SQL ifadesinin içine yeni SQL ifadeleri veya veritabanı komutları ekleyen bir saldırıdır.  *Code injection* ’da genellikle saldırgan iki ifadeyi tek bir ifade gibi çalıştırır.

---

## 🧮 Code Injection Örneği: ENCRYPT_PASSWORD

For example, before the attack the original SQL statement is

Örneğin, saldırıdan önceki orijinal SQL ifadesi şöyledir:

```sql
BEGIN 
  ENCRYPT_PASSWORD('alice', 'mypassword'); 
END;
```

It's really important to understand here that in SQL, a semicolon means an end of a statement.

Burada şunu anlamak çok önemlidir: SQL’de noktalı virgül (`;`) bir ifadenin sonunu belirtir.

After the attack the new SQL statement is

Saldırıdan sonra yeni SQL ifadesi şöyledir:

```sql
BEGIN 
  ENCRYPT_PASSWORD('alice', 'mypassword'); 
  DELETE FROM users WHERE upper(username) = upper('admin'); 
END;
```

so that becomes a complete statement, and then END; with two statements that execute as one.

Böylece bu, iki ifadenin tek bir blok içinde birlikte çalıştırıldığı tam bir ifade haline gelir ve ardından `END;` ile sonlanır.

The attacker inserts a second SQL statement after the Procedural Language for SQL command to delete the admin user from the database.

Saldırgan, SQL için kullanılan prosedürel dil komutundan sonra ikinci bir SQL ifadesi ekleyerek veritabanındaki admin kullanıcısını siler.

In a code injection attack, the attacker can delete a table or your whole database!

Bir *code injection* saldırısında saldırgan bir tabloyu silebilir, hatta tüm veritabanınızı yok edebilir!

---

## 💻 Code Injection İçin Web Uygulaması Örneği

For example, let's say the code uses

Örneğin, diyelim ki kod şu şekilde:

```python
username = request.args.get("username")
```

so it's getting in the username parameter out of the arguments passed into the request

yani isteğe (request’e) iletilen argümanlardan `username` parametresini alıyor

and then

ve ardından:

```python
password = request.args.get("password")
```

to get the password parameter out of the arguments from the request.

istekten gelen argümanlardan `password` parametresini alıyor.

Then it creates a SQL statement that says,

Sonra şu SQL ifadesini oluşturuyor:

```python
sql = 'SELECT * FROM Users WHERE Name = "' + username + '" AND password = "' + password + '"'
```

So it's doing a concatenation of the user name with that string, AND password equals "' + password + '"', so again, it's blinding concatenating whatever was passed in and then it's taking that whole string and assigning it to the variable, sql.

Yani kullanıcı adını bu string ile birleştiriyor ve `password` için de `" ' + password + '"` kısmını ekliyor; böylece içeri ne girilirse girilsin körü körüne bir string birleştirmesi yapıyor ve bu bütün string’i `sql` adlı değişkene atıyor.

And then it runs `db.execute` on that sql statement, and it saves the results in a variable called 'results.'

Sonra bu `sql` ifadesi üzerinde `db.execute` çalıştırıyor ve sonuçları `results` adlı bir değişkende saklıyor.

---

## 💣 Enjeksiyonun Gerçekleşmesi: DROP TABLE

Now, the code injection happens.

Şimdi *code injection* gerçekleşir.

The attacker enters the user name as

Saldırgan kullanıcı adını şu şekilde girer:

```text
" "; DROP TABLE Users; --
```

and for password they type in:

ve parola alanına şunu yazar:

```text
Who Cares?
```

Because as you'll see in a moment, it doesn't matter what the password is because you will never get there.

Çünkü birazdan göreceğiniz gibi, parolanın ne olduğu önemli değildir; uygulama o kontrole hiç ulaşmayacaktır.

The double dash in sql syntax is a comment character. So, the '--' comments out the remainder of the query.

SQL sözdiziminde çift tire (`--`) bir yorum karakteridir. Yani `--` işaretinden sonraki sorgunun tamamı yorum olarak kabul edilir.

---

## 🧾 Ortaya Çıkan SQL Sorgusu

Now, the resulting query is

Artık ortaya çıkan sorgu şudur:

```sql
SELECT * FROM Users WHERE Name = "";
DROP TABLE Users;
-- ...
```

SELECT * FROM Users WHERE Name = ""; That ends that statement-- then DROP TABLE Users;. That's a whole new statement that gets executed.

`SELECT * FROM Users WHERE Name = "";` ifadesi ilk sorguyu bitirir; ardından `DROP TABLE Users;` çalıştırılan tamamen yeni bir ifadedir.

And then dash-dash, it doesn't matter what the rest of the string is, because it's all taken as a comment, and the interpreter ignores it.

Ve daha sonra gelen çift tire (`--`) ile string’in geri kalanının ne olduğu artık önemli değildir; çünkü hepsi yorum olarak kabul edilir ve yorumlayıcı tarafından yok sayılır.

The SQL is valid and it will delete the entire Users table by dropping the table from the database because ';' will terminate one query and start another.

Bu SQL geçerlidir ve `;` karakteri bir sorguyu sonlandırıp diğerini başlattığı için, veritabanından tabloyu düşürerek (drop ederek) `Users` tablosunun tamamını silecektir.

---

## 🧰 Function Call Injection Nedir?

Next, a function call injection is an attack that inserts a custom function into a vulnerable SQL statement.

Sonraki tür ise  *function call injection* ’dır; bu, zafiyet içeren bir SQL ifadesinin içine özel (custom) bir fonksiyon ekleyen bir saldırıdır.

An attacker can compromise a custom function by sending data from a database to a remote computer, changing passwords, or performing sensitive database transactions.

Bir saldırgan, verileri veritabanından uzak bir bilgisayara göndermek, parolaları değiştirmek veya hassas veritabanı işlemleri gerçekleştirmek gibi amaçlarla özel bir fonksiyonu kötüye kullanabilir.

In this example of a function call injection attack, the original SQL statement simply requests user input.

Bu *function call injection* saldırısı örneğinde, orijinal SQL ifadesi yalnızca kullanıcı girdisi istemektedir.

---

## 🧪 Function Call Injection Örneği: TRANSLATE ve ADDUSER

The code is

Kod şöyledir:

```sql
SELECT TRANSLATE(
  'user input',
  '012356789ABCDEFGHIJKLMNOPQRSTUVWXYZ',
  '0123456789'
) FROM dual;
```

After the attack, the code is

Saldırıdan sonra kod şu hale gelir:

```sql
SELECT TRANSLATE(
  '' || myappadmin.adduser('admin', 'newpass') || '',
  '012356789ABCDEFGHIJKLMNOPQRSTUVWXYZ',
  '0123456789'
) FROM dual;
```

and the rest of the statement is left unchanged.

ve ifadenin geri kalanı değiştirilmeden bırakılır.

What you need to understand here is that in SQL the double vertical bar is a concatenation character.

Burada anlamanız gereken şey, SQL’de çift dikey çizginin (`||`) bir birleştirme (concatenation) operatörü olduğudur.

And so it's looking to execute the `adduser` function to concatenate the results into the statement.

Dolayısıyla, ifadenin içine sonuçları birleştirmek için `adduser` fonksiyonunu çalıştırmaya çalışır.

However; it's not the results that we're interested in. The attacker just wants you to run `adduser` and that's exactly what happens so here the attacker can modify the function with user input to create new application users.

Ancak burada önemli olan sonuçlar değildir. Saldırganın istediği tek şey `adduser` fonksiyonunun çalıştırılmasıdır ve tam olarak bu gerçekleşir; böylece saldırgan, kullanıcı girdisini kullanarak yeni uygulama kullanıcıları oluşturmak için fonksiyonu manipüle edebilir.

---

## 🧱 Buffer Overflow Nedir?

Now, a buffer overflow is when a program allocates more data in a buffer than the buffer can store.

Şimdi, *buffer overflow* (tampon taşması), bir programın bir tamponda tutulabilecek kapasiteden daha fazla veri ayırması durumudur.

A buffer contains temporary storage for data transfers.

Bir tampon, veri transferleri için geçici depolama alanı içerir.

A buffer overflow causes a system or program to crash or execute malicious code.

Bir  *buffer overflow* , bir sistemin veya programın çökmesine ya da kötü amaçlı kod çalıştırmasına neden olabilir.

---

## 🧨 Buffer Overflow ile SQL Injection

An attacker can use a buffer overflow SQL injection to exploit an unpatched database with functions such as:

Bir saldırgan, aşağıdaki gibi fonksiyonları kullanan yamalanmamış (unpatched) bir veritabanını sömürmek için *buffer overflow SQL injection* kullanabilir:

* `tz_offset`, which returns the time zone offset;

  zaman dilimi ofsetini döndüren `tz_offset`,
* or `to_timestamp_tz`, which converts an input expression into a timestamp;

  bir girdi ifadesini zaman damgasına dönüştüren `to_timestamp_tz`,
* and `bfilename`, which returns a BFILE locator associated with a physical large object binary file on the system.

  sistemdeki fiziksel büyük nesne (LOB) ikili dosyasıyla ilişkili bir BFILE lokatörü döndüren `bfilename`.

All of these functions had vulnerabilities.

Bu fonksiyonların hepsinde zafiyetler bulunmuştur.

If you do not patch a database for buffer overflow vulnerabilities, an attacker can use SQL injection on these and other functions.

Veritabanınızı *buffer overflow* zafiyetlerine karşı yamazsanız, bir saldırgan bu ve benzeri fonksiyonlara SQL enjeksiyonu uygulayabilir.

---

## 🛡️ SQL Injection’a Karşı Korunma Yöntemleri

You can protect your application against SQL injection attacks with these preventative measures.

Uygulamanızı SQL enjeksiyonu saldırılarına karşı şu önleyici tedbirlerle koruyabilirsiniz:

Use query parameters as placeholders to create statements that are dynamic.

Dinamik ifadeler oluşturmak için sorgu parametrelerini yer tutucu (placeholder) olarak kullanın.

The SQL interpreter will check values in your query when it executes.

SQL yorumlayıcısı, çalıştırma sırasında sorgunuzdaki değerleri kontrol edecektir.

Validate on the server side instead of on the client side to identify untrusted data inputs.

Güvenilmeyen veri girdilerini tespit etmek için istemci tarafı yerine sunucu tarafında doğrulama yapın.

Restrict user privileges to avoid giving the attacker authorization. For example, start their access with read-only access.

Saldırgana yetki vermemek için kullanıcı ayrıcalıklarını kısıtlayın. Örneğin, kullanıcı erişimini başlangıçta yalnızca okuma (read-only) yetkisiyle başlatın.

And perform dynamic application security testing (or DAST), which can identify vulnerabilities when you release new code to production.

Ayrıca, yeni kodu üretim ortamına aldığınızda zafiyetleri tespit edebilen dinamik uygulama güvenliği testleri ( *DAST* ) gerçekleştirin.

---

## 🧾 Parametreli Sorgu Örneği ile Korunma

Here is an example of what you should be doing. This example uses query parameters to prevent SQL manipulation attacks.

Yapmanız gereken şeye bir örnek verelim. Bu örnek, SQL manipülasyon saldırılarını önlemek için sorgu parametreleri kullanır.

The code is

Kod şöyledir:

```python
username = request.args.get("username")
```

just like before, but then the SQL statement is different.

tıpkı önceki gibi, ancak bu kez SQL ifadesi farklıdır:

```sql
SELECT * FROM Users WHERE userid = ?;
```

and then, it calls `db.execute` on not only the `sql` variable, but also passing in the `username` to get the result.

ve ardından, sonuçları almak için sadece `sql` değişkenini değil, aynı zamanda `username` değerini de geçirerek `db.execute` çağrısı yapılır.

The '?' parameter in the statement is a placeholder for a value.

Bu ifadede `?` parametresi, bir değer için yer tutucudur.

Now, you are using variable substitution.

Artık değişken ikamesi (variable substitution) kullanıyorsunuz.

And when the SQL interpreter checks each parameter, it will treat the input as a string, not as a statement.

Ve SQL yorumlayıcısı her parametreyi kontrol ederken girdiyi bir ifade olarak değil, sadece bir string olarak ele alacaktır.

Any bad data will only be stored as a string in your database but will not get executed.

Kötü niyetli herhangi bir veri, veritabanınızda yalnızca bir string olarak saklanır, fakat çalıştırılmaz.

---

## 📚 Özet: Diğer SQL Enjeksiyonu Türleri

In this video, you learned that:

Bu videoda şunları öğrendiniz:

Code injection attacks insert new SQL statements or database commands into another SQL statement, causing them to execute as one.

*Code injection* saldırıları, yeni SQL ifadelerini veya veritabanı komutlarını başka bir SQL ifadesinin içine ekler ve bunların tek bir ifade olarak çalıştırılmasına neden olur.

Function call injection attacks insert a custom function into a vulnerable SQL statement allowing them to perform unauthorized changes, transactions, or potentially compromising remote computers.

*Function call injection* saldırıları, zafiyet içeren bir SQL ifadesinin içine özel bir fonksiyon ekler ve yetkisiz değişiklikler, işlemler yapılmasına veya uzak bilgisayarların potansiyel olarak ele geçirilmesine olanak tanır.

Buffer overflow attacks can cause crashes by allocating more data to the buffer than what it can hold.

*Buffer overflow* saldırıları, bir tampona kapasitesinden fazla veri yükleyerek sistemin veya programın çökmesine neden olabilir.

To prevent SQL injection attacks, use query parameters as placeholders.

SQL enjeksiyonu saldırılarını önlemek için sorgu parametrelerini yer tutucu olarak kullanın.

Use server-side validation to identify untrusted data inputs.

Güvenilmeyen veri girdilerini tespit etmek için sunucu tarafı doğrulama uygulayın.

Restrict user privileges to prevent attackers from obtaining that level of authorization.

Saldırganların bu seviyede yetki elde etmesini engellemek için kullanıcı ayrıcalıklarını kısıtlayın.

And keep your database patched and perform dynamic application security testing (or DAST) to identify vulnerabilities during new code releases.

Ve yeni kod sürümleri sırasında zafiyetleri tespit etmek için veritabanınızı güncel yamalarla koruyun ve dinamik uygulama güvenliği testleri ( *DAST* ) gerçekleştirin.
