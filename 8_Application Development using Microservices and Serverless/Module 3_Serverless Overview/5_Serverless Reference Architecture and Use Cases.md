# 🧩 Serverless Referans Mimarisi ve Kullanım Örnekleri

## 🎯 Giriş ve Öğrenme Hedefleri

“Serverless Referans Mimarisi ve Kullanım Örnekleri”ne hoş geldiniz.

Bu videoyu izledikten sonra şunları yapabileceksiniz: *Serverless Framework* kullanarak bir Web Uygulaması referans mimarisini açıklamak ve  *Serverless Framework* ’ün diğer kullanım örneklerini tanımlamak.

![1765370457594](image/5_ServerlessReferenceArchitectureandUseCases/1765370457594.png)

## 🕸️ Web Uygulaması Referans Mimarisi (To Do Uygulaması)

Kayıtlı bir kullanıcının öğeler oluşturabildiği, okuyabildiği, güncelleyebildiği ve silebildiği basit bir Yapılacaklar ( *To Do* ) uygulamasını hayata geçiren bir Web uygulamasına bakalım.

Web Uygulaması referans mimarisi, iş mantığı için *AWS Lambda* ve *Amazon API Gateway* kullanan, genel amaçlı ve olay güdümlü ( *event-driven* ) bir arka uçtur.

Ayrıca veritabanı olarak *Amazon DynamoDB* ve kullanıcı yönetimi için *Amazon Cognito* kullanır.

Uygulamadaki tüm statik içerik *AWS Amplify Console* kullanılarak barındırılır.

Bu Yapılacaklar uygulamasının mimarisi gösterildiği gibidir. Uygulamada çeşitli bileşenleri görebilirsiniz. Temelde, Web Uygulaması 3 farklı bileşenden oluşur.

![1765370501184](image/5_ServerlessReferenceArchitectureandUseCases/1765370501184.png)

![1765370527216](image/5_ServerlessReferenceArchitectureandUseCases/1765370527216.png)

## 🖥️ Ön Uç (Front-end) Bileşeni

Ön uç ( *front-end* ) uygulaması, *Create React App* kullanılarak üretilen tüm statik içeriği barındırır; bunlar, *HTML* dosyaları, stillendirme için  *CSS* , istemci tarafında çalışacak *JavaScript* ve görsellerden oluşur.

Bu nesnelerin hepsi *AWS Amplify Console* üzerinde barındırılır.

Bir kullanıcı web sitesine bağlandığında, gerekli kaynaklar tarayıcısına indirilir ve orada çalışmaya başlar.

Uygulamanın arka uç ile iletişim kurması gerektiğinde, arka uca *REST API* çağrıları yapar.

![1765370570778](image/5_ServerlessReferenceArchitectureandUseCases/1765370570778.png)

## ⚙️ Arka Uç (Back-end) Bileşeni

Arka uç ( *back-end* ) uygulaması ise gerçek iş mantığının uygulandığı yerdir.

Bu iş mantığı, ön ucun *API Gateway* aracılığıyla *REST API* kullanarak eriştiği *Lambda functions* içinde barındırılır.

Veriler daha sonra *DynamoDB* içinde saklanır.

![1765370601222](image/5_ServerlessReferenceArchitectureandUseCases/1765370601222.png)

## 👤 Kullanıcı Kaydı ve Kimlik Doğrulama

Yapılacaklar uygulaması, kullanıcıları kendi yapılacak öğeleriyle sınırlar.

Bu nedenle kullanıcıların, kendi bireysel Yapılacaklar öğelerine erişebilmek için kayıtlı ve kimliği doğrulanmış olmaları gerekir.

Bunu gerçekleştirmek için, kullanıcıların uygulamaya kayıt olmasını ve kimliklerinin doğrulanmasını sağlayan *Cognito User Pools* kullanırsınız.

![1765370628132](image/5_ServerlessReferenceArchitectureandUseCases/1765370628132.png)

## 📡 Olay Akışı (Event Streaming) Kullanım Senaryosu

Sunucusuz ( *Serverless* ) uygulamalar için yaygın bir kullanım senaryosu  *Event streaming* ’dir.

Bu uygulamalar, önceden altyapı kurmaya gerek kalmadan yazılabilir ve dağıtılabilir.

Ve yayımcı/abone ( *publisher, subscriber* ) konularından ya da olay günlüklerinden tetiklenebilir; böylece karmaşık kümeleri ( *cluster* ) işletme gereksinimi olmadan, esnek ve ölçeklenebilir olay hatları ( *event pipelines* ) elde edersiniz.

Bu olay akışı hatları, analiz sistemlerinizi besleyebilir, ikincil veri depolarını ve önbellekleri güncelleyebilir veya izleme ( *monitoring* ) sistemlerine veri sağlayabilir.

![1765370660367](image/5_ServerlessReferenceArchitectureandUseCases/1765370660367.png)

## 🖼️ Sonradan İşleme (Post-processing) Örnekleri

Sonradan işleme ( *post-processing* ) örnekleri arasında, görselleri dinamik olarak yeniden boyutlandırabildiğiniz ya da farklı hedef cihazlar için video kodlamasını ( *transcoding* ) değiştirebildiğiniz Görüntü ve Video İşleme yer alır.

Sonradan işleme, pasaport fotoğrafınızda gölge olup olmadığını tespit etmek gibi, görüntü tanıma veya yapay zekâ amaçları için de kullanılabilir.

![1765370700450](image/5_ServerlessReferenceArchitectureandUseCases/1765370700450.png)

## 🧑‍💻 Çok Dilli (Multi-language) Uygulamalar

Bir uygulama geliştirirken, uygulamada hangi dili kullanacağınıza karar vermeniz gerekir.

Sunucusuz uygulamalar çok dilli ( *multi-lingual* ) olabilir.

Bu yaklaşım, ekipleri, eski ( *legacy* ) yazılımlarıyla aynı dili süresiz kullanmak zorunda kaldıkları dil bağımlılığı ( *language lock-in* ) durumundan korur.

Genellikle, uygulamayı geliştirmek için seçilen dil, projeye en uygun dil olmaktan ziyade, mevcut kaynaklara bağlı olarak belirlenir.

![1765370725104](image/5_ServerlessReferenceArchitectureandUseCases/1765370725104.png)

## 📌 Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* Web Uygulaması referans mimarisinin,  *AWS Lambda* ,  *Amazon API Gateway* ,  *Amazon DynamoDB* , *Amazon Cognito* ve *Amazon Amplify Console* kullanan olay güdümlü ( *event-driven* ) bir yapı olduğu.
* Web Uygulamasının, ön uç ( *front-end* ), arka uç ( *back-end* ) ve kullanıcı kaydı ile kimlik doğrulama bileşenlerinden oluşan 3 bileşene sahip olduğu.
* Sunucusuz web uygulamaları için kullanım senaryolarının  *Event streaming* , *Post-processing* ve *Multi-language* olduğu.

![1765370758947](image/5_ServerlessReferenceArchitectureandUseCases/1765370758947.png)
