## 🎥 Expert Viewpoints: Sunucu Tarafı JavaScript ve Node.js Üzerine Giriş Düşünceleri

Expert Viewpoints: Sunucu tarafı JavaScript ve Node.js üzerine giriş düşünceleri bölümüne hoş geldiniz. Bu videoda, sunucu tarafı JavaScript ve Node.js ile çalışmayı tartışan çeşitli uygulama geliştirme profesyonellerinden görüşler duyacağız.

## 🧩 Aynı Dil ile Frontend ve Backend

Node.js’i back-end diliniz olarak kullanmanın harika yanı, front-end dilinizle aynı olmasıdır. Bu da front end için yazmak ile back end için yazmak arasında bağlam değiştirmeyi (bir bakıma) daha kolay hale getirir. Temelde aynı geliştiriciler her ikisini de yazabilir. Yani birçok geliştirici birden fazla dil biliyor. Ama bu şekilde, JavaScript’te çok güçlü birine sahipseniz, bu bilgi hem front end’de hem de back end’de karşılığını verir.

## 🧪 Ortak Test ve Güvenlik Taraması Yaklaşımı

Front-end JavaScript için kullandığınız aynı code scanning ve code testing yaklaşımlarını back-end JavaScript için de kullanabilirsiniz. Bu şekilde dependency security scanning ve bunun gibi her şey için de, hem front end hem back end bağımlılıklar için NPM’i, yani node package management’ı kullanıyor olacak. Böylece bağımlılıklar ve paketler için birleşik bir yaklaşımınız olur.

## 🧑‍💻 Full-Stack Perspektifinden En Büyük Çekicilik

Node.js kullanmanın en bariz çekiciliği, en azından full-stack geliştiriciler için, istemci tarafında ve sunucu tarafında aynı dili kullanabilmenizdir. Yani yeni bir geliştiriciyseniz, öğrenmeniz gereken bir dil daha az olur. Yeni değilseniz bile, front-end ve back-end geliştirme arasında bağlam değiştirirken farkları en aza indirmek güzel olabilir.

## 🌍 Topluluk ve Kaynak Bolluğu

Diğer bir fayda da Node.js etrafındaki topluluktur. En güncel Stack Overflow anketinde, profesyonel geliştiricilerin %50’sinden fazlası tarafından kullanılıyor olduğu söyleniyordu.

Bu da, sizin için mevcut olan öğrenme kaynaklarının ve desteğin zenginliğine gerçekten yansıyor.

## 🔁 Bağlam Değişiminin Azalması

Eğer bir front-end geliştiricisiyseniz ve JavaScript’i anlıyorsanız, Node.js gibi bir framework ile back end’e geçmek çok da büyük bir sıçrama değildir. Ben aslında statik web siteleri yapmaya başladım ve sonra JavaScript kullanarak yavaş yavaş dinamik içerik eklemeyi öğrendim. Sonra sunucuda back-end sistemlerimi kurmak için Java veya PHP kullanmak zorunda kaldım. Bunu yaparken biraz bağlam değişimi oluyor, ama Node.js’te güzel olan şey şu: front end’de JavaScript kullanıyorsunuz ve back end’de de JavaScript kullanıyorsunuz. Yani bağlam değişimi biraz daha az oluyor. Back end’de servislerle çalışmaktan çıkıp web sitenize gidip biraz JavaScript eklemek kolay.

## 🧵 Single-Thread ve Callback Odaklı Yapı

İlk başta bana biraz garip gelen bir şey, Node.js’in single-thread yapısı ve her şeyin callback’lere dayanmasıydı. Yani callback’ler kullanarak asenkron programlama, Node.js ile biraz farklı bir yaklaşım. Ama bu, alışma meselesi.

Sevdiğim şeylerden biri ise, uygulamalarınızda kullanabilmeniz için NPM gibi registry’lerdeki paket bolluğuydu.

## ⚡ Performans ve Eşzamanlı İstekler

Node.js kullanmanın temel faydası daha hızlı işlem yapmasıdır. Eşzamanlı istekleri diğer tüm sunucu tarafı dillerden daha hızlı ele alabilir. Node.js; online oyunlar, sohbetler, video konferanslar veya sürekli güncellenen veri gerektiren herhangi bir çözüm için popüler bir tercihtir.

## 📚 JavaScript Bilenler İçin Öğrenme Kolaylığı

JavaScript’i zaten iyi bilen biri için Node.js öğrenmek daha kolaydır. Geliştiriciler bir runtime environment kullanarak hem front end hem back end’i JavaScript ile yazabilir. Bu durumda ayrı front-end ve back-end geliştiricilerine ihtiyaç yoktur.

JavaScript açıkça istemci tarafı web geliştirme için fiili standarttır. Bu nedenle JavaScript geliştiricilerinin bu becerileri sunucu tarafında da kullanabilmesi oldukça doğal bir yaklaşımdır. İşte Node.js bu noktada çok iyi oturur.

## 🧠 Mimari: Asenkron, Event-Oriented ve Yüksek Eşzamanlılık

Node.js’in olayı, mimarisidir; çünkü çok sayıda eşzamanlı bağlantıyı ele almasını sağlayan oldukça benzersiz bir single-thread, asenkron, event-oriented mimari sunar.

Yüz binlerce eşzamanlı bağlantıyı düşünün. Node.js, Google’ın Chrome JavaScript V8 engine’inin üzerine inşa edilmiştir. JSON parsing inanılmaz derecede hızlıdır çünkü JSON, JavaScript’te native bir veri tipidir. Node.js ayrıca microservices yaklaşımının benimsenmesiyle de çok iyi uyum sağlar; çünkü her microservice bir veya az sayıda tutarlı servise adanmıştır ve bu nedenle kapsam olarak doğası gereği sınırlıdır.
