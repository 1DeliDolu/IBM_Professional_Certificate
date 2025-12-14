
# 🧪 Test Odaklı Geliştirme

Bu videoyu izledikten sonra; test odaklı geliştirmeyi (TDD) tanımlayabilecek, TDD’nin nasıl daha yüksek kaliteli kod ürettiğini açıklayabilecek, **Kırmızı, Yeşil, Refactor** iş akışını anlatabilecek ve TDD’nin DevOps için önemini açıklayabileceksiniz.

Bu, en sevdiğim alıntılardan biri: “Eğer inşa etmeye değer bir şeyse, test etmeye de değerdir. Test etmeye değmezse, neden üzerinde çalışarak zamanını boşa harcıyorsun?”

Test senaryoları yazmak, kodunuzun amaçlandığı şekilde çalıştığını kanıtlamak için kritik öneme sahiptir.

---

## 🧠 Test Odaklı Geliştirme Nedir?

Test Odaklı Geliştirme (TDD), test senaryonuzun kodunuzun tasarımını ve geliştirilmesini yönlendirmesi anlamına gelir. Önce kod yazıp sonra test etmezsiniz.

Önce test senaryolarını yazarsınız. Sahip olmayı dilediğiniz kod için testleri yazarsınız, sonra onları geçirecek kodu yazarsınız. Bu kulağa ters gelebilir.

“Peki, daha yazmadığım kod için nasıl test senaryosu yazabilirim?” “Nasıl yazmadığım kod için bir tasarım yazabiliyorsun?” Tasarımda kodun nasıl davranması gerektiğini tarif edersiniz ve sonra o şekilde davranan kodu yazarsınız. TDD bundan farklı değildir.

Test senaryosu, kodun sahip olmasını istediğiniz davranışı tarif eder. Bu, sizi kodun amacına odaklı tutar; yani ne yapması gerekiyor. Herhangi bir kod yazmaya başlamadan önce bunu kesinlikle belirtebilmelisiniz. Aksi halde, ne yazmanız gerektiğini nasıl bileceksiniz?

Bu aynı zamanda sizi, kodunuzu çağıracak istemcilere odaklı tutan şeydir. Epey backend geliştirme yapıyorum. Başkalarının kullanacağı servisler oluşturmayı seviyorum.

---

## 🧩 Çağıranın Perspektifi ve API Tasarımı

Bir gün, harika bir Uygulama Programlama Arayüzü (API) olan muhteşem bir servis oluşturduğumdan emindim. Kodun derinliklerindeydim ve bazı bilgilere ihtiyacım oldu, bu yüzden onu API’ye bir parametre olarak ekledim. Sonra başka bir şeye ihtiyacım oldu ve onu da API’ye başka bir parametre olarak ekledim. En sonunda daha fazla şeye ihtiyacım oldu, onları da parametre olarak ekledim.

Şimdi kodum için bazı test senaryoları yazma zamanı. O sırada TDD’yi takip etmiyordum. Test senaryolarını yazmaya başladığımda, bir anda parametrelerimin gerektirdiği bilgilerin yarısına sahip olmadığımı fark ettim.

Benim güzel API’m berbattı! Nasıl bu kadar kötü olabilirdi? Nerede yanlış yapmıştım? Kodumu çağıranı hesaba katmamıştım çünkü TDD’yi takip etmiyordum.

TDD size çağıranın perspektifini verir. Kodu daha yazmadan önce onu nasıl çağırmak isteyeceğinizi keşfetmenizi sağlar. Şunu düşünmenizi sağlar: “Bir çağıran olarak ne biliyorum, neyi içeri verebilirim ve bir cevap alabilirim?”

Bu perspektife sahip olmak iyi kod yazmak için kritiktir. Kimsenin çağıramadığı kodun hiçbir faydası yoktur.

---

## 🧯 Neden Geliştiriciler Test Yazmaz?

Bu bahaneleri sürekli duyuyorum.

İlk bahane: “Kodumun çalıştığını zaten biliyorum!” Evet, ama gelecekte kodunuz üzerinde çalışacak başkaları bir şeyi bozup bozmadıklarını bilmeyecek; buna “gelecekteki sen” de dahil! Programcılara şunu söylüyorum: Bir repoyu ne zaman klonlasanız ve pull yapsanız, yaptığınız ilk şey test senaryolarını çalıştırmaktır.

Aksi halde bir şeyi bozup bozmadığınızı ya da siz değiştirmeden önce zaten bozuk olup olmadığını nasıl bileceksiniz? Test senaryoları size bir temel sağlar; böylece diğer insanlar kodun hâlâ çalıştığını bilir.

Bir diğeri: “Ben bozuk kod yazmam!” Belki bozuk kod yazmıyorsunuzdur ama ortam sürekli alttan alttan değişiyor. Güvenlik açıkları yamalanıyor ve yeni kütüphaneler yükseltiliyor; dolayısıyla kodunuz artık çalışmayabilir.

Birisi şöyle bir şey diyebilir: “Apache Struts kütüphanesinde bir güvenlik açığımız var. Sunucularımızda güncelleyebilir miyiz?” Kodunuzu test eden ve bu kütüphanenin yeni sürümüyle çalıştığından emin olan test senaryolarınız yoksa, muhtemelen bunu yapmamalısınız.

Ve bunu yapmamak, Equifax’ta yaşanan güvenlik açıklarından da bildiğiniz gibi, felaket olabilir! Şu cümleyi güvenle söyleyebilmek için test senaryoları yazmak zorundasınız: “Test paketini çalıştırayım… evet, Struts’un yeni sürümü gayet iyi çalışıyor. Üretime dağıtın.”

En sevdiğim bahane: “Vaktim yok!” Bu en kötü bahane çünkü test etmek, sonunda size zaman kazandırır. Şimdi birkaç test senaryosu yazmaya harcadığınız zaman, ileride saatlerce ve saatlerce debug yapmaktan sizi kurtaracaktır.

Bana güvenin. Gelecekte kodunuzu kimin kullanacağını bilmiyorsunuz ve kodunuzun sağlam olduğundan emin olmak istersiniz. TDD, sağlam kod yazmaya devam etmenizi sağlar.

---

## 🔴🟢🔧 TDD İş Akışı: Red, Green, Refactor

Bu, TDD iş akışıdır. Sahip olmayı dilediğiniz kod için, başarısız olan bir test senaryosu yazarsınız. Sonra onu geçirecek kadar yeterli kod yazarsınız. Mükemmel olması gerekmez.

Güzel olması gerekmez. Testi geçirmesi gerekir. Sonra kodu daha iyi hâle getirmek ve kaliteyi artırmak için refactor edersiniz. Ve son olarak süreci tekrar edersiniz.

Bu, **Red, Green, Refactor** olarak bilinir. Test araçlarının çoğu bu şemayı takip eder. Bu araçlar, başarısız testleri kırmızı, geçen testleri yeşil renkte gösterir.

**Red, Green, Refactor** ismi buradan gelir.

---

## 🚀 TDD DevOps İçin Neden Önemli?

Her şeyden önce, geliştirirken zaman kazandırır. Koda yeni özellikler ekledikçe ya da mevcut özelliklerde değişiklik yaptıkça, test senaryoları bir şeyin bozulup bozulmadığını hızlıca size söyleyecektir.

Daha hızlı kod yazmanıza izin verir çünkü daha eminsinizdir. Bir değişikliğin kodunuzu bozup bozmadığı ya da bir şeyi bozup bozmadığı konusunda endişelenmek zorunda kalmazsınız. Kodu refactor ederken çok daha hızlı hareket edebilirsiniz çünkü test senaryolarının davranıştaki değişiklikleri yakalayacağını bilirsiniz.

TDD, kodun beklediğiniz gibi çalıştığını garanti eder. İstediğiniz davranışı tanımlamak için testleri önce yazarsanız, testler geçtiğinde o davranışı elde ettiğinizi bilirsiniz.

Ayrıca gelecekteki değişikliklerin kodu bozmaması anlamına gelir. Başarısız testler, birinin kodu bozan bir şey eklediğini size anında haber verir.

Son olarak ve en önemlisi, bir DevOps pipeline’ı (CI/CD pipeline) oluşturmak için, üretime hataları daha hızlı göndermek istemiyorsanız, tüm testlerin otomatikleştirilmiş olması gerekir. Birçok şirket bunu anlamıyor. *Continuous Integration (CI)* ve *Continuous Delivery (CD)* ile otomasyon istiyorlar ama testlerini otomatikleştirmiyorlar.

Ne yazık ki, testlerinizi otomatikleştirmeden bir CI/CD pipeline’ınız olamaz.

---

## 📌 Özet

Bu videoda şunları öğrendiniz:

* TDD, test senaryosunun kodun tasarımını ve geliştirilmesini yönlendirmesi demektir.
* TDD, daha hızlı ve daha fazla güvenle geliştirme yapmanızı sağlar.
* **Red, Green, Refactor** iş akışı; kırmızının başarısız, yeşilin başarılı olmasıyla ilgilidir ve kod kalitesini artırır.
* Bir DevOps **CI/CD pipeline** oluşturmak için önce testlerinizi otomatikleştirmelisiniz.
