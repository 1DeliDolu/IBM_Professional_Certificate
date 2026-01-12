# 🌿 Final Project Walkthrough

React Final Project Walkthrough’a hoş geldiniz. Nihai projeniz için, bir *paradise nursery* alışveriş uygulamasının ön yüzünü (front end) oluşturacaksınız. Uygulama arayüzü, çeşitli ev bitkilerini incelemenize ve bunları bir alışveriş sepetine eklemenize olanak tanıyacaktır. Alışveriş sepeti özelliği, tüm ürünlerinizi ve toplam maliyetlerini görmenizi sağlar. Alışveriş sepetiniz ayrıca, ödeme öncesinde sepetteki ürün sayısını ayarlamanıza da izin vermelidir. Uygulamanızın üç sayfası olacaktır: bir açılış sayfası, bir ürün listeleme sayfası ve bir alışveriş sepeti sayfası. Şimdi uygulamayı önizleyelim ve kullanıcı deneyimini inceleyelim.

---

## 🏁 Açılış sayfası

Burada, Paradise Nursery alışveriş uygulaması için örnek bir açılış sayfası görüyorsunuz. Müşterilerinizi ürün hattınızla etkileyecek ve ana uygulamaya giriş sağlayacak, buna benzer bir açılış sayfası oluşturun. Bu sayfadaki öğeler şunları içermelidir: şirketiniz hakkında bir paragraf, bir arka plan görseli, şirket adınız ve ürün listeleme sayfasına bağlanan bir **Get Started** düğmesi.

---

## 🛒 Ürün listeleme sayfası

**Get Started** seçildikten sonra uygulama, aşağıda gösterilene benzer bir ürün listeleme sayfasına yönlendirmelidir. Bu sayfa, ürün hattınızdaki ev bitkilerini incelemenize olanak tanır. Sayfa öğeleri; bir sayfa başlığı ve her bitki için bir kart içerir. Sayfa, bitkileri hava temizleyici ( *air purifying* ) veya aromatik ( *aromatic* ) gibi ortak bir özelliğe göre gruplamalıdır.

Bazı bölümlerde tek bir bitki birden fazla grupta yer alabilir. Sayfa başlığı, açılış sayfasına geri yönlendirecek şirket adını ve logosunu içermelidir. Ayrıca bir slogan ( *tagline* ) ve mevcut ürün sayısını gösteren bir alışveriş sepeti simgesi de içermelidir. Sepet simgesini seçerseniz uygulama alışveriş sepeti sayfasına yönlenmelidir.

Her bitkinin, burada gördüğünüze benzer kendi kartı olmalıdır. Her kart; bir küçük resim (thumbnail), bitki adı, fiyatı, kısa bir açıklama ve **Add to Cart** etiketiyle bitkiyi sepete ekleme seçeneği içerir. Ürünü sepete eklerseniz, bu seçeneği devre dışı bırakın ve etiketi **Added to Cart** olarak değiştirin.

**Add to Cart** seçeneğini seçtiğinizde, sepet simgesindeki sayı bir artmalıdır. Şimdi, alışveriş sepeti sayfasına ve bileşenlerine bakalım.

---

## 🧾 Alışveriş sepeti sayfası

Alışveriş sepetini, ürün listeleme sayfasından sepete eklenen her bitki türü için bir kart olacak şekilde düzenlemelisiniz. Her kart; bir küçük resim görseli, bir silme seçeneği ve birim fiyatı göstermelidir. Ürün sayısını artırma veya azaltma düğmesiyle artırıp azaltabilirsiniz; bu düğmeler seçildiğinde kart üzerindeki sayı bir artar veya azalır. Ayrıca sepetteki toplam ürün sayısını da güncellemeniz gerekir. Kart, burada gösterildiği gibi o bitki türünün sayısına göre ara toplamı ( *subtotal* ) da göstermelidir.

Şimdi, alışveriş sepeti sayfasındaki diğer öğeleri ele alın. Sepetteki toplam bitki sayısını, tüm ürünlerin toplam maliyetini ve bir **Checkout** düğmesini belirgin şekilde gösterin. Ürün listeleme sayfasındakiyle aynı sayfa başlığını kullanın.

Kullanıcı olaylarının sonuçlarını ele almanız gerekecektir; örneğin sepetteki ürün sayısı sıfıra düştüğünde. Bu durum, ürün listeleme sayfasındaki devre dışı bırakılmış **Added to Cart** seçeneği gibi diğer öğeleri de etkiler. Ürün listeleme sayfasına geri döndüğünüzde, o ürünü tekrar seçebilmek için bu seçeneği yeniden etkinleştirmeniz gerekir. Ayrıca artırma ve azaltma düğmelerini kullanırken başlıktaki sepet simgesinde gösterilen ürün sayısını ayarlamayı da unutmayın.

---

## ✅ Son not

Bu uygulamayı geliştirmeden önce uygulama projesini tamamlamanızı öneriyoruz. Bu projede yazdığınız işlevselliklerin ve kodun büyük kısmı buna aktarılacaktır. Bu projeleri tamamladıktan sonra, kurs boyunca öğrendiğiniz birçok fikri tek bir uygulamaya uygularken kendinizi rahat hissedeceksiniz. İyi şanslar.
