# 🔐 Gizli Bilgilerin Güvenli Şekilde Saklanması

## 🎯 Video Hedefleri ve Secrets Management Tanımı

Gizli Bilgilerin Güvenli Şekilde Saklanmasına hoş geldiniz!

Bu videoyu izledikten sonra şunları yapabileceksiniz:  *secrets management* 'ı açıklamak, Vault'u tanımlamak ve Vault'un dört aşamasını belirlemek.

Önce şunu soralım: *Secrets management* tam olarak nedir?

 *Secrets management* , gizli tutulması gereken tüm ögelerin saklanması ve yönetilmesidir. İster şirket içi ( *on-premises* ) ister bulutta olsun, kodunuzu olası saldırılardan korumak için bu gizli bilgileri güvence altına almalısınız.

Gizli bilgilere örnek olarak parolalar, sertifikalar ve uygulama programlama arayüzü ( *API* ) şifreleme anahtarları verilebilir.

---

## 📦 Gizli Bilgileri Saklarken Karşılaşılan Zorluklar

Bu varlıkları, uygulamalarınız ve veritabanlarınızla yönetmek ve entegre etmek için bir *secrets management* çözümü kullanarak saklayabilirsiniz.

Gizli bilgileri saklarken çeşitli zorluklarla karşılaşacaksınız. Özellikle, aşağıdaki tür erişimleri yönetebilecek kodlar geliştirmeniz gerekir: ara katman uygulamalar ve kodlarla etkileşim için veritabanı erişimi ve ayrık ( *decoupled* ) uygulamalarla iletişim kurmak için servis odaklı mimari mesajlaşması ( *SOA messaging* ).

Bulut tabanlı bir uygulama geliştiriyorsanız, bulut tabanlı hizmetler de ilginizi gerektirecektir. Kimlerin hangi kaynaklara eriştiğini izlemek ve takip etmek için denetim ( *auditing* ) ve günlükleme ( *logging* ) hayati öneme sahiptir.

Ve depolamanızı saldırganlara karşı güvenli hâle getirmelisiniz.

---

## 🧰 Vault Nedir?

Peki, bu zorluklarla nasıl başa çıkabilirsiniz? Kullanabileceğiniz araçlardan biri Vault'tur.

Hashicorp tarafından geliştirilen Vault, gizli bilgileri yönetmek için belirteç ( *token* ) tabanlı bir depolama çözümüdür. Vault'a erişmek için kullanıcıya bir token atanır veya kullanıcı kendi token'ını oluşturur.

Kullanıcılar bir Vault sunucusu ile etkileşime girdiğinde Vault, kullanıcı erişimini ve ayrıcalıklarını kısıtlayan politikalar sağlar.

Vault'un üç farklı sunum şekli (versiyonu) vardır. Açık kaynak, kendi kendini yöneten Vault sürümü, yeni geliştiriciler ve küçük kuruluşların indirip denemesi için idealdir.

Bu çözüm, Vault'u nasıl çalıştıracağınızı ve yöneteceğinizi öğrenmenize yardımcı olur.

İkinci olarak, kurumsal ( *enterprise* ) çözüm de kendi kendini yöneten bir sürümdür ve özel dağıtımlar için özelleştirilebilir.

Üçüncü sunum ise bulutta yönetilen bir çözümdür. Hashicorp bu çözümü bulutta bir yazılım-hizmet olarak ( *SaaS* ) çözümü şeklinde yönetir.

---

## ✅ Vault Kullanmanın Faydaları

Vault'u bir *secrets management* aracı olarak kullanmanın dört faydası şunlardır:

Vault, kriptografik anahtarlar ve diğer gizli varlıkların yönetimini merkezîleştiren bir anahtar yönetimi ( *key management* ) sunar.

Ayrıca Vault, depolanan yazılı verileri şifreleyerek bir şifreleme-hizmet olarak ( *EaaS* ) çözümü sağlar.

Buna ek olarak Vault, veritabanı kimlik bilgisi döndürme ( *database credential rotation* ) uygulayarak aynı anda birden fazla veritabanını güvence altına alabilir.

Veritabanı kimlik bilgisi döndürme, veritabanı kimlik bilgilerini atar ve periyodik olarak değiştirir; bu da güvenliği artırır.

Ayrıca Vault, şirket içi ya da bulut ortamında güvenli soket katmanı ( *SSL* ) sertifikaları gibi kod geliştirirken ihtiyaç duyduğunuz gizli bilgileri yönetmenize ve saklamanıza yardımcı olur.

---

## 🛡️ Vault'un Dört Güvenlik Aşaması

Peki, Vault'un güvenlikle ilgili dört aşaması vardır.

İlk olarak kimlik doğrulama ( *authentication* ): Kullanıcılar, Vault ile etkileşime girmeden önce dahili veya harici bir sistemle kimlik doğrulamasından geçmelidir. Bu ek önlem, depolanan gizli bilgilere erişimin güvenliğini artırır.

Kullanıcının kimliği doğrulandığında Vault ona bir oturum başlatmak için kullanabileceği bir token verir.

İkinci aşama doğrulama ( *validation* ) aşamasıdır. Güvenilir bir üçüncü taraf, kullanıcının kimlik bilgilerinin doğrulanması adımını destekler.

Üçüncü aşama ise yetkilendirme ( *authorization* ) aşamasıdır. Oturumu yetkilendirmek için Vault, güvenlik politikalarını ilgili kullanıcılarla eşleştirir.

Dördüncü aşama ise Vault'a erişimdir. Kullanıcıya, tanımlanmış ve kendisine atanmış politikalara göre gizli bilgilere erişim izni verilir.

---

## 🖥️ Vault ile Etkileşim Yöntemleri: GUI, CLI ve HTTP API

Gizli bilgileri saklamak ve yönetmek için Vault ile etkileşime geçerken üç yaygın yöntemden birini kullanabilirsiniz.

Bu yöntemler şunlardır: grafiksel kullanıcı arayüzü ( *GUI* ), komut satırı arayüzü ( *CLI* ) ve Hiper Metin Aktarım Protokolü uygulama programlama arayüzü ( *HTTP API* ).

Dolayısıyla, kimlik doğrulamak, *unseal* işlemini gerçekleştirmek ve politikaları ile secret engine'lerini yönetmek için web tabanlı bir GUI kullanabilirsiniz.

GUI'yi etkinleştirmek için, Vault sunucu yapılandırmasında `ui` konfigürasyonunu `true` olarak ayarlamanız yeterlidir. Örneğin, `ui = true`.

Ayrıca GUI'ye buradan erişebilmek için en az bir *listener* adresinizin ve tanımlı bir portunuzun olması gerekir.

Bu durumda Vault, `localhost` üzerinde 8200 portunda çalışmaktadır. Bu örnekte GUI, `https://127.0.0.1:8200/ui` adresi üzerinden erişilebilirdir.

Vault'a ayrıca komut satırı arayüzü ( *CLI* ) üzerinden de erişebilirsiniz.

---

## 💻 CLI ve HTTP API ile Vault Sunucusuna Erişim

Vault'u yerel makinenize indirip kurduktan sonra, aşağıdaki komutu çalıştırarak Vault'u varsayılan yapılandırmalarla geliştirme modunda ( *development mode* ) başlatın:

```bash
$ vault server -dev &
```

Bu komut, Vault sunucusunu arka planda çalıştırır; böylece Vault komutlarını kullanabilirsiniz.

Komut yapısı; önce Vault komutlarının, ardından seçeneklerin ( *options* ), sonra yolların ( *paths* ) ve son olarak argümanların geldiği bir sırayı izler.

Vault sunucusunun tamamına, `/v1/` öneki kullanılarak HTTP API üzerinden erişilebilir.

Vault'u çalıştırmak için bir istemci ( *client* ) token'ı gerekli olduğundan, kullanıcıya `X-Vault-Token` HTTP başlığı ve bir *Bearer* token aracılığıyla bir client token gönderilmelidir.

Bir token alındığında, `localhost` üzerinde 8200 portunda çalışan bir Vault sunucusunda `alice` için saklanan gizli bilgiyi almak üzere bu `curl` komutunu çalıştırabilirsiniz.

Bir Vault sunucusunu kurup başlattığınızda, bir gizli bilgi ( *secret* ) yazmaya başlayabilirsiniz. Bu örnek, yeni kurulan ve çalışan bir Vault sunucusuna Python kullanarak nasıl secret yazılacağını göstermektedir.

---

## 🐍 Python ile Secret Yazma Örneği

Kare (`#`) sembolüyle başlayan ilk satır bir açıklama ( *comment* ) ifadesidir: Bu açıklama, yazma işleminin `secret/myapp` yolunun altında bir anahtar/değer ( *key/value* ) çifti içerdiğini belirtir.

Sonraki kod satırı bir yanıt ( *response* ) oluşturur. Bu satır, Vault API'nin `"create or update secret"` fonksiyonuna bir çağrı yapar; `path` parametresini `"myapp"` olarak ve `secret` parametresini anahtar olarak `'alice'`, değer olarak `'mypassword'` içeren bir sözlük ( *dictionary* ) olacak şekilde iletir.

Döndürülen değeri `response` adlı bir değişkende saklar. Yani önce bir açıklama satırı yazıp ardından secret ile bir response oluşturursunuz.

---

## 📖 Python ile Secret Okuma Örneği

Şimdi de Vault'tan bir secret okuma örneğine bakalım. Yine, kullandığınız kod Python'dur.

Kare (`#`) işaretiyle başlayan ilk satır, `secret/myapp` yolu altında yazılmış veriyi okuduğunuzu belirten basit bir açıklamadır.

Sonraki kod satırı, `path` parametresine `"myapp"` değeri verilerek Vault API'nin `"read secret version"` fonksiyonunu çağırır ve sonucu `read_response` değişkeninde saklar.

Bu satır, `"myapp"` yolunu isteyerek secret'ı getirir ve `alice` anahtarını kullanarak `secret/myapp` yolu altındaki değeri yazdırır.

Yazdırılan çıktı şudur:

`Value under path "secret/myapp" / key "alice": mypassword`

Bu çıktı, biçimlendirilmiş hâliyle `alice` anahtarıyla ilişkili `"mypassword"` değerini getirmek içindir.

---

## 📚 Özet

Bu videoda şunları öğrendiniz:

* *Secrets management* , parolalar gibi gizli tutulması gereken ögelerin saklanması ve yönetilmesidir.
* Kod geliştirirken karşılaşılan zorluklar arasında erişilebilirlikler, denetim ve günlükleme ile güvenlik yer alır.
* Vault, gizli bilgileri saklamak için token tabanlı bir çözümdür.
* Ve Vault'un dört aşaması; kimlik doğrulama ( *authenticate* ), doğrulama ( *validation* ), yetkilendirme ( *authorize* ) ve erişim ( *access* ) şeklindedir.
