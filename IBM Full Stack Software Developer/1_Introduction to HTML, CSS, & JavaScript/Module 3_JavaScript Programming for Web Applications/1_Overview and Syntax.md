## 🎵 Overview and Syntax

[MUSIC] Merhaba, JavaScript Dili: Genel Bakış ve Sözdizimi bölümüne hoş geldiniz. Bu videoyu izledikten sonra, JavaScript *primitive* türlerini ve *object* (nesne) türlerini açıklayabileceksiniz. JavaScript, *ECMAScript* standardından türetilmiş ve başlangıçta *Netscape Navigator* tarayıcısında çalışmak üzere tasarlanmış bir *scripting* dilidir. Günümüzde neredeyse tüm tarayıcılar JavaScript’i destekler. *JavaScript* kelimesinde *Java* adı geçse de, bu iki dil birbiriyle ilişkili değildir. Bir tarayıcıya bir JavaScript yorumlayıcısı gömüldüğünde, ortaya dinamik web sayfaları oluşturma yeteneği çıkar. JavaScript, aksi halde statik olan web içeriğine davranış kazandırır.

Bir web sayfasının içeriği, JavaScript yorumlayıcısının *scripting* yeteneği ile dinamik olarak değiştirilebilir. JavaScript kodu, web tarayıcısının ürettiği *document object model* (DOM) üzerinde işlem yapar. Sunucu programlama ve tarayıcı  *scripting* ’inin birlikte çalışmasının yollarından biri, *Ajax* (veya  *Asynchronous JavaScript and XML* ) adı verilen bir mimaridir. *Ajax* terimi, JavaScript ve XML aracılığıyla yapılan asenkron sunucu çağrılarından daha fazlasını kapsar. Ajax; HTML, JavaScript, *cascading stylesheets* ve *document object model* üzerinden web sayfasını değiştirerek daha zengin, etkileşimli web uygulamaları sağlayan bir dizi tekniği temsil eder. Günümüzde XML yerine yaygın olarak *JSON* kullanılır.

---

## 🧱 JavaScript Primitive Türleri

JavaScript’te çeşitli *primitive* değerlerle ilişkili beş *primitive* tür vardır:

* **number:** 0 veya 3.1412 gibi tüm sayılar
* **string:** *Hello World* gibi tüm metinler
* **boolean:** **true** veya **false** değerleri
* **null:** **null** değeri
* **undefined:** **undefined** değeri; çünkü bir veri türü atanmamıştır veya değişken mevcut değildir

Diğer tüm *non-primitive* veri türleri nesnedir.

---

## 🔢 Number Türü Detayları

**number** *primitive* türü; hem tamsayı hem de kayan noktalı değerleri, **NaN** ( *not a number* ) değerini ve sonsuzu ( *infinity* ) temsil eder. Tamsayılar base-10 (decimal), base-8 (octal) veya base-16 (hexadecimal) değerler olarak kodlanabilir. Tamsayı literal’ları (decimal olarak  **16** , octal olarak **020** ve hexadecimal olarak  **0x10** ) aynı değere sahiptir. JavaScript’te tüm sayılar, dahili olarak *double-precision* (veya 64-bit) kayan noktalı sayılar olarak temsil edilir. JavaScript  *string* ’leri çift veya tek tırnak işaretleriyle sınırlandırılır. *Primitive* veri türleriyle ilişkili herhangi bir davranış veya metod yoktur.

---

## 🧩 Wrapper Objects

*Primitive* türler olan  **number** , **string** ve  **boolean** , kendi nesne karşılıklarıyla ( *object counterparts* ) sarılabilir.  *Wrapper object* ’ler *primitive* türle aynı isme sahiptir, ancak büyük harfle başlar. Çoğu nesne yönelimli programlama dili gibi JavaScript de bu  *wrapper object* ’ler ile *primitive* değerler arasında dönüşüm yapmak için yerleşik yollar sağlar.  *Wrapper object* ’ler, nesneler ile  *primitive literal* ’lar arasında dönüşüm yapmak için **valueOf** ve **toString** gibi özel metodları kullanır.

JavaScript’te **"typeof"** anahtar sözcüğü, verilen operand’ın veri türünü bulmak için kullanılır. **new** anahtar sözcüğü kullanılmadan oluşturulan  *string* ’lerin türünün **string** olduğuna dikkat edin. **new** anahtar sözcüğü, **String**  *wrapper object* ’ini oluşturmak için kullanılır.

Bu nesne, **ObjectWrapper** sınıfı üzerinde **valueOf** fonksiyonu çağrılarak *primitive string* türüne dönüştürülebilir.

---

## 🗂️ Arrays

 *Array* ’ler, programcıya indeksli anahtarlarla veri saklama ve geri çağırma konusunda yardımcı olan özelleştirilmiş koleksiyon nesneleridir.  *Array* ’ler sıfır tabanlı indeksleme şeması kullanır; yani bir dizinin ilk elemanının indeksi sıfırdır.  *Array* ’ler eleman ekleme veya çıkarma yoluyla dinamik olarak büyür veya küçülür. **length** özelliği, dizide bulunan eleman sayısını tutar.  *Array* ’ler, bir **Array constructor** veya bir **Array literal** kullanılarak tanımlanabilir.

Bir diziyi constructor ile tanımlarken, **"new Array"** anahtar sözcüklerini kullanır ve dizi elemanlarını yeni dizinin parametreleri olarak belirtirsiniz.

 *Array literal* ’lar, dizi elemanlarını köşeli parantezler içinde tanımlayarak oluşturulur. Daha sonra, slayttaki son örnekte görüldüğü gibi diziyi bir değişkene atarsınız.

---

## 📅 Date Object

**Date** nesnesi, tarih ve saati tutmak için kullanılan özelleştirilmiş bir nesnedir. Bir Date nesnesinin constructor’ı **"new Date"** formatındadır ve isteğe bağlı parametreler alır. Herhangi bir parametre olmadan bir Date nesnesi oluşturursanız, JavaScript mevcut yerel tarih ve saati içeren bir nesne döndürür. Bu Date nesnesini konsola gönderirseniz veya bir web sayfasında görüntülemeye çalışırsanız, JavaScript otomatik olarak nesneye **toString()** metodunu uygular. Görüntülenen sonuç, bu slaytta gösterildiği gibi tarihin *string* sürümüdür.

Ayrıca **new Date** fonksiyonuna parametreler geçirerek yeni tarihler oluşturabilirsiniz. Slayttaki örnekler, yeni Date nesneleri oluştururken tarih parametreleri için *string* veya sayısal değerlerin kullanılabileceğini gösterir.

---

## ⚠️ Error Objects

Diğer nesne yönelimli dillerde olduğu gibi, JavaScript’te bir *exception* oluştuğunda hata nesnesi örnekleri oluşturulur. Hata nesnesi örneği, hata hakkında bilgi içeren iki özellik içerir:

* **message** özelliği, hata hakkında bir açıklama içerir.
* **name** özelliği, **RangeError** gibi hata türünü tanımlar.

 **RangeError** , sayısal bir değer veya parametre geçerli aralığının dışında olduğunda oluşturulan bir hata örneğidir.

Genel bir hata dışında, JavaScript’te altı adet başka çekirdek hata türü daha vardır; bunların üçü slaytta gösterilmiştir. Diğer üçü  **EvalError** , **ReferenceError** ve  **SyntaxError** ’dır. Hata nesnesi genişletilerek özel hata türleri oluşturulabilir. Slaydın son satırı, parametre alanında özel bir hata mesajı ile genel bir hata nesnesi oluşturulmasını gösterir.

---

## ✅ Özet

Bu videoda, JavaScript’in aksi halde statik olan web içeriğine davranış kazandıran bir *scripting* dili olduğunu öğrendiniz.  *Primitive* ’ler değerlerdir ve herhangi bir özellik veya metoda sahip değildir. *Primitive* örnekleri:  **number** ,  **string** ,  **boolean** , **null** ve  **undefined** .

 *Wrapper object* ’ler, karşılık gelen *primitive* veri türlerinden nesnelerin oluşturulmasına izin verir.  *Wrapper object* ’ler bir *primitive* değeri saklayabilir ve onu işlemek için metodlar sağlar.  *Wrapper object* ’ler *primitive* türle aynı isme sahiptir, ancak *primitive* veri türünün kendisinden ayırt etmek için büyük harfle başlar. *Wrapper object* örneklerinden bazıları  *array* , *data* ve *error* nesneleridir.
