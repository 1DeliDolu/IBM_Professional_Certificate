# 📦 Paketleme

## 🎯 Öğrenme hedefleri ve kavramlara giriş

Packaging bölümüne hoş geldiniz. Bu videoyu izledikten sonra şunları yapabileceksiniz:

* Python *module* (modül), *package* (paket) ve *library* (kütüphane) kavramlarını birbirinden ayırt etmek
* Bir Python paketi oluşturmak
* Bir Python paketini doğrulamak
* Bir Python paketini kullanmak

Modüller, paketler ve kütüphaneler Python'da sıkça kullanılan terimlerdir. Şimdi bu terimlerin her birine ayrıntılı olarak bakalım.

---

## 🧩 Python modülü nedir?

Bir Python modülü, Python tanımlarını, deyimlerini, fonksiyonlarını ve sınıflarını içeren `.py` uzantılı bir dosyadır. Bir modülü diğer betiklere ve not defterlerine içe aktarabilirsiniz.

Örneğin, içinde iki fonksiyon bulunan `module.py` adlı bir modül düşünün. İlk fonksiyon, girdiyi kareye alıp sonucu çıktı olarak döndüren `def square number return number asterisk asterisk two` fonksiyonudur.

---

## 🧮 Kare alma ve ikiyle çarpma örnekleri

İkinci fonksiyon, girdiyi ikiyle çarpıp sonucu çıktı olarak döndüren `def doubler number return number asterisk two` fonksiyonudur.

Fonksiyon aynı dizindeyse, onu içe aktarabilir ve bu modüldeki fonksiyonları kullanabilirsiniz.

Kare fonksiyonunu `print` komutuyla kullanmayı ele alalım. “Dört şapka işareti iki kare dört” ifadesi için çıktı, “dört şapka işareti iki eşittir on altı” olarak görüntülenir.

Benzer şekilde, değeri dört olan `print doubler` fonksiyonu için çıktı, “iki yıldız dört eşittir sekiz”dir.

---

## 📁 Python paketi nedir?

Bir paket, içinde bir `init.py` dosyası bulunan bir dizine yerleştirilmiş Python modüllerinin bir koleksiyonudur; bu dosya, o dizini yalnızca Python betiklerinden oluşan sıradan bir dizinden ayırır.

Örnekte, üst dizinde (parent directory) yer alan ve içinde iki modül bulunan `my project` paketi gösterilmektedir: `module one.py` ve `module two.py`.

Ayrıca bir `init.py` dosyası da içerir.

Bir modülü veya paketi içe aktardığınızda, Python tarafından oluşturulan karşılık gelen nesne her zaman *module* türündedir. Modül ile paket arasındaki ayrımın yalnızca dosya sistemi düzeyinde olduğunu unutmayın.

---

## 📚 Kütüphane nedir?

Bir kütüphane, paketlerin bir koleksiyonudur ya da tek bir paket olabilir. Örneklere `NumPy`, `PyTorch` ve `Pandas` dahildir.

*Package* ve *library* terimlerinin çoğu zaman birbirinin yerine kullanıldığını unutmayın. Bu nedenle, `NumPy`, `PyTorch` ve `Pandas` aynı zamanda paketler olarak da adlandırılır.

---

## 🏗️ Python paketi oluşturma adımları

Şimdi bir Python paketi oluşturmanın adımlarına bakalım. İki modül olduğunu varsayın. `module one.py` iki fonksiyon içerir: `square` ve `doubler`. `module two.py` ise `mean` adlı tek bir fonksiyona sahiptir.

`my project` klasörünü bir pakete dönüştürmek için, `my project` klasöründe bir `init.py` dosyanızın olması gerekir. `init.py` dosyasının içeriği şu şekilde olmalıdır:

```python
from .importmodule1
from .importmodule2
```

Bir paket oluşturmanın tipik adımları şunlardır:

1. Önce, paket adıyla bir klasör oluşturun.
2. Sonra, boş bir `init.py` dosyası oluşturun.
3. Gerekli modülleri oluşturun.
4. Son olarak, pakette ihtiyaç duyulan modüllere referans veren kodu `init.py` dosyasına ekleyin.

---

## ✅ Paketi doğrulama

Paketi oluşturduktan sonra, paketi doğrulamanız gerekir.

Paketi doğrulamak için önce bir *bash terminali* açın. Çalışma dizininin, paketinizin bulunduğu klasörle aynı olduğundan emin olun.

Kabukta `python` komutunu çalıştırarak Python yorumlayıcısını açın.

Python istemini kullanarak, `import` ifadesini proje adından sonra yazın. Örneğin:

```python
import my project
```

Komut hata vermeden çalışırsa, bu, paketin başarıyla yüklendiğinin bir göstergesidir.

Paketinizi test etmek için genel yapı, süslü parantezleri kullanmadan ancak yuvarlak parantezleri koruyarak paket adı, `.module` adı, `.function` adı ve ardından parametreler şeklindedir.

Örneğin, `my project` kullanıldığında, `myproject.basic.square to` fonksiyonu 4 değerini döndürecektir.

---

## 🧷 Paketi diğer betiklerde kullanma

Paketi oluşturduktan sonra, paket klasörü aynı dizinde olduğu sürece onu diğer betiklerde kullanabilirsiniz.

Bu durumda, üst dizinde `test.py` adlı bir dosyanız vardır. Paketteki fonksiyonları içe aktarabilirsiniz.

Örneğin, `myproject.module1` içindeki Python kodunu kullanarak `square` ve `doubler` fonksiyonlarını içe aktarırız. `myproject.module2` içinden `mean` fonksiyonunu içe aktarırız.

Daha sonra, `square 4` sonucunu yazdırırız. Ardından, `doubler 4` sonucunu yazdırırız. Son olarak, `mean` fonksiyonunu 2, 1 ve 3 değerleriyle kullanırız.

Daha sonra fonksiyonları çalıştırabilir ve doğru sonuçları alıp almadığınızı kontrol edebilirsiniz.

---

## 🔁 Özet

Bu videoda şunları öğrendiniz:

Bir Python modülü, Python tanımlarını, deyimlerini, fonksiyonlarını ve sınıflarını içeren `.py` uzantılı bir dosyadır. Bir paket, içinde bir `init.py` dosyası bulunan bir dizine yerleştirilmiş Python modüllerinin bir koleksiyonudur. Bir kütüphane, paketlerin bir koleksiyonudur ya da tek bir paket olabilir.

Bir paket oluşturmak için paket adıyla bir klasör oluşturur, boş bir `init.py` dosyası oluşturur ve gerekli modülleri yaratırsınız. `init.py` dosyasında, pakette ihtiyaç duyulan modüllere referans veren kodu eklersiniz.

Paketi bir *bash terminali* aracılığıyla doğrulayabilirsiniz. Paket klasörü aynı dizinde olduğu sürece, paketi diğer betiklerde kullanabilirsiniz.
