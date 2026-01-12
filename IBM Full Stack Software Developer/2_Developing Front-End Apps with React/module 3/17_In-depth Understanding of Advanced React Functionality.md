## 🧾 Hızlı Başvuru: Gelişmiş React İşlevselliğini Derinlemesine Anlama

---

## 🪝 Hooks ve Form Yönetimi

### 🧩 *useState()*

**Açıklama**
*useState()* hook’u, React fonksiyon bileşeninin state’lerini yönetebilir; örneğin boolean, object, array, string gibi herhangi bir veri türünü tanımlayabilirsiniz.

**Kod örneği**

```javascript
import React, { useState, useEffect } from 'react';
function SideEffect() {
 const [empId, setEmpId] = useState(100);
 return (
 <div>
 <p>{empId}</p>
 </div>
 );
}
export default SideEffect;
```

---

### 🧩 *useEffect()*

**Açıklama**
 *useEffect* , fonksiyonel bileşenlerde side effect işlemlerini gerçekleştirmenizi sağlayan bir React hook’udur. Side effect, API’den veri çekmek gibi, ayrı ayrı bu işlemleri/fonksiyonellikleri çağırmadan sayfa yüklenir yüklenmez çalıştırmanız gereken herhangi bir işlemi ifade eder.

**Kod örneği**

```javascript
import React, { useState, useEffect } from 'react';
function SideEffect() {
 const [foods, setFoods] = useState([]);
 useEffect(() => {
 fetch('https://api.npoint.io/d542b9ad99f501ab3dbf')
 .then(response => response.json())
 .then(data => {
 console.log(data);
 setFoods(data);
 })
 .catch(error => console.error('Error fetching users:', error));
 },[]); // Empty dependency array means this effect runs only once when the component mounts
 return (
 <div>
 <h1>Food List</h1>
 <ul>
 {foods.map((food)=>{
 return (<>
 <li><h1>{food.name}</h1></li>
 <p>food.description</p>
 <p>food.price</p>
 <p>food.category</p>
 <p>food.ingredients</p>
 <img src={food.image_url} alt="" height='100px' width='100px' />
 </>
 )
 })}
 </ul>
 </div>
 );
}
export default SideEffect;
```

---

### 🧩 Custom Hook

**Açıklama**
Custom hook’ları başka herhangi bir bileşende kullanabilirsiniz. Bu kod parçasında *UseToggle* adlı bir fonksiyon bileşeni bulunur; bu bileşen bir custom hook olarak işlev görür. Ayrıca bu custom hook’u kullanacak olan *ToggleButton* adlı başka bir fonksiyon bileşeni de vardır.

**Kod örneği**

```javascript
//ToggleButton
import { useState } from 'react';
import UseToggle from './UseToggle';
function ToggleButton() {
 const [isToggled, toggle] = UseToggle(false);
 return (
 <div>
 <h1>Toggle Button</h1>
 <button onClick={toggle}>
 {isToggled ? 'ON' : 'OFF'}
 </button>
 </div>
 );
}
export default ToggleButton;
//UseToggle.jsx
import { useState } from "react";
function UseToggle(initialValue = false) {
 const [value, setValue] = useState(initialValue);
 const toggle = () => {
 setValue(!value);
 };
 return [value, toggle];
 }
 export default UseToggle
```

---

## 🌐 Fetch API Method

**Açıklama**
Fetch yöntemi, API kullanarak veri çekebilir.

**Kod örneği**

```javascript
const apiUrl = 'https://jsonplaceholder.typicode.com/posts';
fetch(apiUrl)
 .then(response => response.json())
 .then(data => {
 console.log(data);
 })
 .catch(error => {
 console.error('There was a problem with the fetch operation:', error);
 });
```

---

## 🔌 Axios API Method

**Açıklama**
Axios yöntemi, API kullanarak veri çekebilir.

**Kod örneği**

```javascript
import axios from 'axios';
const apiUrl = 'https://jsonplaceholder.typicode.com/posts';
axios.get(apiUrl)
 .then(response => {
 console.log(response.data);
 })
 .catch(error => {
 console.error('There was a problem with the fetch operation:', error);
 });
```

---

## ✍️ *onChange*

**Açıklama**
*onChange* event attribute’ü, HTML ve React’te genellikle bir input alanının (ör. bir metin girişi) değerinin ne zaman değiştiğini takip etmek için kullanılır. *onChange* olayı, bir kullanıcı input alanına bir şey yazdığında gerçekleşir. Bu attribute, değişiklikleri kaydetmenizi ve yönetmenizi sağlar.

**Kod örneği**

```javascript
import React, { useState } from 'react';
function FormData() {
 const [empName, setEmpName] = useState('');
 const handleChange = event => {
 setEmpName(event.target.value);
 };
 const handleSubmit = event => {
 event.preventDefault();
 console.log('Form submitted:', empName);
 };
 return (
 <div>
 <h2>My Form</h2>
 <form onSubmit={handleSubmit}>
 <label>
 Input:
 <input type="text" value={empName} onChange={handleChange} />
 </label>
 <button type="submit">Submit</button>
 </form>
 </div>
 );
}
export default FormData;
```

---

## 🧰 Redux Toolkit

**Açıklama**
Redux toolkit, *npm* kullanılarak kurulabilir.

**CLI komutu**

```bash
npm install @reduxjs/toolkit.
```
