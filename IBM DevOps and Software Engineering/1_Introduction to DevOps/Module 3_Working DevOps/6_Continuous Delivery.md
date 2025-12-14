# 🚚 Continuous Delivery

Bu videoyu izledikten sonra bir  *CI/CD pipeline* ’ını açıklayabilecek,  *continuous delivery* ’yi tanımlayabilecek,  *continuous delivery* ’nin beş temel ilkesini sıralayabilecek,  *continuous deployment* ’ı tanımlayabilecek ve DevOps’un riski nasıl yönettiğini açıklayabileceksiniz. Martin Fowler,  *Continuous Delivery* ’yi, yazılımı üretime ( *production* ) herhangi bir zamanda çıkarılabilecek şekilde geliştirdiğiniz bir yazılım geliştirme disiplini olarak tanımlar. Bunu söylemek yapmaktan daha kolaydır.

Martin Fowler’ın “herhangi bir zamanda üretime çıkarabilmek” ile ne demek istediğiyle başlayalım. Bu,  *master branch* ’in her zaman dağıtıma hazır ( *deployable* ) olması gerektiği anlamına gelir. Bunu yapmak için her değişikliği *build* edip test etmeniz gerekir. Her değişikliği *build* etmek ve test etmek  *continuous integration* ’ın tanımıdır; dolayısıyla  *continuous delivery* , *continuous integration* gerektirir.

Bu, insanların neden CI/CD’yi tek bir kelime gibi söylediğini açıklayabilir; çünkü  *continuous delivery* ’yi uygulayabilmek için önce  *continuous integration* ’ın kurulmuş olması gerekir. Bir şeyin “build’i bozup bozmayacağını” bilmenin bir yoluna ihtiyacınız vardır. Bunu başarmanın bir yolu, her değişikliği *production-like* bir ortama teslim etmektir. Bu, gerçek üretim ortamı olmak zorunda değildir; ancak üretime dağıtmak için kullanılan prosedürün aynısının kullanılabilmesi için ona yeterince benzemelidir.

Bu süreçte  *unit testing* ,  *integration testing* , kalite kontrolleri, zafiyet taramaları ( *vulnerability scans* ), güvenlik testleri gibi kontrollerden oluşan bir pipeline yaratan otomatik kapılar ( *automated gates* ) bulunur. Bu testler kodun kalitesini güvence altına alır. Tüm bunlar kurulduğunda buna bir *CI/CD pipeline* deriz.

Bir pipeline gibi, bu da bir aracın çıktısının diğerinin girdisini beslediği bir araçlar bütünüdür.

---

## 🧩 CI/CD Pipeline Kurmak İçin Neler Gerekir?

Bir *CI/CD pipeline* kurmak için gerekenlerden bahsedelim.

İlk olarak, tüm kaynak kodunuzu barındırmak ve yönetmek için bir kod deposuna ( *code repository* ) ihtiyacınız vardır. Bu, pipeline’ı başlangıçta besleyen giriş noktasıdır. Sonra, uygulamayı kaynak koddan derlemek için bir  *build server* ’a ihtiyacınız vardır. Travis CI ve GitHub Actions gibi çoğu bulut tabanlı CI/CD aracı bunu sizin için sağlar.

Ardından,  *build* ’i otomatikleştirmek ve kalite ile diğer testleri çalıştırmak için bir *integration server/orchestrator* gerekir. IBM Cloud Continuous Delivery gibi çoğu bulut tabanlı CI/CD pipeline, size bir orkestrasyon yeteneği sunar.

Ayrıca, ikilileri ( *binaries* ), yani uygulamanın artifact’larını saklamak için bir  *artifact repository* ’ye ihtiyacınız olacaktır. Burası, test edilmiş ve çalıştığı kanıtlanmış *Java jar* ve *war* dosyalarının,  *Python wheel* ’lerin,  *Ruby gem* ’lerin,  *Docker image* ’larının veya her ne tür derlenmiş artifact varsa onların saklandığı yerdir.

Son olarak, dağıtım ortamınızın otomatik konfigürasyonu için bir araca ihtiyacınız olacaktır. Yine çoğu bulut tabanlı CI/CD pipeline aracı, dağıtımınızı otomatikleştirmek için bir yol sağlar.

*Continuous Integration* ve  *Continuous Delivery* ’yi yazılım geliştirme yaşam döngüsünün ( *software development lifecycle* ) üzerine bindirdiğimizde şunu görürüz:  *plan* ,  *code* , *build* ve *test*  *continuous integration* ’ın parçasıdır.  *release* , *deploy* ve *operate* ise  *continuous delivery* ’nin parçasıdır.

Bunlar, birbirini besleyen iki döngüdür: CI ve CD.

---

## 🧱 Continuous Delivery’nin Beş Temel İlkesi

 *Continuous Delivery* ’nin kalbinde yer alan beş temel ilke vardır.

Birincisi  *built in quality* ’dir. *CI/CD pipeline* burada devreye girer; çünkü her kod değişikliğinin, yüksek kod kalitesini sağlamak için sıkı kontrollerden geçmesine imkân tanır.

İkinci ilke, küçük partiler halinde çalışmaktır ( *working in small batches* ). Küçük partiler halinde çalışmak önemlidir; çünkü daha küçük değişiklikler test etmeyi kolaylaştırır ve bir şeyin bozulma riskini azaltır.

Üçüncüsü, bilgisayarların tekrarlayan görevleri yapmakta iyi olduğunu kabul etmektir; insanlar ise pek değil. İnsanlar problem çözmekte iyidir. Tekrarlayan işleri bilgisayarlarla otomatikleştirmek ve problem çözmeyi insanlara bırakmak en iyisidir.

Dördüncü temel ilke, durmaksızın sürekli iyileştirmeyi ( *continuous improvement* ) kovalamaktır. Her zaman iyileştirme yolları aramalıyız. Bu, *actionable measurements* ile ölçmemiz ve ölçüm bize neyi iyileştirebileceğimizi gösterdiğinde harekete geçmemiz gerektiği anlamına gelir.

Son olarak beşinci ilke, herkesin sorumlu olmasıdır ( *everyone is responsible* ). Bir *build* bozulduğunda, build’i düzeltmeye yardımcı olmak herkesin sorumluluğudur. Bozuk build’ler herkesin ilerlemesini engeller.

---

## 🚀 Continuous Deployment

“ *Continuous deployment* ” terimini bilmenizi istiyorum. Keşke bunu,  *continuous delivery* ’nin baş harflerinden ayırt etmek için “continuous release” olarak adlandırsalardı.  *Continuous deployment* , üretime dağıtım ( *deploying to production* ) için ayrılmıştır.

Bu grafikten,  *continuous integration* ’ın sürüm kontrolüne kod göndermeyi ve entegre edildikten sonra build ve testleri otomatikleştirmeyi kapsadığını görebilirsiniz. Ardından *continuous delivery* devralır; build’den çıkan artifact’ları kullanır ve onları otomatik olarak bir ortama dağıtır. Otomasyon ile üretime dağıtım yaptığımızda buna *continuous deployment* denir.

---

## 🛡️ DevOps Riski Nasıl Yönetir?

Şu anda kendinize “Bunca otomasyon riskli gibi geliyor” diye düşünüyor olabilirsiniz. Bu riski nasıl yönetirsiniz? DevOps, değişimden kaçınmak yerine değişim hızını artırarak riski yönetir. Kulağa ters gibi gelir ama şöyle çalışır:

DevOps’ta dağıtım kraldır; dağıtım acısız olmalıdır. Erken ve sık deploy etmek istersiniz. Amaç, kas hafızası ( *muscle memory* ) oluşturmaktır.

Kodunuz üretime gitmeden önce onu birkaç kez deploy edersiniz. Bir geliştirme ortamına deploy edersiniz. Bir test ortamına deploy edersiniz. Bir staging ortamına deploy edersiniz. Bir pre-production ortamına deploy edebilirsiniz. Bu dağıtımlar otomatik olduğu için üretime deploy ettiğinizde çalıştığını bilirsiniz. Bilgisayarlar tekrarlayan görevlerde gerçekten iyi olduklarından, çalışmaması alışılmadık bir durum olur.

Bu nedenle, insanların manuel adımlar yaptığı bir sürece dahil olmasını istemezsiniz. Dağıtımı otomatikleştirdiğinizde, kod her seferinde aynı şekilde üretime gidecektir.

İkinci kavram, dağıtımın aktivasyondan ayrıştırılmasıdır ( *deployment is decoupled from activation* ). Bu kulağa garip gelebilir, ancak *feature flag* denilen bir şeyle kodu deploy edebilirsiniz.  *Feature flag* ’ler yeniden deploy etmeye gerek kalmadan kodunuzu açıp kapatmanızı sağlar. Bir özelliği deploy edebilir, açabilir ve nasıl çalıştığını görebilirsiniz. Çalışmıyorsa kapatabilirsiniz.

Ya da hazır değilse, hazır olana kadar kapalı tutup sonra üretimde açabilirsiniz.  *Feature flag* ’ler, dağıtımı aktivasyondan ayrıştırmak için çok popüler hale gelmiştir.

Ayrıca *blue-green deploys* ve *canary testing* ile aktivasyonu dalgalar halinde yapabilirsiniz. Bu, yeni bir özelliği deploy ettiğiniz ama trafiğinizin yalnızca %10’unu ona yönlendirdiğiniz ve düzgün çalışıp çalışmadığını izlediğiniz bir yaklaşımdır. Ardından yeni sürüme yönlendirilen trafiğin yüzdesini kademeli olarak artırırsınız; düzgün çalıştığından memnun kalana kadar artırmaya devam eder ve sonunda trafiğin %100’ünü yönlendirirsiniz. Ya da düzgün çalışmıyorsa geri alırsınız ( *roll it back* ). Bu, hiçbir noktada sistemin kesintiye uğramadığı için “ *zero down-time* ” dağıtımı olarak da bilinir. Yani yeni kod deploy etmek için sistemi kapatmak zorunda kalmazsınız.

Son olarak, dağıtım “herkese uyan tek beden” ( *one size fits all* ) değildir. Ürettiğiniz ürün ve müşterinizin beklentileri için neyin çalıştığını görmeniz gerekir.  *Continuous delivery* ’yi iş senaryonuza uydurmak için benimsenebilecek birçok teknik vardır.

Bu videoda, *CI/CD pipeline* araçlarının dağıtımı otomatikleştirmek için bir yol sağladığını öğrendiniz.  *Release* , *deploy* ve *operate*  *continuous delivery* ’nin parçasıdır.  *Continuous delivery* ’nin beş temel ilkesi kalite, küçük partiler halinde çalışma, otomasyon, sürekli iyileştirme ve ortak sorumlulukla ilgilidir.  *Continuous deployment* , otomasyonun üretime dağıtım için kullanılmasıdır. DevOps, değişimden kaçınmak yerine değişim hızını artırarak riski yönetir.
