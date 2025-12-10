# 🚀 Red Hat OpenShift Özeti

## 🎬 Giriş

“Red Hat OpenShift Recap”e hoş geldiniz.

## 🎯 Öğrenme Hedefleri

Bu videoyu izledikten sonra şunları yapabileceksiniz:

* Red Hat OpenShift'in ne olduğunu açıklamak
* OpenShift ve Kubernetes arasındaki ilişkiyi açıklamak
* OpenShift'in, operasyon ve geliştirme görevlerini kolaylaştırmak için sağladığı hizmetleri tanımlamak

---

## 📚 OpenShift'in Tanımı ve Hibrit Bulut

Red Hat web sitesinde verilen özlü OpenShift tanımı, OpenShift'in hibrit bulut, kurumsal bir *Kubernetes* uygulama platformu olduğunu söyler.

 *Hibrit bulut* , iş yükü taşınabilirliğini, orkestrasyonunu ve yönetimini yerinde (on-premises) ve bulut ortamları arasında bir araya getiren bir BT mimarisidir.

OpenShift'i hem kurum içi ortamlarda hem de bulut ortamlarında çalıştırabilirsiniz.

OpenShift, bir uygulama platformu oluşturmak için açık kaynaklı  *Kubernetes* 'in üzerine inşa edilir. Bir uygulama platformu olarak OpenShift, konteynerleri orkestre etmekten daha fazlasını yapar.

OpenShift ayrıca, uygulamaların oluşturulmasından ve  *CI/CD* 'den izleme ve günlüklemeye kadar tüm yaşam döngüsü etrafında ek araçlar sağlar. Elbette OpenShift'in Red Hat tarafından geliştirildiğini ve desteklendiğini de belirtmeliyiz.

---

## 🧩 Mikroservisler ve Sunucusuz Mimariler için OpenShift

OpenShift, mikroservisleri çalıştırmak için bir platformdur. OpenShift, bulut-yerel hizmetleri otomatik bir şekilde dağıtmak için özel olarak tasarlanmıştır.

 *Sunucusuz mimariler* , sanal makineler ve konteynerler gibi diğer hesaplama biçimleriyle çoğu zaman birlikte çalışır. OpenShift, konteynerleştirilmiş iş yüklerini orkestre eder ve böylece bulut-yerel bir uygulama için mükemmel bir model sağlar.

Sunucusuz yaklaşımlar, kuruluşunuzun ihtiyaçlarını daha iyi karşıladığında OpenShift'i sunucusuz teknolojilerle entegre edebilirsiniz.

---

## 🧬 Kubernetes ve OpenShift İlişkisi

Kubernetes ve OpenShift yakından ilişkilidir. Kubernetes ile OpenShift arasındaki ilişkiyi aktarmak için sıklıkla *Linux çekirdeği* benzetmesi kullanılır.

Çekirdek, bir işletim sisteminin merkezinde yer alan güçlü bir programdır. Linux çekirdeği temel ve yetkin olsa da, Ubuntu, Fedora ve Debian gibi birçok Linux dağıtımı bu çekirdeğin üzerine inşa edilir.

Bu dağıtımlar, Linux çekirdeğini kendi çekirdekleri olarak kullanan ve ek özellikler ile işlevler sunan işletim sistemleridir. Tıpkı Linux'un Fedora dağıtımı gibi, OpenShift de temel yeteneklerinin üzerine inşa edilen bir *Kubernetes* dağıtımıdır.

---

## 🏗️ OpenShift Mimarisi ve Hizmet Katmanları

OpenShift web sitesinden alınan bir diyagramı kullanarak OpenShift ile nelerin geldiğine bakalım.

Öncelikle, bir OpenShift ortamında Kubernetes ana düğümü Red Hat Enterprise Linux CoreOS üzerinde çalışırken, işçi düğümler Red Hat Enterprise Linux'u destekler.

Sonraki adım Kubernetes'tir. Daha önce de belirttiğimiz gibi, Kubernetes OpenShift'in ayrılmaz bir parçasıdır, sunumun bir bölümüdür. Buraya kadar OpenShift mimarisi Kubernetes'e benzer.

OpenShift altyapısı, üzerine Kubernetes'in dağıtıldığı bir yapıyı içerir. Sonrasında *küme hizmetleri* gelir. Küme hizmetleri; tümleşik izleme, küme içinde dağıtılmış özel bir kayıt defteri, ağ çözümleri ve kullanıcıya yararlı ve sezgisel bir deneyim sunmak üzere tasarlanmış daha birçok özelliği içerir.

Küme hizmetlerinin üzerinde, *platform hizmetleri* kullanıcıların iş yüklerini yönetmesine yardımcı olur. *Uygulama hizmetleri* kullanıcıların bulut-yerel uygulamalar inşa etmesine yardımcı olurken, *geliştirici hizmetleri* geliştirici üretkenliğini artırmaya yardımcı olur.

---

## ✅ Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* Red Hat OpenShift, mikroservisler gibi konteynerleştirilmiş iş yüklerini çalıştırmak için bir platformdur.
* OpenShift, Kubernetes'in üzerine ek yetenekler inşa etmesi bakımından bir *Kubernetes* dağıtımına benzer.
* OpenShift, iş yüklerini yönetmek, bulut-yerel uygulamalar inşa etmek ve geliştirici üretkenliğini artırmak için çeşitli hizmetler sağlar.
