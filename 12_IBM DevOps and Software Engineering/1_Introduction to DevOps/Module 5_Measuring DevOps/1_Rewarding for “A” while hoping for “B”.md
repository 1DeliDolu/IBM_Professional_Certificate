# 🏆 Rewarding for “A” while hoping for “B”

Bu videoyu izledikten sonra, geliştirmek istediğiniz şeyi ölçmenin önemini açıklayabilecek, sosyal ve DevOps metriklerinin değerini belirleyebilecek ve DevOps’un problem çözümüne yaklaşımınızı değiştirdiğini fark edebileceksiniz.

Bir kültürü nasıl değiştirirsiniz? Bu, Academy Management Journal’da Steven Kerr tarafından 1975’te yayımlanan “The folly of rewarding for A, while hoping for B” başlıklı bir makaledendir.

“Whether dealing with monkeys, rats, or human beings, it is hardly controversial to state that most organisms seek information concerning what activities are rewarded, and then seek to do (or at least pretend to do) those things, often to the virtual exclusion of activities not rewarded. The extent to which this occurs, of course, will depend on the perceived attractiveness of the reward offered, but neither operant nor expectancy theorists would quarrel with the essence of this notion.”

A için ölçüp B’yi elde etmeyi umamazsınız. Bu olmayacak, çünkü neyi ölçerseniz onu elde edersiniz.

---

## 📏 Önemli Olanı Ölçmek

Bu yüzden, önemli olanı ölçün. Eğer *widget üretimini* ölçerseniz, çok sayıda widget elde edersiniz. Eğer *kod satırı sayısını* ölçerseniz, çok sayıda kod satırı elde edersiniz. Aşağıya doğru sonsuz  *noktalı virgüller* .

Eskiden kod satırı sayısını binlerce satır kod ( *KLOC* ) ile ölçerdik. İyi bir kod mu? Bilmiyorum; umurumda değil.

Ben kaç satır kod yazdığımla ölçülüyorsam, o zaman *gereksiz uzun* kod yazacağım. Unutmayın, neyi ölçerseniz onu elde edersiniz.

---

## 🧩 Sıralama ile Ölçmenin Yan Etkileri

İnsanları birbirlerine göre sıralayarak ölçerseniz, *antisosyal davranış* elde edersiniz. Birçok şirket bunu yapar—insanları sıralarlar.

O zaman şunu netleştirelim. Benim ekip arkadaşımıma yardım etmemi istiyorsunuz ama bizi birbirimize karşı sıralayacaksınız? Yani ben onlara yardım edeyim, onlar benden daha iyi bir sıralama alsın, sonra benim istediğim zam veya terfiyi onlar alsın?

Evet, bu nasıl işleyecek?

Şirketler bunu sürekli yapıyor ve yönetimleri de bunu anlamıyor gibi görünüyor. Neyi ölçerseniz onu elde edersiniz.

---

## 🤝 Sosyal Davranış İçin Sosyal Metrikler

İnsanların sosyal olmasını istiyorsanız, onları sosyal olmaları üzerinden ölçmelisiniz. Geliştiricileri sosyal etkileşimleri ve kod ile bilgiyi paylaşmaları üzerinden ölçmelisiniz. Sosyal kodlayıcıları böyle elde edersiniz.

Sosyal kodlayıcıları ölçmek için kullanmayı sevdiğim iki metrik şunlar:

### 🔁 Kodunuzu Kim Kullanıyor?

Kim, sizin geliştirdiğiniz koddan faydalanıyor? Şirketin geri kalanı veya açık kaynak topluluğu, çözümlerinde yeniden kullanacak kadar değerli bulduğu kod mu geliştiriyorsunuz?

Ama bu bulmacanın yalnızca yarısı. Bu, insanları “kodlarını başkaları için nasıl değerli hale getirebilirler?” diye düşünmeye yönlendirir. Fakat ikinci metriğe ihtiyacınız var.

### 🧱 Siz Kimin Kodunu Kullanıyorsunuz?

Siz kimin kodundan faydalanıyorsunuz? Tekerleği yeniden icat ederek tüm geliştirme bütçemi boşa mı harcıyorsunuz, yoksa mevcut tekerlekleri kullanıp yalnızca var olmayan *özel (bespoke)* parçaları mı geliştiriyorsunuz?

Bu iki metrik de gereklidir çünkü her iki tarafı da teşvik eder: kod paylaşmayı ve birbirlerinin kodunu yeniden kullanmayı. Çünkü… neyi ölçerseniz onu elde edersiniz.

Sosyal davranış için sosyal metrik gerekir.

---

## 📈 DevOps ve Sürekli İyileştirme İçin Ölçümleme

DevOps tamamen *sürekli iyileştirme* ile ilgilidir. Bu da, doğru yönde gidip gitmediğinizi ölçebilmek için nereden geldiğinizi bilmeniz gerektiği anlamına gelir.

Bu, bir *baz çizgisi (baseline)* almakla başlar. Neyi iyileştirmek istiyorsunuz? Belki ürününüzün bir sürümünü dağıtmak şu anda 6 ekip üyesi ve 10 saat gerektiriyordur.

Belki her sürüm X dolara mal oluyordur. Bu ölçüm her ne ise, baz çizgisidir.

Sonra bir hedef oluşturmanız gerekir. Metrik hedefleri, bu sayılar üzerinde muhakeme etmenize ve ilerlemenizin başarısını değerlendirmenize olanak sağlar.

Belki dağıtım süresini 10 saatten 2 saate düşürmek istiyorsunuz. Bu oldukça ulaşılabilir bir hedeftir. Baz çizginiz 10 saat olduğunu belirler; bu yüzden 2 saate inmek üzere beş kat iyileştirme eşiğini hedeflersiniz.

Ya da 6 ekip üyesi gereksiniminden 1 ekip üyesine inmeyi isteyebilirsiniz.

Ya da üretimde bulunan hata sayısını azaltmak isteyebilirsiniz.

Her ne ise, bir hedef seçin ve her seferinde bir hedef üzerinde çalışın.

Sonra sürecinizin başarısını değerlendirirsiniz. 10 saatten 2 saate indiniz mi? Hayır mı? O zaman bu ölçümü elde edene kadar farklı bir şey deneyin.

Sonra bir sonraki hedef üzerinde çalışmaya başlarsınız.

---

## 🛠️ Problem Çözümünde Hedefin Değişmesi

DevOps hedefi değiştirir.

Eskiden, sunucunun asla düşmemesini sağlamaya çalıştığınız  *mean time to failure* ’ı ölçerdik. Bu eski tarz düşüncedir.

 *Mean time to failure* ’dan  *mean time to recovery* ’ye geçmemiz gerekir.

Sunucunun düşeceğini öngörürsünüz. Sadece hızlıca toparlanabildiğinizden emin olun.

Eğer uygulamalarınız, konteynerlerde birden fazla örnek olarak dağıtılan mikroservislerden oluşan bir koleksiyon olarak inşa edildiyse, yeni bir konteyner ayağa kaldırarak hızlıca toparlanabilirsiniz.

Ve müşteriniz, tek bir hata noktası olmadığı için servis düştüğünü hiç fark etmeyebilir. Konteynerler sürekli ayağa kalkıp iniyor olabilir; ama yeni bir konteyneri hızla çalıştırıp toparlanabiliyorsanız, düşmüş olması kimi ilgilendirir?

Müşteri fark etmedi bile.

Bu, erişilebilirlik hakkında tamamen yeni bir düşünme biçimidir.

---

## ✅ Özet

Bu videoda, geliştirmek istediğiniz şeyi ölçüp ödüllendirmeniz gerektiğini öğrendiniz.

Sosyal metrikleri ölçmek, sosyalleşmenin iyileşmesine yol açar ve DevOps metriklerini ölçmek, hedeflere doğru ilerlemeyi görmenizi sağlar.

DevOps, problem çözümünün hedefini arızayı önlemeden arızadan toparlanmaya dönüştürür.
