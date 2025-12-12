# 📦 Dependencies (Bağımlılıklar)

Welcome to Dependencies! After watching this video, you will be able to: Explain what a dependency is in software development. List the benefits of using dependencies. And understand the challenges and risks of using dependencies.

Dependencies! dersine hoş geldiniz! Bu videoyu izledikten sonra: Yazılım geliştirmede *bağımlılığın* ne olduğunu açıklayabilecek, bağımlılık kullanmanın faydalarını sıralayabilecek ve bağımlılık kullanmanın beraberinde getirdiği zorlukları ve riskleri anlayabileceksiniz.

---

## ❓ Bağımlılık Nedir?

What are dependencies? A dependency is needed when a piece of software or code relies on another to function. They’re commonly used to add features and functionality to software without writing it from scratch.

Bağımlılıklar nelerdir? Bir yazılımın veya kod parçasının çalışmak için başka bir yazılıma ya da koda ihtiyaç duyması durumunda *bağımlılık* söz konusudur. Bağımlılıklar, bir özelliği en baştan yazmak zorunda kalmadan yazılıma yeni özellikler ve işlevler eklemek için yaygın olarak kullanılır.

---

## 📚 Kütüphaneler, Paketler ve Modüller

Dependencies are reusable code found in a library package or module that your code makes calls to. You can use a package manager to automate the download and installation of dependencies.

Bağımlılıklar, kodunuzun çağrılar yaptığı, kütüphane, paket veya modül içinde bulunan yeniden kullanılabilir kod parçalarıdır. Bağımlılıkların indirilmesi ve kurulumu için bir *paket yöneticisi* kullanarak bu işlemleri otomatik hâle getirebilirsiniz.

---

## 🚀 Bağımlılık Kullanmanın Faydaları

Here are some of the benefits of using dependencies in your code: The software development process becomes faster and more efficient. You can deliver software more quickly by building on previous work. Dependencies enable applications to have more features and functionality. Functionalities provided by the dependency eliminate having to write it from scratch. The functionality provided by the dependency could perform better than the native implementation.

İşte kodunuzda bağımlılık kullanmanın bazı faydaları:

* Yazılım geliştirme süreci daha hızlı ve verimli hâle gelir.
* Önceden yapılmış çalışmaları temel alarak yazılımı daha hızlı teslim edebilirsiniz.
* Bağımlılıklar, uygulamaların daha fazla özellik ve işlevsellik kazanmasını sağlar.
* Bağımlılığın sunduğu işlevler, aynı şeyi sıfırdan yazma ihtiyacını ortadan kaldırır.
* Bağımlılığın sağladığı işlevsellik, yerel (native) uygulama içi implementasyondan daha iyi performans gösterebilir.

Dependency is a software development term that references a piece of software that is reliant on another one.

*Dependency* terimi, yazılım geliştirme bağlamında, başka bir yazılıma bağımlı olan yazılım bileşenini ifade eden bir kavramdır.

---

## 🔗 Basit Bir Bağımlılık Senaryosu

Here is a very simple illustration: In this scenario, Program A needs a function that it doesn't have by default – but Program B's code can provide it.

Basit bir örnek üzerinden gidelim: Bu senaryoda Program A’nın, varsayılan olarak sahip olmadığı bir fonksiyona ihtiyacı vardır; ancak Program B’nin kodu bu fonksiyonu sağlayabilmektedir.

Program A is written to make a call to Program B for that function. Program B provides the requested functionality to Program A so the application can work as designed. Program A is considered a dependent, and Program B is the dependency.

Program A, bu fonksiyonu çağırmak için Program B’ye istek gönderecek şekilde yazılmıştır. Program B, istenen fonksiyonu Program A’ya sağlar ve böylece uygulama tasarlandığı şekilde çalışabilir. Bu durumda Program A *bağımlı* (dependent), Program B ise *bağımlılık* (dependency) olarak kabul edilir.

---

## ⚠️ İnternetten Kod Kullanmanın Riskleri

Downloading and using code from the Internet is risky. It could expose your software to vulnerabilities, bugs, or other flaws.

İnternetten kod indirip kullanmak risklidir. Bu durum, yazılımınızı güvenlik açıklarına, hatalara (bug’lara) veya diğer kusurlara maruz bırakabilir.

Production risk could occur as a result of implementing incompatible, outdated, or missing dependencies: Production servers could be impacted, resulting in performance degradation or crashes. Data could be leaked as a result of vulnerabilities. Customer data could be comprised.

Uyumsuz, güncel olmayan veya eksik bağımlılıkların kullanılması sonucunda *prodüksiyon riski* ortaya çıkabilir:

* Prodüksiyon sunucuları etkilenebilir; performans düşüşleri veya çökme yaşanabilir.
* Güvenlik açıkları nedeniyle veri sızıntısı oluşabilir.
* Müşteri verileri tehlikeye girebilir veya ele geçirilebilir.

Your company’s reputation could also be impacted, resulting in loss of business, reputation or even fines.

Şirketinizin itibarı da zarar görebilir; bu da iş kaybına, itibar kaybına ve hatta para cezalarına yol açabilir.

---

## 📜 Lisanslama ile İlgili Zorluklar

Licensing challenges are another important aspect of using dependencies. Be aware of any license requirements for dependencies you use. Use the correct type of licensing for your project. Make sure there's no unlicensed code in your application.

Bağımlılık kullanırken lisanslama ile ilgili zorluklar da önemli bir konudur. Kullandığınız bağımlılıkların lisans gerekliliklerinin farkında olmalısınız. Projeniz için doğru lisans türünü kullanın. Uygulamanızda lisanssız kod bulunmadığından emin olun.

---

## 🧪 Bağımlılıkları Projeye Dahil Etmeden Önce İnceleme

If you plan to use dependencies in your project, it's best practice to vet (or examine) them thoroughly before implementation Vet the dependency by checking the following:

Eğer projenizde bağımlılık kullanmayı planlıyorsanız, bunları projeye dahil etmeden önce detaylıca incelemek en iyi uygulamadır. Bir bağımlılığı aşağıdaki açılardan kontrol ederek *vet* (inceleme) etmelisiniz:

* **Design (Tasarım):** Check that the API is well-designed and well-documented.

  API’nin iyi tasarlanmış ve iyi dokümante edilmiş olduğundan emin olun.
* **Quality (Kalite):** Check the quality of the code for undesired behavior, and semantic problems.

  Kodun kalitesini; istenmeyen davranışlar ve anlamsal (semantic) problemler açısından kontrol edin.
* **Testing (Test):** Test the basic code functionality and look for any possible failures.

  Temel kod işlevselliğini test edin ve olası hataları gözlemleyin.
* **Debugging (Hata Ayıklama):** Check dependency's issue tracker for open issues and bug reports.

  Bağımlılığın  *issue tracker* ’ını inceleyerek açık sorunları ve hata raporlarını kontrol edin.
* **Maintenance (Bakım):** Review the commit history for bug fixes and ongoing improvements. Avoid using dependencies that haven't been updated for more than a year.

  Hata düzeltmeleri ve devam eden iyileştirmeler için *commit geçmişini* gözden geçirin. Bir yıldan uzun süredir güncellenmemiş bağımlılıkları kullanmaktan kaçının.
* **Usage (Kullanım):** Is the dependency widely adopted or seldom used? Seldom-used dependencies could be abandoned.

  Bağımlılık geniş çapta benimsenmiş mi, yoksa nadiren mi kullanılıyor? Nadiren kullanılan bağımlılıklar terk edilmiş olabilir.
* **Security (Güvenlik):** Software dependencies can present a large surface for attacks. Look for weaknesses and vulnerabilities that allow malicious input.

  Yazılım bağımlılıkları, saldırılar için geniş bir *saldırı yüzeyi* oluşturabilir. Kötü niyetli girdilere izin verebilecek zayıflıkları ve güvenlik açıklarını araştırın.

And lastly, use dependency management tools to manage downloads, and track version updates.

Ve son olarak, indirmeleri yönetmek ve sürüm güncellemelerini takip etmek için *bağımlılık yönetim araçları* kullanın.

---

## 🧬 Dolaylı (Indirect) Bağımlılıklar

A dependency that relies on another dependency isn't bad; however, it does pose some challenges. Code problems found within indirect dependencies may have an impact on your code. So, you should inspect all indirect dependencies.

Başka bir bağımlılığa bağlı olan bir bağımlılık (dolaylı bağımlılık) kendi başına kötü değildir; ancak bazı zorluklar doğurur. Dolaylı bağımlılıklardaki kod problemleri, sizin kodunuzu da etkileyebilir. Bu nedenle tüm dolaylı bağımlılıkları da incelemelisiniz.

Use a dependency manager to list any direct and indirect dependencies for inspecting all code. When you upgrade dependencies, be aware of any new, indirect dependencies that could also make their way into your project.

Tüm kodu incelemek amacıyla, doğrudan ve dolaylı tüm bağımlılıkları listelemek için bir *dependency manager* kullanın. Bağımlılıkları yükselttiğinizde, projenize eklenebilecek yeni dolaylı bağımlılıkların da farkında olun.

---

## 🌐 Flask: Python Tabanlı Bir Web Çatısı

Flask is a web framework written in Python that provides you with tools, libraries, and other features for building web applications. LinkedIn and Pinterest are two examples of organizations that use Flask.

Flask, Python ile yazılmış bir  *web framework* ’üdür ve web uygulamaları geliştirmek için size araçlar, kütüphaneler ve başka özellikler sunar. Flask kullanan organizasyonlara LinkedIn ve Pinterest örnek olarak verilebilir.

---

## 🧩 Flask’in Bağımlılıkları

Flask has its own dependencies which include: Werkzeug: which is a web server gateway interface, Jinja: a template language for rendering web pages, MarkupSafe: a security dependency for untrusted input, ItsDangerous: which is a secure data integrity dependency, and Click: a framework for writing command line applications.

Flask’in kendi bağımlılıkları vardır; bunlara şunlar dahildir:

* `Werkzeug`: Bir *web server gateway interface* (web sunucusu ağ geçidi arayüzü).
* `Jinja`: Web sayfalarını oluşturmada kullanılan bir şablon (template) dili.
* `MarkupSafe`: Güvenilmeyen girdiler için güvenlik sağlayan bir bağımlılık.
* `ItsDangerous`: Güvenli veri bütünlüğü ( *secure data integrity* ) sağlayan bir bağımlılık.
* `Click`: Komut satırı uygulamaları yazmak için kullanılan bir framework.

---

## 🔐 ItsDangerous ile Güvenli Token Oluşturma

You can call the dependency ItsDangerous, to generate a token for transmitting account information between web requests Let’s take a look at how this is done with a code example:

`ItsDangerous` bağımlılığını, web istekleri arasında hesap bilgilerini iletmek için bir *token* üretmek amacıyla çağırabilirsiniz. Bunun nasıl yapıldığına bir kod örneği üzerinden bakalım:

In the first line you import the `URLSafeSerializer` from the `itsdangerous` package Then you instantiate a `URLSafeSerializer` passing in a secret key that you control, and the word `'auth'` to signal that you want to use this token for authorization.

İlk satırda, `itsdangerous` paketinden `URLSafeSerializer` sınıfını içe aktarırsınız. Ardından, kontrolünüz altında olan bir gizli anahtarı ( *secret key* ) ve bu token’ı yetkilendirme ( *authorization* ) için kullanmak istediğinizi belirtmek üzere `'auth'` kelimesini geçirerek bir `URLSafeSerializer` örneği oluşturursunuz.

Then you generate a token by calling the `dump()` method passing in the data that you want to serialize which in this example is a dictionary with an `id` of 5 and a `name` of `"alice"` If you were to print out this token it would just look like a string of random characters but it is, in fact, encrypted so that it can only be decrypted with the secret key.

Daha sonra, serileştirmek istediğiniz veriyi — bu örnekte `id` değeri 5 ve `name` değeri `"alice"` olan bir sözlüğü — `dump()` yöntemi ile geçirerek bir token üretirsiniz. Bu token’ı ekrana yazdırsaydınız, rastgele karakterlerden oluşan bir string gibi görünürdü; ancak gerçekte, yalnızca gizli anahtar kullanılarak şifresi çözülebilecek şekilde şifrelenmiştir.

The data can now be safely sent to another service that can decrypt it if it has the key, or perhaps, it was only meant for your eyes so when it is sent back to you later you can decrypt it knowing that it hasn't been tampered with.

Bu veri artık, eğer gizli anahtara sahipse şifresini çözebilecek başka bir servise güvenli bir şekilde gönderilebilir; veya belki sadece sizin görmeniz içindir, bu durumda veri size geri gönderildiğinde, üzerinde oynama yapılmadığını bilerek token’ın şifresini çözebilirsiniz.

---

## 🔓 Token’ın Şifresini Çözme

The final line of code is showing you how to decrypt the message using the token and the `loads()` method, which returns the original message and prints out the name from the original dictionary.

Kodun son satırı, token ve `loads()` yöntemi kullanılarak mesajın şifresinin nasıl çözüldüğünü gösterir; bu yöntem, orijinal mesajı geri döndürür ve orijinal sözlükteki ismi ekrana yazdırır.

Of course if this was really another piece of code, you would instantiate the `URLSafeSerializer` serializer again with the same secret key and use that to decrypt the token.

Elbette bu gerçekten başka bir kod parçası olsaydı, aynı gizli anahtarı kullanarak `URLSafeSerializer` örneğini yeniden oluşturur ve token’ın şifresini çözmek için onu kullanırdınız.

---

## 🧾 Özet

In this video, you learned that: A dependency is a piece of code that another part of a code relies on to work. Dependencies add features and functionality to your program without writing it from scratch. Dependencies can speed up the development process and save money. Dependencies should be carefully vetted before implementation. Use a dependency manager to list all direct and indirect dependencies for inspecting all code. A dependency may have its own dependencies. Flask is a Python-based web development platform providing tools, libraries, and its own dependencies.

Bu videoda şunları öğrendiniz:

* Bir bağımlılık, başka bir kod parçasının çalışmak için güvendiği kod bileşenidir.
* Bağımlılıklar, işlevleri sıfırdan yazmadan programınıza özellik ve işlevsellik ekler.
* Bağımlılıklar, geliştirme sürecini hızlandırabilir ve maliyet tasarrufu sağlayabilir.
* Bağımlılıklar, projeye dahil edilmeden önce dikkatlice incelenmelidir.
* Tüm kodu incelemek için doğrudan ve dolaylı tüm bağımlılıkları listelemek amacıyla bir *dependency manager* kullanın.
* Bir bağımlılığın kendi bağımlılıkları da olabilir.
* Flask, araçlar, kütüphaneler ve kendi bağımlılıklarını sağlayan, Python tabanlı bir web geliştirme platformudur.
