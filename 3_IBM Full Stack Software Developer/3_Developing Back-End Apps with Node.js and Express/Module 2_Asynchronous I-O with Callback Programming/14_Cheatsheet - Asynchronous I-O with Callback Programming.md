## 🧾 Developing Back-End Apps with Node.js and Express

## 🧠 Module 2 Cheat Sheet: Callback Programlama ile Asenkron I/O

### ⏳ Async-await

 *Promise* ’leri, yalnızca asenkron fonksiyonların içinde çağrılıyorlarsa `await` edebiliriz.

```javascript
const axios = require('axios').default;
let url = "some remote url"
async function asyncCall() {
  console.log('calling');
  const result = await axios.get(url);
  console.log(result.data);
}
asyncCall();
```

---

### 🔁 Callback

Callback’ler parametre olarak geçirilen metotlardır. Parametre olarak geçirildikleri metodun içinde, koşullu veya koşulsuz olarak çağrılırlar. Yanıtları veya hataları işlemek için callback’leri bir *promise* ile birlikte kullanırız.

```javascript
//function(res) and function(err) are the anonymous callback functions
axios.get(url).then(function(res) {
    console.log(res);
}).catch(function(err) {
    console.log(err)
})
```

---

### 🤝 Promise

Nihai tamamlanmayı veya başarısızlığı temsil eden ve bazı metotlar tarafından döndürülen bir nesnedir. *Promise* `fulfilled` olana veya bir exception fırlatılana kadar kod bloke olmadan çalışmaya devam eder.

```javascript
axios.get(url).then(
  //do something
).catch(
  //do something
) 
```

---

### 🧩 Promise use case

Çağırdığımız fonksiyonun işlem süresi uzun sürdüğünde, örneğin uzak `URL` erişimi, dosya okuma gibi *I/O* işlemleri vb. durumlarda  *promise* ’ler kullanılır.

```javascript
let prompt = require('prompt-sync')();
let fs = require('fs');
const methCall = new Promise((resolve,reject)=>{
    let filename = prompt('What is the name of the file ?');
    try {
      const data = fs.readFileSync(filename, {encoding:'utf8', flag:'r'});
      resolve(data);
    } catch(err) {
      reject(err)
    }
});
console.log(methCall);
methCall.then(
  (data) => console.log(data),
  (err) => console.log("Error reading file")
);
```

---

### 📡 object.on()

Framework bir event gerçekleştiğinde çağırdığı bir event handler tanımlar.

```javascript
http.request( options, function(response) {
 let buffer = ‘’;
 ...
 response.on('data', function(chunk) {
   buffer += chunk;
 });
 response.on('end', function() {
   console.log(buffer);
 });
}).end();
```

---

### 🔺 Callback Hell / The Pyramid of Doom

İç içe callback’lerin alt alta yığılması ve önceki callback’i beklemesi. Bu, kodun okunabilirliğini ve sürdürülebilirliğini etkileyen bir piramit yapısı oluşturur.

```javascript
const makeCake = nextStep => {
  buyIngredients(function(shoppingList) {
    combineIngredients(bowl, mixer, function(ingredients){
      bakeCake(oven, pan, function(batter) {
        decorate(icing, function(cake) {
          nextStep(cake);
        });
      });
    });
  });
};
```

---

### 🌐 Axios Request

`axios` paketi `HTTP` isteklerini yönetir ve bir *promise* nesnesi döndürür.

```javascript
const axios = require('axios').default;
const connectToURL=(url)=>{
  const req=axios.get(url);
  console.log(req);
  req.then(resp=>{
  console.log("Fulfilled");
  console.log(resp.data);
  })
  .catch(err=>{
  console.log("Rejected");
  });
}
connectToURL('valid-url')
connectToURL('invalid-url')
```
