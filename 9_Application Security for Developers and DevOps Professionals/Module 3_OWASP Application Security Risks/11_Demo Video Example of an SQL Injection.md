# 💻 Demo Videosu: Bir SQL Enjeksiyonu Örneği

## 🎯 Öğrenme Hedefleri

SQL Enjeksiyonu Örneği'ne hoş geldiniz.

Bu videoyu izledikten sonra, bir SQL enjeksiyonunu tanımlayabilecek ve bir SQL ifadesi ile SQL enjeksiyonu içeren bir SQL ifadesini karşılaştırabileceksiniz.

Yapılandırılmış sorgu dili (*Structured Query Language* – SQL) enjeksiyonu, ilişkisel veritabanlarına yönelik yaygın bir saldırı türüdür.

Yamanmamış yazılımlar veya hatalı yapılandırma gibi veritabanlarında bulunan güvenlik açıkları, SQL enjeksiyonları kullanılarak kötü amaçlı saldırıların gerçekleşmesine olanak tanır.

SQL enjeksiyonları ayrıca ilişkisel veritabanlarına gönderilen SQL ifadelerinin içerisinde de ortaya çıkabilir.

Saldırganlar, bir veritabanını ele geçirmek için yaygın SQL saldırılarını uygular. Yaygın saldırılardan biri, bir SQL ifadesine şüpheli karakterler gönderilmesidir.

---

## 🧨 Şüpheli Karakterlerle SQL İfadesine Saldırı

Örneğin, tek tırnak veya çift tırnak gibi karakterler, string birleştirme ( *string concatenation* ) kullanan bir SQL ifadesini değiştirmek için kullanılabilir.

Saldırganlar tırnakları kötüye kullanarak, uygun kriterlerden yoksun SQL ifadeleri bilerek gönderebilir ve normalde yanlış olması gereken bir ifadeyi doğruya dönüştürebilir.

Saldırganların sıkça kötüye kullandığı diğer bir karakter de noktalı virgüldür (`;`), çünkü SQL komutlarını birbirinden ayırır.

Noktalı virgül bir komutu sonlandırdığı için, orijinal SQL komutunu bitirmek ve sistemi hedef alan başka bir komutu başlatmak için kullanılabilir.

Dördüncü yaygın kötüye kullanılan karakter ise eksi (dash) karakteridir (`-`). SQL sözdiziminde iki eksi karakteri (`--`) satır içi bir yorum başlatır.

Bu durum, saldırganların bir SQL sorgusunun ikinci yarısının değerini ortadan kaldırmasına olanak tanıyabilir.

---

## ⚙️ SQL Enjeksiyonuna Açık Bir SQL İfadesi

Şimdi SQL enjeksiyon saldırısına karşı savunmasız bir SQL ifadesi örneğine bakalım.

Bu Python kodunun ilk iki satırı, istek ( *request* ) argümanlarından bir kullanıcı adı ve parola alır.

Daha sonra, bir `SELECT` ifadesi oluşturan birkaç string’i birleştirerek bir SQL ifadesi yaratır.

İfade şu kısım ile başlar:

`SELECT name FROM user WHERE username =`

Ardından, istek parametresi olan `username` içinde ne gönderildiyse, bunu artı (`+`) operatörünü kullanarak birleştirir.

Sonra şu kelimeleri birleştirmeye devam eder:

`AND password =`

Ve yine, istek parametresi olan `password` içinde ne gönderildiyse, onu da artı (`+`) operatörüyle, hiçbir kontrol yapmadan birleştirir.

Son olarak, ortaya çıkan bu string’i çalıştırılmak üzere SQL veritabanı motoruna gönderir.

Saldırının fiilen gerçekleştiği yer burasıdır.

---

## ❗ Şüpheli Karakterler Kullanıldığında Ne Olur?

Saldırgan, bahsettiğimiz şüpheli karakterlerden bazılarını kullanacak olursa, ifade programcının başlangıçta amaçladığı şekilde davranmayabilir.

Şimdi bunun nasıl gerçekleşebileceğine dair bir demonun nasıl işlediğine bakalım.

Önce bir kullanıcının sisteme kullanıcı adı ve parolasını girmesiyle başlıyoruz.

Önce, kullanıcı adı alanına `"admin"` girilir.

Sonra, aynı kullanıcı için parola alanına `"admin"` yazılır.

Ardından **Login** (Giriş) düğmesine tıklanır.

Ne yazık ki, geçersiz kullanıcı adı veya parola nedeniyle erişim reddedilir.

---

## 🔐 Doğru Kimlik Bilgileriyle Giriş

Şimdi bir sonraki kimlik bilgisi setini deneyelim.

Yine kullanıcı adı alanına `admin` girilir, ancak bu kez parola alanına `admin123` girilir.

**Login** düğmesine tıklandığında, kullanıcı yönetici uygulamasına erişebilir.

Kullanıcı, `admin123` parolasını kullanarak başarıyla oturum açmıştır.

---

## 💣 SQL Enjeksiyonu ile Girişin Ele Geçirilmesi

Şimdi bir SQL enjeksiyonu örneğine bakalım.

Demonun bu bölümünde SQL ifadesi, saldırgana, parolayı özel karakterler kullanarak parola alanına kötü amaçlı bilgi girip uygulamanın güvenliğini altüst etme ve başarılı şekilde oturum açma olanağı sağlayacaktır.

Tekrar denemek için **Go back to login** (Giriş sayfasına geri dön) seçeneğine tıklanır.

Önce, kullanıcı adı alanına tekrar `admin` girelim.

Parola için kullanılan karakter dizisine dikkat edin.

Bu dizi, önce `unknown` kelimesinden, ardından bir tek tırnaktan (`'`) oluşur.

Bu tek tırnak, önceki SQL ifadesinde string birleştirme sırasında, parolanın sonu olarak yorumlanacaktır.

Daha sonra bu dizinin devamında SQL anahtar sözcüğü `OR` gelir ve ardından `1 = 1` karakterleri yer alır; bu karakterler, bu örnekte tek tırnaklar içine alınmıştır.

Şimdi sırada ne olduğuna bakalım.

Bu karakter dizisini parola alanına kopyalayıp yapıştırdıktan sonra **Login** düğmesine tıklayın.

---

## 🔓 OR 1 = 1 Mantığı ile Yetkisiz Erişim

Saldırgan bu şekilde başarıyla oturum açabilir.

Tüm SQL enjeksiyonu ifadesi şudur:

```sql
SELECT name FROM user where name = admin and password = unknown or 1 = 1
```

`OR` ifadesinin `TRUE` (doğru) sonuç vermesi için iki argümandan yalnızca birinin doğru olması yeterlidir.

Parola `unknown` değerine eşit olmasa da, `1 = 1` ifadesi her zaman doğrudur; bu da tüm ifadenin doğru olarak değerlendirilmesine neden olur.

Böylece, `SELECT` ifadesinde ne isteniyorsa — bu durumda `name` alanı — SQL ifadesi tarafından başarıyla döndürülür.

Saldırganın oturum açabilmesini sağlayan şey tam olarak budur.

Saldırganlar, bu tür SQL enjeksiyonlarını, hatalar oluşturarak bu uygulama gibi veritabanlarını ve uygulamaları ele geçirmek amacıyla kullanırlar.

Peki bu tür bir SQL enjeksiyon saldırısının gerçekleşmesini nasıl engellersiniz?

---

## 🛡️ SQL Enjeksiyonunu Önlemek: Yer Tutucular (Placeholders)

Bunun sırrı **yer tutucular** ( *placeholders* ) kullanmaktır.

Gösterilen Python kodunda, istekten kullanıcı adı ve parola almak için yine aynı iki satır kod kullanılır.

Farklı olan kısım, SQL ifadesidir.

String birleştirme yapmak yerine, değişkenin hangi noktada yerine geçeceğini belirtmek için bir **soru işareti** (`?`) yer tutucu olarak kullanılır.

Kodun son satırında, veritabanı motorunun SQL ifadesini çalıştırmakla kalmayıp, yerine koyma ( *substitution* ) için kullanılacak iki değişkeni de geçirdiğini görürsünüz.

Bu değişkenler, soru işaretlerinin yerine kullanılacaktır.

Aradaki fark küçük gibi görünse de oldukça önemlidir.

---

## 📊 String Birleştirme ve Yer Tutucuların Karşılaştırılması

İlk durumda, yani string birleştirme kullanıldığında, veritabanı, enjekte edilmiş kötü amaçlı komutlar da dahil olmak üzere tüm string’i yorumlayacaktır.

İkinci durumda ise, veritabanı bu değişkenlerin **veri** olduğunu ve yorumlanmaması gerektiğini bilir.

Örneğin, değişken şu string’i içerseydi:

```sql
DROP TABLE USER;
```

bu komut çalıştırılmazdı.

Bu kelimeler sadece veritabanına eklenir, hiçbir tablo silinmezdi.

Tekrar vurgulamak gerekirse:

String birleştirme kullanıldığında, `DROP TABLE USER;` kelimeleri bir komut olarak yorumlanır ve veritabanı tarafından yürütülür.

Oysa yer tutucular kullanıldığında, `DROP TABLE USER;` kelimeleri **veri** olarak yorumlanır ve yalnızca metin olarak güvenli şekilde veritabanına eklenir.

---

## 📌 Özet

Bu videoda, SQL enjeksiyonunun ilişkisel veritabanlarına yönelik yaygın bir saldırı türü olduğunu öğrendiniz.

SQL enjeksiyonlarının, ilişkisel veritabanlarına gönderilen SQL ifadelerinin içinde de gerçekleşebileceğini gördünüz.

Saldırganların, tek tırnak, çift tırnak, noktalı virgül ve eksi gibi şüpheli karakterler göndererek bir veritabanını ele geçirmek için yaygın SQL saldırıları gerçekleştirdiklerini incelediniz.

Ayrıca, bir SQL ifadesinin nasıl savunmasız olabileceğini ve bunu yer tutucular ( *placeholders* ) kullanarak nasıl önleyebileceğinizi gördünüz.
