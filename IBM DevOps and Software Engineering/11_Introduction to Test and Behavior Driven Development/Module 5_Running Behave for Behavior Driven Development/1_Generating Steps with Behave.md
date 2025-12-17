# 🧩 Adım Dosyalarını Behave ile Üretme

Bu videoyu izledikten sonra, Behave’i Python adımlarını üretmek için nasıl kullanacağınızı açıklayabileceksiniz. Behave aracının harika yanlarından biri, sizin için adımlar üretebilmesidir. Bunlar, yeni başladığınızda ilk adımlar olabilir ya da özellik senaryolarınız üzerinde çalışırken eksik olan herhangi bir adım olabilir. Sadece Behave’i feature dosyanıza karşı çalıştırın ve size eksik adımları gösterecektir.

Eğer hiç adım yazmadıysanız, Behave’i ilk kez çalıştırdığınızda tüm adımlar eksiktir. Durum buysa, Behave aslında geliştirme çabalarınızı bir dizi önerilen adımla başlatır. Bunun nasıl yapıldığını görelim. Bir feature dosyasıyla başlarsınız.

## 🐶 “Köpekleri Ara” Senaryosu (Kısa Sürüm)

Bu, “köpekleri ara” senaryosunun biraz daha kısa bir sürümüdür. Bu sürüm bir senaryo ve beş adım içerir. Bu feature dosyasını oluşturduktan sonra, Behave’i çalıştırırsınız.

## 🖥️ Behave Çıktısı ve Anlamı

Bunun gibi bir çıktı alırsınız. Bu çıktı çok fazla bilgi içerir, o yüzden üzerinden geçelim.

Behave, bu feature’ı hangi dosyada bulduğunu söyler. Bu, 1. satırdaki `pets.feature` dosyasıydı.

Ayrıca, feature dosyasında her senaryoyu bulduğu satır numarasını da söyler. “Köpekleri ara” senaryosu 7. satırdaydı.

Sonra Behave, TDD’nin *Red/Green/Refactor* sürecine benzer bir şey yapar. Bir adım geçtiğinde yeşildir ve başarısız olduğunda kırmızıdır, ancak burada adımlar sarıdır. Behave’de bu, ifadenin tanımsız olduğu anlamına gelir. Sağ tarafta Behave, adımı bulduğu step dosyası adını ve satır numarasını gösterir, ancak adım olmadığı için Behave sadece `None` yazdırır. İşte bu yüzden adım sarıdır.

O noktada Behave, senaryodaki diğer adımları atlar ve atlanan adımların hepsi mavidir. Benzer şekilde, bu adımların hiçbiri uygulanmamıştır; bu yüzden Behave yine adım konumu olarak `None` gösterir.

## 📌 Hatalı Senaryolar Özeti

Sonraki kısım, başarısız senaryoların ve Behave’in onları nerede bulduğunun özetidir. Bu durumda bir başarısız senaryo vardı. `features` klasöründe, 7. satırdaki `pets.feature` dosyasındaydı ve “Search for dogs” olarak adlandırılmıştı.

En altta; kaç feature’ın geçtiği, başarısız olduğu veya atlandığı; kaç senaryonun geçtiği, başarısız olduğu veya atlandığı; ve kaç adımın geçtiği, başarısız olduğu, atlandığı—ya da eksik olduğu özetlenir. Burada Behave, beş adımın tanımsız veya eksik olduğunu belirtir.

Bu özetteki her şey beklenendir; çünkü henüz hiçbir adım uygulamadığınızı biliyorsunuz.

## 🧱 Eksik Adımlar İçin Kod Parçacıkları

Çıktının geri kalanı aslında aradığınız şeydir. Behave size şunu söyler: “Tanımsız adımlar için adım tanımlarını bu parçacıklarla uygulayabilirsiniz.” Ardından, bir step dosyasına başlangıç noktası olarak kesip yapıştırabileceğiniz kod parçacıkları verir.

Her setin, adım türünü belirten uygun bir decorator anahtar sözcüğü içerdiğine dikkat edin: `Given`, `When` veya `Then`. Cümlenin geri kalanı, eşleştirme için string olarak geçirilir. Ayrıca, her uygulamanın yalnızca `NotImplementedError` istisnası fırlattığına dikkat edin.

Elbette bunları gerçek adım koduyla değiştirmeniz gerekir. Önemli nokta, bu çıktıyı kullanarak adımlarınız için bir başlangıç noktası sağlayacak bir step dosyası oluşturabilmenizdir. Bu şekilde tüm senaryolarınızın kapsandığını bilirsiniz.

## ✅ Özet

Bu videoda, Behave’in eksik tüm Python adımlarını raporladığını ve bunlar için kullanabileceğiniz kod parçacıkları önerdiğini öğrendiniz. Bu kodla, adımlar dosyanızı oluşturmak için bir başlangıç noktasına sahip olursunuz.
