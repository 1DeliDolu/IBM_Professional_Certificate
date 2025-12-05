# 🧪 İleri Düzey Bash Betiklemeye Giriş

Final projenin uygulamalı laboratuvar kısmında, derste henüz ele alınmamış daha ileri düzey betik komutlarını ve kavramlarını kullanacaksınız.

Bu okuma, bu daha gelişmiş kavramlara aşina olmanızı sağlayarak laboratuvarı güvenle tamamlamanıza yardımcı olacaktır.

---

## 🎯 Amaçlar

Bu okumayı tamamladıktan sonra, aşağıdakileri yapabilen Bash betikleri oluşturabileceksiniz:

* Belirlenmiş bir koşul yalnızca doğru olduğunda bir komut kümesini çalıştırmak için koşullu ifadeler kullanmak
* Doğru/yanlış karşılaştırmaları oluşturmak için mantıksal operatörler uygulamak
* Temel aritmetik hesaplamaları gerçekleştirmek
* Liste benzeri diziler ( *arrays* ) oluşturmak ve elemanlarına erişmek
* Bir döngü indeksine bağlı olarak işlemleri tekrar tekrar yürütmek için `for` döngülerini uygulamak

---

## 🔀 Koşullar (Conditionals)

Koşullar ( *conditionals* ) veya `if` ifadeleri, bir betiğe yalnızca belirli bir koşul altında bir şey yapmasını söylemenin bir yoludur.

Bash betik koşulları aşağıdaki `if-then-else` sözdizimini kullanır:

```bash
if [ condition ]
then
    statement_block_1  
else
    statement_block_2  
fi
```

Koşul doğruysa, Bash `statement_block_1` içindeki ifadeleri yürütür ve ardından koşullu kod bloğundan çıkar. Çıktıktan sonra, kapanış `fi` ifadesinden sonraki komutları çalıştırmaya devam eder.

Alternatif olarak, koşul yanlışsa Bash bu kez `else` satırı altındaki `statement_block_2` içindeki ifadeleri çalıştırır, ardından koşullu bloktan çıkar ve kapanış `fi`den sonraki komutları çalıştırmaya devam eder.

**İpuçları:**

* Köşeli parantezler `[ ]` içinde yer alan koşulun etrafına her zaman boşluk koymalısınız.
* Her `if` koşul bloğu, Bash’e koşul bloğunun nerede bittiğini söyleyen bir `fi` ile eşleştirilmelidir.
* `else` bloğu isteğe bağlıdır ancak önerilir. Eğer koşul `else` bloğu olmadan yanlış değerlendirirse, `if` koşul bloğu içinde hiçbir şey olmaz. Koşulun yanlış değerlendirildiğini belirtmek için `statement_block_2` içinde yorum `echo`’lamak gibi seçenekleri düşünün.

Aşağıdaki örnekte, koşul, bir Bash betiği tarafından okunan komut satırı argümanlarının sayısının `$#`, 2’ye eşit olup olmadığını kontrol eder:

```bash
if [[ $# == 2 ]]
then
  echo "number of arguments is equal to 2"
else
  echo "number of arguments is not equal to 2"
fi
```

Burada, koşul `[[ $# == 2 ]]` içinde kullanılan çift köşeli parantezlere dikkat edin; bu sözdizimi, koşul içinde tamsayı karşılaştırmaları yapmak için gereklidir.

Dize ( *string* ) karşılaştırmaları da yapabilirsiniz. Örneğin, `string_var` adlı ve değeri `"Yes"` olan bir değişkeniniz olduğunu varsayın. O zaman aşağıdaki ifade doğru olarak değerlendirilir:

```bash
[ $string_var == "Yes" ]
```

Dize karşılaştırmaları yaparken yalnızca tek köşeli parantezlere ihtiyacınız olduğuna dikkat edin.

Ayrıca `"and"` operatörü `&&` veya `"or"` operatörü `||` kullanarak birden fazla koşulun sağlanmasını da isteyebilirsiniz. Örneğin:

```bash
if [ condition1 ] && [ condition2 ]
then
    echo "conditions 1 and 2 are both true"
else
    echo "one or both conditions are false"
fi
```

```bash
if [ condition1 ] || [ condition2 ]
then
    echo "conditions 1 or 2 are true"
else
    echo "both conditions are false"
fi
```

---

## 🧠 Mantıksal Operatörler (Logical operators)

Aşağıdaki mantıksal operatörler, bir `if` koşul bloğu içindeki koşulda tamsayıları karşılaştırmak için kullanılabilir.

### `==`: eşittir ( *is equal to* )

Bir `a` değişkeninin değeri 2 ise, aşağıdaki koşul doğru olarak değerlendirilir; aksi halde yanlış olarak değerlendirilir.

```bash
$a == 2
```

### `!=`: eşit değildir ( *is not equal to* )

Bir `a` değişkeninin değeri 2’den farklıysa, aşağıdaki ifade doğru olarak değerlendirilir. Değeri 2 ise yanlış olarak değerlendirilir.

```bash
a != 2
```

**İpucu:** Mantıksal olumsuzlama operatörü `!`, doğruyu yanlışa ve yanlışı doğruya çevirir.

### `<=`: küçük veya eşit ( *is less than or equal to* )

Bir `a` değişkeninin değeri 2 ise, aşağıdaki ifade doğru olarak değerlendirilir:

```bash
a <= 3
```

ve aşağıdaki ifade yanlış olarak değerlendirilir:

```bash
a <= 1
```

Alternatif olarak, `<=` yerine eşdeğer gösterim olan `-le` kullanabilirsiniz:

```bash
a=1
b=2
if [ $a -le $b ]
then
   echo "a is less than or equal to b"
else
   echo "a is not less than or equal to b"
fi
```

Burada yalnızca birkaç mantıksal operatör örneği verdik. Daha fazlasını öğrenmek için Advanced Bash-Scripting Guide gibi kaynakları inceleyebilirsiniz.

---

## ➗ Aritmetik Hesaplamalar (Arithmetic calculations)

Tamsayı toplama, çıkarma, çarpma ve bölme işlemlerini `$(( ))` gösterimini kullanarak yapabilirsiniz.

Örneğin, aşağıdaki iki komut kümesinin her ikisi de 3 ile 2’nin toplamının sonucunu gösterir.

```bash
echo $((3+2))
```

veya

```bash
a=3
b=2
c=$(($a+$b))
echo $c
```

Bash, tamsayı aritmetiğini yerel olarak işler ancak kayan noktalı ( *floating-point* ) aritmetiği işlemez. Sonuç olarak, bir hesaplama sonucunun ondalık kısmını her zaman keser.

Örneğin:

```bash
echo $((3/2))
```

çıktı olarak kesilmiş tamsayı sonucu olan `1` değerini verir, kayan noktalı sayı olan `1.5` değerini değil.

Aşağıdaki tablo temel aritmetik operatörleri özetler:

| Sembol | İşlem   |
| ------ | --------- |
| `+`  | toplama   |
| `-`  | çıkarma |
| `*`  | çarpma   |
| `/`  | bölme    |

**Tablo: Aritmetik operatörler**

---

## 🧺 Diziler (Arrays)

Dizi ( *array* ), Bash’in yerleşik veri yapısıdır. Bir dizi, parantez içinde tutulan ve boşlukla ayrılmış bir listedir.

Bir dizi oluşturmak için adını ve içeriğini bildirirsiniz:

```bash
my_array=(1 2 "three" "four" 5)
```

Bu ifade, `my_array` dizisini parantez içindeki öğelerle doldurur: `1`, `2`, `"three"`, `"four"` ve `5`.

Boş bir dizi oluşturmak için ise şunu kullanabilirsiniz:

```bash
declare -a empty_array
```

Diziyi oluşturduktan sonra ona öğeler eklemek isterseniz, dizinize bir seferde bir eleman ekleyerek öğe ekleyebilirsiniz:

```bash
my_array+=("six")
my_array+=(7)
```

Bu, `"six"` ve `7` öğelerini `my_array` dizisine ekler.

Dizine indeksleme kullanarak, bir dizinin tekil veya birden fazla elemanına erişebilirsiniz:

```bash
# print the first item of the array:
echo ${my_array[0]}
# print the third item of the array:
echo ${my_array[2]}
# print all array elements:
echo ${my_array[@]}
```

**İpucu:** Dizi indekslemesinin 1’den değil, 0’dan başladığına dikkat edin.

---

## 🔁 `for` Döngüleri (for loops)

Dizi elemanlarının tümü üzerinde yineleme ( *iterate* ) yapmak için, indeksleme ile birlikte kullanılan `for` döngüsü adlı bir yapı kullanabilirsiniz.

Örneğin, aşağıdaki `for` döngüleri, her bir eleman yazdırılana kadar tekrar tekrar çalışmaya devam eder:

```bash
for item in ${my_array[@]}; do
  echo $item
done
```

veya

```bash
for i in ${!my_array[@]}; do
  echo ${my_array[$i]}
done
```

`for` döngüsü, döngüden geçebilmek için `; do` bileşenine ihtiyaç duyar. Ek olarak, `for` döngü bloğunu bir `done` ifadesiyle sonlandırmanız gerekir.

Kaç yineleme yapmak istediğinizi bildiğinizde `for` döngüsünü uygulamanın başka bir yolu da aşağıdaki gibidir. Örneğin, aşağıdaki kod 0’dan 6’ya kadar olan sayıları yazdırır:

```bash
N=6
for (( i=0; i<=$N; i++ )) ; do
  echo $i
done
```

`for` döngülerini her türlü işi gerçekleştirmek için kullanabilirsiniz. Örneğin, bir dizideki öğelerin sayısını hesaplayabilir veya dizinin elemanlarının toplamını alabilirsiniz; aşağıdaki Bash betiği bunu yapar:

```bash
#!/usr/bin/env bash
# initialize array, count, and sum
my_array=(1 2 3)
count=0
sum=0
for i in ${!my_array[@]}; do
  # print the ith array element
  echo ${my_array[$i]}
  # increment the count by one
  count=$(($count+1))
  # add the current value of the array to the sum
  sum=$(($sum+${my_array[$i]}))
done
echo $count
echo $sum
```

Bu döngünün nasıl çalıştığını anlamak için bu betiği çalıştırmayı deneyin.

---

## ✅ Özet

Bu laboratuvarda şunları öğrendiniz:

* Koşullu ifadeler, belirli bir koşulun doğru olup olmamasına göre komutları çalıştırmak için kullanılabilir.
* Mantıksal operatörler, doğru/yanlış karşılaştırmaları yapar.
* Aritmetik operatörler, temel aritmetik hesaplamaları gerçekleştirir.
* Liste benzeri diziler oluşturabilir ve bu dizilerin tek tek elemanlarına erişebilirsiniz.
* `for` döngüleri, bir döngü indeksine bağlı olarak işlemleri tekrar tekrar yürütür.

Tebrikler! Artık edindiğiniz yeni bilgileri, sıradaki uygulamalı laboratuvarda pratiğe dökmeye hazırsınız.
