## 🧪 Uygulamalı Laboratuvar - Node.js ile CRUD İşlemleri

**Tahmini Gerekli Süre:** 1 saat

Bu laboratuvarda, Express sunucusu kullanarak bir **Arkadaş listesi** oluşturmayı öğreneceksiniz. Uygulamanızın aşağıdaki ayrıntılarla bir arkadaş eklemenize izin vermesi gerekir:  **Ad** ,  **Soyad** , **E-posta** ve  **Doğum tarihi** . Ayrıca uygulamaya, ayrıntıları  **alma** , **değiştirme** ve **silme** yeteneği de sağlayacaksınız.

Yukarıdaki veriler üzerinde Express sunucusu kullanarak  **Create** ,  **Retrieve** , **Update** ve **Delete** işlemlerini gerçekleştirmek için API endpoint’lerine sahip bir uygulama oluşturacaksınız.

Ayrıca endpoint’lere **kimliği doğrulanmış erişim** sağlamayı öğreneceksiniz. Uygulanan endpoint’leri test etmek için **cURL** ve **Postman** kullanacaksınız.

---

## 🎯 Hedefler

* Express sunucusu ile geçici ( *transient* ) veri üzerinde Create, Retrieve, Update ve Delete işlemlerini gerçekleştirmek için API endpoint’leri oluşturmak.
* Yetkili erişim için JSON Web Tokens (JWT) kullanarak oturum ( *session* ) seviyesinde authentication uygulamak.

---

## 🛠️ Kurulum: Uygulama Oluşturma

1. Editördeki menüyü kullanarak bir terminal penceresi açın:  **Terminal > New Terminal** .
2. Zaten proje klasöründe değilseniz, proje klasörünüze geçin.

```bash
cd /home/project
```

3. Eğer zaten yoksa, bu laboratuvar için gereken başlangıç kodunu içeren git deposunu klonlamak için aşağıdaki komutu çalıştırın.

```bash
[ ! -d 'mxpfu-nodejsLabs' ] && git clone https://github.com/ibm-developer-skills-network/mxpfu-nodejsLabs.git
```

5. Laboratuvarda çalışmaya başlamak için `mxpfu-nodejsLabs` dizinine geçin.

```bash
cd mxpfu-nodejsLabs/
```

6. Bu laboratuvarın çıktılarını görmek için bu dizinin içeriğini listeleyin.

```bash
ls
```

---

## 🧩 Alıştırma 1: Sunucu Uygulamasını Anlama

1. Files Explorer’da `mxpfu-nodejsLabs` klasörünü açın ve `index.js` dosyasını görüntüleyin.
   5000 portunda çalışacak şekilde yapılandırılmış bir Express sunucunuz var. Sunucuya `/user` ile eriştiğinizde, `routes/users.js` içinde tanımlanan endpoint’lere erişebilirsiniz.
   GET, POST, PUT ve DELETE’nin CRUD işlemlerini gerçekleştirmek için yaygın kullanılan HTTP yöntemleri olduğunu hatırlayın. Bu işlemler sunucuya veri alır ve gönderir.

   * **GET** , belirtilen bir kaynaktan veri istemek için kullanılır.
   * **POST** , bir kaynak oluşturmak üzere sunucuya veri göndermek için kullanılır.
   * **PUT** , bir kaynağı güncellemek için sunucuya veri göndermek için kullanılır.
   * **DELETE** , belirtilen bir kaynağı silmek için kullanılır.
   * **POST** ve **PUT** bazen birbirinin yerine kullanılır.
2. Bu laboratuvarın kurulması gereken bazı paketleri vardır. Express sunucusunu başlatmak ve çalıştırmak için `express` ve `nodemon` paketi ve oturum tabanlı authentication için `jsonwebtoken` ve `express-session`.

   * `express` - API endpoint’lerini sunmak için bir sunucu oluşturmak içindir.
   * `nodemon` - Koda herhangi bir değişiklik yaptığınızda sunucuyu yeniden başlatmaya yardımcı olur.
   * `jsonwebtoken` - Authentication için kullanacağımız JSON web token üretmeye yardımcı olur. JSON web token (JWT), internet üzerinden iki taraf arasında bilgiyi güvenli biçimde iletmek için kullanılan bir JSON nesnesidir. Bilgi alışverişi için kullanılabilir ve genellikle authentication sistemlerinde kullanılır.
   * `express-session` - Oturum için authentication’ı sürdürmemize yardımcı olur.

   Bu paketler `packages.json` içinde dependency olarak tanımlanmıştır.

```json
"dependencies": {
 "express": "^4.18.1",
 "express-session": "^1.17.3",
 "jsonwebtoken": "^8.5.1",
 "nodemon": "^2.0.19"
}
```

3. Express uygulamasının, isteği bir json nesnesi olarak ele almak için `express.json()` middleware’ini kullandığını gözlemleyin.

```javascript
app.use(express.json());
```

4. Express uygulamasının `/user` ile başlayan endpoint’leri ele almak için route’ları kullandığını gözlemleyin. Bu, `/user` ile başlayan tüm endpoint’ler için sunucunun `users.js` içinde bir endpoint handler arayacağı anlamına gelir.

```javascript
app.use("/user", routes);
```

5. Tüm endpoint’lerin `users.js` içinde iskelet, ancak çalışan bir implementasyona sahip olduğunu gözlemleyin. `routes` dizini altındaki `users.js` dosyasına gidin ve içindeki endpoint’leri inceleyin.

---

## ▶️ Alıştırma 2: Sunucuyu Çalıştırma

Verilen başlangıç kodu, sahte ( *dummy* ) dönüş değerleriyle çalışan bir sunucudur. Gerçek endpoint’leri uygulamaya başlamadan önce sunucuyu çalıştırın.

1. Terminalde, `/home/projects/mxpfu-nodejsLabs` içinde olduğunuzdan emin olmak için çalışma dizinini yazdırın.

```bash
pwd
```

2. Sunucuyu çalıştırmak için gereken tüm paketleri yükleyin. Aşağıdaki komutu kopyalayın, yapıştırın ve çalıştırın.

```bash
npm install
```

Bu, `packages.json` içinde tanımlanan tüm gerekli paketleri yükleyecektir.

3. Express sunucusunu başlatın.

```bash
npm start
```

4. Üst menüden **New Terminal** açın. Bu kullanıcıları almak için bir endpoint test edin. Bu henüz kullanıcıları döndürecek şekilde uygulanmamıştır.

```bash
curl localhost:5000/user
```

5. Yukarıda gösterildiği gibi bir çıktı görüyorsanız, bu sunucunun beklendiği gibi çalıştığı anlamına gelir.

---

## 🧱 Alıştırma 2: Endpoint’lerinizi Uygulama

1. `routes` klasöründeki `users.js` dosyasına gidin. Endpoint’ler tanımlanmıştır ve endpoint’leri uygulamanız için size yer sağlanmıştır.
2. CRUD içinde R, *retrieve* anlamına gelir. Önce, tüm kullanıcıların ayrıntılarını almak için `get` metodunu kullanan bir API endpoint’i ekleyeceksiniz. Başlangıç koduna birkaç kullanıcı eklenmiştir.
   Aşağıdaki kodu kopyalayıp `users.js` içinde `router.get("/",(req,res)=>{} )` metodunun `{ }` parantezleri içine yapıştırın.

```javascript
res.send(users);
```

3. Sunucunuzun çalıştığından emin olun. Koda değişiklik yaptıkça, önceki görevde başlattığınız sunucu yeniden başlatılmalıdır. Sunucu çalışmıyorsa, tekrar başlatın.

```bash
npm start
```

3. Soldaki **Skills Network** düğmesine tıklayın. Bu, “Skills Network Toolbox”ı açacaktır. Ardından  **OTHER** ’a ve sonra  **Launch Application** ’a tıklayın. Buradan portu **5000** olarak girip geliştirme sunucusunu başlatabilmelisiniz.
4. Tarayıcı sayfası açıldığında, adres çubuğundaki URL’nin sonuna `/user` ekleyin. Aşağıdaki sayfayı göreceksiniz.
5. GET isteğinin çıktısını, önceki alıştırmada yaptığınız gibi `curl` komutunu kullanarak kontrol edin.

```bash
curl localhost:5000/user/
```

---

## 📧 Alıştırma 3: Belirli Bir E-posta ile GET Metodu Oluşturma

1. `filter` metodunu kullanıcı koleksiyonu üzerinde kullanarak, e-posta ID’sine göre belirli bir kullanıcının ayrıntılarını almak için bir `get` metodu uygulayın. Kodu yazıp kaydettiğinizde sunucu yeniden başlayacaktır.

**Kodu görmek için buraya tıklayın**

```javascript
router.get("/:email",(req,res)=>{
 // İstek URL’sinden email parametresini çıkar
 const email = req.params.email;
 // Çıkarılan email parametresiyle eşleşen email’e sahip kullanıcıları bulmak için users dizisini filtrele
 let filtered_users = users.filter((user) => user.email === email);
 // filtered_users dizisini istemciye yanıt olarak gönder
 res.send(filtered_users);
});
```

2. **Terminal > New Terminal** seçeneğine tıklayın.
3. Yeni terminalde, mail id’si `johnsmith@gamil.com` olan kullanıcının çıktısını görmek için aşağıdaki komutu kullanın.

```bash
curl localhost:5000/user/johnsmith@gamil.com
```

---

## ➕ Alıştırma 4: POST Metodu Oluşturma

1. CRUD içinde C, *Create* anlamına gelir. Bir kullanıcı oluşturmak ve kullanıcıyı listeye eklemek için `/user` endpoint’ini POST metodu ile uygulayın. Kullanıcı nesnesini bir sözlük ( *dictionary* ) olarak oluşturabilirsiniz. Aşağıda gösterilen örnek kullanıcı nesnesini kullanabilirsiniz.

```json
{
 "firstName":"Jon",
 "lastName":"Lovato",
 "email":"jonlovato@theworld.com",
 "DOB":"10/10/1995"
}
```

Sözlüğü kullanıcı listesine eklemek için `push` kullanın. Kullanıcı ayrıntıları, `firstName`, `lastName`, `DOB` ve `email` adlı query parametreleri olarak geçirilebilir.

**İpucu:** Query parametreleri request nesnesinden `request.query.paramname` kullanılarak alınabilir.

**Kodu görmek için buraya tıklayın**

```javascript
router.post("/",(req,res)=>{
 // İstekten gelen query parametrelerine göre users dizisine yeni bir kullanıcı nesnesi ekle
 users.push({
 "firstName": req.query.firstName,
 "lastName": req.query.lastName,
 "email": req.query.email,
 "DOB": req.query.DOB
 });
 // Kullanıcının eklendiğini belirten bir başarı mesajını yanıt olarak gönder
 res.send("The user " + req.query.firstName + " has been added!");
});
```

2. Yeni terminalde, mail id’si `jonlovato@theworld.com` olan yeni bir kullanıcı göndermek için aşağıdaki komutu kullanın:

```bash
curl --request POST 'localhost:5000/user?firstName=Jon&lastName=Lovato&email=jonlovato@theworld.com&DOB=10/10/1995'
```

3. Çıktı aşağıdaki gibi olacaktır:
4. `jonlovato@theworld.com` e-postalı kullanıcının eklenip eklenmediğini doğrulamak için aşağıdaki gibi bir GET isteği gönderebilirsiniz:

```bash
curl localhost:5000/user/jonlovato@theworld.com
```

---

## ♻️ Alıştırma 5: PUT Metodu Oluşturma

1. CRUD içinde U, update anlamına gelir ve PUT metodu ile gerçekleştirilebilir. Veride güncelleme yapmak için PUT metodunu kullanacaksınız. Önce belirtilen email id’sine sahip kullanıcıya bakmalı, sonra onu değiştirmelisiniz. Aşağıdaki kod, bir kullanıcının doğum tarihinin (DOB) nasıl değiştirilebileceğini gösterir. Diğer özniteliklerde değişikliklere izin vermek için gerekli kod değişikliklerini yapın.

```javascript
router.put("/:email", (req, res) => {
 // Email parametresini çıkar ve eşleşen email’e sahip kullanıcıları bul
 const email = req.params.email;
 let filtered_users = users.filter((user) => user.email === email);
 
 if (filtered_users.length > 0) {
 // İlk eşleşen kullanıcıyı seç ve sağlanmışsa öznitelikleri güncelle
 let filtered_user = filtered_users[0];
 
 // Sağlanmışsa DOB’yi çıkar ve güncelle
 
 let DOB = req.query.DOB; 
 if (DOB) {
 filtered_user.DOB = DOB;
 }
 
 /*
 Gerekirse diğer öznitelikleri güncellemek için buraya benzer kod ekleyin
 */
 
 // Eski kullanıcı girişini güncellenmiş kullanıcıyla değiştir
 users = users.filter((user) => user.email != email);
 users.push(filtered_user);
 
 // Kullanıcının güncellendiğini belirten başarı mesajı gönder
 res.send(`User with the email ${email} updated.`);
 } else {
 // Kullanıcı bulunamazsa hata mesajı gönder
 res.send("Unable to find user!");
 }
});
```

2. Tamamlanmış kod aşağıdaki gibi görünecektir.
3. Bölünmüş terminalde, mail id’si `johnsmith@gamil.com` olan kullanıcı için DOB’yi `1/1/1971` olarak güncellemek üzere aşağıdaki komutu kullanın:

```bash
curl --request PUT 'localhost:5000/user/johnsmith@gamil.com?DOB=1/1/1971'
```

4. Çıktı aşağıdaki gibi olacaktır:
5. `johnsmith@gamil.com` e-postalı kullanıcının DOB’sinin güncellenip güncellenmediğini doğrulamak için aşağıdaki gibi bir GET isteği gönderebilirsiniz:

```bash
curl localhost:5000/user/johnsmith@gamil.com
```

---

## 🗑️ Alıştırma 6: DELETE Metodu Oluşturma

1. CRUD içinde “D”, *Delete* anlamına gelir. Belirli bir kullanıcının email’ini silmek için DELETE metodunu aşağıdaki kodla uygulayın:

```javascript
router.delete("/:email", (req, res) => {
 // İstek URL’sinden email parametresini çıkar
 const email = req.params.email;
 // Belirtilen email’e sahip kullanıcıyı hariç tutacak şekilde users dizisini filtrele
 users = users.filter((user) => user.email != email);
 // Kullanıcının silindiğini belirten başarı mesajını yanıt olarak gönder
 res.send(`User with the email ${email} deleted.`);
});
```

2. Tamamlanmış kod aşağıdaki gibi görünecektir.
3. Bölünmüş terminalde, mail id’si `johnsmith@gamil.com` olan kullanıcıyı silmek için aşağıdaki komutu kullanın:

```bash
curl --request DELETE 'localhost:5000/user/johnsmith@gamil.com'
```

4. Çıktı aşağıdaki gibi olacaktır:
5. `johnsmith@gamil.com` e-postalı kullanıcı için bir GET isteği gönderin ve null bir nesne döndürüldüğünden emin olun:

---

## 🧾 İsteğe Bağlı Alıştırma: Çıktıyı Biçimlendirme

1. Çıktıyı daha okunabilir yapmak için, aşağıdaki gibi JSON stringify metodunu kullanabilirsiniz. GET metodu için kodu şu şekilde güncelleyin:

```javascript
// "/" kök path’i için GET isteklerine yönelik bir route handler tanımla
router.get("/",(req,res)=>{
 // Okunabilirlik için 4 boşluk girintili biçimde users dizisini içeren bir JSON yanıtı gönder
 res.send(JSON.stringify({users}, null, 4));
});
```

2. Uygulamayı 5000 portunda başlatın ve URL’nin sonuna `user` ekleyin.
3. Bu, aşağıda gösterilen güncellenmiş GET metoduna göre GET metodunun çıktısını bir JSON string olarak render edecektir:

---

## 🔐 Alıştırma 7: Authentication Uygulama

Bu endpoint’lerin tamamına herkes erişebilir. Şimdi CRUD işlemlerine authentication eklemeyi göreceksiniz. Bu kod `index_withauth.js` dosyasında uygulanmıştır.

1. `index_withauth.js` içinde aşağıdaki kod bloğunu gözlemleyin.

```javascript
app.use(session({secret:"fingerprint",resave: true, saveUninitialized: true}))
```

Bu, express uygulamanıza session middleware’ini kullanmasını söyler.

* `secret` - bir oturumu doğrulamak için kullanılan rastgele benzersiz bir string anahtar.
* `resave` - Boolean bir değer alır. İstek sırasında session hiç değiştirilmemiş olsa bile session’ın tekrar session store’a yazılmasını sağlar.
* `saveUninitialized` - herhangi bir başlatılmamış session’ın store’a gönderilmesini sağlar. Bir session oluşturulduğunda ancak değiştirilmediğinde, buna *uninitialized* denir.

`resave` ve `saveUninitialized` için varsayılan değer her ikisi için de true’dur, ancak varsayılan değer kullanım dışı ( *deprecated* ) bırakılmıştır. Bu nedenle, kullanım senaryosuna göre uygun değeri ayarlayın.

2. Login endpoint’inin implementasyonunu gözlemleyin. Kullanıcı sisteme bir kullanıcı adı sağlayarak giriş yapar. Bir saat geçerli olan bir access token üretilir. Bu geçerlilik süresini, saniye cinsinden zamanı ifade eden `60 * 60` ile belirtildiğini gözlemleyebilirsiniz. Bu access token, yalnızca doğrulanmış kullanıcıların o süre boyunca endpoint’lere erişebilmesini sağlamak için session nesnesine set edilir.

```javascript
// Login endpoint
app.post("/login", (req, res) => {
 const user = req.body.user;
 if (!user) {
 return res.status(404).json({ message: "Body Empty" });
 }
 // JWT access token üret
 let accessToken = jwt.sign({
 data: user
 }, 'access', { expiresIn: 60 * 60 });
 // Access token’ı session içinde sakla
 req.session.authorization = {
 accessToken
 }
 return res.status(200).send("User successfully logged in");
});
```

3. Authentication middleware’inin implementasyonunu gözlemleyin. `/user` ile başlayan tüm endpoint’ler bu middleware’den geçecektir. Session’dan authorization ayrıntılarını alacak ve doğrulayacaktır. Token doğrulanırsa kullanıcı doğrulanmıştır ve kontrol bir sonraki endpoint handler’a aktarılır. Token geçersizse kullanıcı doğrulanmamıştır ve bir hata mesajı döndürülür.

```javascript
// Kullanıcı authentication’ı için middleware
app.use("/user", (req, res, next) => {
 // Kullanıcının doğrulanıp doğrulanmadığını kontrol et
 if (req.session.authorization) {
 let token = req.session.authorization['accessToken']; // Access Token
 
 // Kullanıcı authentication’ı için JWT token’ını doğrula
 jwt.verify(token, "access", (err, user) => {
 if (!err) {
 req.user = user; // Doğrulanmış kullanıcı verisini request nesnesine set et
 next(); // Bir sonraki middleware’e geç
 } else {
 return res.status(403).json({ message: "User not authenticated" }); // Token doğrulaması başarısızsa hata döndür
 }
 });
 
 // Session içinde access token yoksa hata döndür
 } else {
 return res.status(403).json({ message: "User not logged in" });
 }
});
```

---

## 🧪 Alıştırma 8: POSTMAN ile Endpoint’leri Test Etme

API endpoint’lerini cURL ile test ettiniz. Bu endpoint’leri test etmenin daha kolay ve daha kullanıcı dostu bir yolu, grafik kullanıcı arayüzü ( *GUI* ) aracı Postman’dır.

1. Postman’a gidin. Zaten bir hesabınız yoksa yeni bir Postman hesabı oluşturun. Hesabınıza giriş yapın.
2. Postman’a giriş yaptıktan sonra, aşağıda gösterildiği gibi  **New Request** ’e tıklayın:

**Not:** Sunucu theia lab içinde çalışıyorsa lütfen **CTRL + C** tuşlarına basarak sunucuyu durdurun. Şimdi, 5000 portunu dinleyecek şekilde aşağıdaki komutu çalıştırarak sunucuyu başlatın.

```bash
npm run start_auth
```

Şu ana kadar tüm endpoint’lere authentication olmadan erişiyorduk, ancak şimdi endpoint’lere erişmek için authentication kullanacağız.

3. Launch application’dan URL’yi kopyalayın ve user ayrıntılarını POST REQUEST içinde eklemek için endpoint olarak login’i ekleyin; bu aşağıdaki gibi görünecektir:

`https://<sn-lab-username>-5000.theiadocker-2-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/login`

4. Kullanıcı ayrıntıları aşağıdaki formatta olmalıdır:

```json
{
 "user":{
 "name":"abc",
 "id":1
 }
}
```

Şimdi bir HTTP GET Request göndererek teste başlayalım.

### 8.1 GET isteği

a. GET request URL’sini girin: `https://XXXXXXXXXX-5000.theiadocker-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/user` adresini, Postman’da “Enter Request URL” gördüğünüz giriş kutusuna yazın.
b. URL’yi girdikten sonra **Send** düğmesine tıklayın.
c. Çıktı aşağıdaki gibi olacaktır:

### 8.2 Belirli bir ID’ye göre GET isteği

a. Yukarıdaki GET request URL’sine belirli e-posta adresini ekleyerek request URL’sini girin. E-posta adresi `johnsmith@gamil.com` ise, Postman giriş kutusuna aşağıdaki URL’yi girin:

`https://XXXXXXXXXX-5000.theiadocker-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/user/johnsmith@gamil.com`

b. Çıktıyı görmek için URL’yi girdikten sonra **Send** düğmesine tıklayın.
c. Çıktı aşağıdaki gibi olacaktır:

### 8.3 POST isteği

a. Temel post request URL’sini girin:

`https://XXXXXXXXXX-5000.theiadocker-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/user/`

POST metodunu seçtiğinizden ve “Params”ı seçtiğinizden emin olun.

b. Yeni bir kullanıcı için firstName’i `Bob`, lastName’i `Smith`, email’i `bobsmith@gamil.com` ve DOB’yi `1/1/1978` olarak girin:
c. Çıktıyı görmek için URL’yi girdikten sonra **Send** düğmesine tıklayın.
Yeni eklenen değerlerin güncellendiğini, GET isteği yaparak doğrulayın.

**Not:** GET isteğini göndermeden önce POST isteği için eklediğiniz parametreleri sildiğinizden emin olun.

### 8.4 PUT isteği

a. Belirli e-posta adresini ekleyerek URL’yi girin. E-posta adresi `bobsmith@gamil.com` ise, Postman giriş kutusuna şu URL’yi girin:

`https://XXXXXXXXXX-5000.theiadocker-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/user/bobsmith@gamil.com`

PUT metodunu seçtiğinizden ve “Params”ı seçtiğinizden emin olun.

b. Değiştirilecek anahtarları ve değerleri girin. Örneğin “DOB” anahtarını değiştirmek ve yeni değer olarak `1/1/1981` ile değiştirmek istiyorsanız aşağıdaki gibi olacaktır.
c. Çıktıyı görmek için URL’yi girdikten sonra **Send** düğmesine tıklayın.
Yeni eklenen değerlerin güncellendiğini, GET isteği yaparak doğrulayın.

**Not:** GET isteğini göndermeden önce PUT isteği için eklediğiniz parametreleri sildiğinizden emin olun.

### 8.5 DELETE isteği

a. Belirli e-posta adresini ekleyerek URL’yi girin. E-posta adresi `bobsmith@gamil.com` ise, Postman giriş kutusuna şu URL’yi girin:

`https://XXXXXXXXXX-5000.theiadocker-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/user/bobsmith@gamil.com`

DELETE metodunu seçtiğinizden emin olun.

b. Çıktıyı görmek için URL’yi girdikten sonra **Send** düğmesine tıklayın.
c. GET user by ID `bobsmith@gamil.com`’un null bir nesne döndürdüğünü doğrulamak için bir GET isteği gönderin.

**Not:** GET isteğini göndermeden önce herhangi bir parametre (varsa) sildiğinizden emin olun.

---

## 🧩 Pratik Laboratuvarlar

1. Aynı kod içinde, belirli bir Soyad ile tüm kullanıcıları getirmek için bir endpoint oluşturun.
   **İpucu için buraya tıklayın!** İpucu: `users` dizisinden `lastName` filtreleyin. **Çözüm için buraya tıklayın!**
   **Çözüm:**

```javascript
router.get("/lastName/:lastName", (req, res) => {
 // İstek URL’sinden lastName parametresini çıkar
 const lastName = req.params.lastName;
 // Çıkarılan lastName parametresiyle eşleşen lastName’e sahip kullanıcıları bulmak için users dizisini filtrele
 let filtered_lastname = users.filter((user) => user.lastName === lastName);
 // filtered_lastname dizisini istemciye yanıt olarak gönder
 res.send(filtered_lastname);
});
```

2. Aynı kod içinde, kullanıcıları doğum tarihine göre sıralamak için bir endpoint oluşturun.
   **İpucu için buraya tıklayın!** İpucu: DOB’yi bölün ve `yyyy/mm/dd` formatına dönüştürün ve sonra sıralayın. **Çözüm için buraya tıklayın!**
   **Çözüm:**

```javascript
// "dd-mm-yyyy" formatındaki bir tarih string’ini Date nesnesine dönüştürmek için fonksiyon
function getDateFromString(strDate) {
 let [dd, mm, yyyy] = strDate.split('-');
 return new Date(yyyy + "/" + mm + "/" + dd);
}
// "/sort" endpoint’i için GET isteklerine yönelik bir route handler tanımla
router.get("/sort", (req, res) => {
 // users dizisini DOB’ye göre artan sırada sırala
 let sorted_users = users.sort(function(a, b) {
 let d1 = getDateFromString(a.DOB);
 let d2 = getDateFromString(b.DOB);
 return d1 - d2;
 });
 // sorted_users dizisini istemciye yanıt olarak gönder
 res.send(sorted_users);
});
```

---

## ✅ Tebrikler

Node.js ve Express.js ile CRUD operasyonları laboratuvarını Postman kullanarak tamamladınız.

**Özet:** Bu laboratuvarda, bir Express App üzerinde GET, POST, PUT ve DELETE gibi CRUD operasyonlarını gerçekleştirdik ve yukarıdaki yöntemleri Postman kullanarak test ettik.

---

## 👤 Yazar(lar)

Sapthashree K S
K Sundararajan
