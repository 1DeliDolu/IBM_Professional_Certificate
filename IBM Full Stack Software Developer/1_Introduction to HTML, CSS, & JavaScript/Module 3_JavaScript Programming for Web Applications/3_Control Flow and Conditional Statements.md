## 🔀 Control Flow and Conditional Statements

Kontrol akışı ve koşullu ifadeler konusuna hoş geldiniz. Bu videoyu izledikten sonra, JavaScript’te kontrol akışı ve koşullu ifadeleri tanımlayabilecek, ayrıca çeşitli koşullu ifadeleri değerlendirebilecek ve karşılaştırabileceksiniz. Kontrol akışı ve koşullu ifadeler, bir JavaScript programının akışını yönlendirmede temel unsurlardır.  *Control flow* , JavaScript programında ifadelerin hangi sırayla yürütüldüğünü ifade eder. Koşullu ifadeler ise, genellikle karar verme ( *decision-making* ) ifadeleri olarak adlandırılır ve bu akışı belirli koşullara göre yönetmek için kullanılır. JavaScript’te bazı koşullu ifadeler şunlardır: **if** ifadesi, **else if** ifadesi, **else** ifadesi, iç içe ( *nested* ) **if-else** ifadesi, **switch** ifadesi ve  **ternary operator** . Her birini daha ayrıntılı inceleyelim.

---

## ✅ if Statement

**if** ifadesi, belirli bir koşul **true** ise bir kod bloğunu çalıştırmak için kullanılır. Koşul **false** ise kod bloğu atlanır. Bu örnekte, kod **age** değişkeninin  **18** ’den büyük veya eşit olup olmadığını kontrol eder. Koşul **true** ise **"you are an adult"** yazdırır. Aksi halde **"you are a minor"** yazdırır.

---

## 🔁 else if Statement

**else if** ifadesi, özellikle ikiden fazla olası sonuç olduğunda birden fazla koşulu sırasıyla test etmenizi sağlar. Örneğin, içinde bir **p** etiketi bulunan bir HTML dosyanız varsa ve bu **p** etiketinin **time message** adlı bir  **id** ’si varsa, verilen kodu ayrı bir JS dosyasında kullanarak mesajları **p** etiketinin içine ekleyebilirsiniz.

Burada kod, **time** değerini kontrol eder ve tarayıcınızdaki günün saatine bağlı olarak farklı bir selamlama yazdırır.

---

## 🧩 else Statement

**else** ifadesi, **if** ifadesindeki koşul **false** olduğunda çalıştırılacak bir kod bloğunu belirtmek için kullanılır. Bu örnekte, yağmur yağıyorsa (**is raining** **true** ise), bir şemsiye almanızı tavsiye eder. Aksi halde, buna gerek olmadığını söyler.

---

## 🧱 Nested if-else Statements

İç içe ( *nested* ) **if-else** ifadeleri, JavaScript’te ve birçok başka programlama dilinde yaygın bir programlama yapısıdır. Birden fazla koşulu test etmenize ve bu koşulların sonuçlarına göre farklı kod blokları yürütmenize olanak tanır. Burada kod, sıcaklık ve yağış kombinasyonuna göre; havanın sıcak, soğuk, yağmurlu veya güneşli olma durumlarını dikkate alarak farklı mesajlar sağlar.

---

## 🎛️ switch Statement

**switch** ifadesi, bir değeri birden fazla olası **case** değeriyle karşılaştırmanıza ve ilk eşleşen  **case** ’e göre kod çalıştırmanıza olanak tanır. Bu örnekte, kod **day** değerini değerlendirir ve haftanın gününe göre bir mesaj yazdırır.

---

## ⚡ Ternary Operator

 **ternary operator** , **if-else** gibi koşullu ifadeleri yazmanın kısa ve öz bir yoludur.  *Ternary operator* , **age** değerinin  **18** ’den büyük veya eşit olup olmadığını kontrol eder. Eğer öyleyse, **can vote** değerini **yes** olarak ayarlar. Aksi halde **no** olarak ayarlar. Kontrol akışı ve koşullu ifadeler, duyarlı JavaScript uygulamaları oluşturmak için kritiktir: kodunuzun karar vermesini, farklı eylemler yürütmesini ve belirli koşullara göre kullanıcılara kişiselleştirilmiş bir deneyim sunmasını sağlar; böylece programlarınız daha dinamik ve etkileşimli hale gelir.

---

## ✅ Özet

Bu videoda, JavaScript’te kontrol akışının koşullu ifadeleri kullanarak yürütme sırasını yönettiğini öğrendiniz. **if** ifadesi, belirli bir koşul **true** olduğunda kod çalıştırır; aksi halde kod bloğu atlanır.  **else if** , ikiden fazla olası sonucun bulunduğu durumlarda birden fazla koşulu sırayla test ederek her koşula göre farklı eylemler yapılmasını sağlar.  **else** , **if** ifadesinin koşulu **false** olduğunda çalışacak kodu belirler ve alternatif bir eylem sunar. İç içe **if-else** ifadeleri birden fazla koşulu değerlendirir ve her koşul sonucuna göre farklı kod bloklarını yürütür. **switch** ifadesi ise bir değeri birden fazla **case** ile karşılaştırır ve ilk eşleşen  **case** ’e göre kod çalıştırarak çoklu seçeneklerin yapılandırılmış biçimde ele alınmasını sağlar.
