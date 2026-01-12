# 🧭 İyi Kullanıcı Hikâyeleri Oluşturma

## 🎯 Öğrenme Hedefleri

Bu videoyu izledikten sonra bir kullanıcı hikâyesini tanımlayabilecek, iyi bir kullanıcı hikâyesinin parçalarını açıklayabilecek, kabul kriterleri eklemenin neden önemli olduğunu anlatabilecek, *INVEST* kısaltmasını tanımlayabilecek ve bir  *Epic* ’in ne olduğunu ve ne zaman kullanılacağını açıklayabileceksiniz.

## 🧩 Kullanıcı Hikâyesi Nedir?

Peki kullanıcı hikâyesi nedir? Basitçe söylemek gerekirse, kullanıcı hikâyesi ekibin *tamamlanmış (done) bir artırım* içinde teslim edebileceği bir iş değeri parçasını temsil eder. Eskiden bunlara gereksinimler derdik, ancak kullanıcı hikâyeleri bundan çok daha fazlasıdır.

Bir gereksinim genellikle “Şuna ihtiyacım var, buna ihtiyacım var” şeklindedir; ama bir kullanıcı hikâyesi şunları içerir:

* Bu kimin için?
* Ne ihtiyaçları var?
* Ama en önemlisi: Neden buna ihtiyaçları var?
* Bu özellik ya da işlevi elde etmekten hangi iş değerini elde ediyorlar?

## 📝 İyi Bir Hikâyenin Parçaları

Hikâyeler, iş değerinin iyi bir açıklamasını içermelidir: Ne olduğu, kimin ihtiyaç duyduğu ve bu hikâyeden elde ettiğimiz değer nedir?

Sonra, hikâyede varsayımlar ve ayrıntıların belgelenmesini severim. Bazen varsayımlar vardır; bir hikâye yapıyorsunuzdur ve bir tür kalıcılığa ihtiyaç duyar. İlişkisel bir veritabanı kullanacağınızı biliyorsanız, bunu oraya yazın; böylece geliştiriciye “Hey, NoSQL veritabanı aramaya gitme; ilişkisel veritabanı kullanmaya karar verdik” şeklinde bir ipucu vermiş olursunuz.

Bulutta bir şey sağlama (provision) yapacağınızı biliyorsanız, bunu kullanıcı hikâyesine ekleyin; böylece geliştirici niyetinizi bilir. Yani bildiğiniz her şeyi, varsayımları hikâyeye koyun; geliştirici niyetinizin ne olduğunu anlasın.

## ✅ Kabul Kriterleri ve “Bitti” Tanımı

Ve en önemlisi, *bitti tanımı* (definition of done), yani bazı kabul kriterlerine ihtiyacınız var. Bu hikâyenin ne zaman tamamlandığını nasıl bilirim? Ne zaman “done” olur?

Sprint review’da ürün sahibinin “Hey, bu istediğim şey değildi” dediğini öğrenmek istemezsiniz. Bunun yerine “bitti tanımı”nı belgelersiniz ve şöyle dersiniz: “Üzerinde anlaştığımız tanım buydu. Hikâyenin yaptığı şey bu. Eğer istediğiniz bu değilse, başka bir hikâye yazabiliriz; ama bu hikâye için söylediğimiz şeyi yaptık.”

## 🧑‍💼 Hikâye Açıklamasına Ne Yazılır?

Peki hikâye açıklamasına ne koyarsınız? Yine, bir persona’nın bir hedefe ulaşmak veya bir iş değeri elde etmek için bir işlev talep ettiğini belgelersiniz.

Bunu şu problem cümlesi (template) ile yaparız: *Bir rol olarak...* Rol nedir? Pazarlama yöneticisi mi? Müşteriler mi? Sistem yöneticisi mi? Bu kimin için?

Sonra bir işlevselliğe ihtiyacım var. Ne ihtiyaçları var? Bu kullanıcı hikâyesinin etidir; ama çok önemli bir şekilde,  *bir iş faydası elde etmek için* . Bu işlevi teslim etmenin faydası nedir?

Ürün backlog’unu tekrar önceliklendirdiğimizde, “Bu backlog’da daha yukarıda mı olmalı, daha aşağıda mı?” demek için iş değerine kriterlerden biri olarak bakacağız. Bu yüzden sadece ne olduğu değil, elde ettiğimiz değer de çok önemlidir.

## 🧾 Varsayımlar ve Ayrıntılar

Sonra varsayımlar ve ayrıntılar gelir. Bildiğiniz her şey; çok büyük ayrıntı olması gerekmez. Ama bildiğiniz her şey.

Dediğim gibi, bir veritabanı, bir kalıcılık kullanacağınızı biliyorsanız, sadece oraya yazın. Hikâyeyi yazarken konuştuğunuz her şeyi oraya koyun.

Yapmaya çalıştığınız şey, geliştiricinin ne yapılması gerektiğini anlamasına yardımcı olmaktır; bu hikâyenin tamamlanması için açık olmayan her şey.

## 🥒 Gherkin Sözdizimi

Ve sonra kabul kriterleri, yani *bitti tanımı* gelir. Bu, son derece, son derece önemlidir.

Bu kullanıcı hikâyesini bitmiş, tamamlanmış ya da done yapan şeyin ne olduğunu anlamak gerçekten önemlidir. Bunun için “turşunun” adını taşıyan *Gherkin* adlı bir sözdizimi kullanırız.

Gherkin; paydaşların, müşterilerin ve geliştiricilerin sistemin davranışını, yani “bitti tanımı”nı kolayca tarif etmesini sağlar. Şu şekilde gider:

```gherkin
Given <bir önkoşul>
When <bir eylem gerçekleştiğinde>
Then <test edilebilir sonuç>
```

“Given” hikâyeyi kurar: “Alışveriş sepetimde beş ürün var”, “Sisteme zaten giriş yaptım” gibi.

Sonra hangi eylem olur? Tetikleyen şey nedir? “Sepete bir ürün daha eklediğimde” ya da “Sepetten bir ürünü sildiğimde” gibi.

Ve sonunda bunun test edilebilir sonucu nedir? “Bunu görmeliyim”, “Şunu görmemeliyim”, “Sepetimde altı ürün olmalı” ya da “Sepetimde dört ürün olmalı” gibi.

Bu, herkesin anlamasını çok kolaylaştırır: Given temel durumdur, When olan tetikleyicidir, Then ölçülebilir çıktıdır. Ve bu çıktıyı ölçersem, hikâye done’dur.

## 🧪 Örnek Hikâye

Örnek bir hikâyeye bakalım:

```text
Bir pazarlama yöneticisi olarak,
müşteri adları ve e-postalarının bir listesine ihtiyacım var,
böylece onları pazarlama promosyonları hakkında bilgilendirebilirim.
```

Artık rolü biliyoruz. Bu müşteri için değil, sistem yöneticisi için değil; pazarlama yöneticisi için. Yani kimin fayda sağlayacağını biliyoruz.

Fonksiyonu biliyoruz: müşterileri e-postalarıyla listelemek istiyorlar.

Ve iş değerini biliyoruz: pazarlama promosyonları hakkında bilgilendirmek.

Artık “Müşterileri promosyonlardan haberdar etmek ne kadar önemli?” diyebilir ve belki de bunu daha az önemli bir hikâyenin önüne koyabilirsiniz.

Böylece şunları yakaladım: Kimin için? Ne istiyorum? Neden istiyorum? Ne değer elde ediyorum?

## 🧠 Varsayımlar

Sonra bazı varsayımlar eklemeyi severim. Bu varsayımlar, geliştiricinin hikâyeye karşılık gelen kodu yazmasına yardımcı olur.

Örneğin bir varsayım: müşteri e-postalarını tutuyoruz. Belki tutmuyoruz. Belki bu hikâye, müşteri e-postalarını oluşturan başka bir hikâyeye bağımlıdır.

Başka bir varsayım: müşteriler promosyonlara *opt-in* yapmıştır. Bu oldukça önemli. Birisi bunu düşünmemiş olabilir: “Hey, tüm müşterilerimize rastgele e-posta gönderemeyiz; promosyonları almak için opt-in yapmalarına izin vermemiz gerekir.”

## ✅ Kabul Kriterleri (Gherkin ile)

Ve kabul kriterleri: bitti tanımı nedir? Bu hikâyenin sahip olmasını istediğimiz davranış nedir?

Gherkin sözdizimini kullanırız:

```gherkin
Given veritabanında 100 müşteri vardır
And 90'ı e-posta promosyonlarına opt-in yapmıştır
When bir müşteri e-posta listesi talep ettiğimde
Then 100 değil, 90 müşteri e-postasının listesini görmeliyim
```

Bunun kritik olduğunu görebilirsiniz: sadece 100’ün tamamı değil; opt-in yapmış 90 kişi. Böylece geliştiriciler, opt-in yapanlara göre filtrelemeleri gerektiğini bilir.

Bunu bir paydaşa da verebilirsiniz; pazarlama yöneticisi davranışı anlayıp “Evet, istediğim davranış bu” diyebilir. Geliştirici okuyup “Evet, teslim edebileceğim davranış bu” diyebilir.

Sprint sonunda, müşterileri istediğinizde yalnızca opt-in yapanları alıyorsanız, bu bitti tanımıdır. Böylece hikâye done mu değil mi tartışması olmaz. Bu davranış varsa, done’dur.

## 🔤 INVEST Kısaltması

Akrinomları pek sevmem ama Bill Wake’in *INVEST* diye oldukça iyi bir tanesi var.

*INVEST* şunu söyler:

* **Independent (Bağımsız):** Backlog’da sıralayabilmek isterim; yerlerini değiştirebilmek, “Bu, şundan önce gelir” diyebilmek isterim. Her zaman bağımsız olamazlar; bazen bağımlılıklar vardır. Önceki örnekte, veritabanında müşteri e-postalarının olduğu varsayımımız vardı; eğer yoksa hikâye bağımsız değildir, e-postaları veritabanına koyan hikâyeye bağlıdır. Ama çoğunlukla onları bağımsız yazmaya çalışmak istersiniz.
* **Negotiable (Müzakere edilebilir):** Backlog’da hareket ettireceğim, daha yukarı ya da aşağı sıralayacağım. Belki daha fazla değer, daha fazla işlevsellik ya da daha azını koyarak ne kadarının gerçekten yapılması gerektiğini müzakere edeceğim. Çok sıkı şekilde “tam olarak şu gerekli”ye kilitli olmamalıdır.
* **Valuable (Değerli):** “Bu hikâye ne kadar değerli?” diyebilmeliyim. Müşterinin bundan hangi değeri aldığını görebilmeliyim; gerçekten bir kullanıcı hikâyesi olduğundan emin olmak için. Ve sadece müşterinin asla görmediği bir şey olan teknik borç hikâyesi olmamalıdır.
* **Estimable (Tahmin edilebilir):** Tahmin edebilmeliyim. Ne kadar büyük? Küçük mü, orta mı, büyük mü? Yeterli bilgi olmalı ki “Vay, buradaki her şeye bakınca bu çok büyük bir hikâye” diyebileyim. Sadece basit görünen tek satır olup sonra gerçekten zorlaşmamalı.
* **Small (Küçük):** Bir sprint içinde üzerinde çalışılabilecek bir şey olmalı; bu yüzden tanım gereği sprint’ten küçük olmalıdır.
* **Testable (Test edilebilir):** Hikâyenin done olup olmadığını test edebilmeliyim. Bu hikâye için bitti tanımını test etmek isterim. Bu yüzden hikâyeler test edilebilir olmalıdır.

## 🧱 Epic Nedir ve Ne Zaman Kullanılır?

Peki çok büyük fikirler ne olacak? Çok büyük fikirlere *Epic* denir.

Bir hikâye tek bir sprint’ten büyük olduğunda epikleri kullanırız; çünkü hikâye tanım gereği sprint’ten küçük olmalıdır. Daha büyükse, onu bir sprint’te bitiremeyeceğimiz büyük bir fikir olur; onu *Epic* yaparız ve Epic’i oluşturan daha küçük hikâyeleri Epic’in altına ekleriz.

Hiyerarşide Epic, hikâyeden daha üsttedir. Hikâyeler Epics tarafından tüketilir. Bu yüzden genellikle çok büyük olan herhangi bir hikâyeyi Epic yaparız. Eğer kendi başına tahmin edemiyorsak, tahmin edebileceğimiz daha küçük parçalara böleriz.

Epic’i ne zaman kullanırız? Elbette bir hikâye sprint’e sığmayacak kadar büyük olduğunda Epic yaparız.

Genellikle backlog maddeleri büyük fikirler olarak başlar; yani çok büyük olurlar. Bu yüzden Epic olarak başlarlar. Sonra backlog’u rafine ettikçe, onları sprint’e koyabileceğimiz daha küçük ve daha küçük hikâyelere dönüştürürüz.

Sprint planning için, tüm büyük hikâyeleri daha küçük hikâyelere bölmek istersiniz; tüm Epic’leri daha küçük hikâyelere bölmek istersiniz.

Yeni gelen istekler bazen Epic olabilir. Birisi bir özellik ya da işlev ister; kulağa basit gelebilir ama bir sprint’ten fazla sürecektir. O zaman onu Epic olarak girer, sonra daha sonra kullanıcı hikâyelerine bölersiniz.

## 🧾 Özet

Bu videoda, bir kullanıcı hikâyesinin bir persona’nın bir hedefe ulaşmak için bir işlev talep ettiğini belgelendirdiğini öğrendiniz. Bir şablon kullanmak, hikâyelerin tamamlanmış olmasını sağlamaya yardımcı olur.

“Bitti” tanımını belirlemek yanlış anlamaları en aza indirir ve iyi biçimlendirilmiş hikâyeler *INVEST* kısaltmasının kriterlerini karşılar. Ve büyük fikirleri yakalamak için  *Epic* ’ler kullanılabilir.
