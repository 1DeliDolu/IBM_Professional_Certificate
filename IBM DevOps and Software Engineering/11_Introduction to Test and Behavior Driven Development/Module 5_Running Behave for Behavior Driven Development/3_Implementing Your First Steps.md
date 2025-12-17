# 🧩 İlk Adımlarınızı Uygulama

Bu videoyu izledikten sonra, Python adımlarını uygulama iş akışını özetleyebileceksiniz. Oluşturulan Python adımlarını nasıl uygulayacağımızı konuşalım.

Oluşturulan adımlardan bir *steps* dosyası oluşturarak başlarsınız. Behave’i çalıştırırsınız ve ilk adımın başarısız olduğunu gözlemlersiniz — çünkü yaptığı tek şey bir istisna yükseltmektir. Sonra ilk adımı geçecek şekilde uygular ve Behave’i tekrar çalıştırarak geçtiğinden emin olursunuz.

Bu süreci kalan adımlar için, hepsi geçene kadar tekrar edersiniz. Bunun nasıl yapıldığına bakalım.

---

## 🧾 Behave’in Önerdiği Adımlar

Bunlar, Behave’i herhangi bir adım dosyası olmadan bir özellik ( *feature* ) dosyasında çalıştırdığınızda gelen adım önerileridir. Bu önerilen Python fonksiyonlarını panonuza kopyalarsınız ki bir *steps* dosyasına yapıştırabilesiniz.

*steps* klasöründe bir Python dosyası oluşturmak istersiniz. Dosya adının önemi yoktur, ancak herhangi bir web uygulamasında çalışacak genel web adımları oluşturacağınız için dosyayı `web_steps.py` olarak adlandırırsınız.

Önce Behave paketinden `Given`, `When` ve `Then` dekoratörlerini içe aktarırsınız. Önerilen adımların bunlara ihtiyaç duyacağını zaten biliyorsunuz. Sonra panonuza kopyaladığınız önerilen adımları yapıştırırsınız.

Bu noktada başka bir şey yapmanıza gerek yok; dosyayı kaydetmeniz yeterlidir.

---

## 🧪 Behave Çıktısını Çalıştırma ve Yorumlama

Şimdi Behave’i çalıştırır ve çıktısını görüntülersiniz. Başarısız bir adım için kırmızı çıktı alırsınız. Eğer `web_steps.py` dosyasında adım uygulamalarını kurmamış olsaydınız, bu adım sarı olurdu; bu da adımın eksik olduğunu gösterirdi.

Ama durum bu değildir; Behave adımı bulur. Özellikle, Behave bunu `features/steps/web_steps.py` dosyasının 3. satırında bulur; tam da beklendiği gibi.

Hangi dosyada hangi adımın çalıştırıldığını bilmek hata ayıklarken çok değerlidir; çünkü Behave’in özellik dosyasındaki adımları adım dosyasındaki adımlarla nasıl eşleştirdiğini gösterir.

Şimdi bir hata mesajınız vardır. Hatanın `NotImplementedError` istisnası olması şaşırtıcı değildir; çünkü varsayılan adım şu anda bunu yapmaktadır. Senaryodaki diğer adımlar mavi renktedir; bu, Behave’in onları atladığını gösterir.

Başka bir senaryonuz olsaydı, Behave onu çalıştırırdı. Behave yalnızca şu anda başarısız olan senaryodaki kalan adımları atlar; bu başarısızlık diğer senaryoları etkilemez.

Özetinizde bir başarısız adım, dört atlanan adım ve sıfır tanımsız adım olduğunu görürsünüz. Bu tam olarak beklediğiniz şeydir.

---

## 🛠️ İlk Adımı Uygulama

Şimdi bu sorunları düzeltme zamanı. `web_steps.py` dosyanıza geri dönersiniz ve ilk adımı uygulamak istersiniz.

Önce “uygulanmadı” hatası istisnasını yükselten satırı silersiniz. Artık buna ihtiyacınız yoktur. Sonra ana sayfada olduğunuzdan emin olan bir kod satırı eklersiniz.

Unutmayın: `environment.py` dosyanızda temel URL’yi `base_url` adlı bir *context* değişkeninde kaydetmiştiniz. Dolayısıyla ana sayfaya gitmek için `context.base_url` kullanabilirsiniz.

Bu yüzden şu satırı eklersiniz:

```python
context.driver.get(context.base_url)
```

Bu kod, web sürücüsüne ana sayfanın URL’sine bir HTTP `GET` yöntemi uygulamasını ve sayfanın içeriğini almasını söyler.

Behave’i tekrar çalıştırdığınızda, `"Given I am on the ‘Home page’"` adımının artık yeşil olduğunu görürsünüz. Tebrikler; ilk adımınızı geçirdiniz.

---

## 🔁 Kırmızıdan Yeşile Adım Adım İlerleme

Bir sonraki adım `"When I set the category to ‘dog,’"` artık kırmızıdır; yani başarısız olmuştur. Bu şaşırtıcı değildir: hata yine bir `NotImplementedError` istisnasıdır; çünkü varsayılan adım hâlâ bunu yapmaktadır. Umarım bir desen fark ediyorsunuzdur.

Sonraki üç adım mavi renktedir çünkü Behave onları atlamıştır. Başarısız olan özellik ( *feature* ) artık `pets.feature` dosyasının 19. satırındadır. Özetinizde iki geçen adım, bir başarısız adım ve üç atlanan adım olduğunu görürsünüz.

Şimdi `web_steps.py` dosyanıza geri döner, sonraki adımı uygular ve Behave’i tekrar çalıştırırsınız.

---

## ✅ İş Akışı Özeti

Behave ile ilk adımları uygulamanın iş akışı şudur:

* Bir adımı uygularsınız, sonra Behave’i çalıştırır ve adımın yeşile dönüp geçtiğinden emin olursunuz.
* Kırmızı olan bir sonraki adımı uygularsınız ve tekrar edersiniz.
* Tüm adımlar yeşil olana kadar bu döngüyü sürdürürsünüz.

Bu videoda, Python adımlarını uygulama iş akışını öğrendiniz: Bir adımı uygula, Behave’i çalıştır ve adımın geçtiğinden emin ol, başarısız olan bir sonraki adımı uygula, Behave’i çalıştır ve bu adımın geçtiğinden emin ol, tüm adımlar geçene kadar bu süreci tekrarla.
