# 💥 Arıza İçin Tasarlamak

Bu videoyu izledikten sonra, başarısızlığı kabullenmenin önemini fark edebilecek, başarısızlıktan hızlı toparlanmanın önemini açıklayabilecek, *retry* kalıplarının, *circuit breaker* kalıplarının ve *bulkhead* kalıplarının uygulamaları arızaya karşı dirençli hâle getirmeye nasıl yardımcı olduğunu anlatabilecek ve  *chaos engineering* ’i tanımlayabileceksiniz.

Uygulamanızı bir stateless mikroservisler koleksiyonu olarak tasarladığınızda, çok fazla hareketli parça olur; bu da çok şeyin ters gidebileceği anlamına gelir. Servisler zaman zaman yavaş yanıt verebilir veya hatta kesintiler yaşayabilir; bu yüzden ihtiyaç duyduğunuz anda her zaman erişilebilir olacaklarına güvenemezsiniz.

Umarız bu olaylar çok kısa ömürlüdür, ancak bağımlı bir servis yavaş çalışıyor diye veya belirli bir günde ağ gecikmesi çok yüksek diye uygulamanızın başarısız olmasını istemezsiniz. Bu yüzden uygulama seviyesinde arıza için tasarlamanız gerekir.

Başarısızlık kaçınılmaz olduğu için yazılımınızı arızaya dirençli olacak şekilde inşa etmeli ve yatay ölçeklenebilir hâle getirmelisiniz. Arıza için tasarlamalıyız.

---

## 🤝 Başarısızlığı Kabullenmek

Başarısızlığı kabullenmeliyiz. Başarısızlık tek sabittir.

Düşünce biçimimizi, başarısızlıktan nasıl kaçınacağımızdan, başarısızlık olduğunda onu nasıl tespit edeceğimize ve ondan nasıl toparlanacağımıza doğru değiştirmeliyiz. Bu, DevOps ölçümlerini “mean time to failure”dan “mean time to recovery”ye taşımamızın nedenlerinden biridir.

Mesele başarısız olmamaya çalışmak değildir. Mesele, başarısızlık olduğunda —ki olacaktır— hızlı bir şekilde toparlanabildiğinizden emin olmaktır.

Uygulama başarısızlığı artık yalnızca operasyonel bir endişe değildir. Geliştirme için de bir endişedir.

Uygulamanın dirençli veya esnek olması için geliştiricilerin bu dayanıklılığı en baştan itibaren inşa etmesi gerekir. Ve mikroservisler her zaman kontrol etmediğiniz servislere dış çağrılar yaptığı için, bu servisler özellikle sorunlara yatkın hâle gelir.

---

## 🚦 Throttling’e Hazırlıklı Olmak

Throttling’e hazırlanmayı planlayın. Buluttaki arka servislerinizden belirli bir hizmet kalitesi seviyesi için ödeme yaparsınız ve onlar da sizi bu anlaşmaya bağlı tutarlar.

Diyelim ki saniyede 20 veritabanı okumasına izin veren bir plan seçtiniz. Bu sınırı aştığınızda servis sizi throttle edecektir.

200_OK yerine 429_TOO_MANY_REQUESTS hatası alacaksınız ve bunu ele almanız gerekir. Bu durumda retry yaparsınız, değil mi, bu durumda. Bu mantığın uygulama kodunuzda olması gerekir.

Retry yaptığınızda, başarısız olduğunda üssel (exponential) şekilde geri çekilmek istersiniz. Amaç, zarif şekilde bozulmaktır ( *degrade gracefully* ).

Eğer yapabiliyorsanız, uygun yerlerde cache kullanın; böylece yanıt değişmeyecekse bu servislere her seferinde uzaktan çağrı yapmak zorunda kalmazsınız.

Uygulamaları dayanıklı hâle getirmenize yardımcı olan önemli stratejiler olan bir dizi kalıp vardır. Sadece popüler olanlardan birkaçını üzerinden geçmek istiyorum.

---

## 🔁 Retry Pattern

İlki  *retry pattern* ’dır. Bu, bir servise veya bir ağ kaynağına bağlanmaya çalışırken geçici başarısızlıkları ele almayı sağlar; işlemi şeffaf biçimde yeniden deneyerek ve işlemi başarısızlığa uğratarak.

Geliştiricilerin şunu söylediğini duydum: “Servisimi başlatmadan önce veritabanını deploy etmelisiniz çünkü servis başlarken veritabanının orada olmasını bekliyor.” Bu kırılgan bir tasarımdır ve cloud native uygulamalar için uygun değildir.

Veritabanı orada değilse, uygulamanız sabırla beklemeli ve sonra tekrar denemelidir. Bağlanabilmeli, yeniden bağlanabilmeli, bağlanamamalı ve tekrar bağlanabilmelisiniz.

Sağlam cloud native mikroservisleri bu şekilde tasarlarsınız.

Buradaki anahtar,  *retry pattern* ’dır: üssel olarak geri çekilmek ve her deneme arasında daha uzun gecikmek. Servisi bunaltacak şekilde arka arkaya 10 kez retry yapmak yerine, retry edersiniz, başarısız olur. Ve bir saniye beklersiniz, tekrar retry edersiniz.

Sonra 2 saniye beklersiniz, sonra 4 saniye, sonra 8 saniye. Her retry’da bekleme süresini, tüm denemeler tüketilene kadar bir katsayıyla artırırsınız ve sonra bir hata durumu döndürürsünüz.

Bu, arka servise başarısızlığa neden olan şeyden toparlanması için zaman tanır. Bu yalnızca geçici ağ gecikmesi de olabilir.

---

## 🔌 Circuit Breaker Pattern

*C*ircuit breaker pattern, evinizdeki elektrik devre kesicilerine benzer. Muhtemelen evinizde bir devre kesicinin attığını deneyimlemişsinizdir. Devrenin güç limitini aşan bir şey yapmış olabilirsiniz ve bu ışıkların sönmesine neden olur.

O zaman el feneriyle bodruma inip devre kesiciyi resetlersiniz ve ışıklar tekrar yanar. Bu *circuit breaker* kalıbı da aynı şekilde çalışır.

Bir problemi tespit etmek ve kademeli (cascading) arızaları önlemek için bu problem hakkında bir şey yapmak amacıyla kullanılır.

Kademeli arıza, bir servis erişilebilir olmadığında ve bunun diğer servislerin de başarısız olmasına neden olduğu durumdur. *Circuit breaker* kalıbıyla, kesiciyi attırarak bunu önleyebilir ve orijinal servis toparlanıp kesici tekrar kapanana kadar, alternatif bir yol üzerinden faydalı bir şey döndürebilirsiniz.

Çalışma şekli şudur: devre kesici kapalı olduğu sürece her şey normal akar. Devre kesici, belirli bir limite kadar başarısızlığı izler. O limit eşiğine ulaştığında, yani belirli bir eşiğe, devre kesici açılır ve bundan sonraki tüm çağrılar, korunan servisi hiç çağırmadan hata ile döner.

Sonra bir zaman aşımından sonra, bu yarı-açık (half-open) duruma girer ve servisle tekrar iletişim kurmayı dener. Başarısız olursa tekrar doğrudan açık duruma döner.

Ama başarılı olursa, yeniden tamamen kapalı hâle gelir.

---

## 🚢 Bulkhead Pattern

 *Bulkhead pattern* , başarısız olan servisleri izole ederek bir arızanın kapsamını sınırlamak için kullanılabilir.

Bu, ayrı thread pool’ların kullanılmasının, trafiği hâlâ aktif olan alternatif bir thread pool’a yönlendirerek başarısız bir veritabanı bağlantısından toparlanmaya yardımcı olabildiği bir kalıptır.

Adını, bir gemideki bulkhead tasarımından alır. Su hattının altındaki bölmelerin arasında “bulkhead” denen duvarlar vardır. Gövde delinirse sadece bir bölme suyla dolar.

Bulkhead, suyun diğer bölmeleri etkilemesini ve geminin batmasını engeller.

*Bulkhead pattern* kullanmak, bir servis arızası durumunda bir miktar işlevselliği korumalarına izin vererek tüketicileri servislerden kademeli arızalara karşı izole eder.

Uygulamanın diğer servisleri ve özellikleri çalışmaya devam eder.

---

## 🐒 Chaos Engineering

Son olarak *chaos engineering* vardır; diğer adıyla  *monkey testing* . Bir yazılım tasarım kalıbı olmamakla birlikte, tüm tasarım kalıplarınızın arıza altında beklendiği gibi çalıştığını kanıtlamak için iyi bir pratiktir.

 *Chaos engineering* ’de, diğer servislerin nasıl etkilendiğini görmek için servisleri bilerek öldürürsünüz. Netflix’in *The Simian Army* adlı, arıza oluşturan bir araç takımı vardır. *Chaos Monkey* yalnızca rastgele instance’ların sonlandırılmasını ele alır.

Netflix, sistemin tekrar ayağa kalkıp kalkmadığını ve sistemin zarif bir şekilde toparlanıp toparlanamayacağını görmek için rastgele şeyleri öldürür.

Üretimde bir şey gerçekten üretimde başarısız olana kadar, üretimde bir arızaya nasıl yanıt vereceğini bilemezsiniz. Bu yüzden Netflix bunu bilerek yapar.

---

## ✅ Bu Videoda Öğrendikleriniz

Bu kalıpların tümü, daha sağlam yazılım inşa etmenize ve aralıklı başarısızlıklara zarif bir şekilde yanıt vermenize yardımcı olabilir.

Bu videoda, başarısızlığın kaçınılmaz olduğunu öğrendiniz; bu yüzden başarısızlıktan kaçınmaya çalışmak yerine başarısızlık için tasarlarız. Geliştiricilerin hızlı toparlanabilmek için dayanıklılığı inşa etmesi gerekir.

 *Retry pattern* ’ları, başarısız işlemleri yeniden deneyerek çalışır.

 *Circuit breaker pattern* ’ları, kademeli arızaları önlemek için tasarlanmıştır.

 *Bulkhead pattern* ’ları, başarısız olan servisleri izole etmek için kullanılabilir.

 *Chaos engineering* , diğer servislerin nasıl etkilendiğini görmek için servislerin kasıtlı olarak başarısızlığa uğratılmasıdır.
