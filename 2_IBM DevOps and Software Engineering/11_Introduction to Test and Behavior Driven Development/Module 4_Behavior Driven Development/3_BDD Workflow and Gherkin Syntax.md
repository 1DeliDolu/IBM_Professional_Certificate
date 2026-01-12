# 🧩 BDD İş Akışı ve Gherkin Sözdizimi

Bu videoyu izledikten sonra, *davranış odaklı geliştirmenin* ( *behavior driven development – BDD* ) iş akışını özetleyebilecek ve Gherkin sözdiziminde  **Given** ,  **When** ,  **Then** , **And** ve **But** anahtar kelimelerinin nasıl kullanılacağını açıklayabileceksiniz.

## 🔄 BDD İş Akışını Adım Adım İnceleyelim

Önce geliştiriciler, test uzmanları ve paydaşlar problem alanını inceler; herkesin onu anladığından emin olmak için birlikte çalışırlar ve istedikleri davranışı açıklayan somut örnekler ya da senaryolar üretmek üzere iş birliği yaparlar. Bu örnekleri **Gherkin** sözdizimiyle dokümante edersiniz. Sonuç, inşa edeceğiniz sistemin davranışına dair bir spesifikasyondur.

Sonra ekip, **Behave** gibi bir BDD test çalıştırıcısı kullanarak bu spesifikasyondaki örnekleri otomatik test vakaları olarak çalıştırır. Behave, Gherkin sözdizimini ayrıştırır ve sistemin beklenildiği gibi davrandığını doğrulamak için kullanabileceği test adımlarını arar.

Behave ile bu örnekleri çalıştırmak size hangi test adımlarının eksik olduğunu söyler. “Sistemin davranışını kanıtlamak için yazmanız gereken test adımları şunlar.” diyen bir rapor alırsınız. Ardından bu adımları yazarsınız ve her şeyin çalışmasını sağlarsınız.

Ekip çözüm üzerinde çalışırken Behave, hangi örneklerin uygulanmış ve çalışır durumda olduğunu size söyler ve hangilerinin çalışmadığı konusunda sizi uyarır. Farkına bile varmadan, yazılımınız için hem spesifikasyon hem de test görevi gören tek bir dokümana sahip olursunuz. Bu doküman, sistemin tam olarak nasıl çalışması gerektiğini temsil eder.

Bu doküman, bir kütüphanede unutulmuş bir Word dosyası değildir; sonra dönüp baktığınızda sistemin artık öyle çalışmadığını, değişiklik yaptığınızı ve dokümantasyonu güncellemeyi unuttuğunuzu fark ettiğiniz türden bir şey değildir.

Bu, kaynak kontrol sisteminize eklenmiş yaşayan bir dokümandır ve ona karşı test vakaları çalıştırırsınız. Kimse bu dokümanı unutmaz çünkü test paketini her çalıştırdığınızda, doküman sistemin nasıl davranması gerektiğini doğrulamak için kullanılır.

Neredeyse dokümantasyonun sistemi sürüklediği bir durum gibidir; diğer türlü değil.

## 🧾 Örnekleri ve Senaryoları Yazmak İçin Kullandığınız Dil

Örnek ve senaryolarınızı yazmak için kullandığınız dilden bahsedelim. **Gherkin** sözdiziminde her örnek, adım ( *step* ) olarak anılan en az üç satırdan oluşur ve her adım bir anahtar kelimeyle başlamak zorundadır.

Gherkin sözdizimi, üç zorunlu anahtar kelime için yaygın olarak **Given, When, Then** şeklinde anılır. İlk anahtar kelimeyle başlayalım:  **Given** .

## 🧱 Given

 **Given** , bir dizi önkoşul ( *precondition* ) tanımlar. Bunlar, testleri yürütmek için sistemin gerekli duruma getirilmesini sağlayan koşullardır.

Örneğin bir e-ticaret uygulaması düşünün. Şöyle yazabilirim: “Given alışveriş sepetimde iki ürün var.” Bu, test sistemine devam etmeden önce sepetin içinde iki ürün olduğundan emin olmamız gerektiğini söyler.

## ⚡ When

Bir sonraki anahtar kelime  **When** ’dir.

 **When** , bir olay gerçekleştiğinde kullanılır. Bu olaylar, test edilen sistemle etkileşim kurmak için kullanıcının gerçekleştirdiği eylemlerdir.

Alışveriş sepeti örneğimizde şöyle olabilir: “When sepetimden bir ürünü çıkarırım.” Bu, test sistemine test altındaki sepetten bir ürün çıkarması gerektiğini söyler.

## ✅ Then

Son anahtar kelime  **Then** ’dir.

 **Then** , test edilebilir bir sonucun gözlemlendiğini ifade eder. Bu, kullanıcının gerçekleştirdiği eylemin beklenen sonucudur.

Yine alışveriş sepeti örneğini kullanarak şöyle yazabilirim: “Then alışveriş sepetimde yalnızca bir ürün kalmalı.” Bu adım, test sistemine When olayıyla gerçekten bir ürünün sepetten çıkarılıp çıkarılmadığını kontrol etmesini söyler.

## 🧷 Okunabilirliği Artırmak İçin And ve But

Okunabilirliği artırmak için **And** ve **But** anahtar kelimelerini de kullanabilirsiniz.

Bir dizi adımınız olduğunu ve her adımın aynı anahtar kelimeyle başladığını düşünün: “Given şu, Given bu, Given başka bir şey.” Bu, art arda üç Given demektir.

Bir seriyi daha okunabilir ve daha akıcı hale getirmek için, serideki ilk adımdan sonra tekrarlanan her anahtar kelimenin yerine **And** kullanabilirsiniz. Yani bu örnekte şöyle diyebilirsiniz: “Given şu, And bu, And başka bir şey.” Daha hoş okunur.

Şunu da yazabilirsiniz: “When bu olur, And şu olur,” veya “Then bu gözlemlenir, And şu gözlemlenir.”  **And** , her zaman kendisinden önce gelen Given, When ya da Then’in anlamını üstlenir.

Olmaması gereken durumları ifade eden adımlar için, anahtar kelimeyi And yerine **But** ile de değiştirebilirsiniz. Örneğin şöyle yazabilirsiniz: “But bu gözlemlenmez.” And hâlâ kullanılabilir, ancak But anahtar kelimesi okunabilirliği artırmak için ekstra bir seçenektir.

Gherkin sözdizimi bu kadar. **Given** bir önkoşul, **When** bir olay, **Then** test edilebilir bir sonuç gözlemlenir.

Birden fazla Given, When veya Then varsa, okumayı kolaylaştırmak için bunu **And** veya **But** ile değiştirebilirsiniz. Bu anahtar kelimelerle, sistemin beklenen ve gerçekleşen davranışını hem ifade edecek hem de test edecek cümleler oluşturabilirsiniz.

## 📌 Bu Videoda Öğrendikleriniz

BDD iş akışında, istenen davranışı tanımlamak için örnekler oluşturur, bu örnekleri otomatik testler olarak çalıştırır ve gerektiğinde ek testler yazarsınız. Bu iş akışı, yazılımınız için hem spesifikasyon hem de test görevi gören tek bir dokümana götürür.

Gherkin sözdiziminde bir örnek oluşturmak için, onu  **Given** ,  **When** ,  **Then** , **And** ve **But** anahtar kelimelerini kullanarak adımlara ayırırsınız.
