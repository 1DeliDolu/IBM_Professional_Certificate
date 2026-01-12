# ✍️ Özellik Dosyaları Yazma

Bu videoyu izledikten sonra, özellik dosyaları yazmak için temel ipuçlarını tartışabilecek ve Gherkin sözdiziminde **Background** anahtar sözcüğünü ve tabloları nasıl kullanacağınızı açıklayabileceksiniz.

İlk özellik dosyanızı yazarken bu ipuçlarını aklınızda bulundurun.

---

## ✅ Tutarlılık Sağlayın

Tutarlılık için çabalayın. Unutmayın, Behave çalıştıracağı Python adımlarını bulmak için **string eşleştirme** kullanır.

Diyelim ki bir Gherkin ifadesinde `"I see"` ve başka bir ifadede `"I should see"` string’i var. Bunlar iki farklı string’dir; dolayısıyla her string için ayrı bir Python step yazmanız gerekir. Ancak bu string’ler aynı kodu çalıştırıyorsa, özellik dosyanızda sadece **tek bir ifadeyi seçip** onu kullanın.

Tutarlı olun ki **yinelenen Python step** yazmak zorunda kalmayın.

---

## 🧑‍💻 Kullanıcı Deneyimini Düşünün

Bir özellik dosyası yazarken kullanıcı deneyimini de göz önünde bulundurmalısınız. Kullanıcının görmesini istediğiniz davranışı tarif ediyorsunuz.

Arayüzde `"Customer ID"` adlı bir alan varsa, özellik dosyasında da **aynı adı** kullanın. Geliştiricilerin özellik dosyalarında bazen `customer_id` gibi, arka planda güncellenen değişken adını kullandığını gördüm. Sorun şu ki, paydaşınız ne dediğinizi anlamaz; çünkü ekranda gördüğü alanın adı `"Customer ID"`’dir.

Her zaman özellik dosyalarını, özelliğin perde arkasında ne yaptığı gibi değil, **özelliğin nasıl kullanıldığını açıklıyormuş gibi** yazın.

---

## ⏱️ Sistemin Yanıt Verdiğini Gösteren İpuçları Ekleyin

Bir diğer büyük ipucu, sistemin bir isteğe yanıt verdiğini gösteren ipuçları oluşturmaktır. Bu ipuçları, uzaktan test ederken yaşanabilecek gecikme (latency) sorunlarına yardımcı olabilir.

Örneğin birinin `Search/Submit` düğmesine tıkladığında çalıştığını kontrol ediyorsanız, istek tamamlandığında güncellenen ekranda bir durum (status) olduğundan emin olun. Böylece test araçlarına, sonuçları kontrol etmeden önce bu durumu beklemesini söyleyebilirsiniz.

---

## 🐾 Örnek: Evcil Hayvan Dükkanı

Şimdi, bu tür özellik dosyalarından birini nasıl yazdığınızı göstermek için bir örneği tartışalım. Örneğimiz bir evcil hayvan dükkanından.

Bu dükkan, web sitelerine gelen müşterilerin evcil hayvanları **kategoriye göre arayabilmesini** istiyor.

Özellik dosyanızı `Feature` anahtar sözcüğüyle başlatırsınız ve ardından başlığı yazarsınız: `"Search for pets by category"`.

Sonra kullanıcı hikayesini eklersiniz:

> `"As a pet shop customer, I need to be able to search for a pet by category, So that I only see the category of pet that I’m interested in buying."`

---

## 🧩 Background Anahtar Sözcüğünü Kullanma

Sonra `"Background"` anahtar sözcüğünü kullanırsınız. Bazen aynı özellik içindeki birkaç senaryo aynı bağlamla başlar.

 **Background** , bağlamı bir kez belirtmek ve ardından bunu özellikteki **her senaryodan önce** oluşturmak için kullanabileceğiniz bir test fikstürüdür. Genellikle başlangıç test durumunu ayarlamak için bir veya daha fazla `Given` ifadesiyle Background kullanırsınız, ancak uyan herhangi bir anahtar sözcüğü kullanabilirsiniz.

Bu örnekte şunu kullanırsınız: `"Given the following pets."`

Bu `Given` ifadesi diğerleri gibidir. Behave, tüm Python step dosyalarında `Given` dekoratörü ve ardından `"the following pets"` string’ini arar.

---

## 📋 Background İçinde Veri Tablosu

`Given` ifadesinin altında bir **veri tablosu** oluşturursunuz. Tabloyu `Given` ifadesiyle ilişkilendirmek için tablonun girintili olması gerekir.

Çalışan bir tablo oluşturmak için sütunları **dikey çizgilerle** ayırmanız ve ilk satırı sütun adlarını belirtmek için kullanmanız gerekir.

Bu örnekte üç sütun adı vardır: `name`, `category`, `available`.

Diğer satırlar, her senaryonun başında tabloda bulunmasını istediğiniz verileri içerir.

Unutmayın: bu tabloyu Background test fikstürüne dahil ettiğiniz için, verileri her senaryoda yeniden yüklenecektir. Örneğin bir senaryo evcil hayvanlardan birini silerse, Behave tabloyu yeniden yükler ve o evcil hayvan bir sonraki senaryo için tekrar orada olur.

---

## 🎬 Senaryo Yazma

Şimdi bir senaryo yazabilirsiniz.

Evcil hayvan dükkanının web sitesi ana sayfasındaki bir müşterinin kategori alanına `"dog"` girdiğinde ve `"Search"` düğmesine tıkladığında ne olduğunu tanımlamak istiyorsunuz.

`Scenario` anahtar sözcüğüyle başlarsınız ve bu senaryo için bir başlık eklersiniz: `"Search for dogs."`

Sonra başlangıç durumunu `Given` ile ayarlarsınız: `"Given I am on the home page."`

Bu sizin başlangıç noktanız olacaktır.

---

## 🧭 Olayları Tanımlama

Sonra olayı eklersiniz:

`"When I set the 'Category' to 'dog.'"`

Bu ifade sadece kullanıcının eylemini tarif etmez. Ayrıca geliştiricilere ana sayfada kullanıcının arama kriteri olarak `"dog"` metnini belirtebileceği türden bir alan gerektiğini söyler.

Olayın ikinci kısmı:

`"And I click on the 'Search' button."`

Artık geliştiriciler, kategori alanına ek olarak bir arama düğmesi sağlamaları gerektiğini bilir. Bu iki cümle, bu senaryo için ana sayfada ne gerektiği konusunda çok bilgi verir.

---

## 🎯 Ölçülebilir Sonuç

Şimdi ölçülebilir sonucun zamanı.

Şöyle başlarsınız:

`"Then I should see the message 'Success.'"`

Bu ifadenin önemini yeterince vurgulayamam. Birine bir veri tablosuna bakıp bir şeyin değişip değişmediğini fark etmesini söylemek kolaydır. Ama Selenium gibi bir web tarayıcı sürücüsüne bunu yaptırmak daha zordur. Daha spesifik olmanız gerekir.

Bu nedenle, sonuçların tamamlandığını gösteren `"Success"` mesajı gibi ekranda görünen ipuçları ve bir durum oluşturmalısınız.

Böylece `"Success"` mesajını görene kadar beklersiniz; bu, aramanın tamamlandığını gösterir.

---

## ✅ Sonuçları Doğrulama

Son olarak, kullanıcının doğru sonuçları aldığından emin olmak için birkaç doğrulama (assertion) eklersiniz.

İlk doğrulama kullanıcının ne aradığını belirtir:

`"And I should see 'Fido' in the results."`

Fido’nun sonuçlarda olması gerektiğini nereden biliyorsunuz? Background ifadesindeki tabloyu kontrol edersiniz. Tablo `Fido` adlı bir köpek, `Kitty` adlı bir kedi ve `Leo` adlı bir aslan içerir.

Bu durum, Background ifadesinde test verisini belirtmenin neden bu kadar faydalı olduğunu gösterir: sistemin başlangıç durumunun ne olduğunu herkesin bilmesini sağlar.

Sonraki iki doğrulama, kullanıcının ne aramadığını belirtir:

* `"But I should not see 'Kitty' in the results;"`
* `"And I should not see 'Leo' in the results."`

Kitty bir kedidir, Leo bir aslandır. İkisi de köpek değildir.

Doğrulamalardaki tutarlılığa dikkat edin: `"I should see"`, `"I should not see"` gibi ifadeleri tutarlı şekilde kullanıyorsunuz. Böylece daha az Python step yazmanız gerekir.

---

## 📌 Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* Bir özellik dosyası yazarken **tutarlılık** sağlamalı, **kullanıcı deneyimini** düşünmeli ve sistemin bir isteğe yanıt verdiğini gösteren **ipuçları** oluşturmalısınız.
* **Background** kullanarak her senaryodan önce aynı başlangıç durumunu kolayca oluşturabilirsiniz.
* Bir tablonun sütunlarını **dikey çizgilerle** ayırmanız ve ilk satırı sütun adlarını belirtmek için kullanmanız gerekir.
