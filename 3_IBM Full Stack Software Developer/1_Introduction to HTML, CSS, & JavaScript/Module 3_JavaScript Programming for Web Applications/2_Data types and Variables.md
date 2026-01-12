## 🧾 Data types and Variables

Veri türleri ve değişkenler konusuna hoş geldiniz. Bu videoyu izledikten sonra, değişkenlerin ve JavaScript’in verileri nasıl depolayıp yönettiğini açıklayabilecek, yaygın adlandırma kuralları ve kurallarını açıklayabilecek ve JavaScript’te veri türleri kavramını tanımlayabileceksiniz. JavaScript’te değişkenler, verileri depolamak ve yönetmek için kullanılır. Değişkenler, çeşitli bilgi veya değer türleri için birer kapsayıcı gibi davranır. Bir değişkeni, veriyi tutan adlandırılmış bir depolama konumu olarak düşünebilirsiniz ve bu veriyi JavaScript kodunuzda kullanabilirsiniz. JavaScript’te değişkenlerle ilgili bazı önemli noktaları inceleyelim. Bir değişkenin başlatılması ( *initialization* ) için isteğe bağlı olarak ona bir başlangıç değeri atayabilirsiniz.

---

## 🏷️ Değişken Tanımlama

JavaScript’te bir değişken oluşturmak için, onu üç anahtar sözcükten biriyle bildirmeniz ( *declare* ) gerekir:  **var** , **let** veya  **const** . Bildirim, JavaScript’e veriyi depolamak için bellekte bir yer ayırmak istediğinizi söyler.  **var** , JavaScript’te değişken bildirmek için kullanılan orijinal yöntemdi ve fonksiyon seviyesinde kapsam ( *function level scope* ) sağlar. Bu, **var** ile bildirilen bir değişkenin, bildirildiği fonksiyonun tamamı boyunca kullanılabilir olduğu anlamına gelir.

 **let** , *ECMAScript 6 (ES6)* ile tanıtıldı ve blok seviyesinde kapsam ( *block level scoping* ) sağlar. Bu, **let** ile bildirilen bir değişkenin yalnızca süslü parantezlerle çevrili blok içinde kullanılabilir olduğu anlamına gelir. Bu kapsam daha öngörülebilir ve daha az hataya yatkındır.

---

## 🧱 Const Kullanımı

**const** da ES6 ile tanıtılmıştır ve sabit değerli değişkenleri bildirmek için kullanılır. Bir **const** değişkenine bir değer atadıktan sonra, onu farklı bir değerle yeniden atayamazsınız. O da blok seviyesinde kapsam sağlar. **const** değişkenleri, matematiksel sabitler veya değişmemesi gereken değerler ya da değiştirilemez ( *immutable* ) nesnelere referanslar gibi değişmemesi gereken değerler için sıklıkla kullanılır.

---

## ✍️ Değişken Adlandırma Kuralları

Değişken adları bir harf, alt çizgi ( **_** ) veya dolar işareti ( **$** ) ile başlamalıdır ve harfler, sayılar, alt çizgiler ve dolar işaretleri içerebilir. Değişken adları büyük/küçük harfe duyarlıdır ( *case sensitive* ). İşte değişken adlarına dair birkaç örnek.

**let** ile bildirilen değişkenler yeniden atanabilir, ancak aynı blok içinde yeniden bildirilemez; **const** ile bildirilen değişkenler ise sabittir ve aynı blok içinde ne yeniden atanabilir ne de yeniden bildirilebilir. Değişkenleri anlamak, JavaScript programlarında verileri yönetmek ve dönüştürmek için kritiktir. Farklı türde bilgilerle çalışmanıza olanak tanırlar; böylece kodunuz dinamik ve uyarlanabilir olur.

---

## 🧠 JavaScript’te Veri Türleri Kavramı

JavaScript’te veri türleri, bir programda hangi tür verilerin depolanıp işlenebileceğini belirten sınıflandırmalar veya kategorilerdir. JavaScript dinamik türlemeli ( *dynamically typed* ) bir dildir; bu da bir değişkeni bildirirken veri türünü açıkça belirtmeniz gerekmediği anlamına gelir. Veri türü, değişkene atadığınız değere bağlı olarak çalışma zamanında ( *runtime* ) dinamik biçimde belirlenir. JavaScript’te yerleşik ( *built-in* ) birçok veri türü vardır ve bunlar şu ana kategorilere ayrılabilir:  *primitive data types* ,  *composite data types* .

---

## 🧩 Primitive Data Types

*String* metni temsil eder. Bir *string* tek veya çift tırnak içinde yazılır. *Number* hem tamsayıları hem de kayan noktalı sayıları temsil eder. *Boolean* **true** veya **false** değerlerini temsil eder.  *Undefined* , bildirilmiş ancak kendisine değer atanmamış bir değişkeni temsil eder.  *Null* , boş bir değeri veya herhangi bir nesne değerinin yokluğunu temsil eder.

---

## 🧺 Composite Data Types

 *Composite data types* , birden fazla değeri tek bir birim olarak tutup yönetebilen veri türleridir. Bu veri türleri, veri koleksiyonlarını organize etmek ve işlemek için kullanılır; böylece daha karmaşık yapılarla çalışmak kolaylaşır. *Array* ve  *object* , iki  *composite data type* ’tır. JavaScript’te bir  *array* , birden fazla değeri depolamak için liste benzeri bir veri yapısıdır; bir *object* ise yapılandırılmış veri depolama için kullanılan anahtar-değer ( *key value* ) çiftlerinden oluşan bir koleksiyondur. JavaScript’in dinamik türlemesi, değişkenlerin yürütme sırasında veri türlerini değiştirebilmesini sağlar; bu da onu çok yönlü bir dil yapar. Bu veri türlerini anlamak, etkili JavaScript programlama için kritiktir; çünkü farklı türde verilerle çalışmayı ve bunlar üzerinde çeşitli işlemler yapmayı sağlar.

---

## ✅ Özet

Bu videoda, JavaScript değişkenlerinin verileri depolayıp yönettiğini ve isteğe bağlı başlatma ile  **var** , **let** veya **const** kullanılarak bildirildiğini öğrendiniz. **var** fonksiyon seviyesinde kapsam sağlar, **let** blok seviyesinde kapsam sağlar ve **const** sabitler için kullanılır. Değişken adları büyük/küçük harfe duyarlıdır ve bir harf, alt çizgi veya dolar işareti ile başlar ve bunları içerebilir.  *Primitive data types* ;  *string* ,  *number* ,  *boolean* , *undefined* ve *null* içerir. *Composite data types* olan *array* ve *object* ise birden fazla değeri ve yapılandırılmış veriyi yönetir.
