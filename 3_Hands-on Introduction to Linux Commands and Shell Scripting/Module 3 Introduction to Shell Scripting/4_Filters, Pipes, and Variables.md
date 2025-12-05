# 🧮 Filtreler, Pipe ve Değişkenler

## 👋 Giriş

Filtreler, borular ( *pipes* ) ve değişkenlere hoş geldiniz.

Bu videoyu izledikten sonra:

* *Pipes* ve filtreleri açıklayabilecek ve kullanabileceksiniz.
* Kabuk ( *shell* ) ve ortam ( *environment* ) değişkenlerini açıklayabilecek ve ayarlayabileceksiniz.

---

## 🧱 Filtreler: Girdiden Çıktıya Dönüşüm

Filtreler, girdilerini genellikle standart girdiden ( *standard input* ), yani normalde klavyeden alan ve çıktılarını da standart çıktıya ( *standard output* ), yani normalde terminale döndüren kabuk komutları veya programlardır.

Bir filtreyi, girdi verisini çıktı verisine dönüştüren bir dönüştürücü program olarak düşünebiliriz.

Bunlara birçok örnek verilebilir; bunlar arasında `wc`, `cat`, `more`, `head`, `sort`, `grep` ve benzeri komutlar vardır.

Filtrelerin asıl değeri, birbirlerine zincirlenebilmeleridir; bu da bizi *pipe* komutuna getirir.

---

## 🔗 Pipe Komutu ile Komutları Zincirlemek

*Pipe* komutu, dikey çizgi (`|`) ile gösterilir ve kabukların işlevselliğini son derece genişletir.

Bu komut, filtre komutlarını ardışık bir şekilde birbirine zincirlemenize olanak tanır.

Kullanım deseni aşağıdaki gibidir:

* Birinci komutun çıktısı,
* İkinci komutun girdisi haline gelir,
* Ve bu böyle devam eder.

Şaşırtıcı olmayan bir şekilde  *pipe* , *pipeline* sözcüğünün kısaltmasıdır.

Örneğin, `ls` komutunun çıktısını `-r` seçeneği ile `sort` komutuna *pipe* edebilirsiniz:

```bash
ls | sort -r
```

Bu, dizin içeriğinin ters sıralanmış bir listesini üretir.

---

## 🐚 Kabuk Değişkenleri ( *Shell Variables* )

Kabuk değişkenleri, tanımlandıkları kabuğun kapsamı ile sınırlı olan değişkenlerdir.

Dolayısıyla, kabuklar birbirlerinin kabuk değişkenlerini göremezler.

Mevcut kabuk tarafından görülebilen tüm değişkenleri ve bunların tanımlarını listelemek için `set` komutunu çağırabilirsiniz.

Ancak `set` aynı zamanda çok sayıda ek bilgi de listelediğinden, sadece ilk dört değişken tanımını göstermek için çıktıyı `head` komutuna *pipe* edebilirsiniz:

```bash
set | head -4
```

---

### ✍️ Yeni Bir Kabuk Değişkeni Tanımlamak

Yeni bir kabuk değişkeni tanımlamak için, seçtiğiniz değişken adına `=` işaretiyle bir değer atamanız yeterlidir.

Dikkat edin: `=` işaretinin etrafında boşluk yoktur.

Örneğin, `hello` dizgesini saklayan `Greetings` adlı bir kabuk değişkeni tanımlayalım:

```bash
Greetings=hello
```

Yeni `Greetings` değişkeninin içeriğini görmek için, değerine erişmek amacıyla dolar işaretini (`$`) kullanır ve sonra bunu `echo` ile geri yazdırırsınız:

```bash
echo $Greetings
```

---

### 📦 Birden Fazla Değişkeni Görüntülemek

Birden fazla değişkeni de görüntüleyebilirsiniz.

Örneğin, değeri `world` olan başka bir `audience` değişkeni tanımlayalım:

```bash
audience=world
```

Ardından her iki değişkeni birden `echo` ile geri yazdırdığınızda:

```bash
echo "$Greetings $audience"
```

çıktı olarak `Hello World` elde edersiniz.

---

### 🧹 Bir Değişkeni Temizlemek

Bir değişkeni temizlemek için `unset` komutunu kullanırsınız.

Örneğin:

```bash
unset AUDIENCE
```

`AUDIENCE` değişkenini siler.

---

## 🌍 Ortam Değişkenleri ( *Environment Variables* )

Ortam değişkenleri, kabuk değişkenleriyle aynıdır; tek fark, kapsamlarının daha geniş olmasıdır.

Bu değişkenler, oluştukları kabuğun oluşturduğu tüm alt süreçlerde de ( *child processes* ) varlıklarını sürdürürler.

Herhangi bir kabuk değişkenini, üzerine `export` komutunu uygulayarak bir ortam değişkenine dönüştürebilirsiniz.

Örneğin:

```bash
export GREETINGS
```

komutu, `Greetings` değişkenini bir ortam değişkeni yapar.

Tüm ortam değişkenlerini listelemek için `env` komutunu kullanın:

```bash
env
```

---

### 🔍 Ortam Değişkenini Doğrulama

`Greetings` değişkeninin bir ortam değişkeni olarak dışa aktarılıp aktarılmadığını kontrol etmek için, `env` çıktısını `grep` komutuna *pipe* edip, sonucu `GREE` desenini kullanarak filtreleyebilirsiniz:

```bash
env | grep GREE
```

Gerçekten de, `Greetings` artık bir ortam değişkenidir.

---

## 📌 Özet

Bu videoda şunları öğrendiniz:

* Filtrelerin kabuk komutları olduğunu,
* `|` *pipe* operatörünün filtre komutlarını zincirlemenizi sağladığını,
* Kabuk değişkenlerine `=` ile değer atanabildiğini ve `set` komutuyla listelenebildiğini,
* Ortam değişkenlerinin, kabuğun tüm alt süreçlerine genişletilmiş kapsama sahip kabuk değişkenleri olduğunu.
