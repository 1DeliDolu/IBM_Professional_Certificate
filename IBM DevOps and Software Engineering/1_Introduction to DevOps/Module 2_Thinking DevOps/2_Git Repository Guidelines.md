# 🗂️ Git Deposu Yönergeleri

Bu videoyu izledikten sonra,  *Git Feature Branch Workflow* ’unun sosyal kodlamayı nasıl desteklediğini açıklayabileceksiniz.

Depolarınız ve iş akışınız için yönergeler hakkında konuşalım.

Her bileşen için, ister bir *mikroservis* ister üzerinde inşa ettiğiniz başka bir şey olsun, bir depo oluşturun. Birden fazla mikroservisi tek bir depoya koymayın. Bunlara *mono repo* denir ve hoş karşılanmazlar.

İnsanlar genellikle gösterimleri kolaylaştırmak için birden fazla mikroservisin içinde olduğu tek bir depo olan “ *mono repo* ”yu oluştururlar, ancak bu üretim kodu için yapılmamalıdır. Birinin, umursamadığı pek çok kodu sırf umursadığı koda ulaşmak için çekip çıkarmasını istemezsiniz.

Her depo için bir bileşen veya mikroservis olmasını istersiniz. Bu çok önemlidir. Birden fazla depoya sahip olmaktan çekinmeyin.

---

## 🌿 Her İş İçin Yeni Branch

Üzerinde çalıştığınız her issue için yeni bir branch oluşturun. Uzun ömürlü branch’ler istemezsiniz. Tüm işlerin birleştirildiği ve yapıldığı bir "development" branch’ine sahip olmaya inanmıyorum. Bu eski düşünme biçimidir.

Branch’ler Git’te çok hafiftir. Bir *master* branch vardır ve *feature* branch’ler vardır, hepsi budur. Feature branch’i bitirdiğinizde onu silersiniz. Ona fazla bağlanmayın; çünkü onu siler ve üzerinde çalıştığınız bir sonraki issue için yeni bir tane oluşturursunuz.

---

## 🔀 Pull Request ile Master’a Birleştirme

Kodunuzu tekrar master’a birleştirmek için *pull request* kullanın. Kodun master branch’ine girmesinin tek yolu bir pull request üzerinden olmalıdır. Pull request, diğer insanların kodunuza bakıp incelemesi için bir fırsat sağlar.

Kendi pull request’inizi asla merge etmeyin. Yapmayın. Her zaman ekipten başka birinin pull request’inizi merge etmesini istersiniz; çünkü her pull request bir kod incelemesi fırsatıdır. Kodun gözden geçirilmesini, onlara mantıklı gelip gelmediğinin kontrol edilmesini sağlayın ve sonra merge işlemini onların yapmasını sağlayın.

Bu şekilde depoya giren tüm kodlarda iki çift göz olur.

---

## 🧩 Git Feature Branch Workflow Nasıl Çalışır

Buna *Git Feature Branch Workflow* diyoruz ve işte nasıl çalıştığı. GitHub Repo ile başlayalım.

Bileşeniniz için yeni deponuzu oluşturursunuz veya başka birinin bileşenine katkıda bulunuyorsanız mevcut bir depoyu *fork* edersiniz.

Sonra bunu çalışma istasyonunuza *clone* edersiniz ve bu sizin yerel deponuz olur. Tüm değişiklikleriniz bu depoda yapılacaktır.

Sonra özelliğiniz üzerinde çalışmak için bir branch oluşturursunuz. Bu, hatalar veya diğer düzeltmeler için de takip edilebilir. Buna *feature branch* denir, ancak fikir şu ki bu, üzerinde çalıştığınız GitHub Issue ile ilişkili kodun bulunduğu branch’tir.

Kodu ana projeye geri göndermeye hazır olduğunuzda veya sadece birinin değişikliklerinizi gözden geçirip geri bildirim vermesini istediğinizde, kodunuzu uzak bir branch’e *push* edersiniz.

Son olarak, değişikliklerinizin gözden geçirilmesi için bir pull request oluşturursunuz.

Pull request incelenecek ve kod tamamlandıysa ve ekip tarafından belirlenen standartları karşılıyorsa, master branch’ine geri merge edilecek ve orijinal GitHub deposunun bir parçası hâline gelecektir.

---

## ✅ Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz: Her bileşen için bir depo oluşturmanın, Git Feature Branch iş akışını takip etmenin, ardından branch’ler oluşturmanın ve pull request kullanmanın iyi bir uygulama olduğu.
