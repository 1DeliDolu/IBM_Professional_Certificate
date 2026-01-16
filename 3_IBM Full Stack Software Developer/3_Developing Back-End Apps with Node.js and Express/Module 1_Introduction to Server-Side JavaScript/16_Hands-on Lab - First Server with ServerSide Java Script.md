## 🧪 Uygulamalı Laboratuvar - Sunucu Tarafı JavaScript ile İlk Sunucu (20 dk)

### 🎯 Egzersizin Amacı

* Terminali kullanarak `git clone` yapmak ve Node.JS sunucu kodunu almak
* Sunucu tarafı JavaScript kullanarak bir web sunucusu oluşturmak
* Sunucuyu çalıştırmak
* İstemciden sunucuya erişmek ve sunucudan bir yanıt almak

---

## ✅ Adım 1: Ortamı ve Komut Satırı Araçlarını Doğrulama

1. Düzenleyicideki menüyü kullanarak bir terminal penceresi açın:  **Terminal > New Terminal** .
2. *node CLI* ’nin yüklü olduğunu doğrulayın.

```bash
node --version
```

Şuna benzer bir çıktı görmelisiniz (sürümler farklı olabilir):

```bash
v19.9.0
```

3. Proje klasörünüze geçin.

```bash
cd /home/project
```

4. Bu laboratuvar için gerekli yapıtları ( *artifacts* ) içeren git deposunu, zaten mevcut değilse klonlayın.

```bash
git clone https://github.com/ibm-developer-skills-network/lkpho-Cloud-applications-with-Node.js-and-React.git
```

5. Bu laboratuvarın dizinine geçin.

```bash
cd lkpho-Cloud-applications-with-Node.js-and-React/CD220Labs/http_server
```

6. Bu laboratuvarın yapıtlarını görmek için bu dizinin içeriğini listeleyin.

```bash
ls
```

7. `index.js` içeriğini kontrol edin. Bu, bir sonraki bölümde çalıştıracağımız sunucu tarafı betiktir.

```bash
cat index.js
```

Şuna benzer bir çıktı görmelisiniz:

```javascript
// HTTP modülünü içe aktar
const http = require('http');
// İstek dinleyici fonksiyonunu tanımla
const requestListener = function (req, res) {
 res.writeHead(200); // Durum kodunu 200 (OK) olarak ayarla
 res.end('Hello, World!'); // "Hello, World!" yanıtını gönder
};
// Port numarasını tanımla
const port = 8080;
// İstek dinleyici fonksiyonunu kullanarak bir HTTP sunucusu oluştur
const server = http.createServer(requestListener);
// Sunucuyu başlat ve belirtilen portu dinle
server.listen(port);
console.log('Server listening on port: ' + port);
```

**Açıklama:**

* **HTTP Modülü** Node.js’ten HTTP modülünü içe aktarır.
* **İstek Dinleyici Fonksiyonu** Gelen HTTP isteklerini işleyen bir istek dinleyici fonksiyonu tanımlar. Bu durumda fonksiyon durum kodunu 200 (OK) olarak ayarlar ve `"Hello, World!"` yanıtını gönderir.
* **Port Tanımı** `const port = 8080;` kullanarak port numarasını 8080 olarak tanımlar.
* **HTTP Sunucusu Oluşturma** `http.createServer(requestListener);` kullanarak bir HTTP sunucusu oluşturur; burada `requestListener` tanımlanmış istek dinleyicidir.
* **Sunucuyu Başlatma** `server.listen(port);` kullanarak sunucuyu başlatır ve belirtilen portu dinler. Ayrıca sunucunun belirtilen portu dinlediğini belirten bir mesajı loglar.

Alternatif olarak, `index.js` içeriğini dosya gezgini menüsü üzerinden de görüntüleyebilirsiniz. Şöyle görünecektir.

---

## 🖥️ Adım 2: node CLI’yi Kullanma

1. Sunucuyu başlatmak için `index.js` dosyasını `node` komutuyla çalıştırırız.

```bash
node index.js
```

Şuna benzer bir çıktı görmelisiniz:

```bash
server listening on port: 8080
```

2. Terminali bölmek için aşağıdaki görselde gösterildiği gibi  **Split Terminal** ’a tıklayın.
3. İkinci terminal penceresinde, uygulamayı yoklamak ( *ping* ) için `curl` komutunu kullanın.

```bash
curl localhost:8080
```

Şuna benzer bir çıktı görmelisiniz:

```bash
Hello, World!
```

Bu, uygulamanızın çalıştığını göstermelidir.

4. Aynısını tarayıcı penceresi ile doğrulamak için soldaki **Skills Network** düğmesine tıklayın; bu, “Skills Network Toolbox”’ı açacaktır. Ardından  **Other** ’a, sonra  **Launch Application** ’a tıklayın. Buradan sunucunun çalıştığı port numarasını (8080) girip başlatabilirsiniz.
   Yeni bir tarayıcı penceresi aşağıdaki gibi açılacaktır. (Not: Tarayıcı ayarlarınız açılır pencerelere izin vermiyorsa yeni tarayıcı penceresi açılmayabilir.)
5. Sunucuyu durdurmak için ana komut penceresine gidin ve sunucuyu durdurmak için **Ctrl+c** tuşlarına basın ve o terminalde kalın.

---

## 🔗 Adım 3: Başka Bir Modül Gerektiren Sunucu Betiğini node CLI ile Çalıştırma

1. Aynı terminalde `today.js` içeriğini kontrol edin.

```bash
cat today.js
```

Şuna benzer bir çıktı görmelisiniz:

```javascript
// Modülden 'getDate' adlı bir fonksiyonu dışa aktar
module.exports.getDate = function getDate() {
 // "Australia/Brisbane" saat diliminde geçerli tarih ve saati al
 let aestTime = new Date().toLocaleString("en-US", {timeZone: "Australia/Brisbane"});
 return aestTime; // Biçimlendirilmiş tarih ve saati döndür
};
```

**Açıklama:**

* **Fonksiyon Dışa Aktarma** `module.exports` kullanarak modülden `getDate` adlı bir fonksiyonu dışa aktarır.
* **Tarih Biçimlendirme** `getDate` fonksiyonu içinde `new Date().toLocaleString(“en-US”, {timeZone: “Australia/Brisbane”})` kullanarak geçerli tarih ve saati alır. Bu, tarih ve saati “Australia/Brisbane” saat dilimine göre biçimlendirir.
* **Dönüş Değeri** `return aestTime;` kullanarak biçimlendirilmiş tarih ve saati döndürür.

Alternatif olarak, `today.js` içeriğini dosya gezgini menüsü üzerinden de görüntüleyebilirsiniz. Şöyle görünecektir.
Bu dışa aktarılan modülü sunucu tarafı betikte kullanacağız.

2. `index-with-require.js` içeriğini kontrol edin. Gözlemleyeceğiniz üzere, bu betik bir önceki adımda içeriğini gördüğümüz `today` modülünü `require` eder.

```bash
cat index-with-require.js
```

Şuna benzer bir çıktı görmelisiniz:

```javascript
// HTTP modülünü içe aktar
const http = require('http');
// 'today' modülünü içe aktar
const today = require('./today');
// İstek dinleyici fonksiyonunu tanımla
const requestListener = function (req, res) {
 res.writeHead(200); // Durum kodunu 200 (OK) olarak ayarla
 // 'today' modülünden alınan geçerli tarih ile yanıtı gönder
 res.end(`Hello, World! The date today is ${today.getDate()}`);
};
// Port numarasını tanımla
const port = 8080;
// İstek dinleyici fonksiyonunu kullanarak bir HTTP sunucusu oluştur
const server = http.createServer(requestListener);
// Sunucuyu başlat ve belirtilen portu dinle
server.listen(port);
console.log('Server listening on port: ' + port);
```

**Açıklama:**

* **HTTP Modülü** Node.js’ten HTTP modülünü içe aktarır.
* **Modül İçe Aktarma** `const today = require('./today');` kullanarak `today` modülünü içe aktarır. Bu, `getDate` adlı bir fonksiyonu dışa aktaran `today` adlı bir modül olduğunu varsayar.
* **İstek Dinleyici Fonksiyonu** Gelen HTTP isteklerini işleyen bir istek dinleyici fonksiyonu tanımlar. Bu durumda fonksiyon durum kodunu 200 (OK) olarak ayarlar ve `today` modülünden `getDate` fonksiyonunu kullanarak `"Hello, World! The date today is {current date}"` yanıtını gönderir.
* **Port Tanımı** `const port = 8080;` kullanarak port numarasını 8080 olarak tanımlar.
* **HTTP Sunucusu Oluşturma** `http.createServer(requestListener);` kullanarak bir HTTP sunucusu oluşturur; burada `requestListener` tanımlanmış istek dinleyicidir.
* **Sunucuyu Başlatma** `server.listen(port);` kullanarak sunucuyu başlatır ve belirtilen portu dinler. Ayrıca sunucunun belirtilen portu dinlediğini belirten bir mesajı loglar.

Alternatif olarak, `index-with-require.js` içeriğini dosya gezgini menüsü üzerinden de görüntüleyebilirsiniz. Şöyle görünecektir.

3. Sunucuyu başlatmak için `index-with-require.js` dosyasını `node` komutuyla çalıştırırız.

```bash
node index-with-require.js
```

Şuna benzer bir çıktı görmelisiniz:

```bash
server listening on port: 8080
```

4. Daha önce açtığınız ikinci terminal penceresinde, uygulamayı yoklamak ( *ping* ) için `curl` komutunu kullanın.

```bash
curl localhost:8080
```

Şuna benzer bir çıktı görmelisiniz:

```bash
Hello, World! The date today is Wed Oct 14 2020 14:56:42 GMT+1030 (Australian Eastern Standard Time)
```

Bu, uygulamanızın çalıştığını göstermelidir.

5. Aynısını tarayıcı penceresi ile doğrulamak için soldaki **Skills Network** düğmesine tıklayın; bu, “Skills Network Toolbox”’ı açacaktır. Ardından  **Other** ’a, sonra  **Launch Application** ’a tıklayın. Buradan port numarası olarak **8080** girip başlatabilmelisiniz.
   Yeni bir tarayıcı penceresi açılacak ve saat diliminizdeki tarih ve saat ile birlikte `Hello World!` gösterecektir.

---

## 🧠 Challenge

Günün saatine bağlı olarak kullanıcıyı selamlamak için `index-with-require.js` ve `today.js` dosyalarında değişiklik yapın.

* `today.js` dosyasını, `toLocaleString()`’den bir string döndürmek yerine doğru saat dilimi uygulanmış uygun bir *Date* nesnesi döndürecek şekilde güncelleyin.
* `index-with-require.js` dosyasını, `today.js`’den gelen güncellenmiş *Date* nesnesini kullanacak şekilde değiştirin.
* Bu değişiklikler, `getHours()` gibi fonksiyonların doğru çalışmasını sağlayacaktır.

`index-with-require.js` için örnek bir çözüme buradan tıklayın.

```javascript
// Import the HTTP module
const http = require('http');
// Import the 'today' module
const today = require('./today');
// Define the request listener function
const requestListener = function (req, res) {
 res.writeHead(200); // Set the status code to 200 (OK)
 let dateVal = today.getDate(); // Get the current date from the 'today' module
 // Determine the appropriate greeting based on the current time
 let greeting = "It is still not morning";
 if (dateVal.getHours() > 6 && dateVal.getHours() < 12) {
 greeting = "Good morning!";
 } else if (dateVal.getHours() >= 12 && dateVal.getHours() < 18) {
 greeting = "Good afternoon!";
 } else if (dateVal.getHours() >= 18 && dateVal.getHours() < 21) {
 greeting = "Good evening!";
 } else if (dateVal.getHours() >= 21 && dateVal.getHours() < 24) {
 greeting = "Good night!";
 }
 // Send the response with the appropriate greeting
 res.end(`Hello, ${greeting}`);
};
// Define the port number
const port = 8080;
// Create an HTTP server using the request listener function
const server = http.createServer(requestListener);
// Start the server and listen on the specified port
server.listen(port);
console.log('Server listening on port: ' + port);
```

`today.js` için örnek bir çözüme buradan tıklayın.

```javascript
module.exports.getDate = function getDate() {
 // Get the current date and time string in the timezone "Australia/Brisbane"
 let aestString = new Date().toLocaleString("en-US", { timeZone: "Australia/Brisbane" });
 // Convert that string back into a Date object
 let aestDate = new Date(aestString);
 return aestDate;
};
```

---

## 🎉 Tebrikler

Laboratuvarı tamamladınız.

---

## 🧾 Özet

Artık bir sunucuyu nasıl çalıştıracağınızı öğrendiğinize göre, kendi Node.JS sunucunuzu oluşturmaya hazırsınız.

---

## ✍️ Yazar(lar)

Lavanya

---

## © IBM Corporation

Tüm hakları saklıdır.
