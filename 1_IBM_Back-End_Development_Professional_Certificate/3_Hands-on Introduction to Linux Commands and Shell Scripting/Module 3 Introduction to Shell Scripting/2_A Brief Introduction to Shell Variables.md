# 📘 Shell Değişkenlerine Kısa Bir Giriş

## 🎯 Öğrenme Hedefleri

Bu okumayı tamamladıktan sonra şunları yapabileceksiniz:

* Shell değişkenlerini tanımlamak
* Shell değişkenleri oluşturmak

---

## ❓ Shell Değişkeni Nedir?

Shell değişkenleri, sayılar, karakter dizeleri ve diğer veri yapıları gibi bilgileri bir isimle saklamak ve daha sonra bu bilgilere erişmek veya onları değiştirmek için güçlü bir yol sunar.

Fikri kavramak için bazı temel örneklere bakalım.

Şu örneği ele alın:

```bash
$ firstname=Jeff
$ echo $firstname
Jeff
```

İlk satır, `firstname` adlı yeni bir değişkene `Jeff` değerini atar.

Sonraki satır, `echo` komutunu ve değişken adının önüne konan özel karakter `$` işaretini kullanarak değişkenin değerine erişir ve onu görüntüler; bu değer, `Jeff` dizgesidir.

Böylece, değeri `Jeff` olan `firstname` adında yeni bir shell değişkeni oluşturmuş olduk.

Bu, tek adımda bir shell değişkeni oluşturmanın ve onu bir değere atamanın en temel yoludur.

---

## ⌨️ Komut Satırında Kullanıcı Girdisini Shell Değişkenine Okuma

Shell değişkeni oluşturmanın bir başka yolu da `read` komutunu kullanmaktır.

Aşağıdakini girdikten sonra:

```bash
$ read lastname
```

komut satırında shell, sizin bir metin girmenizi bekler:

```bash
$ read lastname
Grossman
$
```

Kopyalandı!

Wrap Toggled!

Şimdi, `Grossman` değerinin `read` komutu tarafından `lastname` değişkenine az önce kaydedildiğini görebiliriz:

```bash
$ read lastname
Grossman
$ echo $lastname
Grossman
```

Bu arada, birden fazla değişkenin değerini aynı anda `echo` komutuyla yazdırabileceğinizi fark edin:

```bash
$ echo $firstname $lastname
Jeff Grossman
```

Yakında göreceğiniz gibi, `read` komutu özellikle shell script’lerinde çok kullanışlıdır.

Bunu bir shell script içinde, kullanıcıları bilgi girmeleri için uyarmak (prompt etmek) amacıyla kullanabilirsiniz; girilen bilgi daha sonra bir shell değişkenine kaydedilir ve script çalışırken shell script tarafından kullanılabilir hale gelir.

Ayrıca, bir script’e geçirilebilen ve otomatik olarak shell değişkenlerine atanabilen komut satırı argümanları hakkında da bilgi edineceksiniz.

---

## 📝 Özet

Bu okumada şunları öğrendiniz:

* Shell değişkenleri, değerleri saklar ve kullanıcıların bu değerlere daha sonra isimleriyle erişmesine olanak tanır.
* Shell değişkenlerini, bir shell değişkeni ve değerini bildirerek veya `read` komutunu kullanarak oluşturabilirsiniz.
