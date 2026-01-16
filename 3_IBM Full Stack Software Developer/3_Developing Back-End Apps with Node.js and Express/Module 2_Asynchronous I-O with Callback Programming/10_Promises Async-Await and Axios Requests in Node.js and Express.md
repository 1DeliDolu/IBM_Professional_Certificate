## 📘 Promises, Async/Await ve Node.js ile Express’te Axios İstekleri

### ⏱️ Tahmini gerekli süre

20 dakika,

---

## 🎯 Amaçlar

Bu okumada şunları öğreneceksiniz:

* *Promises* : JavaScript’te asenkron işlemleri ele almak için temel yapı taşı
* *Async/Await* :  *Promise* ’lerle çalışmak için modern ve daha okunabilir bir sözdizimi
* *Axios* : Ağ istekleri yapmak için yaygın kullanılan bir `HTTP` istemcisi

---

## 🧭 Giriş

JavaScript’in asenkron programlama modeli, tepkisel ve performanslı web uygulamaları geliştirmek için temeldir. Node.js ve Express’te asenkron işlemleri etkili biçimde ele almak; API istekleri yapmak, dosya okumak veya veritabanı sorgulamak gibi görevler için gereklidir.

---

## 🤝 1. Promises

Bir  *Promise* , asenkron bir işlemin nihai olarak tamamlanmasını (veya başarısız olmasını) ve ortaya çıkan değerini temsil eden bir nesnedir. İşlemleri daha okunabilir ve yönetilebilir bir şekilde zincirlemenize olanak tanır.

### 🚦 1.1 Bir Promise’in Durumları

### 🧱 1.2 Bir Promise Oluşturma

Bir *Promise* oluşturmak için, iki parametre alan (`resolve` ve `reject`) bir fonksiyon alan `new Promise` yapıcısını kullanırsınız. `resolve` fonksiyonu, asenkron işlem başarıyla tamamlandığında çağrılır; `reject` fonksiyonu ise başarısız olduğunda çağrılır.

```javascript
// Creating a new Promise object and assigning it to the variable myPromise
const myPromise = new Promise((resolve, reject) => {
 // Simulating a condition with a boolean variable 'success'
 let success = true;
 // If the condition is true, call resolve to mark the promise as fulfilled
 if (success) {
 resolve("The operation was successful!");
 } else {
 // If the condition is false, call reject to mark the promise as rejected
 reject("The operation failed!");
 }
});
```

### 🔗 1.3 `.then()` ve `.catch()` ile Promise Kullanımı

Çözümlenen değeri veya hatayı `.then()` ve `.catch()` metotlarıyla ele alabilirsiniz. Bu metotlar da *Promise* döndürür; böylece birden fazla asenkron işlemi sırayla zincirlemenize olanak tanır.

```javascript
// Execute the promise and handle the fulfilled and rejected states
myPromise
 // Handle the resolved state of the promise
 .then((message) => {
 // This block will execute if the promise is resolved
 console.log(message); // "The operation was successful!"
 })
 // Handle the rejected state of the promise
 .catch((error) => {
 // This block will execute if the promise is rejected
 console.error(error); // "The operation failed!"
 });
```

### 📄 1.4 Örnek: Dosya Okuma

Aşağıda `fs.promises` modülünü kullanarak bir dosya okuma örneği yer almaktadır. `fs.promises` modülü, dosya sistemi işlemleri için *Promise tabanlı* metotlar sağlar.

```javascript
// Import the 'fs' module and use its promise-based methods
const fs = require('fs').promises;
// Read the content of the file 'example.txt' with 'utf8' encoding
fs.readFile('example.txt', 'utf8')
 // Handle the resolved state of the promise
 .then((data) => {
 // This block will execute if the file is read successfully
 console.log(data); // Print the file content to the console
 })
 // Handle the rejected state of the promise
 .catch((err) => {
 // This block will execute if there is an error reading the file
 console.error('Error reading file:', err); // Print the error message to the console
 });
```

---

## ⏳ 2. Async/Await

Daha önce öğrenmiş olabileceğiniz gibi, Java Script tek iş parçacıklı ( *single-threaded* ) bir betik dilidir. Bu, sürecin yalnızca sıralı olarak gerçekleşebileceği ve iki sürecin aynı anda gerçekleşemeyeceği anlamına gelir. Bu, herhangi bir dil için büyük bir caydırıcıdır ve JS bunu  *Promise* ’ler aracılığıyla asenkron programlamayı tanıtarak çözmüştür.  *Promise* ’ler senkron programlamayla ilgili sorunları çözmüş olsa da, iç içe `then` kullanımı kodun yapısını ve okunabilirliğini karmaşıklaştırabilir.

`Async` ve `Await`,  *Promise* ’lerin üzerinde bir sözdizimsel şeker ( *syntactic sugar* ) sağlar; asenkron kodun daha çok senkron kod gibi görünmesini sağlar ve bu da okunmasını ve yazılmasını kolaylaştırır. Bir `async` fonksiyon bir *Promise* döndürür ve bir *Promise* `resolved` veya `rejected` olana kadar yürütmeyi duraklatmak için bir `async` fonksiyon içinde `await` kullanabilirsiniz.

### ✅ 2.1 Async/Await’in Faydaları:

### 🧩 2.2 `async` ve `await` Kullanımı

Bir `async` fonksiyon her zaman bir *Promise* döndürür. `async` fonksiyonun içinde, bir *Promise* `resolved` veya `rejected` olana kadar yürütmeyi duraklatmak için `await` anahtar sözcüğünü kullanabilirsiniz.

```javascript
// Async function that wraps the operation
async function myAsyncFunction() {
 // Simulating a condition with a boolean variable 'success'
 let success = true;
 // If the condition is true, resolve with a success message
 if (success) {
 return "The operation was successful!";
 } else {
 // If the condition is false, throw an error to simulate rejection
 throw new Error("The operation failed!");
 }
}
// Using async function to handle Promise
async function executeAsyncFunction() {
 try {
 // Await the async function call to get the result
 const result = await myAsyncFunction();
 console.log(result); // Output the result if successful
 } catch (error) {
 console.error(error.message); // Handle and output any errors
 }
}
// Call the async function to execute
executeAsyncFunction();
```

Bu örnek, `async` ve `await`’in JavaScript’te asenkron programlamayı nasıl basitleştirebileceğini gösterir. `async` fonksiyonu `myAsyncFunction`, koşullu bir işlemi simüle eder; koşul sağlanırsa bir başarı mesajı döndürür, aksi halde bir hata fırlatır. `executeAsyncFunction`, `myAsyncFunction`’u çağırmak için `await` kullanır ve sonucu veya olası hataları `try` ve `catch` ile ele alır. Bu yaklaşım, `.then()` ve `.catch()` zincirleriyle  *Promise* ’leri ele almaya kıyasla kodu daha kolay okunur ve anlaşılır hale getirir.

---

## 🌐 3. Axios İstekleri

Axios, tarayıcı ve Node.js için *Promise tabanlı* bir `HTTP` istemcisidir. REST uç noktalarına asenkron `HTTP` istekleri göndermeyi ve `CRUD` işlemlerini gerçekleştirmeyi kolaylaştırır. Axios, `JSON` verisini otomatik olarak dönüştürür ve temiz ve basit bir API sağlar.

### 🧰 3.1 Axios Nasıl Kullanılır

1. Axios’u aşağıdaki komutla yükleyebilirsiniz:

```bash
npm install axios
```

2. `GET` İsteği Yapma
   Axios, `HTTP GET` isteklerini kolaylaştırır. Bir genel API’den veri çekmek için örnek:

```javascript
// Import the axios library
const axios = require('axios');
// Using the axios.get method to make a GET request to the specified URL.
axios.get('https://api.example.com/data')
 // If the request is successful, the `.then` block is executed.
 .then(response => {
 // The response object contains the data returned from the server.
 // We log the `data` property of the response to the console.
 console.log(response.data);
 })
 // If there is an error during the request, the `.catch` block is executed.
 .catch(error => {
 
 // We log an error message to the console along with the error object.
 // This helps in debugging and understanding what went wrong with the request.
 
 console.error('Error fetching data:', error);
 });
```

`axios.get` metodu, yanıt nesnesiyle çözümlenen bir *Promise* döndürür; böylece `response.data` ile verilere erişmenizi sağlar.

3. `POST` İsteği Yapma:
   Bir sunucuya veri göndermek için `POST` isteği kullanın:

```javascript
// Import the axios library.
const axios = require('axios');
// Data to be sent in the POST request. This is a JavaScript object containing the user information.
const data = {
 name: 'John Doe',
 age: 30
};
// Using the axios.post method to make a POST request to the specified URL with the data object.
axios.post('https://api.example.com/users', data)
 
// If the request is successful, the `.then` block is executed.
 .then(response => {
 
// The response object contains the data returned from the server.
// We log a message along with the `data` property of the response to the console.
 
 console.log('User created:', response.data);
 })
 // If there is an error during the request, the `.catch` block is executed.
 
 .catch(error => {
 // We log an error message to the console along with the error object.
 // This helps in debugging and understanding what went wrong with the request.
 
 console.error('Error creating user:', error);
 });
```

Bu kod parçası, axios kullanarak `HTTP POST` istekleri yapmanın ve yanıtlar ile hataları ele almanın temel kullanımını gösterir.

---

## 🔄 4. Örnek: Axios ile Async/Await Kullanımı

`async/await` ile Axios’u birleştirmek, `HTTP` isteklerini ele almak için temiz bir yaklaşım sağlar:

```javascript
const axios = require('axios'); // For Node.js, or include via CDN for browser
// Asynchronous function to post data to an API
async function postData() {
 try {
 // Await the response from the Axios POST request
 let response = await axios.post('https://jsonplaceholder.typicode.com/posts', {
 title: 'foo', // The title of the post
 body: 'bar', // The body/content of the post
 userId: 1 // The user ID associated with the post
 });
 // Log the response data to the console
 console.log(response.data);
 } catch (error) {
 // If there is an error, log the error message to the console
 console.error('Error posting data:', error);
 }
}
// Call the async function to execute the request
postData();
```

Burada `await`, `POST` isteği tamamlanana kadar fonksiyon yürütmesini duraklatır ve sonuç `try` bloğu içinde ele alınır.

---

## 🧾 Özet

Bu okumada, Node.js ve Express’te asenkron programlamanın temel kavramlarını;  *Promise* ’lere, `async/await` sözdizimine ve Axios `HTTP` istemcisine odaklanarak öğrendiniz.  *Promise* ’ler, işlemleri zincirlemeye izin vererek asenkron işlemleri ele almanın bir yolunu sunar; kodu daha okunabilir ve yönetilebilir hale getirir. `async/await` sözdizimi  *Promise* ’lerin üzerine inşa edilir; böylece senkron koda benzeyen asenkron kod yazmanızı sağlar ve asenkron görevlerin ele alınmasını basitleştirir. Son olarak, harici API’ler ve servislerle etkileşim için gerekli olan Axios ile `HTTP` istekleri yapmayı keşfettiniz. Bu kavramlarda ustalaşarak, sağlam web uygulamaları geliştirmek için kritik olan daha verimli ve sürdürülebilir asenkron kod yazabilirsiniz.

---

## 👤 Yazar(lar)

Rajashree Patil
Sapthashree K S

Skills Network
