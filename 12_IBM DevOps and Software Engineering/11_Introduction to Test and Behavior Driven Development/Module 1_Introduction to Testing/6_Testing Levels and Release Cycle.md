# 🧪 Testing Seviyeleri ve Yayın Döngüsü

Bu videoyu izledikten sonra, yazılım test sürecinin her seviyesini açıklayabilecek ve geleneksel yayın döngüsünün her aşamasını özetleyebileceksiniz. Yazılım testinin çeşitli seviyelerini size tanıtmak istiyorum. Her seviyenin kapsamı farklıdır, bu yüzden farklı testler çalıştırılır.

---

## 🧩 Unit Testing

En alt seviyede *unit testing* vardır. Bu seviyede, yazılım test sürecinde bir yazılım sisteminin tekil  *unit* ’lerini veya bileşenlerini test edersiniz. Bu testlerin amacı, her bir birimin tasarlandığı şekilde çalıştığını doğrulamaktır. Bu, tek bir geliştiricinin kendi tek modülünde yaptığı şeydir.  *Unit testing* ’in amacı, “modülüm çalışıyor mu?” sorusunu belirlemektir.

Bu seviyede, modülün içinde neler olup bittiğinin tamamen farkındasınızdır ve hem *happy path* hem de *sad path* dediğimiz durumları test etmek istersiniz.  *Happy path* ’ler, iyi veri verdiğinizde her şeyin beklendiği gibi çalıştığı yollardır.  *Sad path* ’ler ise kötü veri verdiğinizde veya alternatif yolları tetikleyen veriler verdiğinizde oluşur. Bunu, yolların doğru çalıştığından ve hataları yakaladığınızdan emin olmak için yaparsınız.

Dolayısıyla modülde bir `if then else` ifadesi olduğunu biliyorsanız, `if` yolunu test eden ve `else` yolunu test eden bir test senaryosu yazarsınız. Modülde *exceptions* yakalamaya yönelik kod varsa,  *exception* ’a sebep olacak bir test senaryosu yazdığınızdan emin olmak istersiniz; böylece  *exception handler* ’ların doğru çalıştığını test edebilirsiniz.

 *Unit testing* , modülün nasıl çalıştığına dair yakın bir bilgi gerektirir. Çeşitli girdiler verirsiniz ve doğru çıktılar beklersiniz. *Continuous integration* ile aşinaysanız, bunlar kodunuzu entegre ettiğinizde CI sunucusunda çalışan testlerdir ve bir şeyi bozup bozmadığınızı size söyler. Bu, *test driven development* uyguladığınız seviyedir.

---

## 🔗 Integration Testing

Bir sonraki seviye  *integration testing* ’dir. Bu seviyede, yazılım test sürecinde tekil birimleri birleştirir ve onları bir grup olarak test edersiniz. Bu testin amacı, entegre edilmiş birimler arasındaki etkileşimdeki kusurları ortaya çıkarmaktır.

Bu seviyede, birkaç modülü birlikte çalışıp çalışmadıklarını görmek için test edersiniz ve çeşitli girdilerle nasıl davrandıklarını incelersiniz. Muhtemelen bu modüllerin iç işleyişi hakkında,  *unit testing* ’de olduğu gibi bir şey bilmiyorsunuzdur, ama bu iyi bir şeydir.

Modüller tek başlarına doğru çalışmış olabilir, ancak birbirleriyle doğru konuşmuyor olabilirler. Birbirlerinin API’lerini doğru mu çağırıyorlar? Bu, *behavior driven development* uyguladığınız seviyedir. Sistemi oluşturan birkaç modülün davranışını birlikte test edersiniz.

---

## 🧱 System Testing

Bir sonraki seviye  *system testing* ’dir. Bu seviyede, tüm yazılım süreci test edilir. Tamamen entegre edilmiş bir sistemi test edersiniz. Bunun amacı, sistemin belirli gereksinimlerle uyumluluğunu değerlendirmek ve tüm sistemin birlikte çalıştığından emin olmaktır.

Bu, tüm sistemi bir araya getirdiğiniz seviyedir.  *Integration testing* ’de muhtemelen hâlâ bir geliştirme ortamındasınızdır. Ancak  *system testing* ’de büyük olasılıkla üretime daha çok benzeyen bir *staging* veya *pre-production* ortamına geçersiniz. Ve tüm sistemin birlikte çalıştığından emin olursunuz.

---

## ✅ User Acceptance Testing

Son olarak *user acceptance testing* vardır. Bu seviyede, yazılım test sürecinde sistemin kabul edilebilirliği test edilir. Bu testin amacı, sistemin iş gereksinimleriyle uyumluluğunu değerlendirmek ve teslim için kabul edilebilir olup olmadığını belirlemektir.

Bu test genellikle son kullanıcı tarafından, “evet, sistemi kabul ediyorum” diyebilmeleri için yapılır. Bu test genellikle *system testing* ortamıyla aynı ortamda veya benzer bir ortamda gerçekleştirilir. Yalnızca kullanıcıların erişebildiği özel bir ortam da olabilir.

![1765914374401](image/6_TestingLevelsandReleaseCycle/1765914374401.png)

---

## 🏗️ Yayın Döngüsü Boyunca Ortamlar

Ortamlar hakkında konuşmuşken, yayın döngüsü boyunca çeşitli ortamlara bakalım. Farklı ortamlardan bahsettim: bir  *development environment* , bir  *testing environment* , bazen *pre-production* olarak adlandırılan bir *staging environment* ve bir  *production environment* .

Bu akış şeması, yayın döngüsünün her aşamasında kullanılan çeşitli ortamları ve her aşamada yapılan testleri gösterir. En soldaki  *development environment* , geliştiricilerin *unit testing* yaptıkları ve kodlarını Git gibi bir kaynak kod yönetim sisteminde sakladıkları yerdir.

Kod artefaktlarını derlemek ve daha fazla *unit testing* yapmak için genellikle bir *build environment* bulunur. Bu artefaktlar bir kez oluşturulduktan sonra, bir *package repository* içinde saklanabilirler. Java `jar` dosyalarınızın, Python  *wheels* ’larınızın, Docker  *images* ’larınızın saklanacağı yer burasıdır.

Sonraki adım, bu oluşturulmuş artefaktları alıp `test`, `stage` ve `prod` ortamlarına deploy ettiğiniz tüm  *testing environments* ’lardır. Her ortam, giderek daha fazla  *production* ’a benzer hâle gelir.

Böylece  *integration testing* , performans testi, uyumluluk testi,  *system testing* , *acceptance testing* gibi şeyleri yapabilirsiniz; bunlar daha küçük geliştirme sunucularında gerçekten yapılamaz. Üretime doğru ilerledikçe daha fazla ve daha ileri seviye test yapabilirsiniz.

Yayın döngüleri bu ortamların daha fazlasına veya daha azına sahip olabilir, ancak tipik bir yayın döngüsünde en yaygın bulacağınız ortamlar bunlardır.

![1765914396820](image/6_TestingLevelsandReleaseCycle/1765914396820.png)

---

## 🧾 Özet

Bu videoda şunları öğrendiniz: Yazılım test süreci dört seviye içerir:  *unit* ,  *integration* ,  *system* ,  *acceptance* . Yaptığınız test seviyesi, geleneksel yayın döngüsünün aşamalarına göre değişir.

 *Unit testing* , geliştirme ve build aşamasında gerçekleşir.  *Integration* , *system* ve *acceptance testing* ise test, stage ve prod aşamalarında gerçekleşir.
