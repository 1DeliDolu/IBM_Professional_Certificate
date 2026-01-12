# 🎭 What is Behavior Driven Development?

Bu videoyu izledikten sonra, *davranış odaklı geliştirme* ( *behavior driven development – BDD* )’nin ne olduğunu açıklayabilecek ve yazılım test sürecinin hangi seviyelerinde BDD uygulanmasının uygun olduğunu belirleyebileceksiniz.

Adından da anlaşılacağı gibi, *davranış odaklı geliştirme* ya da  *BDD* , sistemin dışarıdan gözlemlenen davranışına odaklanır. *Test güdümlü geliştirme* ( *test driven development – TDD* ) gibi sistemin iç işleyişiyle ilgilenmez. Sistemin bir kullanıcısı gibi, sistemin nasıl davrandığını gözlemler. Bu, BDD’yi tüm bileşenlerin birlikte nasıl davrandığını görmek için entegrasyon testlerinde harika kılar. Sizi “dışarıdan içeriye” düşünmeye zorlar. Başka bir deyişle, iş sonuçlarına en doğrudan katkı sağlayan davranışları uygularsınız.

BDD’nin bir avantajı, alan uzmanlarının, test uzmanlarının, geliştiricilerin ve müşterilerin kolayca anlayabileceği tek bir söz dizimiyle davranışları tanımlamasıdır. Bu, ekip genelinde iletişimi geliştirir.

## 🆚 BDD ile TDD Arasındaki Fark

BDD’nin TDD’den nasıl farklı olduğuna bakalım. TDD’de, sistemi içten dışa ya da aşağıdan yukarıya doğru test edersiniz. Fonksiyonların iç işleyişini test eder.

TDD için, çağrıyı önemsersiniz:

* Doğru dönüş kodunu aldı mı?
* Doğru veriyi doğru formatta geri getirdi mi?
* Ve benzeri.

TDD’yi birim test ( *unit testing* ) için kullanırız.

TDD gibi, BDD de geliştirme için *önce test* ( *test-first* ) yaklaşımıdır. Ancak BDD daha üst seviyede bir test yaklaşımıdır. Sistemin davranışını dışarıdan içeriye doğru test eder ve sistemin nasıl davranması gerektiğini dikkate alır. TDD gibi sistemin iç işleyişiyle ilgilenmez.

## 🛒 BDD’ye Örnek

BDD’de, sistemi bir kullanıcının deneyimleyeceği şekilde gözlemlersiniz.

Örneğin, çevrimiçi bir şeyler sipariş ederken kullandığınız sanal alışveriş sepetini düşünün. BDD için şöyle sorabilirsiniz:

* “Alışveriş sepetime bir şey eklediğimde, alışveriş sepetimde görünüyor mu?”

Hangi API’nin çağrıldığını umursamam ve arka planda hangi verinin aktarıldığını da umursamam. Sadece alışveriş sepetimde görünmesini beklediğim şeyin gerçekten görünmesini önemserim.

Aynı şekilde, sepetinizden bir şey kaldırdığınızda, gözlemlenen davranış öğenin artık sepetinizde görünmemesi olmalıdır. Yine, bunu sağlayan arka plandaki API çağrılarıyla ilgilenmezsiniz.

Sistemin dışa dönük davranışıyla ilgilenirsiniz. Yani, “sepetten kaldır” etiketli düğmeye tıkladığınızda, öğenin sepetten kaldırılmasını ve dolayısıyla artık orada bulunmamasını beklersiniz.

## 🧪 Yazılım Test Sürecinde BDD Nerede Uygulanır?

BDD’nin süreçte nereye oturduğunu görmek için yazılım test sürecini kısaca gözden geçirelim.

### 🔹 Unit Testing

Bu seviyede, bir yazılım sisteminin tek tek birimlerini veya bileşenlerini test edersiniz. Amaç, her birimin tasarlandığı gibi çalıştığını doğrulamaktır.

### 🔹 Integration Testing

Bu seviyede, bireysel birimleri birleştirip grup olarak test edersiniz. Amaç, birimler arasındaki etkileşimlerdeki hataları ortaya çıkarmaktır.

### 🔹 System Testing

Bu seviyede, tüm sistemi uçtan uca test edersiniz. Amaç, sistemin belirtilen üst düzey gereksinimlerle uyumunu değerlendirmek ve tüm sistemin birlikte çalıştığından emin olmaktır.

### 🔹 User Acceptance Testing

Bu seviyede, kullanıcı sistemi kabul edilebilirlik açısından test eder.

## 📍 BDD Süreçte Nereye Denk Gelir?

Peki BDD süreçte nereye oturur?

Genellikle BDD’yi  *entegrasyon* , *sistem* veya *kabul (acceptance)* test seviyelerinde uygularsınız. Bu seviyelerde, davranışı değerlendirebilmek için sistemin yeterli kısmı çalışır durumda olur.

## ✅ Özet

Bu videoda şunları öğrendiniz:

* BDD’de, sistemin davranışını *dışarıdan içeriye* doğru test edersiniz.
* BDD, sistemin amaçlandığı şekilde davrandığından emin olmayı sağlar.
* Yazılım test sürecinde BDD için uygun seviyeler:  *entegrasyon testi* , *sistem testi* ve *kullanıcı kabul testi*dir.
