## 🧪 Uygulamalı Laboratuvar - Promise Callback (10 dk)

### 🎯 Alıştırmanın Amacı

Bu laboratuvarı tamamladıktan sonra şunları yapabileceksiniz:

* *Promise callback* ’lerini açıklamak
* *Promise* ’lerle bir Node.js uygulaması oluşturmak

---

### 📌 Ön Koşullar

* JavaScript hakkında temel bilgi

---

## 📝 Görev 1: Promise ile bir betik oluşturma ve çalıştırma

1. Düzenleyicideki menüyü kullanarak bir terminal penceresi açın: `Terminal > New Terminal`.
2. Proje klasörünüze geçin.

```bash
cd /home/project
```

3. Aşağıdaki komutu çalıştırarak yeni bir dosya oluşturun.

```bash
touch promisescript.js
```

5. Dosyanın oluşturulup oluşturulmadığını görmek için geçerli dizindeki dosyaları listeleyin.

```bash
ls
```

6. `promisescript.js` dosyasını açın ve düzenleyin.
   `promisescript.js` dosyasını IDE’de açın.
7. Aşağıdaki kodu dosyaya yapıştırın ve kaydedin. Konsol log’larının hangi sırayla yürütüleceğini tahmin etmek için dosyaya bakabiliyor musunuz?

```javascript
//Creating a promise method. The promise will get resolved when timer times out after 6 seconds.
let myPromise = new Promise((resolve,reject) => {
 setTimeout(() => {
 resolve("Promise resolved")
 },6000)})
//Console log before calling the promise
console.log("Before calling promise");
//Call the promise and wait for it to be resolved and then print a message.
myPromise.then((successMessage) => {
 console.log("From Callback " + successMessage)
 })
//Console log after calling the promise
 console.log("After calling promise");
```

Yukarıdaki kod, 6 saniye sonra `Promise resolved` mesajıyla çözümlenen ( *resolved* ) bir *promise* (`myPromise`) oluşturur.

Betik önce konsola `Before calling promise` yazar.

Ardından  *promise* ’in çözülmesini ele almak için `then` metodunu ayarlar, ancak callback henüz çalışmaz.

Bunun hemen ardından betik konsola `After calling promise` yazar.

6 saniye sonra *promise* çözülür ve callback konsola `From Callback Promise resolved` yazar.

8. Tahmininizi doğrulamak için terminale gidin ve dosyayı çalıştırın.

```bash
node promisescript.js
```

9. Konsol log’larının yürütülme sırası, *promise* çağrısından sonraki ifadelerin art arda çalıştırıldığını ve bu sırada  *promise* ’in eş zamanlı olarak çözümlendiğini ( *resolved* ) veya reddedildiğini ( *rejected* ) gösterir.

---

## 🧩 Alıştırma: İki promise ile bir betik oluşturma ve çalıştırma

1. İki metodu olan ve *promise* döndüren bir betik oluşturun —  *promise* ’lerden biri 6 saniyelik zaman aşımından sonra çözümlenmeli, diğeri ise 3 saniyelik zaman aşımından sonra çözümlenmelidir.  *Promise* ’leri öyle çağırın ki ikinci  *promise* , birinci *promise* çözümlendikten sonra çağrılsın.

**Kodu görüntülemek için buraya tıklayın**

```javascript
let myPromise1 = new Promise((resolve,reject) => {
 setTimeout(() => {
 resolve("Promise 1 resolved")
 },6000)})
let myPromise2 = new Promise((resolve,reject) => {
 setTimeout(() => {
 resolve("Promise 2 resolved")
 },3000)})
 myPromise1.then((successMessage) => {
 console.log("From Callback " + successMessage)
 myPromise2.then((successMessage) => {
 console.log("From Callback " + successMessage)
 })
 })
```

2. Kodu,  *promise* ’leri sıralı olarak çağıracak şekilde değiştirin ve çıktının nasıl değiştiğini görün.

**Kodu görüntülemek için buraya tıklayın**

```javascript
let myPromise1 = new Promise((resolve,reject) => {
 setTimeout(() => {
 resolve("Promise 1 resolved")
 },6000)})
let myPromise2 = new Promise((resolve,reject) => {
 setTimeout(() => {
 resolve("Promise 2 resolved")
 },3000)})
 myPromise1.then((successMessage) => {
 console.log("From Callback " + successMessage)
 })
 myPromise2.then((successMessage) => {
 console.log("From Callback " + successMessage)
})
```

---

## ✅ Tebrikler!

*Promise-Callback* laboratuvarını tamamladınız.

---

## 🧾 Özet

Bu laboratuvarda,  *promise* ’leri callback’lerle iki farklı şekilde kullanmayı öğrendiniz:

* Birinci çözümlendikten sonra ikinci  *promise* ’i nasıl çağıracağınızı.
* *Promise* ’leri sıralı olarak nasıl çağıracağınızı.

Sonraki adımda, bu yöntemleri kullanarak sunucu tarafı yeteneklerini nasıl iyileştireceğinizi öğreneceksiniz.

---

## 👤 Yazar(lar)

Lavanya

© IBM Corporation. Tüm hakları saklıdır.
