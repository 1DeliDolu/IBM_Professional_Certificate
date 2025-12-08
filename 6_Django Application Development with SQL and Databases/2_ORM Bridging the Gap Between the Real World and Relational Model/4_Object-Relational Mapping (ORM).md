# 🧩 Nesne-İlişkisel Eşleme (ORM)

## 👋 ORM'ye Hoş Geldiniz

Nesne-İlişkisel Eşleme'ye, yani  *Object-Relational Mapping* 'e (ORM) hoş geldiniz. Bu videoda, ORM'in veritabanlarıyla uygulama geliştirmeyi nasıl basitleştirebileceğini açıklayacağız.

Bu videoyu izledikten sonra şunları yapabileceksiniz:

* SQL paradigması ile nesne yönelimli programlama (OOP) paradigması arasındaki farkı açıklamak.
* ORM'in temel kavramlarını açıklamak ve ORM'in artılarını ile eksilerini listelemek.

![1765191016435](image/4_Object-RelationalMapping(ORM)/1765191016435.png)

---

## 🗄️ Uygulama Kodunda SQL ve Veritabanı Kullanımı

Yazılım geliştiricileri, uygulamaları için veritabanını çoğu zaman ana veri deposu olarak kullanırlar; bu yüzden SQL'i uygulama kodlarına entegre etmeleri gerekir.

SQL ifadeleri, uygulama kodu içinde birleştirilmeli ve veritabanı API'leri kullanılarak veritabanı sisteminde çalıştırılmalıdır.

Getirilen veritabanı satırları, veritabanındaki satırlar üzerinde yineleme yapmak için kullanılan özel bir kontrol veri yapısı olan `Cursor` olarak uygulama koduna geri döner.

Bu çevrimiçi kurs veritabanı yalnızca iki varlık içerir: `Course` ve `Learner`.

Aralarındaki ilişki *çoktan çoğa* (`Many-To-Many`) bir ilişkidir. Bir derse birçok öğrenci (`learner`) kayıtlı olabilir ve bir öğrenci de birçok derse (`course`) kaydolabilir.

Bu ilişki, ilişkilendirici bir tabloda ( *associative table* ) kalıcı hâle getirilir.

![1765191040234](image/4_Object-RelationalMapping(ORM)/1765191040234.png)![1765191070541](image/4_Object-RelationalMapping(ORM)/1765191070541.png)

---

## 🐍 Python'da SQL Çalıştırma Örneği

Şimdi Python kodu içinde SQL çalıştırmaya bir örnek görelim.

Önce, gömülü bir `SQLite` veritabanına bir bağlantı oluştururuz. Bu, boş olan çevrimiçi kurs veritabanıdır.

Ardından, bağlantı bağlamından (`connection context`) bir `Cursor` nesnesi oluştururuz.

Sonra SQL'i gönderip çalıştırabiliriz. Bir `INSERT` ifadesiyle bir öğrenci (`learner`) kaydı oluşturup ekleyerek başlarız.

`INSERT` ifadesi oluşturulduktan sonra, SQL'i çalıştırmak için `Cursor` nesnesinin yürütme metodunu ( *execute method* ) çağırırız.

Son olarak, az önce eklediğimiz öğrenci kaydını sorgulamak için başka bir `SELECT` ifadesi oluşturur ve ilk satırı almak için `Cursor-Fetch-One` kullanırız.

Çıktı, az önce eklediğimiz öğrenci satırını gösterir.

![1765191118085](image/4_Object-RelationalMapping(ORM)/1765191118085.png)

---

## 🧱 SQL Paradigması ve OOP Paradigması

Modern uygulama geliştirme ortamında OOP ana akımdır ve SQL'den oldukça farklıdır.

Varlıkları tablolar, satırlar ve sütunlar kullanarak modelleyen SQL'in aksine, nesne yönelimli bir dil varlıkları sınıflar ve nesneler kullanarak modeller.

---

## 🧾 OOP'de `Course` ve `Learner` Sınıfları

OOP'de `Course` varlığı, iki ilkel ( *primitive* ) özelliğe (`name` ve `description`) ve bir başvuru ( *reference* ) niteliğine, yani öğrenci listesini (`list of learners`) tutan bir özelliğe sahip bir sınıf olarak tanımlanır.

Sınıf öznitelikleriyle birlikte, veri işleme ( *data manipulation* ) için kullanılacak metodların da tanımlanması gerekir. Burada basit bir metot tanımlarız: `getLearners`.

`Learner` varlığı da dört özelliğe sahip bir sınıf olarak tanımlanır:  *first name* ,  *last name* , *date of birth* ve  *occupation* .

Ayrıca basit bir `printProfile` metodu da tanımlanır.

![1765191139172](image/4_Object-RelationalMapping(ORM)/1765191139172.png)

---

## 🧍‍♀️ SQL ve OOP ile `Learner` Nesnesi Oluşturma

Hem SQL hem de OOP paradigmalarını kullanarak bir `Learner` nesnesini veritabanından oluşturalım.

Önce bir SQL `SELECT` ifadesi çalıştırır ve ilk `Learner` satırını alırız.

Veriyi `Learner` nesnesine yüklemek için, varsayılan kurucusunu ( *default constructor* ) çağırarak bir nesne oluştururuz.

Daha sonra nesneyi, `cursor` üzerinden sorgulanan öznitelik değerleriyle güncelleriz.

Her sütunu, her sınıfın ilkel ( *primitive* ) özniteliğine elle eşlememiz gerekir.

Karmaşık veri ilişkilerimiz varsa, bu süreç karmaşık hâle gelebilir.

Son olarak, nesneyi yazdırmak için `printProfile` metodunu çağırırız.

![1765191173863](image/4_Object-RelationalMapping(ORM)/1765191173863.png)

---

## 🔗 SQL ve OOP'de Veri Modellenmesi ve İlişkiler

Gördüğümüz gibi, OOP ve SQL paradigmaları veriyi farklı şekilde modeller.

OOP, varlıkları sınıflar, nesneler ve öznitelikler kullanarak modellerken SQL, varlıkları tablolar, satırlar ve sütunlar kullanarak modeller.

Ayrıca OOP, ilişkileri kalıtım ( *inheritance* ), ilişki ( *association* ) ve bütünleme ( *aggregation* ) gibi sınıf kalıplarıyla modellerken SQL, ilişkileri `JOIN` ve `FOREIGN KEY` kullanarak modeller.

Son olarak, OOP veriler üzerinde `CRUD` işlemlerini metodlar aracılığıyla gerçekleştirirken SQL, `INSERT`, `DELETE` ve `UPDATE` gibi SQL ifadelerinden oluşan bir veri işleme dili kullanarak `CRUD` işlemlerini yapar.

![1765191238761](image/4_Object-RelationalMapping(ORM)/1765191238761.png)

---

## 🌉 Neden ORM? OOP ve SQL Arasındaki Boşluğu Doldurmak

Modern uygulamaları genellikle OOP kullanarak geliştirdiğimize göre, veritabanlarına SQL yerine OOP kullanarak da erişebilir miyiz?

Bu sayede geliştirme sürecimizde tek bir programlama paradigmasına bağlı kalabiliriz.

İnsanların nesne-ilişkisel eşlemeyi ( *object-relational mapping* ) icat etmelerinin başlıca nedeni, OOP ile SQL arasındaki boşluğu doldurmak ve veritabanlarına erişmek için OOP dillerinin kullanılabilmesini sağlamaktır.

`ORM` kütüphaneleri veya araçları, ilişkisel bir veritabanında satırlar hâlinde saklanan veriyi nesnelere veya nesneleri satırlara eşleyip aktarabilir.

Diyelim ki bir geliştirici tarafından OOP kullanılarak oluşturulmuş bir `Learner` nesne modeli var.

![1765191289964](image/4_Object-RelationalMapping(ORM)/1765191289964.png)

---

## 🔁 ORM ile Nesneler ve Satırlar Arasında Dönüşüm

ORM, `Learner` nesnesini `Learner` tablosundaki bir `Learner` satırına dönüştürmeye ve sonra bunu tekrar bir `Learner` nesnesi olarak geri okumaya yardımcı olabilir.

Bu, geliştiricilerin iş yükünü azaltır çünkü yalnızca nesne işlemlerine odaklanmaları yeterlidir.

---

## 🧮 ORM ile Üç Tabloyu Tek Satır Kodla Sorgulamak

ORM'in, üç tablonun birleştirildiği ( *three-table-join* ) bir SQL sorgusunu tek satırlık bir koda nasıl dönüştürebileceği şöyledir.

Diyelim ki `Introduction to Python` dersine kayıtlı tüm öğrencileri (`learners`) almak istiyoruz.

SQL'de tüm bilgileri almak için `Course`, `Learner` ve bunlara ait başvuru ( *lookup* ) tablolarını birleştirmemiz gerekir.

Ayrıca hem OOP hem de SQL paradigmalarını karıştırmamız gerekir.

Ancak ORM'in yardımıyla, önce `Course` sınıfında adıyla dersi bulmak için `get` metodunu çağırmamız ve ardından o derse ait tüm öğrencileri almamız yeterlidir.

![1765191321630](image/4_Object-RelationalMapping(ORM)/1765191321630.png)

---

## 🧰 Farklı Dillere Yönelik ORM Kütüphaneleri

Artık ORM'in ne kadar kullanışlı olduğunu öğrendiğinize göre, onu kendi uygulamanızda kullanmak isteyebilirsiniz.

Hemen hemen tüm popüler diller için ORM kütüphaneleri vardır.

Python için `Django Model` ve `SQLAlchemy` kullanabilirsiniz.

Java için `Hibernate` ve `OpenJPA`, JavaScript için ise `Sequelize` ve `TypeORM` kullanabilirsiniz.

Bunlar sadece birkaç örnektir.

Bu derste `Django Model` üzerinde yoğunlaşacağız.

![1765191354668](image/4_Object-RelationalMapping(ORM)/1765191354668.png)

---

## ⚖️ ORM'in Avantajları

Tüm üçüncü taraf yazılım kütüphaneleri gibi ORM'in de artıları ve eksileri vardır.

Olumlu taraftan bakarsak:

* ORM ile veritabanlarını sınıf tasarımlarınız tanımlar.
* OOP tabanlı uygulama geliştirme için sadece sınıfları tanımlamanız ve nesneler oluşturmanız gerekir.
* SQL yazmadan veritabanlarını kullanabilirsiniz.
* SQL sözdizimi farklılıklarını dert etmeden, tek bir ORM arayüzüyle birden fazla veritabanı sistemini yönetebilirsiniz.
* Tüm bu avantajlar, uygulamanızı teslim etme sürecinizi hızlandıracaktır.

![1765191395902](image/4_Object-RelationalMapping(ORM)/1765191395902.png)

---

## ⚠️ ORM'in Dezavantajları

Olumsuz tarafta ise:

* SQL ve OOP hâlâ farklı modelleme kavramlarına sahip iki ayrı dildir ve ORM, nesneleri veritabanı tablolarına eşlemede zaman zaman başarısız olabilir.
* ORM, veri erişim mantığını uygulama koduyla birleştirdiği için, veritabanında yapılacak herhangi bir değişiklik hem uygulama mantığında hem de veri erişim mantığında değişiklik yapılmasını gerektirir.
* ORM, implementasyon ayrıntılarını gizlediğinden, hata ayıklama ( *debugging* ) zorlayıcı olabilir.
* ORM, fazladan bir çeviri katmanı eklediği için uygulama performansını düşürebilir ve çevrilen SQL ifadelerinin optimize edilmiş olacağını garanti edemez.

![1765191446519](image/4_Object-RelationalMapping(ORM)/1765191446519.png)

---

## 📝 Bölüm Özeti

Bu videoda şunları öğrendiniz:

* SQL ve OOP, veriyi farklı şekilde modeller.
* ORM, SQL ile OOP arasındaki boşluğu doldurur.
* ORM, uygulama geliştiricilerin SQL kodu yazmadan veritabanlarını kullanabilmesini sağlar.
* ORM, uygulama geliştirme sürecini hızlandırabilir ve ORM'in dezavantajları arasında kusurlu eşleme, artan kod bağımlılığı ( *coupling* ) ve hata ayıklamadaki zorluk yer alır.

![1765191480372](image/4_Object-RelationalMapping(ORM)/1765191480372.png)
