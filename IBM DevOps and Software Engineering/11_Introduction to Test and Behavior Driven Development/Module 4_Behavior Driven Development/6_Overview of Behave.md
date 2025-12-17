# 🎬 Overview of Behave

Bu videoyu izledikten sonra, **Behave’i çalıştırmak için klasör yapısını ve dosya adı kurallarını** açıklayabilecek ve **Behave’in feature ve step dosyalarındaki kodu adım fonksiyonlarını çalıştırmak için nasıl kullandığını** özetleyebileceksiniz. Behave aracının nasıl çalıştığını “perde arkasından” biraz göstermek istiyorum.

## 📁 Gerekli Dosya Yapısı

Behave, **“features”** adlı bir klasör arar. Behave’i kontrol eden tüm dosyalar, en üst düzeydeki **features** klasörünün altında olmalıdır.

**features** klasörünün içinde Behave, uzantısı **`.feature`** olan dosyaları arar. Bu dosyaları istediğiniz gibi adlandırabilirsiniz.

Birden fazla feature dosyanız veya yalnızca bir tane olabilir; bu size bağlıdır. Behave, **features** klasöründe bulduğu her bir dosyayı işleyecektir.

## 🧩 steps Klasörü ve Step Dosyaları

**features** klasörü ayrıca **“steps”** adlı bir alt klasör içerir. **steps** klasörünün içinde, feature dosyalarındaki Gherkin ifadeleriyle eşleşen adımları içeren bir Python dosyaları koleksiyonu bulunur.

Bu step dosyalarını nasıl adlandırdığınız önemli değildir; ancak çoğu kişi bunların step dosyaları olduğunu belirtmek için dosya adında **`_steps`** kullanır. Birazdan bu dosyaların içeriklerini anlamanıza yardımcı olması için bazı örnek step dosyalarına bakacağız.

En iyi uygulama, uygulamadan bağımsız olarak web arayüzünü manipüle eden tüm genel adımları **`web_steps.py`** adlı bir dosyaya koymanızı önerir.

Bu, Ruby on Rails ve Cucumber ile başlayan bir öneridir ve Rails bu web dosyasını sizin için hatta üretiyordu. Ben genellikle bu dosyayı bir projeden diğerine kopyalarım çünkü nadiren değişir.

Eğer adımlar içeren ek Python dosyalarınız varsa, bunları da **steps** klasöründe saklayabilirsiniz. Behave, bu klasördeki Python dosyalarındaki tüm adımları yükler.

Bu örnekte, **`load_steps.py`** adlı bir dosya ekledim; bunu genellikle senaryoları hazırlamak için örnek verileri yüklemek amacıyla kullanırım.

Feature dosyaları ile step dosyaları arasında bire bir bir ilişki olmadığını unutmayın. Örneğin, beş feature dosyam olabilir ama yalnızca iki step dosyam olabilir.

Python adımları feature dosyalarındaki tüm ifadeleri kapsadığı sürece, her şey çalışacaktır.

## 🏃 Behave Nasıl Çalıştırılır?

Dolayısıyla Behave’i kullanmak için önce klasör yapınızı doğru kurmanız gerekir. **features** klasörünüzü ve feature dosyalarınızı oluşturursunuz ve bunun altında Python step dosyalarınız için **steps** klasörünüzü oluşturursunuz.

Klasörleriniz ve dosyalarınız hazır olduktan sonra, Behave aracını **features** klasörünün ebeveyn dizininden çalıştırırsınız.

Behave, her feature dosyasındaki adımları okur, step dosyalarında eşleşen bir Python step’i arar ve bu fonksiyonları çalıştırır.

## 🔎 Step Eşleştirme Nasıl Olur?

Şimdi bu step eşleştirmenin nasıl gerçekleştiğini görmek için bazı örnek step dosyalarına bakalım.

Sol tarafta bir feature dosyanız var. Bu dosya, paydaşlarınızla oluşturduğunuz senaryoları içerir.

Sağ tarafta bir steps dosyanız var. Bu dosya, Behave’in feature dosyasıyla eşleştireceği Python ifadelerini içerir.

Bu dosyadaki tüm Python fonksiyonlarının aynı isme sahip olduğuna dikkat edin:  **`step_impl`** . Behave bu fonksiyon adlarını yok sayar. Yalnızca fonksiyonları saran Python dekoratörlerine bakar.

## 🧠 Eşleştirme Akışı

Behave yürütmeye başladığında, feature dosyasını tarayarak ilk senaryoyu bulur.

Ardından o senaryonun ilk cümlesini işler: “Given some known state.” Bu noktada Behave, **Given** anahtar sözcüğüyle başlayan ve metni “some known state” olan bir Python step’i arar.

Behave, bu step’i **steps.py** dosyasında bulur ve çalıştırır.

Sonra senaryodaki bir sonraki cümleye bakar: “And some other known state.”  **And** , bir  **Given** ’dan sonra geldiği için Behave, steps dosyasında **Given** anahtar sözcüğüyle başlayan ve “some other known state” dizgesiyle eşleşen bir Python step’i arar.

Behave bu step’i bulur ve çalıştırır.

Step’lerin steps dosyasında belirli bir sırada olmak zorunda olmadığını unutmayın. Behave, dosyada hangi sırayla göründüklerine bakmaksızın onları bulacaktır.

Feature dosyasındaki bir sonraki cümle: “When some action is taken.” Bu sefer Behave, steps dosyasında **When** anahtar sözcüğünü ve ardından “some action is taken” metnini arar.

Metin aynı olsa bile **Given** veya **Then** adımlarıyla eşleşmez. Feature dosyasındaki bir  **When** , yalnızca steps dosyasındaki bir **When** ile eşleşir.

Behave step’i bulur ve çalıştırır.

Ardından Behave “Then some outcome is observed.” adımını işler. “some outcome is observed” metnine sahip bir **Then** step’i arar ve o fonksiyonu çalıştırır.

Son olarak “And some other outcome is observed.” adımını işler. **And** anahtar sözcüğü  **Then** ’i takip ettiği için Behave, “some other outcome is observed” metniyle eşleşen bir **Then** step’i arar ve çalıştırır.

İşte sihir böyle gerçekleşir.

Behave, feature dosyasındaki her senaryoyu adım adım okur. Her adımın anahtar sözcüğünü ve metin dizgesini işler, Python steps dosyasında anahtar sözcük ve metin dizgesi çifti olarak eşleşeni bulur ve o fonksiyonu çalıştırır.

Basit ama zarif.

## ✅ Video Özeti

Bu videoda şunları öğrendiniz:

* Behave’i çalıştırmak için feature dosyaları için bir **features** klasörü ve bunun altında Python step dosyaları için bir **steps** klasörü oluşturmalısınız.
* Behave, her feature dosyasındaki adımları okur, steps dosyasında eşleşen Python step’ini arar ve ardından bu fonksiyonları çalıştırır.
