# 🧩 Bash Kabuk Özellikleri Örnekleri

## 🎯 Öğrenme Hedefleri

Bu okumayı tamamladıktan sonra şunları yapabileceksiniz:

* Metakarakter örneklerini listelemek
* Tırnaklamayı kullanarak karakterlerin düz (literal) veya özel anlamlarını belirtmek
* Girdi ve çıktı yönlendirmesini uygulamak
* Komut yerine koyma ( *command substitution* ) kullanmak
* Komut satırı argümanlarının uygulamalarını açıklamak

---

## 🔣 Metakarakterler (Metacharacters)

Metakarakterler, kabuğun talimat olarak yorumladığı özel anlama sahip karakterlerdir.

| Metakarakter | Anlamı                                        |
| ------------ | ---------------------------------------------- |
| `#`        | Bir yorumun önüne gelir                      |
| `;`        | Komut ayırıcı                               |
| `*`        | Dosya adı genişletme için joker karakter    |
| `?`        | Dosya adı genişletmede tek karakterlik joker |

---

### #️⃣ Pound `#`

Pound `#` metakarakteri, kabuk betiklerinde veya yapılandırma dosyalarında yorumları temsil etmek için kullanılır. Bir satırda `#` işaretinden sonra görünen herhangi bir metin yorum olarak değerlendirilir ve kabuk tarafından yok sayılır.

```bash
#!/bin/bash

# This is a comment
echo "Hello, world!"  # This is another comment
```

Yorumlar, kodunuzu veya yapılandırma dosyalarınızı belgelendirmek, bağlam sağlamak ve kodun amacını daha sonra okuyabilecek diğer geliştiricilere açıklamak için kullanışlıdır. Kodunuzu veya yapılandırma dosyalarınızı daha okunabilir ve sürdürülebilir hale getirmek için gerektiği yerlerde yorum eklemek en iyi uygulamalardan biridir.

---

### ➖ Noktalı Virgül `;`

Noktalı virgül `;` metakarakteri, tek bir komut satırında birden fazla komutu ayırmak için kullanılır. Birden fazla komut noktalı virgülle ayrıldığında, komut satırında göründükleri sırayla art arda çalıştırılırlar.

```bash
$ echo "Hello, "; echo "world!"
Hello,
world!
```

Yukarıdaki örnekte de görebileceğiniz gibi, her bir `echo` komutunun çıktısı ayrı satırlara yazdırılır ve komutların belirtilmiş olduğu sırayı izler.

Noktalı virgül metakarakteri, birden fazla komutu tek bir komut satırında art arda çalıştırmanız gerektiğinde kullanışlıdır.

---

### ✳️ Yıldız `*`

Yıldız `*` metakarakteri, hiçbir karakter dahil herhangi bir karakter dizisini temsil etmek için kullanılan bir joker karakterdir.

```bash
ls *.txt
```

Bu örnekte `*.txt`, geçerli dizindeki `.txt` uzantısına sahip herhangi bir dosyayla eşleşen bir joker kalıptır. `ls` komutu, eşleşen tüm dosyaların adlarını listeler.

---

### ❓ Soru İşareti `?`

Soru işareti `?` metakarakteri, herhangi bir tek karakteri temsil eden bir joker karakter olarak kullanılır.

```bash
ls file?.txt
```

Bu örnekte `file?.txt`, adının başlangıcında `file` bulunan, ardından herhangi tek bir karakter gelen ve `.txt` uzantısıyla biten geçerli dizindeki herhangi bir dosyayla eşleşen bir joker kalıptır.

---

## 🧷 Tırnaklama (Quoting)

*Tırnaklama* (quoting), bir komut argümanında veya kabuk betiğinde, karakterlerin, boşlukların veya diğer metakarakterlerin özel anlamını kaldırmanızı sağlayan bir mekanizmadır. Kabuğun karakterleri düz (literal) olarak yorumlamasını istediğinizde tırnaklama kullanırsınız.

| Sembol  | Anlamı                                                        |
| ------- | -------------------------------------------------------------- |
| `\`   | Metakarakter yorumlamasını kaçır (escape)                  |
| `" "` | Dize içinde metakarakterleri özel anlamlarına göre yorumla |
| `' '` | Dize içinde tüm metakarakterlerin yorumlanmasını kaçır   |

---

### ⬅️ Backslash `\`

Ters eğik çizgi karakteri `\` bir kaçış karakteri olarak kullanılır. Kabuğa, boşluk, sekme ve `$` gibi özel karakterlerin düz biçimde korunması talimatını verir. Örneğin, adında boşluk bulunan bir dosyanız varsa, bu boşlukları düz olarak ele almak için boşluktan önce ters eğik çizgi kullanabilirsiniz:

```bash
touch file\ with\ space.txt
```

*Kopyalandı!*

*Satır kaydırma değiştirildi!*

---

### 💬 Çift Tırnak `" "`

Bir dize çift tırnak `" "` içine alındığında, çoğu karakter düz olarak yorumlanır, ancak metakarakterler özel anlamlarına göre yorumlanır. Örneğin, `$` dolar karakterini kullanarak değişken değerlerine erişebilirsiniz:

```bash
$ echo "Hello $USER"
Hello <username>
```

*Kopyalandı!*

*Satır kaydırma değiştirildi!*

---

### 🔐 Tek Tırnak `' '`

Bir dize tek tırnak `' '` içine alındığında, tırnaklar arasındaki tüm karakterler ve metakarakterler düz olarak yorumlanır. Tek tırnaklar, yukarıdaki örneği aşağıdaki çıktıyı üretecek şekilde değiştirir:

```bash
$ echo 'Hello $USER'
Hello $USER
```

*Kopyalandı!*

*Satır kaydırma değiştirildi!*

Dikkat ederseniz, `$USER` değişkeninin değerini yazdırmak yerine, tek tırnaklar terminalin `"${USER}"` dizgesini yazdırmasına neden olur.

---

## 🔁 Girdi/Çıktı Yönlendirmesi (Input/Output Redirection)

| Sembol  | Anlamı                                           |
| ------- | ------------------------------------------------- |
| `>`   | Çıktıyı dosyaya yönlendir, üzerine yaz      |
| `>>`  | Çıktıyı dosyaya yönlendir, sonuna ekle       |
| `2>`  | Standart hatayı dosyaya yönlendir, üzerine yaz |
| `2>>` | Standart hatayı dosyaya yönlendir, sonuna ekle  |
| `<`   | Dosya içeriğini standart girdiye yönlendir     |

Girdi/çıktı (IO) yönlendirme, bir program ile onun girdi/çıktı kaynakları arasındaki veri akışını yönlendirme işlemidir.

Varsayılan olarak, bir program girdiyi standart girdi olan klavyeden okur ve çıktıyı standart çıktı olan terminale yazar. Ancak IO yönlendirme kullanarak, bir programın girdisini veya çıktısını bir dosyaya ya da başka bir programa yönlendirebilirsiniz.

---

### 📄 Çıktıyı Yönlendirme `>`

Bu sembol, bir komutun standart çıktısını belirtilen bir dosyaya yönlendirmek için kullanılır.

```bash
ls > files.txt
```

Bu komut, `files.txt` adlı bir dosya yoksa oluşturur ve `ls` komutunun çıktısını bu dosyaya yazar.

**Uyarı:** Dosya zaten mevcut olduğunda, çıktı dosyanın tüm içeriğinin üzerine yazar!

---

### ➕ Çıktıyı Yönlendirme ve Ekleme `>>`

Bu gösterim, bir komutun çıktısını bir dosyanın sonuna yönlendirmek ve eklemek için kullanılır. Örneğin:

```bash
ls >> files.txt
```

Bu komut, `ls` komutunun çıktısını `files.txt` dosyasının sonuna ekler ve dosyada daha önce var olan içeriği korur.

---

### ⚠️ Standart Hata Yönlendirme `2>`

Bu gösterim, bir komutun standart hata çıktısını bir dosyaya yönlendirmek için kullanılır. Örneğin, `ls` komutunu var olmayan bir dizin üzerinde aşağıdaki gibi çalıştırırsanız:

```bash
ls non-existent-directory 2> error.txt
```

Kabuk, `error.txt` adlı bir dosya yoksa oluşturur ve `ls` komutunun hata çıktısını bu dosyaya yönlendirir.

**Uyarı:** Dosya zaten mevcut olduğunda, hata iletisi dosyanın tüm içeriğinin üzerine yazar!

---

### ➕ Standart Hata Ekleyerek Yönlendirme `2>>`

Bu sembol, bir komutun standart hata çıktısını yönlendirir ve hata iletisini dosyanın mevcut içeriğinin üzerine yazmadan dosyanın sonuna ekler.

```bash
ls non-existent-directory 2>> error.txt
```

Bu komut, `ls` komutunun hata çıktısını `error.txt` dosyasının sonuna ekler.

---

### 📥 Girdiyi Yönlendirme `<`

Bu sembol, bir komutun standart girdisini bir dosyadan veya başka bir komuttan yönlendirmek için kullanılır. Örneğin:

```bash
sort < data.txt
```

Bu komut, `data.txt` dosyasının içeriğini sıralar.

---

## 🔄 Komut Yerine Koyma (Command Substitution)

Komut yerine koyma ( *command substitution* ), bir komutu çalıştırmanıza ve çıktısını başka bir komutun argümanının bir bileşeni olarak kullanmanıza olanak tanır. Komut yerine koyma, bir komutu ters tırnaklar içine alarak ``command`` ya da `$()` sözdizimini kullanarak belirtilir. Kapsanan komut yürütüldüğünde, çıktısı yerine konur ve başka bir komut içinde argüman olarak kullanılabilir. Bu, bir komutun çıktısının başka bir komut için girdi olarak kullanılmasını gerektiren görevlerin otomatikleştirilmesinde özellikle kullanışlıdır.

Örneğin, geçerli dizinin yolunu `pwd` komutuna komut yerine koyma uygulayarak bir değişkende saklayabilir, sonra başka bir dizine geçebilir ve son olarak `cd` komutunu sakladığınız değişken üzerinde çağırarak başlangıç dizininize geri dönebilirsiniz:

```bash
$ here=$(pwd)
$ cd path_to_some_other_directory
$ cd $here
```

*Kopyalandı!*

*Satır kaydırma değiştirildi!*

---

## 💻 Komut Satırı Argümanları

Komut satırı argümanları, bir program komut satırı arayüzünden çalıştırıldığında programa iletilebilen ek girdilerdir. Bu argümanlar, programın adından sonra belirtilir ve programın davranışını değiştirmek, girdi verisi sağlamak veya çıktı konumları belirtmek için kullanılabilir. Komut satırı argümanları, bir kabuk betiğine argüman geçirmek için kullanılır.

Örneğin, aşağıdaki komut, Bash betiğinizin içinden erişilebilecek `arg1` ve `arg2` olmak üzere iki argüman sağlar:

```bash
$ ./MyBashScript.sh arg1 arg2
```

*Kopyalandı!*

*Satır kaydırma değiştirildi!*

---

## 📌 Özet

Bu okumada şunları öğrendiniz:

* `#`, `;`, `*` ve `?` gibi metakarakterler, kabuğun özel anlamlarla yorumladığı karakterlerdir.
* Tırnaklama, özel karakterlerin, boşlukların veya diğer metakarakterlerin kabuk tarafından düz biçimde yorumlanmasını sağlamanıza olanak tanır.
* Girdi/çıktı yönlendirmesi, bir programın girdisinin veya çıktısının bir dosyaya yönlendirilmesini veya bir dosyadan alınmasını sağlar.
* Komut yerine koyma ( *command substitution* ), bir komutun çıktısını başka bir komut için argüman olarak kullanmanıza olanak tanır.
* Komut satırı argümanları, bir kabuk betiğine bilgi geçirmek için kullanılabilir.
