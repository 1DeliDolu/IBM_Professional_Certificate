
## ⚛️ React ile Front-End Uygulama Geliştirme: Özet

### 🏗️ 1. React ve ES6 ile Zengin Front-End Uygulamaları Oluşturma

React, kullanıcı arayüzleri oluşturmak için verimli ve esnek bir JavaScript kütüphanesidir.

JavaScript’te ES6’nın bir parçası olarak sunulan yeni özellikler `let`, `const`,  *arrow functions* , *promise* ve  *class* ’tır.

JSX kullanmanın başlıca faydaları, HTML içinde JavaScript’in tüm gücünden yararlanabilmeniz ve bir şablonlama dili öğrenmek veya kullanmaktan kaçınabilmenizdir. React’in faydalı hata ve uyarı mesajları göstermesini sağlar.

React bileşenlerinin dört türü: Fonksiyonel ( *Functional* ), Sınıf ( *Class* ), Saf ( *Pure* ) ve Yüksek Dereceli ( *High-order* ) bileşenlerdir.

Fonksiyonel bileşenler, bileşenin yaşam döngüsünün yönetilmesine gerek olmadığında en kullanışlıdır.

Sınıf bileşenleri daha çok yönlüdür.

---

## 🧩 2. React Bileşenleri

State, React’in bileşenin mevcut durumu hakkında bilgiyi temsil etmek için kullandığı düz bir JavaScript nesnesidir.

Props, *properties* kelimesinin kısaltılmış halidir ve React bileşenleri arasında veriyi ebeveynden çocuğa tek yönlü bir akışla aktarmak için kullanılır.

Bileşenler arasında veri aktarımı; ebeveynden çocuğa özellikler ( *properties* ) ile, çocuktan ebeveyne  *callback* ’ler ile ve kardeş bileşenler arasında gerçekleşebilir.

Bileşenler DOM üzerinde oluşturulur veya mount edilir; güncellenerek büyür ve ardından DOM’dan kaldırılır veya unmount edilir. Buna bileşen yaşam döngüsü ( *component lifecycle* ) denir.

React bileşenleri Mocha, Chai ve Sinon kullanılarak test edilebilir; ancak tercih edilen yaklaşımlar Jest ve React Testing Library kullanmaktır.

---

## 🧠 3. İleri Seviye React

Hooks, sınıflar olmadan *context* veya *state* gibi işlevleri kullanmanın bir yolunu sağlar.

React’te input’lar iki türden biri olabilir: kontrollü ( *controlled* ) veya kontrolsüz ( *uncontrolled* ).

Redux, uygulamanızın durumunu ( *state* ) yönetmek için React ile birlikte sıklıkla kullanılan bir state yönetim kütüphanesidir.

Bileşen özelliklerini güncellemede yer alan Redux öğeleri  *action* , *store* ve  *reducer* ’dır.

React Redux uygulamanızda *middleware* kullanarak asenkron verilerle etkileşime girebilirsiniz.

React-Redux uygulamasındaki veri akışı tek yönlüdür ( *unidirectional* ).
