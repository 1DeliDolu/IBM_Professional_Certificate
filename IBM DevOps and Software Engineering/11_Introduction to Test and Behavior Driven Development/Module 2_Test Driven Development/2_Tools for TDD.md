# 🧰 TDD İçin Araçlar

Bu videoyu izledikten sonra şunları yapabileceksiniz: **test güdümlü geliştirme (TDD)** için popüler test araçlarını listelemek ve TDD için popüler **Python** test araçlarının özelliklerini özetlemek.

## 🧱 Birim Testlerinin Temeli

Birim testi, yazılım geliştirmenin temelidir. Geçmişte, yazılım geliştiricileri veya test uzmanları hataları bulmak için kodu manuel olarak test ederdi. Bu yaklaşım sürdürülebilir değildir.

Otomatik test, geliştiricileri manuel testten kurtarır ve **test güdümlü geliştirme** gibi tekniklerle test yazma biçimlerini değiştirir.

## 🧩 Popüler Test Çerçeveleri

Çeşitli programlama dilleri için birçok popüler test çerçevesi vardır. Muhtemelen hepsinin içinde en popüler olanı **xUnit serisi** olarak bilinen settir.

Bu seri şunları içerir:

* Java için **JUnit**
* Python için **PyUnit**
* .Net platformu için **NUnit**
* C ve C++ için **Embunit**

xUnit’in birden fazla dili desteklemesini gerçekten seviyorum. xUnit’in tüm sürümleri ortak bir söz dizimini paylaşır; bu yüzden bir dilde bir sürümünü öğrendiyseniz diğerlerini öğrenmek çok daha kolaydır. Bu erişilebilirlik xUnit’i çok popüler yapar.

Diğer dikkat çekici test çerçeveleri arasında JavaScript için  **Jasmine** , Node.js için  **Mocha** , PHP için **SimpleTest** ve daha birçokları vardır. Mesaj şudur: Kullandığınız dil için bir test çerçevesi aramalı ve onu öğrenmelisiniz.

Bu size çok zaman kazandıracaktır çünkü her biri kodunuzu düzgün şekilde test etmeniz için ihtiyacınız olan araçları sağlar.

## 🐍 Python İçin Popüler Test Çerçeveleri

Şimdi Python’daki popüler test çerçevelerinden bazılarına bakalım.

### 🧪 PyUnit

İlki  **PyUnit** ’tir; **unittest** paketi olarak da bilinir. xUnit ailesinden gelir ve bu kursta öğreneceğimiz araç budur.

PyUnit’i sevmemin ana nedeni, Python’un içine gömülü olmasıdır; her zaman orada olacağına güvenebilirsiniz. Ayrıca daha fazla Python geliştiricisi yerleşik yeteneklere aşina olacaktır; bu da onu bilen bir Python geliştiricisi bulmayı kolaylaştırır. PyUnit, Python testleri için en popüler iki çerçeveden biridir.

### ✅ Pytest

Diğeri  **Pytest** ’tir. Diğer Python test çerçevelerinde, birden fazla seviyede *setup* ve *teardown* kullanabilirsiniz. *Setup* ve  *teardown* , her testten önce ve sonra çalıştırılacak talimatları tanımlamanıza izin veren iki Python yöntemidir.

Ancak Pytest’te neredeyse sonsuz sayıda *setup* ve *teardown* seviyesi olabilir. Bununla birlikte, bu seviyelerin çok fazla kullanılması bazen oldukça yapılandırmasız hale gelebilir ve birim testlerini okumayı zorlaştırabilir.

Bu nedenle Pytest’i kullanmamamın ana sebebi şudur: PyUnit ihtiyacım olan her şeyi yapıyor ve Python’un içine gömülü; o halde neden başka bir kütüphaneyi ön koşul olarak ekleyeyim?

### 📝 Doctest

Bir diğer araç  **Doctest** ’tir. Bu araç testlerinizi kodunuzun  *docstring* ’lerinde veya yorumlarında yazmanıza olanak tanır. Basit şeyler için idare eder, ancak sınırlıdır ve karmaşık ve yüksek derecede etkileşimli kod için gerçekten ölçeklenmez.

### 💎 RSpec

Bir de **RSpec** vardır; Ruby için son derece popüler bir çerçevedir ve Python’da da mevcuttur. Ben TDD’yi Ruby on Rails kodu yazarken öğrenmiştim; bu yüzden çok fazla RSpec kodu yazdım ve sözdiziminin Python tarafından da desteklenmesine sevindim. Eğer RSpec’e aşinaysanız, bu sizin için kötü bir seçim olmayabilir.

## 🧪 Python’da Diğer Önemli Test Araçları

### 🏃 Nose

**Nose** bir test çalıştırıcısıdır. PyUnit’in kendi test çalıştırıcısı olsa da Nose, renk ve biçimlendirme ile diğer test çıktısı özelliklerini eklemenize olanak tanır. Gerçekten **Red/Green/Refactor** çıktısını görürsünüz.

Satırlar gerçekten kırmızıya döner; PyUnit’te ise her şey sadece siyah-beyazdır ya da terminalinizin renk şemasına bağlıdır. Nose’u seviyorum çünkü çıktıyı okumayı kolaylaştırıyor.

Nose ayrıca **coverage** aracını çağırma yeteneğine sahiptir.

### 📊 Coverage

Bu araç **kod kapsamını (code coverage)** destekler; bu, otomatik testleri çalıştırdığınızda yürütülen kod yüzdesidir. Bu özelliği özellikle seviyorum çünkü her test vakasını çalıştırdığımda bir kod kapsam raporu alıyorum.

Bu rapordan, kapsamımın artıp artmadığını, azalıp azalmadığını veya aynı kaldığını görebilirim. Coverage aracı ayrıca bir test çalıştırması sırasında yürütülmemiş kod satırlarını raporlamak için seçeneklere sahiptir. Bu raporu, eksik satırları bulmak ve daha fazla test vakasını nereye yazmanız gerektiğini bilmek için kullanabilirsiniz.

Laboratuvarlarda  **PyUnit** , **Nose** ve **coverage** kullanacağız. Böylece tüm kodunuzu kapsayan bir test paketi oluşturmanıza yardımcı olacak eksiksiz bir araç setine sahip olacaksınız.

## ✅ Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* **xUnit serisi** , TDD için en popüler test çerçevelerinden biridir.
* Python için en popüler iki test çerçevesi **PyUnit** ve  **Pytest** ’tir.
* Python için diğer iki popüler test çerçevesi **Doctest** ve  **RSpec** ’tir.
* **Nose** , test çıktısına renk ekleyebilen ve ardından kod kapsam aracını çağırabilen bir Python test çalıştırıcısıdır.
