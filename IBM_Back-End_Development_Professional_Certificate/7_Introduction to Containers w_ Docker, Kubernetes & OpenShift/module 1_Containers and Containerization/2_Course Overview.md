# 📚 Kurs Genel Bakış

Merhaba ve bu kursa hoş geldiniz!

Bu kursta,  *Docker* , container registry’ler,  *Kubernetes* ,  *Red Hat* , *OpenShift* ve *Istio* gibi güncel konteynerleştirme araç ve teknolojilerini kullanarak *cloud-native* uygulamalar oluşturmayı öğreneceksiniz. Ayrıca uygulamalarınızı herhangi bir genel (public), özel (private) veya hibrit buluta nasıl dağıtıp ölçeklendirebileceğiniz konusunda da fikir edineceksiniz.

Bu kursta öğretilen beceriler; yazılım geliştirme, back-end ve full-stack geliştirme, bulut mimarisi, bulut sistem mühendisliği, *DevOps* uygulayıcılığı, site reliability engineer ( *SRE* ), bulut ağ uzmanlığı ve daha birçok rol için vazgeçilmezdir.

---

## ✅ Önkoşullar

Konteynerler hakkında önceden bilgi sahibi olmanız gerekmez. Bulut ve programlama kavramları hakkında temel bir anlayışa sahip olmanız ise tavsiye edilir.

---

## 🎯 Dersin Hedefleri

Bu kursu tamamladıktan sonra şunları yapabileceksiniz:

* Konteynerleri kullanabilecek ve uygulamaları herhangi bir ortama nasıl hızlı bir şekilde taşıyacağınızı biliyor olacaksınız.
* *Docker* ,  *Kubernetes* , *OpenShift* ve *Istio* kullanarak bulut-yerel ( *cloud-native* ) uygulamalar geliştirebileceksiniz.
* Yaşam döngüsü temelli, uçtan uca bir konteyner yönetim sistemi kurup kullanmak için *Kubernetes* mimarisini açıklayabilecek ve ondan yararlanabileceksiniz.
* Pod, servis ( *service* ), *ReplicaSet* ve diğer kaynakları deklaratif bir şekilde yapılandırmak ve oluşturmak için bir YAML deployment dosyası oluşturup ondan yararlanabileceksiniz.

Bu kurs beş modülden oluşur; bu modüller aşağıda listelenmiştir. Tüm modülleri beş hafta içinde başarıyla tamamlayabilmek için her hafta birkaç saatinizi ayırmanızı öneriyoruz. Düzenli ve tutarlı çalışmak, öğrenme hedeflerinize ulaşmanıza en iyi şekilde yardımcı olacaktır!

Tüm videoları izlemeniz, okumaları tamamlamanız ve bu bilgiyi tüm etkinlikleri yaparak pekiştirmeniz, bu kurstan en yüksek düzeyde fayda sağlamanızı sağlayacaktır.

---

## 🧱 Modül 1: Konteynerler ve Konteynerleştirme

İlk haftanıza, konteyner kavramlarını, özelliklerini, kullanım senaryolarını ve sağladıkları faydaları öğrenerek başlayacaksınız.

Konteynerler hakkındaki yeni bilginiz üzerine inşa ederek  *Docker* ’ın ne yaptığını öğrenecek ve  *Docker* ’ın neden geliştiriciler arasında kazanan bir teknoloji olduğunu keşfedeceksiniz.  *Docker* ’ın ne olduğunu öğrenecek, Docker süreçleriyle tanışacak ve Docker’ın altında yatan teknolojiyi keşfedeceksiniz.

Geliştiricilerin ve organizasyonların Docker kullanmaktan nasıl fayda sağlayabileceğini öğrenecek ve Docker kullanımının zorlayıcı olduğu durumların hangileri olduğunu göreceksiniz.

Ardından, bir `Dockerfile` kullanarak nasıl konteyner imajı oluşturacağınızı, bu imajı kullanarak çalışan bir konteyneri nasıl oluşturacağınızı öğrenecek, Docker komut satırı arayüzü ( *CLI* ) ile tanışacak ve sık kullanılan Docker komutlarını keşfedeceksiniz.

Docker nesneleri, `Dockerfile` komutları, konteyner imajı adlandırma kuralları hakkında bilgi sahibi olacak ve Docker’ın ağları, depolamayı ve eklentileri (plugins) nasıl kullandığını öğreneceksiniz.

Sonrasında, Docker mimarisi bileşenlerini çalışır hâlde gördüğünüzde bu bilgiyi pekiştirecek ve Docker kullanarak konteynerleştirmeyi inceleyeceksiniz.

Bu ilk haftanın sonunda, bir Docker Hub registry’sinden bir imaj çekeceksiniz. Bir imajı Docker kullanarak konteyner olarak çalıştıracak, bir `Dockerfile` kullanarak bir imaj oluşturup etiketleyecek ve bu imajı bir registry’ye göndereceksiniz.

---

## 🚀 Modül 2: Kubernetes Temelleri

Bu modülde, konteyner orkestrasyonunun ne olduğunu öğreneceksiniz. Ardından, geliştiricilerin konteyner orkestrasyonunu kullanarak karmaşık konteyner ortamlarının geliştirme yaşam döngülerini nasıl oluşturup yönettiklerini keşfedeceksiniz.

*Kubernetes* günümüzde en popüler konteyner orkestrasyon platformudur. Kontrol düzlemi bileşenleri ve denetleyiciler dâhil olmak üzere Kubernetes’in temel mimari bileşenlerini inceleyeceksiniz.

Kubernetes nesnelerini inceleyecek ve Pod’lar, ReplicaSet’ler ve Deployment’lar gibi belirli Kubernetes nesnelerinin nasıl çalıştığını öğreneceksiniz.

Daha sonra geliştiricilerin Kubernetes komut satırı arayüzü ( *CLI* ) olan `kubectl`’i kullanarak nesneleri nasıl yönettiklerini, bir Kubernetes kümesindeki iş yüklerini nasıl yönettiklerini ve temel `kubectl` komutlarını nasıl uyguladıklarını öğreneceksiniz.

İmperatif ve deklaratif komutlar kullanmanın avantajlarını ve dezavantajlarını ayırt edebileceksiniz.

Bu modülün sonunda, gerçek bir Kubernetes kümesinde kaynaklar oluşturmak için `kubectl` CLI komutlarını kullanacaksınız. Kubernetes CLI’yi kullanarak bir Kubernetes pod’u oluşturacak, bir Kubernetes deployment’ı oluşturacak, bir ReplicaSet oluşturacak ve Kubernetes yük dengelemesinin nasıl çalıştığını göreceksiniz.

---

## 🛠️ Modül 3: Kubernetes ile Uygulama Yönetimi

Modül 3’te ReplicaSet’leri, autoscaling, rolling updates, ConfigMap’ler, Secret’lar ve *service bindings* kavramını inceleyecek ve bu yetenekleri Kubernetes uygulamalarını yönetmek için nasıl kullanabileceğinizi öğreneceksiniz.

ReplicaSet’lerin artan talebi karşılamak için uygulamaları nasıl ölçeklendirdiğini ve autoscaling’in talebe dayalı dinamik ölçeklendirme oluşturduğunu öğreneceksiniz.

Rolling updates’i kullanarak uygulama güncellemelerini kullanıcı deneyimini kesintiye uğratmadan nasıl yayınlayıp geri alabileceğinizi göreceksiniz.

Ayrıca ConfigMap’ler ve Secret’ları kullanarak yapılandırma değişkenlerini ve hassas bilgileri deployment’larınıza nasıl sağlayabileceğinizi ve kodunuzu nasıl temiz tutabileceğinizi öğreneceksiniz.

Bu modülün sonunda, Kubernetes üzerinde dağıtılmış uygulamaları ölçeklendirip güncelleyeceksiniz.

---

## 🌐 Modül 4: Kubernetes Ekosistemi: OpenShift, Istio ve Diğerleri

Modül 4’te, büyüyen Kubernetes ekosistemi hakkında daha fazla bilgi edinecek ve cloud-native geliştirmeyi desteklemek için Kubernetes ile iyi çalışan ek araçları keşfedeceksiniz.

Red Hat® OpenShift® ile Kubernetes arasındaki benzerlikleri ve farklılıkları anlayacak ve OpenShift mimarisinin nasıl göründüğünü göreceksiniz.

OpenShift build’leri ve BuildConfig’leri ile OpenShift build stratejileri ve *triggers* hakkında bilgi edineceksiniz. Ayrıca operator’ların tüm uygulamaları ne kadar kolay bir şekilde dağıtabileceğini keşfedeceksiniz.

Son olarak, Istio service mesh’in bir uygulamanın servisleri arasındaki trafiği ve iletişimi nasıl yönettiğini ve güvence altına aldığını inceleyeceksiniz.

Bu modülün sonunda, bir OpenShift kümesi üzerinde komutlar çalıştırmak için `oc` CLI’yi kullanacaksınız. Ayrıca, bir Git deposunda saklanan kaynak koddan bir uygulamayı dağıtmak için OpenShift’in build yeteneklerini kullanacaksınız.

---

## 🧪 Modül 5: Final Ödevi

Final Projesi için, bu kursta öğrendiğiniz araç ve kavramları uygulamaya dökecek ve *Docker* ile *Kubernetes* kullanarak basit bir guestbook uygulaması dağıtacaksınız.

Tüm uygulama OpenShift üzerinde dağıtılacak ve yönetilecektir.

---

Bilginizi ve kariyerinizi ilerletmek için attığınız bu adımlar nedeniyle tebrikler! Yolculuğunuzun tadını çıkarın.
