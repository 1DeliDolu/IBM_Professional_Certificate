## 🧾 Developing Back-End Apps with Node.js and Express

### 📝 Module 1 Cheat Sheet: Introduction to Server-Side JavaScript

---

### 🌐 `http/createServer`

**Açıklama**
`http` paketi, bir sunucuya uzaktan bağlantı kurmak veya istemciyi dinleyen bir sunucu oluşturmak için kullanılır.

`createServer` — *requestListener* alır; bu, `request` ve `response` parametrelerini alan bir fonksiyondur. Burada `request`, istemciden gelen isteğin tanıtıcısıdır; `response` ise istemciye gönderilecek yanıtın tanıtıcısıdır.

**Kod Örneği**

```javascript
const http = require('http');
const requestListener = function(req, res) {
  res.writeHead(200);
  res.end('Hello, World!');
}
const port = 8080;
const server = http.createServer(requestListener);
console.log('server listening on port: '+ port);
server.listen(port);
```

---

### 📅 `new Date()`

**Açıklama**
`new Date()` metodu, geçerli tarihi bir nesne ( *object* ) olarak döndürür. Tarih nesnesi üzerinde biçimlendirme yapmak veya saat dilimini değiştirmek için metotlar çağırabilirsiniz.

**Kod Örneği**

```javascript
module.exports.getDate = function getDate() {
    let aestTime = new Date().toLocaleString("en-US", {timeZone: "Australia/Brisbane"});
    return aestTime;
}
```

---

### 📥 `import()`

**Açıklama**
`import` ifadesi, başka bir modülün dışa aktardığı ( *export* ) modülleri içe aktarmak için kullanılır. Yeniden kullanılabilir kod içeren bir dosya bir modül olarak adlandırılır.

**Kod Örneği**

```javascript
// addTwoNos.mjs
function addTwo(num) {
  return num + 4;
}
export { addTwo };
// app.js
import { addTwo } from './addTwoNos.mjs';
// Prints: 8
console.log(addTwo(4));
```

---

### 🧩 `require()`

**Açıklama**
Yerleşik ( *built-in* ) NodeJS metodu `require()`, farklı dosyalarda yer alan harici modülleri dahil etmek için kullanılır. `require()` ifadesi temelde bir JavaScript dosyasını okur ve çalıştırır; ardından `export` nesnesini döndürür.

**Kod Örneği**

```javascript
module.exports = 'Hello Programmers';
let msg = require('./messages.js');
console.log(msg);
```
