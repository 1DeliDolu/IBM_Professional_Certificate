# 📦 Küçük Partilerle Çalışmak

Bu videoyu izledikten sonra, küçük partilerle çalışmayı açıklayabilecek ve *tek parça akışının* ( *single piece flow* ) daha hızlı geri bildirim sağladığını fark edebileceksiniz.

Küçük partilerle çalışmak, *Yalın Üretim* ( *Lean Manufacturing* ) kökenli bir kavramdır. Hızlı geri bildirimin gerektiği durumlarda önemlidir; çünkü kararlarınızdan hızlıca öğrenmenizi sağlar. Bir hipotezi test ediyor olabilirsiniz ve işe yarayıp yaramadığını bilmeden çok ilerlemek istemezsiniz. Küçük partilerle çalışmak, daha fazla deney yapmanıza ve hızlıca içgörü kazanmanıza imkân tanır.

Buna karşılık, tamamlanması aylar süren büyük partilerle çalışmak, aylarca geri bildirim alamamanız anlamına gelir. Küçük partilerle çalışmak aynı zamanda israfı da en aza indirir. Çünkü geri bildirimi daha hızlı alırsınız ve müşterinizin beğenmediği şeyleri geliştirmek için zaman harcamazsınız.

Büyük partiler kullanırken, müşteri istemediği bir şeyi geliştirmek için aylar harcayabilirsiniz. DevOps uygulamalarındaki *çapraz fonksiyonlu ekipler* ve *hafif yaklaşımlar* doğrultusunda, geliştirmeden test ve operasyonlara, oradan da dakikalar içinde üretime hızlı şekilde ilerlemenin en iyi yolu küçük partilerle çalışmaktır.

---

## 📬 Büyük Parti ve Küçük Parti Karşılaştırması

Büyük partiler ile küçük partilerle çalışmayı karşılaştıran bir örneğe bakalım. Diyelim ki bin broşürü postalamam gerekiyor. Adımlar şunlar:

1. Broşürleri katlamak
2. Broşürleri zarflara koymak
3. Zarfları kapatmak
4. Zarflara pul basmak

Bu broşür örneğini, büyük parti ve küçük parti yürütmesini karşılaştırmak için kullanacağız. Diyelim ki ilk bin broşürü 50’lik partiler hâlinde işleyeceğim.

Bunlar büyük partilerdir; her partide 50 broşür vardır. Her adımın tamamlanmasının yaklaşık altı saniye sürdüğünü varsayın. Yani dakikada yaklaşık 10 adım yapabilirim.

İlk adım olan katlamayla başlıyorum. Dakikada 10 tane yaptığımda, 50 tanesini katlamam yaklaşık beş dakika sürer. Sonra bir sonraki adıma geçerim: hepsini zarflara yerleştirmek.

Dakikada yaklaşık 10 tane yapabilirim, bu da beş dakika daha sürer; önceki beş dakika ile birlikte artık 10 dakika olmuş olur. Hepsi katlandı ve zarflara konduktan sonra bir sonraki adıma geçerim: hepsini kapatmak. Dakikada 10 tane kapatıyorsam, 50 tanesi için beş dakika daha gerekir. Böylece duvar saati zamanı ( *wall clock time* ) olarak 15 dakikaya ulaşırım.

Son olarak dördüncü adım olan pullamaya gelirim ve ilk bitmiş ürünü elde etmem 16 dakika sürer. Bu, kaliteyi kontrol etmek için gerçekten inceleyebileceğim ilk andır. Ya zarflarda hiç yapıştırıcı yoksa?

Bir şeylerin yanlış gittiğini fark etmem 11 dakika sürecekti. Ya broşürde bir yazım hatası varsa? En başa dönmem gerekir. Yani bu büyük partilerle çalışmak oldukça israf yaratır.

---

## 🔁 Tek Parça Akışı ile Küçük Partiler

Şimdi aynı örneğe, *tek parça akışı* ( *single piece flow* ) kullanarak küçük partilerle bakalım. Yine her adımın yaklaşık altı saniye sürdüğünü varsayalım.

Tek parça akışında bir tane katlarım, zarfın içine koyarım, kapatırım ve pul basarım; ilk bitmiş ürün yaklaşık 24 saniyede ortaya çıkar.

Artık onu inceleyebilirim, çalışıp çalışmadığını görebilirim, düşündüğüm şey olup olmadığını kontrol edebilirim ve kabul edilebilir ise akışın geri kalanının devam etmesine izin veririm. Büyük partide 11 dakika süren hızlı geri bildirimi, burada yalnızca 24 saniyede almış olurum.

Ya zarflarda hiç yapıştırıcı yoksa? Yaklaşık 18 saniyede öğrenirdim. Broşürde yazım hatası varsa, 24 saniye sonra. Büyük partilerle çalışmamamız çok önemlidir. Hızlı geri bildirime ihtiyacımız var, böylece gerekirse hızlıca yön değiştirebiliriz.

Küçük partilerle çalışmak, *Sürekli Entegrasyon* ( *Continuous Integration* ) ve *Sürekli Teslimat* ( *Continuous Delivery* ) gibi diğer DevOps uygulamalarını hayata geçirmenize yardımcı olur.

---

## 🧩 Partilerinizin Yeterince Küçük Olduğunu Nasıl Anlarsınız?

Partilerinizin yeterince küçük olup olmadığını nasıl anlarsınız? Ben,  *backlog* ’unuzdaki hikâyelerin ( *stories* ) boyutuyla başlardım. Uygulama özellikleriniz, sık sürümleri destekleyecek şekilde ayrıştırılmış mı?

Kendinize şu soruları sormalısınız:

* Sürümler ne sıklıkla mümkün?
* Özellikler çok büyük olduğu için sürümde gecikmeler oluyor mu?
* Özellikler bir sprint içinde tamamlanabiliyor mu?

Eğer birkaç sprint süren özellikleriniz varsa, partileriniz fazla büyüktür. İdeal olarak bir özellik, bir hafta veya daha kısa sürede tamamlanabilecek kadar küçük olmalıdır.

İnşa ettiğiniz özellikler, bir hedefe doğru atılan bir adımdır. Pek çok kişi yalnızca tamamlanmış bir hedefin göndermeye değer olduğunu düşünür. Bunun yerine, nihai hedefe doğru geri bildirim kazanmak için artışlar hâlinde teslim edilebilecek faydalı alt kümeler düşünülmelidir.

---

## ✅ Özet

Bu videoda, küçük partilerle çalışmanın hızlıca faydalı bir şey teslim etmek anlamına geldiğini öğrendiniz. Ayrıca *tek parça akışı* kullanmanın daha hızlı geri bildirim döngülerine yol açtığını öğrendiniz.
