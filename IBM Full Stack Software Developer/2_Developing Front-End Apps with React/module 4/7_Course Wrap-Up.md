## 🎓 Course Wrap-Up

Bu kursu tamamladığınız için tebrikler. Artık JavaScript React kütüphanesini kullanmanın temel kavramlarını bildiğinize göre, öğrenmeye devam etmek ve becerilerinizi uygulamak için pek çok fırsat bulacaksınız. Bunları tartışmadan önce, kurs boyunca öğrendiklerinizin bazı temel yönlerini gözden geçirelim.

## 🧩 React Bileşenleri ve Modüler Geliştirme

Bileşenler ( *components* ), React JavaScript kütüphanesini kullanarak istemci tarafı uygulamaları geliştirmenin arkasındaki temel yapı taşlarından birini oluşturur. Bileşenleri, olay ( *event* ) yönetimi için kullanıcı arayüzünü ( *UI* ) render etmek ve bileşenlerin iç durum ( *state* ) değişikliklerine göre kullanıcı arayüzünü güncellemek için kullanırsınız.

React’te modüler bileşenlerle uygulama geliştirme becerisi birkaç büyük avantaj sunar. Bileşenler, React kodunu test etmeyi ve hata ayıklamayı ( *debug* ) basitleştirir.

## 🧱 Component Composition ve Bileşen Türleri

Bileşen birleştirme ( *component composition* ) adı verilen yöntemle bileşenleri birleştirerek karmaşık kullanıcı arayüzleri oluşturabilirsiniz; buna rağmen kodu hâlâ kolayca okuyabilirsiniz.

React bileşenlerini iki yoldan biriyle oluşturabilirsiniz: sınıflarla ( *classes* ) veya fonksiyonlarla ( *functions* ). React’te geliştirme yapmak, bir bileşen durumuna ( *component state* ) erişim gerektirir.

## 🪝 Hooks ve Functional Components’a Geçiş

React Sürüm 16.8’den önce, geliştiriciler ve mimarlar sınıf bileşenlerini ( *class components* ) tercih ederdi çünkü bir bileşenin durumuna en kolay erişimi onlar sağlıyordu. Bu sürümün fonksiyonel bileşenlerle ( *functional components* ) birlikte *hooks* kullanımını tanıtmasından sonra, React ile geliştirme yapanlar, daha iyi performans gösterdikleri ve kodu sadeleştirip okunmasını ve üzerinde akıl yürütmeyi kolaylaştırdıkları için giderek fonksiyonel bileşenlere yönelmiştir.

## 🧾 Props ve Veri Akışı

Bileşenin özellikleri ( *properties* ), kısaca  *props* , bileşen için veriyi içerir. Veri, *props* nesnesini bir parametre olarak çocuk bileşene aktararak ebeveynlerden çocuk bileşenlere geçirilebilir.

React,  *props* ’u ebeveynden çocuğa geçirmeniz konusunda sizi sınırlar. Veriyi ters yönde aktaramazsınız. Bir çocuk bileşen ebeveynden aktarılan veriyi içeriyorsa, o veriyi değiştiremezsiniz.

## 🧠 State Yönetimi: Class vs Function Components

Bir bileşen durumuna erişip onu yönetme biçiminiz, fonksiyon tabanlı bileşenler ile sınıf tabanlı bileşenler arasında önemli ölçüde farklılık gösterir.

Bir sınıf bileşeninin durumuna erişmek için `this.state` kullanırsınız ve onu başlatmak veya güncellemek için bileşenin `this.setState` metodunu kullanırsınız.

Fonksiyon bileşenlerinde bir duruma erişirken *hooks* kullanmalısınız; özellikle `useState` hook’u.

## 🌐 Virtual DOM ve Performans

React, gerçek DOM’u soyutlayan ve bileşenler, *props* ve onların durumları ( *state* ) aracılığıyla güncellemeler yapmanıza olanak tanıyan bir sanal DOM ( *virtual DOM* ) kullanır.

Sanal DOM, gerçek DOM’u günceller ve yalnızca belirli öğeleri etkiler. React’in sanal DOM kullanımı, uygulamanın performansını önemli ölçüde artırır.

## 📝 Formlar ve Doğrulama

Bir kullanıcı arayüzü bir form içerdiğinde, genellikle formdan gelen girdi verisini bir bileşen durumunda saklarsınız.

Değerlerde doğru biçimlendirmeyi sağlamak için form verisini doğrulamanız ( *validate* ) gerekir. Form doğrulama süreci; girdi alma, form durumunu yönetme ve güncelleme, girdi değerlerini doğrulama, uygun hata mesajlarını görüntüleme gibi görevleri içerir.

## 🗃️ Redux ile Uygulama Düzeyi State Yönetimi

Uygulama düzeyinde durum ( *state* ) yönetiminde size yardımcı olması için Redux kütüphanesini kullanabilirsiniz. Büyük uygulamalar, kodunuzu sadeleştirmek için uygulama durumu yönetimine ihtiyaç duyar.

Bileşen sayısının yüksek olması,  *props* ’u bileşen ağacı ( *component tree* ) boyunca sıkça aktarmak yerine Redux gibi bir kütüphaneye ihtiyaç duyulduğunu gösterir.

## 📚 Kaynaklar, GitHub ve Sonraki Adımlar

Bu kursta sunulan bazı temel fikirleri gözden geçirdiğinize göre, her modülün sözlüklerini ( *glossaries* ) ve kopya kağıtlarını ( *cheat sheets* ) hatırlayın. Bu varlıkları, öğrendiklerinizin çoğunu hızlıca referans almak için kullanabilirsiniz.

Ayrıca laboratuvarlarda ve final projelerinde oluşturduğunuz uygulamaları GitHub’da paylaşabilirsiniz. Bu projeler, becerilerinizi potansiyel işverenlere göstermek için örnekler sağlar. Bu projeleri başkalarının erişimine açmak istiyorsanız, bu dizinleri ( *directories* ) herkese açık ( *public* ) yapmayı unutmayın.

## 🧭 Programlar ve Sertifika Yolculuğu

Eğer bu kursun bir parçası olduğu yazılım geliştirici programlarımızdan birine hâlihazırda kayıtlı değilseniz, bunu yapmanızı öneririz.

Programlardaki kurs sayısına ve programınıza bağlı olarak, bu programlar yaklaşık **2-6 ay** sürer. Daha kapsamlı program konuları şunları içerir: JavaScript ile full-stack geliştirme, Python ve JavaScript ile full-stack geliştirme, front-end geliştirme, çapraz platform mobil uygulama geliştirme.

Web ve uygulama geliştirme yolculuğunuza devam etmek istiyor ancak daha kısa bir program tercih ediyorsanız, aşağıdakileri değerlendirmek isteyebilirsiniz: bulut uygulama geliştirme temelleri, istemci tarafı, sunucu tarafı ve Mongo veritabanı, JavaScript ile programlama.

İlgileniyorsanız, bu programların bağlantılarını bu kursun sonunda yer alan tebrikler ve sonraki adımlar ( *congratulations and next steps* ) okumasında bulabilirsiniz. Her program birden fazla uygulamalı laboratuvar ve bir final projesi içerir. Profesyonel sertifika programlarında ayrıca, program boyunca öğrendiğiniz tüm becerileri sentezleyip sergilediğiniz bir bitirme ( *capstone* ) dersi de bulunur.

## ✅ Kapanış

Bu kursu tamamladığınız için tebrikler ve web uygulaması geliştirme yolculuğunuzda başarılar dileriz.
