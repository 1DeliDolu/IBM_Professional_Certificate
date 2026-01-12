## ✅ Lesson 1 Summary: Introduction to Function Components

Tebrikler! Bu dersi tamamladınız. Bu noktada kursta şunları biliyorsunuz:

* *Props* ilkeleri  **reusability** ,  **unidirectional data flow** , **customization** ve **composition** kavramlarını içerir.
* Bir alt bileşeni kontrol etmek için bir event ile birlikte **useState** hook’unu kullanabilirsiniz.
* Daha karmaşık bir UI oluşturmak için daha küçük bileşenleri birleştirmede ( *component composition* ) kullanırsınız.
* Component composition ilkeleri  **abstraction** ,  **reusability** ,  **hierarchy** , **props and children** ve **higher-order components** kavramlarını içerir.
* *State management* , bir bileşen içinde zamanla değişebilecek veriyi yönetmenizi sağlar.
* **useState** hook’u, function component’lerin bileşenin state’ini yerel olarak yönetmesini sağlar.

---

## 🪝 useState Hook Sözdizimi

**useState** hook’unu kullanırken şu sözdizimini kullanabilirsiniz:

* **useState** fonksiyonunu çağırın ve başlangıç state değerini parametre olarak verin.
* Dönüş değerini *destructured array* kullanarak bir `const` dizi değişkenine atayın.
* Dizi iki değere sahiptir: **state name** ve başına **set** anahtar kelimesi getirilmiş  **state name** .

---

## 🔄 Lifecycle Aşamaları

* **Mounting** aşaması, bileşeni başlatır, başlangıç state’ini ayarlar ve yan etkileri ( *side effects* ) gerçekleştirir.
* **Updating** aşamasında React, fonksiyon gövdesini yeniden çağırır ve JSX’i yeniden değerlendirir.
* **Unmounting** aşamasında React, bir bileşeni DOM’dan kaldırırken cleanup işlemlerini yürütür.
