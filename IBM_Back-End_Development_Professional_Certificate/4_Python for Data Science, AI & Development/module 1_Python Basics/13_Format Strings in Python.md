# 🔤 Python'da Format String'ler

Format string'ler, Python'da değişkenleri bir string'in içine yerleştirmenin bir yoludur. String'leri biçimlendirmek ve çıktıları insanlar için daha okunabilir hâle getirmek için kullanılırlar.

Python'da string biçimlendirmek için birkaç farklı yol vardır:

---

## 🧩 String interpolation ( *f-string* 'ler)

Python 3.6 ile tanıtılan  *f-string* 'ler, Python'da string biçimlendirmenin yeni bir yoludur. Başına `f` öneki getirilir ve biçimlendirilecek değişkenleri sarmak için süslü parantezler `{}` kullanılır. Örneğin:


```python
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")
```

*Kopyalandı!*

*Satır kaydırma değiştirildi!*

Bu şu çıktıyı üretir:

1

```text
My name is John and I am 30 years old.
```


---

## 🧾 `str.format()`

Bu, Python'da string biçimlendirmenin bir başka yoludur. Süslü parantezler `{}` değişkenler için yer tutucu olarak kullanılır ve bu değişkenler `format()` metoduna argüman olarak geçirilir. Örneğin:

```python
name = "John"
age = 50
print("My name is {} and I am {} years old.".format(name, age))
```


Bu şu çıktıyı üretir:

1

```text
My name is John and I am 50 years old.
```

---

## 🔢 `%` Operatörü

Bu, Python'da string biçimlendirmek için kullanılan en eski yöntemlerden biridir. String içindeki değişkenleri değiştirmek için `%` operatörünü kullanır. Örneğin:

```python
name = "Johnathan"
age = 30
print("My name is %s and I am %d years old." % (name, age))
```

Bu şu çıktıyı üretir:

1

```text
My name is Johnathan and I am 30 years old.
```

“`My name is %s and I am %d years old.`”: Bu, format belirteçleri ( *format specifiers* ) içeren bir string'tir:

* `"%s"`: Bu, bir string için yer tutucudur.
* `"%d"`: Bu, bir tam sayı ( *integer* ) için yer tutucudur.
* `% (name, age)`: Bu, `name` ve `age` değişkenlerini içeren bir tuple'dır. Bu değişkenlerin değerleri string içindeki yer tutucuların yerini alacaktır.

Bu yöntemlerin her birinin kendi avantajları ve kullanım durumları vardır. Ancak, okunabilirlikleri ve performansları nedeniyle  *f-string* 'ler genellikle Python'da string biçimlendirmek için en modern ve tercih edilen yol olarak kabul edilir.

---

## ➕ Ek yetenekler (*f-string* ifadeleri*)

F-string'ler süslü parantezlerin `{}` içine yazılan ifadeleri de değerlendirebilir; bu da oldukça kullanışlı olabilir. Örneğin:

```python
x = 10
y = 20
print(f"The sum of x and y is {x+y}.")
```

Bu şu çıktıyı üretir:

1

```text
The sum of x and y is 30.
```

---

## 📁 Ham String ( *Raw String* , `r''`)

Python'da ham string'ler ( *raw string* ), özellikle kaçış karakterleri ( *escape characters* ) ile çalışırken metinsel veriyi ele almak için güçlü bir araçtır. Bir string literal'inin başına `r` harfini ekleyerek Python'a bu string'i ham olarak ele almasını söylersiniz; yani ters eğik çizgileri (`\`) kaçış dizileri olarak değil, olduğu gibi ( *literal karakterler* ) yorumlar.

Aşağıdaki normal ve ham string örneklerini ele alalım:

### 📄 Normal (regular) string:

```python
regular_string = "C:\new_folder\file.txt"
print("Regular String:", regular_string)
```

Bu şu çıktıyı üretir:

```text
Regular String:  C:
ew_folderile.txt
```

Normal string olan `regular_string` değişkeninde ters eğik çizgiler (`\n`) kaçış dizileri olarak yorumlanır. Dolayısıyla `\n`, yeni satır karakterini ( *newline character* ) temsil eder ve bu da dosya yolu gösteriminin yanlış olmasına yol açar.

### 📄 Ham (raw) string:

```python
raw_string = r"C:\new_folder\file.txt"
print("Raw String:", raw_string)
```

Bu şu çıktıyı üretir:

1

```text
Raw String: C:\new_folder\file.txt
```

Ancak ham string olan `raw_string` içinde ters eğik çizgiler ( *backslash* ) olduğu gibi, yani *literal karakter* olarak ele alınır. Bu, `\n` dizisinin yeni satır karakteri olarak değil, iki ayrı karakter olan `\` ve `n` olarak yorumlandığı anlamına gelir.

Sonuç olarak, dosya yolu tam olarak göründüğü şekliyle temsil edilir.
