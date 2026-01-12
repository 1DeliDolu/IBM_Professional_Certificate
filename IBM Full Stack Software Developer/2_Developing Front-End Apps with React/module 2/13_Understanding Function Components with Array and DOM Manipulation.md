# 🧾 Hile Sayfası: Dizi ve DOM Manipülasyonu ile Function Components’i Anlama

---

## 🧩 Function Component (function anahtar sözcüğü ile)

**Açıklama**
Function component, bileşenin adıyla birlikte `function` anahtar sözcüğü ile başlar ve `return` içinde HTML etiketlerini içerir. Ayrıca bileşen adını varsayılan olarak dışa aktarır.

**Kod Örneği**

```jsx
import React from 'react'
function Extra() {
 return (
 <>
 <p>This is paragraph</p>
 </>
 )
}
export default Extra
```

---

## 🏹 Function Component (arrow function ile)

**Açıklama**
Function component, bileşenin adıyla birlikte değişken türü ile başlar ve `return` içinde HTML etiketlerini içerir. Ayrıca bileşen adını varsayılan olarak dışa aktarır.

**Kod Örneği**

```jsx
import React from 'react'
const Extra = () => {
 return (
 <div>Extra</div>
 )
}
export default Extra
```

---

## 🧷 Function Component’te Props

**Açıklama**
Props, parent component’ten child component’e, child component ile birlikte attribute olarak gönderilebilir.

**Kod Örneği**

```jsx
import React from 'react'
import ChildComponent from './ChildComponent'
function ParentComponent () {
 let title='Project Manager';
 return (
 <>
 <ChildComponent title={title}/>
 </>
 )
}
export default ParentComponent
```

---

## 🔎 Child Function Component İçinde Props’a Erişim

**Açıklama**
Props, child function component içinde `props.variable_name` kullanılarak kolayca erişilebilir.

**Kod Örneği**

```jsx
import React from 'react'
const ChildComponent = (props) => {
 return (
 <>
 <p>The title is {props.title}</p>
 </>
 )
}
export default ChildComponent
```

---

## 🖱️ Class Component’te Event Handling

**Açıklama**
Click event gibi event’ler, function component’in `return` kısmından önce tanımlanan fonksiyon çağrılarak gerçekleştirilebilir.

**Kod Örneği**

```jsx
import React from 'react'
const Extra = (props) => {
 function show(){
 console.log('Show function');
 }
 return (
 <>
 <p>The title is {props.title}</p>
 <button onClick={()=>show()}>Click Here</button>
 </>
 )
}
export default Extra
```

---

## 🧠 Function Component’te State Management

**Açıklama**
State management, `useState()` hook’u ile kolayca yapılabilir.

**Kod Örneği**

```jsx
import React, { useState } from 'react'
const StateManagement = () => {
 const[name,setName]=useState('John');
 return (
 <>
 <h1>State Management using useState</h1>
 <p>The name is {name}</p>
 </>
 )
}
export default StateManagement
```

---

## 🧺 Array Declaration

**Açıklama**
Array, köşeli parantez içinde tanımlanabilir.

**Kod Örneği**

```jsx
const names = ['Alice', 'Bob', 'Charlie'];
```

---

## 🧺 Stateful Array

**Açıklama**
Array, `useState` kullanılarak tanımlanabilir.

**Kod Örneği**

```jsx
const [todos, setTodos] = useState(['Learn React', 'Build Project']);
```

---

## 🏗️ Dinamik Olarak Oluşturulan Arrays

**Açıklama**
Arrays, uygulama mantığına veya alınan verilere göre dinamik olarak oluşturulabilir.

**Kod Örneği**

```jsx
const numbers = [];
for (let i = 0; i < 10; i++) {
 numbers.push(i);
}
```

---

## 🗺️ Array `map()` Metodu

**Açıklama**
`map()` metodu, bir array’in her bir elemanı üzerinde dolaşmak ve React elementlerinden oluşan yeni bir array döndürmek için yaygın olarak kullanılır.

**Kod Örneği**

```jsx
const items = ['Apple', 'Banana', 'Orange'];
const itemList = items.map((item, index) => <li key={index}>{item}</li>);
return <ul>{itemList}</ul>;
```

---

## 🔁 `for...of` Döngüsü

**Açıklama**
`for...of` döngüsünü, bir array’in elemanları üzerinde dolaşmak için kullanabilirsiniz:

**Kod Örneği**

```jsx
const items = ['Apple', 'Banana', 'Orange'];
for (const item of items) {
 console.log(item);
}
```

---

## 🧾 Öğelerin Listesini Render Etme

**Açıklama**
Bir array üzerinde `map` kullanarak dolaşıp her öğe için bir JSX elementi döndürerek bir öğe listesi render edebilirsiniz.

**Kod Örneği**

```jsx
import React from 'react';
function ArrayComponent() {
 const items = ['Autumn', 'Spring', 'Summer','Winter'];
 return (
 <div>
 <h1> Seasons Names</h1>
 <ul>
 {items.map((item, index) => (
 <li key={index}>{item}</li>
 ))}
 </ul>
 </div>
 );
}
export default ArrayComponent;
```

---

## ➕➖ Array İçinde Öğeleri Ekleme ve Çıkarma

**Açıklama**
State ve React’in `setState` metodu kullanılarak bir array’e öğe ekleyebilir veya bir array’den öğe çıkarabilirsiniz.

**Kod Örneği**

```jsx
import React, { useState } from 'react';
function MyComponent() {
 const [items, setItems] = useState([‘Autumn’, ‘Spring’, ‘Winter’,’Summer’]);
 const [inputValue, setInputValue] = useState('');
 const addItem = () => {
 setItems([...items, inputValue]);
 setInputValue('');
 };
 const removeItem = (index) => {
 const newItems = [...items];
 newItems.splice(index, 1);
 setItems(newItems);
 };
 return (
 <div>
 <h1>Fruits</h1>
 <ul>
 {items.map((item, index) => (
 <li key={index}>
 {item}
 <button onClick={() => removeItem(index)}>Remove</button>
 </li>
 ))}
 </ul>
 <input
 type="text"
 value={inputValue}
 onChange={(e) => setInputValue(e.target.value)}
 />
 <button onClick={addItem}>Add</button>
 </div>
 );
}
```

---

## 🔀 Ternary Operator ile Koşullu Render

**Açıklama**
Bir array’in içeriğine bağlı olarak bileşenleri koşullu şekilde render edebilirsiniz.

**Kod Örneği**

```jsx
import React, { useState } from 'react';
function ArrayComponent() {
 const [items, setItems] = useState(['React JS','Vue JS','Angular JS','Vanilla JS']);
 return (
 <div>
 <h1>Front End Languages</h1>
 {items.length > 0 ? (
 <ul>
 {items.map((item, index) => (
 <li key={index}>{item}</li>
 ))}
 </ul>
 ) : (
 <p>No Front End language is available</p>
 )}
 </div>
 );
}
export default ArrayComponent;
```

---

## 🎨 React’te Inline Style

**Açıklama**
Inline style, double curly braces içinde bir attribute olarak etiketin içinde uygulanabilir.

**Kod Örneği**

```jsx
import React from 'react';
function MyComponent() {
 return (
 <div style={{ backgroundColor: 'lightblue', padding: '20px', borderRadius: '5px' }}>
 <p style={{ color: 'white', fontSize: '18px' }}>This is a paragraph with inline styles.</p>
 </div>
 );
}
export default MyComponent;
```

---

## 🧩 Object Kullanarak Style

**Açıklama**
Style, inline style gibi bir object olarak uygulanabilir.

**Kod Örneği**

```jsx
import React, { useState } from 'react';
function ToggleMessage() {
 const [isVisible, setIsVisible] = useState(true);
 const toggleVisibility = () => {
 setIsVisible(!isVisible);
 };
 const messageStyle = {
 display: isVisible ? 'block' : 'none',
 color: 'green',
 fontSize: '18px',
 marginTop: '10px'
 };
 return (
 <div>
 <h2>Toggle Message</h2>
 <button onClick={toggleVisibility}>
 {isVisible ? 'Hide Message' : 'Show Message'}
 </button>
 <p style={messageStyle}>This is a hidden message.</p>
 </div>
 );
}
```
