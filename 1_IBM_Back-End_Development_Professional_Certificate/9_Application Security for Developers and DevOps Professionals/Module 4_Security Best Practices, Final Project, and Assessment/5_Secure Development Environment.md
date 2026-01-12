# 🛡️ Güvenli Geliştirme Ortamı

## 🎯 Bu Dersten Sonra Neler Yapabileceksiniz?

Güvenli Geliştirme Ortamına hoş geldiniz! Bu videoyu izledikten sonra şunları yapabileceksiniz:

* Güvenli bir geliştirme ortamını tanımlamak.
* Güvensiz bir geliştirme ortamına neyin sebep olduğunu açıklamak.
* Güvenli bir geliştirme ortamı uygulamak için en iyi uygulamaları özetlemek.

## ⚠️ Ops Katılımı Olmadan Geliştirilen Uygulamalar

Geliştirilmekte olan uygulamaların, tasarım ve geliştirme aşamasında güvenlik hesaba katılmadan kodlanması oldukça yaygındır. Genellikle olan şudur: Tamamlanan bir uygulama, üretim ortamına dağıtılması için Operasyon ekibine verilir, uygulama saldırıya uğrar ve Operasyon ekibi sunucuları kapatmak zorunda kalır. Operasyon ekibinden güvenlik girdisi alınmadan geliştirilen uygulamalar, siber saldırılara son derece açık hale gelir.

## 💸 Güvenliği Son Dakikaya Bırakmanın Maliyeti

Kesinti süresinin maliyetini, güvenlik açıklarını düzeltme maliyetini, olası bir veri ihlali veya sızıntısını ve kuruluşunuzun itibarını hesaba kattığınızda, uygulama geliştirmede güvenliğin son dakikada alınacak bir karar olmaması gerektiği netleşir.

## 🤝 Güvenlik Ekibinin Erken Dahil Edilmesi

Bunun kuruluşunuzda yaşanmasını, güvenlik ekibini yazılım geliştirme sürecinin erken aşamalarına dâhil ederek önleyebilirsiniz. Tasarım aşamasının başında güvenlik ekibiyle sağlam bir iş birliği kurun. Kodunuzu en baştan itibaren güvenli biçimde yazmaya başlamak kritik önemdedir. Ancak güvenli kod yazmak tek başına yeterli değildir. Geliştirme ortamının da güvenli olması gerekir. Geliştirme sistemleri ve platformları da üretim makineleriyle aynı tür saldırılara karşı savunmasızdır.

## 🧱 Ortamı Sertleştirmek ve Güvenlik Ekibine Güvenmek

Tehdit aktörlerini dışarıda tutmak için ortamı sertleştirmeniz gerekir. Bunun için Güvenlik ekibine güveniriz. *DevOps* ile nasıl güvenli bir uygulama geliştirileceğini anlayalım. Güvenli geliştirme teknikleri konusunda pratik bilgi ve anlayış olmadan, kodunuzun saldırılara dayanabilmesi pek olası değildir.

Herkes, güvenli uygulama geliştirmeyi ve uygulamaların geliştirildiği ve dağıtıldığı ortamların güvence altına alınmasını ne kadar önemli olduğunu anlamalıdır. Ortam güvenli değilse, buradan çıkan kodun da güvenli olduğunu kabul etmek zordur. Güvenlik bir ekip işidir.

## 👥 Güvenlikten Kim Sorumlu?

*DevOps* ekibindeki herkes güvenlikten sorumludur. Uygulamaya, onun servislerine ve üzerinde çalıştığı platforma temas eden herkes ve her şey; tasarımdan dağıtıma ve üretim ortamına kadar güvenlikten sorumludur.

*DevOps* ve Güvenlik ekiplerinin birleşen yetenekleri, savunmacı kod geliştirme ve üzerinde çalıştıkları sistemlere yönelik riskler konusunda daha derin bir anlayış sağlar.

## 🌐 Güvenli Geliştirme Ortamı Nedir?

Güvenli bir geliştirme ortamı; hem kurum içi ( *on-premise* ) hem de bulutta ağın, işlem kaynaklarının ve depolama aygıtlarının güvence altına alınmasını içeren, süreklilik arz eden bir süreçtir.

Geliştirme ortamınızı güvence altına almak, şu girişimlerde bulunmaya çalışan bir saldırganın riskini azaltır:

* Şifreleme ve erişim anahtarları gibi hassas bilgileri veya fikri mülkiyeti çalmak.
* Bilginiz olmadan projenize kötü amaçlı kod gömmek.
* Sisteminizi, derleme ve dağıtım hattınıza (build and deployment pipeline) veya ağdaki diğer makinelere yönelik başka saldırıları başlatmak için bir araç olarak kullanmak.

## 🛠️ Ortamı Sertleştirme Süreci

Süreç şunları içerir:

* Tüm yazılımları güncel tutmak.
* Gereksiz servisleri kaldırmak veya devre dışı bırakmak.

Geliştirme makinelerini fiziksel olarak güvence altına almak ve kodlama ile iş amaçlı kullanım için ayrı makineler kullanmak önemlidir.

İşle ilgili işlevler için sanal bir makine, bir *Docker* konteyneri veya ayrı bir bilgisayar kullanın ve oltalama ( *phishing* ), kötü amaçlı yazılım saldırıları ve diğer siber tehditleri azaltmak için kodunuzu sertleştirilmiş bir sistem üzerinde geliştirin.

Ben tüm geliştirmemi *Docker* konteynerlerinde yapıyorum; böylece her kod yazmaya başladığımda yalıtılmış ve bilinen bir ortama sahip oluyorum. Ve proje depolarım, ekipteki her üyenin de aynı konteynerize ortamı kullanabileceği şekilde yapılandırılmış durumda.

Yapmanız gereken diğer şeyler arasında karmaşık parolalar kullanmak, parolaları sık sık değiştirmek ve çok faktörlü kimlik doğrulama ( *multifactor authentication* ) uygulamak bulunur. Kod deponuzu koruyun ve derleme ile geliştirme hattınızı (pipeline) güvence altına alın.

## 📈 İzleme, Günlükleme ve Sürekli Test

İzleme ( *monitoring* ), günlükleme ( *logging* ) ve denetim ( *auditing* ) kontrollerine yatırım yapmanız gerekir. Ayrıca güvenlik için sürekli testler yapmalı ve güvenlik kusurları için planlama yapmalısınız.

## ⚙️ Güvensiz Geliştirme Ortamı Nedir?

Peki, güvensiz bir geliştirme ortamı nedir? Şöyle bir ortamdan bahsediyoruz:

* Üretim sistemleri güvenlidir, ancak kodun oluşturulduğu ve dağıtıldığı geliştirme ortamı, üretim altyapısına doğrudan bağlantıları olan, kuralsız ( *free-for-all* ) bir ortamdır.
* Geliştirme makineleriniz ele geçirilirse, üretim ortamınız da ele geçirilmiş olur.
* Geliştirme ortamında kritik süreçler eksik olabilir.
* Geliştirme ortamında koruyucu izleme, günlükleme veya denetim mekanizmaları yoksa, bir saldırının gerçekleşip gerçekleşmediğini, gerçekleştiyse ne zaman gerçekleştiğini veya başka güvenlik açıklarının bulunup bulunmadığını tespit etme imkânı yoktur.
* Saldırganlar kuruluşunuza sızabilir ve aylarca, hatta daha uzun süre fark edilmeden kalabilir.

## 🦠 Zararlı Yazılımlar ve Onaysız Depolar

Son olarak, geliştirme sistemlerinizde güncel bir antivirüs veya anti-malware ürünü kurulu değilse, geliştirme makineleriniz ve üzerlerindeki herhangi bir kod; oltalama, kötü amaçlı yazılım ve diğer saldırılara karşı savunmasız hale gelebilir.

Onaylanmamış kod depolarına sınırsız erişim ve kod edinmeye yönelik yönetişim veya politikaların eksikliği, şüpheli yazılım bağımlılıklarının uygulamanıza girmesine yol açabilir.

## ✅ En İyi Uygulamalarla Geliştirme Ortamını Güvenceye Almak

Geliştirme ortamınızı güvence altına almak için uygulayabileceğiniz bazı en iyi uygulamalar şunlardır.

### 🌍 İnternet Bağlantısını Güvenli Hale Getirmek

İnternet bağlantısını güvenli hale getirin. Güvensiz ağlar, ağ saldırılarına son derece açıktır.

Güvenli bir internet bağlantısını şu şekilde sağlayabilirsiniz:

* Açık portları düzenli olarak kontrol etmek ve ihtiyaç duyulmayan portları kapatmak,
* İzin verilen trafik dışında hiçbir şeye izin verilmediğinden emin olmak için sıkı giriş ( *ingress* ) ve çıkış ( *egress* ) trafik politikalarına sahip güvenlik duvarları yapılandırmak.

Bu noktada *Docker* konteynerlerinde geliştirme yapmak gerçekten yardımcı olur; çünkü konteynerler, geliştirme bilgisayarınızdan ayrı, yalıtılmış bir ağdadır ve tüm portlar varsayılan olarak dışarıya kapalıdır.

### 🔐 Çok Faktörlü Kimlik Doğrulama ve Kimlik Hırsızlığına Karşı Koruma

Kimlik hırsızlığına karşı korunmak için çok faktörlü kimlik doğrulama uygulamalısınız. Yalnızca parolalar yeterli değildir. Sadece parolalara bel bağlamak, sisteminizi saldırıya uğrama konusunda yüksek risk altında bırakır.

Ayrıca, parola ele geçirilirse, diğer varlıklarla birlikte tüm kodunuz da risk altına girer. Çok faktörlü kimlik doğrulama, saldırganın bir geliştiricinin yetkilerini kullanmasını da engeller.

Gizli bilgileri ( *secrets* ) de çok faktörlü kimlik doğrulama ile güvence altına alabilirsiniz. Bu da onların çalınmasını engeller ve kaybedilme riskini azaltır.

### 🏭 Üretim Sistemlerine Erişim için Ek Güvenlik

Son olarak, geliştirici makinelerinden üretim sistemlerine erişmesi gereken geliştiriciler için ek güvenlik önlemleri ekleyin.

Geliştiricilerin ortamlarını izlemelisiniz, ancak geliştiricilerin ortamlarını ve aktivitelerini izlemek, yaptıkları her şeyi gözetlemek anlamına gelmez. Geliştirici makineleri, işi yapmak için gerekli kaynaklara erişime hâlâ izin verirken, mümkün olduğunca sıkı şekilde kilitlenmelidir.

Bu konuda bana güvenin; aksi takdirde geliştiriciler, güvenlik kontrollerini aşmak için “geçici çözümler” ( *workaround* ) kullanmaya başlar ve makinelerini saldırılara karşı savunmasız bırakırlar.

### 📡 Günlük Güvenlik Alışkanlıkları ve Kayıt Tutma

Günlük güvenlik alışkanlıkları ve davranışları edinin. Şüpheli aktiviteleri izlemeli ve ziyaret edilen web sitelerinin şüpheli mi yoksa güvenli mi olduğunu kontrol etmek için ağ araçlarını kullanmalısınız.

Herhangi bir şey ters gittiğinde başvurmak üzere, ortamda geliştiriciler tarafından yapılan tüm commit’leri ve değişiklikleri takip edin.

## 🧩 Pre-Commit Hook’larıyla Hassas Verileri Engellemek

Ve  *pre-commit hook* ’ları kullanarak, geliştiricilerin kimlik bilgileri ( *credentials* ) gibi hassas verileri kod depolarına commit etmediklerinden emin olmak için kontroller dahi yapabilirsiniz.

## 📝 Özet: Bu Videoda Öğrendikleriniz

Bu videoda şunları öğrendiniz:

* Güvenliğin, yazılım geliştirme sürecinin dışında bırakılması veya yalnızca son dakika ele alınması yaygındır; bu da saldırılara son derece açık ve kuruluşunuzu riske atan yazılımlarla sonuçlanır.
* Güvenlik ve Geliştirme ekipleri arasındaki iş birliği, savunmacı kod geliştirme konusunda daha derin bir anlayış sağlar.
* Güvenlik, uygulamaya, geliştirme ortamına ve üzerinde çalıştığı platforma temas eden herkesin ve her şeyin sorumluluğudur.
* Bu bir ekip işidir.
* Açık portları, şüpheli davranışları ve eksik antivirüsü tespit etmek için ağınızdaki, geliştirici makinelerinizdeki ve üretim ortamınızdaki aktiviteleri izleyin.
* Parolaları korumak ve gizli bilgileri güvence altına almak için çok faktörlü kimlik doğrulama ve şifreleme ekleyin ve saldırganların geliştirici yetkileri elde etmesini engelleyin.
* Makinelerinden üretim sistemlerine erişmesi gereken geliştiriciler için ek güvenlik önlemleri ekleyin.
* Sorunlar ortaya çıktığında başvurmak üzere, geliştiriciler tarafından yapılan tüm commit’leri ve değişiklikleri takip edin.
