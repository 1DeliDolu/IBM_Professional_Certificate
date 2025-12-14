# 🧩 Required DevOps Behaviors

Bu videoyu izledikten sonra, **geleneksel Ops** ile **DevOps** arasındaki farkları ayırt edebilecek, **Dev ve Ops’un birbirini nasıl gördüğünü** açıklayabilecek ve **gerekli DevOps davranışlarını** listeleyebileceksiniz.

DevOps, geleneksel işletmelerin düşünme biçimine taban tabana zıt bir yaklaşım sunar. Kurumlar, uçtan uca süreçler etrafında inşa edilmiştir ve “yeni” olanı karmaşık, yüksek riskli, pahalı ve zaman alıcı görür. Yeni olan her şeyi, sabit bütçe ve sabit zaman çerçevesinde tamamlanacak **tek seferlik bir proje** olarak ele alırlar; ardından insanları bir sonraki projeye taşırlar.

DevOps ise bunu tersine çevirmeyi hedefler; büyük projeleri parçalayarak **sürekli bir dizi küçük değişiklik** teslim etmeye odaklanır. Daha küçük değişiklikler daha az riskle tamamlanabildiği için DevOps, büyük projelerin riskini azaltır.

Buradaki kritik nokta şudur: Küçük değişiklikler, kurumların her işe eklediği geleneksel “üst yük” ile yaşayamaz. *Change review board* gibi süreçler DevOps’ta çalışmaz, çünkü küçük değişikliklerin ihtiyaç hızına yetişemezler.

---

## ⚔️ Geleneksel Ops ve DevOps Kültür Çatışması

Geleneksel Ops ile DevOps arasında bir çalışma kültürü çatışması vardır.

Geleneksel Ops’ta, kritik altyapıda **manuel yapılandırma değişiklikleri** yapılır. DevOps’ta ise **tüm ortamlara otomatik dağıtım** yapılır. Geleneksel Ops’un  *change review board* ’lara ihtiyaç duymasının sebebi budur: Her şey manuel yapıldığından insanlar hata yapabilir ve değişiklik onaylansa bile doğru uygulanacağının garantisi yoktur.

Geleneksel Ops’ta uygulama mimarileri, **ağ tasarımı** tarafından belirlenir. DevOps’ta bunun tersi geçerlidir: Ağ tasarımı, **uygulama mimarileri** tarafından belirlenir.

 *Software-defined network* ’ler, mimarinin ihtiyaç duyduğu şeye uyum sağlar.

---

## 🧱 Altyapı Yaklaşımı: Kalıcı vs. Ephemeral

Geleneksel Ops’ta, özel (bespoke) altyapı bir kez kurulur ve sonra sonsuza dek bakım yapılır. DevOps’ta ise yeni dağıtımlar için **ephemeral altyapı** oluşturulur. Altyapıyı “bakımını yapmayız”; onu yıkar ve tamamen yenisiyle değiştiririz.

Bunu yapabilmek için her şeyin otomatik olması gerekir. Aksi halde manuel operasyon yükü sizi fazla yavaşlatır.

---

## 🕒 Risk Yönetimi: Change Window vs. Progressive Activation

Geleneksel Ops’ta risk,  **change window** ’lar aracılığıyla yönetilir. Değişiklikler yalnızca önceden belirlenmiş zamanlarda yapılır; bu pencerelerin dışında değişiklik yapılamaz.

DevOps’ta risk, **progressive activation** ile yönetilir. Sisteme herhangi bir zamanda değişiklik yapılabilir. Değişikliği gerektiğinde etkinleştirmek ya da devre dışı bırakmak için dağıtım teknikleri kullanılır.

---

## 🧰 Süreçler: “Build Once” vs. Tekrarlanabilir Yüksek Hacim

Geleneksel Ops, “ *build once* ” yaklaşımına eğilimlidir. Her şeyi manuel kurar ve sonsuza dek (ya da ihtiyaç bitene kadar, genellikle yıllarca) sürdürür.

Bazen bir kere kurarlar ve daha sonra aynı şekilde tekrar nasıl kuracaklarını bilemezler; çünkü kurulum belgelenmemiştir.

DevOps’ta süreçler, değişikliklerin yüksek hacimde ve hızlı akışla geçmesi için yeniden tasarlanır. Kurulumlar tekrarlanabilir hale getirilir ve *Infrastructure as Code* kullanılarak yapılan her şeyin yeniden inşa edilebilir olması sağlanır.

---

## 🧱 “No-Win Scenario” ve Dev–Ops Gerilimi

Kültürler çarpıştığında bu bir **kazan-kazan** değil, **kazanı olmayan (no-win)** bir senaryodur.

Geliştirme, geliştiricilerin ne kadar inovasyon üretebildiğiyle ölçülür. Kullanıcıların değişen ihtiyaçlarına yeni ve geliştirilmiş yetenekler geliştirip dağıtarak ayak uydururlar.

Operasyon ise **istikrar** ister. Kullanıcıların servisleri ve uygulamaları kullanabilmesini ve verilerinin güvende kalmasını sağlamak ister.

Bu iki hedef birbiriyle çelişir.

Her ikisine birden sahip olamazsınız.

Andrew Clay Shafer buna Dev ve Ops arasında var olan “ **wall of confusion** ” adını vermiştir. Yapmamız gereken şey bu duvarı yıkmaktır.

---

## 👀 Dev ve Ops’un Birbirini Görme Biçimi

İlk adım, geliştirme ve operasyonun birbirini nasıl gördüğünü değiştirmektir.

Ops’un geliştirmeye bakışı şudur: geliştirme “duvarın üzerinden ölü kedi fırlatıyordur.” Değişiklikleri manuel uygularlar. Geri alma planları yoktur ve test yoktur. Ortamları production ortamlarına benzemez.

Geliştiriciler ise Ops’un gecenin bir yarısı, bu change window’larda, hep ya da hiç gibi değişiklikler yaptığını düşünür. Koda en uzak taraftadırlar, bu yüzden kodu anlamazlar. Ops,  *runbook* ’lardan ya da Word dokümanlarından kopyala-yapıştır yapıyordur.

Silo’lar ilgisizliği (apathy) besler.

Birbirine taban tabana zıt metriklerle iki silo halinde çalışan insanlara sahip olamazsınız. Bu asla çalışmayacaktır. Bu insanları bir araya getirmelisiniz. Müşteriye değer katan tek bir metrik seti vermelisiniz.

Web sitesi çalışıyorsa övgüyü geliştiriciler alır. Web sitesi çökerse suç Ops’a kalır.

Bahsetmiş miydim, no-win senaryosu?

Bu sağlıklı bir çalışma ortamı değildir.

---

## ✅ Gerekli DevOps Davranışları

İşte gerekli bazı DevOps davranışları. DevOps bunların birçoğunu tersine çevirir.

Organizasyonel silo’ları ve onların yarattığı el değiştirmeleri (handoff) yıkmanız; **paylaşılan sahiplik (shared ownership)** ve yüksek iş birliği (high collaboration) kültürüne geçmeniz gerekir.

Teknede “senin tarafında delik yok.” Herkes kendini ortak bir hedef için birlikte hareket eden taraf olarak görmelidir.

Değişim korkusundan, değişimi kucaklayarak riski yönetmeye geçmelisiniz; küçük değişiklikleri yönetmelisiniz. Büyük değişiklikler herkes için her zaman korkutucudur. Değişiklikleri küçük yapın ve değişimi yönetin.

Bir şeyi bir kez kurmaktan; el yapımı, “snowflake server” denilen, her biri benzersiz ve bir daha aynısı bulunamayan sunuculardan; *Infrastructure as Code* teknikleriyle dağıtılan **ephemeral altyapıya** geçin ki tekrar üretilebilir olsunlar.

Her Docker container’ı oluşturduğunuzda, her sanal makine kurduğunuzda, onu tam olarak aynı şekilde kurun. Eğer kod değişmediyse, tam olarak aynı şekilde inşa edilecek ve aynı sonuçları verecektir.

Manuel yerine getirme (ticket kuyrukları, insanların manuel iş yapması) yaklaşımından, **otomatik self-service** sağlamaya geçin.

Bulutu benimseyip, sonra önüne bir ticket kuyruğu koyarak sadece IT’nin buluttan provizyon yapmasına izin veren şirketler gördüm. Bu, self-service cloud’un tüm amacını boşa çıkarır. Self-service hızlı hareket etmenin yoludur.

Son olarak, alarm/callback/escalation yaklaşımından, **veri odaklı hızlı geri bildirim döngülerine** geçmelisiniz. Production’da nelerin yanlış gittiğine dair bilgiyi alabildiğinizden emin olun ve gerektiğinde buna tepki verin.

Bunlar, tam anlamıyla bir DevOps organizasyonu olabilmek için değişmesi gereken davranışlardır.

---

## 🧾 Videodan Öğrendikleriniz

Bu videoda şunları öğrendiniz: Kurumlar değişimi karmaşık ve zaman alıcı görür. DevOps büyük projeleri küçük, yönetilebilir değişiklikler serisine böler. Geleneksel Ops bir kez kurar ve sürdürür. DevOps’ta her yeni dağıtım için ephemeral altyapı oluşturulur. Dev inovasyon isterken Ops istikrar ister. Gerekli DevOps davranışları arasında paylaşılan sahiplik, iş birliği, değişimi kucaklama ve veri odaklı tepkiler yer alır.
