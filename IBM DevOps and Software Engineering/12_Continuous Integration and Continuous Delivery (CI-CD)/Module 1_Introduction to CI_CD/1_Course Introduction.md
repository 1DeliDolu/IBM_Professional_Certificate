## 🎓 Course Introduction

Merhaba. Ben IBM Research’te Kıdemli Teknik Personel Üyesi ve DevOps Şampiyonu John Rofrano. Continuous Integration and Continuous Delivery’e, yani daha yaygın adıyla  **CI/CD** ’ye hoş geldiniz.

Bu kurs, tüm kod değişikliklerinizi **sürekli entegre etmek** ve bu değişiklikleri bir ortama **sürekli teslim etmek** için otomatikleştirilmiş hatlar (pipelines) oluşturmanız için ihtiyaç duyacağınız becerileri size kazandıracak. IBM’de bir yazılım mühendisi olarak her gün kullandığım iş akışlarını ve teknikleri öğretecek.

John Allspaw ve Paul Hammond 2009’daki Velocity konferansında, **“10+ Deploys per Day: Dev and Ops Cooperation at Flickr”** başlıklı artık ünlü olan konuşmalarını yaptıklarından beri, şirketler daha hızlı ve daha yüksek güvenilirlikle nasıl dağıtım yapacaklarını çözmeye çalışıyor. Bugün, değişiklikleri günde yüzlerce kez, sahip oldukları birçok  *Dev* , test ve üretim ortamından birine dağıtan şirketler var. Peki bunu nasıl yapıyorlar?

---

## 🧠 DevOps Zihniyeti ve Otomasyon

*DevOps* zihniyetini benimsediler. DevOps’un temel ilkelerinden biri de yazılım teslimatını  **otomatikleştirmektir** .

Ancak sayılar anlamsızdır. Amaç, **ihtiyaç hızında** dağıtım yapabilmektir. İşiniz için mantıklı olduğu kadar sık dağıtım yapabilmelisiniz. Fakat bu dağıtımın **güvenilir** ve **tekrarlanabilir** olması gerekir; bunun için de otomasyon şarttır. İşte burada **CI/CD** devreye girer.

Başlangıçta bunaltıcı görünebilir ama eski bir sözün dediği gibi: **“Bir fili nasıl yersin? Bir seferde bir lokma.”** Bu kurs, bir CI/CD hattı kurma gibi göz korkutucu görünen görevi, tüketilebilir “lokmalık” parçalara bölecek ve sizi adım adım ilerletecek.

---

## ⏱️ CI/CD ve Ortalama Liderlik Süresi

CI/CD, **ortalama liderlik süresi (mean lead time)** ile ilgilidir; yani fikirden üretime gitmenin ne kadar sürdüğü.

Bu ortalama liderlik süresi, **yayın sıklığı (release frequency)** tarafından sınırlandırılır; yani bir değişikliği ne kadar sık teslim edebildiğiniz.

---

## 🔁 Continuous Integration (CI)

Önce **continuous integration (CI)** ile başlayacağız. Bu, her geliştirici değişikliğinin bir dizi testten geçtikten sonra ana dala ( *main branch* ) **sürekli entegre edilmesi** sürecidir ve sonuçta **dağıtıma hazır olabilecek** bir kod ortaya çıkar.

Şunları öğreneceksiniz:

* **Sosyal kodlama (social coding)** faydaları
* **Git feature branch** iş akışını nasıl kullanacağınız
* Popüler bazı **CI araçlarına** genel bakış
* Ardından **GitHub Actions** kullanarak CI hattınızı nasıl oluşturacağınız (derinlemesine)

---

## 🚀 Continuous Delivery (CD)

Sonra **continuous delivery (CD)** bölümüne geçeceğiz. CD, her değişikliği üretime benzer bir ortama teslim ederek, kodun herhangi bir zamanda **hızlı ve güvenli** biçimde üretime dağıtılabilmesini sağlamayı hedefleyen bir yazılım geliştirme disiplinidir.

Bu,  **main branch** ’inizin her zaman dağıtıma hazır olması gerektiği anlamına gelir.

CD modülünde:

* CD’nin faydalarını öğrenecek,
* Popüler bazı **CD araçlarına** genel bakış alacak,
* Ardından **Tekton** adlı bir teknolojiyle, bir hattı görev görev inşa etmeyi derinlemesine öğreneceksiniz.

Tekton ile dağıtımlarınızı **Kubernetes kümeniz içinde** otomatikleştirebilirsiniz. Laboratuvarlarda, hattınızı **OpenShift** üzerine dağıtacaksınız.

---

## 🧩 OpenShift ile DevOps ve GitOps

Ardından **DevOps and GitOps with OpenShift** modülünde, **OpenShift Pipeline** özelliğini öğrenecek ve kullanacaksınız.

Bu özellik, OpenShift geliştirici perspektifinden CI/CD iş akışlarınızı tanımlamak ve yönetmek için sezgisel bir kullanıcı arayüzü sunar. Bu özelliği kullanarak, tek bir satır kod yazmadan gerçek dünyaya yönelik hatlar yazmayı öğreneceksiniz.

OpenShift pipeline, sağlanan tuval (canvas) üzerinden görevler ve hatlar oluştururken, arka planda **Tekton kodunu otomatik olarak** üretip bu süreci basitleştirir.

Son olarak, bir laboratuvarda, daha önce Tekton ile oluşturduğunuz hattı, yalnızca **OpenShift pipeline kullanıcı arayüzünü** kullanarak yeniden inşa ederek bilginizi uygulamaya dökeceksiniz.

---

## 🤝 Kapanış

Yazılım teslimat pratiğinizi otomatikleştirmeyi ve her dağıtım yaptığınızda kodunuzu **tekrarlanabilir** ve **yeniden üretilebilir** biçimde teslim etmeyi öğrenmek için bana katılın.

Videoları izleyin, laboratuvarlara kendinizi verin, quizleri çözün ve forumlarda akranlarınızla etkileşime geçin; çünkü yazılım mühendisliği bir takım sporudur ve iş birliği teşvik edilir.

Sınıfta görüşürüz.
