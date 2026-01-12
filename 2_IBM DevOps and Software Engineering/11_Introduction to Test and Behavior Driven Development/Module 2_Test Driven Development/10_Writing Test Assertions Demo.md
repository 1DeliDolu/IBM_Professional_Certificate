# 🧪 Writing Test Assertions Demo

Bu laboratuvara, **test assertion yazma** konusuna hoş geldiniz. Burada size düşünce sürecimi, test case yazmaya ve assertion’lar oluşturmaya nasıl yaklaştığımı göstermek istiyorum. Böylece benim kullandığım iş akışını öğrenebilirsiniz.

## 🧰 Test Ortamıyla Başlangıç

Test ortamında başlayacağız. Laboratuvarda yapacağınız bazı başlangıç ayarları olacak; ben bunları zaten yaptım. Ancak herhangi bir kod yazmadan önce yapmamız gereken ilk şey, **nose testlerini çalıştırmak** ve hangi testlerin çalıştığını, hangilerinin çalışmadığını görmek.

Komut satırına şunu yazıyorum:

```bash
nosetests
```

Enter’a basıyorum ve… vay canına, hiçbir şey çalışmıyor! Üç testin tamamı başarısız. Bunun sebebi, testlere baktığınızda göreceğiniz gibi, bu üç testin de sadece exception fırlatıyor olması.

## 📂 Test Kodlarını İnceleme

Geliştirme ortamına geçelim. İkinci laboratuvara gidiyoruz ve `test_stack.py` dosyasına bakıyoruz. Bunlar testler ve her biri yalnızca bir exception fırlatıyor.

Testleri yazmadan önce,  **test ettiğimiz kodu anlamamız gerekiyor** . Aslında `stack.py` sınıfını test ediyoruz. Bu sınıfta dört fonksiyon var:

* `push`
* `pop`
* `peek`
* `is_empty`

Test etmek istediğimiz dört fonksiyon bunlar. Tüm çalışmamızı `test_stack.py` dosyasında yapacağız.

## ▶️ Testleri Çalıştırma ve `--stop` Parametresi

Testleri tekrar çalıştıracağım. Yine `nosetests` yazıyorum ama bu sefer bir parametre ekliyorum:

```bash
nosetests --stop
```

Bu parametre, ilk hatada testlerin durmasını sağlar.

Burada önemli bir noktaya dikkat edin: Testleri ilk çalıştırdığımda sırasıyla şunlar çalıştı:

* Test that the stack is empty
* Test peek
* Test pop
* Test pushing

Ancak dosyada yazılı sıraları farklı:

* test pushing
* test popping
* test peeking
* test if empty

Yani testler  **yazıldıkları sırada çalışmaz** . Rastgele bir sırayla çalışırlar. Bunun sebebi, testlerin birbirine bağımlı olmamasını ve her birinin **atomik** olmasını sağlamaktır.

## 🟢 İlk Test: Stack Boş mu?

`nosetests --stop` çalıştırıldığında ilk hata “Test if the stack is empty” testinde oluştu. Şimdi onu düzeltelim.

Bu testin koduna baktığımızda sadece “exception not implemented” fırlattığını görüyoruz. Peki stack’in boş olup olmadığını nasıl test ederiz?

Test fixture’lara bakarsak şunu görürüz:

* `setup` → yeni bir stack oluşturur
* `teardown` → stack’i siler (None yapar)

Yani stack **başlangıçta boş** olmalıdır. Bu ilk assertion’ımız olabilir.

```python
self.assertTrue(self.stack.is_empty())
```

Bunu yazdıktan sonra tekrar çalıştırıyorum:

```bash
nosetests --stop
```

Artık bu test geçiyor.

### 🔎 Testi Daha Sağlam Hale Getirme

Ama bu yeterince sağlam bir test değil. Stack’e bir şey ekleyip sonra çıkardığımızda hâlâ boş mu, onu da test edelim.

Önce stack’e bir değer ekliyoruz:

```python
self.stack.push(5)
```

Artık stack boş olmamalı. O yüzden:

```python
self.assertFalse(self.stack.is_empty())
```

Bunu ekleyip tekrar çalıştırıyorum. Test hâlâ geçiyor. Böylece:

* Başlangıçta boş
* Push sonrası boş değil

durumlarını doğrulamış olduk.

## 🔍 Peek Testi

Sıradaki hata:  **“Test peeking at the top of the stack”** .

Peek, stack’in en üstündeki elemanı göstermelidir. O halde önce stack’e bir şey ekleyelim:

```python
self.stack.push(5)
self.assertEqual(self.stack.peek(), 5)
```

Testleri tekrar çalıştırıyoruz ve bu test geçiyor.

### ⚠️ Daha Derin Düşünme

Ama gerçekten doğru mu? Ya `peek` stack’in en altına bakıyorsa?

Tek bir eleman varken bunu anlayamayız. O yüzden iki eleman ekleyelim:

```python
self.stack.push(3)
self.stack.push(5)
self.assertEqual(self.stack.peek(), 5)
```

Eğer `peek` en altı gösterseydi 3 dönerdi. Ama 5 dönüyorsa, doğru çalıştığını söyleyebiliriz.

## 🔄 Pop Testi

Sıradaki hata:  **“Test popping an item off the stack”** .

Pop’u test etmek için önce stack’e bir şey eklemeliyiz:

```python
self.stack.push(5)
self.assertEqual(self.stack.pop(), 5)
```

Ama bu da yeterli değil. Çünkü pop sadece peek gibi davranıyor olabilir.

O yüzden iki eleman ekleyelim:

```python
self.stack.push(3)
self.stack.push(5)
self.assertEqual(self.stack.pop(), 5)
```

Şimdi pop doğru elemanı döndürüyor.

### 🧠 Daha Sağlam Test

Ama gerçekten stack’ten çıkardı mı? Bunu kontrol etmek için:

```python
self.assertEqual(self.stack.peek(), 3)
```

Yani 5 çıkmış olmalı ve 3 en üstte kalmalı.

## 📥 Push Testi

Son kalan test:  **“Test pushing an item onto the stack”** .

Basitçe bir eleman ekleyip peek ile kontrol edebiliriz:

```python
self.stack.push(3)
self.assertEqual(self.stack.peek(), 3)
```

Ama yine aynı sorun: Ya push hep tek eleman tutuyorsa?

O yüzden bir tane daha ekleyelim:

```python
self.stack.push(5)
self.assertEqual(self.stack.peek(), 5)
```

İstersek ek olarak:

```python
self.assertEqual(self.stack.pop(), 5)
```

diyerek gerçekten stack’te olduğunu da doğrulayabiliriz.

## 🧪 Testleri Derinleştirme

Burada pop testini biraz daha ileri götürebiliriz:

* 3 push
* 5 push
* 5 pop
* 3 pop
* sonra stack boş mu?

```python
self.assertTrue(self.stack.is_empty())
```

Testleri tekrar çalıştırıyoruz ve hepsi geçiyor. Ayrıca **%100 test coverage** elde etmiş oluyoruz.

## 🎯 Sonuç ve Düşünce Süreci

Bu demo şunu gösteriyor:
Bir testin geçmesi,  **yeterli olduğu anlamına gelmez** . Köşe durumlarını düşünmelisiniz.

Kendinize şu soruları sorun:

* Gerçek davranış bu mu?
* Stack’e eklenen eleman üste mi ekleniyor, alta mı?
* Pop gerçekten elemanı kaldırıyor mu, yoksa sadece gösteriyor mu?

Bu yüzden:

* Birden fazla elemanla test edin
* Pozisyonları doğrulayın
* Fonksiyonun gerçek davranışını test edin

### 🧠 Temel İlke

Fonksiyonun nasıl çalışması gerektiğini düşünün.
Sonra bir işlem yapın.
Ardından bir **assertion** yazarak, yapılan işlemin **beklediğiniz davranışı gerçekten gerçekleştirdiğini** doğrulayın.

İşte test assertion yazmanın özü budur.
