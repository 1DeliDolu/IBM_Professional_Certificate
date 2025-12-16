# 🧪 Neden Geliştiriciler Test Yazmaz?

Bu videoyu izledikten sonra şunları yapabileceksiniz: Geliştiriciler kodlarını test etmediğinde ortaya çıkan sorunları özetlemek ve test etmenin neden önemli olduğunu açıklamak.

Neden geliştiriciler test yazmaz? Verdikleri nedenlerden biri, kodun zaten çalıştığını bilmeleridir! Ama gelecekte kodunuz üzerinde çalışacak diğer insanları, hatta gelecekteki SİZ’i düşünün. Diyelim ki yeni kod yazdınız ve sonra yazılım çalışmadı. Orijinal kod üzerinde testleri çalıştırıp o kodun çalıştığından emin olamazlarsa bir şeyi bozup bozmadıklarını bilemezler.

Benim tavsiyem, bir proje için yeni bir deposu *clone* ettiğinizde, başka hiçbir şey yapmadan önce testleri çalıştırmanızdır. Tek bir satır kod yazmadan önce testlerin geçtiğinden emin olun.

Eğer bunu yapmazsanız, daha sonra kodun neden çalışmadığını anlamaya çalıştığınızda, onu sizin mi bozduğunuzu yoksa başka birinin depoya bozuk kod mu *check-in* ettiğini bilemezsiniz.

## 🕰️ Geleceği Düşünerek Test Etme

Test yazma konusunda bir diğer düşünce de geleceği hesaba katmaktır. Diyelim ki bir süre kod üzerinde çalışmayı bıraktınız ve başka bir projede çalıştınız. Sonra gelecekte geri döndünüz; kodu hangi durumda bıraktığınızı bilemeyeceksiniz.

Test senaryolarınız, sizin ve başkalarının neyin çalıştığını, neyin çalışmadığını ve kodun nasıl çağrılacağını bilmesine yardımcı olur. Kodun nasıl kullanılacağına dair örnekler olarak hizmet ederler.

## 🧱 “Bozuk Kod Yazmam!” Gerekçesi

Geliştiricilerin test yazmamak için verdiği bir başka neden de şudur: “Ben bozuk kod yazmam!”

Tamam, belki bozuk kod yazmıyorsunuz, ama sistem sizin altınızda sürekli değişiyor: güvenlik açıkları yamalanıyor ve yeni kütüphaneler yükseltiliyor.

Biri size, “Hey, şu Apache Struts kütüphanesinde bir güvenlik açığımız var. Tüm sunucularımızda bunu güncelleyebilir miyiz?” dediğinde… Kodunuzu test edecek ve yeni sürümle çalıştığını doğrulayacak test senaryolarınız yoksa, muhtemelen yapmamalısınız.

Kodunuzun o kütüphanenin yeni bir sürümüyle hâlâ çalışacağını test edebilene kadar yükseltme yapmamalısınız. Ve hızlıca “Evet, güncellenmiş sürüm çalışıyor. Üretime dağıtın.” diyebilecek durumda olmak istersiniz.

Aksi takdirde, sonuçlar felaket olabilir. Amerika’nın en büyük kredi raporlama kuruluşlarından biri olan Equifax’ı ele alın. Bir Apache Struts güvenlik açığını düzeltmeyi geciktirdiler; bilgisayar korsanları da bu açığı istismar etti. Sonuç? 147 milyon ABD vatandaşının kişisel, kimlik bilgileri ve finansal bilgileri çalındı.

## ⏳ “Vaktim Yok!” Gerekçesi

Geliştiricilerin test etmemek için verdiği bir başka neden de, “Vaktim yok!”tur.

Aslında bu en kötü bahanedir, çünkü test yazmak size zaman kazandırır. Şimdi birkaç test senaryosu yazmaya harcadığınız zaman, daha sonra saatlerce sürecek hata ayıklamadan sizi kurtaracaktır.

Test senaryolarına sahip olmak, kodunuzu *refactor* etmenize ve yeni özellikleri güvenle eklemenize imkân verir; çünkü test senaryoları herhangi bir gerileme ( *regression* ) hatasını yakalayacaktır. Bu da sonuçta çok daha hızlı çalışmanızı sağlar.

Test etmek uzun vadede gerçekten zaman (ve stres) kazandırır.

## 📦 Neden Testlere İhtiyacımız Var?

Peki neden testlere ihtiyacımız var? Çünkü kodunuzun nerede ortaya çıkacağını asla bilemezsiniz. O “Road Not Found Exception”a sebep olan geliştirici olmak istemezsiniz.

Ama cidden, artık birçok proje açık kaynak ve kodunuzun nasıl kullanılacağını asla bilemezsiniz. Kodunuz nasıl kullanılırsa kullanılsın, tam olarak beklendiği gibi davranacağından emin olmak istersiniz.

Bu, özellikle Python paketlerinizi PyPi’ye veya Java paketlerinizi Maven’a ya da herhangi bir  *artifact repository* ’ye gönderiyorsanız çok önemlidir.

Geliştiricilerin iyi test edilmiş koda güvenebilmesi gerekir. Paketinizi kimlerin kendi çözümlerine dahil edeceğini bilmiyorsunuz; bu yüzden kodunuzun sağlam olduğundan emin olmak istersiniz ve test senaryoları bunu yapmanıza yardımcı olur.

## ✅ Bu videoda şunları öğrendiniz:

* Test etmek, gelecekteki kod bozulmalarını ve uyumluluk sorunlarını önler.
* Test etmek, toplam geliştirme süresini azaltır.
* Test etmek, başkaları kullandığında kodunuzun beklendiği gibi davrandığını garanti eder.
