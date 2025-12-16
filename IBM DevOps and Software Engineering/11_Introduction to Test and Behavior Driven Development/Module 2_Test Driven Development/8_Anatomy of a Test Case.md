# 🧪 Test Vakası Anatomisi

Bu videoyu izledikten sonra şunları yapabileceksiniz: test  *fixture* ’larının test etmedeki rolünü özetlemek, test çerçevelerinin geliştiricilere *assertion* oluşturma konusunda nasıl yardımcı olduğunu tartışmak ve test vakalarının nasıl yapılandırılacağını açıklamak.

Bir örnek test vakasına bakalım. Bu örnekte, *stack* olarak bilinen yaygın bir programlama yapısını kullanacağız. Öncelikle bir  *stack* ’in ne olduğunu ve nasıl çalıştığını anlamanız gerekir.

Bir  *stack* , son giren ilk çıkar (*last-in, first-out* ya da  *LIFO* ) davranışını uygulayan bir veri yapısıdır. Bu şu anlama gelir: stack’e bir şey eklediğinizde en üste yerleştirilir ve bir şey çıkardığınızda da üstten çıkarılır. Yani en son eklenen öğe, ilk çıkarılan öğedir.

Bir  *stack* ’i içine tenis topları yerleştirilmiş bir tüp gibi düşünebilirsiniz. En alttaki tenis topunu, önce en üstteki tenis topunu çıkarmadan alamazsınız.

Bu örnekte, bu stack’e birisi zaten A ve B eklemiş. Stack’e bir öğe ekleme ya da bir öğeyi “itme” komutuna *push* denir. Bu örnekte, C öğesi stack’e yeni *push* edilmiştir.

Ayrıca *peek* komutunu da kullanabilirsiniz.  *Peek* , stack’teki öğeyi çıkarmadan, en üstteki öğeye bakar. Bu örnekte *peek* C döndürür, çünkü C şu anda stack’in en üstündedir.

Stack’ten bir şeyi çıkarmaya yarayan komut *pop* olarak adlandırılır. Bu örnekte olduğu gibi *pop* çağırdığınızda, C’yi kaldırır ve stack’ten değer olarak C’yi döndürür.  *Peek* ’i tekrar kullanırsanız, bu kez *peek* B döndürür; çünkü artık B stack’in en üstündedir.

Bir stack uygulamasında olan biten budur. Üç fonksiyon:  *push* , *pop* ve  *peek* .

---

## 🧰 Stack’in Doğru Çalıştığını Test Etmek

Stack’imizin doğru çalışıp çalışmadığını görmek için bazı test vakaları yazalım. İlk olarak *push* fonksiyonunu test edeceğiz.

Önce, Python’daki *unittest* paketinden *TestCase* sınıfını içe aktararak başlarım. Bu sınıfı tüm testler için üst sınıf (parent class) olarak kullanacağım; böylece birazdan göreceğimiz temel test işlevlerini miras alacaktır.

Sonra kendi *Stack* sınıfımı içe aktarırım. Onu *stack.py* adlı bir modüle koydum, bu yüzden o modülden içe aktarmalıyım.

Test vakalarımı yazmaya,  *unittest* ’ten içe aktardığımız  *TestCase* ’in bir alt sınıfı olan bir sınıf tanımlayarak başlarım. Bu sınıfa *StackTestCase* adını verdim. Birazdan göreceğimiz gibi her test, bu sınıfın bir metodu olacaktır.

---

## 🧩 Test Fixture’ları: Setup ve Teardown

Sonrasında iki test  *fixture* ’ı tanımlıyorum. Test  *fixture* ’larını başka bir derste daha ayrıntılı tartışacağız; ama şimdilik bilin ki test  *fixture* ’ı, bir test vakası çalıştırılmadan önce sistemin başlangıç durumunu belirlemenizi sağlar.

İki test  *fixture* ’ı kullanıyoruz: *setup* ve  *teardown* . Bunlar sırasıyla her testten önce ve sonra çalışır.

 *Setup* , `self.stack` adlı bir örnek değişkeni (instance variable) tanımlar ve ona yeni bir stack atar. Bu, test edeceğimiz stack olacaktır.

*Teardown* ise `self.stack`’i `None` yapar; böylece yeniden kullanılmadığından emin oluruz, çünkü yeniden kullanım yan etkilere ( *side effects* ) neden olabilir.

Artık ilk test vakamızı yazmaya hazırız.

---

## ✅ Test Vakası: `test_push`

Bir metot tanımlar ve adını `test_push` koyarız. `test` kelimesiyle başlayan her metot bir test vakası olarak kabul edilir. Diğer tüm metotlar görmezden gelinir.

Bu test vakasında, *push* fonksiyonunun beklendiği gibi çalışıp çalışmadığını test edeceğiz. Dosyayı kaydedip test vakasını çalıştırırız.

Test vakası çalıştığında, önce *setup* çalışır; yeni bir stack oluşturur ve onu `self.stack` örnek değişkenine atar. Unutmayın, *setup* her testten önce çalışır.

Ardından `self.stack.push` çalışır ve stack’e dokuz sayısını *push* etmek için 9 değerini parametre olarak gönderir. Bunun stack üzerindeki etkisine dikkat edin. Dokuz, stack’in en üstüne *push* edilmiştir.

Sonraki satırda bir *assertion* çalıştırılır. Bu, karşılaştığımız ilk  *assertion* ’dır. Bu metot nereden geldi? Önündeki `self` bize bir ipucu verir. Bu metot, üst sınıf olan  *TestCase* ’ten gelmiştir. Bu yüzden  *TestCase* ’i alt sınıflayarak ( *subclassing* ) assertion yapmak için kullanabileceğimiz bir dizi metodu miras alıyoruz.

Bu metot, iki argümanla kendisine verilen değerlerin eşit olduğunu doğrular. Bu örnekte, stack’in en üstüne *peek* attığımızda 9 döneceğini doğruluyoruz. Örnekte de görüyoruz ki 9 gerçekten en üsttedir; dolayısıyla bu *assertion* doğrudur. Test geçebilir.

Son olarak *teardown* metodu çağrılır. `self.stack` örnek değişkeni `None` yapılır ve stack ortadan kalkar. Unutmayın, *teardown* her test vakasından sonra çağrılır.

Bu, ilk test vakamızdı.

![1765918628917](image/8_AnatomyofaTestCase/1765918628917.png)

---

## ✅ Test Vakası: `test_pop`

Şimdi bir test vakası daha yazalım; bu sefer *pop* fonksiyonu için. Başka bir metot oluşturur ve adını `test_pop` koyarız. Test vakasını kaydedelim ve nasıl çalıştığını izleyelim.

Beklendiği gibi, testi çalıştırdığımızda ilk adım olarak *setup* çağrılır; yeni bir stack oluşturur ve onu `self.stack` örnek değişkenine atar.

Ardından `self.stack.push` çalışır ve stack’e 9 sayısını *push* etmek için 9 değerini geçirir.

Bunu yapıyoruz çünkü önce stack’e bir şey *push* etmeden  *pop* ’u test edemeyiz. Pop edilecek bir şeye ihtiyacımız var.

Sonra eşitlik  *assertion* ’ını tekrar görürüz. Bu kez ilk parametre olarak `self.stack.pop` fonksiyonunu veriyoruz; bu fonksiyon stack’in en üstündeki öğeyi döndürecektir. İkinci parametre olarak ise 9 sayısını veriyoruz; pop’un döndürdüğü değerle eşit olmasını umuyoruz.

O satır çalıştığında 9 stack’ten *pop* edilir ve  *assertion* ’a döndürülür. *Assertion* dönen değeri 9 ile karşılaştırır ve eşit olduklarını doğrular; böylece satır geçer.

Bir *assertion* daha yaparız. Bu sefer `assertTrue` metodunu kullanırız ve `is_empty` metodunun çağrıldığında `True` döndüreceğini doğrularız. Stack gerçekten boştur, dolayısıyla `is_empty` `True` döndürür ve *assertion* geçer.

Son olarak *teardown* metodu çağrılır. Bir kez daha `self.stack` örnek değişkeni `None` yapılır ve stack ortadan kalkar.

![1765918656317](image/8_AnatomyofaTestCase/1765918656317.png)

---

## 🧾 Özet

Test vakası yazmak bu kadar.  *TestCase* ’ten türeyen ( *subclass* ) bir sınıf oluşturursunuz. İsteğe bağlı olarak her testi kurmak ve temizlemek için birkaç test  *fixture* ’ı eklersiniz. Sonrasında, test etmek istediğiniz kodu kullanarak tek tek testlerinizi yazarsınız ve beklediğiniz gibi çalıştığını ya da çalışmadığını doğrulayan  *assertion* ’lar eklersiniz.

Bu videoda, test  *fixture* ’larının geliştiricilere bir başlangıç test durumu oluşturma konusunda yardımcı olduğunu öğrendiniz. Test çerçevelerinin test koşullarını basitleştiren araçlar sağladığını ve test vakalarının kodun beklendiği gibi davrandığını doğrulayan  *assertion* ’lar içerdiğini öğrendiniz.
