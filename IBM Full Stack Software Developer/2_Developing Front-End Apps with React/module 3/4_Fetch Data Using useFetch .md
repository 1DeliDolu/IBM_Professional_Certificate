# 🧪 Lab: useFetch Kullanarak Veri Çekme

## ⏱️ Gerekli Tahmini Süre

40 dakika

---

## 📚 Ne Öğreneceksiniz?

Bu lab’de, React’te bir **custom hook** ( *useFetch* ) ve buna karşılık gelen bir component ( *FetchData* ) kullanarak veri çekmeyi öğreneceksiniz. Veri çekme mantığını yeniden kullanılabilir hook’lar içine kapsülleyerek kodun sürdürülebilirliğini artırabilirsiniz. State yönetimi ve asenkron operasyonları verimli şekilde yönetmek için React’in *useState* ve *useEffect* hook’larında ustalaşacaksınız. Ayrıca, JSX ile çekilen veriyi UI üzerinde dinamik olarak render etmeyi öğrenecek, böylece dinamik ve etkileşimli component’ler oluşturabileceksiniz.

---

## 🎯 Öğrenme Hedefleri

Bu lab’i tamamladıktan sonra şunları yapabileceksiniz:

* Bir React uygulaması içinde *fetch API method* kullanarak harici bir API’den veri çekmek
* Veri çekme mantığını kapsüllemek için bir **custom React hook** ( *useFetch* ) uygulamak
* API’den alınan veriyi UI üzerinde render etmek ve her bir öğe için  *name* ,  *importance* , *benefits* ve *best time to intake* gibi ilgili bilgileri göstermek

---

## ✅ Ön Koşullar

* HTML hakkında temel bilgi
* JavaScript hakkında orta seviye bilgi
* React hooks ve custom hook hakkında temel bilgi

---

## 🛠️ Ortamı Kurma

1. Lab’in üst menüsünden, ekran görüntüsünde 1 numarada gösterilen yerde sağ üstteki **Terminal** sekmesine tıklayın ve ardından 2 numarada gösterildiği gibi  **New Terminal** ’a tıklayın.
2. Bu React uygulaması için boiler template’i klonlamak üzere terminale aşağıdaki komutu yazın ve Enter’a basın. *custom_hook* uygulaması, **useFetch.jsx** ve **FetchData.jsx** adlı class component’leri ve **FetchData.css** adlı bir css dosyasını içerir.

```bash
git clone https://github.com/ibm-developer-skills-network/custom_hook.git
```

3. Bu işlem, proje klasörü altında **custom_hook** adlı bir klasör oluşturacaktır ve yapı, verilen ekran görüntüsündeki gibi olacaktır.
4. Terminalde **custom_hook** klasörüne girmek için komutu yazın. Terminalde **custom_hook** klasörüne gitmek için aşağıdaki komutu kullanın.

```bash
cd custom_hook
```

5. Klonladığınız kodun doğru çalıştığından emin olmak için aşağıdaki adımları izlemelisiniz:
   Terminalde aşağıdaki komutu yazın ve uygulamayı çalıştırmak için gerekli tüm paketleri yüklemek üzere Enter’a basın:

```bash
npm install
```

Ardından uygulamayı çalıştırmak için aşağıdaki komutu yürütün; bu işlem size **4173** port numarasını sağlayacaktır:

```bash
npm run preview
```

6. React uygulamanızı görüntülemek için sol paneldeki **Skills Network** ikonuna tıklayın (1 numaraya bakın). Bu işlem  **SKILLS NETWORK TOOLBOX** ’ı açacaktır. Ardından  **Launch Application** ’a tıklayın (2 numaraya bakın). **Application Port** alanına **4173** port numarasını girin (3 numaraya bakın) ve tıklayın.
7. Çıktı, verilen ekran görüntüsündeki gibi görünecektir.

---

## 🧩 Custom Hook Oluşturma

1. Sonraki adımda, klonladığınız **custom_hook** klasörünüzde, **src** dizini altındaki **Components** klasörü içinde yer alan **FetchData.jsx** component’ine giderek dosyayı açın.
2. FetchData.jsx component’inin temel yapısı, bir `<h1>` etiketiyle başlık ve **list_data_main** adlı class’a sahip bir `<ul>` etiketi içeren varsayılan bir function component olarak sağlanmıştır.

```jsx
import React from 'react'
const FetchData = () => {
 return (
 <>
 <ul className='list_data_main'>
 <h1 className='useFetch_heading'>Use Fetch Custom Hook</h1>
 </ul>
 </>
 )
}
export default FetchData
```

3. Şimdi **API Data Link** üzerinden API’den veri çekmeniz gerekiyor. Veriyi çekmek için iki yaklaşım vardır:
   * İlk olarak, veriyi çekmesi gereken her component içinde *fetch API method* kullanarak mantığı uygulamak. Diyelim ki harici kaynaktan veri yüklemeniz gereken 5 component var. Bu durumda her component için benzer veri çekme mantığını yazmanız gerekir.
   * İkinci olarak, yeniden kullanılabilir bir custom hook oluşturmak. Bu custom hook, veri çekme mantığını kapsüller ve birden fazla component’te, her seferinde tüm veri çekme kodunu yeniden yazmadan yeniden kullanılmasına olanak tanır.
4. Custom hook oluşturmak için **src** klasörü altındaki **Components** klasöründe bulunan **useFetch.jsx** component’ine gidin. Component içinde aşağıdaki gibi temel bir iskelet sağlanmıştır:

```js
const useFetch = (url) => {
}
```

```js
export default useFetch
```

Yukarıdaki örnekte, tek bir parametre alan ( **url** ) bir arrow function tanımlanmıştır. Bu metot **default** olarak export edilmiştir.

5. Temel iskelette, veriyi çekmek için bir şablon oluşturmak üzere *useEffect* hook’unu uygulamanız gerekir.
6. *useState* hook’unu kullanarak **data** adlı bir değişken ve fonksiyon olarak **setData** oluşturun. Bu kodu arrow function component’in içine ekleyin.

```js
const[data,setData]=useState();
```

7. *useState* hook’unun çalışmasını sağlamak için **useFetch.jsx** component’inin en üstüne aşağıdaki ifadeyi ekleyin.

```js
import { useState } from "react";
```

8. Şimdi arrow function içinde *useEffect* hook’unu uygulayın. Burada *fetch api method* kullanarak verilen herhangi bir url’den veri çekme mantığını oluşturacak ve veriyi bir array olarak döndüreceksiniz. Bu kodu, *useState* hook’u ile değişken tanımlamasından sonra ekleyin.

```js
 useEffect(()=>{
 fetch(url).then((res)=>res.json())
 .then((data)=>setData(data))
 },[])
return [data]
```

* *useEffect* : Functional component’lerde side effect gerçekleştirmek için kullanılan bir React Hook’udur. Genellikle veri çekme, event’lere abone olma veya render ile ilgili olmayan diğer side effect’ler için kullanılır.
* *fetch(url)* : Belirtilen  **url** ’e bir HTTP isteği başlatır.
* *.then((res) => res.json())* : Sunucudan gelen response’u JSON formatına dönüştürür.
* *.then((data) => setData(data))* : Alınan veriyi **data** state değişkenine atar.  *setData* , React function component’lerde state’i güncelleyen bir fonksiyondur.

9. *useEffect* hook’unun çalışmasını sağlamak için **useFetch.jsx** component’inin en üstüne aşağıdaki kodu ekleyin.

```js
import {useState, useEffect } from "react";
```

10. Tüm kod aşağıdaki yapıyla aynı olmalıdır:

```jsx
import React, { useEffect, useState } from 'react'
const useFetch = (url) => {
 const[data,setData]=useState();
 useEffect(()=>{
 fetch(url).then((res)=>res.json())
 .then((data)=>setData(data))
 },[])
 return [data]
}
export default useFetch
```

**url** değişkeni, belirli bir web sitesinin tam URL’ini belirtmek için *useFetch* arrow function’ına parametre olarak geçirilir; böylece herhangi bir component, veriyi kolayca çekebilir. Bu fonksiyon, custom hook’u kullanan component’lerin URL’i dinamik olarak sağlamasına olanak tanır; bu da redundant kod ihtiyacı olmadan çeşitli kaynaklardan sorunsuz veri çekmeyi mümkün kılar.

---

## 📥 Custom Hook Kullanarak Veri Çekme

1. Şimdi tekrar, klonladığınız **custom_hook** klasörünüzde, **src** dizini altındaki **Components** klasöründe bulunan **FetchData.jsx** dosyasına gidin.
2. **FetchData** arrow function’ı içinde, veriyi çekmek istediğiniz belirli URL’i geçirerek custom hook’u uygulayın. Ayrıca verinin **data** değişkenine alınıp alınmadığını kontrol etmek için **console.log** ekleyin. Aşağıdaki kodu, FetchData.jsx function component’inin **return** ifadesinden önce ekleyin.

```js
const [data]=useFetch('https://api.npoint.io/9045c260b1565daa9e15');
 console.log(data);
```

3. Bu component’in çalışması için  **useFetch** ’i import edin. Bunun için FetchData.jsx component’inin en üstüne aşağıdaki kodu ekleyin.

```js
import useFetch from './UseFetch';
```

4. Çıktıyı kontrol etmek için React uygulamasını yeniden çalıştırın. Tarayıcıda sağ tıklayın ve **inspect** seçin; ardından **Console** sekmesine tıklayın. Çıktı, verilen ekran görüntüsündeki gibi görünmelidir.

---

## 🖥️ Front End’de Veriyi Getirme

1. Veriyi almak için **data** array’i üzerinde iterasyon yapmanız gerekir. FetchData.jsx component’inde `<ul>` etiketi içinde `<h1>...</h1>` etiketinden sonra aşağıdaki gibi *map* array metodunu uygulamalısınız:

```jsx
{data && data.map((e)=>(
 <>
 </>
 ))}
```

2. Bunu uygulamak için `<ul>` etiketindeki fragment’ler (`<>...</>`) içinde **list_data** class adına sahip `<li>` etiketi oluşturun. Sonrasında, front end’de hangi veriyi göstermek istediğinizi belirlemek için console.log çıktısını inceleyin. Örneğin, verilen ekran görüntüsünde array’in ilk index nesnesini genişlettiğinizde erişilebilen 5 farklı bilgi türü olduğunu fark edeceksiniz.
3. Bu farklı türler, *map* metodunda parametre olarak geçtiğiniz **e** değişkeni kullanılarak veriyi çekebilir.

```jsx
<li key={index} className='list_data'>
 <h3>{e.name}</h3>
 <p><strong>Importance: </strong>{e.importance}</p>
 <p><strong>Benefits: </strong>{e.benefits}</p>
 <p><strong>Time to eat: </strong>{e.best_time_to_intake}</p>
 </li>
```

4. FetchData.jsx component’ine css dosyasını import ifadesiyle dahil edin. Aşağıdaki ifadeyi, diğer import ifadeleriyle birlikte function component’ten önce ekleyin.

```js
import './FetchData.css'
```

5. Tüm kod aşağıdaki gibi görünecektir:

```jsx
import React from 'react'
import useFetch from './UseFetch'
import './FetchData.css'
const FetchData = () => {
 const [data]=useFetch('https://api.npoint.io/9045c260b1565daa9e15');
 console.log(data);
 return (
 <>
 <h1 className='useFetch_heading'>Use Fetch Custom Hook</h1>
 <ul className='list_data_main'>
 {data && data.map((e,index)=>(
 <li key={index} className='list_data'>
 <h3>{e.name}</h3>
 <p><strong>Importance: </strong>{e.importance}</p>
 <p><strong>Benefits: </strong>{e.benefits}</p>
 <p><strong>Time to eat: </strong>{e.best_time_to_intake}</p>
 </li>
 ))}
 </ul>
 </>
 )
}
export default FetchData
```

**Not:** **e** parametresi, her iterasyonda array’in her index’inin değerini içerir.

---

## ✅ Çıktıyı Kontrol Etme

1. Terminalde React uygulamasının çalışmasını durdurmak için çıkmak üzere **ctrl+c** yapın.
2. Ardından terminale aşağıdaki komutu yazın ve Enter’a basın.

```bash
npm run preview
```

3. React uygulamanızı görmek için tarayıcınızda React uygulaması için zaten açık olan web sayfasını yenileyin. Eğer açık değilse sol paneldeki **Skills Network** ikonuna tıklayın. Bu işlem  **“SKILLS NETWORK TOOLBOX.”** ’ı açacaktır. Ardından **“Launch Application”** seçin. **“Application Port”** alanına **4173** port numarasını girin ve tıklayın.
4. Çıktı, verilen ekran görüntüsündeki gibi görüntülenecektir.

**Not:** En son değişiklikleri görmek için terminalde **npm run preview** komutunu tekrar çalıştırmanız gerekir.

5. **“FetchData.jsx”** için tam çözümü görmek için buraya tıklayın.

```jsx
import React from 'react'
import useFetch from './UseFetch'
import './FetchData.css'
 const FetchData = () => {
 const [data]=useFetch('https://api.npoint.io/9045c260b1565daa9e15');
 console.log(data);
 return (
 <>
 <h1 className='useFetch_heading'>Use Fetch Custom Hook</h1>
 <ul className='list_data_main'>
 {data && data.map((e,index)=>(
 <li key={index} className='list_data'>
 <h3>{e.name}</h3>
 <p><strong>Importance: </strong>{e.importance}</p>
 <p><strong>Benefits: </strong>{e.benefits}</p>
 <p><strong>Time to eat: </strong>{e.best_time_to_intake}</p>
 </li>
 ))}
 </ul>
 </>
 )
}
export default FetchData
```

6. **“useFetch.jsx”** için tam çözümü görmek için buraya tıklayın.

```js
import {useState, useEffect } from "react";
const useFetch = (url) => {
 const[data,setData]=useState();
 useEffect(()=>{
 fetch(url).then((res)=>res.json())
 .then((data)=>setData(data))
 },[])
return [data]
}
export default useFetch
```

7. Parent component **“App.jsx”** için tam çözümü görmek için buraya tıklayın.

```jsx
import React from 'react'
import FetchData from './Components/FetchData'
function App() {
 return (
 <>
 <FetchData/>
 </>
 )
}
export default App
```

---

## 🔁 Veri Çekmeye Alternatif Adımlar

**Not:** API’ye erişmekte zorluk yaşıyorsanız, aşağıda verilen veriyi kullanarak alternatif olarak bir JSON dosyası oluşturabilirsiniz. Lab’i API kullanarak zaten tamamladıysanız bu bölümü atlayıp **Practice Exercise** bölümüne geçebilirsiniz.

1. Tüm meyve verilerini saklamak için **Components** klasörü içinde **fruit.json** adlı bir dosya oluşturun.
   **“Fruit.json”** dosyanız için meyve verilerini almak üzere buraya tıklayın.

```json
[
 {
"name": "Banana",
"image": "https://blog-images-1.pharmeasy.in/blog/production/wp-content/uploads/2021/01/30152155/shutterstock_518328943-1.jpg",
"benefits": "Energy boost, aids digestion and etc",
"importance": "High in potassium and vitamins and fatty acids",
"best_time_to_intake": "Morning or as a snack"
 },
 {
"name": "Spinach",
"image": "https://media.post.rvohealth.io/wp-content/uploads/2019/05/spinach-732x549-thumbnail.jpg",
"benefits": "Strengthens bones, improves eyesight",
"importance": "Rich in iron and antioxidants",
"best_time_to_intake": "Lunch or dinner or breakfast"
 },
 {
"name": "Salmon",
"image": "https://www.onceuponachef.com/images/2018/02/pan-seared-salmon-.jpg",
"benefits": "Promotes heart health, supports brain function",
"importance": "High in omega-3 fatty acids",
"best_time_to_intake": "Lunch or dinner"
 },
 {
"name": "Avocado",
"image": "https://www.cookrepublic.com/wp-content/uploads/2023/08/green-avocado-salad-process11.jpg",
"benefits": "Aids weight management, supports heart health",
"importance": "Rich in healthy fats",
"best_time_to_intake": "Morning or as a snack"
 },
 {
"name": "Broccoli",
"image": "https://detoxinista.com/wp-content/uploads/2021/03/instant-pot-steamed-broccoli-1.jpg",
"benefits": "Helps prevent cancer, supports digestive health",
"importance": "High in fiber and antioxidants",
"best_time_to_intake": "Lunch or dinner"
 },
 {
"name": "Oats",
"image": "https://www.allrecipes.com/thmb/nvX2ZrnQHpfSCBBmc5PTCWBlHEI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/263512-ddmfs-in
"benefits": "Lowers cholesterol, regulates blood sugar",
"importance": "Rich in fiber and minerals",
"best_time_to_intake": "Breakfast"
 },
 {
"name": "Eggs",
"image": "https://www.allrecipes.com/thmb/0VXMwCY9RVNrNvWcF_9v0iZpNqA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/JF_241160_Cream
"benefits": "Builds muscles, improves brain health",
"importance": "High in protein and nutrients",
"best_time_to_intake": "Breakfast or lunch"
 },
 {
"name": "Yogurt",
"image": "https://www.luvele.com.au/cdn/shop/articles/probiotic_yogurt_02_1024x.png?v=1585795322",
"benefits": "Supports digestion, strengthens bones",
"importance": "Rich in probiotics and calcium",
"best_time_to_intake": "Snack or dessert"
 },
 {
"name": "Blueberries",
"image": "https://www.hkvitals.com/blog/wp-content/uploads/2023/09/900-9-1.jpg",
"benefits": "Boosts brain health, supports heart health",
"importance": "High in antioxidants and vitamins",
"best_time_to_intake": "Morning or as a snack"
 },
 {
"name": "Almonds",
"image": "https://saaragroups.com/wp-content/uploads/2021/04/almond.jpg",
"benefits": "Promotes heart health, aids weight management",
"importance": "Rich in healthy fats and antioxidants",
"best_time_to_intake": "Morning or as a snack"
 },
 {
"name": "Chicken Breast",
"image": "https://www.budgetbytes.com/wp-content/uploads/2024/01/Air-Fryer-Chicken-Breast-Plated.jpg",
"benefits": "Builds lean muscle, aids weight loss",
"importance": "High in protein",
"best_time_to_intake": "Lunch or dinner"
 },
 {
"name": "Sweet Potatoes",
"image": "https://www.eatingbirdfood.com/wp-content/uploads/2023/11/baked-sweet-potato-hero.jpg",
"benefits": "Regulates blood sugar, supports eye health",
"importance": "Rich in vitamins and fiber",
"best_time_to_intake": "Lunch or dinner"
 },
 {
"name": "Quinoa",
"image": "https://www.onceuponachef.com/images/2024/03/thai-quinoa-salad-1-760x933.jpg",
"benefits": "Boosts metabolism, supports heart health",
"importance": "High in protein and fiber",
"best_time_to_intake": "Lunch or dinner"
 },
 {
"name": "Kale",
"image": "https://joyfoodsunshine.com/wp-content/uploads/2021/05/kale-salad-recipe-3.jpg",
"benefits": "Strengthens bones, reduces inflammation",
"importance": "Rich in vitamins and antioxidants",
"best_time_to_intake": "Lunch or dinner"
 },
 {
"name": "Apples",
"image": "https://www.acouplecooks.com/wp-content/uploads/2022/11/Apple-Salad-010s.jpg",
"benefits": "Supports heart health, aids digestion",
"importance": "Rich in fiber and vitamins",
"best_time_to_intake": "Morning or as a snack"
 },
 {
"name": "Greek Yogurt",
"image": "https://spicecravings.com/wp-content/uploads/2023/09/Greek-Yogurt-Parfait-Featured.jpg",
"benefits": "Aids muscle recovery, supports digestion",
"importance": "Rich in protein and probiotics",
"best_time_to_intake": "Snack or dessert"
 },
 {
"name": "Carrots",
"image": "https://www.allrecipes.com/thmb/nH0ibTts6V4xHLjBPEtQt4Lbsuo=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/18256-Buttery-C
"benefits": "Promotes healthy eyesight, boosts immunity",
"importance": "High in beta-carotene and minerals",
"best_time_to_intake": "Morning or as a snack"
 },
 {
"name": "Brown Rice",
"image": "https://www.myweekendkitchen.in/?attachment_id=3777",
"benefits": "Supports digestive health, provides stable energy",
"importance": "Rich in fiber and minerals",
"best_time_to_intake": "Lunch or dinner"
 },
 {
"name": "Tuna",
"image": "https://www.bigbasket.com/media/uploads/p/l/40227733_1-fresho-yellofin-tuna-steaks.jpg",
"benefits": "Promotes heart health, aids muscle repair",
"importance": "High in protein and omega-3 fatty acids",
"best_time_to_intake": "Lunch or dinner"
 },
 {
"name": "Oranges",
"image": "https://www.mashed.com/img/gallery/believe-it-or-not-oranges-dont-actually-exist-naturally-in-nature/l-intro-1676042900.jpg",
"benefits": "Supports immune system, aids digestion",
"importance": "Rich in vitamin C and fiber",
"best_time_to_intake": "Morning or as a snack"
 }
]
```

2. Artık veriyi **fruit.json** dosyasından çekmeniz gerekiyor; bu nedenle **src/Components/FetchData.jsx** dosyasını güncelleyin.
   Parent component **“FetchData.jsx”** için tam çözümü görmek için buraya tıklayın.

```jsx
import React from 'react';
import fruitData from './Fruit.json'; // Import from same folder
import './FetchData.css';
const FetchData = () => {
 const data = fruitData;
 return (
<>
 <h1 className='useFetch_heading'>Use Fetch Custom Hook</h1>
 <ul className='list_data_main'>
 {data && data.map((e, index) => (
 <li key={index} className='list_data'>
 <h3>{e.name}</h3>
 <img src={e.image} alt={e.name} width="200" />
 <p><strong>Importance: </strong>{e.importance}</p>
 <p><strong>Benefits: </strong>{e.benefits}</p>
 <p><strong>Time to eat: </strong>{e.best_time_to_intake}</p>
 </li>
 ))}
 </ul>
</>
 );
};
export default FetchData;
```

3. Aşağıdaki kodla **src/Components/useFetch.jsx** dosyasını güncelleyerek *useFetch* hook’unu ekleyin:
   Parent component **“useFetch.jsx”** için tam çözümü görmek için buraya tıklayın.

```jsx
import React, { useEffect, useState } from 'react';
const useFetch = (url) => {
 const [data, setData] = useState(null);
 useEffect(() => {
 if (!url) return; // prevent fetch if url is empty or undefined
 fetch(url)
 .then((res) => res.json())
 .then((data) => setData(data))
 .catch((error) => {
 console.error('Fetch error:', error);
 setData(null);
 });
 }, [url]); // add url as dependency
 return [data];
};
export default useFetch;
```

4. Çıktıyı kontrol etmek ve hooks kullanarak meyve verisini çekmek için **npm run preview** komutunu çalıştırın.

---

## 🏋️ Practice Exercise

1. Bu practice exercise’ta, **useFetch.jsx** custom hook component’inin başka bir component’te API verisi çekmek için nasıl kullanılacağını göreceksiniz.
2. Yoga ile ilgili API’den veri çekmeniz gerekecek. API verisini görmek için bu bağlantıya tıklayın:  **Yoga-Benefits** .
3. Önce bir component oluşturun: **Components** klasörünü seçtikten sonra sağ tıklayın ve  **New File** ’a tıklayın. Component’e **FetchYogaData.jsx** adını verin.
4. FetchYogaData.jsx component’inde temel iskeleti oluşturun.
   **İpucu:** Function component yapısını kullanın
   Örnek çözüm için buraya tıklayın.

```jsx
 import React from 'react'
 const FetchYogaData = () => {
 return (
 <>
 </>
 )
 }
 export default FetchYogaData
```

5. Şimdi **useFetch.jsx** custom hook component’ini **FetchYogaData.jsx** içine import edin ve API linkini url olarak geçin.
   API URL: `https://api.npoint.io/4459a9a10e43812e1152`

```js
import UseFetch from './UseFetch';
```

**İpucu:** Mevcut component’te custom hook component’ini kullanmak için import statement kullanın ve url’i geçirmek için değişken tanımlayın.
Örnek çözüm için buraya tıklayın.

```js
 import UseFetch from './UseFetch';
 const [data]=useFetch('https://api.npoint.io/4459a9a10e43812e1152');
```

Import statement’ı component’in en üstüne ve **data** değişkenini function component’in return ifadesinden önce ekleyin.

6. Verinin tarayıcıdaki console sekmesine gelip gelmediğini kontrol etmek için **console.log** yazın.
   **İpucu:** Return ifadesinden önce `console.log(data)` yazın.
7. **FetchYogaData.jsx** component’ini **App.jsx** parent component’ine dahil edin ve terminalde uygulamayı yeniden çalıştırarak çıktıyı kontrol edin.
   **İpucu:** Import statement kullanın.
8. **list_data_main** className’ine sahip bir `<ul>` etiketi oluşturun. Bunun içinde, çekilen veriyi map ile dolaşarak her bir öğeyi `<li>` etiketleri içinde görüntüleyin. Aşağıdaki ekran görüntüsü örnek bir çıktıyı gösterir.

**“FetchYogaData.jsx”** için tam çözümü görmek için buraya tıklayın.

```jsx
import React from 'react';
import UseFetch from './UseFetch';
import './FetchData.css';
const FetchYogaData = () => {
 // Use the custom hook to fetch data from the Yoga API.
 const [data] = UseFetch('https://api.npoint.io/4459a9a10e43812e1152');
 console.log(data);
 return (
 <ul className="list_data_main">
 <h1 className="usefetch_heading">Yoga Benefits</h1>
 {data && data.map((e,index) => (
 <li className="list_data" key={index}>
 <h3>{e.name}</h3>
 <p><strong>Benefits: </strong>{e.benefits}</p>
 <p><strong>Duration: </strong>{e.time_duration}</p>
 </li>
 ))}
 </ul>
 );
};
export default FetchYogaData;
```

**“App.jsx”** için tam çözümü görmek için buraya tıklayın.

```jsx
import React from 'react'
import FetchData from './Components/FetchData';
import FetchYogaData from './Components/FetchYogaData'
function App() {
 return (
<>
{/* <FetchData/> */}
<FetchYogaData/>
</>
 )
}
export default App
```

---

## 🎉 Sonuç

Tebrikler! Veriyi kendi kişiselleştirilmiş custom hook’unuzu kullanarak çekmek için React uygulamanızı oluşturdunuz!

Bu lab’de, çekilen veriyi kullanıcı arayüzüne render etmekten sorumlu **FetchData** adlı bir React component’i oluşturdunuz. Bu component, bir URL ile belirtilen API endpoint’inden veri almak için **useFetch** custom hook’unu kullanır.

**useFetch** adlı custom React hook’u, belirtilen bir URL’den veri çekme mantığını kapsüller. Bu hook, veri çekme sürecini yönetmek için *useState* ve *useEffect* kullanır; böylece veri asenkron olarak alınır ve component’in state’inde saklanır.

Çekilen veri array’i üzerinde *map* metodunu uygulamayı ve JSX kullanarak her bir öğeyi UI’a render etmeyi öğrendiniz. Her bir veri öğesinin çeşitli niteliklerini (ör.  *name* ,  *importance* , *benefits* ve  *best time to intake* ) stillenmiş liste öğeleri içinde gösterir.

Veri çekme mantığını bir custom hook’a ( **useFetch** ) ayırarak modüler ve yeniden kullanılabilir bir yaklaşımı benimsediniz. Bu yaklaşım, uygulama genelindeki component’lerin, istenen URL’i *useFetch* hook’una argüman olarak vererek farklı API endpoint’lerinden kolayca veri çekebilmesini sağlar; böylece kod verimliliğini ve sürdürülebilirliğini artırır.

---

## ✍️ Yazar(lar)

Richa Arora

---

## ©️ Telif

© IBM Corporation. Tüm hakları saklıdır.
