# 📁 Dosya ve Dizin Yönetim Komutları

## 🎬 “Dosya ve Dizin Yönetim Komutları”na Hoş Geldiniz

“File and Directory Management Commands” (Dosya ve Dizin Yönetim Komutları) oturumuna hoş geldiniz.

Bu videoyu izledikten sonra şunları yapabileceksiniz:

* Dosya ve dizinleri oluşturmak ve silmek
* Dosya ve dizinleri kopyalamanın ve taşımanın ( *move* ) nasıl çalıştığını keşfetmek
* Dosyaları çalıştırılabilir ( *executable* ) hale getirmek için dosya izinlerini nasıl yöneteceğinizi keşfetmek

---

## 📂 Dizin Oluşturma: `mkdir`

 **`make directory` komutu** , dizin oluşturmak için kullanılır.

Diyelim ki şu anda içi boş olan *documents* klasörünüzdesiniz.

`test` adında bir klasör oluşturmak için yalnızca şunu yazarsınız:

```bash
mkdir test
```

Artık geçerli dizininizde `test` adında bir alt klasör vardır.

---

## 🗑️ Dosya ve Dizin Silme: `rm` ve `rm -r`

`rm` komutu, bir dosya veya dizini kaldırmanıza ( *remove* ) olanak tanır.

Solda gösterildiği gibi bir dosya yapınız olduğunu varsayalım. Ve *documents* klasöründesiniz, `file1` öğesini kaldırmak istiyorsunuz. Bunu yalnızca şunu yazarak yapabilirsiniz:

```bash
rm file1
```

Artık yalnızca `folder1`’in kaldığını görebilirsiniz.

`folder1` dizinini, içinde başka dosyalar bulunabileceği için, basitçe kaldıramazsınız. Ancak, `rm` komutunu `-r` seçeneğiyle kullanarak bunu kolayca aşabilirsiniz.

`-r` seçeneği, dizini tüm alt dosya nesneleriyle birlikte kaldırmak istediğinizi ifade eder:

```bash
rm -r folder1
```

Artık *Documents* klasörünüz boştur.

Bu nedenle, `rm` komutunu `-r` seçeneğiyle kullanırken her zaman dikkatli olmalısınız. Önemli veriler içeren klasörleri yanlışlıkla kaldırmak çok kolaydır.

---

## 🗂️ Boş Dizin Silme: `rmdir`

Şimdi, `mkdir` komutuyla boş bir dizin oluşturduğunuzu ve sonrasında bunu kaldırmaya karar verdiğinizi varsayalım.

`rm` komutunun `-rf` seçeneğini kullanmak önerilmez. Bunun yerine yalnızca boş dizinleri kaldırmak için kullanılan `rmdir` komutunu kullanmalısınız. Bu komut, yanlışlıkla önemli dosya veya dizinleri silmemenizi garanti eder.

```bash
rmdir test
```

`ls` komutunu girmeniz, geçerli dizinin gerçekten boş olduğunu gösterir:

```bash
ls
```

---

## 📄 Dosya Oluşturma ve Zaman Bilgisi Güncelleme: `touch`

`touch` komutu, boş dosyalar oluşturmak için kullanılabilir.

Diyelim ki içi boş olan *Documents* klasörünüzdesiniz ve birkaç boş metin dosyası oluşturmak istiyorsunuz. Bunu, `touch` komutuyla birlikte bazı dosya adları vererek yapabilirsiniz: `.txt` uzantılı `"a"`, `"b"`, `"c"` ve `"d"`.

```bash
touch a.txt b.txt c.txt d.txt
```

Artık *Documents* klasörünüzde oluşturduğunuz dört dosyanın bulunduğunu görebilirsiniz.

`touch` komutunun mevcut bir dosyaya ne yaptığını merak edebilirsiniz.

Geçerli dizininizde `notes.txt` adında bir dosya olduğunu varsayalım. Bu dosyanın en son ne zaman değiştirildiğini şununla görebilirsiniz:

```bash
date -r notes.txt
```

`notes.txt` dosyası üzerinde `touch` komutunu kullanırsanız, dosyanın son değiştirilme tarihinin geçerli zamana güncellendiğini görebilirsiniz:

```bash
touch notes.txt
date -r notes.txt
```

---

## 📑 Dosya ve Dizin Kopyalama: `cp` ve `cp -r`

`cp` komutu, bir dosya veya dizini kopyalamanıza olanak tanır.

Dosyaları kopyalamak için:

* Bir kaynaktan ( *source directory* ) bir dosya kopyalayıp, hedef dizinde dosya adı belirtebilirsiniz, veya
* Hedef dosya adını atlayabilir ve aynı dosya adını kullanmaya devam edebilirsiniz.

Tüm dizinleri kopyalamak için, `cp` komutuna `-r` seçeneğini vermeniz gerekir; böylece tüm alt dizinleri ve dosyaları özyinelemeli ( *recursively* ) olarak kopyalayacağını bilir.

Birkaç örneğe bakalım:

Çalışma dizininizde `notes.txt` adında bir dosyanız ve `Documents` adında bir klasörünüz olduğunu varsayalım. `notes.txt` dosyasını `Documents` klasörünüze şu komutla kopyalayabilirsiniz:

```bash
cp notes.txt Documents
```

Artık *Documents* klasörünüzün `notes.txt` dosyasının bir kopyasını içerdiğini görebilirsiniz.

Kaynak dizin belirtmeniz gerekmediğine dikkat edin; çünkü `cp` varsayılan olarak geçerli dizininizi kullanır.

Sonraki adımda, solda verilen sözdizimini ( *syntax* ) kullanarak `Documents` klasörünüzün bir kopyasını `Docs_copy` adında oluşturabilirsiniz:

```bash
cp -r Documents Docs_copy
```

Beklendiği gibi, artık orijinal *Documents* klasörüyle aynı içeriğe sahip `Docs_copy` adlı bir klasörünüz vardır.

---

## 📦 Dosya ve Dizin Taşıma / Yeniden Adlandırma: `mv`

`mv` komutu, bir dosya veya dizini taşımanıza ( *move* ) olanak tanır.

Dosyaları taşımak için, `mv` komutunu; taşımak istediğiniz dosyaların yollarını ve bunları taşımak istediğiniz klasörü art arda yazarak kullanabilirsiniz.

Benzer şekilde, dizinleri taşımak için, taşınacak dizinin yolunu ve ardından taşınacağı yol ve dizini yazarsınız.

Bir örneğe bakalım:

Çalışma dizininizde `my_script.sh` adında bir dosya ve `Scripts`, `Notes` ve `Documents` adında üç klasör olduğunu varsayalım. Solda verilen sözdizimini kullanarak `my_script.sh` dosyasını `Scripts` klasörünüze taşıyabilirsiniz:

```bash
mv my_script.sh Scripts
```

Buna göre:

```bash
ls my_script.sh
```

komutunu girmeniz hiçbir şey döndürmezken,

```bash
ls Scripts
```

komutunu girmeniz, `my_script.sh` dosyasını başarıyla `Scripts` klasörünüze taşıdığınızı gösterir.

Sonraki adımda, soldaki sözdizimini kullanarak `Notes` ve `Scripts` klasörlerinizi `Documents` klasörünüze taşıyabilirsiniz:

```bash
mv Notes Scripts Documents
```

Artık dizininizin yalnızca `Documents` klasörünü içerdiğini ve `Documents` klasörünüzün, az önce taşıdığınız `Scripts` ve `Notes` klasörlerini içerdiğini görebilirsiniz.

---

## 🔐 Dosya İzinlerini Yönetme: `chmod`

`chmod`, *“change mode”* ifadesinin kısaltmasıdır ve dosyalardaki okuma ( *read* ), yazma ( *write* ) ve çalıştırma ( *execute* ) izinlerini değiştirmek için kullanılır.

Geçerli dizininizde, içeriğinde `"Learning Linux is fun!"` yazan `my_script.sh` adında bir kabuk betiği ( *shell script* ) dosyanız olduğunu varsayalım.

```bash
ls -l my_script.sh
```

komutunu girdiğinizde, betiğinizin okuma ve yazma izinlerine sahip olduğunu, bunun da `r` ve `w` karakterleriyle gösterildiğini görürsünüz.

Ancak dosyayı çalıştırmayı denerseniz, bir *permission denied* (izin reddedildi) hatası alırsınız.

Betik dosyanızı çalıştırılabilir ( *executable* ) hale getirmek için, `my_script.sh` üzerinde `chmod` komutunu `+x` seçeneğiyle çağırırsınız:

```bash
chmod +x my_script.sh
ls -l my_script.sh
```

Artık çıktıda `my_script.sh` dosyasının çalıştırma iznine sahip olduğunu, bunun da `x` karakteriyle gösterildiğini görebilirsiniz.

Harika! Şimdi betiği çalıştırmak işe yarar:

```bash
./my_script.sh
```

---

## ✅ Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* Yeni bir dosya oluşturmak veya var olan bir dosyanın son değiştirilme tarihini güncellemek için `touch` komutunu kullanabilirsiniz.
* `mkdir` komutuyla bir dizin oluşturabilir ve boş bir dizini `rmdir` komutuyla silebilirsiniz.
* Dosya ve dizinleri kopyalamak, taşımak ve yeniden adlandırmak için `cp` ve `mv` komutlarını kullanabilirsiniz.
* Dosyalardaki okuma, yazma ve çalıştırma izinlerini değiştirmek için `chmod` komutunu kullanabilirsiniz.
