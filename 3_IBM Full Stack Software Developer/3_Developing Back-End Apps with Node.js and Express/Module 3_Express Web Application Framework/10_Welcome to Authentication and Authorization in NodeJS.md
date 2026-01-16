## 🔐 Node.js’te Authentication ve Authorization’a Hoş Geldiniz

**Gerekli tahmini süre:** 20 dakika

---

## 🎯 Hedefler

Bu okumada şunları yapabileceksiniz:

* Authentication’ı tanımlamak
* Session-based, token-based ve passwordless authentication’ı açıklamak
* Session-based, token-based ve passwordless dahil olmak üzere farklı authentication türlerini karşılaştırmak ve aralarındaki farkları açıklamak

---

## 🪪 Authentication

Authentication süreci, bir kullanıcının kimliğini, kim olduğunu iddia ettiğini doğrulamak için kimlik bilgilerini ( *credentials* ) doğrulayarak teyit eder. Authentication, yalnızca geçerli kimlik bilgilerine sahip olanların sisteme erişebilmesini garanti ederek bir uygulamanın güvenliğini sağlar. Authentication, bir uygulamanın arka ucunun ( *backend* ) sorumluluğudur.

Node.js’te üç popüler authentication yöntemi şunlardır:

1. Session-based
2. Token-based
3. Passwordless

Bu yöntemlerin her birini biraz açıklayalım ve karşılaştıralım.

---

## 🗝️ Session-based

Session-based authentication, authentication teknolojisinin en eski biçimidir. Tipik olarak bir session akışı şu şekildedir:

1. Kullanıcı, kimlik bilgileriyle giriş yapar.
2. Giriş kimlik bilgileri, bir veritabanındaki kimlik bilgileriyle doğrulanır. Veritabanı, session ID’ye göre hangi kaynaklara erişilebileceğini saklamaktan sorumludur.
3. Sunucu, benzersiz şifrelenmiş bir dize olan bir session ID ile bir session oluşturur. Session ID veritabanında saklanır.
4. Session ID ayrıca tarayıcıda bir çerez ( *cookie* ) olarak saklanır.
5. Kullanıcı çıkış yaptığında veya belirli bir süre geçtiğinde, session ID hem tarayıcıda hem de veritabanında yok edilir.

Aşağıda, bir Express uygulamasında session-based authentication’ı gösteren bir kod parçası yer almaktadır:

```javascript
const express = require('express');
const session = require('express-session');
const app = express();
// Middleware to set up session management
app.use(session({
 secret: 'secret-key', // Replace with a strong secret key
 resave: false, // Whether to save the session data if there were no modifications
 saveUninitialized: true, // Whether to save new but not modified sessions
 cookie: { secure: false } // Set to true in production with HTTPS
}));
// POST endpoint for handling login
app.post('/login', (req, res) => {
 const { username, password } = req.body;
 // Simulated user authentication (replace with actual logic)
 if (username === 'user' && password === 'password') {
 req.session.user = username; // Store user information in session
 res.send('Logged in successfully');
 } else {
 res.send('Invalid credentials');
 }
});
// GET endpoint for accessing dashboard
app.get('/dashboard', (req, res) => {
 if (req.session.user) {
 res.send(`Welcome ${req.session.user}`); // Display welcome message with user's name
 } else {
 res.send('Please log in first');
 }
});
// Start the server on port 3000
app.listen(3000, () => console.log('Server running on port 3000'));
```

**Açıklama:**

* **Express Setup:** Bu kod, bir Express uygulaması kurar ve `express-session` kullanarak session yönetimini yapılandırır.
* **Session Configuration:** `express-session` middleware’i, session verisini şifrelemek için bir gizli anahtar (`secret: 'secret-key'`) ve `resave` ile `saveUninitialized` gibi diğer seçeneklerle yapılandırılır.
* **Login Endpoint (`/login`):** Kullanıcı girişi için **POST** isteklerini yönetir. Sağlanan kullanıcı adı ve parola eşleşirse, kullanıcı adını (`req.session.user`) session içinde saklar.
* **Dashboard Endpoint (`/dashboard`):** Kullanıcının doğrulanmış olup olmadığını kontrol eder (`req.session.user` var mı). Doğrulanmışsa kullanıcıyı karşılar; değilse giriş yapmasını ister.
* **Start the server:** Sunucuyu 3000 portunda başlatır.

---

## 🪙 Token-based

Token-based güvenlik iki parçadan oluşur: authentication ve authorization. Authentication, kimlik bilgilerini sağlayıp kullanıcının kimlik bilgilerini kanıtlayan bir token elde etme sürecidir. Authorization ise, kaynak sunucusunun kullanıcının hangi kaynaklara erişmesi gerektiğini bilmesi için bu token’ı kullanma sürecini ifade eder.

---

## 🧾 Token-based Authentication

Token-based authentication, kullanıcıları doğrulamak için access token’lar kullanır. Bir access token, kullanıcı hakkında bilgi, izinleri, grupları ve sona erme ( *expiration* ) bilgilerini içeren ve bir sunucudan istemciye aktarılan küçük bir kod parçasıdır. Bir ID token, kullanıcının doğrulandığını kanıtlayan bir artefaktır.

Token üç bölüm içerir:  **header** , **payload** ve  **signature** . Header, token türü ve onu oluşturmak için kullanılan algoritma hakkında bilgi içerir. Payload, izinler, gruplar ve sona erme süreleri gibi *claims* olarak adlandırılan kullanıcı özniteliklerini içerir. Signature, token’ın iletim sırasında değişmediğini ifade eden bütünlüğünü ( *integrity* ) doğrular. “jot” diye telaffuz edilen ama JWT olarak yazılan bir JSON web token, JSON formatında şifrelenmiş payload verisi oluşturmak için bir internet standardıdır.

Bir kullanıcının tarayıcısı bir authentication sunucusuna çağrı yapar ve bir web uygulamasına erişim elde eder. Authentication sunucusu daha sonra, istemci tarafından şifrelenmiş bir çerez olarak saklanan bir ID token döndürür. ID token daha sonra, kullanıcının doğrulandığının kanıtı olarak web sunucusundaki uygulamaya iletilir.

---

## 🛡️ Token-based Authorization

Bu akış şeması, authorization süreci boyunca bir token’ın iş akışını gösterir.

Authorization süreci, web uygulaması yetkisiz erişime karşı korunan bir kaynağa, örneğin bir API’ye erişmek istediğinde yürütülür. Kullanıcı, Authorization sunucusuna karşı doğrulanır. Authorization sunucusu bir access token oluşturur (ID token ve access token iki ayrı nesnedir) ve access token’ı istemciye geri gönderir; access token istemcide saklanır. Ardından kullanıcı isteklerde bulunduğunda veya kaynaklara eriştiğinde token, kaynak sunucusuna (API sunucusu olarak da adlandırılır) iletilir. Token her HTTP isteğiyle birlikte gönderilir. Token, kullanıcının izinleriyle ilgili gömülü bilgileri, authorization sunucusundan bu izinleri almaya gerek kalmadan içerir. Token çalınsa bile, saldırgan kullanıcının kimlik bilgilerine erişemez; çünkü token şifrelenmiştir.

Aşağıda, bir Express uygulamasında Token-based Authentication’ı gösteren bir kod parçası yer almaktadır:

```javascript
const express = require('express');
const jwt = require('jsonwebtoken');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.json());
const secretKey = 'your-secret-key'; // Replace with a strong secret key
// POST endpoint for user login and JWT generation
app.post('/login', (req, res) => {
 const { username, password } = req.body;
 // Simulated user authentication
 if (username === 'user' && password === 'password') {
 // Generate JWT with username payload
 const token = jwt.sign({ username }, secretKey, { expiresIn: '1h' });
 res.json({ token }); // Send token as JSON response
 } else {
 res.send('Invalid credentials');
 }
});
// GET endpoint to access protected resource (dashboard)
app.get('/dashboard', (req, res) => {
 // Get token from Authorization header
 const token = req.headers['authorization'];
 if (token) {
 // Verify JWT token
 jwt.verify(token, secretKey, (err, decoded) => {
 if (err) {
 res.send('Invalid token');
 } else {
 // Token is valid, send welcome message with username
 res.send(`Welcome ${decoded.username}`);
 }
 });
 } else {
 res.send('Token missing');
 }
});
// Start server
app.listen(3000, () => console.log('Server running on port 3000'));
```

**Açıklama:**

* **Express Setup:** JSON isteklerini ayrıştırmak için `body-parser` gibi middleware’lerle bir Express uygulamasını yapılandırır.
* **JWT Generation (`/login`):** Kullanıcı girişi için **POST** isteklerini yönetir. Kimlik bilgileri geçerliyse, kullanıcı adını içeren bir JWT üretir (`jwt.sign({ username }, secretKey, { expiresIn: '1h' })`).
* **JWT Verification (`/dashboard`):** Gelen isteklerin Authorization header’ında bir JWT arar (`const token = req.headers['authorization']`). Varsa token’ı doğrular (`jwt.verify(token, secretKey)`) ve erişim vermek için kullanıcı adını (`decoded.username`) çıkarır.

---

## 🔑 Passwordless

Passwordless authentication’ta kullanıcı login kimlik bilgilerine ihtiyaç duymaz; bunun yerine kimliğini kanıtlayan bir faktöre sahip olduğunu göstererek sisteme erişim kazanır. Yaygın faktörler arasında parmak izi gibi biyometrikler, e-posta adreslerine gönderilen bir “magic link” veya mobil cihaza gönderilen tek kullanımlık bir şifre ( *one-time passcode* ) bulunur. Parola kurtarma sistemleri artık yaygın olarak passwordless authentication kullanır.

Passwordless authentication, Public Key ve Private Key şifrelemesi kullanılarak gerçekleştirilir. Bu yöntemde, bir kullanıcı uygulamaya kayıt olduğunda, kullanıcının cihazı yukarıda belirtilen faktörlerden yararlanan bir private key/public key çifti üretir.

Public key, mesajları şifrelemek için kullanılır ve private key, bunların şifresini çözmek için kullanılır. Private key kullanıcının cihazında saklanır ve public key uygulama ile birlikte saklanır ve bir kayıt ( *registration* ) servisine kaydedilir.

Herkes public key’e erişebilir; ancak private key yalnızca istemci tarafından bilinir. Kullanıcı uygulamaya giriş yaptığında, uygulama bir giriş sınaması ( *login challenge* ) üretir; örneğin biyometri isteme, bir “magic link” gönderme veya SMS ile özel bir kod gönderme gibi. Bu sınama public key ile şifrelenir. Private key mesajın şifresinin çözülmesini sağlar. Uygulama daha sonra giriş sınamasını doğrular ve kullanıcıyı yetkilendirmek için yanıtı kabul eder.

Aşağıda, bir Express uygulamasında Passwordless-based Authentication’ı gösteren bir kod parçası yer almaktadır:

```javascript
const express = require('express');
const bodyParser = require('body-parser');
const nodemailer = require('nodemailer');
const app = express();
app.use(bodyParser.json());
const users = {}; // In-memory storage for demo purposes
// Endpoint to request access and send verification code via email
app.post('/request-access', (req, res) => {
 const { email } = req.body;
 // Generate a 6-digit verification code
 const code = Math.floor(100000 + Math.random() * 900000).toString();
 
 // Store the code in memory (users object)
 users[email] = code;
 // Simulated email sending (for demonstration)
 console.log(`Sending code ${code} to ${email}`);
 res.send('Code sent to your email');
});
// Endpoint to verify the received code
app.post('/verify-code', (req, res) => {
 const { email, code } = req.body;
 // Compare the received code with stored code for the email
 if (users[email] === code) {
 // Code matches, access granted
 res.send('Access granted');
 } else {
 // Code does not match, access denied
 res.send('Invalid code');
 }
});
// Start the Express server
app.listen(3000, () => console.log('Server running on port 3000'));
```

**Açıklama:**

* **Express Setup:** JSON isteklerini ayrıştırmak için middleware ile (body-parser) bir Express uygulaması kurar.
* **Request Access (`/request-access`):** Kullanıcıların erişim talep etmek için e-postalarını sağladığı **POST** isteklerini yönetir. 6 haneli bir doğrulama kodu (`code`) üretir ve bellek içi bir nesnede saklar (`users[email] = code`).
* **Verify Code (`/verify-code`):** Alınan kodu saklanan kodla karşılaştırmak için **POST** isteklerini yönetir (`if (users[email] === code)`). Eşleşirse erişim verir; aksi halde reddeder.

---

## 🧾 Özet

Bu okumada şunları öğrendiniz:

Authentication, bir kullanıcının kimliğini, kim olduğunu iddia ettiğini doğrulamak için kimlik bilgilerini kullanarak teyit etme sürecidir.

Session-based authentication, veritabanında ve istemcinin tarayıcısında saklanan bir session ID oluşturmak için kimlik bilgilerini kullanır. Kullanıcı çıkış yaptığında session ID yok edilir. Token-based authentication, çoğunlukla JWT olan access token’ları kullanır; bunlar, iki taraf arasında aktarılan verilerle birlikte sunucu ve istemci arasında iletilir.

Passwordless authentication, parola gereksinimi olmadan istemci ile sunucu arasında aktarılan veriyi şifrelemek ve şifresini çözmek için public/private key çiftlerini kullanır.

---

## 👤 Yazar(lar)

Rajashree Patil
Sapthashree K S
