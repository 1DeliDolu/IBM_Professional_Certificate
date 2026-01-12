# 🏅 Golden Signals of Monitoring

Golden Signals of Monitoring’e hoş geldiniz! Bu videoyu izledikten sonra şunları yapabileceksiniz: İzlemenin dört *Altın Sinyali*ni tanımlamak ve *Altın Sinyallerin* önemini açıklamak. Dizüstü bilgisayarınızda çalıştığınızı ve bir mesajın belirdiğini hayal edin; bu mesaj pilinizin azaldığı konusunda uyarır. Hızla fişe takarsınız ve kapanmadan önce harekete geçersiniz. Bu uyarı sorunu tanımlar ve beklenmedik bir kapanmadan sizi kurtararak zaman kazandırır.

Şimdi benzer bir senaryoyu hayal edin. Geliştirdiğiniz uygulama doğru şekilde çalışmayı durdurur.

## 🧭 Sorunu Nasıl Belirlersiniz?

Sorunun ne olduğunu nasıl belirlersiniz? Uygulamalarınızı izlersiniz; böylece olası problemler için uyarıları takip edebilirsiniz. Uygulamanızı izleyerek, bir problemin nerede olduğunu belirleyebilir ve onu izole edebilirsiniz.

 *Altın sinyaller* , bir web uygulamasının metriklerini izlemek için altın standarttır. İster yerleşik bir *Application Performance Monitoring* (veya  *APM* ) aracınız olsun ister izlemeye yeni başlıyor olun, *altın sinyallere* odaklanmak uygulamanızın sağlığına dair bir genel görünüm elde etmenizi ve proaktif şekilde izlemenizi sağlar. Bir ekip sistem genelinde daha fazla metrik veya log izleyebilir; ancak dört  *altın sinyal* , etkili herhangi bir izleme stratejisinin temel, vazgeçilmez yapı taşlarıdır.

## ✨ Altın Sinyaller Nelerdir?

Bunlar, hizmetinizin veya sistemlerinizin sağlığını ölçmek için en önemli dört metriktir. “ *Latency* ”, “ *traffic* ”, “ *errors* ” ve “ *saturation* ” izleyerek bir sorunu belirleyip çözebilirsiniz; bazen sorun haline gelmeden önce bile.  *Altın Sinyaller* , tüm servislerin sağlığına odaklı bir görünüm sunar ve eyleme dönük izlemeyi mümkün kılar.

---

## ⏱️ 1) Latency

İlk *Altın Sinyal* olan  *latency* , bir isteğin gönderilmesi ile isteğin tamamlanması arasındaki süreyi ölçer. Bir kullanıcının bir sayfayı yüklemesi veya başka bir istekte bulunması ne kadar uzun sürerse, kullanıcının uygulamanızı bırakıp bir rakibe gitme olasılığı o kadar artar.

İsteklerin ortalama *latency* değerini ölçmek, bir web uygulamasının performansına kuş bakışı bir görünüm sağlar; ancak başarılı ve başarısız isteklerin ikisinin de  *latency* ’si olduğunu unutmayın. Bu nedenle ikisini de takip etmelisiniz. Örneğin, bir veritabanına yanıt hızlı görünebilir. Ancak daha yakından baktığınızda yanıtın aslında bir bağlantı kaybı hatası olduğunu, yani başarısız bir istek olduğunu görürsünüz. Ayrıca daha uzun *latency* sürelerine de bakmalısınız; çünkü bunlar daha yavaş bağlantı hatalarını gösterebilir. Uygulamanızın sağlığına dair eksiksiz bir genel bakış için, hata  *latency* ’lerini diğer tüm  *latency* ’lerle birlikte dahil etmek önemlidir.

Latency ölçerken iyi bir *latency* oranı hedefi belirlemeli ve sistemin sağlığını izlemek için başarılı istekleri başarısız olanlara karşı takip etmelisiniz. Gösterilen örnekte *latency* hedefi ayarlanmıştır. Sistem 1 bazen hedef  *latency* ’ye ulaşıyor ama her zaman değil. Bu, aralıklı bazı problemlere işaret edebilir. Grafik ayrıca sistem 2’nin hiçbir zaman hedef  *latency* ’ye ulaşmadığını gösterir; bu da onda ciddi bir sorun olduğunu belirtir. Bu verilerle, *latency* problemlerini çözmek için sistem 2’yi incelemeniz gerektiğini bilirsiniz.

---

## 🚦 2) Traffic

Bir diğer *Altın Sinyal* “ *traffic* ”tir. Genellikle  *traffic* , siteyi ziyaret eden kullanıcı sayısıyla ilişkilendirilir. Ancak uygulama izleme bağlamında “ *traffic* ”, hizmetinizin ne kadar talep gördüğünü ifade eder. *Traffic* ölçtüğünüzde kullanıcılarınızı daha iyi anlarsınız ve deneyimlerini ince ayar yapabilirsiniz.

*Traffic* izlemenin farklı şeyleri ölçebileceğinin farkında olmalısınız. Bir depolama sisteminde  *traffic* , saniye başına işlem sayısı veya saniye başına geri getirme sayısı olabilir. Web uygulamaları için, saniye başına toplam web sitesi isteği sayısını ölçebilirsiniz. Ayrıca sayfa veya kaynak bazında  *traffic* ’e de bakabilirsiniz; bu, hangi sayfalarınızın en başarılı olduğunu veya hangi sayfaların geliştirmeye ihtiyaç duyduğunu gösterir.

---

## ❌ 3) Errors

Üçüncü *Altın Sinyal* “ *errors* ”tur. Uygulamaları izlemenin başlıca nedenlerinden biri, kullanıcıları etkilemeden önce hataları bulup düzeltmektir. Bir hata, bir isteğin başarısız olması olabilir ya da bir isteğin tamamlanmasına rağmen yanlış bilgiyle tamamlanması anlamına gelebilir.

Sistem genelindeki tüm hataları ve tek tek servis seviyelerindeki hataları izleyerek hangi hataların kritik, hangilerinin daha az ciddi olduğunu tanımlamalısınız. Hataları takip ettiğinizde, sisteminizin sağlığını kullanıcının bakış açısından anlayabilir ve sık görülen hataları düzeltmek için hızlı aksiyon alabilirsiniz.

Açık hataları takip etmelisiniz. Bunlara *HTTP 500 Internal Server Error* gibi tüm sunucu hataları ve *HTTP 404 Page Not Found* gibi istemci hataları dahildir. Ancak yakalaması daha zor olabilecek diğer hatalara da dikkat etmelisiniz. Örneğin bir istek *HTTP 200 OK* durum kodu döndürebilir. Ancak istek doğru içeriği döndürmüyorsa, istek hatalı şekilde tamamlandığı için bu bir hata olarak kabul edilir.

Bu hataları da takip etmeli ve servis seviye hedeflerinizle ( *service-level objectives* ) eşleşecek şekilde hataları belirlemelisiniz.

---

## 📈 4) Saturation

Dördüncü *Altın Sinyal* “ *saturation* ”dur. Bu, bir sistemin kullanım yüzdesini ölçer; örneğin sisteminizin ne kadar bellek veya CPU kaynağı kullandığı gibi. Bir web uygulaması %100  *saturation* ’a yaklaşıyorsa, performans düşüşü muhtemeldir ve kullanıcılarınız olumsuz etkilenir. Öte yandan, *saturation* sürekli %50 veya daha düşükse, gereğinden fazla kaynak ayırıyor ve kullanmadığınız hizmetler için fazla ödeme yapıyor olabilirsiniz. Bir web uygulamasının  *saturation* ’ını ölçerek, kullandığınız servisleri nasıl optimize edeceğinize dair içgörüler elde edersiniz.

Bir kullanım hedefi ( *utilization target* ) belirlediğinizden emin olun; bu, servis performansını ve kullanılabilirliğini sağlamaya yardımcı olur. Ayrıca, *latency* artışının çoğu zaman  *saturation* ’ın öncü bir göstergesi olduğunun farkında olmalısınız.

---

## 🧩 Neden Altın Sinyaller?

Büyük sistemler çok fazla bileşen, sorun ve izlenecek uyarı ile karmaşık hale gelebildiğinden, dört  *Altın Sinyal* ’i kullanmak sizin için en iyisidir.  *Latency* ,  *traffic* , *errors* ve  *saturation* ’ı takip ettiğinizde, uygulamanızın en kritik performans göstergelerine odaklanabilir ve uygulamaları proaktif şekilde izleyebilirsiniz.

*Altın Sinyaller* ile şunları yapabilirsiniz: Bir sistemin bileşenlerinde sorun gidererek kök nedeni bulup problemleri düzeltmek. Ekibinizi bir olay hakkında uyararak sorunu tanımlamalarını ve düzeltmeye yönelik çalışmaları başlatmalarını sağlamak, ve Uygulamalarınız veya servisleriniz için kapasite planlamasına yardımcı olarak izlemeyi ve iyileştirmeyi desteklemek.

## 🧪 Örnek Senaryo

Şimdi izleme aracınızın, uygulamanız *App A* ile ilgili bir *latency* sorununu bildirdiğini hayal edin. Yüzlerce olasılığı gözden geçirmek yerine, sorunu belirlemek için dört  *Altın Sinyal* ’i kullanarak başlarsınız. Servis B’yi kontrol edersiniz, ancak servis herhangi bir sorun yaşamıyordur.

Ardından  *Altın Sinyaller* ’i kullanarak servis C’yi kontrol edersiniz. Beklendiği gibi çalışıyordur. Sonra servis D’yi kontrol edersiniz ve—eyvah—yüksek *saturation* seviyelerinin işaretlerini gösteriyordur.  *Altın Sinyaller* ’i kullanarak, servis D’nin muhtemelen  *App A* ’nın *latency* sorunlarının nedeni olduğunu hızla belirlersiniz ve gerekli adımları atarak sorunu, kullanıcılarınız fark etmeden önce bile düzeltebilirsiniz.

---

## 📝 Bu Videoda Öğrendikleriniz

Dört  *Altın sinyal* , uygulamanızın en kritik performans göstergelerine odaklanmanıza yardımcı olur. *Latency* izleme, bir hedef *latency* metriği belirlemenizi ve istek yanıtlarını ölçmenizi sağlar. *Traffic* izleme, hizmetinizin ne kadar talep gördüğünü ölçer ve kullanıcı deneyimini ince ayar yapmanıza yardımcı olur. *Errors* izleme, sisteminizin sağlığını kullanıcının bakış açısından anlamanıza yardımcı olur; böylece sık görülen hataları düzeltmek için aksiyon alabilirsiniz. Ve son olarak, *saturation* izleme, bir sistemin kullanım yüzdesini ölçer.
