
# 🧩 Uygulama Projesi: Konferans Gider Planlayıcı

**Tahmini gereken süre:** 90 dakika

---

## 🧠 Görevi anlayın

Alejandre, iş konferansları için bir mekân yönetir. Ana şirketi  **“BudgetEase”** , BudgetEase müşterilerinin konferans etkinliklerini kolayca fiyatlandırabilmesi için bir web sitesi geliştirmeniz üzere sizi işe almak istiyor.

Uygulamanın gereksinimleri; kullanıcıların konferans merkezindeki odaları seçip fiyatlandırabilmesini, mikrofon ve projektör gibi *eklentileri (add-ons)* seçebilmesini ve belirli sayıda misafir için yemekleri seçebilmesini içerir.

**BudgetEase konferans gider planlayıcısının** özellikleri şunları içerecektir:

* Kullanıcı seçimlerine göre gerçek zamanlı güncellenen dinamik bir kullanıcı arayüzü
* Mekân seçimi, eklentiler ve yemek seçenekleri için bileşenler
* Durum değişikliklerini yönetmek için *Redux Toolkit* kullanılarak *Redux* entegrasyonu
* Farklı bölüm durumlarını yönetmek için *Redux slices*
* Seçilen öğeleri ve maliyetlerini açılır bir pencerede tablo ile gösterme
* Kullanıcı seçimlerine göre ara toplamları ve genel toplam maliyeti hesaplama ve gösterme

---

## 🎯 Öğrenme hedefleri

Bu laboratuvarı tamamladıktan sonra şunları yapabileceksiniz:

* **React bileşenleri oluşturma:** Bileşen birleştirme ve iç içe yerleştirme kullanarak fonksiyonel React bileşenleri oluşturma.
* **Hook’larla durum yönetimi:** Özellikle *useState* ve *useEffect* hook’larını uygulama. Hook’ları, bileşen düzeyi durumu yönetmek ve öğelerin görünürlüğünü kontrol etmek için kullanacaksınız.
* **Redux entegrasyonu:** Eylemler ( *actions* ), azaltıcılar ( *reducers* ) ve store gibi Redux kavramlarını kullanarak bir uygulamaya Redux entegre etme.
* **Dinamik veriyi render etme:** Nesne dizilerinden alınan verileri arayüzde dinamik olarak render etme. Bileşen listeleri üretmek için diziler üzerinde *map()* ile dolaşacaksınız.
* **Koşullu render ile olay yönetimi:** Düğme seçimi gibi kullanıcı olaylarını yönetme ve karşılık gelen eylemleri tetikleme.

---

## 🧾 Proje görevleri

1. Proje ortamını kurun
2. *ConferenceEvent.jsx* bileşeninin yapısını inceleyin
3. *Venue* modülünün kodunu inceleyin
4. Güncellemeleri ve durum değişikliklerini yönetmek için Redux’u bileşenlerle birleştirin
5. Ara toplamları ve toplam maliyeti hesaplayan mantığı ekleyin
6. Seçilen ürünleri göstermek için dinamik bir tablo oluşturun; öğe adı, birim maliyet, miktar ve o öğe için toplam maliyeti görüntüleyin
7. Konforlu bir kullanıcı deneyimi için web tasarımı oluşturun
8. Web sitenizi herkese açık bir barındırma hizmetine dağıtın

---

## 🧩 Çözümler

Çözüm kodunu bu laboratuvarın sonunda bulacaksınız. Görevlerden herhangi birini tamamlamakta yardıma ihtiyacınız olursa, orada çalışan kodun önerilen bir sürümünü bulabilirsiniz. Ayrıca, kendi çözümünüzü veya laboratuvarın sonundaki kodu kaydettiğinizden emin olun. Bu, nihai proje için kod geliştirirken size yardımcı olacaktır.

---

## ✅ Ön koşullar

* Temel HTML ve CSS
* Orta düzey JavaScript
* React fonksiyon bileşenleri, hook’lar ve durum yönetimi için *Redux toolkit* ile aşinalık
* GitHub kullanarak kod yönetimi

GitHub’da nasıl çalışılacağıyla ilgili yönlendirmeye ihtiyacınız olursa bu talimatları inceleyin.

---

## ⚠️ Bu laboratuvar ortamıyla ilgili önemli bildirim

*Skills Network Cloud IDE* (Theia ve Docker tabanlı), kurs ve proje laboratuvarlarında uygulamalı çalışmalar için ortam sağlayan açık kaynaklı bir IDE’dir ( *Integrated Development Environment* ).

Bu laboratuvar ortamındaki oturumların kalıcı olmadığını lütfen unutmayın. Bu laboratuvara her bağlandığınızda, sizin için yeni bir ortam oluşturulur. Kodunuzu GitHub’a veya başka bir harici kaynağa kaydetmeden ortamdan çıkarsanız verilerinizi kaybedersiniz. Veri kaybını önlemek için bu laboratuvarları tek bir oturumda tamamlamayı planlayın.

---

# 🧰 Görev 1: Ortamı kurma

## 🧷 1. Depoyu fork’layın

React uygulamanız için GitHub deposunu fork’lamanız gerekir. Bu proje için iskelet kodun bulunduğu GitHub deposu şuradadır:

[https://github.com/ibm-developer-skills-network/conference_event_planner.git](https://github.com/ibm-developer-skills-network/conference_event_planner.git)

Yukarıdaki bağlantıyı takip ettikten sonra **fork** düğmesine tıklayın.

Bu depo, bu laboratuvar için React uygulamasının temel yerleşimini içerir.

## 🧬 2. Depoyu klonlayın

Depoyu **git clone `<repository-link>`** komutunu kullanarak klonlayın.

`<repository-link>` ifadesini, fork’ladığınız **conference_event_planner** deposunun bağlantısıyla değiştirin.

```bash
git clone <repository-link>
```

Depoyu klonladıktan sonra, “Project” klasörü altında **conference_event_planner** adlı bir klasör göreceksiniz. Ekran görüntüsü dizin yapısını gösterir.

## 💾 3. Çalışmanızı düzenli olarak push edin

Bu fork’lanmış depoyu, yaptığınız işin kaydını tutmak için en son kodunuzu push etmekte kullanacaksınız. Dosyalarınızı periyodik olarak kaydedin. Git komutlarını çalıştırabilmek için dosyalarınızın kaydedilmiş olması gerekir.

## 🖼️ 4. Görseller

Projede kendi görsellerinizi kullanabilir veya telifsiz görseller sağlayan Pixabay’den önerilen görselleri kullanabilirsiniz.

* Conference room
  [https://pixabay.com/photos/chairs-empty-office-room-table-2181916/](https://pixabay.com/photos/chairs-empty-office-room-table-2181916/)
* Auditorium:
  [https://pixabay.com/photos/event-venue-auditorium-meeting-1597531/](https://pixabay.com/photos/event-venue-auditorium-meeting-1597531/)
* Presentation room:
  [https://pixabay.com/photos/convention-center-chair-seminar-3908238/](https://pixabay.com/photos/convention-center-chair-seminar-3908238/)
* Meeting room:
  [https://pixabay.com/photos/chairs-empty-office-room-table-2181916/](https://pixabay.com/photos/chairs-empty-office-room-table-2181916/)
* Small meeting room:
  [https://pixabay.com/photos/laptops-meeting-businessmen-593296/](https://pixabay.com/photos/laptops-meeting-businessmen-593296/)
* Projector:
  [https://pixabay.com/photos/business-computer-conference-20031/](https://pixabay.com/photos/business-computer-conference-20031/)
* Speakers:
  [https://pixabay.com/photos/speakers-bluetooth-tech-speaker-4109274/](https://pixabay.com/photos/speakers-bluetooth-tech-speaker-4109274/)
* Microphone:
  [https://pixabay.com/photos/public-speaking-mic-microphone-3926344/](https://pixabay.com/photos/public-speaking-mic-microphone-3926344/)
* Whiteboard:
  [https://pixabay.com/photos/whiteboard-dry-erase-marker-blank-2903269/](https://pixabay.com/photos/whiteboard-dry-erase-marker-blank-2903269/)
* Signs:
  [https://pixabay.com/photos/signpost-waypoint-wood-grain-board-235079/](https://pixabay.com/photos/signpost-waypoint-wood-grain-board-235079/)

## 📁 5. Terminal yolunu değiştirin

Terminal yolunuzu aşağıdaki komutla **conference_event_planner** klasörüne değiştirin.

```bash
cd conference_event_planner
```

## ✅ 6. Klonladığınız kodun doğru çalıştığından emin olun

Uygulamayı çalıştırmak için gerekli paketleri *npm* ile yükleyin.

```bash
npm install
```

Uygulamayı çalıştırmak için aşağıdaki komutu yürütün. Bu komut, 4173 port numarası üzerinde uygulama sunucusunu başlatır.

```bash
npm run preview
```

## 🌐 7. Uygulamayı görüntüleyin

Şimdi uygulamayı görüntüleyebilirsiniz.

Sol paneldeki *Skills Network* simgesine tıklayın (1 numaraya bakın). Bu işlem  *Skills Network Toolbox* ’ı açacaktır. Ardından  **Launch Application** ’a tıklayın (2 numaraya bakın). **Application Port** alanına **4173** port numarasını girin (3 numaraya bakın) ve **[↗]** simgesine tıklayın.

## 🧭 8. Beklenen çıktı

Çıktı aşağıdaki ekran görüntüsüne benzer olmalıdır. **Get Started** düğmesine tıklamak, kullanıcıyı ürün seçimi sayfasına götürmelidir. Üst bilgi ve ilk bölüm **“Room selection”** görünmelidir.

> *Not:* Size *backgroundImage* yerine *backgroundColor* sağlanmıştır. Renk yerine görsel tercih ediyorsanız, kendi görselinizi ekleyebilirsiniz. Verilen kodla uygulama ürün sayfası aşağıdakine benzer görünmelidir.

## 🔄 9. Değişiklik yaptıysanız push edin

Herhangi bir değişiklik yaparsanız **git add** ve **git commit** çalıştırın. Ardından, commit edilen değişiklikleri uzak GitHub deponuza yüklemek için **git push** komutunu çalıştırın ve kodunuzun en son sürümünü kaydettiğinizden emin olun.

> *Not:* Kodu GitHub deponuza push ederken kullanıcı adı ve parola girmeniz istenebilir. GitHub’da nasıl çalışılacağıyla ilgili daha fazla yönlendirme gerekiyorsa ilgili talimatları inceleyin.

---

# 🧩 Görev 2: ConferenceEvent.jsx yapısını gözden geçirin

İki çalışan modülünüz vardır:

* Başlamak için bir düğme ve şirket açıklaması içeren açılış sayfası
* Mekândaki oda seçimini ve artırma/azaltma düğmelerini içeren **“venue section”**

**src** dizinindeki **ConferenceEvent.jsx** dosyasını açın. Bu bileşen ürün seçimi sayfası için fonksiyonları ve yerleşimleri içerir.

## 🧱 Yerleşimler

* Bir *navbar* öğesi
* `<div>` etiketi içinde **main_container** sınıfı
* Koşullu operatör `? :` kullanarak işlevi aç/kapat eden bir **showItems** değişkeni
* `<div>` etiketi içinde **items-information** sınıfı
* Mekân, eklentiler ve yemekler için `<div>` etiketlerinde yerleşimler. Bu yerleşimlerin her birinde iki ortak sınıf adı bulunur: **venue_container** ve **container_main**
* Seçilen öğelerin ayrıntılarını göstermek için `<div>` içinde **total_amount_detail** sınıfı

---

# 🏢 Görev 3: Venue modülü kodunu gözden geçirin

Sonraki adımda, size sağlanan mekân oda seçimi işlevselliği kodunu inceleyeceksiniz. Durum akışına ve **ConferenceEvent** bileşeninin **venueSlice** ile birlikte nasıl çalıştığına odaklanın. Mekân oda seçimi işlevselliği kodu üç dosyadadır:  **venueSlice.js** , **ConferenceEvent.jsx** ve  **store.js** . Bu dosyalardaki kodu ve aralarındaki etkileşimleri inceleyelim.

Mekân işlevselliği, *Redux toolkit* içinden **createSlice()** fonksiyonunu içe aktararak  *slice* ’ları kullanır.  *Slice* , uygulama durumunuzu daha küçük özelliklere böler; bu da kodunuzu düzenlemenize, daha okunabilir hâle getirmenize ve bakımını basitleştirmenize yardımcı olur.

## 🧩 venueSlice.js

**venueSlice.js** dosyasındaki kodu adım adım inceleyelim. Bu dosya, *@reduxjs/toolkit* içinden **createSlice** kullanarak mekân seçimine ilişkin Redux durumunu dilimleyen kodu içerir.

1. Başlangıç durumu ( *initial state* ), her biri mekânda kiralanabilir bir odayı temsil eden *venue* nesnelerinden oluşan bir dizidir. Bir venue nesnesi; küçük resim görseli, ad, maliyet ve miktar gibi özelliklere sahiptir.
2. **venueSlice.js** dosyası, durumdaki venue öğelerinin sayısını yönetmek için **incrementQuantity** ve **decrementQuantity** adlı *reducer* fonksiyonlarını içerir.

> *Not:* Bu laboratuvarın son sayfasında, uygun atıflarla Pixabay görsel bağlantıları sağlıyoruz; ayrıca kendi görsellerinizi de bulabilirsiniz.

### ➕ incrementQuantity()

Bu fonksiyon, durumdaki bir venue öğesinin miktarını artırmayı yönetir. Artırılacak öğenin indeksini içeren bir action alır.

Önce, verilen indekste durum içinde öğenin var olup olmadığını kontrol eder. Öğe mevcutsa ve **Auditorium Hall** olup miktarı 3’e eşit veya büyükse, durumu değiştirmeden erken döner.

Aksi hâlde, öğenin miktarını 1 artırır.

### ➖ decrementQuantity()

Bu fonksiyon, durumdaki bir venue öğesinin miktarını azaltmayı yönetir. Azaltılacak öğenin indeksini içeren bir action alır.

Önce, verilen indekste öğenin var olup olmadığını ve miktarının 0’dan büyük olup olmadığını kontrol eder.

Her iki koşul da sağlanırsa, öğenin miktarı 1 azaltılır.

```js
reducers: {
 incrementQuantity: (state, action) => {
 const { payload: index } = action;
 if (state[index]) {
 if (state[index].name === "Auditorium Hall (Capacity:200)" && state[index].quantity >= 3) {
 return; }
 state[index].quantity++;
 }
 },
 decrementQuantity: (state, action) => {
 const { payload: index } = action;
 if (state[index] && state[index].quantity > 0) {
 state[index].quantity--;
 }
 },
 },
```

---

## 🗄️ Redux Store kurulumu

Şimdi **store.js** dosyasına bakalım.

1. *@reduxjs/toolkit* içinden **configureStore()** fonksiyonuyla Redux store’u oluşturun.
2. **store.js** dosyası, **venueSlice.js** içinden içe aktarılan **venue()** adlı bir reducer içerir.

```js
import { configureStore } from '@reduxjs/toolkit';
import venueReducer from './venueSlice';
export default configureStore({
 reducer: {
 venue: venueReducer,
 },
});
```

3. Bu kod, *@reduxjs/toolkit* **configureStore()** fonksiyonunu kullanarak global bir Redux store oluşturur; böylece uygulamadaki tüm bileşenler **venueReducer()** tarafından yönetilen duruma erişebilir.

---

## 🧩 ConferenceEvent bileşeni

Şimdi **ConferenceEvent.jsx** dosyasından ilgili kodu inceleyelim.

### 1) Gerekli bağımlılıkları içe aktarın

```js
import { useSelector, useDispatch } from "react-redux";
import { incrementQuantity, decrementQuantity } from "./venueSlice";
```

### 2) useSelector() ile venue öğelerini alın

```js
const venueItems = useSelector((state) => state.venue);
```

### 3) Artırma/azaltma için olay işleyicilerini tanımlayın

```js
const handleAddToCart = (index) => {
 if (venueItems[index].name === "Auditorium Hall (Capacity:200)" && venueItems[index].quantity >= 3) {
 return; // Prevent further additions
 }
 dispatch(incrementQuantity(index));
};
const handleRemoveFromCart = (index) => {
 if (venueItems[index].quantity > 0) {
 dispatch(decrementQuantity(index));
 }
};
```

### 4) Auditorium Hall için kalan miktarı hesaplayın

Kullanıcının üç adetten fazla istememesini sağlamak için, kullanılabilir auditorium hall sayısını 3’e göre kalan olarak hesaplar:

```js
const remainingAuditoriumQuantity = 3 - venueItems.find(item => item.name === "Auditorium Hall (Capacity:200)").quantity;
```

### 5) Seçilen odaların toplam maliyetini hesaplayın

Kullanıcı odaların sayısını artırıp azalttığında, sistem seçilen tüm odaların maliyetini hesaplamalıdır.

Bunun için bir **calculateTotalCost()** fonksiyonu tanımlanır ve **venueTotalCost** değişkeni atanır.

```js
const calculateTotalCost = (section) => {
 let totalCost = 0;
 if (section === "venue") {
 venueItems.forEach((item) => {
 totalCost += item.cost * item.quantity;
 });
 }
 return totalCost;
};
const venueTotalCost = calculateTotalCost("venue");
```

* Fonksiyon, ok fonksiyonu sözdizimiyle tanımlanır ve **calculateTotalCost** sabitine atanır.
* Bir string parametre alır:  **section** . Bu, hangi bölümün hesaplanacağını belirtir.
* **totalCost** , 0 ile başlatılır ve ilgili bölüm için kümülatif toplamı tutar.
* **section** değeri `"venue"` ise, **venueItems** dizisi üzerinde **forEach** ile dolaşılır. Her öğe için `item.cost * item.quantity` hesaplanıp  **totalCost** ’a eklenir.
* Döngü bittiğinde **totalCost** döndürülür.
* **calculateTotalCost("venue")** çağrısının sonucu **venueTotalCost** olarak saklanır.

### 6) Toplam maliyeti gösterin

```jsx
<div className="total_cost">Total Cost: ${venueTotalCost}</div>
```

---

# ➕ Görev 4: Add-ons için kod yazın

Bu bölümde, add-ons bölümünü oluşturacaksınız. Başlamak için önce **src** klasörü altındaki **avSlice.js** içinde mantığı oluşturmanız gerekir.

## 🧱 Başlangıç verisini oluşturun (initialState)

Veri yapısı sağlamak için **initialState** dizi değişkenini nesnelerle başlatın. Aşağıdaki veride kendi görsellerinizi ve onlara uygun yolları eklemeniz gerektiğini unutmayın. Örnek görsel bağlantıları **Görev 1: Ortamı kurma** bölümünde verilmiştir. Aşağıdaki kodu **avSlice.js** içindeki **initialState** içine ekleyin.

```js
 {
 img: "https://pixabay.com/images/download/business-20031_640.jpg",
 name: "Projectors",
 cost: 200,
 quantity: 0,
 },
 {
 img: "https://pixabay.com/images/download/speakers-4109274_640.jpg",
 name: "Speaker",
 cost: 35,
 quantity: 0,
 },
 {
 img: "https://pixabay.com/images/download/public-speaking-3926344_640.jpg",
 name: "Microphones",
 cost: 45,
 quantity: 0,
 },
 {
 img: "https://pixabay.com/images/download/whiteboard-2903269_640.png",
 name: "Whiteboards",
 cost: 80,
 quantity: 0,
 },
 {
 img: "https://pixabay.com/images/download/signpost-235079_640.jpg",
 name: "Signage",
 cost: 80,
 quantity: 0,
 },
```

---

## ➕➖ Artırma ve azaltma (increment ve decrement)

Şimdi **incrementAvQuantity()** ve **decrementAvQuantity()** fonksiyonlarının mantığını oluşturmanız gerekir.

### incrementAvQuantity()

1. **incrementAvQuantity()** reducer fonksiyonu, durumdaki belirli bir öğenin miktarını artırır.
2. İki parametre alır: **state** ve  **action** .
3. **action.payload** , artırılacak öğenin tanımlayıcısını içerir.
4. Reducer, `state[action.payload]` ile öğeyi alır.
5. Öğe varsa, **quantity** değerini 1 artırır.

```js
incrementAvQuantity: (state, action) => {
 const item = state[action.payload];
 if (item) {
 item.quantity++;
 }
},
```

### decrementAvQuantity()

6. **decrementAvQuantity()** reducer fonksiyonu, durumdaki belirli bir öğenin miktarını azaltır.
7. **incrementAvQuantity()** gibi iki parametre alır: **state** ve  **action** .
8. **action.payload** , azaltılacak öğenin tanımlayıcısını içerir. Reducer, `state[action.payload]` ile öğeyi alır.
9. Öğe varsa ve miktarı 0’dan büyükse, **quantity** değerini 1 azaltır; miktarın 0’ın altına düşmemesini sağlar ve daha fazla kullanılabilir öğe olmadığını belirtir.

```js
decrementAvQuantity: (state, action) => {
 const item = state[action.payload];
 if (item && item.quantity > 0) {
 item.quantity--;
 }
},
```

10. **avSlice.js** içindeki tüm reducer fonksiyonlarını ve action’ları export edin.
11. **avSlice** ’ı **store.js** dosyasına ekleyin. **store.js** dosyasına gidin ve **avSlice.js** dosyasını içe aktarın. Dosya yapısı aşağıdaki gibi görünmelidir.

```js
import { configureStore } from '@reduxjs/toolkit';
import venueReducer from './venueSlice';
import avReducer from './avSlice';
export default configureStore({
 reducer: {
 venue: venueReducer,
 av: avReducer,
 },
});
```

---

## 🖥️ Add-ons detaylarını ekranda gösterin

12. Şimdi **avSlice.js** içinde başlattığınız add-ons detaylarını göstermelisiniz.
13. **ConferenceEvent.jsx** bileşenini açın.  **avSlice.js** ’in reducer’lar aracılığıyla gönderdiği detayları almak için add-on öğelerini *store* içinden **ConferenceEvent.jsx** bileşenine içe aktarın.

```js
const avItems = useSelector((state) => state.av);
```

> *Not:* Yukarıdaki kodu, **ConferenceEvent.jsx** içinde `const venueItems = useSelector((state) => state.venue);` satırından sonra ekleyin.

14. **map()** metodunu kullanarak **avItems** içindeki öğeleri gösterin. Ayrıca miktarı 1 artırıp azaltmak için artırma ve azaltma düğmelerini ekleyin. Kodu aşağıdaki gibi **addons_selection** sınıf adına sahip bir `<div>` içinde yerleştirin.

```jsx
{avItems.map((item, index) => (
 <div className="av_data venue_main" key={index}>
 <div className="img">
 <img src={item.img} alt={item.name} />
 </div>
 <div className="text"> {item.name} </div>
 <div> ${item.cost} </div>
 <div className="addons_btn">
 <button className="btn-warning" onClick={() => handleDecrementAvQuantity(index)}> – </button>
 <span className="quantity-value">{item.quantity}</span>
 <button className=" btn-success" onClick={() => handleIncrementAvQuantity(index)}> + </button>
 </div>
 </div>
))}
```

15. Bu kod, **avItems** adlı bir dizi üzerinde dolaşmak için **map()** fonksiyonunu kullanır; dizi, ses/görüntü öğeleri hakkında bilgi içerir.
16. Dizideki her öğe için **av_data venue_main** sınıfına sahip bir `<div>` oluşturur.
17. Bu `<div>` içinde:

* `<img>` etiketi, öğenin görselini gösterir. Görsel kaynağı `item.img`’den alınır, `alt` metni `item.name` olarak ayarlanır.
* Bir `<div>`, öğe adını (`item.name`) gösterir.
* Bir `<div>`, öğe maliyetini (`item.cost`) dolar cinsinden gösterir.
* **addons_btn** sınıfına sahip bir `<div>` içinde, miktarı ayarlayan düğmeler bulunur:
  * **btn-warning** sınıfındaki ilk düğme, n-dash (–) ile etiketlenmiştir ve seçildiğinde miktarı azaltır. Tıklama olayı `handleDecrementAvQuantity()` fonksiyonuna bağlanır.
  * **btn-success** sınıfındaki ikinci düğme, artı işareti (+) ile etiketlenmiştir ve seçildiğinde miktarı artırır. Tıklama olayı `handleIncrementAvQuantity()` fonksiyonuna bağlanır.

18. Öğenin mevcut miktarı, azaltma ve artırma düğmelerinin arasında gösterilir; bu değer `item.quantity` üzerinden alınır.

---

## 🧷 Action dispatch edin

19. **handleDecrementAvQuantity()** ve **handleIncrementAvQuantity()** fonksiyonları için, bileşen dönmeden önce ilgili fonksiyonların içine aşağıdaki kodu ekleyin.

```js
const handleIncrementAvQuantity = (index) => {
 dispatch(incrementAvQuantity(index));
};
const handleDecrementAvQuantity = (index) => {
 dispatch(decrementAvQuantity(index));
};
```

20. Yukarıdaki kodu uygulamak için, **incrementAvQuantity** ve **decrementAvQuantity** fonksiyonlarını **avSlice** içinden içe aktardığınızdan emin olun. Aşağıdaki import’u **ConferenceEvent.jsx** bileşeninin en üstüne ekleyin.

```js
import { incrementAvQuantity, decrementAvQuantity } from "./avSlice";
```

---

## 🧮 AV toplam maliyetini hesaplayın

21. Tıpkı venueSlice için maliyet hesaplandığı gibi, **calculateTotalCost** fonksiyonu içinde seçilen AV öğeleri için toplam maliyeti hesaplayan mantığı oluşturun.

```js
const calculateTotalCost = (section) => {
 let totalCost = 0;
 if (section === "venue") {
 venueItems.forEach((item) => {
 totalCost += item.cost * item.quantity;
 });
 } else if (section === "av") {
 avItems.forEach((item) => {
 totalCost += item.cost * item.quantity;
 });
 }
 return totalCost;
 };
```

22. Ayrıca **avTotalCost** adlı bir değişken oluşturun ve bu fonksiyonu parametre olarak **av** geçirerek çağırın.

```js
const avTotalCost = calculateTotalCost("av");
```

23. Seçilen AV öğelerinin toplam maliyetini göstermek için, add-ons bölümünde **avTotalCost** değerini ekleyin.

```jsx
<div className="total_cost">Total Cost: {avTotalCost}</div>
```

---

# 🍽️ Görev 5: Yemek seçimi için kod yazın

Bu bölümde, yemek seçimi işlevselliğinin kodunu yazacaksınız. Bu işlevsellik için, yemekleri seçmek üzere onay kutuları ( *checkboxes* ) ekleyeceksiniz; müşteriler bir öğeyi seçmek için kutuyu işaretleyebilir veya seçimi kaldırmak için işareti kaldırabilir.

---

## 🧾 Yemek durumları (Meal states)

1. **src** klasörü içindeki **mealsSlice.js** dosyasına gidin. Bu dosya bir dizi içinde dört yemek öğesi içerir. Aşağıdaki kodu **initialState** değişkeninin içine ekleyin.

```js
{ name: 'Breakfast', cost: 50, selected: false },
{ name: 'High Tea', cost: 25, selected: false },
{ name: 'Lunch', cost: 65, selected: false },
{ name: 'Dinner', cost: 70, selected: false },
```

2. Sonra, reducer içinde durum yönetmek üzere yemek öğelerini seçme veya seçimden çıkarma mantığını oluşturun.

```js
toggleMealSelection: (state, action) => {
 state[action.payload].selected = !state[action.payload].selected;
},
```

3. **toggleMealSelection** fonksiyonu, durumdaki belirli bir öğenin **selected** özelliğini değiştirir. Mevcut durumu ve bir action nesnesini alır; güncellenecek öğeyi belirlemek için **action.payload** kullanır. Ardından, seçili olma durumunu **true** ile **false** arasında değiştirir.

**mealsSlice.js** koduna bakın.

---

## 🗄️ Reducer’ları store’a ekleyin

4. Sonra, **mealsSlice.js** dosyasını içe aktarmak için reducer detaylarını **store.js** dosyasında düzenleyin.

```js
import { configureStore } from '@reduxjs/toolkit';
import venueReducer from './venueSlice';
import avReducer from './avSlice';
import mealsReducer from './mealsSlice';
export default configureStore({
 reducer: {
 venue: venueReducer,
 av: avReducer,
 meals: mealsReducer,
 },
});
```

---

## 🧾 Yemek öğelerini görüntüleyin

5. Şimdi, **mealsSlice.js** içinde başlattığınız yemek öğelerinin detaylarını göstermeniz gerekir. Bunun için **ConferenceEvent.jsx** dosyasını açın.
6. **mealsSlice.js** ’in reducer’lar aracılığıyla gönderdiği detayları almak için, yemek öğelerini *store* içinden **ConferenceEvent.jsx** bileşenine içe aktarın.

```js
const mealsItems = useSelector((state) => state.meals);
```

---

## 👥 Kişi sayısı için giriş kutusu ekleyin

7. Toplam kişi sayısını almak için, **input-container** sınıf adına sahip `<div>` içine bir giriş kutusu ekleyin.

```jsx
<div className="input-container venue_selection">
 <label htmlFor="numberOfPeople"><h3>Number of People:</h3></label>
 <input type="number" className="input_box5" id="numberOfPeople" value={numberOfPeople}
 onChange={(e) => setNumberOfPeople(parseInt(e.target.value))}
 min="1"
 />
</div>
```

8. Yukarıdaki kod, kişi sayısını belirtmek için etiketli bir giriş alanı oluşturur. Minimum değeri 1 olan number tipinde bir `<input>` kullanır ve kullanıcının girdiği değeri `parseInt` ile tamsayıya çevirerek **numberOfPeople** durumunu günceller.

---

## ✅ Checkbox’larla yemekleri listeleyin

9. Yemek öğelerini göstermek için, add-ons bölümünde yaptığınız gibi **meal_selection** sınıfına sahip `<div>` içinde **map()** ile diziyi dolaşmalısınız.

```jsx
<div className="meal_selection">
 {mealsItems.map((item, index) => (
 <div className="meal_item" key={index} style={{ padding: 15 }}>
 <div className="inner">
 <input type="checkbox" id={ `meal_${index}` }
 checked={ item.selected }
 onChange={() => handleMealSelection(index)}
 />
 <label htmlFor={`meal_${index}`}> {item.name} </label>
 </div>
 <div className="meal_cost">${item.cost}</div>
 </div>
 ))}
</div>
```

10. Bu kodu adım adım inceleyelim.

* `<div className="meal_selection">` yemek öğeleri listesini tutan kapsayıcıdır.
* `{mealsItems.map((item, index) => ( ... ))}` mealsItems dizisi üzerinde dolaşır ve her öğe için HTML üretir.
* `<div className="meal_item" key={index} style={{ padding: 15 }}>` her yemek öğesi için kapsayıcıdır. React’in listedeki öğeleri takip edebilmesi için **key** gereklidir.
* `<input type="checkbox" ... />` onay kutusudur. Öğenin **selected** özelliği, checkbox’ın **checked** durumunu kontrol eder. Checkbox durumu değiştiğinde, `handleMealSelection(index)` tetiklenir.
* `<label ...>{item.name}</label>` etiket checkbox ile ilişkilidir; etikete tıklamak checkbox’ı değiştirir.
* `<div className="meal_cost">${item.cost}</div>` her yemek öğesinin maliyetini gösterir.

---

## 🧮 handleMealSelection() mantığını ekleyin

11. Kişi sayısına göre yemek ara toplamını hesaplamak için **ConferenceEvent.jsx** dosyasındaki **handleMealSelection()** fonksiyonunda mantığı oluşturmanız gerekir.

```js
const handleMealSelection = (index) => {
 const item = mealsItems[index];
 if (item.selected && item.type === "mealForPeople") {
 // Ensure numberOfPeople is set before toggling selection
 const newNumberOfPeople = item.selected ? numberOfPeople : 0;
 dispatch(toggleMealSelection(index, newNumberOfPeople));
 }
 else {
 dispatch(toggleMealSelection(index));
 }
};
```

12. **handleMealSelection()** fonksiyonunun açıklaması:

* Fonksiyon, seçimi tetikleyen yemek öğesinin indeks parametresini alır
* Verilen indeksle mealsItems dizisinden yemek öğesi nesnesini alır
* Alınan öğenin hem seçili olup olmadığını ( **item.selected === true** ) hem de türünün **mealForPeople** olup olmadığını kontrol eder
* Bu iki koşul sağlanırsa, seçimi değiştirmeden önce numberOfPeople durumunu güncellemeye hazırlanır
* Öğenin türü mealForPeople ise ve zaten seçiliyse, mevcut numberOfPeople korunur
* Seçili değilse, numberOfPeople 0’a ayarlanır
* İndeksi ve gerekiyorsa yeni kişi sayısını geçirerek **toggleMealSelection** action’ını dispatch eder
* Öğenin türü mealForPeople değilse veya seçili değilse, ek bir değerlendirme olmaksızın seçimi değiştirmek için action dispatch eder

13. Yukarıdaki **handleMealSelection()** fonksiyonunda, **mealsSlice.jsx** dosyasından **toggleMealSelection** fonksiyonunu dispatch ediyorsunuz. Bunun için, **“./mealsSlice”** içinden toggleMealSelection’ı içe aktardığınızdan emin olun.

```js
import { toggleMealSelection } from "./mealsSlice";
```

---

## 🧮 Seçilen yemeklerin toplam maliyetini hesaplayın

14. **calculateTotalCost** fonksiyonu içinde, kişi sayısına göre seçilen yemeklerin toplam maliyetini hesaplayan mantığı oluşturun.

```js
const calculateTotalCost = (section) => {
 let totalCost = 0;
 if (section === "venue") {
 venueItems.forEach((item) => {
 totalCost += item.cost * item.quantity;
 });
 } else if (section === "av") {
 avItems.forEach((item) => {
 totalCost += item.cost * item.quantity;
 });
 } else if (section === "meals") {
 mealsItems.forEach((item) => {
 if (item.selected) {
 totalCost += item.cost * numberOfPeople;
 }
 });
 }
 return totalCost;
 };
```

15. **mealsTotalCost** adlı bir değişken oluşturun ve fonksiyonu parametre olarak **meals** geçirerek çağırın.

```js
const mealsTotalCost = calculateTotalCost("meals");
```

16. Seçilen yemeklerin toplam maliyetini göstermek için yemek bölümünde **mealsTotalCost** değerini ekleyin.

```jsx
<div className="total_cost">Total Cost: {mealsTotalCost}</div>
```

---

# 📊 Görev 6: Seçilen öğeleri tabloda gösterin

17. Sonraki adımda, kullanıcı seçtiği öğeleri ve maliyet detaylarını tablolu bir formatta göstermek için kod yazacaksınız. Bu detaylar, kullanıcı üst bilgideki **Show Details** düğmesine tıkladığında görünecektir.
18. **ConferenceEvent.jsx** bileşeni, ternary operatörden `:` sonra aşağıdaki kodu içerir.

```jsx
<div className="total_amount_detail">
 <TotalCost totalCosts={ totalCosts } ItemsDisplay={() => <ItemsDisplay items={ items } />} />
</div>
```

19. Bu kod parçasını inceleyelim.

* **TotalCost** bileşeni, **total_amount_detail** sınıfına sahip bir `<div>` içinde render edilir.
* **TotalCost** bileşeni, **totalCosts** ve **ItemsDisplay** prop’larını alır.
* **totalCosts** prop’u maliyet verisini içerir ve **items** içeren **ItemsDisplay()** bileşeni TotalCost’a prop olarak geçirilir.

---

## 🧮 Ara toplamları hesaplayın (venue, add-ons, meals)

21. Üç seçim türünün her biri için ara toplam hesaplamalısınız:  *venue* , *add-ons* ve  *meals* .
22. Üç ara toplamı içeren **totalCosts** adlı bir nesne oluşturun.

```js
const totalCosts = {
 venue: venueTotalCost,
 av: avTotalCost,
 meals: mealsTotalCost,
};
```

23. Yukarıdaki kodu, fonksiyon bileşeni **ConferenceEvents.jsx** içinde return’den önce ekleyin.

---

## 🧾 Seçilen öğeleri toplayın: getItemsFromTotalCost()

24. Seçilen öğeleri almak için **getItemsFromTotalCost()** fonksiyonunda mantık oluşturmanız gerekir. Aşağıdaki kodu inceleyebilir ve açıklamasını okuyabilirsiniz.

```js
const getItemsFromTotalCost = () => {
 const items = [];
 venueItems.forEach((item) => {
 if (item.quantity > 0) {
 items.push({ ...item, type: "venue" });
 }
 });
 avItems.forEach((item) => {
 if (
 item.quantity > 0 &&
 !items.some((i) => i.name === item.name && i.type === "av")
 ) {
 items.push({ ...item, type: "av" });
 }
 });
 mealsItems.forEach((item) => {
 if (item.selected) {
 const itemForDisplay = { ...item, type: "meals" };
 if (item.numberOfPeople) {
 itemForDisplay.numberOfPeople = numberOfPeople;
 }
 items.push(itemForDisplay);
 }
 });
 return items;
 };
```

25. **getItemsFromTotalCost()** fonksiyonu, kullanıcının seçtiği tüm öğeleri bir dizi içinde tutmak için **items** adlı boş bir dizi oluşturur.
    Her öğe türü (venue, av ve meals) için ayrı bir **forEach()** kullanılır. Bu fonksiyonlar, yalnızca kullanıcının seçtiği öğeleri diziye ekler ve her öğeyi “venue”, “av” veya “meals” olarak etiketler.
    Fonksiyon, üç kategoriden (venue, AV, meals) öğeleri içeren **items** dizisini döndürür.
26. **getItemsFromTotalCost()** fonksiyonu, **ConferenceEvent.jsx** bileşeninde size verilen kodda `const items = getItemsFromTotalCost();` şeklinde çağrılır.

---

## 🧾 Tabloyu oluşturun: ItemsDisplay bileşeni

27. Şimdi, öğe detaylarını tablo olarak göstermek için mantık yazmanız gerekir. **ConferenceEvent.jsx** bileşeninde, **items** değişkeninin prop olarak `{}` içinde geçirildiği boş bir bileşen olan  **ItemsDisplay** ’i göreceksiniz.
28. Bu bileşen için kod aşağıdaki gibidir. Aşağıdaki kodu inceledikten sonra **ItemsDisplay** bileşenine girin.

```jsx
const ItemsDisplay = ({ items }) => {
 console.log(items);
 return <>
 <div className="display_box1">
 {items.length === 0 && <p>No items selected</p>}
 <table className="table_item_data">
 <thead>
 <tr>
 <th>Name</th>
 <th>Unit Cost</th>
 <th>Quantity</th>
 <th>Subtotal</th>
 </tr>
 </thead>
 <tbody>
 {items.map((item, index) => (
 <tr key={index}>
 <td>{item.name}</td>
 <td>${item.cost}</td>
 <td>
 {item.type === "meals" || item.numberOfPeople
 ? ` For ${numberOfPeople} people`
 : item.quantity}
 </td>
<td>{item.type === "meals" || item.numberOfPeople
 ? `${item.cost * numberOfPeople}`
 : `${item.cost * item.quantity}`}
 </td>
 </tr>
 ))}
 </tbody>
 </table>
 </div>
 </>
};
```

29. Bu kodun nasıl çalıştığını gözden geçirelim.

* İlk olarak, öğe listesini konsola yazar; bu test için yardımcıdır.
* Bileşen **display_box1** sınıfına sahip bir `<div>` döndürür. Bu öğe içinde:
  * **items** dizisi boşsa “No items selected” mesajı gösterilir.
  * Dizi öğe içeriyorsa, **table_item_data** sınıfına sahip bir tablo gösterilir.
* Tablo yerleşiminde dört sütun vardır: “Name”, “Unit Cost”, “Quantity” ve “Subtotal”.
* **items** dizisi üzerinde **map()** ile dolaşılır; her öğe bir `<tr>` satırı oluşturur.
* Her satır sırasıyla şunları gösterir:
  * Öğe adı
  * Dolar işaretiyle birlikte birim fiyat
  * Odalar ve add-ons için öğe miktarı
  * Yemekler için “For x people” ifadesi (x kişi sayısıdır)
  * Öğe türüne göre ara toplam: birim maliyet × miktar veya birim maliyet × kişi sayısı

---

# 🧾 Görev 7: TotalCost bileşenini yazın

1. Şimdi, kullanıcı **Show Details** düğmesini seçtiğinde tablodaki öğeleri göstermek için mantığı oluşturmanız gerekir.
2. **src** klasörü altındaki **TotalCost.jsx** bileşenine gidin. Sağlanan temel yerleşimi göreceksiniz. Aşağıdaki gibi görünmelidir:

```js
import React, { useState, useEffect } from 'react';
import "./TotalCost.css";
const TotalCost = ({ totalCosts, ItemsDisplay }) => {
 return (
 <div className="pricing-app">
 <div className="display_box">
 <div className="header">
 <p className="preheading"><h3>Total cost for the event</h3></p>
```

3. Bu kodu gözden geçirelim.

* Dosyanın başındaki import ifadeleri; React’e,  *useState* ’e,  *useEffect* ’e ve `./TotalCost.css` stil dosyasına erişimi sağlar.
* **TotalCost()** fonksiyon bileşeni, **totalCosts** ve **ItemsDisplay** prop’larını parametre olarak alır.
* TotalCost bileşen yapısı, sınıf adlarıyla birlikte birden fazla `<div>` içerir.
* **ConferenceEvent.jsx** bileşeninde **totalCosts** adlı bir nesne, venue, AV ve meals toplamlarını bir araya getirir ve bunları sırasıyla  **venue** , **av** ve **meals** özelliklerine atar.

---

## 🧮 Toplam tutarı hesaplayın

4. Venue, AV ve meals toplamlarını toplayarak toplam tutarı almak için **total_amount** adlı bir değişken oluşturun.
5. Bu değeri,  **totalCosts.venue** , **totalCosts.av** ve **totalCosts.meals** değerlerini toplayarak aşağıdaki gibi hesaplayabilirsiniz:

```js
const total_amount = totalCosts.venue + totalCosts.av + totalCosts.meals;
```

6. Yukarıdaki kodu, fonksiyon bileşeninin return’ünden önce ekleyin.
7. **total_amount** değişkenini, id’si **pre_fee_cost_display** olan bir `<h2>` içinde aşağıdaki gibi gösterin:

```jsx
<h2 id="pre_fee_cost_display" className="price">
 ${total_amount}
</h2>
```

8. Son olarak, öğe detaylarını render etmek için **ItemsDisplay** prop’unu **render_items** sınıfına sahip bir `<div>` içinde kullanın:

```jsx
<div className="render_items">
 <ItemsDisplay />
</div>
```

---

# ✅ Görev 8: Çıktıyı kontrol edin

Artık tüm kodu tamamlamış olmalısınız ve tablonuzun çıktısını kontrol edebilirsiniz.

1. Tüm dosyaları kaydedin ve uygulamayı tekrar çalıştırın. Uygulama tarayıcıda açıksa, tekrar çalıştırdıktan sonra sayfayı yenileyebilirsiniz.
2. **Get Started** düğmesine tıklayın.
3. Venue, add-ons ve meals bölümlerinden birden fazla öğe ekleyin. Ayrıca meals bölümünde kişi sayısını girin.
4. Navbar’daki **Show Details** seçeneğini seçin. Ürün seçimi sayfasında yaptığınız seçimlere göre çıktı görüntülenecektir. Çıktınız aşağıdaki örneğe benzer görünebilir.

---

# 🧾 Özet ve Nihai Çözümler

Bu projede şunları yaptınız:

* Fonksiyon bileşenleri oluşturma
* *ConferenceEvent.jsx* bileşeninin yapısını gözden geçirme
* Uygulama durumlarının farklı bölümlerini yönetmek için *Redux Toolkit* slice’ları kullanma
* Artırma/azaltma işlemlerini gerçekleştirmek ve değerleri dinamik olarak göstermek için Redux action’ları, reducer’ları ve Redux store’u uygulama
* Diziler üzerinde dolaşmak için *map()* fonksiyonunu kullanarak maliyetleri hesaplama ve gösterme
* Seçilen ürünleri tabloyla dinamik şekilde gösterme; öğe adları, birim maliyet, miktar ve ara toplamı görüntüleme

Artık nihai projenizde alışveriş sepeti uygulamasını geliştirmeye hazırsınız.

---

# 🧩 Çözümler

## ✅ avSlice.jsx için çözüm

**Click here to see solution**

```js
 import { createSlice } from "@reduxjs/toolkit";
export const avSlice = createSlice({
 name: "av",
 initialState: [
 {
 img: "",
 name: "Projectors",
 cost: 200,
 quantity: 0,
 },
 {
 img: "",
 name: "Speaker",
 cost: 35,
 quantity: 0,
 },
 {
 img: "",
 name: "Microphones",
 cost: 45,
 quantity: 0,
 },
 {
 img: "",
 name: "Whiteboards",
 cost: 80,
 quantity: 0,
 },
 {
 img: "",
 name: "Signage",
 cost: 80,
 quantity: 0,
 },
 ],
 reducers: {
 incrementAvQuantity: (state, action) => {
 const item = state[action.payload];
 if (item) {
 item.quantity++;
 }
 },
 decrementAvQuantity: (state, action) => {
 const item = state[action.payload];
 if (item && item.quantity > 0) {
 item.quantity--;
 }
 },
 },
});
export const { incrementAvQuantity, decrementAvQuantity } = avSlice.actions;
export default avSlice.reducer;
```

---

## ✅ ConferenceEvent.jsx için çözüm

**Click here to see solution**

```jsx
import React, { useState } from "react";
import "./ConferenceEvent.css";
import TotalCost from "./TotalCost";
import { toggleMealSelection } from "./mealsSlice";
import { incrementAvQuantity, decrementAvQuantity } from "./avSlice";
import { useSelector, useDispatch } from "react-redux";
import { incrementQuantity, decrementQuantity } from "./venueSlice";
const ConferenceEvent = () => {
 const [showItems, setShowItems] = useState(false);
 const [numberOfPeople, setNumberOfPeople] = useState(1);
 const venueItems = useSelector((state) => state.venue);
 const avItems = useSelector((state) => state.av);
 const mealsItems = useSelector((state) => state.meals);
 const dispatch = useDispatch();
 const remainingAuditoriumQuantity = 3 - venueItems.find(item => item.name === "Auditorium Hall (Capacity:200)").quantity;
 
 const handleToggleItems = () => {
 console.log("handleToggleItems called");
 setShowItems(!showItems);
 };
 const handleAddToCart = (index) => {
 if (venueItems[index].name === "Auditorium Hall (Capacity:200)" && venueItems[index].quantity >= 3) {
 return;
 }
 dispatch(incrementQuantity(index));
 };
 
 const handleRemoveFromCart = (index) => {
 if (venueItems[index].quantity > 0) {
 dispatch(decrementQuantity(index));
 }
 };
 const handleIncrementAvQuantity = (index) => {
 dispatch(incrementAvQuantity(index));
};
const handleDecrementAvQuantity = (index) => {
 dispatch(decrementAvQuantity(index));
};
const handleMealSelection = (index) => {
 const item = mealsItems[index];
 if (item.selected && item.type === "mealForPeople") {
 // Ensure numberOfPeople is set before toggling selection
 const newNumberOfPeople = item.selected ? numberOfPeople : 0;
 dispatch(toggleMealSelection(index, newNumberOfPeople));
 }
 else {
 dispatch(toggleMealSelection(index));
 }
};
const getItemsFromTotalCost = () => {
 const items = [];
 venueItems.forEach((item) => {
 if (item.quantity > 0) {
 items.push({ ...item, type: "venue" });
 }
 });
 avItems.forEach((item) => {
 if (
 item.quantity > 0 &&
 !items.some((i) => i.name === item.name && i.type === "av")
 ) {
 items.push({ ...item, type: "av" });
 }
 });
 mealsItems.forEach((item) => {
 if (item.selected) {
 const itemForDisplay = { ...item, type: "meals" };
 if (item.numberOfPeople) {
 itemForDisplay.numberOfPeople = numberOfPeople;
 }
 items.push(itemForDisplay);
 }
 });
 return items;
 };
 const items = getItemsFromTotalCost();
 const ItemsDisplay = ({ items }) => {
 console.log(items);
 return <>
 <div className="display_box1">
 {items.length === 0 && <p>No items selected</p>}
 <table className="table_item_data">
 <thead>
 <tr>
 <th>Name</th>
 <th>Unit Cost</th>
 <th>Quantity</th>
 <th>Subtotal</th>
 </tr>
 </thead>
<tbody>
 {items.map((item, index) => (
 <tr key={index}>
 <td>{item.name}</td>
 <td>${item.cost}</td>
 <td>
 {item.type === "meals" || item.numberOfPeople
 ? ` For ${numberOfPeople} people`
 : item.quantity}
 </td>
<td>{item.type === "meals" || item.numberOfPeople
 ? `${item.cost * numberOfPeople}`
 : `${item.cost * item.quantity}`}
 </td>
 </tr>
 ))}
 </tbody>
 </table>
 </div>
 </>
 };
 const calculateTotalCost = (section) => {
 let totalCost = 0;
 if (section === "venue") {
 venueItems.forEach((item) => {
 totalCost += item.cost * item.quantity;
 });
 } else if (section === "av") {
 avItems.forEach((item) => {
 totalCost += item.cost * item.quantity;
 });
 } else if (section === "meals") {
 mealsItems.forEach((item) => {
 if (item.selected) {
 totalCost += item.cost * numberOfPeople;
 }
 });
 }
 return totalCost;
 };
 const venueTotalCost = calculateTotalCost("venue");
const avTotalCost = calculateTotalCost("av");
const mealsTotalCost = calculateTotalCost("meals");
 const navigateToProducts = (idType) => {
 if (idType == '#venue' || idType == '#addons' || idType == '#meals') {
 if (showItems) { // Check if showItems is false
 setShowItems(!showItems); // Toggle showItems to true only if it's currently false
 }
 }
 }
 const totalCosts = {
 venue: venueTotalCost,
 av: avTotalCost,
 meals: mealsTotalCost,
 };
 return (
 <>
 <navbar className="navbar_event_conference">
 <div className="company_logo">Conference Expense Planner</div>
 <div className="left_navbar">
 <div className="nav_links">
 <a href="#venue" onClick={() => navigateToProducts("#venue")} >Venue</a>
 <a href="#addons" onClick={() => navigateToProducts('#addons')}>Add-ons</a>
 <a href="#meals" onClick={() => navigateToProducts('#meals')}>Meals</a>
 </div>
<button className="details_button" onClick={() => setShowItems(!showItems)}>
 Show Details
 </button>
 </div>
 </navbar>
 <div className="main_container">
 {!showItems
 ?
(
 <div className="items-information">
 <div id="venue" className="venue_container container_main">
 <div className="text">
 <h1>Venue Room Selection</h1>
 </div>
 <div className="venue_selection">
 {venueItems.map((item, index) => ( <div className="venue_main" key={index}>
 <div className="img">
 <img src={item.img} alt={item.name} />
 </div>
 <div className="text">{item.name}</div>
 <div>${item.cost}</div>
 <div className="button_container">
 {venueItems[index].name === "Auditorium Hall (Capacity:200)" ? (
 <>
 <button
 className={venueItems[index].quantity === 0 ? "btn-warning btn-disabled" : "btn-minus btn-warning"}
 onClick={() => handleRemoveFromCart(index)}
 >
 –
 </button>
 <span className="selected_count">
 {venueItems[index].quantity > 0 ? ` ${venueItems[index].quantity}` : "0"}
 </span>
 <button
 className={remainingAuditoriumQuantity === 0? "btn-success btn-disabled" : "btn-success btn-plus"}
 onClick={() => handleAddToCart(index)}
 >
 +
 </button>
 </>
 ) : (
 <div className="button_container">
 <button
 className={venueItems[index].quantity ===0 ? " btn-warning btn-disabled" : "btn-warning btn-plus"}
 onClick={() => handleRemoveFromCart(index)}
 >
 –
 </button>
 <span className="selected_count">
 {venueItems[index].quantity > 0 ? ` ${venueItems[index].quantity}` : "0"}
 </span>
 <button
 className={venueItems[index].quantity === 10 ? " btn-success btn-disabled" : "btn-success btn-plus"}
 onClick={() => handleAddToCart(index)}
 >
 +
 </button>
 
 
 </div>
 )}
 </div>
 </div>
 ))}
 </div>
 <div className="total_cost">Total Cost: ${venueTotalCost}</div>
 </div>
 {/*Necessary Add-ons*/}
<div id="addons" className="venue_container container_main">
 <div className="text">
 <h1> Add-ons Selection</h1>
 </div>
<div className="addons_selection">
 {avItems.map((item, index) => (
 <div className="av_data venue_main" key={index}>
 <div className="img">
 <img src={item.img} alt={item.name} />
 </div>
 <div className="text"> {item.name} </div>
 <div> ${item.cost} </div>
 <div className="addons_btn">
 <button className="btn-warning" onClick={() => handleDecrementAvQuantity(index)}> – </button>
 <span className="quantity-value">{item.quantity}</span>
 <button className=" btn-success" onClick={() => handleIncrementAvQuantity(index)}> + </button>
 </div>
 </div>
))}
 </div>
<div className="total_cost">Total Cost: {avTotalCost}</div>
 </div>
{/* Meal Section */}
<div id="meals" className="venue_container container_main">
 <div className="text">
 <h1>Meals Selection</h1>
 </div>
<div className="input-container venue_selection">
 <div className="input-container venue_selection">
 <label htmlFor="numberOfPeople"><h3>Number of People:</h3></label>
 <input type="number" className="input_box5" id="numberOfPeople" value={numberOfPeople}
 onChange={(e) => setNumberOfPeople(parseInt(e.target.value))}
 min="1"
 />
</div>
 </div>
<div className="meal_selection">
 {mealsItems.map((item, index) => (
 <div className="meal_item" key={index} style={{ padding: 15 }}>
 <div className="inner">
 <input type="checkbox" id={ `meal_${index}` }
 checked={ item.selected }
 onChange={() => handleMealSelection(index)}
 />
 <label htmlFor={`meal_${index}`}> {item.name} </label>
 </div>
 <div className="meal_cost">${item.cost}</div>
 </div>
 ))}
</div>
<div className="total_cost">Total Cost: {mealsTotalCost}</div>
 </div>
 </div>
 ) : (
 <div className="total_amount_detail">
 <TotalCost totalCosts={ totalCosts } ItemsDisplay={() => <ItemsDisplay items={ items } />} />
</div>
 )
 }
 </div>
 </>
 );
};
export default ConferenceEvent;
```

---

## ✅ mealsSlice.jsx için çözüm

**Click here to see solution**

```js
import { createSlice } from '@reduxjs/toolkit';
export const mealsSlice = createSlice({
 name: 'meals',
 initialState: [
 { name: 'Breakfast', cost: 50, selected: false },
{ name: 'High Tea', cost: 25, selected: false },
{ name: 'Lunch', cost: 65, selected: false },
{ name: 'Dinner', cost: 70, selected: false },
 
 ],
 reducers: {
 toggleMealSelection: (state, action) => {
 state[action.payload].selected = !state[action.payload].selected;
 },
 },
});
export const { toggleMealSelection } = mealsSlice.actions;
export default mealsSlice.reducer;
```

---

## ✅ store.js için çözüm

**Click here to see solution**

```js
import { configureStore } from '@reduxjs/toolkit';
import venueReducer from './venueSlice';
import avReducer from './avSlice';
import mealsReducer from './mealsSlice';
export default configureStore({
 reducer: {
 venue: venueReducer,
 av: avReducer,
 meals: mealsReducer,
 },
});
```

---

## ✅ TotalCost.jsx için çözüm

**Click here to see solution**

```js
import React, { useState, useEffect } from 'react';
import "./TotalCost.css";
const TotalCost = ({ totalCosts, ItemsDisplay }) => {
 const total_amount = totalCosts.venue + totalCosts.av + totalCosts.meals;
 return (
 <div className="pricing-app">
 <div className="display_box">
 <div className="header">
 <p className="preheading"><h3>Total cost for the event</h3></p>
 </div>
 <div>
 <h2 id="pre_fee_cost_display" className="price">
 ${total_amount}
</h2>
<div className="render_items">
 <ItemsDisplay />
</div>
 </div>
 </div>
 </div>
 );
};
export default TotalCost;
```

---

## ✅ VenueSlice.jsx için çözüm

**Click here to see solution**

```js
// venueSlice.js
import { createSlice } from "@reduxjs/toolkit";
export const venueSlice = createSlice({
 name: "venue",
 initialState: [
 {
 img: "",
 name: "Conference Room (Capacity:15)",
 cost: 3500,
 quantity: 0,
 },
 {
 img: "",
 name: "Auditorium Hall (Capacity:200)",
 cost: 5500,
 quantity: 0,
 },
 {
 img: "",
 name: "Presentation Room (Capacity:50)",
 cost: 700,
 quantity: 0,
 },
 {
 img: "",
 name: "Large Meeting Room (Capacity:10)",
 cost: 900,
 quantity: 0,
 },
 {
 img: "",
 name: "Small Meeting Room (Capacity:5)",
 cost: 1100,
 quantity: 0,
 },
 
 ],
 reducers: {
 
 incrementQuantity: (state, action) => {
 const { payload: index } = action;
 if (state[index]) {
 if (state[index].name === " Auditorium Hall (Capacity:200)" && state[index].quantity >= 3) {
 return; }
 state[index].quantity++;
 }
 },
 decrementQuantity: (state, action) => {
 const { payload: index } = action;
 if (state[index] && state[index].quantity > 0) {
 state[index].quantity--;
 }
 },
 },
});
export const { incrementQuantity, decrementQuantity } = venueSlice.actions;
export default venueSlice.reducer;
```

---

# 👤 Yazar(lar)

Richa Arora
Bethany Hudnutt

© IBM Corporation. Tüm hakları saklıdır.
