## 🧪 Uygulamalı Laboratuvar: React ile Hello World


Tahmini Süre: 20 dakika

Bu laboratuvarda, ilk React sayfanızı ve ilk React uygulamanızı oluşturacaksınız. Kod dünyasında yeni bir şey öğrenmenin ilk adımı olarak, bir **“Hello World”** sayfası render edeceksiniz.

---

## 🎯 Öğrenme Hedefleri

Bu alıştırmayı tamamladıktan sonra aşağıdaki görevleri yapabiliyor olmalısınız:

* Basit bir React sayfası oluşturma
* Bir React uygulaması oluşturma, çalıştırma ve render etme
* Bir React bileşeni için özellik (properties) ayarlama

---

## 🖥️ İlk React Uygulaması

Laboratuvarın üst kısmındaki menüden  **Terminal** ’e gidin ve yeni bir terminal açın.

Terminalde, `/home/project` dizinine gitmek için aşağıdaki komutu yapıştırıp çalıştırın.

```bash
cd /home/project
```

Vite aracıyla `myfirstapp` adlı bir React uygulaması oluşturmak için aşağıdaki komutu çalıştırın. React uygulaması adının büyük harf içermemesi zorunludur.

```bash
npm create vite@latest myfirstapp -- --template react
```

Gerekli paketlerin kurulabileceğini onaylamanız istenir. Kurulumu başlatmak için klavyenizde **y** tuşuna basarak onaylayın.

Kurulum tamamlandığında uygulama, sizin belirttiğiniz adla bir klasör içinde oluşturulur. Aşağıdaki komutla bu klasöre geçin.

```bash
cd myfirstapp
```

React uygulamasını çalıştırmak için gerekli tüm dosyaları kurmak üzere şu komutu çalıştırın:

```bash
npm install
```

Ardından terminalde aşağıdaki komutları yazarak `package.json` dosyasındaki script’leri güncelleyin ve Enter’a basın.

```bash
npm pkg set scripts.lint="eslint . --ext js,jsx --report-unused-disable-directives --max-warnings 0"
```

```bash
npm pkg set scripts.preview="vite build && vite preview --host"
```

Oluşturulan React uygulamasını kontrol etmek için aşağıdaki komutu çalıştırın.

```bash
npm run preview
```

React uygulamanızın nasıl göründüğünü görmek için soldaki **Skills Network** düğmesine tıklayın (1 numaraya bakın). Bu işlem “Skills Network Toolbox”’ı açacaktır. Ardından “Launch Application”’ı seçin (2 numaraya bakın). Sonrasında “Application Port” alanına **4173** port numarasını girin (3 numaraya bakın) ve bu düğmeye tıklayın.

Launch Application

Bu, uygulamayı yeni bir tarayıcı sekmesinde başlatacaktır.

Vite n react.png

React geliştirme sunucusunu durdurmak için komut isteminde **Ctlr+C** tuşlarına basın.

---

## ✏️ Hello World Uygulamasını Değiştirme

`myfirstapp` proje klasörünün içindeki `src` klasörü altında `App.jsx` ve `main.jsx` dosyalarını bulacaksınız.

file structure 1.png

`src` klasörü içindeki `main.jsx` dosyasında aşağıdaki kodu değiştirin. Sonuç olarak tüm stil kaldırılacak ve size yalnızca temel ihtiyaçlar kalacaktır.

```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <App />
);
```

`src` klasörü içindeki `App.jsx` içeriğini aşağıdaki kodla değiştirin:

```javascript
function App() {
  return (
      <h1>Hello World</h1>
  );
}
export default App;
```

Şimdi sunucuyu tekrar başlatın ve uygulamayı tarayıcıda başlatıp görüntülemek için daha önce belirtilen adımları izleyin.

```bash
npm run preview
```

Aşağıdaki Launch Application’a tıklayın.

Launch Application

“Hello World” mesajıyla render edilen sayfayı göreceksiniz.

---

## ⏰ Zamanla Birlikte Hello World

`App.jsx` dosyasındaki kodu aşağıda gösterilen kodu yapıştırarak değiştirin. Tarayıcı sayfasında Hello World mesajıyla birlikte zaman damgasını da render edecektir.

```javascript
function App(props) {
  const currDate = new Date();
  return (
    <div>
      <h1>Hello, world!</h1>
      <h2>The time now is {currDate.toLocaleTimeString()}.</h2>
    </div>
  );
}
export default App;
```

Şimdi “Hello World” ile birlikte zamanı da göreceksiniz. Şimdi sunucuyu durdurun ve tarayıcıda uygulamayı başlatıp görüntülemek için tekrar çalıştırın.

Zamanın güncel kalmasını ve sürekli değişmesini sağlamak için `main.jsx` dosyasındaki kodu aşağıdaki kodu yapıştırarak değiştirin:

```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
const root = ReactDOM.createRoot(document.getElementById('root'));
function ref() {
  root.render(<App/>);
}
setInterval(ref, 1000);
```

Şimdi sunucuyu tekrar başlatın; eğer çalışmıyorsa, tarayıcıda uygulamayı başlatıp görüntülemek için daha önce belirtilen adımları izleyin.

```bash
npm run preview
```

Launch Application

---

## 🧩 Alıştırma

* “Hello World” mesajını, bunun yerine adınızı gösterecek şekilde değiştirin.
* Tarihi, zamanla birlikte gösterecek şekilde kodu değiştirin.

İpucu için buraya tıklayın

1
`currDate.toLocaleDateString()` kullanarak tarih string’ini alın.

Çözüm için buraya tıklayın

```javascript
function App(props) {
  const currDate = new Date();
  return (
    <div>
      <h1>Hello, world!</h1>
      <h2>It is {currDate.toLocaleDateString()} and the time now is {currDate.toLocaleTimeString()}.</h2>
    </div>
  );
}
export default App;
```

Tebrikler! Vite build tool kullanarak ilk React projenizi başarıyla tamamladınız. Yeni bir React uygulaması başlattınız, geliştirme sunucusunu çalıştırdınız ve ilk “Hello World” bileşeninizi tarayıcıda render ettiniz. Bu laboratuvar, React ve Vite ile modern front-end geliştirmeye attığınız ilk adımı işaret ediyor!

---

## ✍️ Yazar(lar)

Lavanya T S

© IBM Corporation. Tüm hakları saklıdır.
