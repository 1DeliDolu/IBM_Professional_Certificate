## ✅ Lab: Todo List Application

### 📚 What you will learn

Bu lab’de, React functional component’leri ve **useState** hook’unu kullanarak basit bir yapılacaklar listesi ( *to-do list* ) uygulaması oluşturmayı öğreneceksiniz. **useState** hook’u ile state yönetimini nasıl yapacağınızı öğreneceksiniz. Lab; React state’lerini yönetmenin temellerini, kullanıcı girdisi almayı ve dinamik öğe listelerini göstermeyi içerir.

---

## 🎯 Learning objectives

Bu lab’i tamamladıktan sonra şunları yapabileceksiniz:

* React kullanarak basit bir Todo List uygulaması oluşturmak ve görevleri organize etmek için başlıklar ( *headings* ) ve ilişkili listeler eklemek.
* Todo öğelerini yönetmek ve belirli başlıkları ve listeleri silmek; temel CRUD ( **Create, Read, Update, Delete** ) işlevselliği sağlamak.
* Todo List’in state’ini (başlıkların listesi ve ilişkili listeler dahil) yönetmek için React’in **useState** hook’unu kullanmak.
* Değerleri dinamik olarak render etmek için React’in **useState** hook’unu kullanmak.

---

## ✅ Prerequisites

* HTML hakkında temel bilgi
* JavaScript hakkında orta düzey bilgi
* React functional component ve **useState** hook ile state management hakkında temel bilgi

---

## 🛠️ Setting up the environment

Lab’in üst menüsünden, verilen ekran görüntüsünde **1** numara ile gösterilen pencerenin sağ üstündeki **Terminal** sekmesine tıklayın ve ardından **2** numara ile gösterildiği gibi **New Terminal** seçeneğine tıklayın.

*SN screenshot*

React uygulaması için boiler template’i klonlamak üzere terminale aşağıdaki komutu yazın ve  **Enter** ’a basın:

```bash
git clone https://github.com/ibm-developer-skills-network/todo_list.git
```

Yukarıdaki komut, **Project** klasörü altında **todo_list** adlı bir klasör oluşturacaktır. Yapıyı ekran görüntüsünde görebilirsiniz.

Sonra, terminalde verilen komutu kullanarak klasörün içine girerek React uygulamasını çalıştırmanız gerekir. Bu işlem terminal yolunuzu ( *path* ) `todo_list` klasörü içinde uygulamayı çalıştıracak şekilde ayarlar.

```bash
cd todo_list
```

Klonladığınız kodun doğru çalıştığından emin olmak için şu adımları gerçekleştirmelisiniz:

Terminalde aşağıdaki komutu yazın ve  **Enter** ’a basın. Bu komut, uygulamayı çalıştırmak için gerekli tüm paketleri yükler:

```bash
npm install
```

Ardından uygulamayı çalıştırmak için aşağıdaki komutu yürütün; bu işlem size **4173** port numarasını sağlayacaktır:

```bash
npm run preview
```

React uygulamanızı görüntülemek için soldaki **Skills Network** ikonuna tıklayın ( **1** numaraya bakın ). Bu işlem  **SKILLS NETWORK TOOLBOX** ’ı açacaktır. Sonra  **Launch Application** ’ı seçin ( **2** numaraya bakın ). **Application Port** alanına **4173** port numarasını girin ( **3** numaraya bakın ) ve sağa doğru çıkan ok ikonuna tıklayın.

**Launch Your Application**

Çıktı, verilen ekran görüntüsünde gösterildiği gibi görüntülenecektir.

---

## 🧩 Setting the initial state

Sonraki adımda, klonladığınız `todo_list` klasörünüzde, `src` dizini içindeki **Components** klasöründe bulunan **TodoList.jsx** dosyasına gidin.

Bu bileşenin temel yapısı ekran görüntüsünde gösterildiği gibi olacaktır.

Yukarıdaki kod, bir React uygulamasında todo list bileşeninin temel yapısını temsil eder. `My Todo List` başlığını ve bir todo heading girmek için input alanı ile **Add Heading** etiketli bir buton içeren bir input container’ı barındıran bir todo list container’ı (`<div className="todo-container">`) içerir.

Todo öğelerini görüntülemek için tasarlanmış bir ana bölüm (`<div className="todo_main">`) vardır. Kullanıcı girdisini ele alma, todo öğelerini yönetme ve bunları dinamik olarak render etme işlevselliğini uygulamanız gerekir; bu, React state ve event handling kullanılarak implement edilir.

Aşağıdaki üç state’i initialize etmeniz gerekir:

* **todos** : Todo öğelerinden oluşan bir diziyi temsil etmek için. Başlangıç değeri boş dizi `[]` olmalıdır; bu, başlangıçta hiç todo öğesi olmadığını gösterir.
* **headingInput** : Kullanıcının todo öğesi için yeni bir heading eklemek amacıyla input alanına girdiği değeri temsil etmek için. Başlangıç değeri boş string `''` olmalıdır.
* **listInputs** : `listInputs`’u boş bir object `{}` olarak initialize edin. Bu state, her todo öğesi için input alanlarının değerini ayrı ayrı tutacaktır.

```jsx
const [todos, setTodos] = useState([]);
const [headingInput, setHeadingInput] = useState('');
const [listInputs, setListInputs] = useState({});
```

> Not: Yukarıdaki kodu bileşenin `return` kısmından önce ekleyin.

---

## ➕ Implement Add Heading Functionality

### Add Heading Functionality for Todo List

Öncelikle, benzer todo görevleri için **Grocery Items** gibi belirli bir heading ekleyeceksiniz. Bu heading altında,  **milk** , **butter** ve **bread** gibi todo list öğeleri yer alacaktır.

Bunun için `heading-input` class name’ine sahip bir input etiketi zaten sağlanmıştır. Bu input kutusundan heading’i almak için **Add Heading** butonuna tıklanınca tetiklenecek `handleAddTodo` adlı bir fonksiyon oluşturmanız gerekir.

`headingInput` boş mu kontrol edin. Boş değilse, `headingInput`’tan heading alan ve `lists` için boş bir dizi içeren yeni bir todo nesnesi oluşturun.

Sonra bu todo nesnesini todo dizisine ekleyin ve `headingInput`’u boş string yaparak temizleyin.

```jsx
const handleAddTodo = () => {
  if (headingInput.trim() !== '') {
    setTodos([...todos, { heading: headingInput, lists: [] }]);
    setHeadingInput('');
  }
};
```

Yukarıdaki kodda:

* `const handleAddTodo = () => { ... }`: `handleAddTodo` adlı bir constant tanımlar ve ona bir arrow function atar.
* `if (headingInput.trim() !== '') { ... }`: `headingInput` değişkeninin başındaki ve sonundaki whitespace karakterlerini kırptıktan ( *trim* ) sonra boş olup olmadığını kontrol eder. Bu koşul, kullanıcı bir içerik girmişse devam edilmesini sağlar.
* `setTodos([...todos, { heading: headingInput, lists: [] }]);`: Koşul sağlanırsa, mevcut `todos` dizisini spread syntax ile yeni bir diziye yayar (`...todos`) ve sonuna `heading` değeri `headingInput` olan, `lists` değeri ise boş dizi olan yeni bir nesne ekler.
* `setHeadingInput('');`: Yeni bir todo eklendikten sonra `headingInput` state’ini temizler, böylece kullanıcı yeni bir heading girebilir.

> Not: Yukarıdaki kodu üç state’i initialize ettikten sonra ekleyin.

### JSX içinde input ve button güncellemesi

“Add Todo” işlevini implement etmek için, heading ekleme input’u ve butonunun bulunduğu `input-container` sınıf adına sahip `div` içinde değişiklik yapılmalıdır.

`div` içindeki input field ve button elementleri, buton tıklamasıyla yeni todo öğesi ekleme işlevini içerecek şekilde güncellenmelidir.

```jsx
<div className="input-container">
  {/* Input field to enter a new heading */}
  <input
    type="text"
    className="heading-input" // CSS class for styling
    placeholder="Enter heading" // Text shown when input is empty
    value={headingInput}
    onChange={(e) => { setHeadingInput(e.target.value); }} // Add onChange event handler to update headingInput state
  />
  {/* Button to add the entered heading to the todo list */}
  <button className="add-list-button" onClick={handleAddTodo}>Add Heading</button>
</div>
```

Input elementinde:

* `value` attribute’ü `{headingInput}` olarak ayarlanır; bu, input’un değerini `headingInput` state değişkenine bağlar.
* `onChange`: Input değerinin değiştiği zaman tetiklenen bir React event handler’dır.
* `(e) => { ... }`: JavaScript’te fonksiyon tanımlamanın kısa yoludur ve event’i (`e`) parametre olarak alır.
* `setHeadingInput(e.target.value)`: `headingInput` state’ini input alanına girilen güncel değerle günceller.

Button elementinde:

* `onClick` event handler eklenir ve butona tıklandığında `handleAddTodo` fonksiyonunu tetikler. Bu fonksiyon, girilen heading altında yeni bir todo öğesi ekler.

---

## 🧾 Display Todo Heading

Her todo öğesinin heading’ini görüntülemek için `todos` dizisi üzerinde iterate etmeniz ve JSX içinde heading’i render etmeniz gerekir.

`todo-card` class name’ine sahip `div` içinde her todo öğesi render edilirken heading’i gösterecek şekilde JSX’i güncellemelisiniz.

Bu kodu, `todo_main` class name’ine sahip `div` içinde kullanmanız gerekir.

```jsx
{todos.map((todo, index) => ( // Iterate over each todo item in the todos array
  <div key={index} className="todo-card">
    <div className="heading_todo">
      {/* Display the heading text of the current todo item */}
      <h3>{todo.heading}</h3> {/* Display the heading here */}
      {/* Button to delete the current heading by passing its index */}
      <button className="delete-button-heading" onClick={() => handleDeleteTodo(index)}>Delete Heading </button>
    </div>
  </div>
))}
```

Bu kodda:

* `todos.map((todo, index) => ...)`: `todos` dizisi içindeki her todo öğesi üzerinde dolaşır. `map()` fonksiyonu dizideki her todo öğesi için belirtilen fonksiyonu çalıştırır.
* `<div key={index} className="todo-card"> ... </div>`: Her todo öğesi için `todo-card` sınıfına sahip bir `div` render edilir. `key` attribute’ü `index` olarak ayarlanır ve her öğenin listede benzersiz şekilde tanımlanmasına yardımcı olur.
* `<h3>{todo.heading}</h3>`: Todo heading’i `h3` içinde gösterilir; metin todo nesnesinin `heading` alanından alınır.
* `<button ... onClick={() => handleDeleteTodo(index)}>`: Her todo öğesinin yanında “Delete Heading” butonu vardır. Tıklandığında ilgili `index` parametresi ile `handleDeleteTodo` çalışır ve doğru todo öğesini siler.

Şimdi **TodoList.jsx** bileşenini kaydedin ve uygulamayı yeniden çalıştırarak kodun çalışmasını kontrol edin. Uygulamanız zaten açıksa yalnızca sayfayı yenileyin.

Şimdi input kutusuna **Grocery Item** gibi bir heading girin ve **Add Heading** butonuna tıklayın. Verilen ekran görüntüsüne benzer bir çıktı göreceksiniz.

---

## ➕ Implement Add List Functionality

Bu görevde artık belirli heading’ler altında todo list öğeleri ekleyeceksiniz. Bunu yapmak için verilen adımları izleyin.

### Add Form in JSX

Liste eklemek ve listeyi göstermek için, kullanıcının list adını gireceği bir input kutusu ve listeyi eklemek için bir buton eklemeniz gerekir.

Liste, yalnızca ekleme bölümü dahil edildikten sonra görüntülenmelidir. Bu nedenle bir input kutusu ve bir buton eklemeniz gerekir.

Aşağıdaki kodu, `heading_todo` class name’ine sahip `div`’den sonra, `todo-card` class name’ine sahip `div`’in child’ı olarak ekleyin; böylece yalnızca heading eklendikten sonra görünecektir.

```jsx
<div className='add_list'>
  {/* Input field for adding a new item under a specific heading */}
  <input
    type="text"
    className="list-input"
    placeholder="Add List"
    value={listInputs[index] || ''} // Use the value from listInputs array based on the current heading index
    onChange={(e) => handleListInputChange(index, e.target.value)}
  />
  {/* Button to add the list item to the corresponding heading */}
  <button className="add-list-button" onClick={() => handleAddList(index)}>Add List</button>
</div>
```

Yukarıdaki JSX code snippet şunları temsil eder:

Belirli bir todo öğesi içinde yeni bir list öğesi eklemek için bir form elementini temsil eder. Yeni list öğesinin metnini girmek için bir `<input>` ve değeri `listInputs` state’i ile bağlıdır.

Input elementinin `onChange` event handler’ı vardır. Input değeri değiştiğinde event yakalanır ve `handleListInputChange` fonksiyonu, güncel index ve `e.target.value` ile gelen yeni değer ile çağrılır. Bu, `listInputs` state object’ini güncelleyerek her todo öğesinin list input’unun ayrı ayrı takip edilmesini sağlar.

Ek olarak “Add List” butonu vardır ve tıklandığında `handleAddList` fonksiyonunu güncel index parametresiyle çağırarak ilgili todo heading altına list öğesini ekler.

---

## 🧠 handleAddList() Function To Add Todo Items

Heading içine list ekleme işlevini implement etmek için şu adımları uygulamalısınız:

* `handleAddList` adlı bir fonksiyon oluşturun ve todo item’ın index’ini parametre olarak alın.
* `listInputs[index]` değerinin trim sonrası boş olmadığını kontrol edin. Boş değilse, `todos` dizisinin bir kopyasını oluşturun.
* Yeni list öğesini `newTodos[index].lists` dizisine ekleyin.
* Güncellenmiş `todos` dizisini state’e atayın ve `listInputs[index]` değerini boş string yaparak temizleyin.

```jsx
// Function to handle adding a new list item to a specific todo heading
const handleAddList = (index) => {
    // Check if the input for the given index is not empty or just whitespace
    if (listInputs[index] && listInputs[index].trim() !== '') {
        const newTodos = [...todos]; // Create a copy of the current todos array
        newTodos[index].lists.push(listInputs[index]); // Add the new list item to the corresponding heading's list
        setTodos(newTodos); // Update the todos state with the new list item
        setListInputs({ ...listInputs, [index]: '' }); // Clear the input field for that index
    }
};
// Function to update list input value for a specific heading index
const handleListInputChange = (index, value) => {
    setListInputs({ ...listInputs, [index]: value }); // Update the listInputs state for the corresponding index
};
```

---

## 📋 Display Todo List in JSX

Listeyi görüntülemek için `todo.lists` üzerinde `<ul>` içinde iterate edin ve kullanıcı girdisini `<li>` içinde gösterin.

```jsx
<ul>
  {/* Iterate over each list item inside the current todo */}
  {todo.lists.map((list, listIndex) => (
    <li key={listIndex} className='todo_inside_list'>
      {/* Display the text content of the list item */}
      <p>{list}</p>
    </li>
  ))}
</ul>
```

Bu JSX code snippet, bir todo öğesi içindeki öğe listesini render eder. `map` fonksiyonunu kullanarak `todo` nesnesinin `lists` dizisi üzerinde dolaşır.

`lists` dizisindeki her öğe için, doğru render ve performans optimizasyonu için `key` attribute’ü `listIndex` olan bir `<li>` üretir.

Her `<li>` içinde, list öğesi içeriği bir `<p>` içinde gösterilir.

> Not: Yukarıdaki kodu `add_list` class name’ine sahip `<div>`’den önce ekleyin.

Uygulamayı yeniden çalıştırarak çıktıyı kontrol edin. İlk başta verilen ekran görüntüsüne göre bir çıktı göreceksiniz.

Sonra grocery list öğelerinizi sırayla yazıp **Add List** butonuna tıklayın. Ardından öğeleriniz aşağıdaki gibi görüntülenecektir.

---

## 🗑️ Delete Heading With Todo List

Heading bölümü silindiğinde, tüm todo list de silinmelidir. Örneğin kullanıcı **Grocery List** heading’ini girmiş ve altındaki tüm öğeleri eklemişse, kullanıcı tüm listeyi arayüzden silebilmelidir.

Listeyi silmek için `handleDeleteTodo` adlı bir fonksiyon oluşturun ve elemanı silmek için mantığı uygulayın.

```jsx
const handleDeleteTodo = (index) => {
  // Create a shallow copy of the current todos array
  const newTodos = [...todos];
  // Remove the todo at the specified index
  newTodos.splice(index, 1);
  // Update the state with the new array (without the deleted todo)
  setTodos(newTodos);
};
```

`handleDeleteTodo` fonksiyonu, `todos` dizisindeki belirli bir index’teki todo öğesini kaldırmak için tasarlanmıştır:

* `const handleDeleteTodo = (index) => { ... }`: Silinecek todo öğesinin index’ini alan bir arrow function ile `handleDeleteTodo` constant’ını tanımlar.
* `const newTodos = [...todos];`: `todos` dizisinin shallow copy’sini alır; bu adım state’i doğrudan mutate etmemek için kritiktir.
* `newTodos.splice(index, 1);`: `splice` metodu ile belirtilen index’ten itibaren 1 eleman silinir.
* `setTodos(newTodos);`: `useState` tarafından sağlanan `setTodos` ile state güncellenir; UI öğesi kaldırılır ve bileşen yeniden render edilir.

> Not: Yukarıdaki kodu bileşenin `return` kısmından önce ekleyin.

Şimdi `delete-button-heading` class name’ine sahip butonda `onClick` event’ini eklemeniz gerekir.

```jsx
<button className="delete-button-heading" onClick={handleDeleteTodo}>Delete Heading</button>
```

---

## 🧩 TodoList.jsx Solution Code

```jsx
import React, { useState } from 'react';
import './TodoList.css';

const TodoList = () => {
    // State to store all todo sections (each with a heading and associated lists)
    const [todos, setTodos] = useState([]);
    // State to manage the current heading input
    const [headingInput, setHeadingInput] = useState('');
    // State to manage each input field for the nested list items by heading index
    const [listInputs, setListInputs] = useState({});
    // Function to add a new todo heading (if input is not empty)
    const handleAddTodo = () => {
        if (headingInput.trim() !== '') {
            // Append new todo with empty list array
            setTodos([...todos, { heading: headingInput, lists: [] }]);
            setHeadingInput(''); // Clear the input field
        }
    };
    // Function to delete a todo section based on index
    const handleDeleteTodo = (index) => {
        const newTodos = [...todos];       // Create a copy of current todos
        newTodos.splice(index, 1);         // Remove the selected heading
        setTodos(newTodos);                // Update state with modified list
    };
    // Function to add a new list item under a specific heading
    const handleAddList = (index) => {
        if (listInputs[index] && listInputs[index].trim() !== '') {
            const newTodos = [...todos];                        // Copy current todos
            newTodos[index].lists.push(listInputs[index]);      // Add list to the right section
            setTodos(newTodos);                                 // Update state
            setListInputs({ ...listInputs, [index]: '' });      // Clear list input for that section
        }
    };
    // Function to handle change in list input field for a specific section
    const handleListInputChange = (index, value) => {
        setListInputs({ ...listInputs, [index]: value }); // Track input for each heading index
    };
    return (
        <>
            {/* Input section to add a new heading */}
            <div className="todo-container">
                <h1 className="title">My Todo List</h1>
                <div className="input-container">
                    <input
                        type="text"
                        className="heading-input"
                        placeholder="Enter heading"
                        value={headingInput}
                        onChange={(e) => setHeadingInput(e.target.value)} // Update heading input value
                    />
                    <button className="add-list-button" onClick={handleAddTodo}>
                        Add Heading
                    </button>
                </div>
            </div>
            {/* Main section displaying all todos */}
            <div className="todo_main">
                {todos.map((todo, index) => (
                    <div key={index} className="todo-card">
                        <div className="heading_todo">
                            <h3>{todo.heading}</h3> {/* Display heading */}
                            <button
                                className="delete-button-heading"
                                onClick={() => handleDeleteTodo(index)}
                            >
                                Delete Heading
                            </button>
                        </div>
                        {/* Render all list items under this heading */}
                        <ul>
                            {todo.lists.map((list, listIndex) => (
                                <li key={listIndex} className='todo_inside_list'>
                                    <p>{list}</p> {/* Display individual list item */}
                                </li>
                            ))}
                        </ul>
                        {/* Input section to add list item under this heading */}
                        <div className='add_list'>
                            <input
                                type="text"
                                className="list-input"
                                placeholder="Add List"
                                value={listInputs[index] || ''} // Maintain controlled input
                                onChange={(e) => handleListInputChange(index, e.target.value)} // Update list input value
                            />
                            <button
                                className="add-list-button"
                                onClick={() => handleAddList(index)}
                            >
                                Add List
                            </button>
                        </div>
                    </div>
                ))}
            </div>
        </>
    );
};

export default TodoList;
```

---

## 🔍 Check the output

Terminalde React uygulamasının çalışmasını durdurmak için **ctrl+c** ile çıkın.

Sonra terminalde aşağıdaki komutu yazın ve  **Enter** ’a basın:

```bash
npm run preview
```

React uygulaması için tarayıcıda açık olan sayfayı yenileyin. Açık değilse, sol paneldeki **Skills Network** ikonuna tıklayın. Bu işlem  **SKILLS NETWORK TOOLBOX** ’ı açar. Ardından  **Launch Application** ’ı seçin. **Application Port** alanına **4173** port numarasını girin ve sağa doğru ok ikonuna tıklayın.

Çıktı, birden fazla heading ve her heading içinde birden fazla todo list eklendikten sonra verilen ekran görüntüsüne göre görüntülenecektir.

> Not- En güncel değişiklikleri görmek için terminalde `npm run preview` komutunu tekrar çalıştırmanız gerekir.

Tebrikler! Bir ToDo list React uygulaması oluşturdunuz!

---

## 🎉 Conclusion

Bu lab’de, **useState** hook’unu kullanarak bir React functional component’te state’in nasıl yönetileceğini öğrendiniz.  **todos** , **headingInput** ve **listInput** gibi state değişkenleri, Todo List’in state’ini ve kullanıcı input alanlarını korumak için kullanılır.

React’in **useState** hook’u tarafından korunan state’e dayanarak heading’leri ve ilişkili listeleri render etmeyi öğrendiniz.

Yeni heading ve list eklemek ve input alanlarındaki değişiklikleri yönetmek için event handling fonksiyonları uygulayan kod kullandınız. Bu fonksiyonlar Todo List state’ini günceller ve UI’daki değişiklikleri yansıtmak için yeniden render tetikler.

Input alanları, heading gösterimi, liste gösterimi ve liste ekleme işlevselliği için ayrı bölümler içeren, iyi yapılandırılmış bir Todo List bileşeni oluşturdunuz. Bu modüler yapı, kod okunabilirliğini ve sürdürülebilirliğini artırır.
