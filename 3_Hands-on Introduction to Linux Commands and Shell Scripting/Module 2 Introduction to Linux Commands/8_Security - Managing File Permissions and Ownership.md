# 🔐 Güvenlik: Dosya İzinlerini ve Sahipliğini Yönetme

## 🎯 Öğrenme hedefleri

Bu okumayı tamamladıktan sonra şunları yapabileceksiniz:

* Dosya sahipliğini ve izinlerini açıklamak
* Dosya ve dizin izinlerini görüntülemek
* Bir dosyayı özel hâle getirmek

---

## ❓ Dosya izinlerine ve sahipliğine neden ihtiyaç duyarız?

Linux, çok kullanıcılı ( *multi-user* ) bir işletim sistemidir. Bu, varsayılan olarak sistemde sakladığınız dosyaların diğer kullanıcılar tarafından görüntülenebilir olduğu anlamına gelir.

Ancak, kişisel vergi belgeleriniz veya işvereninizin fikri mülkiyet belgeleri gibi özel ya da gizli bazı dosyalarınız olabilir. Bu hassas belgeleri başkaları tarafından görüntülenmekten veya değiştirilmekten nasıl koruyabilirsiniz?

---

## 👥 Dosya sahipliği ve izinleri

Linux’ta üç olası dosya sahipliği seviyesi vardır:  **kullanıcı (user)** , **grup (group)** ve  **diğer (other)** .

Bir dosyayı kim oluşturursa, yani oluşturma anındaki kullanıcı, varsayılan olarak o dosyanın sahibi olur. Bir kullanıcı grubu da bir dosyanın sahipliğini paylaşabilir.

*Other* (diğer) kategorisi ise, temelde Linux makinenize erişimi olan “evrendeki” herhangi bir kişiyi ifade eder – bu seviyeye sahiplik izni atarken dikkatli olun!

Yalnızca bir dosyanın resmi sahibi, o dosyanın izinlerini değiştirebilir. Bu, sadece sahiplerin dosyayı kimin okuyabileceğine, dosyaya yazıp yazamayacağına veya onu çalıştırıp çalıştıramayacağına karar verebileceği anlamına gelir.

---

## 👁️ Dosya izinlerini görüntüleme

Diyelim ki aşağıdaki komut satırlarını girdiniz:

```bash
$ echo "Who can read this file?" > my_new_file
$ more my_new_file
Who can read this file?
$ ls -l my_new_file
-rw-r--r-- 1 theia users 25 Dec 22 17:47 x
```

Burada, `"Who can read this file?"` dizgesini `my_new_file` adlı yeni bir dosyaya *echo* komutuyla yazdık.

Sonraki satır, yeni dosyanın içeriğini yazdırmak için `more` komutunu kullanır.

Son olarak, `-l` seçeneğiyle kullanılan `ls` komutu, dosyanın (varsayılan) izinlerini görüntüler: `rw-r--r--`

İlk üç karakter (`rw-`), **kullanıcı izinlerini** tanımlar; sonraki üç (`r--`),  **grup izinlerini** ; son üç (`r--`) ise  **diğerlerinin izinlerini** .

Bu durumda siz, kullanıcı olarak `rw-` iznine sahipsiniz; bu da varsayılan olarak **okuma (r)** ve **yazma (w)** izinleriniz olduğu, ancak **çalıştırma (execute)** izniniz olmadığı anlamına gelir. Aksi hâlde, sondaki `-` yerine `x` olurdu.

Dolayısıyla, tüm satıra `rw-r--r--` olarak baktığınızda,  **herkesin dosyayı okuyabildiğini** , **hiç kimsenin çalıştıramadığını** ve **yalnızca sizin dosyaya yazabildiğinizi** görebilirsiniz.

> Not: Terminalde satırın en başındaki `-` işareti, izinlerin bir **dosyaya** ait olduğunu gösterir. Eğer bir **dizine** ait izinleri görseydiniz, en başta “directory” (dizin) anlamına gelen bir `d` görürdünüz.

---

## 📁 Dizin izinleri

Dizinler için izinler, dosyalarla benzer ama onlardan farklıdır. Dizinler de aynı `rwx` formatını kullanır, ancak sembollerin anlamı biraz farklıdır.

Aşağıdaki tablo, dizinler için her iznin anlamını göstermektedir:

| Dizin izni | İzin verilen eylem(ler)                              |
| ---------- | ----------------------------------------------------- |
| `r`      | `ls`komutunu kullanarak dizin içeriğini listeleme |
| `w`      | Dosya veya dizin ekleme ya da silme                   |
| `x`      | `cd`komutunu kullanarak dizine girme                |

Dizinler üzerinde uygun izinler ayarlamak, hem güvenlik hem de sistem kararlılığı açısından **en iyi uygulamalardan** ( *best practice* ) biridir.

Bu okuma güvenlik tarafına odaklanıyor olsa da, dosya izinlerini ve sahipliğini ayarlamanın diğer nedenlerini bu kursun ilerleyen kısımlarında daha ayrıntılı öğreneceksiniz.

---

## 🔒 Bir dosyayı özel hâle getirme

Grubunuzun ve diğer tüm kullanıcıların okuma izinlerini `chmod` komutunu kullanarak kaldırabilirsiniz.

Başarılı bir değişiklik yaptığınızdan emin olmak için `ls -l` komutunu tekrar kullanın:

```bash
chmod go-r my_new_file
ls -l my_new_file
-rw------- 1 theia users 24 Dec 22 18:49 my_new_file
```

`chmod` komutunda, `go-r` uygulanacak izin değişikliğidir; bu örnekte, **grup (g)** ve **diğer (o)** kullanıcılar için **okuma (r)** izninin kaldırılması anlamına gelir.

`chmod` komutu hem dosyalar hem de dizinler için kullanılabilir.

---

## ⚙️ Çalıştırılabilir dosyalar – ileriye bakış

Bir dosyayı okuyup yazmanın ne anlama geldiğini öğrendiniz, peki Linux’ta bir dosyayı çalıştırma iznine sahip olmak ne anlama gelir?

Bir Linux dosyası, işletim sistemi tarafından doğrudan yorumlanabilecek talimatlar içeriyorsa **çalıştırılabilir** ( *executable* ) kabul edilir. Temelde, çalıştırılabilir bir dosya,  **çalıştırılmaya hazır bir programdır** . Bu tür dosyalar *binary* (ikili) ya da *executable* (çalıştırılabilir) olarak da adlandırılır.

Bu kursta, **betik (script)** adı verilen özel bir tür çalıştırılabilir dosyayla çok haşır neşir olacaksınız. Betik, bir **betik dilinde (scripting language)** yazılmış bir programdır.

 *Shell scripting* , daha özel olarak  *Bash scripting* , yani çok popüler bir kabuk betik dili olan **Bash (Bourne Again Shell)** ile betikler yazmak, hakkında her şeyi öğreneceksiniz.

Bir  **kabuk betiği (shell script)** , bir kabuk tarafından yorumlanabilen düz metin ( *plain text* ) dosyasıdır.

Resmî olarak konuşursak, bir metin dosyasının belirli bir kullanıcı için çalıştırılabilir bir kabuk betiği sayılabilmesi için iki şeye sahip olması gerekir:

* O kullanıcı için ayarlanmış **çalıştırma (execute) izni**
* İşletim sistemine kendisini bir *binary* olarak bildirmek için ilk satırında, **“shebang”** adı verilen bir yönerge ( *directive* )

Kabuk betikleme konusuna geldiğimizde, tüm bunlar sizin için çok daha net hâle gelecektir.

---

## 📝 Özet

Bu okumada şunları öğrendiniz:

* Linux’ta dosya sahipliğinin, bir dosyayı kimin okuyabileceğini, dosyaya yazabileceğini ve onu çalıştırabileceğini belirleyen **üç seviyesi** vardır:  **kullanıcı (user)** , **grup (group)** ve  **diğer (other)** .
* Dosya ve dizin izinlerini görüntülemek için `ls -l` komutunu kullanabilirsiniz.
* Bir dosyanın izinlerini değiştirmek için `chmod` komutunu kullanabilirsiniz.
