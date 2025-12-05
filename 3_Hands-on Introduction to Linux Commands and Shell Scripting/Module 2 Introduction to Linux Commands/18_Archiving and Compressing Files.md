# 📦 Dosyaları Arşivleme ve Sıkıştırma

## 🎯 Öğrenme Hedefleri

Bu laboratuvarı tamamladıktan sonra şunları yapabileceksiniz:

* Dosya ve klasör kümeleri için arşivler oluşturmak
* Dosyaları sıkıştırmak ve sıkıştırmalarını açmak
* Mevcut bir arşivden dosya ve klasör çıkarmak

---

## 💻 Skills Network Cloud IDE Hakkında

**Skills Network Cloud IDE** (Theia ve Docker tabanlı), kurs ve proje ile ilgili uygulamalı laboratuvarlar için bir ortam sağlar.

 **Theia** , masaüstünde veya bulutta çalıştırılabilen, açık kaynaklı bir  **IDE** ’dir ( *Integrated Development Environment – Tümleşik Geliştirme Ortamı* ).

Bu laboratuvarı tamamlamak için, Theia tabanlı  **Cloud IDE** ’yi kullanacaksınız.

---

## ⚠️ Bu Laboratuvar Ortamı Hakkında Önemli Uyarı

Bu laboratuvar ortamındaki oturumların **kalıcı olmadığını** lütfen unutmayın.

Bu nedenle, her bağlandığınızda sizin için **yeni bir ortam** oluşturulur ve önceki oturumda kaydetmiş olabileceğiniz veri veya dosyalarınızın tümü kaybolur.

Verilerinizi kaybetmemek için, bu laboratuvarları **tek bir oturumda** tamamlamayı planlayın.

---

## 🧪 Alıştırma 1 – Dosya ve klasör arşivleme ve sıkıştırma

### 1.1. Dosya arşivleri oluşturma ve yönetme

`tar`

`tar` komutu, birden fazla dosya ve dizini tek bir arşiv dosyası içinde paketlemenizi sağlar.

Aşağıdaki komut, tüm `/bin` dizininin bir arşivini oluşturur ve bu arşivi `bin.tar` adlı tek bir dosyaya yazar.

Kullanılan seçenekler şöyledir:

| Seçenek | Açıklama                                |
| -------- | ----------------------------------------- |
| `-c`   | Yeni arşiv dosyası oluştur             |
| `-v`   | İşlenen dosyaları ayrıntılı listele |
| `-f`   | Arşiv dosyası adı                      |

`1`

```bash
tar -cvf bin.tar /bin
```


Arşivdeki dosyaların listesini görmek için `-t` seçeneğini kullanın:

```bash
tar -tvf bin.tar
```


Arşivin içini açmak veya dosyaları arşivden çıkarmak için `-x` seçeneğini kullanın:

```bash
tar -xvf bin.tar
```


`bin` klasörünün çıkarıldığını doğrulamak için `ls` komutunu kullanın:

```bash
ls -l
```


---

### 1.2. Arşiv dosyalarını paketleme ve sıkıştırma

`zip`

`zip` komutu, dosyaları sıkıştırmanızı sağlar.

Aşağıdaki komut, `/etc` dizinindeki `.conf` uzantısına sahip tüm dosyalardan oluşan ve `config.zip` adını taşıyan bir zip dosyası oluşturur:

```bash
zip config.zip /etc/*.conf
```


`-r` seçeneği, tüm bir dizini zip’lemek için kullanılabilir.

`-y` bayrağı ise sembolik bağlantıların özyinelemeli olarak takip edilmesini önler:

Aşağıdaki komut, `/bin` dizininin bir arşivini oluşturur:

```bash
zip -ry bin.zip /bin
```


---

### 1.3. ZIP arşivindeki sıkıştırılmış dosyaları çıkarma, listeleme veya test etme

`unzip`

`unzip` komutu, dosyaları çıkarmanızı sağlar.

`config.zip` arşivindeki dosyaları listelemek için aşağıdakini girin:

```bash
unzip -l config.zip
```


Aşağıdaki komut, `bin.zip` arşivindeki tüm dosyaları çıkarır:

```bash
unzip -o bin.zip
```


Komutu birden fazla kez çalıştırmanız durumunda üzerine yazmayı zorlamak için `-o` seçeneğini ekledik.

Dizininizde `bin` adlı bir klasör oluşturulduğunu görmelisiniz.

---

## 🧾 Özet

Bu laboratuvarda şunları öğrendiniz:

* `tar`, birden fazla dosya ve dizini tek bir arşiv dosyası içinde paketlemenizi sağlar
* `zip`, dosyaları sıkıştırmanızı sağlar
* `unzip`, dosyaları çıkarmanızı sağlar
