# 📘 Türler

## 🧩 Python'da Tür Nedir?

Bir *type* (tür), Python'ın farklı veri türlerini temsil etme biçimidir.

Bu videoda, Python'da yaygın olarak kullanılan bazı türleri tartışacağız.

Python'da farklı türleriniz olabilir. Bunlar 11 gibi tamsayılar, 21.213 gibi gerçek sayılar olabilir, hatta kelimeler bile olabilir.

Tamsayılar, gerçek sayılar ve kelimeler, farklı veri türleri olarak ifade edilebilir.

Aşağıdaki tablo, son örnekler için üç veri türünü özetler. Birinci sütun, ifadeyi gösterir. İkinci sütun, veri türünü gösterir.

Python'da gerçek veri türünü `type` komutunu kullanarak görebiliriz.

`int`, tamsayıyı ifade eder ve `float`, özünde gerçek sayı anlamına gelen *float* türünü ifade eder.

`string` türü, bir karakter dizisidir.

## 🔢 Tamsayılar ( *int* )

İşte bazı tamsayılar. Tamsayılar negatif veya pozitif olabilir.

Tamsayılar için sonlu bir aralık olduğunu, ancak bunun oldukça büyük olduğunu belirtmek gerekir.

## 📏 Ondalıklı Sayılar ( *float* )

`float`lar gerçek sayılardır. Tamsayıları içerirler, fakat tamsayıların arasındaki sayıları da içerirler.

0 ile 1 arasındaki sayıları düşünün. Bu aralığın içinden sayılar seçebiliriz. Bu sayılar `float`tır.

Benzer şekilde, 0.5 ile 0.6 arasındaki sayıları düşünün. Bu aralıktaki sayıları da seçebiliriz. Bunlar da `float`tır.

Bu süreci, farklı sayılar için yakınlaştırarak sürdürmeye devam edebiliriz. Elbette bir sınır vardır, ancak bu sınır oldukça küçüktür.

## 🔁 Tür Dönüştürme ( *Typecasting* )

Python'da bir ifadenin türünü değiştirebilirsiniz; buna *typecasting* (tür dönüştürme) denir.

Bir `int`i `float`a dönüştürebilirsiniz. Örneğin, 2 tamsayısını `float` 2.0'a dönüştürebilir veya *cast* edebilirsiniz.

Bu durumda gerçekte pek bir şey değişmez; ancak bir `float`ı tamsayıya dönüştürürseniz dikkatli olmalısınız.

Örneğin, 1.1 `float`ını 1'e dönüştürürseniz, bazı bilgileri kaybedersiniz.

Bir `string` bir tamsayı değeri içeriyorsa, onu `int`e dönüştürebilirsiniz. Tamsayı olmayan bir değer içeren bir `string`i dönüştürmeye çalışırsak, bir hata alırız.

Daha fazla örnek için laboratuvara göz atın.

Bir `int`i `string`e veya bir `float`ı `string`e dönüştürebilirsiniz.

## ✅ Boolean (Mantıksal) Türü

`Boolean`, Python'da bir diğer önemli türdür. Bir *Boolean* iki değer alabilir.

İlk değer `True`'dur; büyük harf **T** kullandığımızı unutmayın.

Boolean değerler ayrıca büyük harf **F** ile `False` da olabilir.

Bir Boolean değer için `type` komutunu kullandığımızda, `bool` terimini elde ederiz. Bu, *Boolean*ın kısaltmasıdır; bir Boolean `True` değeri bir tamsayıya veya `float`a dönüştürülürse, 1 elde ederiz.

Bir Boolean `False` değerini tamsayıya veya `float`a dönüştürürsek, 0 elde ederiz.

1'i Boolean'a dönüştürürseniz, `True` elde edersiniz. Benzer şekilde, 0'ı Boolean'a dönüştürürseniz, `False` elde edersiniz.
