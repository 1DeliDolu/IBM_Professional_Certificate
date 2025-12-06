# ⚠️ İstisna (Exception) Yönetimi

## 👋 Giriş ve Öğrenme Hedefleri

Hello. Exception Handling'e hoş geldiniz.

Bu videoyu izledikten sonra, istisna (exception) yönetimini açıklayabilecek, istisna yönetiminin kullanımını gösterebilecek ve istisna yönetiminin temellerini anlayabileceksiniz.

## 🤔 Yanlış Girdi ve Hata Mesajları

Hiç bir giriş alanına metin girmeniz gerekirken yanlışlıkla sayı girdiğiniz oldu mu? Çoğumuz ya hata sonucu ya da bir programı denerken bunu yapmışızdır, peki programı tamamlayıp sonlandırmak yerine neden bir hata mesajı verdiğini biliyor musunuz?

Hata mesajının görüntülenebilmesi için arka planda bir olay tetiklendi. Bu olay, program isim girişinde bir hesaplama yapmaya çalıştığı ve girdinin harfler değil sayılar içerdiğini fark ettiği için etkinleşti.

## 🛡️ İstisna Yakalayıcı ile Hataları Yönetmek

Bu kodu bir istisna yakalayıcı (exception handler) içine alarak, program bu tür bir hatayla nasıl başa çıkacağını bildi ve programla devam edebilmesi için hata mesajını çıktı olarak verebildi.

Bu, kullanıcı girdisi isterken oluşabilecek birçok hatadan yalnızca biridir; o halde istisna yönetiminin nasıl çalıştığına bakalım.

## 🔁 `try…except` Yapısı Nasıl Çalışır?

İlk olarak `try…except` ifadesini inceleyeceğiz. Bu tür bir ifade, önce `try` bloğundaki kodu çalıştırmaya çalışır, ancak bir hata oluşursa devre dışı kalır ve hatayla eşleşen istisnayı bulmak için aramaya başlar.

Doğru istisnayı bularak hatayı nasıl ele alacağını belirlediğinde, o satırdaki kodu yürütür.

Örneğin, bir dosyayı açıp ona yazacak bir program yazıyor olabilirsiniz. Programı çalıştırdıktan sonra, veriler okunamadığı için bir hata oluştu.

Bu hata nedeniyle program `try` ifadesinin altındaki kod satırlarını atladı ve doğrudan `except` satırına geçti. Bu hata `IOError` kapsamına girdiği için, konsolumuza “Unable to open or read the data in the file.” yazısını bastı.

## ➕ Birden Fazla `except` ve Belirsiz Hataların Sakıncaları

Basit programlar yazarken bazen yalnızca bir `except` ifadesiyle idare edebiliriz, peki ya `IOError` tarafından yakalanmayan başka bir hata oluşursa ne olur? Böyle bir durumda başka bir `except` ifadesi eklememiz gerekir.

Bu `except` ifadesi için, yakalanacak hata türünün belirtilmediğini fark edeceksiniz. Bu, program tüm hataları yakalasın ve sonlanmasın diye mantıklı bir adım gibi görünse de, en iyi uygulama değildir.

Örneğin, küçük programımızın bin satırdan uzun, çok daha büyük bir programın yalnızca bir bölümü olduğunu düşünelim. Görevimiz, kullanıcılar için kesintiye neden olan bir hata fırlatmaya devam eden programı hatadan arındırmaktı (debug).

Programı incelerken bu hatanın sürekli ortaya çıktığını gördünüz. Bu hata herhangi bir ayrıntı içermediği için, hatayı tespit edip düzeltmeye çalışırken saatlerinizi harcadınız.

## ✅ `else` ile Başarılı Çalışma Bildirimi

Şu ana kadar programımızda, bir hata oluşursa bir hata mesajının yazdırılması gerektiğini tanımladık, ancak programın düzgün bir şekilde çalıştığına dair hiçbir mesaj almıyoruz. İşte bu noktada bize bu bildirimi verecek bir `else` ifadesi ekleyebiliriz.

Bu `else` ifadesini ekleyerek, konsola “The file was written successfully.” şeklinde bir bildirim sağlanmış olur.

## 📌 `finally` ile Temizlik İşlemleri

Artık programımız başarılı bir şekilde çalışırsa ne olacağını ve bir hata oluşursa ne olacağını tanımladığımıza göre, eklenecek son bir ifade daha vardır.

Bu örnekte bir dosya açtığımız için yapmamız gereken son şey dosyayı kapatmaktır. Bir `finally` ifadesi ekleyerek, programın sonucu ne olursa olsun dosyayı kapatmasını ve konsolumuza “File is now closed” yazmasını söylemiş oluruz.

## 📚 Özet

Bu videoda, bir `try…except` ifadesinin nasıl yazılacağını, istisnalar oluştururken hataların her zaman tanımlanmasının neden önemli olduğunu ve nasıl `else` ve `finally` ifadeleri ekleyeceğinizi öğrendiniz.
