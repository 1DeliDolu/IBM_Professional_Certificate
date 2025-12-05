# ℹ️ Bilgilendirici Komutlar

## 🎯 Video Amaçları ve Genel Bakış

Bilgilendirici Komutlara Hoş Geldiniz.

Bu videoyu izledikten sonra şunları yapabileceksiniz:

* Kullanıcı ve işletim sistemi bilgilerini bulmak
* Sistem disk kullanımını görüntülemek
* Çalışan süreçleri ve kaynak kullanımlarını izlemek
* Metinleri, değişkenleri ve tarihleri yazdırmak
* Komutlar için kılavuz sayfalarını (manual) görüntülemek

Terminalinizde bilgilendirici komutları kullanarak sisteminiz hakkında kullanıcı bilgilerini görüntüleyebilirsiniz.

Kullanıcı bilgisi komutları, geçerli kullanıcının kimliğini doğrulamanız gerektiğinde veya belirli bir komutu ya da süreci hangi kullanıcı hesabının çalıştırdığını belirlemeniz gerektiğinde faydalıdır.

Örneğin, `whoami` komutu geçerli kullanıcının kullanıcı adını görüntüler.

---

## 👤 Kullanıcı Bilgisi Komutları: `whoami` ve `id`

`whoami` komutu hiçbir argüman almaz ve hiçbir seçeneği yoktur.

Burada, “John Doe” kullanıcısı olarak oturum açmış birisi için kullanım örneğini görüyorsunuz.

Benzer şekilde, `id` komutu, Linux sisteminde her kullanıcıya veya gruba atanan bir numara olan kullanıcı veya grup kimliğini (ID) döndürür.

Bu örnekte, `id` komutunu `-u` seçeneğiyle kullanmak, kullanıcının sayısal kimliğini döndürür.

Sayısal kullanıcı kimliğine karşılık gelen ismi görmek isterseniz, `-n` seçeneğini ekleyebilirsiniz.

Örnek komutlar:

```bash
whoami
id -u
id -u -n
```

---

## 🖥️ İşletim Sistemi Bilgisi: `uname`

`uname` komutu, *“Unix name”* ifadesinin kısaltmasıdır ve çekirdek adı ve sürüm numarası gibi işletim sistemi bilgilerini döndürür.

Bu komut, üzerinde çalıştığınız sistemin türünü belirlemek veya sistemle ilgili sorunları teşhis etmek için kullanılabilir.

`uname` komutunu yazmak, bu örnekte Darwin olan işletim sisteminin adını döndürür.

`-s` ve `-r` seçeneklerini eklemek, hem işletim sistemi adını hem de sürümünü döndürür.

Ayrıca, `-v` seçeneğini kullanarak daha ayrıntılı sürüm bilgilerini görüntüleyebilirsiniz.

Örnek komutlar:

```bash
uname
uname -s -r
uname -v
```

---

## 💽 Disk Kullanımı: `df` ve Disk Bağlama (Mount)

`df` (disk free) komutunu sisteminizin disk kullanımını görüntülemek için kullanabilirsiniz.

Bu komut, disk kullanımını izlemeniz veya belirli bir dosya sistemi üzerinde kullanılabilir alanı kontrol etmeniz gerektiği durumlarda faydalıdır.

Örneğin:

```bash
df -h ~
```

`df -h ~` komutunu girmek, tilda (`~`) simgesiyle temsil edilen ev dizininize özgü aşağıdaki tabloyu görüntüler.

Bu tabloda, ev dizininize bağlanmış tüm diskleri görebilirsiniz.

Linux’ta bir diski bir dizine *“mount”* edebilirsiniz; bu, o diskin dosya sisteminin bu dizin üzerinden erişilebilir hale gelmesi anlamına gelir.

Tablo ayrıca her disk üzerinde kullanılan depolama yüzdesini de gösterir.

`-h` seçeneği, çıktıdaki disk alanını bayt yerine gigabayt ve terabayt gibi birimlerle ifade ederek çıktıyı *insan tarafından okunabilir* hale getirir.

Tüm dosya sistemlerindeki disk kullanımını görüntülemek için bir dizin belirtmeden yalnızca şu komutu yazabilirsiniz:

```bash
df -h
```

Çıktı, her dosya sistemi için boyutu, kullanılan kapasiteyi ve kullanılabilir alanı içerir.

---

## 🧠 Süreç İzleme: `ps` ve `top`

Sisteminizde şu anda çalışan süreçleri görmek için `ps` ( *process status* ) komutunu kullanabilirsiniz.

Bu komut, süreçleri izlemeniz veya yönetmeniz gerektiğinde yardımcı olur.

```bash
ps -e
```

`ps` komutunu `-e` seçeneğiyle kullanmak, hangi kullanıcı tarafından başlatılmış olursa olsun sistemde çalışan tüm süreçleri listeler.

`ps` komutu, her çalışan sürecin adı, süreç kimliği (PID) ve sürecin kaç dakika ve saniyedir çalıştığı gibi bilgileri görüntüler.

`top` ( *table of processes* ) komutu, bir görev yöneticisi gibi davranır ve çalışan süreçleri ile bu süreçlerin kaynak kullanımını gösteren bir tablo görüntüler.

Bu komut, sistem performansını izlemeniz veya çok fazla kaynak kullanan süreçleri belirlemeniz gerektiğinde kullanışlıdır.

Örneğin:

```bash
top -n 3
```

Burada, `-n` seçeneği ve `3` sayısı ile `top` komutunu kullanarak en çok CPU kullanan ilk üç görevi görüntüleme örneğini görüyoruz: Chrome, `top` ve Spotify.

Varsayılan olarak görevler CPU kullanımına göre sıralanır.

Bu video için gösterilen çıktı, `top` komutunun basitleştirilmiş bir sürümüdür; ancak `top`, bellek kullanımı ve çalıştırılabilir dosyanın konumu gibi başka birçok ayrıntı da sağlar.

---

## 🗣️ Metin ve Değişken Yazdırma: `echo` ve `PATH`

Basit görünmesine rağmen, Linux’taki `echo` komutu terminalde veya bir kabuk (shell) betiğinde metin ya da değişkenleri görüntülemek için güçlü bir araçtır.

Yalnızca:

```bash
echo
```

komutunu girmek, terminale “hiçbir şey yazdırma” talimatı vermeye benzer ve komut yalnızca bir satır sonu (newline) döndürür.

Tek bir kelimeyi, örneğin “hello” kelimesini ekrana bastırmak isterseniz:

```bash
echo hello
```

komutunu yazabilir ve terminal bu kelimeyi döndürür.

Teknik olarak, `echo` komutunun beklendiği gibi çalışması için arada boşluklar olan bir dizeyi tırnak içine almanız gerekmez, ancak tırnak kullanmak en iyi uygulama (best practice) olarak kabul edilir.

```bash
echo "Learning Linux is fun!"
```

Tırnak içine alınmış bir dize ile `echo` kullanmak, tırnak içindeki içeriği döndürür: `"Learning Linux is fun!"`.

Ek olarak, sistemimizin `PATH` değişkeni gibi bir değişkenin değerini, dolar işaretinden sonra değişken adını yazarak görüntüleyebilirsiniz:

```bash
echo "$PATH"
```

Bu, sorun giderme veya betik yazma sırasında faydalı olabilir.

Burada, sisteminizin `PATH` değişkeninin her bir yolunu, iki nokta (`:`) karakteri ile ayrılmış şekilde görebilirsiniz.

---

## 📅 Tarih ve Saat Bilgisi: `date` ve Biçimlendirme

Bir diğer faydalı komut ise geçerli sistem tarihini ve saatini görüntüleyen `date` komutudur.

```bash
date
```

`date` komutunu girmek, varsayılan tarih biçimini döndürür: haftanın günü, gün, ay, yıl, saat ve saat dilimi.

Ayrıca, bu örnekte olduğu gibi, yazdırmak için tarihin belirli kısımlarını da çıkarabilirsiniz.

Çıktıyı biçimlendirmek için, tırnak içine alınmış, başında `+` işareti bulunan bir metin ve kontrol karakterleri birleşimi kullanırsınız.

Biçim denetimleri `%` sembolü ile gösterilir.

Bu durumda `%j` ve `%Y` kontrol karakterleri, sırasıyla yılın sayısal gününü ve yılın kendisini çıktı olarak verir.

Bu komut, yılın 97. günü için `"97"`, ardından `"day of"` kelimelerini ve `"2023"` yılını yazdırır.

`%Y` ifadesinin 2023 yılı ile değiştirildiğine dikkat edin.

Son olarak, biçim denetimlerini metinle birleştirerek benzersiz dizgiler yazdırmanın nasıl mümkün olduğunu göstermek için başka bir örnek daha verilir.

`%A`, `%j` ve `%Y` gibi kontrol karakterlerini metinle bir araya getirerek haftanın günü, yılın kaçıncı günü ve yılı söyleyen bir satır yazdırabilirsiniz.

---

## 📖 Komut Kılavuzları: `man`

Bu video sadece bu komutların temel özelliklerini kapsamıştır.

Bir komutu nasıl kullanacağınız hakkında daha fazla bilgi edinmek isterseniz `man` ( *manual* ) komutunu kullanabilirsiniz.

Tüm varsayılan Linux komutlarının, `man` kullanılarak görüntülenebilen bir kılavuz sayfası vardır.

Örneğin:

```bash
man id
```

komutunu girmek, `id` komutunun kılavuz sayfasını görüntüler.

Kılavuz, “kullanıcı kimliğini döndür” gibi komutun ne yaptığına dair temel bir özet sağlar.

Ayrıca `id` komutu için `-a` gibi seçenekler de listelenir.

Köşeli parantezler, bir kullanıcı adı belirtmenize olanak tanıyan `user` gibi isteğe bağlı parametreleri gösterir.

`man` komutu, komutun daha ayrıntılı bir açıklamasını da sağlar ve bu açıklama komutu daha ayrıntılı olarak açıklar.

`man` komutunun kendi `man` sayfası bile vardır — bu sayfayı, `manual` komutu ve kullanım alanları hakkında daha fazla bilgi edinmek için kullanabilirsiniz.

---

## 📌 Video Özeti

Bu videoda şunları öğrendiniz:

* `whoami` ve `id` komutlarıyla kullanıcı bilgilerini alma
* `uname` komutunu kullanarak işletim sistemi bilgilerini edinme
* `df` komutuyla sistem disk kullanımını kontrol etme
* `ps` ve `top` komutlarıyla süreçleri ve kaynak kullanımını izleme
* `echo` komutuyla bir metin veya değişken değerini yazdırma
* `date` komutuyla tarih hakkındaki bilgileri yazdırma ve belirli kısımlarını çıkartma
* `man` komutunu kullanarak herhangi bir komutun kılavuz sayfasını okuma

---

## 🔁 Zaman Damgalı Transkript ve Tekrar Eden Kısım

Bilgilendirici Komutlara Hoş Geldiniz.

Bu videoyu izledikten sonra şunları yapabileceksiniz: Kullanıcı ve işletim sistemi bilgilerini bulmak. Sistem disk kullanımını görüntülemek. Çalışan süreçleri ve bunların kaynak kullanımını izlemek. Metinleri, değişkenleri ve tarihleri yazdırmak. Komutlar için kılavuz sayfalarını görüntülemek.

Terminalinizde bilgilendirici komutları kullanarak sisteminiz hakkında kullanıcı bilgilerini görüntüleyebilirsiniz.

Kullanıcı bilgisi komutları, geçerli kullanıcının kimliğini doğrulamanız gerektiğinde veya belirli bir komutu ya da süreci hangi kullanıcı hesabının çalıştırdığını belirlemeniz gerektiğinde faydalıdır.

Örneğin, `whoami` komutu geçerli kullanıcının kullanıcı adını görüntüler.

*Videoyu ::51 zamanından başlatarak oynatın ve transkripti 0:51'den itibaren takip edin.*

`whoami` komutu hiçbir argüman almaz ve hiçbir seçeneği yoktur.

Burada, “John Doe” kullanıcısı olarak oturum açmış birisi için kullanım örneğini görüyorsunuz.

Benzer şekilde, `id` komutu, Linux sisteminde her kullanıcıya veya gruba atanan bir numara olan kullanıcı veya grup kimliğini döndürür.

Bu örnekte, `id` komutunu `-u` seçeneğiyle kullanmak, kullanıcının sayısal kimliğini döndürür.

Sayısal kullanıcı kimliğine karşılık gelen ismi görmek isterseniz, `-n` seçeneğini ekleyebilirsiniz.

`uname` komutu, *“Unix name”* ifadesinin kısaltmasıdır ve çekirdek adı ve sürüm numarası gibi işletim sistemi bilgilerini döndürür.

Bu komut, üzerinde çalıştığınız sistemin türünü belirlemek veya sistemle ilgili sorunları teşhis etmek için kullanılabilir.

*Videoyu 1:40 zamanından başlatarak oynatın ve transkripti 1:40'tan itibaren takip edin.*

`uname` komutunu girmek, bu örnekte Darwin olan işletim sisteminin adını döndürür.

`-s` ve `-r` seçeneklerini eklemek, hem işletim sistemi adını hem de sürümünü döndürür.

Ayrıca, `-v` seçeneğini kullanarak daha ayrıntılı sürüm bilgilerini görüntüleyebilirsiniz.

Sisteminizin disk kullanımını görüntülemek için `df` ( *disk free* ) komutunu kullanabilirsiniz.

Bu komut, disk kullanımını izlemeniz veya belirli bir dosya sistemi üzerindeki kullanılabilir alanı kontrol etmeniz gerektiğinde faydalıdır.

Örneğin, `df -h ~` komutunu girmek, tilda (`~`) simgesiyle temsil edilen ev dizininize özgü aşağıdaki tabloyu görüntüler.

Bu tabloda, ev dizininize bağlanmış tüm diskleri görebilirsiniz.

*Videoyu 2:29 zamanından başlatarak oynatın ve transkripti 2:29'dan itibaren takip edin.*

Linux’ta bir diski bir dizine *“mount”* edebilirsiniz; bu, o diskin dosya sisteminin bu dizin üzerinden erişilebilir hale gelmesi anlamına gelir.

Tablo ayrıca her disk üzerinde kullanılan depolama yüzdesini de gösterir.

`-h` seçeneği, çıktıdaki disk alanını bayt yerine gigabayt ve terabayt gibi birimlerle ifade ederek çıktıyı insan tarafından okunabilir hale getirir.

Tüm dosya sistemlerindeki disk kullanımını görüntülemek için, bir dizin belirtmeden yalnızca `df -h` komutunu yazabilirsiniz.

Çıktı, her dosya sistemi için boyutu, kullanılan kapasiteyi ve kullanılabilir alanı içerir.

Sisteminizde şu anda çalışan süreçleri görmek için `ps` ( *process status* ) komutunu kullanabilirsiniz.

Bu komut, süreçleri izlemeniz veya yönetmeniz gerektiğinde yardımcı olur.

*Videoyu 3:19 zamanından başlatarak oynatın ve transkripti 3:19'dan itibaren takip edin.*

`ps` komutunu `-e` seçeneğiyle kullanmak, hangi kullanıcı tarafından başlatılmış olursa olsun sistemde çalışan tüm süreçleri listeler.

`ps` komutu, her çalışan sürecin adı, süreç kimliği ve sürecin kaç dakika ve saniyedir çalıştığı gibi bilgileri görüntüler.

`top` ( *table of processes* ) komutu, bir görev yöneticisi gibi davranır ve çalışan süreçleri ile bu süreçlerin kaynak kullanımını gösteren bir tablo görüntüler.

Bu komut, sistem performansını izlemeniz veya çok fazla kaynak kullanan süreçleri belirlemeniz gerektiğinde kullanışlıdır.

Burada, `-n` seçeneği ve `3` sayısı ile `top` komutunu kullanarak en çok CPU kullanan ilk üç görevi görüntüleme örneğini görüyoruz: Chrome, `top` ve Spotify.

Varsayılan olarak görevler CPU kullanımına göre sıralanır.

Bu video için gösterilen çıktı, `top` komutunun basitleştirilmiş bir sürümüdür; ancak `top`, bellek kullanımı ve çalıştırılabilir dosyanın konumu gibi başka birçok ayrıntı da sağlar.

*Videoyu 4:20 zamanından başlatarak oynatın ve transkripti 4:20'den itibaren takip edin.*

Basit olmasına rağmen, Linux’taki `echo` komutu terminalde veya bir kabuk betiğinde metin ya da değişkenleri görüntülemek için güçlü bir araçtır.

Yalnızca `echo` komutunu girmek, terminale “hiçbir şey yazdırma” talimatı vermeye benzer ve komut bir satır sonu döndürür.

“hello” gibi tek bir kelimeyi ekrana bastırmak isterseniz, `echo hello` komutunu yazabilir ve terminal bu kelimeyi döndürür.

Teknik olarak, `echo` komutunun beklendiği gibi çalışması için arada boşluklar olan bir dizeyi tırnak içine almanız gerekmez, ancak tırnak kullanmak en iyi uygulama olarak kabul edilir.

Tırnak içine alınmış bir dize ile `echo` kullanmak, `"Learning Linux is fun!"` içeriğini döndürür.

Ek olarak, sistemimizin `PATH` değişkeni gibi bir değişkenin değerini, dolar işaretinden sonra değişken adını yazarak görüntüleyebilirsiniz.

Bu, sorun giderme veya betik yazma sırasında faydalı olabilir.

*Videoyu 5:14 zamanından başlatarak oynatın ve transkripti 5:14'ten itibaren takip edin.*

Burada, sisteminizin `PATH` değişkeninin her bir yolunu, iki nokta (`:`) karakteri ile ayrılmış şekilde görebilirsiniz.

Bir diğer faydalı komut ise geçerli sistem tarihini ve saatini görüntüleyen `date` komutudur.

`date` komutunu girmek, varsayılan tarih biçimini döndürür: haftanın günü, gün, ay, yıl, saat ve saat dilimi.

Ayrıca, bu örnekte olduğu gibi, yazdırmak için tarihin belirli kısımlarını da çıkarabilirsiniz.

Çıktıyı biçimlendirmek için, tırnak içine alınmış, başında `+` işareti bulunan bir metin ve kontrol karakterleri birleşimi kullanırsınız.

Biçim denetimleri `%` sembolü ile gösterilir.

Bu durumda `%j` ve `%Y` kontrol karakterleri, sırasıyla yılın sayısal gününü ve yılın kendisini çıktı olarak verir.

*Videoyu 5:58 zamanından başlatarak oynatın ve transkripti 5:58'den itibaren takip edin.*

Bu komut, yılın 97. günü için `"97"`, ardından `"day of"` kelimelerini ve `"2023"` yılını yazdırır.

`%Y` ifadesinin 2023 yılı ile değiştirildiğine dikkat edin.

Son olarak, biçim denetimlerini metinle birleştirerek benzersiz dizgiler yazdırmanın nasıl mümkün olduğunu göstermek için başka bir örnek daha verilir.

`%A`, `%j` ve `%Y` gibi kontrol karakterlerini metinle bir araya getirerek haftanın günü, yılın kaçıncı günü ve yılı söyleyen bir satır yazdırabilirsiniz.

Bu video sadece bu komutların temel özelliklerini kapsamıştır.

Bir komutu nasıl kullanacağınız hakkında daha fazla bilgi edinmek isterseniz `man` ( *manual* ) komutunu kullanabilirsiniz.

Tüm varsayılan Linux komutlarının, `man` kullanılarak görüntülenebilen bir kılavuz sayfası vardır.

*Videoyu 6:47 zamanından başlatarak oynatın ve transkripti 6:47'den itibaren takip edin.*

Örneğin, `man id` komutunu girmek, `id` komutunun kılavuz sayfasını görüntüler.

Kılavuz, “kullanıcı kimliğini döndür” gibi komutun ne yaptığına dair temel bir özet sağlar.

Ayrıca `id` komutu için `-a` gibi seçenekler de listelenir.

Köşeli parantezler, bir kullanıcı adı belirtmenize olanak tanıyan `user` gibi isteğe bağlı parametreleri gösterir.

`man` komutu, komutun daha ayrıntılı bir açıklamasını da sağlar ve bu açıklama komutu daha ayrıntılı olarak açıklar.

`man` komutunun kendi `man` sayfası bile vardır — bu sayfayı, `manual` komutu ve kullanım alanları hakkında daha fazla bilgi edinmek için kullanabilirsiniz.

Bu videoda şunları öğrendiniz: `whoami` ve `id` komutlarıyla kullanıcı bilgilerini almak, `uname` komutunu kullanarak işletim sistemi bilgilerini edinmek, `df` komutuyla sistem disk kullanımını kontrol etmek, `ps` ve `top` komutlarıyla süreçleri ve kaynak kullanımını izlemek, `echo` komutuyla bir metin veya değişken değerini yazdırmak, `date` komutuyla tarih hakkındaki bilgileri yazdırmak ve belirli kısımlarını çıkartmak ve `man` komutunu kullanarak herhangi bir komutun kılavuz sayfasını okumak.

Bilgilendirici Komutlara Hoş Geldiniz.

Bu videoyu izledikten sonra şunları yapabileceksiniz: Kullanıcı ve işletim sistemi bilgilerini bulmak. Sistem disk kullanımını görüntülemek. Çalışan süreçleri ve bunların kaynak kullanımını izlemek. Metinleri, değişkenleri ve tarihleri yazdırmak. Komutlar için kılavuz sayfalarını görüntülemek.

Terminalinizde bilgilendirici komutları kullanarak sisteminiz hakkında kullanıcı bilgilerini görüntüleyebilirsiniz.

Kullanıcı bilgisi komutları, geçerli kullanıcının kimliğini doğrulamanız gerektiğinde veya belirli bir komutu ya da süreci hangi kullanıcı hesabının çalıştırdığını belirlemeniz gerektiğinde faydalıdır.

Örneğin, `whoami` komutu geçerli kullanıcının kullanıcı adını görüntüler.

*Videoyu ::51 zamanından başlatarak oynatın ve transkripti 0:51'den itibaren takip edin.*

`whoami` komutu hiçbir argüman almaz ve hiçbir seçeneği yoktur.

Burada, şu şekilde oturum açmış birisi için bir kullanım örneği görüyorsunuz:
