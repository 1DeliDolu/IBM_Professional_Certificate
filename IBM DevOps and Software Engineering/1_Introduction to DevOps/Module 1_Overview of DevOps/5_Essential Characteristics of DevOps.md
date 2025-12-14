# ⚙️ DevOps’un Temel Özellikleri

Bu videoyu izledikten sonra şunları yapabileceksiniz: Uygulamaların DevOps’un ortaya çıkmasına yol açacak şekilde nasıl evrildiğini açıklamak, DevOps’un üç boyutunu listelemek ve DevOps’un bazı temel özelliklerini tanımlamak.

Hedefi gözden kaçırmayalım. Hedef nedir? Hedef çevikliktir ( *agility* ). Akıllı denemeler yapıyor olmak istersiniz. Pazarda maksimum hız ve minimum riskle ilerlemek istersiniz. Bu şekilde, değer önerisini ve müşterilerinize sunduğunuz kaliteyi tutarlı biçimde değiştirmek için hızlı, değerli içgörüler elde edebilirsiniz.

---

## 🧱 Çeviklik İçin Üç Sütun

Çeviklik için üç sütun vardır. Sütunlardan biri DevOps’tur. Buna kültürel değişim, otomatikleştirilmiş hatlar ( *automated pipelines* ), *infrastructure as code* ve *immutable infrastructure* dahildir.

İkinci sütun *microservices*tir ve REST API’leri üzerinden iletişim kuran gevşek bağlı ( *loosely coupled* ) bir uygulama tasarımını içerir. Mikroservisler, arızaya karşı dayanıklı olacak şekilde tasarlanır ve onları bozarak ve hızlı başarısız olarak ( *failing fast* ) test edilir.

Üçüncü sütun *containers*tır. Container’lar taşınabilirlik ( *portability* ) ve hızlı başlangıç ( *fast startup* ) sağlayan, geliştirici merkezli ortamlardır.

Ayrıca *immutable infrastructure* ile hızlı dağıtımlar sağlayan bir ekosistemi mümkün kılarlar. Buna “mükemmel fırtına” demeyi seviyorum. Ayrı ayrı ele alındığında bunlar tek başlarına etkileyici teknolojilerdir; ancak birlikte güçlü bir değişimi mümkün kılarlar. Hız ve çeviklik için DevOps, küçük dağıtımlar için mikroservisler ve hızlı başlangıçla geçici çalışma süreleri ( *ephemeral run times* ) için container’lar.

*Ephemeral* çok kısa süre devam eden anlamına gelir. Geçicidirler çünkü bir container bozulduğunda onu düzeltmeye çalışmayız. Sadece siler ve yenisiyle değiştiririz.

Bunlar “atılabilir” ( *throw-away* ) çalışma süreleridir.

---

## 👥 DevOps Kültürü

Tony Stafford şöyle diyor: “DevOps, farklı çalışmayı öğrenmekle başlar. Açıklık ( *openness* ), şeffaflık ( *transparency* ) ve saygıyı ( *respect* ) temel sütunlar olarak benimseyen çapraz fonksiyonlu ekipleri ( *cross-functional teams* ) kucaklar.”

Bu büyük bir beklenti. Kurumunuz açıklığı, şeffaflığı ve saygıyı benimsiyor mu? DevOps olmak için gereken budur.

Şimdi uygulama evriminden biraz bahsedelim.

---

## 🧬 Uygulamaların Evrimi

Geçmişte Waterfall vardı; fiziksel sunucular üzerinde dağıtılan monolitik uygulamalarla.

Sonra, zamanın bir noktasında Agile’a geçtik ve  *Service Oriented Architecture* ’lar ile sanal makineler ( *virtual machines* ) kullandık.

Ardından DevOps geldi. Şimdi *immutable containers* içinde dağıtılan mikroservisler kullanıyoruz.

Bu artımlı ( *incremental* ) bir evrim olmuştur. Monolitleri servislere böldük. Servisler hâlâ büyüktü; *Service Oriented Architecture* kullanıyordu, ancak tasarım konsepti olarak servisleri benimsemiştik.

Sonra sanallaştırma ( *virtualization* ) ve Cloud geldi. Bu, işleri çok daha küçük hale getirdi. DevOps ile tekrar evrildik; mikroservislere ve onları dağıtmak için container’lara.

---

## 📐 DevOps’un Üç Boyutu

DevOps’un üç boyutu vardır: kültür ( *culture* ), yöntem ( *method* ) ve araçlar ( *tools* ).

Çoğu şirket araçlara odaklanır. Çoğu satıcı da araçlara odaklanır çünkü satabilecekleri tek şey budur. Bazı şirketler yöntemlere de odaklanır; bunlar önemlidir.

Ama odaklanılacak en önemli şey kültürdür!

Atlassian şöyle diyor: “Kültür, DevOps’ta bir numaralı başarı faktörüdür. Paylaşılan sorumluluk, şeffaflık ve daha hızlı geri bildirim kültürü inşa etmek, her yüksek performanslı DevOps ekibinin temelidir.”

Yüksek performanslı bir DevOps organizasyonu olmak istiyorsanız kültürünüzü değiştirmeniz gerekir. Araçlar ve yöntemler önemli olsa da… en büyük etkiyi kültür yaratır.

---

## 🧠 Kültür Nasıl Değiştirilir?

Bir kültürü nasıl değiştirirsiniz? Kültür, içimize işlemiştir.

Kim olduğumuzu tanımlar. Dilimiz, yiyeceğimiz, değerlerimiz ve hikâyelerimiz gibi unsurları içerir. Bir kültürü değiştirmek son derece zordur. Ülkelerin kültürleri vardır. Şirketlerin kültürleri vardır.

Birçok şirket DevOps olmaya çalışır ama kültürünü değiştirmeyi başaramaz. Bu değişim, gerçekleşmesi için yukarıdan aşağıya gelmeli ve aşağıdan yukarıya benimsenmelidir.

Bu kolay bir şey değildir. Bir kültürü nasıl değiştirirsiniz?

İnsanların düşünme biçimini değiştirmelisiniz. Farklı düşünmeye başlamaları gerekir. *Social coding* ve paylaşımı düşünmeniz gerekir.

Çalışma biçimlerini değiştirmelisiniz. Farklı çalışmaya başlamaları gerekir.

Küçük partiler halinde çalışmak ve test güdümlü ( *test-driven* ) ve davranış güdümlü geliştirme ( *behavior-driven development* ) kullanmak.

Organize olma biçiminizi değiştirmelisiniz. Pek çok şirket bunu anlamıyor. Farklı organize olmalısınız çünkü organizasyon, bir şeyleri nasıl inşa ettiğiniz üzerinde doğrudan etkiye sahiptir.

Hepsinden önemlisi, insanların nasıl ölçüldüğünü değiştirmelisiniz. Ölçüm sisteminizi değiştirmeniz ve farklı ölçmeniz gerekir çünkü her zaman ölçtüğünüz şeyi elde edersiniz.

Bu kursun geri kalanında, DevOps düşünme, çalışma, organize olma ve ölçme biçimini inceleyeceğiz.

---

## ✅ Bu Videoda Öğrendikleriniz

Bu videoda şunu öğrendiniz: Uygulamalar, monolitlerin Waterfall geliştirmesinden mikroservislerin Agile geliştirmesine evrildi.

DevOps’un üç boyutu vardır: kültür, yöntem ve araçlar.

Ve DevOps’un temel özellikleri; kültürel değişim, otomatikleştirilmiş hatlar,  *infrastructure as code* , mikroservisler, container’lar ve  *immutable infrastructure* ’ı içerir.
