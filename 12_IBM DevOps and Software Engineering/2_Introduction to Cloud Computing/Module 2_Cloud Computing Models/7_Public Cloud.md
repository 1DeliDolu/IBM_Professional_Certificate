# ☁️ Public Cloud

Giriş niteliğindeki bulut videomuzda, bulut için dört dağıtım modelinden kısaca bahsetmiştik. Bu videoda, **Public Cloud (Genel Bulut)** dağıtım modelini daha ayrıntılı ele alacağız. Dağıtım modelleri; altyapının  **nerede bulunduğunu** , **kimin sahip olup yönettiğini** ve bulut kaynakları ile hizmetlerinin kullanıcılara **nasıl sunulduğunu** gösterir.

![1765803807092](image/7_PublicCloud/1765803807092.png)

Dört bulut dağıtım modeli şunları içerir:  **Public Cloud** ,  **Private Cloud** , **Community Cloud** ve  **Hybrid Cloud** .

![1765803825495](image/7_PublicCloud/1765803825495.png)

---

## 🌐 Genel Bulutun Tanımı ve Sunum Şekli

Genel bulut modelinde kullanıcılar; sunuculara, depolamaya, ağa, güvenliğe ve uygulamalara, bulut hizmet sağlayıcıları tarafından internet üzerinden sunulan hizmetler olarak erişir.

Web konsolları ve API’ler kullanılarak, kullanıcılar ihtiyaç duydukları kaynak ve hizmetleri sağlayabilir (provision edebilir). Bulut sağlayıcısı altyapının  **sahibidir** ,  **yönetir** , **sağlar** ve  **bakımını yapar** ; bunu müşterilere ya abonelik ücretiyle ya da kullanıma dayalı ücretle kiralar.

![1765803878752](image/7_PublicCloud/1765803878752.png)

---

## 🧩 Mülkiyet ve Sorumluluklar

Kullanıcılar; uygulamalarının çalıştığı sunuculara veya verilerinin kullandığı depolamaya  **sahip değildir** ; sunucuların operasyonlarını **yönetmez** ve hatta platformların nasıl bakım gördüğünü  **belirlemez** .

Gündelik yaşamda su, elektrik veya gaz gibi hizmetleri tüketip ödediğimiz şekilde, bu bulut kaynaklarının hiçbirine sahip olmayız—hizmet sağlayıcıyla bir anlaşma yapar, kaynakları kullanır ve belirli bir dönem içinde kullandığımız kadar öderiz.

---

## 💸 Maliyet, Ölçeklenebilirlik ve Kontrol

Genel bulutlar, altyapı ve barındırıldığı tesislerle ilgili tüm sermaye, operasyon ve bakım giderlerini sağlayıcı üstlendiği için, **Toplam Sahip Olma Maliyeti (TCO)** açısından önemli maliyet tasarrufları sunar.

Ölçeklenebilirliği, daha fazla kapasite talep etmek kadar kolay hâle getirir. Ancak genel bulutta kullanıcı, bilişim ortamı üzerinde herhangi bir kontrole sahip değildir ve sağlayıcının altyapısının performansı ve güvenliğine tabidir.

![1765803914893](image/7_PublicCloud/1765803914893.png)

---

## 🏢 Piyasadaki Örnek Sağlayıcılar

Günümüzde pazarda Amazon Web Services, Microsoft Azure, IBM Cloud, Google Cloud Platform ve Alibaba Cloud gibi çeşitli genel bulut sağlayıcıları vardır.

Tüm sağlayıcılar; sunucular, depolama, ağ, güvenlik ve veritabanları gibi ortak bir çekirdek hizmet seti sunsa da, çeşitli ödeme seçenekleriyle geniş bir niş hizmet yelpazesi de sunarlar.

![1765803929338](image/7_PublicCloud/1765803929338.png)

---

## 🧱 Genel Bulutun Özellikleri

Genel bulutun bazı özelliklerinden bahsedelim:

* Genel bulut, kullanıcıların (tenant’ların) bilişim kaynaklarını paylaşmasını sağlayan **sanallaştırılmış çok kiracılı (multi-tenant)** bir mimaridir ve **güvenlik duvarlarının (firewall) dışında** yer alır.
* Bulut sağlayıcısının altyapı, platform ve yazılım dâhil kaynak havuzu, tek bir tenant veya kuruluşun kullanımına  **adanmış değildir** .
* Kaynaklar ihtiyaç oldukça dağıtılır ve çeşitli abonelik ile **pay-as-you-go** modelleri üzerinden sunulur.

![1765803980330](image/7_PublicCloud/1765803980330.png)

---

## ✅ Genel Bulutun Faydaları

Genel bulutların önemli faydaları vardır; burada bazılarını ele alacağız:

Talep üzerine çok geniş kaynaklar mevcuttur; bu da uygulamaların talepteki dalgalanmalara sorunsuz biçimde yanıt vermesini sağlar.

Merkezî bulut kaynaklarını talep üzerine paylaşan çok sayıda kullanıcı göz önüne alındığında, genel bulut en büyük ölçek ekonomilerini sunar.

Genel bulutta mevcut sunucu ve ağ kaynaklarının çokluğu, genel bulutu **yüksek erişilebilir** kılar—bir fiziksel bileşen arızalansa bile hizmet, kalan kullanılabilir bileşenlerde etkilenmeden çalışmaya devam eder.

![1765804011614](image/7_PublicCloud/1765804011614.png)

---

## ⚠️ Güvenlik ve Veri Egemenliği Kaygıları

Genel bulutlarla ilgili kullanıcıların bazı endişeleri olduğunu da belirtmek önemlidir—bunların başında **güvenlik** ve **veri egemenliği (data sovereignty) uyumluluğu** gelir.

Veri ihlalleri, veri kaybı, hesap ele geçirilmesi, yetersiz durum tespiti (due diligence) ve sistem ile uygulama zafiyetleri gibi güvenlik sorunları, kullanıcıların genel buluttaki güvenliğe ilişkin sürdürdüğü endişelerden bazıları gibi görünmektedir.

Verilerin farklı konumlarda saklanması ve ulusal sınırlar üzerinden erişilmesiyle birlikte, şirketlerin verilerin depolanması, aktarımı ve güvenliğiyle ilgili veri egemenliği düzenlemelerine uyumlu olması giderek daha kritik hâle gelmiştir.

Bir hizmet sağlayıcının yalnızca düzenlemelere ayak uydurabilmesi değil, aynı zamanda bu düzenlemelerin yorumlanmasına da uyum sağlayabilmesi, birçok işletmenin paylaştığı bir endişedir.

![1765804049752](image/7_PublicCloud/1765804049752.png)

---

## 🧪 Genel Bulut için Yaygın Kullanım Senaryoları

Genel bulut için bazı yaygın kullanım senaryolarına bakalım:

Kuruluşlar, ekiplerinin uygulama geliştirme ve test etmeye odaklanabilmesi ve ürün ile hizmetleri için pazara çıkış süresini (time-to-market) azaltabilmesi amacıyla giderek daha fazla bulut tabanlı uygulama ve platformlara erişmeyi tercih etmektedir.

Kapasite ve kaynak ihtiyacı dalgalanan işletmeler genel bulutu tercih etmektedir.

Kuruluşlar, felaket kurtarma (disaster recovery), veri koruma (data protection) ve iş sürekliliği (business continuity) için ikincil altyapılar oluşturmak amacıyla genel bulut bilişim kaynaklarını kullanmaktadır.

Daha fazla kuruluş, daha yüksek erişilebilirlik, kolay dağıtım ve verilerini yedeklemek için bulut depolama ve veri yönetimi hizmetlerini kullanmaktadır.

BT departmanları, daha az kritik ve standartlaşmış iş platformları ve uygulamalarının yönetimini pubic cloud sağlayıcılarına dış kaynak olarak devretmektedir.

![1765804114156](image/7_PublicCloud/1765804114156.png)

---

## 🎬 Sonraki Video

Bir sonraki videoda, **private cloud** modeline; özelliklerine, faydalarına ve bazı kullanım senaryolarına bakacağız.
