# 💡 İçeriden Bakış: Araçlar ve Teknolojiler

İçeriden Bakışlar: Araçlar ve Teknolojiler’e hoş geldiniz. Bu videoda, yazılım mühendisliği projeleri için en sevdikleri araçlar ve teknolojiler hakkında konuşan uzmanları dinleyeceğiz.

## 🧰 Git ve GitHub

Ekibimiz, tüm projelerimizde her gün Git ve GitHub kullanıyor. Bunları kodu takip etmek için kullanıyoruz. İşbirliği için kullanıyoruz ve tüm projelerimizde hataları, özellikleri ve görevleri takip etmek için kullanıyoruz. Bence artık çoğu açık kaynak proje Git kullanıyor. Açık ya da kapalı kaynak fark etmeksizin katkıda bulunduğum her proje Git kullanıyordu.

Git’in gerçek değeri, bir ekiple, birden fazla kişiyle çalıştığınızda ortaya çıkıyor; bu noktada **feature branch’ler** ve **pull request’ler** gibi şeylerin ne kadar işe yaradığını görüp mutlu oluyorsunuz. Ama bir projede tek katkı yapan kişi siz olsanız bile, yine de Git ve özellikle topluluk yönü nedeniyle GitHub kullanmanızı tavsiye ederim.

## 🎨 Front-end geliştirme ve IDE’ler

Eğer bir front-end geliştiriciyseniz, JavaScript’i anlıyorsanız, Node.js gibi bir framework kullanarak back-end’e geçmek o kadar da zor değildir. Ben aslında statik web siteleriyle başlamıştım ve sonra yavaş yavaş JavaScript kullanarak dinamik içerik eklemeyi öğrendim. Sonra sunucuda arka uç sistemlerimi geliştirmek için Java ya da PHP kullanmam gerekti.

Front-end geliştirme için temel olarak **HTML, CSS ve JavaScript** kullanırsınız. Eğer çok front-end odaklıysanız, özellikle bu amaç için geliştirilmiş **Brackets** gibi bir IDE’yi denemek isteyebilirsiniz; işleri daha genel tutmak istiyorsanız  **VS Code** ’u tavsiye ederim.

Her iki durumda da, kodunuzun otomatik biçimlendirilmesi ve lint edilmesi için **Prettier** ve **ESLint** gibi IDE uzantılarını kurmanızı öneririm. Bunlar sorunları olabildiğince erken yakalamanıza yardımcı olur.

Back-end geliştirme için araçlar oldukça daha çeşitlidir, bu yüzden net önerilerde bulunmak zordur. Ama eğer **Node.js** seçerseniz, front-end geliştirme için bahsettiğim araçların bazılarını yine kullanabilirsiniz. Aksi takdirde, hangi IDE uzantılarının mevcut olduğuna ve hangi linter’lar ile otomatik biçimlendiricilerin bulunabildiğine bakmanızı tavsiye ederim.

JavaScript çok güçlü bir dildir. Düşünebileceğiniz hemen hemen her şeyi yapmanıza izin verir; dikkatli olmazsanız kendi ayağınıza sıkmanız da dahil.

Benim JavaScript ile çalışırken genellikle takip ettiğim uygulamalar, değişkenlerin ve fonksiyonların doğru kapsamda tanımlanması ve özelliklerim için birim (unit) ve entegrasyon testleri yazmaktır.

## ⚛️ JavaScript framework’leri ve kütüphaneleri

 **React JS** , Facebook’ta geliştirildi ve çok popüler.  **Angular** , Google tarafından işletilen ve tek sayfalı uygulamalar (SPA’ler) geliştirilmesine imkan veren bir framework.

 **jQuery** , muhtemelen en popüler ve en eski kütüphanedir; 2006’da John Resig tarafından oluşturulmuştur ve jQuery, hem Angular hem de React ile birlikte sıklıkla kullanılır.

 **Backbone** , hafif bir JavaScript kütüphanesidir ve oldukça popülerdir.

## 🖥️ Back-end dilleri ve framework’ler

Back-end dilleri ve framework’leri açısından:

 **Node.js** , Google Chrome JavaScript motoru üzerine kurulmuş, açık kaynaklı, sunucu taraflı bir platformdur. Asenkron, tek iş parçacıklı (single-threaded) bir mimari kullanır; bu da çok büyük sayıda eşzamanlı bağlantıya hizmet verebilmesini sağlar.

 **Flask** , Python üzerinde kullanılan ve Pythonseverler (Pythonistas) arasında popüler olan bir framework’tür ve Java tabanlı **Spring** framework’ü yıllardır varlığını sürdürmektedir ve popülerliğini korumaktadır.

## ⚛️ React ve JSX’in avantajları

Biz **React JavaScript framework’ünü** kullanıyoruz; hız ve verim açısından Angular’dan daha iyi. React, diğer JavaScript framework’lerine göre öğrenmesi daha kolaydır; bu da ekibe adapte edilmesini kolaylaştırır. Ayrıca tarayıcılar arası uyumlulukla ilgili sorunları da çözer, evet, bu sorunları da çözer.

React’in bir diğer harika özelliği **JSX** kullanımıdır. JSX, JavaScript kodunun içinde kullanıcı arayüzü (UI) ile çalışırken çok yardımcı olur. React’in daha yararlı hata ve uyarı mesajları göstermesine yardımcı olur.

En sevdiğim front-end JavaScript framework’ü **React JS** olurdu; React JS tabanlı bir uygulama oluştururken takip etmeniz gereken tüm o bileşen odaklı tasarım ve mimariyi çok seviyorum. Ayrıca, uygulamanızın durumunu tutmak için **props** ve **state** kavramlarını kullanma fikrini de seviyorum.

## 🚀 Express JS, Node.js ve paketler

Back-end geliştirme için **Express JS** kullanarak uygulamaları hızlı bir şekilde ölçeklendirebiliyoruz. Express JS kullanarak JavaScript yardımıyla hem front-end hem de back-end kodlayabiliyoruz. Express JS, **Google V8** motoru tarafından desteklenir; bunun sayesinde gecikme veya işleme sırasında hata olmadan daha yüksek performans elde edebilirsiniz.

Aynı zamanda önbellekleme (caching) özelliklerini de destekler; böylece kodları tekrar tekrar çalıştırmak zorunda kalmazsınız. Dahası, web sayfalarının her zamankinden daha hızlı yüklenmesine yardımcı olur.

Node.js ile çalışırken, size günlük olarak kullandığım iki favori paketimi söyleyeyim.

İlk olarak, web servislerine istek yapmak için, doğru header’larla bu istekleri oluşturmama yardımcı olan ve gelen yanıtları ele almak için bana geri çağırma fonksiyonları (callback) ve/veya **promiseler** sağlayan **Axios** gibi bir kütüphane kullanırım.

İkinci paketim ise veritabanlarıyla çalışırken olur; harici bir veritabanıyla konuşmak için, ister ilişkisel bir veritabanı olsun ister NoSQL veritabanı olsun, büyük olasılıkla **NPM paketleri** kullanırım.

JavaScript yazarken, kodumu daha temiz, okunması daha kolay ve sadece daha güzel gösterebildiği için **ES6** özelliklerinden yararlanmayı gerçekten seviyorum; örneğin **ok (arrow) fonksiyonları** ya da **üç nokta (… / dot dot dot) operatörü** gibi. Bu yüzden, JavaScript’i öğrendikten sonra ES6’ya biraz dalmanızı ve onunla eğlenmenizi tavsiye ederim.
