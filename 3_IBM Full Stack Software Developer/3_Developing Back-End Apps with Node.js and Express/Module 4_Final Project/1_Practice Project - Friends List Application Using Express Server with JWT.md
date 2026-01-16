## 📘 Uygulama Projesi - JWT ile Express Sunucusu Kullanarak Arkadaş Listesi Uygulaması

**Tahmini Gereken Süre:** 1 saat

---

## 🧭 Genel Bakış

CRUD laboratuvarında, Express Sunucusu ile API uç noktaları oluşturarak geçici veriler üzerinde CRUD işlemleri gerçekleştirdiniz. Bu laboratuvarda, bu işlemleri JWT ve oturum (session) kimlik doğrulaması kullanarak yalnızca kimliği doğrulanmış kullanıcılara kısıtlayacaksınız.

Bu laboratuvarda, *friends* nesnesi, anahtar olarak e-posta ve değer olarak *friends object* olacak şekilde bir JSON/sözlük olacaktır.  *friends object* ;  *firstName* ,  *lastName* , *DOB* alanlarının kendi değerlerine eşlendiği bir sözlüktür. Bu nedenle, HTTP isteğindeki *query* ve *params* yerine *body* kullanıyor olacaksınız.

Tüm CRUD işlemlerini yalnızca kimliği doğrulanmış kullanıcılar gerçekleştirebilecektir.

Uç noktaların çıktısını Postman üzerinde test edeceğiz.

---

## 🛠️ Kurulum: Uygulama Oluşturma

1. Düzenleyicideki menüyü kullanarak bir terminal penceresi açın:  **Terminal > New Terminal** .
2. Proje klasörünüzde değilseniz, proje klasörünüze geçin.

```bash
cd /home/project
```

3. Bu laboratuvar için gerekli başlangıç kodunu içeren git deposunu (zaten yoksa) klonlamak için aşağıdaki komutu çalıştırın.

```bash
[ ! -d 'nodejs_PracticeProject_AuthUserMgmt' ] && git clone https://github.com/ibm-developer-skills-network/nodejs_PracticeProject_AuthUserMgmt.git
```

4. Laboratuvara başlamak için *nodejs_PracticeProject_AuthUserMgmt* dizinine geçin.

```bash
cd nodejs_PracticeProject_AuthUserMgmt
```

5. Bu laboratuvarın çıktıları/artefaktlarını görmek için dizin içeriğini listeleyin.

```bash
ls
```

---

## 📦 Sunucu Uygulaması için Gerekli Paketler

1. Bu laboratuvar için gerekli paketler *packages.json* içinde bağımlılıklar olarak aşağıdaki gibi tanımlanmıştır. Dosyayı dosya gezgininde görüntüleyebilirsiniz.

```json
"dependencies": {
 "express": "^4.18.1",
 "express-session": "^1.17.3",
 "nodemon": "^2.0.19",
 "jsonwebtoken": "^8.5.1"
}
```

2. Terminalde aşağıdaki komutu çalıştırarak tüm paketleri yükleyin.

```bash
npm install --save
```

Bu, sunucu uygulamanızın çalışması için gerekli tüm paketleri yükleyecektir.

---

## 🔐 Alıştırma 1: Kullanıcı Kimlik Doğrulama Sürecini Anlama

*index.js* içindeki kodu anlayalım.

1. Bu uygulamanın amacı API uç noktalarına yalnızca kimliği doğrulanmış kullanıcıların erişimini sağlamak olduğundan, kullanıcıları kaydetmenin bir yolunu sağlamanız gerekir. Bu uç nokta, gövde (body) üzerinden kullanıcı adı ve parola kabul eden bir POST isteği olacaktır. Kullanıcının bu uç noktaya erişmek için kimliği doğrulanmış olması gerekmez.

```js
// Register a new user
app.post("/register", (req, res) => {
 const username = req.body.username;
 const password = req.body.password;
 // Check if both username and password are provided
 if (username && password) {
 // Check if the user does not already exist
 if (!doesExist(username)) {
 // Add the new user to the users array
 users.push({"username": username, "password": password});
 return res.status(200).json({message: "User successfully registered. Now you can login"});
 } else {
 return res.status(404).json({message: "User already exists!"});
 }
 }
 // Return error if username or password is missing
 return res.status(404).json({message: "Unable to register user."});
});
```

2. Tekrarlamaları önlemek ve kullanıcı adını benzersiz tutmak için, kullanıcı adının kayıtlı kullanıcılar listesinde mevcut olup olmadığını kontrol edecek bir yöntem sağlamanız gerekir. Bu bir yardımcı (utility) fonksiyondur ve bir uç nokta değildir.

```js
// Check if a user with the given username already exists
const doesExist = (username) => {
 // Filter the users array for any user with the same username
 let userswithsamename = users.filter((user) => {
 return user.username === username;
 });
 // Return true if any user with the same username is found, otherwise false
 if (userswithsamename.length > 0) {
 return true;
 } else {
 return false;
 }
}
```

3. Ardından kullanıcı adı ve parolanın, kayıtlı kullanıcılar listesindeki bilgilerle eşleşip eşleşmediğini kontrol edeceksiniz. Kimlik bilgileri eşleşip eşleşmediğine göre bir boolean döndürür. Bu da bir yardımcı (utility) fonksiyondur ve bir uç nokta değildir.

```js
// Check if the user with the given username and password exists
const authenticatedUser = (username, password) => {
 // Filter the users array for any user with the same username and password
 let validusers = users.filter((user) => {
 return (user.username === username && user.password === password);
 });
 // Return true if any valid user is found, otherwise false
 if (validusers.length > 0) {
 return true;
 } else {
 return false;
 }
}
```

4. Şimdi, istekleri yakalayıp oturumun geçerli olduğundan emin olmak için, kullanıcı tanımlı bir *secret* ile bir session nesnesi oluşturacak ve bunu bir middleware olarak kullanacaksınız.

```js
app.use(session({secret:"fingerpint"},resave=true,saveUninitialized=true));
```

5. Kayıtlı kullanıcıların giriş yapabilmesi için bir uç nokta sağlayacaksınız. Bu uç nokta şunları yapacaktır:

* Kullanıcı adı veya parola sağlanmadıysa hata döndürür.
* Kimlik bilgileri doğruysa, 1 saat (60 X 60 saniye) geçerli bir access token oluşturur ve kullanıcıyı oturum açmış hale getirir.
* Kimlik bilgileri yanlışsa hata fırlatır.

Lütfen bunu not edin; final projede bu kavramı kullanıyor olacaksınız.

```js
// Login endpoint
app.post("/login", (req, res) => {
 const username = req.body.username;
 const password = req.body.password;
 // Check if username or password is missing
 if (!username || !password) {
 return res.status(404).json({ message: "Error logging in" });
 }
 // Authenticate user
 if (authenticatedUser(username, password)) {
 // Generate JWT access token
 let accessToken = jwt.sign({
 data: password
 }, 'access', { expiresIn: 60 * 60 });
 // Store access token and username in session
 req.session.authorization = {
 accessToken, username
 }
 return res.status(200).send("User successfully logged in");
 } else {
 return res.status(208).json({ message: "Invalid Login. Check username and password" });
 }
});
```

6. Şimdi, kimliği doğrulanmış kullanıcılara kısıtlanan tüm işlemlerin middleware tarafından yakalandığından emin olacaksınız. Aşağıdaki kod, */friends* ile başlayan tüm uç noktaların middleware’den geçmesini sağlar. Oturumdan yetkilendirme (authorization) ayrıntılarını alır ve doğrular. Token doğrulanırsa kullanıcı kimliği doğrulanmıştır ve kontrol bir sonraki uç nokta işleyicisine aktarılır. Token geçersizse kullanıcı kimliği doğrulanmamıştır ve hata mesajı döndürülür.

```js
// Middleware to authenticate requests to "/friends" endpoint
app.use("/friends", function auth(req, res, next) {
 // Check if user is logged in and has valid access token
 if (req.session.authorization) {
 let token = req.session.authorization['accessToken'];
 // Verify JWT token
 jwt.verify(token, "access", (err, user) => {
 if (!err) {
 req.user = user;
 next(); // Proceed to the next middleware
 } else {
 return res.status(403).json({ message: "User not authenticated" });
 }
 });
 } else {
 return res.status(403).json({ message: "User not logged in" });
 }
});
```

---

## 🧩 Kodu Görüntülemek için Tıklayın

```js
const express = require('express');
const jwt = require('jsonwebtoken');
const session = require('express-session')
const routes = require('./router/friends.js')
let users = []
// Check if a user with the given username already exists
const doesExist = (username) => {
 // Filter the users array for any user with the same username
 let userswithsamename = users.filter((user) => {
 return user.username === username;
 });
 // Return true if any user with the same username is found, otherwise false
 if (userswithsamename.length > 0) {
 return true;
 } else {
 return false;
 }
}
// Check if the user with the given username and password exists
const authenticatedUser = (username, password) => {
 // Filter the users array for any user with the same username and password
 let validusers = users.filter((user) => {
 return (user.username === username && user.password === password);
 });
 // Return true if any valid user is found, otherwise false
 if (validusers.length > 0) {
 return true;
 } else {
 return false;
 }
}
const app = express();
app.use(session({secret:"fingerpint"},resave=true,saveUninitialized=true));
app.use(express.json());
// Middleware to authenticate requests to "/friends" endpoint
app.use("/friends", function auth(req, res, next) {
 // Check if user is logged in and has valid access token
 if (req.session.authorization) {
 let token = req.session.authorization['accessToken'];
 // Verify JWT token
 jwt.verify(token, "access", (err, user) => {
 if (!err) {
 req.user = user;
 next(); // Proceed to the next middleware
 } else {
 return res.status(403).json({ message: "User not authenticated" });
 }
 });
 } else {
 return res.status(403).json({ message: "User not logged in" });
 }
});
// Login endpoint
app.post("/login", (req, res) => {
 const username = req.body.username;
 const password = req.body.password;
 // Check if username or password is missing
 if (!username || !password) {
 return res.status(404).json({ message: "Error logging in" });
 }
 // Authenticate user
 if (authenticatedUser(username, password)) {
 // Generate JWT access token
 let accessToken = jwt.sign({
 data: password
 }, 'access', { expiresIn: 60 * 60 });
 // Store access token and username in session
 req.session.authorization = {
 accessToken, username
 }
 return res.status(200).send("User successfully logged in");
 } else {
 return res.status(208).json({ message: "Invalid Login. Check username and password" });
 }
});
// Register a new user
app.post("/register", (req, res) => {
 const username = req.body.username;
 const password = req.body.password;
 // Check if both username and password are provided
 if (username && password) {
 // Check if the user does not already exist
 if (!doesExist(username)) {
 // Add the new user to the users array
 users.push({"username": username, "password": password});
 return res.status(200).json({message: "User successfully registered. Now you can login"});
 } else {
 return res.status(404).json({message: "User already exists!"});
 }
 }
 // Return error if username or password is missing
 return res.status(404).json({message: "Unable to register user."});
});
const PORT =5000;
app.use("/friends", routes);
app.listen(PORT,()=>console.log("Server is running"));
```

5000 portunda çalışacak şekilde yapılandırılmış bir express sunucunuz var. Sunucuya */friends* ile eriştiğinizde, *routes/friends.js* içinde tanımlı uç noktalara erişebilirsiniz. Ancak bunu yapmak için, */register* uç noktasında yeni bir kullanıcı olarak kayıt olmanız ve */login* uç noktasında bu kimlik bilgileriyle giriş yapmanız gerekir.

**Not:** Şimdi, gerekli kodları ekleyerek arkadaş ekleme, düzenleme ve silme için çeşitli CRUD işlemlerini uygulayacak ve ardından çıktıyı Postman üzerinde test edeceksiniz.

---

## 🟢 Alıştırma 2: GET Metodunu Uygulama

*router* dizini altındaki *friends.js* dosyasına gidin; içindeki uç noktaların iskelet halinde tanımlandığını ve get metodunu uygulamanız gerektiğini göreceksiniz.

1. *router/friends.js* dosyasında, *router.get("/",(req,res)=>{}* içinde verilen boşlukta, JSON string kullanarak tüm kullanıcı bilgisini almak için kodu yazın.
   **İpucu:** Module 3’teki CRUD laboratuvarında Alıştırma 2’ye bakın.

**Çözümü görüntülemek için tıklayın**

```js
router.get("/",(req,res)=>{
 // Send JSON response with formatted friends data
 res.send(JSON.stringify(friends,null,4));
});
```

---

## 🔎 Alıştırma 3: Belirli E-posta için GET Metodunu Uygulama

1. *router.get("/:email",(req,res)=>{}* içine, *filter* metodu kullanmadan e-postaya göre kullanıcıyı görüntülemek için kodu yazın.
   **İpucu:** CRUD laboratuvarında Alıştırma 3’e bakın.

**Çözümü görüntülemek için tıklayın**

```js
router.get('/:email', function(req, res) {
 // Retrieve the email parameter from the request URL and send the corresponding friend's details
 const email = req.params.email;
 res.send(friends[email]);
});
```

---

## ➕ Alıştırma 4: POST Metodunu Uygulama

1. Yeni kullanıcıyı JSON/sözlüğe eklemek için aşağıdaki kodu *router.post("/",(req,res)=>{}* içine yapıştırın. Ayrıca belirtilen yerlerdeki kodları güncelleyin.

```js
router.post("/", function(req, res) {
 // Check if email is provided in the request body
 if (req.body.email) {
 // Create or update friend's details based on provided email
 friends[req.body.email] = {
 "firstName": req.body.firstName,
 // Add similarly for lastName
 // Add similarly for DOB
 };
 }
 // Send response indicating user addition
 res.send("The user" + (' ') + (req.body.firstName) + " Has been added!");
});
```

---

## ♻️ Alıştırma 5: PUT Metodunu Uygulama

1. Arkadaş bilgilerini değiştirmek için aşağıdaki kodu *router.put("/:email", (req, res) => {}* içine yapıştırın. Ayrıca belirtilen yerlerde kod ekleyin.

```js
router.put("/:email", function(req, res) {
 // Extract email parameter from request URL
 const email = req.params.email;
 let friend = friends[email]; // Retrieve friend object associated with email
 if (friend) { // Check if friend exists
 let DOB = req.body.DOB;
 // Add similarly for firstName
 // Add similarly for lastName
 // Update DOB if provided in request body
 if (DOB) {
 friend["DOB"] = DOB;
 }
 // Add similarly for firstName
 // Add similarly for lastName
 friends[email] = friend; // Update friend details in 'friends' object
 res.send(`Friend with the email ${email} updated.`);
 } else {
 // Respond if friend with specified email is not found
 res.send("Unable to find friend!");
 }
});
```

---

## 🗑️ Alıştırma 6: DELETE Metodunu Uygulama

1. E-postaya göre arkadaş bilgisini silmek için aşağıdaki kodu *router.delete("/:email", (req, res) => {}* içine yapıştırın.
   **İpucu:** CRUD laboratuvarında Alıştırma 6’ya bakın.

**Kodu görüntülemek için buraya tıklayın**

```js
router.delete("/:email", (req, res) => {
 // Extract email parameter from request URL
 const email = req.params.email;
 if (email) {
 // Delete friend from 'friends' object based on provided email
 delete friends[email];
 }
 
 // Send response confirming deletion of friend
 res.send(`Friend with the email ${email} deleted.`);
});
```

---

## ▶️ Çıktıyı Görmek için Sunucuyu Çalıştırma

1. Terminalde */home/projects/nodejs_PracticeProject_AuthUserMgmtdirectory* içinde olduğunuzdan emin olun.
2. Sunucuyu çalıştırmak için gerekli tüm paketleri yükleyin.

```bash
npm install
```

3. Express sunucusunu başlatın.

```bash
npm start
```

---

## 🧪 Alıştırma 7: Kullanıcı Kaydı, Giriş ve Postman ile Uç Noktaları Test Etme

Postman’a gidin ve yeni bir HTTP istek penceresi açın (Hands-on Lab - CRUD operations with Node.js’de yaptığınız gibi).

### 👤 Kullanıcı Kaydı

1. Aşağıdaki JSON parametrelerini isteğin *body* kısmında kullanarak uç noktaya bir POST isteği gönderin:
   https://-5000.theianext-1-labs-prod-misc-tools-us-east￾0.proxy.cognitiveclass.ai/register
   **Body** >> **raw** >> **JSON** seçin ve parametreleri gönderin.

```json
{"username":"user2", "password":"password2"}
```

**Not:** “user2” ve “password2” referans amaçlıdır. İstediğiniz herhangi bir kullanıcı adı ve parola kullanabilirsiniz.

2. Şu çıktıyı döndürmelidir: `{"message": "User successfully registered. Now you can login"}`.

### 🔑 Kullanıcı Girişi

1. Aşağıdaki uç noktaya POST isteği gönderin:
   https://-5000.theianext-1-labs-prod-misc-tools-us-east-0.proxy.cognitiveclass.ai/login
   İsteğin *body* kısmında aynı JSON formatında yukarıdaki kullanıcı adı ve parolayı kullanın.
2. Şu çıktıyı döndürmelidir: `User successfully logged in.`

---

## 🧾 Postman’da Uç Noktaları Test Etme

Aşağıdakiler, Hands-on Lab - CRUD operations with Node.js’de yaptıklarınıza benzerdir:

1. *friends* uç noktasına bir GET isteği gönderin:
   https://-5000.theianext-1-labs-prod-misc-tools-us-east￾0.proxy.cognitiveclass.ai/friends
   Kodda eklenmiş tüm arkadaşları gördüğünüzden emin olun.
2. Şu uç noktaya GET isteği gönderin:
   https://-5000.theianext-1-labs-prod-misc-tools-us-east￾0.proxy.cognitiveclass.ai/friends/
   Belirli arkadaşın detaylarının döndüğünden emin olun.
   Kullanıcı *[johnsmith@gamil.com](mailto:johnsmith@gamil.com)* için şu olacaktır:
   ‘[johnsmith@gamil.com](mailto:johnsmith@gamil.com)'" target="_blank" rel="noopener noreferrer"">[https://XXXXXXXXXX-5000.theiadocker-0-labs￾prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/user/johnsmith@gamil.com](https://xxxxxxxxxx-5000.theiadocker-0-labs%EF%BF%BEprod-theiak8s-4-tor01.proxy.cognitiveclass.ai/user/johnsmith@gamil.com)'
3. Aşağıdaki formatta istek gövdesini kullanarak şu uç noktaya POST isteği ile yeni bir arkadaş ekleyin:
   https://-5000.theianext-1-labs-prod-misc-tools-us-east￾0.proxy.cognitiveclass.ai/friends/

```json
{"email":"andysmith@gamil.com","firstName":"Andy","lastName":"Smith","DOB":"1/1/1987"}
```

Yukarıdaki, *[andysmith@gamil.com](mailto:andysmith@gamil.com)* e-postalı yeni bir kullanıcı eklemek için bir referanstır.

**Not:** Burada yapıldığı gibi (gamil.com) kurgusal/mevcut olmayan e-posta alan adları kullandığınızdan emin olun.  *gmail.com* , *yahoo.com* gibi gerçek e-posta alan adlarını kullanmaktan kaçının.

4. Şu uç noktaya PUT isteği göndererek bir arkadaş özniteliğini ( *firstName* ,  *lastName* ,  *DOB* ) güncelleyin:
   https://-5000.theianext-1-labs-prod-misc￾tools-us-east-0.proxy.cognitiveclass.ai/friends/
   Aşağıdaki formatta istek gövdesini kullanarak *DOB* değerini 1/1/1989 olarak güncelleyin ve aynı şekilde  *firstName* , *lastName* güncellemesi yapın.

```json
{"DOB":"1/1/1989"}
```

5. Şu uç noktaya DELETE isteği göndererek bir arkadaşı silin:
   https://-5000.theianext-1-labs-prod-misc-tools-us-east￾0.proxy.cognitiveclass.ai/friends/.

---

## ⏱️ Access Token Geçerliliğini Değiştirme

1. Daha önce *index.js* dosyasında gördüğümüz access token geçerlilik kod parçacığını aşağıda inceleyin.

```js
 if (authenticatedUser(username, password)) {
 // Generate JWT access token
 let accessToken = jwt.sign({
 data: password
 }, 'access', { expiresIn: 60 * 60 });
 // Store access token and username in session
 req.session.authorization = {
 accessToken, username
 }
 return res.status(200).send("User successfully logged in");
 } else {
 return res.status(208).json({ message: "Invalid Login. Check username and password" });
 }
});
```

2. Şimdi geçerliliği kontrol etmek için *expiresIn* özniteliğini 60 saniye olarak düzenleyin:

**Kodu görüntülemek için buraya tıklayın**

```js
 if (authenticatedUser(username, password)) {
 // Generate JWT access token
 let accessToken = jwt.sign({
 data: password
 }, 'access', { expiresIn: 60 });
 // Store access token and username in session
```

3. Değişiklikleri doğrulamak için Postman’da Kullanıcı Kaydı ve Kullanıcı Girişi adımlarını tekrar edin.
   Access token oluşturulduktan sonra 60 saniye içinde */friends* uç noktasına istek yaparsanız kimliğiniz doğrulanır. Aksi halde, erişim kazanmak için tekrar giriş yapmanız gerektiğini belirten aşağıdaki mesajı alırsınız:

`{message: "User not authenticated"}.`

CRUD işlemlerini Session ve JWT kimlik doğrulaması kullanarak Express sunucusunda gerçekleştirme ve bunları Postman ile test etme uygulama projesini tamamladınız. Tebrikler!

---

## 🧾 Özet

Bu laboratuvarda, verilen kullanıcı detayları üzerinde Express sunucusunda Session ve JWT kimlik doğrulaması kullanarak CRUD işlemleri gerçekleştirdik ve Postman kullanarak test ettik.

---

## 👩‍💻 Yazar(lar)

Lavanya T S
Sapthashree K S
K Sundararajan

© IBM Corporation. Tüm hakları saklıdır.
