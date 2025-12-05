# 🆘 Linux Komutları için Yardım Alma

Komutları keşfetmek ve denemeler yapmak için zaman harcamanın çok büyük bir değeri vardır, ancak yalnızca deneyerek çözemeyeceğiniz pek çok şey vardır. Nelerin mevcut olduğunu, nelerin mümkün olduğunu görmeye ve yanıtları bulmak için nereye bakmanız gerektiğini öğrenmeye ihtiyacınız vardır.

İlerleme kaydetmenize yardımcı olacak bilgilere ulaşmak için bazı harika yöntemlere göz atalım.

Bu okumada, harici kaynaklara giden bağlantılar görebilirsiniz. Bunları, bağlantıya sağ tıklayıp **“Open in new tab”** seçeneğine basarak yeni bir sekmede açabilirsiniz.

---

## 📘 1. Yerleşik `man` komutunu kullanma

`man` komutu, *“manual”* (kılavuz) kelimesinin kısaltmasıdır ve Unix benzeri komutlar için komut satırından yardım almanın standart yolunu sağlar. 1971’den beri geliştirilmektedir.

Sisteminizde kılavuz (man) sayfası olan tüm komutların bir listesini almak için şunu yazabilirsiniz:

```bash
man -k .
```

Ortaya çıkan listede, her komutun ne yaptığına dair kısa bir açıklama bulunur.

Bir komutun `man` sayfasını görmek için şu komutu yazmanız yeterlidir:

```bash
man command_name
```

Tüm `man` sayfaları aşağıdaki bölümlere ayrılır:

* **NAME**

  Komutun veya özelliğin adı ve ne yaptığına dair kısa bir açıklama.
* **SYNOPSIS**

  Komutun sözdiziminin özeti; kullanılabilecek tüm seçenekleri ve argümanları içerir.
* **DESCRIPTION**

  Komutun işlevi ve davranışı da dahil olmak üzere daha ayrıntılı bir açıklama.
* **OPTIONS**

  Komutla birlikte kullanılabilecek mevcut tüm seçenekler ve argümanlar.
* **EXAMPLES**

  Komutun nasıl kullanılacağına dair bazı örnekler.
* **SEE ALSO**

  Faydalı olabilecek ilgili komutlar ve belgeler.

Ayrıca şu bölümleri de görebilirsiniz:  **EXIT STATUS** ,  **RETURN VALUE** ,  **ENVIRONMENT** ,  **BUGS** ,  **FILES** ,  **AUTHOR** ,  **REPORTING BUGS** , **HISTORY** ve  **COPYRIGHT** .

---

## 📄 2. `tldr` komutunu yükleme ve kullanma

`man` sayfalarına benzer şekilde, **TLDR Pages** ücretsiz ve açık kaynaklı, işbirliğine dayalı bir dokümantasyon çalışmasıdır. Amacı, oldukça uzun ve detaylı olma eğilimindeki geleneksel `man` sayfalarından daha erişilebilir dokümantasyon oluşturmaktır.

*TLDR Pages* – *“Too Long; Didn’t Read”* ifadesinin kısaltmasıdır ve kısaca `tldr` olarak da bilinir – çeşitli komutların yaygın kullanım senaryoları için örnekler sunar. TLDR sayfalarının formatı, bir **cheatsheet** (kopya kâğıdı) formatına benzer.

Terminalinizden TLDR Pages’e erişmek için bir komut satırı aracı yükleyebilirsiniz. Bunu şu komutla kurabilirsiniz:

```bash
npm install -g tldr
```

Aracı yükledikten sonra, bir komutun TLDR sayfasına kolayca erişmek için `tldr` komutunu kullanabilirsiniz:

```bash
tldr command_name
```

Araç, komutun kısa ve anlaşılması kolay bir özetini ve nasıl kullanılacağına dair bazı örnekleri görüntüler.

---

## 🌐 3. Stack Overflow’da arama yapma

 **Stack Overflow** , programcılar, geliştiriciler ve sistem yöneticileri için popüler, topluluk odaklı bir soru–cevap platformudur. Linux dahil olmak üzere, çeşitli programlama dilleri, araçlar ve işletim sistemleriyle ilgili çok geniş bir soru ve cevap arşivine sahiptir.

Komutlar hakkında bilgi aramak için Stack Overflow ana sayfasındaki arama çubuğunu kullanabilir; aradığınız komutun adını, birlikte kullanmak istediğiniz belirli anahtar sözcükler veya parametrelerle birlikte yazabilirsiniz.

Ayrıca, aramanızı “linux” veya “command-line” gibi ilgili etiketleri ekleyerek de daraltabilirsiniz.

Arama sorgunuzu girdikten sonra, Stack Overflow sorgunuzla eşleşen ilgili soru ve cevapların bir listesini görüntüler. Bu sonuçlar arasında gezinebilir, ihtiyacınız olan bilgiyi bulabilir ve kendi sorunuza yanıt bulamazsanız yeni bir soru da gönderebilirsiniz.

Komutlarla ilgili bilgi ararken, verilen cevapların tarihine dikkat etmek önemlidir; böylece bilginin hâlâ güncel ve geçerli olduğundan emin olabilirsiniz. Ayrıca, komutla ilgili bağlamı ve olası sorunları ya da kısıtlamaları daha iyi anlamak için yorumları ve tartışma başlıklarını da okumalısınız.

Linux etiketli en yeni Stack Overflow soruları:

[https://stackoverflow.com/questions/tagged/linux](https://stackoverflow.com/questions/tagged/linux)

---

## 🌍 4. Stack Exchange’de arama yapma

 **Stack Exchange** , Stack Overflow’a benzer bir soru–cevap toplulukları ağıdır; ancak yalnızca programlama yerine çok daha geniş bir konu yelpazesini kapsar. Linux ve açık kaynak yazılımla ilgili konularda uzmanlaşmış birkaç Stack Exchange topluluğu vardır; örneğin  **Unix & Linux** , **Ask Ubuntu** ve  **Server Fault** .

Stack Exchange’de bilgi aramak için ilgili topluluğu ziyaret edin. Stack Overflow’da olduğu gibi, arama çubuğuna aradığınız komutun adını, anahtar sözcükleri veya parametreleri yazabilirsiniz.

Unix ve Linux topluluğu:

[https://unix.stackexchange.com/](https://unix.stackexchange.com/)

---

## 🔍 5. Google’da arama yapma

Google, neredeyse her sorunun cevabını bulmanıza yardımcı olabilecek güçlü bir araçtır. Doğru sorguları nasıl yazacağınızı ve sonuçlarınızı nasıl filtreleyeceğinizi öğrenin; örneğin aramanıza “Wikipedia”, “Stack Overflow” veya “Linux” ekleyebilirsiniz.

Ancak, bunu **kendi sorumluluğunuzda** kullanın. Web’de bulduğunuz hiçbir şeye körü körüne güvenmeyin – ortada çok fazla “gürültü” (yanıltıcı veya alakasız bilgi) vardır!

---

## 📝 6. Bu kurstaki kopya kâğıtlarını (cheat sheet) kullanma

Bu kurs boyunca, öğrendiğiniz bilgileri kolay başvuru rehberleri hâline getiren “cheat sheet”lerle karşılaşacaksınız. Bunlar, öğrendiğiniz materyali gözden geçirmek için harikadır ve ayrıca notla değerlendirilen ödevlerinizde de size yardımcı olabilirler.

---

## 📚 7. Wikipedia’nın Unix komutları listesine başvurma

Son olarak, Wikipedia; Unix işletim sistemlerinde bulunabilen komutların, kısa açıklamalarıyla birlikte bir listesini tutar. Bir Unix komutuna hızlıca göz atmak için bu sayfayı kontrol edebilirsiniz:

[https://en.wikipedia.org/wiki/List_of_Unix_commands](https://en.wikipedia.org/wiki/List_of_Unix_commands)

---

## ✅ Özet

Bu okuma, Linux komutları hakkında daha fazla bilgi bulmanın yollarına genel bir bakış sağlamıştır.

Bu derste ve sonrasında komutları kullanmaya devam ettikçe, muhtemelen aynı komut kalıplarını tekrar tekrar kullandığınızı fark edeceksiniz. Her komutu kullandığınızda, kendinizi onunla biraz daha rahat ve ona daha aşina hissedeceksiniz.

Parmaklarınız, komutları kullanma konusunda kas hafızası geliştirecek ve sonunda komut kullanmak sizin için tamamen doğal bir hâle gelecektir!
