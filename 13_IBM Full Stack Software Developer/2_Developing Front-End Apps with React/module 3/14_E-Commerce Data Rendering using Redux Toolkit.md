## 🧪 Lab: Redux Toolkit Kullanarak E-Ticaret Veri Render Etme

**Tahmini gerekli süre:** 60 dakika

## 🧭 Giriş

Bu lab’de, Redux Toolkit’i kullanarak uygulamanızın tamamında state’i yönetmeyi öğreneceksiniz; böylece bileşenler arasındaki hiyerarşiyi takip etmeden herhangi bir bileşen tarafından erişilebilir olacaktır. React ve Redux kullanarak basit bir E-Ticaret uygulaması oluşturacaksınız; her ürün için bir **“Add to Cart”** butonu olan ürün listesini görüntüleyecek, sepete eklenen öğeleri gösterecek ve kullanıcıların öğeleri sepetten kaldırmasına izin vereceksiniz. Tüm bu bilgiler, Redux Toolkit kullanılarak uygulama genelinde global olarak erişilebilir olacaktır.

## 🎯 Öğrenme hedefleri

Bu lab’i tamamladıktan sonra şunları yapabileceksiniz:

* State yönetimi için React bileşenlerini Redux ile entegre etmek
* Sepete öğe ekleme, sepetten öğe kaldırma ve sepeti temizleme gibi temel E-Ticaret özelliklerini uygulamak
* Tutarlı bir kullanıcı arayüzü oluşturmak için birden fazla React bileşenini bir araya getirme pratiği yapmak

## 📌 Ön koşullar

* React’te bileşenleri birleştirme (composition) konusunda temel bilgi
* JavaScript’te orta seviye bilgi
* React functional component, *useState hook* kullanarak state yönetimi ve Redux Toolkit bilgisi

---

## 🛠️ Adım 1: Ortamı Kurma

1. Lab’in üst kısmındaki menüden, verilen ekran görüntüsünde 1 numara ile gösterilen sağ üstteki **Terminal** sekmesine tıklayın; ardından 2 numara ile gösterildiği gibi  **New Terminal** ’a tıklayın.
2. Şimdi terminale aşağıdaki komutu yazın ve Enter’a basarak bu React uygulaması için  *boiler template* ’i klonlayın.

```bash
git clone https://github.com/ibm-developer-skills-network/ecommerce_rtk.git
```

3. Yukarıdaki komut, **Project** klasörü altında **“ecommerce_rtk”** adlı bir klasör oluşturacaktır. Yapıyı ekran görüntüsünde görebilirsiniz.
4. Sonraki adımda, bu React uygulaması için bazı işlemleri gerçekleştirmek üzere terminal yolunuzun klonlanan klasöre işaret etmesi gerekir. Terminalde **ecommerce_rtk** klasörüne gitmek için aşağıdaki komutu kullanın.

```bash
cd ecommerce_rtk
```

5. Klonladığınız kodun doğru çalıştığından emin olmak için aşağıdaki adımları uygulayın:
   Verilen komutu terminale yazın ve Enter’a basın. Bu komut, uygulamayı çalıştırmak için gerekli tüm paketleri yükleyecektir.

```bash
npm install
```

Ardından uygulamayı çalıştırmak için aşağıdaki komutu çalıştırın; bu size **4173** port numarasını verecektir.

```bash
npm run preview
```

6. React uygulamanızı görüntülemek için soldaki **Skills Network** ikonuna tıklayın (1 numaraya bakın). Bu işlem  **SKILLS NETWORK TOOLBOX** ’ı açacaktır. Ardından  **Launch Application** ’a tıklayın (2 numara). **Application Port** alanına **4173** girin (3 numara) ve  **.** ’a tıklayın.
7. Çıktı, verilen ekran görüntüsündeki gibi görünecektir.

---

## 🧾 Adım 2: ProductList Bileşenini Uygulama

1. Sonraki adımda, klonladığınız **ecommerce_rtk** klasörünün **src** dizinindeki **Components** klasöründe bulunan **ProductList.jsx** dosyasına gidin.
2. Bu bileşenin temel yapısı, ekran görüntüsünde gösterildiği gibi olacaktır.
3. Şimdi  *front end* ’de ürün listesini göstermeniz gerekir. Bunun için **"product-list-items"** sınıf adına sahip `<ul>` etiketi içinde *map* metodunu uygulayın.

```jsx
{products.map(product => (
 <li key={product.id} className="product-list-item">
 <span>{product.name} - ${product.price}</span>
 <button>
 Add to Cart
 </button>
 </li>
))}
```

4. Terminalde React uygulamasının çalışmasını durdurmak için **ctrl+c** yaparak çıkın. Ardından terminale verilen komutu yazın ve Enter’a basın.

```bash
npm run preview
```

5. Çıktıyı kontrol edin; verilen ekran görüntüsünde gösterildiği gibi görüntülenecektir.

---

## 🧠 Adım 3: Redux Mantığını Uygulama

1. **Add to Cart** butonuna tıklayıp bir ürünü sepete eklediğinizde, girdiğiniz ürün miktarı bilgisinin herhangi bir bileşen tarafından global olarak erişilebilir olması için Redux Toolkit mantığını uygulamanız gerekir.
2. Şimdi klonladığınız **ecommerce_rtk** klasörünün **src** dizinindeki **Components** klasöründe bulunan **CartSlice.jsx** dosyasına gidin.
3. Aşağıdaki gibi bir yapı göreceksiniz:

```js
const CartSlice = ({
});
```

4. İlk olarak,  **CartSlice** ’ın dışında **cartItems** adlı boş bir diziyle başlangıç state’i başlatın.

```js
const initialState = {
 cartItems: [],
};
```

5. Şimdi  **CartSlice** ’ı bir **createSlice** Redux Toolkit fonksiyonu ile başlatın. *@reduxjs/toolkit* ve  *react-redux* ’u üçüncü taraf modül olarak kurmanız gerekir. Bu lab için, *package.json* dosyasında zaten sağlandığı için ayrıca kurmanız gerekmez ve  *createSlice* , Redux Toolkit tarafından sağlanan bir  *utility function* ’dır; Redux’un üzerine inşa edilmiş bir kütüphanedir. Redux slice’larını (Redux state’inin bölümleri) ve bunlarla ilişkili *action creators* ile  *reducers* ’ları oluşturma sürecini basitleştirir.

```js
const CartSlice = createSlice({
 
});
```

6. **createSlice** ’ın bu bileşenin en üstünde import edildiğinden emin olun.

```js
import { createSlice } from '@reduxjs/toolkit';
```

---

## 🧱 Adım 4: Action ve Reducer Oluşturma

1. **Slice Oluşturma:**
   Slice’ınız için yapılandırma seçeneklerini içeren bir nesne ile **createSlice** çağırırsınız. Yapılandırma seçenekleri şunları içerir:

* **name:** Slice’ınızın adını temsil eden string bir değer. Redux Toolkit tarafından action type ön eki (prefixing) ve diğer amaçlar için dahili olarak kullanılır.
* **initialState:** Slice’ınızın başlangıç state’ini temsil eden bir nesne.
* **reducers:** Reducer fonksiyonlarını içeren bir nesne. Her bir anahtar-değer çifti tek bir reducer’ı temsil eder; anahtar action adıdır, değer reducer fonksiyonudur.

```js
const CartSlice = createSlice({
 name: 'cart',
 initialState,
 reducers: {
 }
});
```

---

## 🧩 Adım 5: Reducer’ları Oluşturma ve Action’ları Export Etme

1. **reducers** nesnesinin içinde, beş fonksiyon oluşturmanız gerekir: ikisi alışveriş sepetine ürün ekleme ve kaldırmayı yönetmek için, biri tüm öğeleri tek seferde temizlemek için, diğer ikisi ise miktarı artırıp azaltmak içindir.

### ➕ addItemToCart

Bu reducer fonksiyonu sepete öğe ekleme eylemini yönetir. İki parametre alır: *state* (slice’ın mevcut state’i) ve *action* (payload içeren dispatch edilen action).

Önce, *state.cartItems* içinde ID ile arayarak öğenin sepette zaten var olup olmadığını kontrol eder. Öğe varsa (*existingItem* true), sepetteki mevcut öğenin *quantity* değerini 1 artırır. Öğe yoksa, öğeyi *cartItems* dizisine *quantity: 1* ile ekler.

```js
addItemToCart(state, action) {
 const existingItem = state.cartItems.find(item => item.id === action.payload.id);
 if (existingItem) {
 existingItem.quantity += 1;
 } else {
 state.cartItems.push({ ...action.payload, quantity: 1 });
 }
},
```

### ➖ removeItemFromCart

Bu reducer fonksiyonu sepetten bir öğeyi kaldırmayı yönetir. İki parametre alır: *state* ve  *action* . *action payload* içinde verilen ID’ye sahip öğeyi filtreleyerek *cartItems* dizisini günceller.

```js
removeItemFromCart(state, action) {
 state.cartItems = state.cartItems.filter(item => item.id !== action.payload);
},
```

### 🧹 clearCart

Bu reducer fonksiyonu tüm sepeti temizlemeyi yönetir. Sadece *state* parametresini alır. *cartItems* dizisini boş bir diziye ayarlar ve böylece tüm öğeleri temizler.

```js
clearCart(state) {
 state.cartItems = [];
},
```

### ⬆️ increaseItemQuantity

Bu reducer fonksiyonu sepetteki belirli bir öğenin miktarını artırmayı yönetir. İki parametre alır: *state* ve  *action* .

* *state:* Redux store’un mevcut state’ini temsil eder. Genellikle uygulamayla ilgili verileri içerir.
* *action:* Oluşan eylemi tanımlayan bir nesnedir. Redux action’ları, gerçekleştirilen action türünü belirten bir *type* özelliğine sahip düz JavaScript nesneleridir. Ayrıca görevi gerçekleştirmek için gerekli ek verileri içerebilir. Bu durumda, *action.payload* muhtemelen miktarı artırılacak öğenin tanımlayıcısını ( *id* ) içerir.

Fonksiyon mantığı: Alışveriş sepetinde tanımlayıcısı (id) action payload ile eşleşen öğeyi bulur. Öğe bulunursa ( *itemToIncrease undefined değilse* ), o öğenin *quantity* özelliğini 1 artırır.

```js
increaseItemQuantity(state, action) {
 const itemToIncrease = state.cartItems.find(item => item.id === action.payload);
 if (itemToIncrease) {
 itemToIncrease.quantity += 1;
 }
},
```

### ⬇️ decreaseItemQuantity

Bu reducer fonksiyonu sepetteki belirli bir öğenin miktarını azaltmayı yönetir. İki parametre alır: *state* ve  *action* .

* *state:* Redux store’un mevcut state’ini temsil eder; genellikle uygulamayla ilgili tüm verileri içerir.
* *action:* Benzer şekilde gerçekleştirilen action’ı tanımlayan bir nesnedir. Bir *type* özelliğine sahip olması beklenir ve görevi gerçekleştirmek için gerekli ek verileri içerebilir. Burada, *action.payload* muhtemelen miktarı azaltılacak öğenin tanımlayıcısını ( *id* ) tutar.

Fonksiyon mantığı: Alışveriş sepetinde tanımlayıcısı (id) action payload ile eşleşen öğeyi bulmaya çalışır. Öğe bulunursa ( *itemToDecrease undefined değilse* ) ve miktarı 1’den büyükse, o öğenin *quantity* özelliğini 1 azaltır.

```js
decreaseItemQuantity(state, action) {
 const itemToDecrease = state.cartItems.find(item => item.id === action.payload);
 if (itemToDecrease && itemToDecrease.quantity > 1) {
 itemToDecrease.quantity -= 1;
 }
},
```

2. **Action Creator’ları ve Reducer’ı Export Etme:**
   **createSlice** , üretilen action creator’ları ve reducer fonksiyonunu içeren bir nesne döndürür. Ardından bu action creator’ları ve reducer fonksiyonunu Redux store kurulumunda ve uygulamanız boyunca kullanmak üzere export edebilirsiniz.

```js
export const {
 addItemToCart,
 removeItemFromCart,
 clearCart,
 increaseItemQuantity,
 decreaseItemQuantity,
} = CartSlice.actions;
export default CartSlice.reducer;
```

Bu kodu **CartSlice** bileşeninin en sonuna ekleyebilirsiniz.

---

## 🏪 Adım 6: store.js Dosyasını Oluşturma

1. Sonraki adımda bir **store.js** dosyası oluşturun.
2. **src** klasörünü seçin ve klasöre sağ tıklayın. Ardından **New File** seçin ve adını **store.js** yazın.
3. Bu dosyanın içinde aşağıdaki işlemleri gerçekleştirin:

### 📥 configureStore ve Reducer Import Etme

Kod, Redux store’u oluşturmak için kullanılan **configureStore** fonksiyonunu  *@reduxjs/toolkit* ’ten import eder. Ayrıca, alışveriş sepeti state’ini yönetmek üzere bir slice tanımladığınızı varsayarak, reducer fonksiyonu  **cartReducer** ’ı **CartSlice** dosyasından import eder.

### 🧩 Store Yapılandırması

 **configureStore** , store yapılandırma seçeneklerini içeren bir nesneyle çağrılır. **reducer** özelliği, her anahtarın bir state slice’ını temsil ettiği ve her değerin ilgili reducer fonksiyonunu temsil ettiği bir nesne olarak belirtilir.

Bu durumda,  **cartReducer** , state’in **cart** slice’ı ile ilişkilendirilir. Bu, **cartReducer** tarafından yönetilen state’in Redux store içinde **cart** anahtarı altında saklanacağı anlamına gelir.

### ⚙️ Diğer Store Yapılandırma Seçenekleri

 **configureStore** ’a verilen nesneye ek yapılandırma seçenekleri eklenebilir. Örneğin, middleware, enhancers veya devtools yapılandırması gibi seçenekler ekleyebilirsiniz.

### 📤 Store’u Export Etme

Son olarak, yapılandırılmış Redux store ( **store** ) modülden export edilir ve uygulama genelinde kullanılabilir hale gelir.

```js
import { configureStore } from '@reduxjs/toolkit';
import cartReducer from './Components/CartSlice';
const store = configureStore({
 reducer: {
 cart: cartReducer,
 },
});
export default store;
```

4. Şimdi bu veriyi uygulamadaki herhangi bir bileşen için global olarak kullanılabilir yapmak üzere, veriyi **main.jsx** bileşeninde import etmeniz gerekir. Bunun için **main.jsx** dosyasına gidin ve aşağıdaki kodu dosyaya yapıştırın.

```jsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { Provider } from 'react-redux'
import store from './store.js'
ReactDOM.createRoot(document.getElementById('root')).render(
 <React.StrictMode>
<Provider store={store}>
 <App />
 </Provider>
 </React.StrictMode>,
)
```

Yukarıdaki kodda **store.js** dosyası `<React.StrictMode>` içinde import edilir.  *react-redux* ’ten `<Provider>`, store’u prop olarak geçirerek Redux store’u hiyerarşisi içindeki tüm bileşenlere sağlar. Bu, `<App />` dahil bileşenlerin state yönetimi için Redux store’a erişmesine ve onunla etkileşime girmesine olanak tanır.

---

## 🧺 Adım 7: Ürün ve Store Verisini Global Olarak Ekleme

1. **ProductList** bileşeninin içinde  **dispatch** ’i başlatın ve Redux store’dan  **cartItems** ’a erişmek için **useSelector** kullanın.

```js
const dispatch = useDispatch();
const cartItems = useSelector(state => state.cart.cartItems); // Get cart items globally
```

Verilen ifadeyi bileşenin üst kısmına eklediğinizden emin olun.

```js
import { useDispatch, useSelector } from 'react-redux';
import { addItemToCart } from './CartSlice';// Action to add product to cart
```

Yukarıdaki kodda  **addItemToCart** , hangi ürünün store.js’e eklendiğini dispatch etmek için reducer fonksiyon detayını almak üzere kullanılır.

2. **ProductList** bileşeninde, veriyi sepete ekleme ve Redux’taki global state’i kullanarak **“Add to Cart”** butonunu devre dışı bırakma işlevini uygulayın. `<button>` etiketi içinde **onClick** olayı için **handleAddToCart** fonksiyonunu çağırın.

```jsx
<button
 className={`add-to-cart-btn ${cartItems.some(item => item.id === product.id) ? 'disabled' : ''}`}
 onClick={() => handleAddToCart(product)}
 disabled={cartItems.some(item => item.id === product.id)} // Disable if already in cart
>
 {cartItems.some(item => item.id === product.id) ? 'Added' : 'Add to Cart'}
</button>
```

Bu buton tıklandığında, ürünü argüman olarak alarak **handleAddToCart** fonksiyonunu çağırır. Butonun görünümü, ürünün *disabledProducts* dizisine dahil olup olmadığına göre dinamik olarak belirlenir; ürün dizideyse veya ürün eklendiyse buton devre dışı kalır. Bu işlev, sepete aynı öğenin tekrar eklenmesini engeller ve gerekli durumlarda butonu devre dışı biçimde stil vererek görsel geri bildirim sağlar.

3. **handleAddToCart** adlı fonksiyonu başlatın.

```js
const handleAddToCart = product => {
 dispatch(addItemToCart(product));// Add product to cart
 };
```

**ProductList.jsx kodu için buraya tıklayın**

```jsx
import React from 'react';
import './ProductList.css';
import { useDispatch, useSelector } from 'react-redux';
import { addItemToCart } from './CartSlice';// Action to add product to cart
const ProductList = () => {
 const dispatch = useDispatch();
 const cartItems = useSelector(state => state.cart.cartItems); // Get cart items globally
 const products = [
 { id: 1, name: 'Product A', price: 60 },
 { id: 2, name: 'Product B', price: 75 },
 { id: 3, name: 'Product C', price: 30 },
 ];
 const handleAddToCart = product => {
 dispatch(addItemToCart(product));// Add product to cart
 };
 return (
 <div className="product-list">
 <h2 className="product-list-title">Products</h2>
 <ul className="product-list-items">
 {products.map(product => (
 <li key={product.id} className="product-list-item">
 <span>{product.name} - ${product.price}</span>
 <button
 className={`add-to-cart-btn ${cartItems.some(item => item.id === product.id) ? 'disabled' : ''}`}
 onClick={() => handleAddToCart(product)}
 disabled={cartItems.some(item => item.id === product.id)} // Disable if already in cart
 >
 {cartItems.some(item => item.id === product.id) ? 'Added' : 'Add to Cart'}
 </button>
 </li>
 ))}
 </ul>
 </div>
 );
};
export default ProductList;
```

---

## 🛒 Adım 8: Alışveriş Sepetinde Ürünleri Gösterme

1. Şimdi **ShoppingCart.jsx** bileşeninde, kullanıcının alışveriş sepetine eklediği öğeleri gösteren bir mantık oluşturacaksınız. Sepeti Redux kullanarak yönetmek ve kullanıcının ne satın aldığını takip etmek için Redux adlı özel bir araç kullanır. Bileşen, kullanıcının sepetteki öğeleri, fiyatlarını ve her bir öğeden kaç tane eklediğini görmesini sağlar. Kullanıcılar ayrıca öğeleri sepetten kaldırabilir veya her bir öğenin miktarını değiştirebilir. Bu, kullanıcının satın alacaklarını takip etmesine yardımcı olan sanal bir alışveriş sepeti gibidir.
2. Bunu uygulamak için **src** klasörü altındaki **ShoppingCart.jsx** bileşenine gidin.
3. Bu bileşenin temel yapısı, ekran görüntüsünde gösterildiği gibi olacaktır.
4. Verilen işlevleri uygulayın:

### 📥 Import

Bileşen; gerekli bağımlılıkları import eder: React,  *react-redux* ’ten  **useDispatch** , **useSelector** ve  **CartSlice** ’tan action creator’lar ( **removeItemFromCart** ,  **clearCart** ,  **increaseItemQuantity** ,  **decreaseItemQuantity** ).

```js
import { useDispatch, useSelector } from 'react-redux';
import { removeItemFromCart, clearCart, increaseItemQuantity, decreaseItemQuantity } from './CartSlice'; // Assuming you have action 
```

### 🧩 Function Component

**ShoppingCart** bileşeni, arrow function sözdizimi kullanılarak tanımlanan bir functional component’tir.

### 🪝 Redux Hooks

Bileşen, Redux store ile etkileşim kurmak için  *react-redux* ’ten **useDispatch** ve **useSelector** hook’larını kullanır. **useDispatch** action dispatch etmek için, **useSelector** ise Redux store’dan veri çıkarmak için kullanılır.

### 📦 State Retrieval

**cartItems** değişkeni, store state’inden **state.cart.cartItems** seçilerek öğelerin dizisini alır.  **totalAmount** , **cartItems** üzerinde dolaşarak her öğenin fiyatını miktarıyla çarpar ve toplayarak toplam tutarı hesaplar.

```js
const dispatch = useDispatch();
 const cartItems = useSelector(state => state.cart.cartItems);
 const totalAmount = cartItems.reduce((total, item) => total + item.price * item.quantity, 0);
```

Yukarıdaki kodu function component’in  **return** ’ünden önce ekleyin.

### 🎛️ Event Handlers

 **handleRemoveItem** , kaldırılacak öğenin ID’si ile **removeItemFromCart** action’ını dispatch eder.  **handleClearCart** , sepeti temizlemek için **clearCart** action’ını dispatch eder.  **handleIncreaseQuantity** , belirli bir öğenin miktarını artırmak için **increaseItemQuantity** action’ını dispatch eder.  **handleDecreaseQuantity** , belirli bir öğenin miktarını azaltmak için **decreaseItemQuantity** action’ını dispatch eder.

```js
const handleRemoveItem = itemId => {
 dispatch(removeItemFromCart(itemId));
 };
 const handleClearCart = () => {
 dispatch(clearCart());
 };
 const handleIncreaseQuantity = itemId => {
 dispatch(increaseItemQuantity(itemId));
 };
 const handleDecreaseQuantity = itemId => {
 dispatch(decreaseItemQuantity(itemId));
 };
```

### 🖼️ Rendering

Bileşen; sepet arayüzünü render eder; `<ul>` etiketi içinde **cart-items** sınıf adıyla, sepetteki her öğeyi adı, fiyatı, miktar kontrol düğmeleri (miktarı artırma/azaltma) ve her öğe için bir kaldırma butonuyla listeler. Toplam tutar, 0’dan büyükse sepetin altında görüntülenir.

```jsx
{cartItems.map(item => (
 <li key={item.id} className="cart-item">
 <span>{item.name} - ${item.price}</span>
 <div className="quantity-controls">
 <button onClick={() => handleDecreaseQuantity(item.id)}>-</button>
 <span> {item.quantity}</span>
 <button onClick={() => handleIncreaseQuantity(item.id)}>+</button>
 </div>
 <button className="remove-item-btn" onClick={() => handleRemoveItem(item.id)}>Remove</button>
 </li>
 ))}
```

### 🧹 Button Controls

Miktarı azaltmak veya artırmak için (- ve +) düğmeleri sağlanır. - düğmesine tıklamak öğenin ID’si ile  **handleDecreaseQuantity** ’yi çağırır. + düğmesine tıklamak öğenin ID’si ile  **handleIncreaseQuantity** ’yi çağırır.

Tıklandığında sepetteki tüm öğeleri kaldırmak için **Clear Cart** etiketli bir buton sağlanır; **handleClearCart** fonksiyonunu tetikler.

```jsx
<button className="clear-cart-btn" onClick={handleClearCart}>Clear Cart</button>
```

Ürünler eklendiyse  **totalAmount** ’ı görüntüleyin; aksi halde hiçbir şey render etmeyin.

```jsx
<div>{totalAmount ? <div>'The total amount is {totalAmount}</div> : ''}</div>
```

Bunu parçalayalım:

* En dıştaki `div` öğesi, süslü parantezler `{}` içinde bir ifade içerir.
* İfadenin içinde, JSX’te koşullu render için bir ternary operator vardır (`condition ? expression1 : expression2`).
* **totalAmount** truthy ise, iç içe bir `div` render edilir. Bu `div`, `‘The total amount is {totalAmount}’` string’ini içerir; burada `{totalAmount}`, *totalAmount* değişkeninin değerinin string içine yerleştirilmesi amaçlanır.
* **totalAmount** falsy ise, boş bir string render edilir.
* Ternary işlemin sonucu dıştaki `div` içinde render edilir.

**CartSlice.jsx kodunu görüntülemek için aşağıya tıklayın.**
**CartSlice.jsx kodu için buraya tıklayın**

```js
import { createSlice } from '@reduxjs/toolkit';
const initialState = {
 cartItems: [],
 };
const CartSlice = createSlice({
 name: 'cart',
 initialState,
 reducers: {
 addItemToCart(state, action) {
 const existingItem = state.cartItems.find(item => item.id === action.payload.id);
 if (existingItem) {
 existingItem.quantity += 1;
 } else {
 state.cartItems.push({ ...action.payload, quantity: 1 });
 }
 },
 removeItemFromCart(state, action) {
 state.cartItems = state.cartItems.filter(item => item.id !== action.payload);
 },
 clearCart(state) {
 state.cartItems = [];
 },
 increaseItemQuantity(state, action) {
 const itemToIncrease = state.cartItems.find(item => item.id === action.payload);
 if (itemToIncrease) {
 itemToIncrease.quantity += 1;
 }
 },
 decreaseItemQuantity(state, action) {
 const itemToDecrease = state.cartItems.find(item => item.id === action.payload);
 if (itemToDecrease && itemToDecrease.quantity > 1) {
 itemToDecrease.quantity -= 1;
 }
 },
 }
});
export const {
 addItemToCart,
 removeItemFromCart,
 clearCart,
 increaseItemQuantity,
 decreaseItemQuantity,
 } = CartSlice.actions;
 export default CartSlice.reducer;
```

**ShoppingCart.jsx bileşeninin kodunu görüntülemek için aşağıya tıklayın.**
**ShoppingCart.jsx kodu için buraya tıklayın**

```jsx
import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { removeItemFromCart, clearCart, increaseItemQuantity, decreaseItemQuantity } from './CartSlice'; // Assuming you have action creators fo
import './ShoppingCart.css'; // Import CSS file for component-specific styles
const ShoppingCart = () => {
 const dispatch = useDispatch();
 const cartItems = useSelector(state => state.cart.cartItems);
 const totalAmount = cartItems.reduce((total, item) => total + item.price * item.quantity, 0);
 const handleRemoveItem = itemId => {
 dispatch(removeItemFromCart(itemId));
 };
 const handleClearCart = () => {
 dispatch(clearCart());
 };
 const handleIncreaseQuantity = itemId => {
 dispatch(increaseItemQuantity(itemId));
 };
 const handleDecreaseQuantity = itemId => {
 dispatch(decreaseItemQuantity(itemId));
 };
 return (
 <>
 <div className="shopping-cart">
 <h2 className="shopping-cart-title">Shopping Cart</h2>
 <ul className="cart-items">
 {cartItems.map(item => (
 <li key={item.id} className="cart-item">
 <span>{item.name} - ${item.price}</span>
 <div className="quantity-controls">
 <button onClick={() => handleDecreaseQuantity(item.id)}>-</button>
 <span> {item.quantity}</span>
 <button onClick={() => handleIncreaseQuantity(item.id)}>+</button>
 </div>
 <button className="remove-item-btn" onClick={() => handleRemoveItem(item.id)}>Remove</button>
 </li>
 ))}
 </ul>
 <button className="clear-cart-btn" onClick={handleClearCart}>Clear Cart</button>
 </div>
 <div>{totalAmount ? <div>'The total amount is {totalAmount}</div> : ''}</div>
 </>
 );
};
export default ShoppingCart;
```

---

## ✅ Adım 9: Çıktıyı Kontrol Etme

1. Terminalde React uygulamasının çalışmasını durdurmak için **ctrl+c** yaparak çıkın.
2. Ardından terminale aşağıdaki komutu yazın ve Enter’a basın.

```bash
npm run preview
```

3. React uygulamanızı görüntülemek için, tarayıcınızda React uygulaması için zaten açık olan sayfayı yenileyin. Açık değilse, sol paneldeki **Skills Network** ikonuna tıklayın. Bu işlem  **“SKILLS NETWORK TOOLBOX.”** ’ı açacaktır. Sonra  **“Launch Application”** ’ı seçin. **“Application Port”** alanına **4173** port numarasını girin ve  **.** ’a tıklayın.
4. Sepete ürün ekledikten sonra çıktı, verilen ekran görüntüsündeki gibi görüntülenecektir.
5. Bir ürün daha ekleyin; toplam tutardaki değişimi göreceksiniz.

Lütfen **Add to Cart** butonunun bir ürünü eklemek için yalnızca bir kez kullanılabileceğini unutmayın. Bundan sonra devre dışı kalacaktır ve tekrar tıklasanız bile aynı ürünü eklemeyecektir.

**Not-** En son değişiklikleri görmek için terminalde tekrar **npm run preview** çalıştırmanız gerekir.

Tebrikler! Bir E-Commerce Data Rendering React uygulaması oluşturdunuz!

---

## 🪙 Adım 10: Pratik Görevi

1. Şimdi bu pratik egzersizde, *super coin* kavramını uygulayacağınız bir bileşen daha oluşturacaksınız.

Super coins, bazı e-ticaret platformları veya perakendeciler tarafından müşteri sadakat programlarının bir parçası olarak sunulan bir tür sadakat veya ödül puanıdır. Toplam sepet tutarına göre kullanıcının ne kadar kazandığını görmek için bu işlevselliği oluşturmanız gerekir.

2. Bunun için **Components** klasörünü seçtikten sonra sağ tıklayarak **SuperCoin.jsx** adlı bir Super Coin Component oluşturun.
3. Bileşenin  **return** ’ünden önce, **useState hook** kullanarak **superCoins** değişkenini ve karşılık gelen fonksiyonunu başlatın.
   **İpucu:** Değişkeni 0 ile başlatmak için *useState hook* kullanın.
   **Örnek çözüm için buraya tıklayın**

```js
const [superCoins, setSuperCoins] = useState(0);
```

4. Şimdi, ürün sayısının toplam miktarını almak için Redux store state’inin cart slice’ından  **cartItems** ’ı **useSelector hook** kullanarak çekmeniz gerekir.
   **İpucu:** cart items state’ini almak için *useSelector hook* kullanın.
   **Örnek çözüm için buraya tıklayın**

```js
const cartItems = useSelector(state => state.cart.cartItems);
```

5. Ardından, **cartItems** dizisindeki her öğe için fiyat ve miktarın çarpımını toplayarak toplam tutarı **reduce** metoduyla hesaplayın.
   **İpucu:** cart items state’ini almak için *useSelector hook* kullanın.
   **Örnek çözüm için buraya tıklayın**

```js
const totalAmount = cartItems.reduce((total, item) => total + item.price * item.quantity, 0);
```

6. Şimdi  **totalAmount** ’a göre **superCoins** state’ini güncellemeniz gerekir: toplam tutarın farklı aralıkları için 10, 20 veya 30 coin olarak ayarlayın; tutar 100’ün altındaysa 0 olarak ayarlayın. Bu effect, **totalAmount** her değiştiğinde çalışır.
   **İpucu:** superCoins state’ini güncellemek için *useEffect hook* kullanın.
   **Örnek çözüm için buraya tıklayın**

```js
useEffect(() => {
 if (totalAmount >= 100 && totalAmount < 200) {
 setSuperCoins(10);
 } else if (totalAmount >= 200 && totalAmount < 300) {
 setSuperCoins(20);
 } else if (totalAmount >= 300) {
 setSuperCoins(30);
 } else {
 setSuperCoins(0);
 }
}, [totalAmount]);
```

7. Şimdi function component’in return’ü içinde JSX sözdizimiyle `<div>` oluşturun ve `<div>` etiketi içinde **superCoins** state değişkenini entegre edin.
   **İpucu:** superCoins değişkenini eklemek için `{}` kullanın.
   **Örnek çözüm için buraya tıklayın**

```jsx
<div className="super-coins" style={{textAlign:'center'}}>
 <h2 className="super-coins-title">Super Coins</h2>
 <p className="super-coins-info">You will earn {superCoins} super coins with this purchase.</p>
</div>
```

8. Bileşeni  **App** ’e bağlayın: **SuperCoin** bileşenini **App.jsx** (ana uygulama dosyası) içine import edin ve sayfada render edilmesi için JSX içinde `<SuperCoin />` bileşenini ekleyin.
   **Örnek çözüm için buraya tıklayın**

```jsx
// App.js
import React from 'react';
import ProductList from './Components/ProductList';
import ShoppingCart from './Components/ShoppingCart';
import './App.css'
import SuperCoin from './Components/SuperCoin'
const App = () => {
 return (
 <div>
 <h1 className='app-heading'>E-Commerce Application</h1>
 <ProductList />
 <ShoppingCart />
 <SuperCoin />
 </div>
 );
};
```

9. **Çıktıyı kontrol edin**
   Değişiklikleri kaydedin ve uygulamayı yeniden çalıştırın.
   Ürünü sepete ekleyin ve tutar  **$100** ’a ulaştığında, **10 Super Coins** kazandığınızı gösterecektir.
10. Tutarı artırabilirsiniz; mantığa bağlı olarak *supercoins* değeri de artacaktır.

---

## 🏁 Sonuç

Tebrikler! Bir E-Commerce React uygulaması oluşturdunuz!

Bu lab’de şunları yaptınız:

* Uygulama genelinde evrensel state yönetimi için Redux Toolkit’i uyguladınız.
* React ve Redux kullanarak temel bir e-ticaret platformu geliştirdiniz.
* Her öğe için “Add to Cart” butonu bulunan bir ürün listesi sundunuz.
* Kullanıcıların sepete eklenen öğeleri görüntülemesini ve yönetmesini sağladınız; buna öğeleri kaldırma da dahildir.
* Global veri erişilebilirliği sağlayarak Redux ile etkileşim kurmak için **useDispatch** ve **useSelector** hook’larını kullandınız.
* Uygulama genelinde sorunsuz state yönetimi sağlayarak kullanıcı deneyimini ve ölçeklenebilirliği geliştirdiniz.

## ✍️ Yazar(lar)

Richa Arora

© IBM Corporation. Tüm hakları saklıdır.
