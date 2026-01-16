## 🚀 Gelişmiş Node.JS Modülleri

### 🎯 Hedefler

Bu okumayı tamamladıktan sonra, Node.js modüllerinin üç türünü tanımlayabileceksiniz. Ayrıca, bazı önde gelen *core* (çekirdek) modüllerin ne amaçla kullanılabileceğini açıklayabileceksiniz.

---

### 📚 Kütüphaneler ve Modüller

Kütüphaneler, Node.js açısından modüller ile aynı şeydir. Kütüphaneler, bir uygulama boyunca yeniden kullanılabilecek şekilde geliştirilmiş kod içerir.

Üç tür modül vardır:  *core* , *local* ve  *third-party* .

---

### 🧱 Modül Türleri

#### 🧩 Core (Çekirdek) Modüller

Core Node.js modülleri minimal bir kütüphane oluşturur. Node.js uygulamaları geliştirmek için gereken minimum işlevselliği içerirler.

#### 🏗️ Local (Yerel) Modüller

Local modüller, Node.js uygulamanızı oluşturmanın bir parçası olarak sizin ve geliştirme ekibinin yazdığı modüllerdir.

#### 🌍 Third-Party (Üçüncü Taraf) Modüller

Third-party modüller çevrimiçi olarak mevcuttur ve back-end Node.js topluluğu tarafından oluşturulmuştur. Bu kütüphaneler, lisanslarında belirtildiği şekilde kullanılabilir.

Birçok third-party modül ya kamu malıdır ( *public domain* ) ve lisans gerektirmez ya da açık kaynaktır ( *open source* ). Açık kaynak kaynaklar genellikle, geliştiricinin kodu kullanmasına ve değiştirmesine izin veren, ancak geliştiricinin çalışmalarını aynı lisans altında paylaşmasını da gerektiren *“copyleft”* lisansı tarafından yönetilir.

---

### 🧰 Önemli Core Modüller

Core modüllerin en önemlileri `http`, `path`, `fs`, `os`, `util`, `url` ve `querystring` modülleridir. Şimdi bunların her birini kısaca ele alalım ve kod örnekleri verelim.

---

### 🌐 http Modülü

`http` modülü, HTTP üzerinden veri aktarmak için yöntemler sağlar. Uygulamanıza `http` modülünü dahil etmek için onu `require` etmelisiniz.

Aşağıda `http` modülünü kullanarak bir sunucu örneği oluşturan örnek kod yer almaktadır. Bu kod, sunucu örneğini oluşturmak için `http.createServer()` yöntemini kullanır.

```javascript
let http = require('http');
http.createServer(function (req, res) {
 res.write('hello from server');//istemciye bir yanıt yaz
 res.end();//istemciden yanıtın sonu
}).listen(6000);//sunucu örneği 6000 portunda http isteklerini dinler
```

---

### 📁 fs Modülü

`fs` modülü bir dosya sistemiyle etkileşim kurmak için kullanılır. Node.js çekirdeğinin bir parçası olduğu için kurulmasına gerek yoktur ve basitçe `require` edilebilir.

Aşağıdaki kod örneği, `fs` modülünü kullanarak yerel bir dosyayı asenkron olarak okur ve dosya içeriğini konsola yazdırır.

```javascript
const fs = require('fs');
// 'sample.txt' dosyasını asenkron olarak oku
fs.readFile('sample.txt', 'utf8', (err, data) => {
 if (err) {
 console.error(err);
 return;
 }
 // 'sample.txt' içeriğini konsola yazdır
 console.log(data);
});
```

`fs` modülü, giriş ve çıkış için ( *I/O* ) de kullanılabilir. `fs` modül yöntemleri, harici bir dosyadan bilgi almak veya harici bir dosyaya veri yazmak için kullanılabilir.

```javascript
const fs = require('fs');
// '/content.md' dosyasının içeriğini senkron olarak oku ve 'data' içinde sakla
const data = fs.readFileSync('/content.md', 'utf8');
// 'content.md' içeriğini konsola yazdır
console.log(data);
```

---

### 🖥️ os Modülü

`os` modülü, uygulamanın üzerinde çalıştığı işletim sistemi hakkında bilgi almak ve onunla etkileşim kurmak için yöntemler sağlar.

Bu, bilgisayarın platformunu ve mimarisini alan `os` modülünden örnek bir koddur.

```javascript
let os = require('os');
console.log("Computer OS Platform Info : " + os.platform());
console.log("Computer OS Architecture Info: " + os.arch());
```

---

### 🗺️ path Modülü

`path` modülü, dizin ve dosya yollarını almanıza ve değiştirmenize olanak tanır.

Aşağıdaki kod, verilen bir dosya yolunun son kısmını alır ve bu değeri konsola yazdırır:

```javascript
const path = require('path');
let result = path.basename('/content/index/home.html');
console.log(result); //konsola home.html çıktısını verir
```

---

### 🛠️ util Modülü

Node.js `util` modülü, *debugging* (hata ayıklama) ve fonksiyonları kullanım dışı bırakma ( *deprecating* ) gibi görevleri gerçekleştirmek için dahili kullanım amaçlıdır.

Diyelim ki bir programda bir döngüdeki iterasyon sayısını saymak için hata ayıklamak istiyorsunuz. `util.format()` yöntemini aşağıdaki gibi kullanabilirsiniz:

```javascript
let util = require('util');
let str = 'The loop has executed %d time(s).';
for (let i = 1; i <= 10; i++) {
 console.log(util.format(str, i)); // 'The loop has executed i time(s)' çıktısını verir
}
```

---

### 🔗 url Modülü

`url` modülü, bir web adresini okunabilir parçalara bölmek için kullanılır.

Aşağıda, verilen URL’den `"firstName"` sorgu nesnesinin değerini döndüren örnek kod yer almaktadır.

```javascript
const url = require('url');
let webAddress = 'http://localhost:2000/index.html?lastName=Kent&firstName=Clark';
let qry = url.parse(webAddress, true);
let qrydata = qry.query; //bir nesne döndürür: {lastName: 'Kent', firstName: 'Clark'}
console.log(qrydata.firstName); //Clark çıktısını verir
```

---

### 🧾 querystring Modülü

`querystring` modülü, bir URL’nin  *query string* ’i üzerinden ayrıştırma yapmak için yöntemler sağlar.

Örneğin,

```javascript
let qry = require('querystring');
let qryParams = qry.parse('lastName=Kent&firstName=Clark');
console.log(qryParams.firstName); //Clark döndürür
```

---

### 🧩 Üçüncü Taraf Paketler

Node.js ile kullanım için bir dizi faydalı third-party paket de vardır. Bunlardan bazıları AsyncJS, Axios ve Express’tir. Bu kütüphaneler kursun ilerleyen bölümlerinde tartışılacaktır.
