# 🔄 Sürekli Entegrasyon (CI) Nedir?

“ **Sürekli Entegrasyon Nedir?** ” bölümüne hoş geldiniz. Bu videoyu izledikten sonra şunları yapabileceksiniz: Sürekli Entegrasyon’u ( *Continuous Integration* ), yani  **CI** ’ı tanımlamak, CI’nin ana özelliklerini açıklamak ve CI tabanlı geliştirme ile geleneksel geliştirme arasındaki farkı açıklamak.

![1766090238107](image/2_WhatIsContinuousIntegration(CI)/1766090238107.png)

Sürekli Entegrasyon (*Continuous Integration* ya da  **CI** ), adından da anlaşılacağı gibi, kod değişikliklerinin ana kod tabanına sürekli olarak entegre edilmesini sağlayan bir otomasyon sürecidir. Geliştiricilerin çalışmalarını düzenli olarak bir depoya ( *repository* ) entegre etmelerine olanak tanır; böylece değişiklikleri *master* ya da *main* daldan çok fazla uzaklaşmaz. Bir geliştirici çalışmasını kaynak kod deposuna ( *source code repository* ) gönderdiğinde, CI; herhangi bir bozulmayı tespit etmek için bir dizi testi otomatik olarak çalıştırarak yazılımın düzgün çalışmaya devam etmesini sağlar.

CI, ekip genelinde iş birliğine dayalı geliştirmeyi mümkün kılar; çünkü bir geliştirici birim testlerini ( *unit tests* ) çalıştırmayı unutsa bile CI süreci testleri onun yerine çalıştırır ve herhangi bir başarısızlık durumunda onu uyarır. Bu da entegrasyon hatalarının ( *integration bugs* ) daha geç değil, daha erken tespit edilmesine yardımcı olur.

![1766090285253](image/2_WhatIsContinuousIntegration(CI)/1766090285253.png)

---

## 🏗️ Geleneksel Geliştirmeyi Anlamak

CI’ye geçmeden önce geleneksel geliştirmeyi anlamanız gerekir. Geleneksel olarak geliştiriciler büyük özellikler veya düzeltmeler üzerinde çalışır ve bunları kendi geliştirme dallarına ( *development branches* ) commit eder. Bu dallar uzun süre var olabilir, kapsamı büyük olabilir ve genellikle çok sayıda kod değişikliği ve düzenleme gerektirir.

Bu dallardaki geliştirme tamamlandıktan sonra ancak o zaman test edilir ve ana dala birleştirilir ( *merged into the main branch* ); ardından üretim için derlenir ( *built for production* ). Bu geliştirme yöntemi, ana dal ile geliştirme dalı arasında **sapmaya** ( *drift* ) ve diğer sorunlara yol açabilir.

![1766090325388](image/2_WhatIsContinuousIntegration(CI)/1766090325388.png)

---

## ⭐ CI’nin Ana Özellikleri

CI’nin ana özellikleri şunlardır:

* Kısa ömürlü dallar ( *short-lived branches* )
* Sık yapılan pull request’ler
* Otomatik CI araçları

CI’de geliştiriciler kodlarını geliştirdikleri kısa ömürlü özellik dallarında ( *feature branches* ) çalışır.

![1766090344892](image/2_WhatIsContinuousIntegration(CI)/1766090344892.png)

---

## 🌿 Kısa Ömürlü Dallar

Bu dallar, ana veya *master* dala hızlıca geri birleştirilebilmesi için, koda katkı sağlayan küçük özellikleri geliştirmek amacıyla tasarlanmıştır. Dal, birleştirildikten sonra silinir; çünkü tek amacı o küçük özelliği geliştirmekti.

Bu, birkaç temel fayda sağlar:

* Özellik dalları ile ana dal arasında oluşabilecek sapmayı ( *drift* ) azaltır.
* Kritik veya gerekli düzeltmeler, geliştiriciler kendi özellikleri üzerinde çalışırken birden fazla kişi tarafından farklı şekillerde uygulanabilir. Ancak CI ile geliştiriciler, test edilip birleştirilecek tek bir düzeltmeyi hızlıca uygulayabilir; böylece paralel değişiklikler azalır.

Sonuç olarak bu, kodunuzu genel olarak daha hızlı dağıtabilmeniz ( *deploy* ) anlamına gelir; çünkü her push işleminde değişiklikleri kontrol ettiğiniz için kapsamlı bir kod inceleme sürecinden geçmeniz gerekmez.

![1766090403147](image/2_WhatIsContinuousIntegration(CI)/1766090403147.png)

---

## 🔁 Sık Pull Request Oluşturma

*Master* veya *main* dala sık pull request göndermek bir **en iyi uygulamadır** ( *best practice* ). Bu pull request’ler, belirli bir amaca hizmet eden kod güncellemelerini içermelidir. Bu, kod değişikliklerini daha temiz ve anlaşılması daha kolay hale getirir.

Bir pull request’in başarıyla birleştirilebilmesi için bir depo bakım sorumlusu ( *repository maintainer* ) veya sahibi ( *owner* ) tarafından onaylanması gerekir. En azından hiç kimse kendi pull request’ini onaylayamamalıdır. Her değişikliğin üzerinde en az iki çift göz olmasını istersiniz.

Bu sık pull request’ler, çok daha büyük bir yapbozun küçük parçaları gibi çalışır ve en güncel kodun üzerine inşa etmeyi kolaylaştırır.

![1766090470635](image/2_WhatIsContinuousIntegration(CI)/1766090470635.png)

---

## 🤝 İş Birliği ve Hızlı Tepki Yeteneği

Bu işlev, birçok faydayı beraberinde getirir:

Her pull request’in gözden geçirilmesi gerekir; bu da geliştiriciler arasında artan iş birliğini destekler. Ayrıca geliştiricilerin hızlı tepki vermesini sağlar. Gerekli değişiklikler daha hızlı test edilip üretime alınabilir; böylece çözümler müşteriye daha hızlı ulaşır.

Sürekli Entegrasyon’un sıklığı sayesinde, bugüne kadar ne kadar işlevsellik geliştirdiğinizi tam olarak bilirsiniz; bu da yönetim riskini azaltır. Gerekli işlevselliği zamanında teslim edip edemeyeceğinizi daha iyi öngörmenizi sağlar.

---

## ⚙️ CI Otomasyonu Ne Demektir?

Sürekli Entegrasyon otomatikleştirilebilir. Peki bu ne anlama gelir?

Otomatik CI araçları (sağ taraftakiler gibi), *webhook* kullanarak pull request’ler ve dosya değişiklikleri gibi olaylara ( *events* ) abone olur ve ardından bir iş akışını ( *workflow* ) tetikleyebilir.

Bu iş akışı, bir uygulamayı derlemek ( *building an application* ) gibi herhangi bir şey olabilir. Tamamlandığında bu araçlar, başarılı veya başarısız bir derleme hakkında mesajlarla geri bildirimde bulunur.

Bu araçlar, dosya değişikliklerinizin veya pull request’lerinizin tüm uygulamayı bozmadığından emin olmak için testler çalıştırabilir. Bu otomasyon araçlarıyla, geliştirme sürecinizi sadeleştirebilirsiniz; böylece kodunuzu test etmek ve kontrol etmek hiçbir zaman yorucu bir iş olmaz.

![1766090522689](image/2_WhatIsContinuousIntegration(CI)/1766090522689.png)

---

## 🧾 Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

CI, kısa ömürlü dallardan yararlanarak kodu küçük parçalar halinde ve sıkça entegre etmek için kullanılan süreçtir. Bu, geliştiriciler arasında iş birliğini teşvik eder; geliştiriciler, öz ve net değişiklikler için pull request’leri sıkça tartışır. Ayrıca, geliştirmeyi ve test etmeyi sadeleştirerek CI’nin uygulanmasını kolaylaştıran araçlar vardır.

![1766090541082](image/2_WhatIsContinuousIntegration(CI)/1766090541082.png)
