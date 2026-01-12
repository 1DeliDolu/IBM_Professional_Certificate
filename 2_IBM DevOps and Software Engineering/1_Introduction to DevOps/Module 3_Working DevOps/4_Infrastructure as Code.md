## 🧱 Infrastructure as Code

Bu videoyu izledikten sonra *infrastructure as code* kavramını tanımlayabilecek,  *ephemeral infrastructure* ’ı açıklayabilecek ve konteynerler aracılığıyla *immutable delivery* yaklaşımını tanımlayabileceksiniz.

 *Infrastructure as code* , altyapının metinsel bir formatta tanımlanması uygulamasıdır. Burada dokümantasyondan bahsetmiyorum. Burada, çalıştırılabilir olan, yani kod olarak da bilinen bir metinsel formattan bahsediyorum. Altyapınızı, bir araca verip çalıştırabileceğiniz metinsel bir açıklama kullanarak yapılandırabilmek istersiniz.

Bunu mümkün kılan araçlara *configuration management systems* denir. Bunlar, altyapınızı kod olarak tanımlamanıza, ardından bu altyapıyı oluşturmanıza ve o durumda tutmanıza olanak sağlayan Ansible, Puppet, Chef gibi araçlardır.

---

## ⚙️ Manuel Değişikliklerden Kaçınma

Sistem değişikliklerini yazılım yapılandırmalarında asla manuel olarak yapmak istemezsiniz. Bu tekrarlanabilir değildir ve son derece hataya açıktır. Sistemler, cihazlar, yazılımlar ve kullanıcılar gibi öğeleri nasıl kuracağınızı ve otomatik olarak nasıl yapılandıracağınızı tanımlayan şablonlar ve betikler kullanmak istersiniz.

Sonra bu metinsel kodu alıp sürüm kontrol sisteminizde saklayabilirsiniz; böylece tüm değişikliklerin geçmişi elinizde olur. Bu şekilde herkes hangi sürümün en güncel sürüm olduğunu ve altyapının nasıl görünmesi gerektiğini bilir.

Docker, Vagrant, Terraform ve hatta Kubernetes gibi teknolojiler de altyapınızı kod olarak tanımlamanıza olanak sağlar ve bu kod sürüm kontrolüne *check-in* edilmelidir. Bunun bu kadar önemli olmasının nedeni,  *server drift* ’in büyük bir hata kaynağı olmasıdır.

---

## 🧭 Server Drift ve Öngörülemez Hatalar

Zaman içinde sunucular çeşitli nedenlerle güncellenir ve her zaman aynı kişiler tarafından güncellenmez. Bu da onların orijinal yapılandırmalarından sapmasına neden olur. Bazen bu değişikliklerin birikimi, öngörülemez şekillerde hatalara yol açar.

Daha da kötüsü, aynı olması gereken sunucuların var olmasıdır; ama içlerinden biri bir yerdeki yanlış yapılandırma yüzünden sürekli hata verir.

---

## 🐄 “Servers are cattle, not pets”

“Servers are cattle, not pets” sözü, sunuculara nasıl davrandığınızı ifade eder. Diyelim ki bin baş sığırınız var. Her birine isim vermek için zaman harcamazsınız.

İçlerinden biri hastalandığında, acısına son verirsiniz ve onu bir başkasıyla değiştirirsiniz. Öte yandan evcil hayvanlar? Hastalandıklarında sevgiyle ilgilenilir ve sağlıklarına kavuşmaları için bakımları yapılır.

Mesaj şudur: Sunucuları sevgiyle el işçiligiyle üretmemeli veya çalışmadıklarında çok fazla zaman harcayıp debug etmemelisiniz. Onları, düzgün çalışan birebir aynı bir sunucuyla değiştirebilmelisiniz.

Bu da altyapınızı *ephemeral* ya da geçici ( *transient* ) bir şey olarak düşünmeniz gerektiği anlamına gelir. Yalnızca ihtiyaç duyduğunuz süre boyunca var olur ve kullanılmadığında kaldırırsınız.

---

## ⏳ Ephemeral Altyapı

Örneğin geçmişte test ortamlarını oluşturmak haftalar alırdı. Bu yüzden haftalarca inşa etmek gerektiğinden onları aylarca çalışır halde tutardınız.

Ama *infrastructure as code* olduğunda, yeni bir sunucu setini dağıtmak dakikalar alır. Bir test ortamını ayağa kaldırabilirsiniz, bir süre kullanırsınız ve sonra yok edersiniz.

Başka bir gün tekrar ihtiyacınız olursa, yenisini oluşturursunuz. Onu sonsuza kadar çalışır halde tutmazsınız. Sadece ihtiyaç duyduğunuzda ayağa kaldırır, artık ihtiyaç duymadığınızda kapatırsınız.

Bu geçicidir ( *transient* ).

---

## 🔁 Parallel Infrastructure ile Yayınlama

Bu aynı zamanda paralel altyapı üzerinden yayın yapmamızı sağlar. Örneğin, üretimde olan sunucunun aynısı gibi görünen bir sunucu inşa edebilirim. Uygulamanın yeni bir sürümünü dağıtabilirim veya doğru çalışıp çalışmadığını görmek için izleyebilirim.

Doğru davrandığı görülürse, üretimdeki olanı kapatırım ve yenisini üretim sunucusu yaparım. Paralel altyapı ile her şeyi sürekli çalışır durumda tutabilirim.  *Infrastructure as code* , her seferinde aynı altyapıyı oluşturabilmemi sağlar.

---

## 📦 Docker ile Immutable Delivery

*Ephemeral infrastructure* kullanılabilir ve sonra atılabilir; çünkü sunucular, talep üzerine otomasyonla, *infrastructure as code* teknikleri kullanılarak inşa edilir.

Docker gibi araçlar, *immutable delivery* oluşturmamıza yardımcı olur. Docker, işleri tutarlı bir şekilde ayağa kaldırmamıza ve indirmemize olanak sağlayan bir paketleme teknolojisidir; *container* adı verilen izole bir ortamda çalışır.

Docker, bir *Dockerfile* denilen koddan imajın nasıl inşa edileceğini belirtmenize izin vererek *infrastructure as code* yaklaşımını destekler. Bu Dockerfile’lar her seferinde aynı imajı aynı şekilde üretir.

Docker daha sonra, o imajdan her dağıtımda aynı şekilde bir konteyner oluşturur. Bu, üretimde çalışan konteynerin geliştiricinin dizüstü bilgisayarında da çalıştırılabileceği anlamına gelir.

Bu, nihai  *development-production parity* ’dir. Bunun nedeni, uygulamayı çalıştırmak için gereken tüm bağımlılıkların konteynerin içinde birlikte paketlenmesidir. Bu, olası varyansı veya yan etkileri sınırlar. Çalıştırmak için konteyner çalışma zamanı (Docker gibi) dışında başka hiçbir şeye ihtiyaç yoktur.

---

## 🔄 Rolling Update ve Anında Rollback

Docker gibi araçlar, anında geri alma ( *immediate roll-back* ) ile *rolling update* yapmanıza da olanak sağlar. Yani uygulamayı kurup çalışıp çalışmadığına bakıp sonra çalışmıyorsa kaldırmazsınız.

Bunun yerine yeni sürümle bir Docker konteyneri ayağa kaldırırsınız. Yanlış davranmaya başlarsa, durdurur, indirir ve zaten kendi konteynerine kurulmuş olan önceki sürümü tekrar ayağa kaldırırsınız. Bu kelimenin tam anlamıyla saniyeler sürer.

Yanlış davranmaya başlayan konteynerleri de aynı şekilde ele alırsınız. Konteyneri siler ve yerine bir tane daha oluşturursunuz.

Yeni konteyner, ilk gün ayağa kalktığındaki eski konteynerle tamamen aynı olacaktır. Eğer bir tür bozulma ( *corruption* ) olduysa, bu bozulma tamamen ortadan kalkacak; her şey tekrar orijinal haline dönecektir. Bu, çok farklı bir çalışma biçimidir.

---

## 🧬 Çalışan Konteynerleri Değiştirmemek

Çalışan konteynerlerde, çalışan bir sunucuda yaptığınız gibi değişiklik yapmazsınız. Unutmayın: “cattle, not pets.” Konteynerleri zafiyetler için yamalamaz ( *patch* ) veya onları herhangi bir şekilde değiştirmezsiniz.

Herhangi bir değişiklik yapmak için, konteynerin oluşturulduğu imaja bir değişiklik yaparsınız. Sonra eski konteynerin yerine geçmesi için yeni konteyneri yeniden dağıtırsınız.

Nedeni basittir: Eğer bir konteyneri yamalarsanız ve o ölürse, yerine yenisi ayağa kaldırılır; yeni konteynerde yamalar olmayacaktır. Bu yüzden imajı değiştirmeniz zorunludur.

Onlar konteynerleri oluşturmak için şablondur ve güncel tutulması gereken şeyler çalışan konteynerler değil, bu şablonlardır.

---

## ✅ Video Özeti

Bu videoda,  *infrastructure as code* ’un altyapıyı çalıştırılabilir metinsel bir formatta tanımladığını öğrendiniz.

*Ephemeral infrastructure* kullanılabilir ve sonra atılabilir. Sunucular, otomasyon yoluyla talep üzerine inşa edilir.

Çalışan bir konteyneri yamalamak yerine, *immutable delivery* konteyner imajında değişiklik yapmayı ve ardından yeni bir konteyneri yeniden dağıtmayı ifade eder.
