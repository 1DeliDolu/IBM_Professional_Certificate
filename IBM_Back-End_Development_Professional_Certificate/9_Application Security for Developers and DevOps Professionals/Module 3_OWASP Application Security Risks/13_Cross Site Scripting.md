# 🛡️ Cross-Site Scripting

## 🎯 Video Hedefleri

Cross-Site Scripting’e hoş geldiniz!

Bu videoyu izledikten sonra şunları yapabileceksiniz: Cross-site scripting’i tanımlamak, cross-site scripting türlerini belirlemek ve cross-site scripting saldırılarını önlemenin yollarını açıklamak.

## 🔍 Cross-Site Scripting Nedir?

Cross-site scripting, bir uygulama güvensiz veriyi alıp uygun doğrulama veya kaçış ( *escaping* ) olmaksızın bir web tarayıcısına gönderdiğinde ortaya çıkar.

Saldırganlar cross-site scripting’i, kurbanın tarayıcısında betikler ( *scripts* ) çalıştırmak için kullanırlar.

Cross-site scripting’i `"XSS"` olarak temsil edilmiş şekilde görebilirsiniz.

## ⚠️ Cross-Site Scripting Saldırılarının Etkileri

Cross-site scripting farklı şekillerde saldırı gerçekleştirebilir. Örneğin, cross-site scripting saldırıları saldırganların kullanıcı oturumlarını ele geçirmesini sağlayabilir.

Bir cross-site scripting saldırısı, görselleri veya içeriği değiştirerek ya da kaldırarak web sitelerini tahrif edebilir.

Ve cross-site scripting, kullanıcıları güvenilir bir web sitesinden kötü niyetli bir web sitesine yönlendirebilir.

## 🧬 Cross-Site Scripting Türleri

Üç yaygın cross-site scripting saldırı türü vardır:  **stored** , **blind** ve  **reflected** .

### 💾 Stored (Persistent) XSS

Stored cross-site scripting saldırısı, bir betiğin, bir veritabanına veya hedeflenen bir sunucuya kalıcı olarak kaydedilecek şekilde enjekte edilmesidir.

Kurban, kötü amaçlı betiği aldığında, bu betik sunucuda depolanan bilgileri isteyebilir.

Stored cross-site scripting, **persistent cross-site scripting** olarak da adlandırılır.

### 👁️ Blind XSS

Sonra, blind cross-site scripting, bir uygulamanın arka ucunda ( *backend* ) kullanıcı veya yönetici tarafından, onların haberi olmadan yürütülecek bir payload içeren betiğin enjekte edilmesidir.

Bu payload, uygulamayı veya sunucuyu tehlikeye atabilir.

Hatta kullanıcıya saldırabilir.

### 🪞 Reflected XSS

Ve reflected cross-site scripting saldırısı, bir betiğin saldırıya uğrayan sunucudan sistemdeki kullanıcılara yansıtılacak şekilde enjekte edilmesidir.

Birçok kurbanı tehlikeye atabilecek kötü amaçlı bağlantılar içeren kimlik avı e-posta mesajları göndermek, reflected cross-site scripting saldırısına bir örnektir.

## 🛡️ Cross-Site Scripting’e Karşı Korunma Yöntemleri

Uygulamanızı cross-site scripting saldırılarına karşı aşağıdaki önleyici tedbirlerle koruyabilirsiniz.

Önlemlerden biri, şüpheli HTTP isteklerini ve bir betik motorunu tetikleyebilecek anahtar sözcükleri aramaktır.

İki örnek, yasaklanmış HTML etiketleri ve kaçış dizileridir ( *escape sequences* ).

Başka bir önleyici tedbir, şüpheli görünen liste veya anahtar sözcükleri kaçışla işlemek ( *escape etmek* ) ya da özel karakterleri engellemektir.

Bir web sunucusunda HTTP `TRACE` desteğini kapatmak, kullanıcı çerezlerini toplayıp bunları kötü niyetli bir sunucuya gönderebilecek HTTP `TRACE` çağrılarını ortadan kaldırmak için iyi bir fikirdir.

Ve web sayfalarındaki fonksiyonlar veya değişkenler olan güvensiz  *sinks* ’lerden kaçının.

Kodu, `innerHTML` gibi güvensiz *sink* referanslarını kaldırmak için yeniden düzenlemelisiniz (*refactor* etmelisiniz).

Ya da daha da iyisi, `textContext` veya `values` kullanın.

## 💻 Cross-Site Scripting Saldırısına Örnek

İşte bir cross-site scripting saldırısı örneği.

Burada saldırgan, başka bir siteden gelen bir betiği sizin sitenize enjekte edebilmektedir.

Buradaki kodda, `page` adlı bir değişken ve `+=` birleştirici ( *concatenator* ) bulunmaktadır.

Ve bu değişken, bir giriş alanı ( *input field* ) içeren bir HTML dizesine sahiptir; bu giriş alanının adı `credit card`, türü `text` ve değeri ise yine `request.getParameters("CC")` fonksiyon çağrısıdır.

Sorun şu ki, burada dizeleri birleştiriyorsunuz.

Bir kredi kartı numarası vermek yerine, bir saldırgan **JavaScript** girebilir!

Saldırgan, `"CC"` parametresini değiştirebilir ve bunun yerine bir `script` etiketi koyabilir.

Sonrasında `document.location`, saldırganın sitesine yapılan `CGI bin` çağrısında payload haline gelir.

Bu, kurbanın oturum kimliğinin ( *session ID* ) saldırganın web sitesine gönderilmesine neden olur; bu da saldırganın, kullanıcının mevcut oturumunu ele geçirmesine olanak tanır.

## 📌 Özet

Bu videoda şunları öğrendiniz:

* Cross-site scripting, bir uygulamanın güvensiz veriyi bir tarayıcıya göndermesi durumudur.
* Saldırganlar, cross-site scripting’i kurbanlarının tarayıcısında betikler çalıştırmak için kullanırlar.
* Üç yaygın cross-site scripting saldırısı  **stored** , **blind** ve **reflected** saldırılarıdır.
* Önleyici tedbirler arasında şüpheli HTTP isteklerini aramak, kaçış listelerini kullanmak, HTTP `TRACE`’i devre dışı bırakmak ve güvensiz  *sinks* ’lerden kaçınmak yer alır.
