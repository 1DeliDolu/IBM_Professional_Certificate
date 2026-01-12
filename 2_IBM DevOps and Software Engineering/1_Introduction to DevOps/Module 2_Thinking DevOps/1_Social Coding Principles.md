# 👥 Social Coding İlkeleri

Bu videoyu izledikten sonra şunları yapabileceksiniz: Sosyal kodlama ilkelerini açıklamak ve çift programlamanın nasıl daha iyi kod ve daha iyi programcılar oluşturduğunu fark etmek.

Sosyal kodlama nedir? Ben buna “Inner Source için Open Source” demeyi seviyorum. Sosyal kodlama, açık kaynak topluluğunun yıllardır yaptığı bir şeydir. Yeni olan şey, bu kavramları kuruma taşımak ve iç projelerde topluluk olarak kodlamaktır.

Geçmişte geliştiriciler özel depolarda çalışırdı ve katkıda bulunmak için ekibin üyesi olmanız gerekirdi. Her şey erişim kontrol listeleri ve sıkı bir “bilmesi gereken” esasıyla kontrol edilirdi.

Bunun sorunu, kimsenin üzerinde çalıştığınızı bilmemesidir; dolayısıyla kodu yeniden kullanma imkânı yoktur çünkü kimse var olduğunu bile bilmez. Bu yüzden kurumlar sürekli tekerleği yeniden icat eder; çünkü kimse tekerleğin zaten yapılmış olduğunu bilmez.

Sosyal kodlamada depolar herkese açıktır ve herkesin kodu fork’layıp katkıda bulunması teşvik edilir. Bu, düşünme biçiminde çok büyük bir farktır. Geliştirme ekipleri “bu benim kodum ve başka kimse dokunamaz” diye düşünmeyi sever, ancak şirketin iyiliği için bunu aşmaları gerekir. Anarşi olacağını düşünebilirsiniz ama aslında oldukça iyi çalışır; çünkü depo sahibi tarafından kontrol edilir. Depoya sahip olan kişi katkılar üzerinde hâlâ tamamen kontrol sahibidir.

---

## 🧩 Sosyal Kodlama Hangi Sorunu Çözüyor?

Sosyal kodlama hangi problemi çözüyor? Diyelim ki bir bileşen görüyorsunuz; ihtiyacınızın %80’i, ama bazı eksik özellikler var. O eksik özellikleri nasıl eklersiniz? Şimdi bir karar vermeniz gerekir:

* Depo sahibine yeni bir özellik için talep açıp, talebinizin öncelik listelerinin en altında kalmasını mı göze alırsınız?
* Ya da daha kötüsü, fonları kesilir ve sizin talebiniz ilk kesilen şey olur.
* Veya başka bir ekibe bağımlı kalmamak için, ihtiyacınız olan %20 için kodun %100’ünü yeniden mi inşa edersiniz?

Üzücü ama birçok ekip ikincisini seçer ve ihtiyaç duyduğu işlevselliği elde etmek için tüm tekerleği yeniden icat eder.

Bu, herhangi bir şirket için çok büyük bir kaynak israfıdır, ama her zaman olur.

---

## 🔁 Sosyal Kodlama ile Çözüm Akışı

Peki sosyal kodlama ilkelerini benimsemek bunu nasıl çözer?

Depo sahibiyle yeni özelliği konuşursunuz ve onlar için geliştirmeyi siz üstlenmek üzere anlaşırsınız. Bu, onların yaptıklarının tamamından faydalanmanıza ve ihtiyaç duyduğunuz özelliği eklemenize imkân verir.

Bir GitHub Issue açar ve kendinize atarsınız; böylece herkes üzerinde çalıştığınızı bilir. Sonra depoyu fork’larsınız, bir branch oluşturursunuz ve değişikliklerinizi yaparsınız. İşiniz bittiğinde ve geri katkı sunacak bir şeyiniz olduğunda, incelemeye hazır olduğunuzu belirten bir pull request açarsınız ve depo sahibi kodunuzu ana projeye geri merge edip etmeyeceğine karar verir.

Depo sahipleri tamamen kontrol sahibidir. Merge’i onlar yaptığı için değişiklik isteyebilirler. Yeterli test kapsamınız yoksa daha fazla test yazmanızı isteyebilirler. Sizi ve katkınızı ekibin diğer üyeleri gibi değerlendirirler. Bu, kazan-kazan durumudur.

Siz başka bir ekibin kodundan ve ihtiyaç duyduğunuz tüm işlevsellikten faydalanırsınız; diğer ekip ise ücretsiz bir özellik kazanır. Şirket, kod yeniden yazılmak yerine yeniden kullanıldığı için para tasarrufu yapar ve herkes mutlu olur.

Açık kaynak böyle çalışır ve şirketlerin inner source’u da böyle ele alması gerekir.

---

## 👯 Pair Programming

Çift programlama, Extreme Programming’den alınmış sosyal kodlamanın bir yönüdür. İki programcının tek bir iş istasyonunu paylaşmasından oluşur (bir ekran, bir klavye ve fare ikili arasında paylaşılır).

Klavyedeki programcıya genellikle **“driver”** denir. Diğer programcı da programlama görevine aktif olarak dâhildir, ancak daha çok genel yön ve istikamet üzerine odaklanır; ona da **“navigator”** denir.

Driver yazarken navigator onların işini kontrol eder, belki bir şeyi araştırır ya da sırada ne geleceğini düşünür. Ardından yaklaşık 20 dakika sonra rollerini değiştirirler.

Bu şekilde ikisi de her rolü oynar.

İş yerinde mümkün olduğunda çift programlama yaparım. Sosyal kodlamanın bu yönünü severim. Kişisel zayıflıklarımdan biri, yeni bir değişkene veya fonksiyona ne isim vereceğim konusunda uzun uzun düşünüp durmamdır. Okunabilirliği mümkün olduğunca artırmak için mükemmel olmasını isterim. Başka biriyle fikir alışverişi yapmak, bu kararları daha hızlı vermeme yardımcı olur.

Çift programlamanın aynı işi yapmak için iki kat kaynak kullandığını düşünebilirsiniz, ama öyle değildir.

---

## ✅ Çift Programlamanın Faydaları

Çift programlamanın birçok faydası vardır.

İlk fayda daha yüksek kod kalitesidir. “Yüksek sesle programlama” diye bir şey vardır ve bu, kodun daha net anlaşılmasına yol açar.

Geçmişte kod yazdığımda, onu tek başıma yazardım ve sonra birine açıkladığımda, konuşurken bir bug fark ederdim. Kodu zihnimde gözden geçirirken bug’ı görmezdim, ama yüksek sesle anlatırken görürdüm. Birine kodu açıklamak zorunda olmak, açıklık zorlar. Bu da kusurların daha erken bulunması anlamına gelir.

Bu iyi bir şeydir çünkü bakım maliyetlerini süreç boyunca aşağı çeker. Sürecin daha geç bir aşamasında bulunan bir kusurun düzeltilmesi daha pahalıdır.

Çift programlama aynı zamanda beceri transferini zorlar ve daha iyi programcılar oluşturur. Junior programcıları senior geliştiricilerle eşleştirmeyi severim. Bunu sürekli yaparım; böylece her biri diğerinin probleme yaklaşımından öğrenir. Diğerinin kullandığı ipuçlarını ve küçük teknikleri kaparlar. Daha iyi programcılar oluşturur.

Ayrıca her satır kod üzerinde iki çift gözünüz olur. Sadece bir kişinin anladığı kod istemezsiniz. Sonra o kişi tatile gider ve kimse onun kodunu nasıl düzelteceğini bilmez. Çift programlama, kodun daha iyi anlaşılmasına yol açar. Daha fazla kişi kodu düzeltip geliştirecek kadar iyi anlar.

---

## 🧾 Özet

Bu videoda şunları öğrendiniz:

Sosyal kodlama, herkese açık depolarla topluluk halinde yapılır ve tüm ekip üyeleri katkı vermeye teşvik edilir.

Çift programlama, kusurlar daha erken bulunduğu, maliyetler düştüğü ve kod tabanına dair daha geniş bir anlayış oluştuğu için daha yüksek kaliteli kodla sonuçlanır.
