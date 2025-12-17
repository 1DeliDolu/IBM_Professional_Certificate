# 🧩 Mocking

Bu videoyu izledikten sonra şunları yapabileceksiniz:

* *Mocking* ’in ne olduğunu açıklamak
* Geliştiricilerin hangi durumlarda *mock* kullanması gerektiğini tartışmak
* *Mocking* için iki yöntemi tanımlamak:  *patch* ’ler ve  *mock object* ’ler

 *Mocking* ’i anlamak, yalnızca kendi kodunuzu test ettiğinizden (başka birinin sistemini değil) emin olmak için kritiktir.  *Mocking* , gerçek nesnelerin davranışını taklit eden nesneler oluşturma sürecidir.

Kendi kendinize “Neden bir şeyi  *mock* ’lamak isteyeyim?” diye sorabilirsiniz.  *Mocking* , kodunuzun bağımlı olduğu başka bir sistemi çağırdığı durumlarda çok faydalı olabilir. Örneğin, kodunuzun Internet Movie Database’den (IMDB olarak da bilinir) film yorumlarını işlediğini varsayalım. Bir test vakası çalıştırırken, gerçekten IMDB’yi saniyede 1000 kez çağırmak ister misiniz? IMDB sunucuları sizi saniyede 1000 kez çağırmanıza izin verir mi?

IMDB servisi kapalı olursa ne olur? Artık kendi hatanız olmamasına rağmen test vakalarınız çalışmaz. Bu yüzden testler sırasında bunun gibi sistemleri  *mock* ’lamak istersiniz. Test edilmeyen her türlü harici servisi  *mock* ’lamalısınız. Bunu yapmak için, o sistem gibi davranan  *mock object* ’ler oluşturursunuz. Onu  *mock* ’larsınız çünkü test ettiğiniz şey sistemin kendisi değildir; kodunuzun sistemi çağırıp çağıramadığını, veri geri alıp almadığını ve sonra bu veriyle bir şey yapıp yapmadığını test ediyorsunuz. Harici sistemi  *mock* ’lamak, testi yalnızca sizin kodunuza izole eder.

---

## 🎛️ Davranışı Kontrol Etme

Sistemi  *mock* ’layarak başka bir avantaj daha elde edersiniz. Bazen test edilen bağımlı bir sistemin davranışını değiştirmeniz gerekir. Diyelim ki IMDB veritabanını  *mock* ’ladınız. O zaman ihtiyacınız olan her tür yorumu göndermesini sağlayabilirsiniz: iyi yorumlar, kötü yorumlar, hatta hiç yorum olmaması.

Harici bir sistemi  *mock* ’layarak, o  *mock* ’lanmış sistemden geri dönen veri üzerinde tam kontrole sahip olursunuz. Bunu bir an düşünün.  *Mock* ’lanmış bir sistemin davranışını değiştirebilirsiniz. Onu başarısız olacak şekilde ayarlayabilirsiniz.

Kötü bir dönüş kodu getirmesini sağlayabilir ve hata yakalayıcılarınızın doğru çalışıp çalışmadığını kontrol edebilirsiniz.  *Mocking* , test etmeniz gereken herhangi bir koşulu oluşturmanıza imkân verir.

---

## 🌐 Yalnızca Harici Sistemlerle Sınırlı Değil

Ancak *mocking* yalnızca harici sistemlerle sınırlı değildir.  *Mocking* , test için önemli olan başka bir bileşene uzaktan bağlantınız yoksa da faydalıdır. Bu bileşen, uygulamanızın test sırasında kullanılamayan bir parçası da olabilir.

Kısacası, testlerinizi uzak bir bileşenden veya harici bir sistemden izole etmek istediğiniz her zaman, onun yerine geçecek bir *mock* kullanabilirsiniz.

---

## 🧰 Mocking Yöntemleri: Patch ve Mock Object

*Mocking* için iki tür yeni yöntem vardır.

### 🩹 Patch ile Mocking

Bir yöntem *patch* üzerinden yapılır: bir fonksiyon çağrısını  *patch* ’leyebilir ve çağrının davranışını değiştirmenizi sağlayabilirsiniz. Bu, hata koşullarını simüle etmek ve herhangi bir fonksiyon çağrısından neyin döneceğini kontrol etmek için güçlü bir araçtır.

“Herhangi bir fonksiyon” derken, üzerinde hiçbir kontrolünüz olmayan üçüncü taraf ( *third-party* ) kütüphaneleri de kastediyorum. *Patching* ile, bu kütüphanelere yapılan çağrıların davranışını kontrol edebilir ve farklı koşulları simüle edebilirsiniz.

### 🎭 Mock Object ile Mocking

Diğer yöntem, bir test çatısının ( *test framework* )  *mock object* ’i üzerinden yapılır; bu, tüm bir nesneyi  *mock* ’lar ve davranışını değiştirir. Bu  *mock* ’ların en iyi kullanımı, yalnızca bir fonksiyon çağrısı değil, başka bir nesne gibi davranan bütün bir nesneye ihtiyaç duyduğunuz zamanlardır.

Ayrıca, bir nesne döndüren bu sahte çağrıları da kullanabilirsiniz; yani çağrı, fonksiyon çağrısından dönmesini beklediğiniz nesne gibi davranan bir *mock object* döndürür.

Python’da bu  *mock object* ’lerden ikisi PyUnit’in içine gömülüdür: *Mock* ve  *MagicMock* .

*Patches* ve çatınızın sağladığı  *mock object* ’lerin bir kombinasyonunu kullanarak, test koşulları altında harici bağımlılıklar üzerinde tam kontrol sağlayabilir ve böylece tekrarlanabilir sonuçlar elde edebilirsiniz.

---

## 📌 Özet

Bu videoda şunları öğrendiniz:

* *Mocking* , gerçek nesnelerin davranışını taklit eden nesneler oluşturma sürecidir.
* Geliştiriciler, testleri uzak bir bileşenden veya harici bir sistemden izole etmek istediklerinde *mock* kullanmalıdır.
* Geliştiriciler, bir fonksiyon çağrısını  *patch* ’leyerek çağrının davranışını değiştirebilir.
* *Mock object* ’ler, tüm bir nesnenin yerine geçebilir ve o nesnenin davranışını değiştirebilir.
