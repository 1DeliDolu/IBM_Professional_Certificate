# 🔁 Değişken Yerine Koyma Kullanımı

Bu videoyu izledikten sonra, Behave ile çalışırken değişken yerine koymanın ( *variable substitution* ) faydalarını tartışabilecek ve Python adımlarında değişken yerine koymayı nasıl kullanacağınızı açıklayabileceksiniz. Python adımlarınızı daha genel ( *generic* ) hale getirmek için değişken yerine koymayı kullanabilirsiniz. Çoğu zaman özellik ( *feature* ) dosyanızda yalnızca bir isim alanı ya da bir değer bakımından farklı olan cümleler bulunur ve bu cümlelerin uygulamaları da bu isim ya da veri değeri dışında aynıdır. Cümledeki bu kelimeleri değişkenlere çevirerek, daha az Python adımı yazmanız gerekir; çünkü tek bir adım artık özellik dosyanızdaki birden fazla cümleyle eşleşebilir. Bu, daha fazla yeniden kullanım ( *reuse* ) sağlar ve adımları mümkün olduğunca genel yapmak, maksimum yeniden kullanım için her zaman iyi bir fikirdir.

---

## 🐾 Örnek Senaryo: Bir Evcil Hayvan Oluşturma

Bir evcil hayvan oluşturmak için bir senaryoyla başlayalım. Bu senaryo şöyle diyor:

“Given I am on the Home Page, When I set the ‘Name’ field to ‘Maxwell’ And I set the ‘Category’ field to ‘Dog,’ And I set ‘Available’ to ‘True,’ And I click the ‘Create’ button, Then I should see the message ‘Success’”.

Ortadaki üç benzer cümleye dikkat edin. “When I set the ‘Name’ field to ‘Maxwell,’ And I set the ‘Category’ field to ‘Dog’” cümleleri, alan adları ve veri dışında aynı cümledir. Benzer şekilde, bir sonraki cümle olan “And I set ‘Available’ field to ‘True,’” da önceki ikisiyle aynıdır. Sadece alan adı ve veri farklıdır.

Bu cümleler için adımları, değişken yerine koyma olmadan ve değişken yerine koyma ile nasıl uygulayacağınıza bakalım.

---

## 🧩 Değişken Yerine Koyma Olmadan Adım Uygulama

Beklediğiniz gibi, bu üç cümle onları eşleştirmek için üç adım gerektirir. İlk adımda, alan adının küçük harfli ( *lowercase* ) halini öğe kimliği ( *element ID* ) olarak kullanırsınız. Varsayım, kullanıcı arayüzünde o ada sahip bir ID ile bir alan olduğudur.

Aynı şekilde, veriyi (metin dizesini) alır ve `send_keys()` fonksiyonunu kullanarak bu veriyi alana gönderirsiniz. Sonraki adımları da aynı şekilde ele alırsınız. Alanın küçük harfli adını kullanır ve özellik cümlesindeki metin dizesini `send_keys()` fonksiyonuyla gönderirsiniz.

Tutarlılığa dikkat edin: Alan adı her zaman ifadede geçen adın küçük harfli halidir. Aynı şekilde, veriyi her zaman metin dizesi olarak değiştirmeden gönderirsiniz.

---

## 🧠 Değişken Yerine Koyma ile Tek Adımda Çözüm

Bu iki olgudan yararlanıp, tüm bu ifadeleri karşılayacak değişken yerine koyma kullanan tek bir adım oluşturabilirsiniz. Bu kodun en kötü kısmı, uygulamaların sadece öğe adı ve veri için sabit ( *hardcoded* ) dizeler dışında aynı olmasıdır. Daha iyisini yapabiliriz.

Değişken yerine koyma kuralları basittir. İki süslü parantezle başlarsınız. Behave, adım dizesinde açık bir süslü parantez gördüğünde, kapalı süslü paranteze kadar gelen kısmın bir değişken adı olduğunu anlar.

Sonra, dizedeki verinin yerine geçecek bir değişken adı oluşturursunuz. Python değişken adlarında olduğu gibi boşluk olamaz; ama alt çizgi ile ayırabilirsiniz. Ardından, dizede süslü parantez içindeki değişken adını kullanarak yerine koyma yaparsınız. Behave, o konumda görünen metni alır ve o isimdeki değişkene atar. Bu değişken daha sonra fonksiyonunuza parametre olarak aktarılır.

---

## 🔍 Özellik Cümlesini Analiz Etme

Özellik dosyasındaki üç ifadeden birincisini inceleyelim:

“When I set the ‘Name’ field to ‘Maxwell’”.

Bu cümlede değişecek kelimeler “Name” ve “Maxwell”dir. Burada gösterildiği gibi, bunların etrafına tırnak koymak bir en iyi uygulamadır; çünkü bunlar dize içinde yerine koyacağınız kelimeler olduğunu belirtir. Tırnak kullanmak ayrıca Behave’in dize eşleştirmesine yardımcı olur. Zorunlu değildir ama buna güvenin: iyi bir fikirdir.

Sonra Python adımlarınıza geçersiniz. Dekoratörün dizesinde iki değişken adı oluşturursunuz: "name" için `{element_name}` ve gerçek veri için `{text_string}`. Bunları istediğiniz gibi adlandırabilirsiniz, ama bu adlar uygundur.

---

## 🧱 Python Adımı Uygulaması

Gerçek adım fonksiyon uygulamasında bunları nasıl kullandığınıza bakalım. `@when` dekoratörü ve iki değişkenin tanımlı olduğu dize ile başlarsınız. Adım uygulamanızda, adım dizesindeki değişken adlarıyla aynı isimlerde iki ek parametre eklersiniz.

Artık bu değişken adlarını, özellik dosyasından gelen dizeler için yerine koyma olarak fonksiyonunuz içinde kullanabilirsiniz. Öğenin ID’sinin alan adının küçük harfli hali olacağını hatırlayın. Bu nedenle küçük harfli halini alan bir satır ekler, geçerli bir HTML ID olduğundan emin olmak için boşlukları alt çizgi ile değiştirirsiniz. Bu ID’yi `element_id` adlı bir değişkene atarsınız.

Sonra `context.driver.find_element_by_ID` çağırır ve o öğeyi almak için bu öğe ID’sini geçirirsiniz. Öğeyi aldıktan sonra, yeni veri göndermeden önce içinde veri olmadığından emin olmak için temizlersiniz ( *clear* ). Son olarak, öğe üzerinde `send_keys()` çağırır ve `text_string` değişkenini geçirirsiniz. Bu `text_string` değişkeni, özellik dosyasındaki ifadede çift tırnak içine alınmış her ne metin varsa onu içerir. Çift tırnak kullanmayı sevmemin nedeni budur: dizenin nasıl ayrıştırılacağına dair faydalı bir görsel temsil sunar.

Böylece Behave, özellik dosyasındaki üç ifadeyi yalnızca tek bir adım fonksiyonu ile eşleştirebilir ve hepsi doğru alanı manipüle edip doğru veriyi gönderir.

---

## ♻️ Yeniden Kullanım Kazancı

Değişken yerine koymayı kullanmak işte bu kadar. Bunun güzelliği, çok büyük sayıda adımı yalnızca tek bir genel adım ile değiştirebilmenizdir. Bu örnekte üç adım bir adıma düştü; ancak tahmin edebileceğiniz gibi pek çok web sayfasında pek çok alana çok fazla metin yazacaksınız ve bunların hepsi değişken yerine koyma kullanan o tek adımı kullanabilir.

Bunun gibi adımlar `web_steps.py` dosyası için iyi adaylardır; ben tüm genel web adımlarımı buraya koymayı severim. Böylece bu adımları tüm uygulamalarınızda yeniden kullanabilirsiniz; çünkü bir alana metin yazmak, uygulama ne yapıyor olursa olsun aynıdır.

Bu şekilde, minimum sayıda adım yazar ve değişken yerine koyma kullanarak maksimum yeniden kullanım elde edersiniz.

---

## ✅ Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* Değişken yerine koyma, gereken adımları azaltır ve yeniden kullanımı maksimize eder.
* Değişkenleri yerine koymak için:
  * Dekoratör dizesinde veriyi, süslü parantez içine alınmış değişkenlerle değiştirirsiniz.
  * Adım uygulamasına, bu değişkenlerle aynı isimlerde parametreler eklersiniz.
  * Özellik dosyasından gelen dizeler yerine bu değişken adlarını kullanırsınız.
