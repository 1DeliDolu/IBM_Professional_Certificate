# 🗓️ Günlük Plan Uygulaması İçin İş Akışı

Bu videoyu izledikten sonra şunları yapabileceksiniz: günlük iş akışını tanımlamak, sırada hangi hikâye üzerinde çalışmanız gerektiğini belirlemek ve aynı anda birden fazla hikâye üzerinde neden çalışmamanız gerektiğini açıklamak.

Scrum sürecindeki adımlarda backlog refinement ve sprint backlog aşamalarını tamamen geçtik ve şimdi sprinti gerçekten **uygulamaya** geçiyoruz. Yani sprint; tasarla, kodla, test et, dağıt döngüsünün bir iterasyonudur. Bunu iki haftalık artışlarla yaparız.

Ve her birinin bir hedefi olması çok önemlidir; böylece herkes çalıştığı hedefi bilir.

## 🎯 Sprintin Günlük Uygulanması

Günlük uygulamada her üyenin yapmak istediği şey şudur: sprint başladığında, **üzerinde çalışabilecek becerilere sahip olduğu** sprint backlog’daki **en yüksek sıradaki** bir sonraki öğeyi alır.

Bazı UI geliştiricilerin backend işi yapamayacağını biliyorum, sorun değil. Ama bir sonraki öğe, en üstteki öğe olmalıdır; ortadan bir tane seçemezsiniz, favori öğenizi seçemezsiniz; **iş önceliği sırasına göre** çalışmalısınız.

## 📌 Hikâyeyi Üzerine Alma ve Görünür Kılma

Sprint backlog’daki bir sonraki en üstteki işi alırsınız ve onu kendinize atarsınız. Herkesin üzerinde çalıştığınızı bilmesi için **kendinize atamanız** çok, çok önemlidir.

Sonra onu **In Progress** durumuna taşırsınız ki artık görsel olarak herkes üzerinde çalıştığınızı görebilsin.

Şimdi Kanban panomuza geri dönelim. Sprint backlog’da üç hikâyemiz olduğunu görüyoruz ve şu an sprint backlog’un solundaki hiçbir şey umurumuzda değil çünkü sprint backlog’a odaklanmak istiyoruz:

* Neler  **işleniyor** ?
* Nelerin **gözden geçirilmesi** gerekiyor?
* Neler  **tamamlanacak** ?

Dolayısıyla günlük uygulama için sprint backlog’daki bir sonraki en üst sıradaki şeyi alıp **In Process** durumuna taşırsınız ve kendinize atamak için açarsınız.

## 👤 GitHub Üzerinden Kendine Atama

Açıldıktan sonra **assignees** kısmına tıklarsınız. Güzel özelliklerden biri, “Assign Yourself” yazan bir bağlantıya tıklayabilmenizdir; yoksa açılır menüden başkasına da atayabilirsiniz.

Ama siz bunu GitHub’daki kimliğiniz kimse ona atamak istersiniz.

Şimdi bunu GitHub’da kendime atadım, yani o hikâyeyi kapatabilirim ya da tabii ki hikâyeyi okuyacağım, ne olduğunu anlayacağım, ne yapmam gerektiğini anlayacağım ve sonra o hikâyeyi kapatacağım. Ardından küçük bir avatar ile **In Progress** sütununda görünür.

Bu avatar GitHub’daki resmim (avatarım) olur; sizinki de GitHub’daki avatarınız ne ise o olur.

## 👀 Şeffaflık ve Takım İçi Görünürlük

Şimdi burada ne görebildiğime bakın: artık herkes, yönetim dahil herkes, kimin ne üzerinde çalıştığını görebilir.

Takımımdaki bir başkası “Aa, şu Rofrano adamı, şu işi süreçte tutuyor” diyebilir; o da backlog’dan bir sonrakini alır, kendine atar ve üzerinde çalışmaya gider.

## 🚫 Aynı Anda Birden Fazla Hikâye Üzerinde Çalışmamak

Günlük uygulama sırasında akılda tutmanız gereken bazı önemli noktalar var: **Kimse aynı anda birden fazla hikâye üzerinde çalışmamalı.**

Küçük avatarların görünmesi bunun bir başka önemli özelliğidir; çünkü aynı avatarı birden fazla yerde görürsem, birinin birden çok hikâye üzerinde çalıştığını anlarım.

Sorun şudur: tamamlanmamış iki şeyin yüzde ellisini sevk edemem. Sadece tamamlanmış bir şeyin yüzde yüzünü sevk edebilirim.

Bu yüzden insanların odağının çok fazla yere çekilmesini istemem. Tek bir şeye odaklanmalarını, bir özelliği teslim etmelerini, sonra bir sonraki özelliğe geçmelerini isterim—tabii ki **bloklanmadıkları** sürece.

Eğer bloklandılarsa, o zaman sorun değil; biri sizi bloktan çıkarırken (scrum master sizi unblock edecek), yeni bir özellik üzerinde çalışmaya başlayabilir ve sonra bloklanan işe geri dönebilirsiniz.

## 🔍 Pull Request ve Review QA Akışı

İşiniz bittiğinde bir **pull request** oluşturursunuz ve hikâyeyi **Review QA** durumuna taşırsınız.

GitHub’da ZenHub ile pull request’leri, bir pull request oluşturduğunuzda otomatik olarak Review QA’ya gelecek şekilde ayarlamanın bir yolu vardır.

Ve eğer o pull request’e bir hikâye atarsanız—yani o pull request’e bir Git issue bağlarsanız—issue’u **In Process** sütunundan **Review QA** sütununa taşır ve ikisini birbirine bağlar.

Bu, her şeyi düzenli tutmanın güzel bir yoludur; böylece herkes bir pull request oluşturulduğunu bilir. Çünkü artık Review QA sütununda muhtemelen gidip birisi için gözden geçirmem gereken şeyleri görürüm.

## ✅ Birleştirme ve Done

Pull request merge edildiğinde, bunu alıp **Done** sütununa sürükleyebilirsiniz.

Kodunuz base branch ile—master branch ya da main branch ile—merge edildikten sonra, bunu Done sütununa taşıyabilirsiniz çünkü artık bitti.

Sonra her şeye baştan başlarsınız:

Sprint backlog’a geri dönersiniz, sprintteki bir sonraki en üst sıradaki işi alırsınız, kendinize atarsınız ve üzerinde çalışmaya başlarsınız.

## 🧾 Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz: herkes ne üzerinde çalıştığınızı bilsin diye Kanban panosunu güncel tutmanız gerekir; sahip olduğunuz beceriler dahilinde her zaman en yüksek öncelikli hikâye üzerinde çalışmak önemlidir; aynı anda birden fazla hikâye üzerinde çalışmak sprint sonunda hiçbir hikâyenin bitmemesine yol açabilir.
