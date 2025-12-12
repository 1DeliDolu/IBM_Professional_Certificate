# 🔐 Kod Uygulamaları

## 🎯 Öğrenme Hedefleri

Code Practices’e hoş geldiniz! Bu videoyu izledikten sonra şunları yapabileceksiniz: Kod uygulamalarını açıklamak. Genel kod uygulamalarını tanımlamak. Ve girdi doğrulama ile temizleme sürecini açıklamak.

Kod uygulamaları, güvenli yazılım geliştirilmesi için yazılım geliştirme sürecinin bir parçasıdır. Güvenlik, *DevOps* topluluğunda önemli bir endişe kaynağıdır, çünkü saldırganlar uygulama katmanındaki güvensiz kodları hedef alırlar.

Kod uygulamalarını hayata geçirmek, güvenli yazılım geliştirme sürecinin önemli bir parçasıdır ve geliştirme sürecinin erken aşamalarında uygulandığında maliyet açısından etkilidir, çünkü güvensiz kodu yazılım geliştirme sürecinin daha geç aşamalarında düzeltmek pahalıdır.

---

## ⚙️ Genel Kod Uygulamaları

Kod uygulamalarını uygulamak, zafiyetleri ve saldırıları azaltmaya yardımcı olur. Yazılım geliştirirken uymanız gereken bazı genel kod uygulamaları vardır.

Güvenli bir yazılım geliştirme yaşam döngüsü uygulayın. Geliştirme yaşam döngüsüne güvenliği dahil etmek, maliyet açısından etkilidir ve uygulamanızın en başından itibaren olabildiğince güvenli olmasını sağlar.

Güvenli kodlama standartları oluşturun. Bir dizi güvenli kodlama standardını takip etmek, iyi alışkanlıklar kazandırır.

Verimlilik sağlamak ve riski azaltmak için yeniden kullanılabilir nesne kütüphaneleri oluşturun ve kullanın.

---

## 🧩 Yönetilen Kod ve Güvenli Güncelleme

Yalnızca test edilmiş ve onaylanmış *managed code* (yönetilen kod) ile geliştirin.

Güvenli güncellemeyi, ifşa olmuş tehditlere veya güvenlik açısından kritik bileşenler içeren kaynak koda odaklanarak uygulamalısınız ve güvenli yazılım geliştirmeye odaklanan eğitim kurslarına katılın.

Bu kurslar, güvenlik farkındalığınızı artırabilir ve becerilerinizi güçlendirebilir.

---

## ✅ Girdi Doğrulama (Input Validation)

Girdiyi doğrulamak, (sunucu tarafında) kullanıcı veya saldırgan tarafından sağlanan girdinin, beklediğiniz şey olduğundan emin olmak anlamına gelir.

Peki neyi doğrulamalısınız? Bir saldırganın manipüle edebileceği, kullandığınız her türlü girdi verisini.

Girdi verinizi aşağıdakiler için kontrol edin:

* Beklenen veri türleri
* Veri aralığı ve veri uzunluğu
* "Beyaz" listeye göre izin verilen karakterler ( *allowed characters against a "white" list* )

Eğer girdi verisi doğru türde değilse reddedilmelidir. Güvenilmeyen kaynaklardan gelen herhangi bir veri de doğrulanmalıdır.

Yalnızca güvenilir ve sertleştirilmiş sistemlerde geliştirerek ilave riski azaltın. İzin verilen karakterler için her zaman *whitelist* (beyaz liste) doğrulaması yapılmalıdır.

Girdi verisi olarak girildiyse, herhangi bir kötü amaçlı karakteri temizleyin veya kaldırın.

---

## 🚫 Kötü Amaçlı Karakterler ve Ek Kontroller

Kötü amaçlı karakterler aşağıdakileri içerebilir:

```text
<>>"'%()&+\\'\"
```

Saldırganın, uygulamanızın amaçlanmayan bir şey yapmasına neden olmak için kullanabileceği her şey bu kapsama girer.

Bu kötü amaçlı karakterlerden herhangi biri gerçekten geçerli girdi olarak izin verilen karakterler ise,  *output encoding* , göreve özgü  *API* ’leri güvenli hale getirme ve tüm uygulama boyunca tüm veri girdisini hesaba katma gibi ek kontroller uygulamalısınız.

*Output encoding* (çıktı kodlaması), girdi kodunun güvenli çıktı koduna dönüştürülmesidir. Kullanılan her tür çıkış kodlaması için bir politika ve uygulama hayata geçirin.

Yorumlayıcı için güvensiz olanlar dışında tüm karakterleri kodlamalısınız. Ve  *SQL* , *XML* ve *LDAP* gibi güvenilmeyen sorguların tüm çıktısını temizlemelisiniz.

Ayrıca, güvenilmeyen verilerin yerel işletim sistemi komutlarına yönelik tüm çıktısını da temizleyin.

---

## 🧯 Hata Yönetimi ve Günlükleme (Logging)

Uygun olmayan hata işleme, bir uygulama için çeşitli güvenlik risklerini ortaya çıkarabilir. Çok fazla ayrıntı içeren hata mesajları, saldırganlara sömürebilecekleri potansiyel zayıflıklar hakkında değerli ipuçları sağlar.

Hedef, kullanıcıya anlamlı hata mesajları sağlamak, sorun gidermek için tanısal bilgiler sağlamak ve saldırgana hiçbir faydalı bilgi vermemek olmalıdır.

Hata işleme ve günlükleme (logging) için özel hata sayfaları ve genel mesajlar kullanın. Herhangi bir hata durumu meydana geldiğinde, bozulmayı önlemek için ayrılmış belleği serbest bırakın. Ve saldırganları dışarıda tutmak için günlük dosyalarına erişim kısıtlamaları uygulayın.

Ayrıca, girdi, kimlik doğrulama girişimleri ve erişim denetimi gibi her türlü kurcalama olayı ve hatasını da günlüğe kaydetmelisiniz.

---

## 📌 Bu Videodan Öğrendikleriniz

Bu videoda şunları öğrendiniz: *DevOps* topluluğunda güvenlik bir endişe kaynağıdır ve saldırganlar  *Application layer* ’daki (Uygulama katmanı) güvensiz kodları hedef alırlar.

Kod uygulamaları, zafiyetlerin ve saldırıların etkisini azaltmaya yardımcı olan güvenli yazılım geliştirmenin bir parçasıdır.

Geliştirme sürecine güvenliği erken dahil etmek para tasarrufu sağlar, çünkü güvenlik sorunlarını sürecin daha geç aşamalarında düzeltmek daha maliyetlidir.

Güvenilir kod kullanmak ve güvenilir, sertleştirilmiş sistemlerde geliştirme yapmak riski (veya saldırı yüzeyini) azaltır.

Veri girdisini doğrulayın ve güvenilmeyen sorguların çıktısını temizleyin.

Kullanıcılar için anlamlı hata mesajları, sorun gidermek için tanısal günlükler sağlayın ve mesajlarınızın saldırganlara hiçbir faydalı bilgi sunmadığından emin olun.

Ve güvenli yazılım geliştirmeye odaklanan eğitim kursları, farkındalığı artırmaya ve becerileri güçlendirmeye yardımcı olabilir.
