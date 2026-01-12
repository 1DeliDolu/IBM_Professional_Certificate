# 🌿 Final Proje: Paradise Nursery Alışveriş Uygulaması

**Tahmini gerekli süre:** 1 saat

## 🧩 Giriş

Bu final projede, çeşitli ev bitkileri sunan çevrimiçi bir bitki mağazası için bir alışveriş sepeti uygulaması oluşturacaksınız.

Paradise Nursery alışveriş sepeti özellikleri şunları içerecektir:

* Ürün listeleme sayfasına bağlantı veren bir düğmeye sahip bir **Landing** sayfası
* Landing, ürün listeleme ve alışveriş sepeti sayfalarına bağlantılar içeren bir **navigasyon çubuğu**
* Her bitki için; görseli, adı, açıklaması, maliyeti ve **Add to cart** düğmesi ile bitkileri sergileyen bir **kart**
* O bölümdeki bitkileri açıklayan en az  **iki bölüm** . Örneğin, “Aromatic Plants” ve “Medicinal Plants”.
* Sepetteki ürünleri gösteren bir **cart** sayfası

Sepet şu özelliklere sahip olmalıdır:

* Sepetteki her bitki türü için bir kart
* Her kartta küçük görsel, birim maliyet, o türdeki tüm bitkilerin maliyeti ve miktarı artırıp azaltmaya yarayan düğmeler ile birlikte **Delete** düğmesi
* **Continue Shopping** ve **Checkout** düğmeleri

Bu final projede dinamik işlevleri uygulamak için alıştırma projesinde edindiğiniz bilgi ve becerileri kullanacaksınız. Bu nedenle final projeye başlamadan önce alıştırma projesini tamamlamanız önerilir. Örneğin, navbar ikonunda sepet miktarını göstermek ve kullanıcı ürün miktarını değiştirdiğinde toplam maliyeti güncellemek gibi özellikler final projenin bir parçası olacaktır.

## 📝 Not

1. Lütfen tüm dosyalarınızın güncellenip public GitHub deposuna gönderildiğinden ve deployed URL’nizin canlı ve public olarak erişilebilir olduğundan emin olun.
2. “Final Project Overview” kısmında belirtildiği üzere, proje teslimlerinizi **Option 1: AI-Graded Submission and Evaluation** veya **Option 2: Peer-Graded Submission and Evaluation** üzerinden gönderebilirsiniz.
3. **Option 1: AI-Graded Submission and Evaluation**
   Aşağıdaki proje dosyaları için public GitHub repository URL’lerini gönderin: **README.md, AboutUs.jsx, App.css, App.jsx, CartSlice.jsx, ProductList.jsx ve CartItem.jsx.** Proje kodunuz **e-plantShopping** adlı public bir GitHub repository’de saklanmalıdır.
4. **Option 2: Peer-Graded Submission and Evaluation**
   Peer değerlendirmesi için deployed uygulama URL’sini ve public GitHub repository URL’sini gönderin. Deploy ettiğinizde, live uygulama URL’sini not alın.

Lütfen şunlardan emin olun: Tüm proje dosyaları gönderimden önce commit edilip push edilmelidir. Uygulamanız deployed olmalıdır ve live URL mevcut olmalıdır. Uygulamanızı GitHub Pages veya seçtiğiniz başka bir hosting platformunda barındırabilirsiniz.

## 🎯 Öğrenme hedefleri

Bu lab’i tamamladıktan sonra şunları yapabileceksiniz:

* **React Components:** Component composition ve nesting kullanarak fonksiyonel React bileşenleri oluşturma.
* **State Management with Hooks:** Özellikle *useState* ve *useEffect* hook’larını uygulama. Elementlerin görünürlüğünü kontrol etmek için hook’larla component-level state yönetme.
* **Redux Integration:** Actions, reducers ve store gibi Redux kavramlarıyla bir uygulamaya Redux entegre etme.
* **Rendering Dynamic Data:** Object array’inden alınan veriyi UI’a dinamik olarak render etme. Listeler üretmek için array’ler üzerinde map kullanma.
* **Handling Events and Conditional Rendering:** Button seçimi gibi kullanıcı event’lerini ele alma ve karşılık gelen action’ları tetikleme.

## ✅ Ön koşullar

* GitHub hakkında temel bilgi ve kendi GitHub hesabınız
* React function components, props, hooks ve React Redux Toolkit hakkında bilgi
* Console’a sahip web tarayıcısı (Chrome DevTools veya Firefox Console gibi)
* Practice Project’i tamamlamak zorunludur

## 🧪 Bu lab ortamı hakkında önemli bildirim

Skills Network Cloud IDE (Theia ve Docker tabanlı), course ve proje ile ilgili hands-on lab’ler için bir ortam sağlayan açık kaynaklı bir IDE’dir (Integrated Development Environment).

Lütfen bu lab ortamındaki oturumların kalıcı olmadığını unutmayın. Bu lab’e her bağlandığınızda yeni bir ortam oluşturulur. GitHub’a veya başka bir dış kaynağa kaydetmeden ortamdan çıkarsanız verileri kaybedersiniz. Bu lab’leri veri kaybını önlemek için tek bir oturumda tamamlamayı planlayın.

---

# 🧷 GitHub’da ortamınızı kurma

## 1) 🍴 Depoyu fork’lama

React uygulamanız için GitHub repository’sini fork’lamanız gerekir. Bu projenin skeleton code’unu içeren GitHub repository’si buradadır. Fork oluştururken aynı repository adını kullanın:

`https://github.com/ibm-developer-skills-network/e-plantShopping.git`

Yukarıdaki linki açtıktan sonra **fork** düğmesine tıklayın.

## 2) 🧱 Depo içeriği

Bu repository, bu proje için React uygulamasının temel yerleşimini içerir.

## 3) 💾 Çalışmalarınızı kaydetme

En güncel kodunuzu push ederek yaptığınız işleri kaydetmek için bu fork’lanmış repository’yi kullanacaksınız. Dosyalarınızı periyodik olarak kaydedin. Git komutlarını çalıştırmak için dosyalarınızın kaydedilmiş olması gerekir.

## 4) 🔁 Git komutları

Uygulama klasörünüzden GitHub repository’nize değişiklikleri güncellemek için:

* `git add`
* `git commit`
* `git push`

komutlarını çalıştırın.

## 5) 🚀 Deploy gereksinimi

Peer review projesinin bir parçası olarak (bu seçeneği seçerseniz), UI’ın akranlar tarafından incelenebilmesi için uygulamanızı deploy etmeniz gerekir. GitHub ve React uygulaması deploy yönergeleri için bu talimatları inceleyebilirsiniz.

Eğer çıkış yaptıysanız ve projeye devam etmek istiyorsanız, daha önce kodu push ettiğiniz fork’lanmış repository’yi clone edin. Clone işleminden sonra, `git remote add...` çalıştırmanıza gerek kalmadan doğrudan `git push origin` kullanarak değişikliklerinizi gönderebilirsiniz.

---

# 🛠️ React projenizi oluşturma

1. Eğer açık bir terminal yoksa, ekranın sağ üstündeki **Terminal** sekmesini seçin ve ardından **New Terminal** seçin. Aşağıdaki ekran görüntüsü bu seçenekleri nerede bulacağınızı gösterir.
2. Şimdi `<forked-repo-link>` yerine kendi repository linkinizi koyarak aşağıdaki komutla fork’lanmış repository’yi clone edin:

```bash
git clone <forked-repo-link>
```

**Not:** Orijinal repository adını **e-plantShopping** olarak korumalısınız.

3. Uygulama adınızın projenizle eşleştiğinden emin olun.
4. Repository’yi clone ettikten sonra, aşağıdaki ekran görüntüsündeki gibi klasör yapısını göreceksiniz.
5. Terminalde uygulama klasörüne girmek için komutu yazın. Bu komut, React uygulamasını `<forked-folder-name>` klasörü içinde çalıştırmak için terminal yolunu ayarlar.

```bash
cd e-plantShopping
```

6. Clone ettiğiniz kodun doğru çalıştığından emin olmak için aşağıdaki adımları izleyin:
   Gerekli tüm paketleri yüklemek için terminalde şu komutu yazın ve Enter’a basın:

```bash
npm install
```

Ardından, size 4173 port numarasını sağlayarak uygulamayı çalıştırmak için şu komutu yürütün:

```bash
npm run preview
```

7. React uygulamanızı görüntülemek için sol paneldeki Skills Network ikonuna tıklayın (1 numaraya bakın). Bu, Skills Network Toolbox’ı açacaktır. Ardından Launch Application’a tıklayın (2 numaraya bakın). Application Port alanına 4173 port numarasını girin (3 numaraya bakın) ve **click .**
8. Çıktı, arka plan resmiyle birlikte verilen ekran görüntüsüne göre olacaktır.
9. Şimdi **Get Started** düğmesine tıklayın ve ardından yeşil arka plan renkli navbar içeren, ekran görüntüsüne göre verilen yerleşimi göreceksiniz.
10. Navbar üç bağlantı içerir:

* **Paradise Nursey** – Bu sizi uygulamanın landing sayfasına geri götürür.
* **Plants** – Bu, sayfayla ilgili bilgilerin görüntüleneceği sayfaya yönlendirir.
* **Cart icon** – Bu, sepet öğeleri bölümüne yönlendirir.

11. Cart ikonuna tıkladığınızda çıktı, verilen ekran görüntüsüne göre görünecektir.

Aşağıdaki sayfalarda açıklanan gerekli görevleri tamamlayın. Bu görevler üzerinden değerlendirileceksiniz.

---

# 📝 README.md dosyasını güncelleme

GitHub repository’nizde **README.md** dosyanızı açın.

* Dosya içeriğinde repository adı **e-plantShopping** yer almalıdır. Ayrıca proje adını belirtebilir ve uygulamanıza kısa bir genel bakış sağlayabilirsiniz.
* **Not:** Dosyada repository adı **e-plantShopping** mutlaka yer almalıdır.
* Bu değişiklikleri GitHub repository’nize push ederek kaydettiğinizden emin olun.
* **Not:** Peer Graded Assignment’a devam etmeyi seçerseniz bu adım atlanabilir.

---

# ✅ Görev 1: ProductList bileşeni yerleşimi

Ürün sayfası, kullanıcıların sattığınız farklı bitkiler için alışveriş yapmasına izin verecektir. Her bitki, bitki nesnesinde saklanan ilgili verilerle kendi “card”ı üzerinde görüntülenecektir. Bitki nesnelerini bir array’de saklayacaksınız. Array ve bitki nesneleri için şu adımları izleyin:

1. **Plant Array’i görüntüleyin**
   ProductList.jsx bileşenine gidin; bitki detaylarını içeren **plantsArray** adlı bir array göreceksiniz.
   Her bitki nesnesi; categories, name, image URL, description ve cost özelliklerini içerir.
2. **Plant detaylarını product-grid sınıf adına sahip div etiketi içinde gösterin**
   * Plant array’i üzerinde map işlemi yapmak için array metotlarını kullanın.
   * **İpucu:** Array’i iterate etmek için *map()* metodunu kullanın.
   * Sayfada her bitkinin detaylarını (name, image, description, cost) render edin.
3. **Her bitki için bir Add to Cart düğmesi görüntüleyin**

**Bitkileri ve Add to cart düğmesini görüntüleme çözümü:**

```jsx
{plantsArray.map((category, index) => ( // Loop through each category in plantsArray
 <div key={index}> {/* Unique key for each category div */}
 <h1>
 <div>{category.category}</div> {/* Display the category name */}
 </h1>
 <div className="product-list"> {/* Container for the list of plant cards */}
 {category.plants.map((plant, plantIndex) => ( // Loop through each plant in the current category
 <div className="product-card" key={plantIndex}> {/* Unique key for each plant card */}
 <img 
 className="product-image"
 src={plant.image} // Display the plant image
 alt={plant.name} // Alt text for accessibility
 />
 <div className="product-title">{plant.name}</div> {/* Display plant name */}
 {/* Display other plant details like description and cost */}
 <div className="product-description">{plant.description}</div> {/* Display plant description */}
 <div className="product-cost">${plant.cost}</div> {/* Display plant cost */}
 <button
 className="product-button"
 onClick={() => handleAddToCart(plant)} // Handle adding plant to cart
 >
 Add to Cart
 </button>
 </div>
 ))}
 </div>
 </div>
))}
```

Yukarıdaki kodu **product-grid** sınıf adı içinde ekleyin.

4. **State management için addedToCart adlı bir değişken oluşturun**
   useState hook’unu kullanarak hangi ürünlerin sepete eklendiğini takip edin.

**useState hook için örnek çözüm:**

```jsx
const [addedToCart, setAddedToCart] = useState({});
```

5. **Add to Cart işlevselliği**
   Kullanıcı Add to Cart düğmesini seçtiğinde bitkiyi sepete ekleme işlevini uygulamak için **handleAddToCart** fonksiyonunu oluşturun. Bu fonksiyon, seçilen bitkinin bilgisini içeren tek bir parametre almalıdır. Bu bilgi daha sonra CartSlice fonksiyon bileşeni içindeki **addItem** içine dispatch edilmelidir.
   Ayrıca, ürünün sepete eklendiğini yansıtın. setAddedToCart state’ini, ürün adını anahtar ve değerini true olacak şekilde güncelleyin.

**Sepete ekleme için örnek çözüm:**

```jsx
const handleAddToCart = (product) => {
 dispatch(addItem(product)); // Dispatch the action to add the product to the cart (Redux action)
 setAddedToCart((prevState) => ({ // Update the local state to reflect that the product has been added
 ...prevState, // Spread the previous state to retain existing entries
 [product.name]: true, // Set the current product's name as a key with value 'true' to mark it as added
 }));
};
```

**Not:** CartSlice.jsx dosyasından addItem reducer’ını import ettiğinizden emin olun.

6. handleAddToCart() fonksiyonu, kullanıcının sepete eklemek istediği bitkinin detaylarını taşıyacaktır. Ve bitki detayları CartSlice.jsx kullanılarak global düzeyde sepete eklenecektir.
7. Bu değişiklikleri GitHub repository’nize push ederek kaydettiğinizden emin olun.

---

# 🧠 Görev 2: Redux kullanarak state yönetimi

1. CartSlice.jsx dosyasında temel yerleşim hazırdır.
2. **Reducer fonksiyonlarını tanımlayın**
   Slice’ın reducer özelliğini; sepete ekleme, çıkarma ve sepetteki ürünlerin sayısını güncelleme için uygulayın.

Bu reducer fonksiyonları, kullanıcı cartItems bileşeni içinde bitkilerin miktarını artırmak veya azaltmak istediğinde çağrılacaktır.

* **addItem() reducer** ’ı, önceki adımda initialize ettiğiniz items array’ine yeni bir bitki öğesi ekler.
* addItem() fonksiyonu, kullanıcı bitki listeleme sayfasında Add to cart seçtiğinde çağrılmalıdır. Ardından, bitki türünü parametre olarak alan handleAddToCart() çağrılır.
* handleAddToCart() fonksiyonu daha sonra bitki detaylarını CartSlice.jsx içindeki addItem() reducer fonksiyonuna dispatch eder.

**addItem() reducer örnek çözüm:**

```jsx
addItem: (state, action) => {
 const { name, image, cost } = action.payload; // Destructure product details from the action payload
 // Check if the item already exists in the cart by comparing names
 const existingItem = state.items.find(item => item.name === name);
 if (existingItem) {
 // If item already exists in the cart, increase its quantity
 existingItem.quantity++;
 } else {
 // If item does not exist, add it to the cart with quantity 1
 state.items.push({ name, image, cost, quantity: 1 });
 }
},
```

Şimdi removeItem() ve updateQuantity() reducer’ları için kodu tamamlamanız gerekir.

* **removeItem():** Bu reducer, adına göre bir öğeyi sepetten kaldırır ve kullanıcı sepetten ürün kaldırmak istediğinde çağrılır.

**removeItem() reducer örnek çözüm:**

```jsx
state.items = state.items.filter(item => item.name !== action.payload);
```

* **updateQuantity():** Bu fonksiyonu oluşturmak için, action.payload içinden öğenin name ve amount değerini çıkararak başlayın. Ardından, çıkarılan name ile eşleşen öğeyi state.items array’inde arayın. Öğeyi bulursanız, quantity değerini payload’da verilen yeni amount değerine güncelleyin. Bu, action’a göre öğe miktarının doğru şekilde güncellenmesini sağlar.

**updateQuantity() reducer örnek çözüm:**

```jsx
const { name, quantity } = action.payload; // Destructure the product name and new quantity from the action payload
// Find the item in the cart that matches the given name
const itemToUpdate = state.items.find(item => item.name === name);
if (itemToUpdate) {
 itemToUpdate.quantity = quantity; // If the item is found, update its quantity to the new value
}
```

3. **Action’ları ele alın**
   Action creator’ları export edin: ProductList.jsx içinde kullanmak için addItem(), CartItem.jsx içinde kullanmak için removeItem() ve updateQuantity(). Ayrıca reducer’ı store.js içinde kullanmak üzere default olarak export edin.
4. Bu değişiklikleri GitHub repository’nize push ederek kaydettiğinizden emin olun.

---

# 🛒 Görev 3: CartItems bileşeni

Sonraki adımda, alışveriş sepetindeki öğeleri gösteren CartItem.jsx bileşeninin geliştirilmesini tamamlayacaksınız. Bu bileşen, tipik bir alışveriş sepetinde bulunan çeşitli işlevlere sahiptir:

* Sepetteki tüm öğeler için toplamı hesaplama
* Sepetteki her bitki türü için ara toplamı hesaplama
* Continue shopping
* Sepette her bitki türünün miktarını artırma ve azaltma
* Bir bitki türünü sepetten tamamen kaldırma (delete)

Increment, decrement ve update quantity detaylarını bir Redux dosyasından dispatch edeceksiniz.

İşiniz bittiğinde sepet sayfası aşağıdakine benzer görünmelidir:

## 1) 💰 Sepetteki tüm öğelerin maliyeti

calculateTotalAmount() içinde, sepetteki tüm öğelerin maliyetini hesaplayan bir fonksiyona ihtiyacınız var. Bunu hesaplamanın çeşitli yolları vardır.

**Toplam maliyeti hesaplamak için örnek algoritma açıklaması:**

* Kümülatif toplamı tutmak için total adlı bir değişken initialize edin.
* cart array’i üzerinde cart.forEach() kullanarak iterate edin.
* Her öğe için quantity ve cost değerlerini çıkarın. cost string’ini (örn. “$10.00”) `parseFloat(item.cost.substring(1))` ile sayıya dönüştürün, sonra quantity ile çarpın. Elde edilen değeri total’e ekleyin.
* Tüm öğeler işlendiğinde, final toplamı döndürün.

## 2) 🧭 Continue shopping

Kullanıcılar alışveriş sepeti sayfasındayken bitki listeleme sayfasına geri dönerek alışverişe devam edebilmelidir. Bu nedenle handleContinueShopping() fonksiyonunda, parent bileşenden geçirilen onContinueShopping(e) fonksiyonunu çağırın.

## 3) ✅ Checkout

Bu projede handleCheckoutShopping() fonksiyonunu sağlamanız zorunlu değildir, ancak daha fazla keşif ve pratik için isteyebilirsiniz. Şimdilik, kullanıcıya bu fonksiyonun daha sonra ekleneceğini bildirmek için aşağıdaki kodu ekleyin.

```jsx
const handleCheckoutShopping = (e) => {
 alert('Functionality to be added for future reference');
};
```

## 4) ➕➖ Increment ve decrement

handleIncrement() ve handleDecrement() fonksiyonları için CartSlice.jsx dosyasındaki updateQuantity() reducer’ını dispatch etmeniz gerekir. Fonksiyon argümanında item.quantity değerine sırasıyla 1 ekleyin veya 1 çıkarın.

Ayrıca handleDecrement() için bir if-else ile şu durumu ele almanız gerekir:

* Eğer öğenin quantity değeri 1’den büyükse, quantity’yi 1 azaltmak için updateQuantity dispatch edin.
* Aksi halde quantity 0’a düşecekse, bitki türünü sepetten kaldırmak için removeItem action’ını dispatch edin.

**İpuçlarını görmek için buraya tıklayın**
Redux slice’ınızdan updateQuantity action’ını dispatch ederek öğenin quantity değerini 1 artırın veya azaltın. Hangi öğenin quantity’sinin güncelleneceğini belirlemek için item’ın name parametresini kullanın.

**Örnek kod:**

```jsx
dispatch(updateQuantity({ name: item.name, quantity: item.quantity + 1 }));
```

## 5) 🗑️ Sepetten bitki kaldırma

handleRemove() fonksiyonu için removeItem action’ını dispatch ederek öğeyi silin.

## 6) 🧾 Item ara toplamı

calculateTotalCost() fonksiyonunda, quantity ile birim fiyatı çarparak bir öğenin toplam maliyetini hesaplayın. Çarpma işleminden önce item.cost string’inden sayısal değeri `parseFloat(item.cost.substring(1))` kullanarak çıkarın.

**Not:** Bu event handler’ların UI’ı gerçek zamanlı güncellediğinden emin olun. Kullanıcı bir bitki türünün miktarını değiştirdiğinde aşağıdakiler buna göre güncellenmelidir:

* Bireysel bitki miktarı
* Öğenin ara toplamı
* Genel toplam maliyet
* Cart ikonunda sepetteki toplam öğe sayısı
* Kullanıcı bir bitki öğesi için “Add to Cart” düğmesine tıkladıktan sonra, düğme devre dışı kalmalı ve gri olmalı; etiketi, öğenin zaten eklendiğini belirtmek için “Added to Cart” olarak güncellenmelidir.

7. Bu değişiklikleri GitHub repository’nize push ederek kaydettiğinizden emin olun.

---

# 🧩 Görev 4: Bileşenlerinizde Redux işlevselliğini entegre etme

## 1) 🪴 ProductList bileşeni

Redux store içinde cart state’ini initialize ederek cart item’larını takip edin.

**İpuçlarını görmek için buraya tıklayın**

```jsx
dispatch(addItem(product));
```

Seçilen ürünleri sepete eklemek için addItem action’ını kullanın.

Redux store’a erişerek sepetteki toplam öğe miktarını alın ve dinamik olarak görüntüleyin.

**İpuçlarını görmek için buraya tıklayın**

```jsx
const calculateTotalQuantity = () => {
return CartItems ? CartItems.reduce((total, item) => total + item.quantity, 0) : 0;
 };
```

## 2) 🛒 CartItem bileşeni

Sepette kaç öğe olduğunu değiştirmek için updateQuantity action’ını kullanın. Sepete yeni bir ürün eklemek için addItem action’ını kullanın. Bir öğeyi tamamen silmek için removeItem action’ını kullanın.

**İpuçlarını görmek için buraya tıklayın**

```jsx
dispatch(removeItem(item.name));
```

**Not:** Bu değişiklikleri GitHub repository’nize push ederek kaydettiğinizden emin olun.

---

# 🗄️ Görev 5: Detayları store.js dosyasına import etme

## 1) Gerekli fonksiyonları ve dosyaları import etme

@reduxjs/toolkit paketinden configureStore() fonksiyonu, Redux store’u kurmak için import edilir. CartSlice.jsx dosyasından import edilen cartReducer, alışveriş sepetiyle ilgili state slice’ını yönetir.

```jsx
import { configureStore } from '@reduxjs/toolkit';
import cartReducer from './CartSlice';
```

## 2) Store’u yapılandırma

configureStore() fonksiyonu Redux store’u kurmak için kullanılır. configureStore()’a geçirilen configuration object içinde reducer anahtarı reducer fonksiyonlarını belirtir. Bu örnekte cartReducer, state’in cart slice’ını yönetmek için atanır.

```jsx
// Create a Redux store using configureStore from Redux Toolkit
const store = configureStore({
 // Define the root reducer object
 reducer: {
 // 'cart' is the name of the slice in the store, and it's managed by cartReducer
 cart: cartReducer,
 },
});
export default store; // Export the store for use in the app (e.g., in <Provider store={store}>)
```

## 3) Store’u export etme

Yapılandırılmış Redux store, uygulama genelinde state yönetimi için kullanılabilmesi amacıyla `export default store;` ile export edilir.

```jsx
export default store;
```

**Not:**

* Bu store.js kodu repository’de önceden yapılandırılmıştır ve kullanıma hazırdır.
* Bu değişiklikleri GitHub repository’nize push ederek kaydettiğinizden emin olun.

---

# 🌐 Görev 6: Global store’u kurma

1. src klasöründeki main.jsx dosyasına gidin.
2. react-redux kütüphanesinden Provider bileşeni zaten import edilmiştir. Bu bileşen, uygulamadaki tüm bileşenlerin Redux store’a erişmesini sağlar.

```jsx
import { Provider } from 'react-redux';
```

3. Redux store, store.js dosyasından import edilir. Bu store, CartSlice.jsx dosyasında tanımlanan reducer’ı kullanarak uygulamanın state’ini tutar.

```jsx
import store from './store.js';
```

4. App bileşeni, Redux store’un prop olarak verildiği Provider bileşeni ile sarılır. Bu, uygulamadaki tüm bileşenlerin Redux tarafından yönetilen global state’e erişmesini ve onunla etkileşime girmesini sağlar.

```jsx
<Provider store={store}>
 <App />
</Provider>
```

---

# 🚀 GitHub Pages ile uygulamanızı deploy etme

## GitHub Pages ile deploy

1. React uygulamanızı GitHub’da deploy etmek için gh-pages’i yüklemeniz gerekir. Bu, projenizi GitHub Pages’e deploy etmek için bir araç olarak kullanmanızı sağlar. Terminalde şu komutu çalıştırın:

```bash
npm install gh-pages --save-dev
```

2. package.json dosyasında `"build": "vite build"` satırından önce aşağıdaki satırları ekleyin:

```json
"predeploy": "npm run build",
"deploy": "gh-pages -d dist",
```

3. vite.config.js dosyasında `plugins: [react()]` satırından önce şu satırı ekleyin:

```js
base: "/YOUR_REPOSITORY_NAME",
```

**Not:** `<YOUR_REPOSITORY_NAME>` yerine kendi repository adınızı yazın; örneğin GitHub repository adınız learning_react ise şöyle olmalıdır: `base: "/learning_react"`

4. Şimdi terminalde deploy komutunu çalıştırın. Bu komut, package.json dosyasında tanımlanan “deploy” script’ini yürütür ve gh-pages aracıyla projeyi GitHub Pages’e deploy eder.

```bash
npm run deploy
```

**Not:** Kodunuzda her değişiklik yaptığınızda, tüm dosyalarınızı kaydedip onlar için git komutlarını çalıştırmanız gerekir.

5. Kodunuzdaki değişiklikleri güncellemek için `git add` ve `git commit` komutlarını çalıştırın. Ardından proper code management için GitHub repository’nizi güncellemek üzere `git push` komutunu çalıştırın.
6. GitHub repository’nize gidin. Ardından oluşturduğunuz sitenin repository’sine gidin.
7. Repository adınızın altında  **Settings** ’e tıklayın.
8. Sol taraftaki navigation bar’a gidin. Sidebar’daki Code and Automation bölümünde  **Pages** ’e tıklayın.
9. Aşağıdaki gibi sayfayı göreceksiniz. None gördüğünüz açılır menüye tıklayın, ardından  **gh-pages** ’i seçin ve sonra **Save** düğmesine tıklayın.
10. Sayfayı yeniden yenileyin; aşağıdaki gibi bağlantıyı göreceksiniz. shoppingreact yerine GitHub repository adınızı göreceksiniz.
    **Not:** Bağlantıyı göremiyorsanız, lütfen (1-2) dakika bekleyin ve sayfayı yeniden yenileyin.
11. Live web sitenizi görmek için oluşturulan linke tıklayın.

**Not:**

* Bu kod repository’de önceden yapılandırılmıştır ve kullanıma hazırdır.
* Deploy ettikten sonra, tüm içerik ve görsellerin düzgün görünmesi biraz zaman alabilir. Lütfen uygulamanın tamamen yüklenmesi için birkaç dakika daha bekleyin.

---

# 🎉 Proje Tamamlama

Tebrikler!

Bu projeyi tamamladınız! Harika iş.

Henüz yapmadıysanız, uygulamanızı deploy edin. GitHub Pages veya kendi hosting sitenizi kullanarak deploy edebilirsiniz.

Güncellenmiş tüm dosyaları GitHub repository’nize push ettiğinizden emin olun.

---

# 📌 Özet

* Fonksiyonel React bileşenleri oluşturdunuz, compose ettiniz ve nested yaptınız.
* Component-level state’leri yönetmek için özellikle useState ve useEffect hook’larını uyguladınız.
* React uygulamanıza Redux entegre ettiniz ve actions, reducers ve store gibi Redux kavramlarını uyguladınız.
* Object array’inden alınan veriyi UI’a dinamik olarak render ettiniz. Listeler üretmek için array’ler üzerinde map kullandınız.
* Button seçimi gibi kullanıcı event’lerini ele aldınız ve sepete öğe eklemek ve çıkarmak için karşılık gelen action’ları tetiklediniz.

---

# ✅ Gönderim için kontrol listesi

Göndermeden önce, tüm linklerin doğru açıldığını ve public olarak erişilebilir olduğunu doğrulayın.

## 🤖 AI-Graded Submission and Evaluation

AI grading için, aşağıda listelenen belirli proje dosyalarının public GitHub URL’lerini gönderin.

### Checklist

1. Proje adı detaylarını içeren README.md dosyasının GitHub URL’sini gönderin.
   İçerikte repository adı **e-plantShopping** yer aldığından emin olun.
2. Şirket detaylarını içeren AboutUs.jsx dosyasının GitHub URL’sini gönderin.
3. Paradise Nursery landing sayfası için arka plan görselini içeren App.css dosyasının GitHub URL’sini gönderin.
4. Şirketin hoş geldiniz mesajı ve “Get Started” düğmesi (ürün listeleme sayfasına linklenen) içeren Paradise Nursery landing sayfasını barındıran App.jsx dosyasının GitHub URL’sini gönderin.
5. Alışveriş sepeti için Redux slice’ını içeren CartSlice.jsx dosyasının GitHub URL’sini gönderin.
   Sepet öğelerini ekleme, kaldırma ve güncelleme için Redux işlevselliğini tanımladığından emin olun.
6. Ürün listeleme sayfasını aşağıdaki işlevlerle uygulayan ProductList.jsx dosyasının GitHub URL’sini gönderin:
   * Her kategori için en az altı benzersiz ev bitkisini, küçük görsel, ad ve fiyat ile görüntüleme.
   * Bitkileri en az üç kategoriye ayırma.
   * “Add to Cart” düğmeleri:
     * Ürünü sepete ekler.
     * Ürün eklendikten sonra düğmeyi devre dışı bırakır.
     * Sepeti günceller.
   * Hem Product Listing hem de Cart sayfalarında görünen bir navbar: Home, Plants ve Cart bağlantıları.
   * Toplam öğe sayısını dinamik gösteren cart ikonunu görüntüleme.
7. Shopping Cart sayfasını aşağıdaki işlevlerle gösteren CartItem.jsx dosyasının GitHub URL’sini gönderin:
   * Tüm bitkiler için toplam sepet tutarını gösterme.
   * Sepetteki bitki başına toplam maliyeti gösterme. Her sepet öğesi küçük görsel, bitki adı ve birim fiyatı göstermelidir.
   * Miktarı artırıp azaltmak için düğmeler ve toplamları doğru güncelleme.
   * Öğeleri sepetten kaldırmak için delete düğmesi.
   * “Coming Soon” veya benzeri bir mesaj gösteren checkout düğmesi.
   * Product Listing sayfasına geri bağlanan continue shopping düğmesi.

### Göndermeden önce

Tüm dosyaların e-plantShopping repository’sine güncellenip commit edilerek push edildiğinden emin olun. Her gönderilen link, belirli dosyaya doğrudan işaret eden public bir GitHub URL’si olmalıdır. Göndermeden önce tüm işlevlerin doğru çalıştığını doğrulayın.

---

# 👥 Peer-Graded Submission and Evaluation

Peer grading için aşağıdaki URL’leri göndermelisiniz:

### Checklist

1. GitHub Pages veya başka bir platformda barındırılan deployed uygulamanızın URL’sini gönderin.
   Uygulamanızın tamamen işlevsel ve public erişilebilir olduğundan emin olun.
2. **e-plantShopping** adlı public repository’nizin GitHub URL’sini gönderin.
   Tüm dosyaların commit edilip push edildiğinden emin olun.

## 📏 Peer review için proje değerlendirme rubriği

### GitHub Link:

* Public GitHub repository URL
* Redux ile ilgili dosyalar ve kod doğru şekilde uygulanmış

### Deployed uygulama URL’si ile:

**Landing Page**

* Background image düzgün görüntülenir
* Şirket hakkında bir paragraf içerir
* Şirket adını görüntüler
* Ürün listeleme sayfasına linklenen “Get Started” düğmesini içerir

**Product Listing Page**

* Satışta en az altı benzersiz ev bitkisini küçük görsel, ad ve fiyat ile görüntüler
* Bitkileri en az üç kategoriye ayırır
* Her bitki için bir “Add to Cart” düğmesi içerir; bu düğme:
  * Seçilen bitkiyi shopping cart’a ekler
  * Shopping cart ikon sayacını artırır
  * Bitki eklendikten sonra düğmeyi devre dışı bırakır

**Header**

* Hem product listing hem de shopping cart sayfalarında görüntülenir
* Toplam öğe sayısını dinamik gösteren shopping cart ikonunu içerir
* Product listing ve shopping cart sayfaları arasında gezinmeye izin verir

**Shopping Cart Page**

* Sepetteki toplam bitki sayısını görüntüler
* Tüm öğelerin toplam maliyetini görüntüler
* Her bitki türü küçük görsel, ad ve birim fiyat görüntüler
* Her bitkinin miktarını artırıp azaltmak ve toplamları buna göre güncellemek için düğmeler içerir
* Öğeleri sepetten kaldırmak için delete düğmesi içerir
* “Coming Soon” veya benzeri bir mesaj görüntüleyen checkout düğmesi içerir
* Product listing sayfasına linklenen “Continue Shopping” düğmesi içerir

**Before You Submit**

* Deployed uygulama linkinizin doğru açıldığını doğrulayın.
* GitHub repository’nizin public olduğunu ve en son güncellemeleri içerdiğini doğrulayın.

---

# ✍️ Yazar

Richa Arora

© IBM Corporation. Tüm hakları saklıdır.
