
# 🚀 OpenShift ile Mikroservisler

## 👋 OpenShift ile Mikroservislere Hoş Geldiniz

OpenShift ile Mikroservisler'e hoş geldiniz. Bu videoyu izledikten sonra, OpenShift'in geliştiricilerin hayatını nasıl kolaylaştırdığını açıklayabilecek, mikroservislerin OpenShift üzerinde hangi süreçle dağıtıldığını açıklayabileceksiniz.

Mikroservislerin OpenShift ile nasıl dağıtılacağını anlatan IBM Cloud ekibinden Si Vennam'ı izleyeceksiniz. Geliştiricilerle başlayacağız. Yani, buraya bir geliştirici çizeceğiz.

Peki, bir geliştiricinin ne yapması gerekir? Genellikle uygulamalar yazmak, değişiklikler yapmak, bunları test etmek, bir kümeye dağıtmak zorundadırlar ve gerçekten de buna odaklanırlar; bunun dışında kalan her türlü dikkat dağıtıcı unsur, bu görevlerini yavaşlatacaktır.

---

## 👨‍💻 OpenShift ile Çalışmaya Başlayan Geliştirici

Dolayısıyla geliştirici açısından, OpenShift ile çalışmaya başlarken yapmak isteyecekleri ilk şey bir proje ve bir uygulama oluşturmaktır.

Bunu yapmak için OpenShift, geliştiricilerin platformla çalışmasını sağlayan iki farklı yol sunar. Bunlardan biri  *CLI* 'dan yararlanmaktır ve ayrıca üzerinde çalışabilecekleri gerçekten güçlü bir web konsolu da vardır.

Yani geliştiricinin yapmak istediği ilk şey, bu iki form faktöründen birini kullanarak bir proje ve uygulama oluşturmaktır. Ve geliştiricinin çalışmak istediği her türlü kaynak kodu ve programlama dili için şablonlar mevcuttur.

Dolayısıyla bunu yapacaklar ve sonra, uygulamaya güncellemeler yapma akışına girdiklerinde, atmak isteyecekleri ilk adım değişiklikleri bir depoya ( *repository* ) *push* etmektir. Bu durumda örnek olarak  *GitHub* 'ı kullanalım.

---

## 🧱 GitHub Deposu ile Çalışma Akışı

Diyelim ki bu geliştirici GitHub üzerinde değişiklikler yapıyor. Aslında yapmaları gereken tek şey budur.

Perde arkasında, geri kalan her şeyle *OpenShift* ilgilenecektir. Bu uygulama ve proje oluşturulduğunda, OpenShift arka planda bu uygulamanın dağıtımını sağlayan bir  *Jenkins job* 'ı ve  *pipeline* 'ı oluşturacaktır.

Dolayısıyla kod GitHub'a *push* edildiğinde, bir *web hook* tetiklenecek ve bu da bir  *Jenkins job* 'ını başlatacaktır. Bu da aslında sadece iki şey yapacaktır:

İlk olarak, *source to image* denilen bir işlemi gerçekleştirecek ve bu işlem, o kaynak koddan bir *Docker image* oluşturacaktır. Sonrasında ise bunu alıp bir  *registry* 'ye koyacaktır.

---

## 📦 Registry ve OpenShift Kümesine Dağıtım

OpenShift ile birlikte yerleşik gelen özel bir *registry* söz konusudur ve aslında bunun dışında, bu bağlamın dışında sahip olduğunuz kendi  *registry* 'nizi ya da genel ( *public* )  *registry* 'leri de kullanabilirsiniz.

Bu imaj oluşturulup o  *registry* 'ye *push* edildikten sonra, OpenShift'in bir sonraki yapacağı şey bu imajı gerçek kümeye ( *cluster* ) *push* etmektir. Ve burada sahip olduğumuz şey, OpenShift içindeki kümemizde bulunan iki *host*tur.

Bu imajı alacağız ve bunu iki kez dağıtacak şekilde yapılandırdığımızı varsayalım. Ve buna uygulamanın v1'i diyeceğiz.

---

## 🔁 Image Streams ve Kesintisiz Güncelleme Süreci

Şimdi bu süreci bir kez daha üstünkörü gözden geçirelim. Yani geliştirici kodda bazı değişiklikler yapar, ardından *Jenkins* bu  *build* 'i başlatır, bir imaj oluşturur, bu imajı bir  *registry* 'ye *push* eder ve sonra burada biraz farklı bir şey devreye girer.

Bu adımda OpenShift, *image streams* denilen bir şeyden yararlanır; bu, Kubernetes'in işleri yapma biçiminden biraz farklıdır ve temelde sağladığı şey, bu imajla ilgili bir değişiklik algılandığında bir  *image stream* 'in bunları uygulamalarınıza kesinti süresi olmadan *push* etmenize olanak tanımasıdır.

Yani yapacağı şey, bildiğiniz gibi, bu kodun yeni sürümüyle eski sürümü kapatmak, yeni sürümü başlatmak ve uygulamanın yeni sürümünü tamamen yayına alana kadar bunu sürdürmektir.

Bu, OpenShift'in geliştiricilerin hayatını kolaylaştırdığı yollardan sadece birkaçıdır. Bu videoda, OpenShift'in mikroservisleri otomatik olarak konteynerlara *build* etmek için bir *Jenkins job* oluşturduğunu, OpenShift'in oluşturulan konteynerları bir  *registry* 'ye *push* ettiğini ve bu konteynerları kümeye ( *cluster* ) dağıttığını öğrendiniz.
