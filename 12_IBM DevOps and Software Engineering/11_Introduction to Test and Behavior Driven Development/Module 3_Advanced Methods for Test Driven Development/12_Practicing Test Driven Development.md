# 🧪 Test Odaklı Geliştirme Uygulaması

Bu videoyu izledikten sonra şunları yapabileceksiniz: Test Odaklı Geliştirme (TDD) iş akışını uygulamak ve bir TDD iş akışının nasıl daha iyi koda yol açtığını açıklamak.

Test etme teknikleri hakkında, özellikle de test odaklı geliştirme hakkında çok konuştuk. Ama şimdi bunları pratiğe dökme zamanı. Ancak önce, bir TDD iş akışındaki üç adımı gözden geçirelim ve bunun neden geliştirme için bu kadar değerli olduğu hakkında daha fazla konuşalım.

TDD’de önce sahip olmayı dilediğiniz kod için bir test senaryosu yazarsınız. Kodu yazarak başlamazsınız. Önce test senaryolarını yazarsınız.

İkinci olarak, o test senaryosunun geçmesini sağlayacak kodu yazarsınız.

Üçüncü olarak da, test senaryolarının kodun davranışını değiştirip değiştirmediğinizi size bildireceğini bilerek, kodu daha sağlam hale getirmek için yeniden düzenlersiniz (refactor). Son olarak, süreci tekrarlarsınız.

Bu iş akışının tamamı **Kırmızı, Yeşil, Refactor** iş akışı olarak bilinir. Test senaryoları başlangıçta kırmızıdır çünkü çalıştırılacak bir kod yoktur. Sonra onları yeşile çevirmek için kodu yazarsınız. Ve son olarak, test senaryosunun davranışı değiştirirseniz sizi uyaracağını bilerek, o kodu daha sağlam hale getirmek için refactor edersiniz.

Şu senaryoyu hayal edin.

Birden fazla sayacı takip edebilen bir web servisi oluşturmanız istendi. Bu sayaçlar, bir web sayfasındaki hit sayaçları gibidir. Bu nedenle API’nin *RESTful* olması gerektiği söylendi. Bu, servisi oluşturmak için kullanacağınız davranış ve HTTP fiilleri hakkında size biraz bilgi verir. RESTful yönergeleri takip etmelidir.

Uç noktanın `/counters` olarak adlandırılması gerekir. Bunu bilmek ve RESTful olması gerektiği gerçeği, uç noktayı nasıl çağırmanız gerektiği konusunda size çok fazla bilgi verir.

Ayrıca, bir sayaç oluştururken adını çağrının yolunda (path) belirtmeniz gerektiği söylendi. Dolayısıyla çağrı `/counters/` ve ardından sayacın adı şeklinde olacaktır.

Son gereksinim, yinelenen adların bir hata kodu döndürmesi gerektiğini belirtir. RESTful bir serviste HTTP çakışması (conflict) için hata kodları  **429 Conflict** ’tir.

Bu gereksinimler verildiğinde, `/counters` üzerinde POST çağırarak ve sonuna “shoes” gibi bir ad ekleyerek bir sayaç oluşturan bir test senaryosu yazmaya başlayabiliriz.

API RESTful olmak zorunda olduğundan, RESTful yönergeleri doğrultusunda **201_CREATED** dönüş kodu almamız gerektiğini biliriz. Ayrıca, adın doğru oluşturulduğunu ve değerinin başlangıçta sıfırdan başladığını kontrol edebilmek için sayacı geri almamız gerekir.

Tek bir satır uygulama kodu yazmadan bir sayaç oluşturmak için bir test senaryosu yazabiliriz. Elbette testi çalıştırsak başarısız olurdu, ama en azından kodun nasıl davranması gerektiğini tanımlamış oluruz; böylece artık test senaryosunun geçmesini sağlayacak kodu yazabiliriz.

Ayrıca yinelenen sayaçların **429 Conflict** döndürmesi gerektiği yönünde bir gereksinimimiz vardı. Bir kez daha, bir sayaç oluşturmak için ona bir ad vererek POST isteği yapabiliriz ve yine dönüş değerinin **201_CREATED** olduğunu kontrol edebiliriz.

Sonra aynı sayaç adını tekrar oluşturmak için aynı isteği yapabiliriz. Ancak bu sefer, **429 Conflict** dönüş kodu aldığımızı kontrol ederiz. Eğer alamazsak, kodun beklendiği gibi davranmadığını biliriz.

Bu iki test senaryosu da uygulama kodu yazmadan önce kolayca yazıldı; çünkü kodun belirtilen gereksinimlere uymasını doğrulayabildik.

TDD ile ilgili hatırlanması gereken en önemli nokta şudur: TDD’de test senaryolarınız geliştirmeyi yönlendirir. Test senaryolarınızı uygulamanızın gereksinimlerine dayandırırsınız. Gereksinimler, uygulamanın nasıl davranması gerektiğini tarif eder ve test senaryoları da uygulamanın gerçekten o şekilde davranıp davranmadığını doğrular.

Bunların herhangi birini belirtmek için uygulama koduna ihtiyacınız yoktur. Test senaryolarını yazdıktan sonra, test senaryolarının geçmesini sağlayacak kodu yazarsınız.

Ve kod yazmak daha kolaydır, çünkü nasıl davranması gerektiğini zaten bilirsiniz. Örneğin, hangi dönüş kodlarının olması gerektiğine zaten karar vermiş olursunuz. Bu yüzden, test senaryolarını yazdıktan sonra TDD kodlamayı daha hızlı hale getirir.

Ve kendinizi kandırmayın; kodu önce yazsaydınız bile muhtemelen onu test etmek için küçük bir program yazardınız. Neden o programı en baştan resmi bir test senaryosu haline getirmeyesiniz? Böylece, her yeni geliştirmede kodunuzun çalışmaya devam ettiğini bilirsiniz.

Bir diğer önemli çıkarım da şudur: TDD iş akışı, gidip gelmeli (back-and-forth) bir süreçtir. Bir test senaryosu yazarsınız, sonra kodu yazarsınız.

Farklı girdileri veya etkilenen davranışları kontrol etmek için daha fazla test senaryosu yazarsınız ve sonra daha fazla kod yazarsınız. Ve böyle devam eder.

Bu iş akışını bundan sonra, tüm geliştirmelerinizde kullanmalısınız.

Bu videoda şunları öğrendiniz: TDD iş akışında, kodu yazmadan önce test senaryolarını yazarsınız. Önce test senaryolarını yazmak, kodu yazmadan önce kodun nasıl davranması gerektiğine odaklanmanızı sağlar. TDD daha yüksek kod kalitesi sağlar.
