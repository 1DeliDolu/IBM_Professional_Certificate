# 🔄 Continuous Integration

Bu videoyu izledikten sonra, *Continuous Integration* ve *Continuous Delivery* kavramlarını açıklayabilecek,  *Continuous Integration* ’da küçük partiler ( *small batches* ) kullanmanın nedenini anlatabilecek ve  *Continuous Integration* ’ın faydalarını tanımlayabileceksiniz.

İnsanlar *CI/CD* kısaltmasını tek bir şeymiş gibi kullanır, ancak *Continuous Integration* ve *Continuous Delivery* iki ayrı ve farklı uygulamadır.

 *Continuous Integration (CI)* , her geliştirici değişikliğini bir dizi testten geçtikten sonra sürekli olarak  **build etmek** , **test etmek** ve  **master branch** ’e **entegre etmek** sürecidir. Sonuç, potansiyel olarak deploy edilebilir koddur.

*Continuous Delivery (CD)* ise, her değişikliği production benzeri bir ortama teslim ederek kodun production’a hızlı ve güvenli şekilde dağıtılabilmesini sağlamaya yönelik bir dizi uygulamadır. Dikkat edin, “production benzeri” dedim. Production’a deploy edilmesi gerekmez ve hatta birçok kişi production’a sürekli deploy ettiğiniz durumu “ *Continuous Deployment* ” terimine ayırır. *Continuous Delivery* için, development, test, staging gibi production ortamını taklit eden bir yere deploy etmeniz yeterlidir.

Örneğin, production ortamı Kubernetes üzerinde çalışan container’lardan oluşuyorsa, development ortamına da Kubernetes üzerinde container’lar şeklinde deploy etmelisiniz.

---

## 🧱 Geleneksel Geliştirme Yaklaşımı

Geleneksel geliştirmede geliştiriciler uzun ömürlü ( *long-lived* ) development branch’lerinde çalışır. Genellikle bunu böyle yaparlar çünkü eski sürüm kontrol sistemleri bir branch oluşturduğunuzda kodun tamamının bir kopyasını çıkarırdı, bu yüzden branch oluşturmak çok pahalıydı. Bu maliyet insanların branch açmaya direnmesine yol açar ve branch açtıklarında da çok sık silmezler.

Ancak Git gibi modern sürüm kontrol sistemleriyle artık durum böyle değildir. Yine de bazı geliştirme ekipleri geleneksel uygulamayı sürdürmektedir.

Bu development branch’leri release branch’lerinden ayrı tutulur ve periyodik olarak bir release branch’ine merge edilir, fakat bu süreç genellikle çok fazla bozulma olmadan gerçekleşmez. Bunun nedeni, uzun bir zaman diliminde yapılan değişiklik miktarının branch’i merge conflict’lere daha açık hale getirmesidir.

Build’ler periyodik olarak, bazen nightly şekilde, release candidate branch’inde çalıştırılır. Bu sırada geliştiriciler development branch’ine eklemeye devam eder ve bu branch master release branch’inden giderek daha fazla uzaklaşır. Bu senaryoda, kodu tekrar çalışır hale getirmek için merge işlemi günler sürebilir.

---

## ⚙️ Continuous Integration Nasıl Çalışır?

Buna karşılık  *Continuous Integration* , geliştiricilerin kodu paylaşılan bir repository’ye sık sık entegre etmesini gerektiren bir geliştirme pratiğidir ve “sık sık” derken mümkünse günlük ( *daily* ) demek istiyorum.

Bu, geliştiricilerin kısa ömürlü ( *short-lived* ) feature branch’lerinde çalışması ve feature tamamlandığında master’a merge etmesiyle gerçekleştirilir.

Bu, her feature tamamlandığında entegre ettiğiniz anlamına gelir. Uzun bir feature listesinin tamamlanmasını bekleyip sonra entegre etmezsiniz.

Her check-in daha sonra otomatik test ve otomatik build ile doğrulanır; bu da ekiplerin sorunları erken ve sık tespit etmesini sağlar. Merge’den sonra branch silinir ve yeni feature için yeni bir branch oluşturulur.

---

## 📦 Küçük Partilerle Çalışmanın Önemi

Küçük partilerle çalışmak  *Continuous Integration* ’ı gerçekleştirmeye yardımcı olur.

Düzenli commit atarak, her geliştirici merge’ler arasındaki süre daha kısa olduğu için çakışan değişikliklerin sayısını azaltabilir. Ne kadar çok zaman geçerse, merge conflict riski o kadar artar.

Kod üzerinde bir hafta çalışıp hepsini tek seferde check-in yapmak, yeni feature’ların diğer feature’larla çakışma riskini artırır.

Bu çakışmalar çözmesi zor ve zaman alıcı olabilir.

---

## 🔍 Pull Request ve Code Review

*Pull request* kullanmak, takım üyelerinin yaptıkları değişiklik hakkında iletişim kurmasını sağlar. Her pull request bir code review fırsatıdır; böylece diğer geliştiriciler kodu inceler.

Bu, tüm kodun birden fazla kişi tarafından görülmesini sağlar ve bir şeylerin ters gitme riskini azaltır.

En az günde bir kez veya her feature build’inde bir kez tüm değişiklikleri commit etmek, genellikle *Continuous Integration* tanımının bir parçası olarak kabul edilir.

Pull request’lerden bahsetmişken, her pull request build edilmeli ve test edilmelidir. Bu otomatik olarak gerçekleşmelidir. Sistem, entegrasyonun doğru çalıştığını doğrulamak için mevcut çalışma sürümünün değişikliklerini build etmelidir.

---

## 🛠️ CI Araçları ve Otomasyon

Yaygın bir uygulama, otomasyon kullanmaktır; burada bir CI aracı sürüm kontrol sistemini izler ve build’i otomatik olarak çalıştırır.

Travis CI, Circle CI, Jenkins, GitHub Actions gibi çoğu CI aracı, sürüm kontrol sisteminizi değişiklikler için izleme ve build sürecini otomatikleştirme yeteneğine sahiptir.

Kod build edildikten sonra, tüm testler kodun geliştiricinin beklediği şekilde davrandığını doğrulamak için çalıştırılmalıdır. Başka bir deyişle, build’i kendi kendini test eden ( *self-testing* ) hale getirin.

Test sonuçları pull request’e geri beslenmelidir ve failing test’leri olan bir pull request’i asla merge etmemelisiniz.

---

## ✅ Continuous Integration’ın Faydaları

*Continuous Integration* uygulamasının faydalarından biri, değişikliklere daha hızlı tepki verebilmeniz ve daha hızlı hareket edebilmenizdir.

Daha hızlı hareket edebilirsiniz çünkü testleriniz otomatikleştirilmiştir.

Testler otomatik olduğu için, o ana kadar yaptığınız her şeyin test edildiğini ve çalıştığının bilindiğini bilirsiniz. Bu testleri otomatik çalıştırırsanız, zamanınızı test etmeye harcamazsınız; zamanınızı feature geliştirmeye harcarsınız.

 *CI* , kod entegrasyon riskini azaltır çünkü daha küçük değişiklikleri entegre edersiniz. Değişiklikler daha küçük olduğunda, değişiklik kaynaklı bozulma riski de daha düşüktür.

Pull request göndermek kod üzerinde daha fazla göz olmasını sağlar ve bu da daha yüksek kod kalitesiyle sonuçlanır. Herkes kodun kalitesi üzerinde söz sahibidir.

Son olarak, sürüm kontrolünde bulunan kodun çalıştığını bilirsiniz. Unutmayın, master branch her zaman deploy edilebilir olmalıdır.

---

## 🧪 Testi Sonradan Yazma Yanılgısı

Öğrencilerimin bana sorduğu bir soru şudur: “Kullanıcı arayüzünü yaptıktan sonra test case yazabilir miyim?”

Ben de onlara bunun o noktada çok geç olduğunu söylerim.

Kullanıcı arayüzünü master branch’e commit etmişsinizdir ve master branch’i deploy etmemiz gerekirse, kullanıcı arayüzünün çalışıp çalışmadığı hakkında hiçbir fikrimiz yoktur.

Test edilmemiş kodun çalışmadığını varsaymalısınız.

Test edilmemiş kodu asla master branch’e merge etmemelisiniz.

Master branch her zaman deploy edilebilir olmalıdır.

---

## 🧾 Video Özeti

Bu videoda,  *Continuous Integration* ’ın testler geçtikten sonra her değişikliği master branch’e build etmek, test etmek ve entegre etmek olduğunu öğrendiniz.

 *Continuous Delivery* , her değişikliği production benzeri bir ortama teslim ederek kodun production’a hızlı ve güvenli şekilde deploy edilebilmesini sağlar.

Küçük partilerle çalışmak, çakışan değişikliklerin sayısını azaltarak  *Continuous Integration* ’a yardımcı olur.

 *Continuous Integration* ’ın faydaları arasında daha hızlı tepki süresi, daha hızlı hareket etme ve kod entegrasyon riskini azaltma yer alır.
