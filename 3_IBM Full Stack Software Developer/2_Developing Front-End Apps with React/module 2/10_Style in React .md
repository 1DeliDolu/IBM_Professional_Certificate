## 🎨 Style in React

Tahmini gereken süre: **3 dakika**

React’te stillendirme ( *styling* ) çeşitli yollarla yapılabilir; bunlara  *inline styles* ,  **CSS modules** , *styled components* ve daha fazlası dahildir. Her yaklaşımı kısaca inceleyelim.

---

## 🎯 Objective

Bu okumayı tamamladıktan sonra şunları yapabileceksiniz:

* React’teki çeşitli stilleri keşfetmek
* *Inline styles*

---

## 🧩 Inline styles

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

`<div>` öğesine, `style` attribute’ü kullanılarak doğrudan inline stiller uygulanmıştır.

Stiller, anahtarların CSS property adları, değerlerin ise karşılık gelen CSS property değerleri olduğu bir JavaScript nesnesi ( *object* ) olarak belirtilir.

Benzer şekilde, `<div>` içindeki `<p>` öğesine de `style` attribute’ü kullanılarak inline stiller uygulanmıştır.

Yukarıdaki bileşen; açık mavi arka plana, padding’e ve border-radius’a sahip bir `<div>` render eder. `<div>` içinde, beyaz metin rengi ve 18 piksel font boyutuna sahip bir `<p>` öğesi bulunur; tümü inline stiller kullanılarak stillendirilmiştir.

---

## 🧩 CSS modules

### `toggleMessage.module.css`

```css
.message {
  display: block;
  color: green;
  font-size: 18px;
  margin-top: 10px;
}
```

### `ToggleMessage.js`

```jsx
import React, { useState } from 'react';
import styles from './toggleMessage.module.css';
function ToggleMessage() {
  const [isVisible, setIsVisible] = useState(true);
  const toggleVisibility = () => {
    setIsVisible(!isVisible);
  };
  return (
    <div>
      <h2>Toggle Message</h2>
      <button onClick={toggleVisibility}>
        {isVisible ? 'Hide Message' : 'Show Message'}
      </button>
      <p className={isVisible ? styles.message : ''}>This is a hidden message.</p>
    </div>
  );
}
export default ToggleMessage;
```

`import styles from './toggleMessage.module.css';`: Bu ifade, CSS module `toggleMessage.module.css` dosyasını `styles` adlı bir nesne olarak içe aktarır. CSS’te bir module tipik olarak, uygulamanızdaki belirli bir bileşene veya modüle scope edilmiş bir dizi CSS kuralı içeren (genellikle `.module.css` uzantılı) bir dosyayı ifade eder. Bu CSS kuralları, bileşenler arasında istenmeyen stil çakışmalarını önlemek için yerel olarak scope edilir.

`const [isVisible, setIsVisible] = useState(true);`: Bu, `useState` hook’u kullanarak `isVisible` adlı bir state değişkenini başlatır. Mesaj paragrafının görünür olup olmamasını temsil eder ve varsayılan olarak `true` değerine sahiptir.

`const toggleVisibility = () => {...};`: Bu, butona tıklandığında `isVisible` state değişkenini güncelleyerek mesaj paragrafının görünürlüğünü değiştiren bir fonksiyondur.

`<p className={isVisible ? styles.message : ''}>This is a hidden message.</p>`: Bu paragraf öğesi mesajı görüntüler. `className` değeri `isVisible` değerine göre koşullu biçimde ayarlanır. `isVisible` **true** ise CSS module içindeki `message` sınıfını uygular; aksi halde boş string uygular ve ek stilleri etkili biçimde kaldırır.

---

## 🧰 Styled components

CSS, React bileşenlerinde JavaScript nesneleri kullanılarak da uygulanabilir; bu, sağlanan React bileşenindeki `messageStyle` nesnesine benzer.

Örneğin, aşağıdaki kodda `messageStyle` adlı bir nesne vardır. `{ color: 'green', fontSize: '18px' }` ifadesi, renk ve font boyutu için CSS property’lerini temsil eder. Ayrıca koşullu stilendirme de vardır. Örneğin, `{ display: isVisible ? 'block' : 'none' }` ifadesi, `isVisible` değerine bağlı olarak `display` property’sini dinamik biçimde ayarlar.

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
