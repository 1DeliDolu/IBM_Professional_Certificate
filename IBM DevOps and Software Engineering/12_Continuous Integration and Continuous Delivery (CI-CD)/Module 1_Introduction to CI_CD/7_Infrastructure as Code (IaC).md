# 🧱 Infrastructure as Code (IaC)

Infrastructure as Code’a hoş geldiniz. Bu videoyu izledikten sonra şunları yapabileceksiniz:  *Infrastructure as Code’un ne olduğunu açıklamak* , *IaC’nin faydalarını tanımlamak* ve  *IaC’nin çeşitli araçlarını açıklamak* .

![1766088437777](image/7_InfrastructureasCode(IaC)/1766088437777.png)

Infrastructure as Code, yani *IaC* ile ne demek istediğimizi konuşalım. IaC, altyapınızı metinsel bir formatta tanımlamanız için harika bir yol sunar. Ancak bir kelime işlemci belgesinden bahsetmiyorum. Sistemlerinizi tıpkı kod gibi yapılandırmak için gerçekten kullanabileceğiniz metinsel bir dosya formatından söz ediyoruz. Bir IaC aracına verebileceğiniz metinsel bir koddan bahsediyoruz.

![1766088464000](image/7_InfrastructureasCode(IaC)/1766088464000.png)

Ve bu araç kodu okur; ardından sunucularınızı, ağlarınızı, depolama alanlarınızı vb. — yani ihtiyacınız olan temel altyapı öğelerini — oluşturur. Bu araçları bu metinsel kodla kullanmak, herkesin her seferinde aynı ortamı elde etmesi anlamına gelir; yani ortam *tutarlı* ve *tekrarlanabilir* olur.

Metinsel kod genellikle *YAML* formatında yazılır; bu, IaC yazmak ve bildirmek için çok yaygın bir yöntemdir.

---

## 🎯 Neden Bu Derste IaC’yi Tartışıyoruz?

Peki bu derste neden Infrastructure as Code’u tartışıyoruz? Çünkü bu sistem yapılandırmalarını manuel olarak yapmak hataya açıktır ve zaman alıcıdır. İhtiyaçlarınıza göre sistemi nasıl kuracağınızı ve yapılandıracağınızı; ne kadar depolama istediğinizi, ne kadar işlem gücü istediğinizi vb. tanımlamak için şablonlar veya komutlar kullanabilirsiniz.

DevOps’un ilk günlerinde, *Configuration Management Systems* (ya da  *CMS’ler* ) bunu mümkün kıldı ve daha yeni IaC araçlarından önce vardı; yani bu tür işleri yapmak için elinizde olan tek şey onlardı.

CMS’leri daha sonra daha ayrıntılı olarak tartışacağız.

Tekrarlanabilir yapılandırma sayesinde aynı platformu tekrar tekrar hızlıca sağlayabilir ve her seferinde aynı durumda olacağından emin olabilirsiniz.

![1766088530890](image/7_InfrastructureasCode(IaC)/1766088530890.png)

---

## 🧩 IaC Yaklaşımları: Declarative ve Imperative

Infrastructure as code araçları *declarative* veya *imperative* olabilir.

*Declarative* yaklaşımda, sağlamak istediğiniz altyapı kaynaklarının istenen durumunu belirtirsiniz ve ardından IaC aracı bu duruma nasıl ulaşacağını belirler. Bağımlılıkları yönetir ve komutları doğru sırada çalıştırır; yürütme sırasını sizin belirtmenize gerek kalmaz.

Bu yaklaşımı kullanan araçlar arasında Terraform, Puppet, SaltStack, CloudFormation ve bir ölçüde Ansible yer alır.

*Imperative* yaklaşım ise, istenen duruma ulaşmak için gereken komutların belirli sırasını tanımlamanızı gerektirir. Bağımlılıkları doğru kurgulamak size kalır; çünkü araç komutları sizin belirttiğiniz sırayla çalıştırır.

Chef gibi araçlar  *imperative* ’tir ve bir ölçüde Ansible da bu şekilde kullanılabilir.

![1766088579817](image/7_InfrastructureasCode(IaC)/1766088579817.png)

---

## 🧰 Ansible ile IaC Örneği: Inventory, VAR ve Playbook’lar

Ansible’ın bir IaC aracı olarak nasıl çalıştığını görmek için *inventory* dosyalarını ve *VAR* dosyalarını nasıl kullandığına bakalım. Burada Ansible playbook’larını açıklayıcı bir örnek olarak kullanıyoruz; ancak süreç temelde diğer IaC araçlarıyla da aynıdır.

Chef’in  *cookbook* ’ları ve  *recipe* ’leri vardır; Ansible’ın ise  *Playbook* ’ları ve  *Play* ’leri vardır. Temelde aynı şeydirler.

*Inventory* dosyaları; IP adresleri veya host adları biçiminde olabilecek sunucu ya da cihaz listesini içerir. Ayrıca tüm web sunucuları ya da tüm veritabanı sunucuları gibi sunucu gruplamalarını da belirtebilirler. Ansible’ın ne üzerinde çalışacağını bilme şekli budur.

Ayrıca, bir playbook bir cihazda veya cihaz grubunda çalıştırıldığında gerekli olabilecek ilgili değişkenleri içeren *VAR* dosyaları vardır. Değişkenleri nasıl tanımladığınıza bağlı olarak Ansible’ın uzak hostlar veya cihazlarla nasıl etkileşime gireceğini kontrol edebilirsiniz.

Inventory dosyaları, Ansible mimarisinin en temel yapı taşını oluşturur. Ansible’ı veya Ansible playbook’larını çalıştırırken inventory dosyalarına referans vermeniz gerekir.

![1766088646667](image/7_InfrastructureasCode(IaC)/1766088646667.png)

---

## 📚 Playbook, Play ve Hedefleme Mantığı

Ansible’da, herhangi bir sayıda *play* içerebilen bir *playbook* kavramı vardır.

 *Play* ’ler, her sunucu veya cihaz üzerinde gerçekleştirilecek talimatları içerir. Play’ler ayrıca tüm web sunucuları veya tüm veritabanı sunucuları gibi belirli sunucu gruplarına hedeflenebilir.

Dolayısıyla bir playbook; Ansible’a yürütmesi için verdiğiniz talimatlar olan yeniden kullanılabilir play’lerin bir koleksiyonudur. Ansible playbook’u okur, inventory’deki hangi sunucuların play’lere uygun olduğunu belirler ve play’leri bu sunucuların her birinde çalıştırır.

Bir web sunucusu, bir uygulama sunucusu, bir veritabanı sunucusu kurmanız gerekebilir; ya da belki iki web sunucusu ve üç uygulama sunucusu; ya da hatta bir sunucunun mevcut yapılandırmasını değiştirmeniz gerekebilir. Ne yapmasını isterseniz, Ansible gerekli tüm yapılandırma değişikliklerini yapacak ve altyapınız için ihtiyaç duyduğunuz her şeyi sağlayacaktır.

Ayrıca Ansible’ın *idempotent* olduğunu belirtmek önemlidir. Sunucu zaten istenen durumdaysa onu etkilemez. Bu, bir playbook’u yeniden uygulayabilmenizi ve aynı şeyleri iki kez kurmasından endişe etmemenizi sağlar. Gerekli değilse Ansible bunu yapmamaya dikkat eder.

![1766088685121](image/7_InfrastructureasCode(IaC)/1766088685121.png)

---

## 🚀 IaC’nin Faydaları

Peki IaC’nin faydaları nelerdir?

IaC otomasyonu, geliştirme, test ve üretim için altyapı sağlama sürecini dramatik biçimde hızlandırır (ve üretim altyapısını gerektiğinde ölçeklemek veya kapatmak için de). Hatta, aksi halde bir ticket açmanız ve birinin manuel olarak yapmasını beklemeniz gibi zaman alan süreçlerle yönetilebilecek eski altyapının sağlanmasını bile otomatikleştirebilir.

Geliştiriciler hızlıca sandbox’lar ve *Continuous Integration/Continuous Delivery* ortamları sağlayabilir; QA ise yüksek doğrulukta test ortamlarını hızlıca sağlayabilir.

IaC, sağlama bilgisinin her zaman organizasyonla birlikte kalmasını sağlar. Geçmişte, sunucuların nasıl yapılandırılacağı bilgisi organizasyonunuzda yalnızca birkaç kişi tarafından biliniyor olabilirdi. Bu bilgiyi infrastructure as code kullanarak kodlaştırdığınızda, herkes ihtiyaç duyduğu şeyi sağlayabilir ve personel değişimiyle oluşabilecek “tribal knowledge” kaybı korkusu artık sorun olmaktan çıkar.

Son olarak, IaC organizasyonların bulut bilişimin tüketim bazlı maliyet yapısından maksimum faydayı sağlamasına olanak tanır. Altyapıyı sağlamak ve ölçeklemek için gereken zaman, emek ve uzmanlaşmış beceriyi azaltır. Ayrıca geliştiricilerin altyapı tesisatıyla daha az vakit geçirip iş açısından kritik yazılım çözümlerine daha çok odaklanmasını sağlar.

![1766088794384](image/7_InfrastructureasCode(IaC)/1766088794384.png)

---

## 🛠️ Başlıca IaC Araçları

Şimdi, mevcut başlıca IaC araçlarından bazılarını kısaca tartışalım.

 *Terraform* , Hashi Corp’un ücretsiz ve açık kaynaklı bir IaC aracıdır. IaC’ye *declarative* yaklaşımı uygular ve yapacağı işin beklediğiniz şekilde olmasını sağlamak için çalıştırma öncesi bir kontrol içerir. Terraform’u Ansible ile birlikte temel bir araç olarak kullanabilirsiniz; Terraform temel altyapıyı sağlar, Ansible ise bunun üzerine yazılımı yapılandırır. Bulut sağlama için çok popüler bir araçtır.

 *Ansible* , intra-service orkestrasyonu, uygulama dağıtımı, bulut sağlama ve daha fazlası gibi IT görevlerini otomatikleştiren açık kaynaklı bir araçtır. Ulaşmak istediğiniz durumu tanımlamak için tanıdık YAML dosyalarını kullanır. Ansible kurulumu basittir; çünkü istemci tarafında agent veya özel güvenlik altyapısı gerektirmez ve modülleri istemcilere ileterek çalışır. Bu, onu Internet of Things cihazlarını yapılandırmak gibi bellek kısıtlı ortamlar için ideal hale getirir. Bu modüller istemci tarafında çalıştırılır ve sonuçlar Ansible sunucusuna geri gönderilir.

 *Chef* , durumun kendisini tanımlamak yerine nihai duruma ulaşmak için gerekli adımları tanımlar. “Cookbook”lar kullanarak bir sistemi istenen duruma ulaştıracak çeşitli süreçleri tanımlayabilirsiniz. Chef’in güçlü yanlarından biri popüler olması ve geniş desteğe sahip olmasıdır; ancak dezavantajlarından biri cookbook’ların Ruby ile yazılmasıdır, yani ekibinizde Ruby becerilerine ihtiyaç duyarsınız.

*Puppet* ile mevcut herhangi bir platformu kullanabilirsiniz. Puppet ile Chef arasındaki temel fark, Puppet’ın *declarative* olmasıdır; bazıları bunu tercih edilen bir yöntem olarak görür.

 *SaltStack* ’in uzaktan yürütme yetenekleri, yöneticilerin esnek bir hedefleme sistemiyle çeşitli makinelerde paralel olarak komut çalıştırmasına olanak tanır. SaltStack, kullanıcıların birden fazla makineyi açıkça hedefleyip doğrudan komutlar çalıştırmasına izin verecek şekilde tasarlanmıştır.

![1766088902948](image/7_InfrastructureasCode(IaC)/1766088902948.png)

---

## ✅ Özet

Bu videoda şunları öğrendiniz: Configuration Management Systems, IaC araçları kullanılabilir hale gelmeden önce altyapı sistemlerini yapılandırmak için gerçekten mevcut olan tek araçlardı; IaC araçları geliştirme ortamınızın altyapısını sağlama sürecini dramatik biçimde hızlandırabilir; ve farklı türlerde çeşitli IaC araçları vardır.

![1766088921184](image/7_InfrastructureasCode(IaC)/1766088921184.png)
