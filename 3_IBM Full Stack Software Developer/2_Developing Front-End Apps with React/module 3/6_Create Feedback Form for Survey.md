# 🧪 Lab: Anket için Geri Bildirim Formu Oluşturma

## ⏱️ Gerekli Tahmini Süre

40 dakika

---

## 📚 Ne Öğreneceksiniz

Bu lab’de, React functional component’ler kullanarak bir geri bildirim formu oluşturacak ve kullanıcı detaylarını *useState* hook’u ile yöneteceksiniz. Form input değişikliklerini yönetmek, kullanıcı input’larını doğrulamak ve form gönderimlerini ele almak için event handler’lar uygulayacaksınız. Ayrıca, final gönderimden önce kullanıcı detaylarını doğrulamak için *confirm* metodunu kullanarak bir confirmation dialog oluşturacaksınız. Başarılı gönderimden sonra, form alanlarını sıfırlayacak ve kullanıcıya bir teşekkür mesajı göstereceksiniz. Bu lab, React uygulamalarında etkileşimli formlar oluşturma ve kullanıcı input’larını yönetme konusunda size pratik deneyim kazandıracaktır.

---

## 🎯 Öğrenme Hedefleri

Bu lab’i tamamladıktan sonra şunları yapabileceksiniz:

* Kullanıcıdan geri bildirim toplamak için bir form oluşturmak; buna kullanıcı adı, e-posta ve geri bildirim mesajı dahildir.
* Form gönderimini yönetmek (veri doğrulaması dahil) ve kullanıcıların göndermeden önce isimlerini girmesini ve geri bildirim sağlamasını temin etmek.
* Kullanıcılar geri bildirimlerini gönderdikten sonra, girdikleri bilgileri gösteren ve final gönderimden önce onaylamalarını isteyen bir confirmation dialog göstermek.
* Input değerlerini temizlemek için form alanlarını sıfırlamak ve kullanıcıya ek geri bildirim gönderebilmesi için temiz bir form sunmak.

---

## ✅ Ön Koşullar

* HTML hakkında temel bilgi
* JavaScript hakkında orta seviye bilgi
* React function component, *useState* hook’u ve form kullanımı hakkında temel bilgi

---

## 🧰 Adım 1: Ortamı Kurma

1. Lab’in üst menüsünden, verilen ekran görüntüsünde 1 numarada gösterilen yerde sağ üstteki **Terminal** sekmesine tıklayın ve ardından 2 numarada gösterildiği gibi  **New Terminal** ’a tıklayın.
2. Bu React uygulaması için boiler template’i klonlamak üzere terminale aşağıdaki komutu yazın ve Enter’a basın.

```bash
git clone https://github.com/ibm-developer-skills-network/feedback_form.git
```

3. Bu işlem, proje klasörü altında **feedback_form** adlı bir klasör oluşturacaktır ve yapı, verilen ekran görüntüsündeki gibi olacaktır. *feedback_form* uygulaması, **FeedbackForm.jsx** adlı bir class component ve **FeedbackForm.css** adlı bir css dosyası içerir.
4. Terminalde **feedback_form** klasörüne girmek için komutu yazın. Bu komut, React uygulamasını *feedback_form* klasöründe çalıştırmak için terminal path’inizi ayarlayacaktır.

```bash
cd feedback_form
```

5. Klonladığınız kodun doğru çalıştığından emin olmak için aşağıdaki adımları izlemelisiniz:
   Terminalde aşağıdaki komutu yazın ve uygulamayı çalıştırmak için gerekli tüm paketleri yüklemek üzere Enter’a basın.

```bash
npm install
```

Ardından uygulamayı çalıştırmak için aşağıdaki komutu yürütün; bu işlem size **4173** port numarasını sağlayacaktır.

```bash
npm run preview
```

6. React uygulamanızı görüntülemek için sol paneldeki **Skills Network** ikonuna tıklayın (1 numaraya bakın). Bu işlem  **Skills Network Toolbox** ’ı açacaktır. Ardından  **Launch Application** ’a tıklayın (2 numaraya bakın). **Application Port** alanına **4173** port numarasını girin (3 numaraya bakın) ve tıklayın.
7. Çıktı, verilen ekran görüntüsündeki gibi görüntülenecektir.
8. Bu lab’deki en son çalışmanızı, GitHub repository’nize ekleyip commit’leyerek ve push’layarak saklayabilirsiniz. Bu, görev üzerinde sürekli çalışmıyor olsanız bile ilerlemenizin kaydedilmesini sağlar ve kaldığınız yerden devam etmenize olanak tanır.
   **Not:** Adım 8 isteğe bağlıdır.

---

## 🧱 Adım 3: Temel Şablonu Oluşturma

1. React projenizin **src** klasörü içindeki **Components** klasörüne gidin.
2. React projenizin **src** klasörü içinde yer alan **FeedbackForm.jsx** component’ine gidin. Bu component’in return kısmında bir `<nav>` etiketi ve **feedback-form** class adına sahip bir `<form>` etiketi bulunmaktadır; bu form, bir `<p>` etiketi içeren bir alt `<h2>` etiketi barındırır.
3. Geri bildirim formunu oluşturmak için üç input alanı eklemeniz ve kullanıcının aşağıdaki detaylarını almak için bir buton oluşturmanız gerekir:
   * Kullanıcı adı için ilk input kutusu
   * Kullanıcı e-posta ID’si için ikinci input kutusu
   * Kullanıcı geri bildirimi için üçüncü input kutusu

```jsx
<input
 type="text"
 name="name"
 placeholder="Your Name"
 />
 <input
 type="email"
 name="email"
 placeholder="Your Email"
 />
 <textarea
 name="feedback"
 placeholder="Your Feedback"
 ></textarea>
 <button type="submit">Submit Feedback</button>
```

4. En güncel çıktıyı görmek için terminalde **ctrl+c** yapın ve uygulamayı yeniden çalıştırın. Çıktıyı ekran görüntüsünde göreceksiniz.
   **Not:** Uygulama zaten çalışıyorsa, yalnızca uygulama sayfasını yenilemeniz gerekir.

---

## 🧾 Adım 4: Form Verisini Yönetmek İçin State’leri Başlatma

1. Form veri state’ini yönetmek için component’in en üstünde React’ten *useState* hook’unu entegre edin. *useState* hook’unu, name, email ve feedback gibi form veri detayları için state değişkenleri oluşturmak üzere kullanın.

```jsx
import React, { useState } from 'react';
```

2. Detayları boş string’lerle başlatın. *useState* hook’u kullanarak name, email ve feedback form detaylarını içeren bir object initialize etmeniz gerekir.

```js
const [formData, setFormData] = useState({
 name: '',
 email: '',
 feedback: ''
 });
```

**Not:** Yukarıdaki kodu bu component’in return’ünden önce ekleyin.

---

## 🔄 Adım 5: Change Handler’ları Uygulama

1. Kullanıcılar bilgilerini girerken form veri state’ini güncellemek için bir **handleChange** fonksiyonu tanımlayın. Bunu, *useState* hook’u ile değişkenleri initialize ettikten sonra oluşturun.
2. **handleChange** fonksiyonu içinde, event nesnesinden input field’ın name ve value değerlerini çıkarın.
3. Yeni değeri mevcut form verisiyle birleştirmek için *setFormData* fonksiyonunu ve spread operator’ünü kullanarak form veri state’ini güncelleyin.

```js
const handleChange = (event) => {
 const { name, value } = event.target;
 setFormData({
 ...formData,
 [name]: value
 });
};
```

* `const handleChange = (event) => { ... }`: Bu satır, handleChange adlı bir constant tanımlar ve ona bir arrow function atar. Fonksiyon, kullanıcının bir input element’iyle etkileşimi sonucu tetiklenen event’i temsil eden `event` parametresini alır.
* `const { name, value } = event.target;`: Bu satır, event nesnesinin `target` özelliğinden `name` ve `value` özelliklerini çıkarır. `target`, event’i tetikleyen DOM element’ini ifade eder; bu durumda bir input field. `name`, input field’ın `name` attribute’una karşılık gelirken `value`, kullanıcının input field’a girdiği mevcut değeri temsil eder.
* `setFormData({ ...formData, [name]: value });`: `setFormData`, *useState* hook’u tarafından sağlanan bir state güncelleme fonksiyonudur ve `formData` state değişkenini günceller. Mevcut `formData` object’ini spread eder ve ardından `name` değişkeniyle belirtilen property’yi yeni değerle günceller. Bu pattern, state’in immutable şekilde güncellenmesini sağlar; yani mevcut state’i doğrudan değiştirmek yerine, güncellenmiş property ile yeni bir object oluşturulur.

---

## 🔗 Adım 6: Form State’i ve onchange Event’ini Entegre Etme

1. JSX kodunda form input field’larını (name, email ve feedback) ilgili state değişkenlerine `formData.name`, `formData.email` ve `formData.feedback` kullanarak bağlayın.
2. Input field değerlerini ayarlamak için `value` attribute’unu ve input değerleri değiştiğinde `handleChange` fonksiyonunu çağırmak için `onChange` attribute’unu kullanın.

```jsx
<input
 type="text"
 name="name"
 placeholder="Your Name"
 value={formData.name}
 onChange={handleChange}
 />
 <input
 type="email"
 name="email"
 placeholder="Your Email"
 value={formData.email}
 onChange={handleChange}
 />
 <textarea
 name="feedback"
 placeholder="Your Feedback"
 value={formData.feedback}
 onChange={handleChange}
 ></textarea>
```

**Not:** Önceki input field ve textarea’nıza value ve onchange attribute’larını ekleyin.

---

## 📨 Adım 7: Form Gönderimini Yönetme

1. **handleSubmit** adlı bir fonksiyon tanımlayarak form gönderim işlevselliğini uygulayın. Bu fonksiyon bir event parametresi almalı ve default form gönderimini engellemelidir.
2. Ardından, kullanıcı detaylarını yakalamak için **confirmationMessage** adlı bir değişken oluşturun.
3. Sonra, kullanıcının detaylarının doğru olup olmadığını doğrulamak için **isConfirmed** adlı başka bir değişken oluşturun.
4. Eğer doğrulanırsa, form verisini console’a loglayın, kullanıcıya alert kutusu ile bir teşekkür mesajı gösterin ve form veri state’ini resetleyerek form alanlarını temizleyin.

```js
const handleSubmit = (event) => {
 event.preventDefault();
 const confirmationMessage = `
 Name: ${formData.name}
 Email: ${formData.email}
 Feedback: ${formData.feedback}
 `;
 const isConfirmed = window.confirm(`Please confirm your details:\n\n${confirmationMessage}`);
 if (isConfirmed) {
 console.log('Submitting feedback:', formData);
 setFormData({
 name: '',
 email: '',
 feedback: ''
 });
 alert('Thank you for your valuable feedback!');
 }
 };
```

Bu kod şunları içerir:

* `const confirmationMessage = ...`: Bu template, `formData` object’indeki verileri kullanarak bir confirmation mesajı oluşturur. Kullanıcının girdiği name, email ve feedback alanlarını içerir.
* `const isConfirmed = window.confirm(...);`: Bu satır, `window.confirm()` kullanarak bir confirmation dialog gösterir ve kullanıcıya `confirmationMessage`’ı sunar. Kullanıcı dialog’da detayları onaylarsa `isConfirmed` true olur; aksi halde false olur.
* `if (isConfirmed) { ... }`: Bu koşullu ifade, kullanıcının confirmation dialog’da “OK” tıklayarak detaylarını onaylayıp onaylamadığını kontrol eder.
* `setFormData({ ... });`: `setFormData`, `formData` state’ini boş değerlere resetlemek için çağrılır; gönderimden sonra form alanlarını temizler.
* `alert('Thank you for your valuable feedback!');`: Form resetlendikten sonra, kullanıcıya geri bildirimi için teşekkür eden bir alert gösterilir.

**Not:** Bu kodu FeedbackForm component’inin return’ünden hemen önce ekleyin.

---

## 🧷 Adım 8: onSubmit Event Handler’ını Uygulama

1. Detayları göndermek için `<form>` etiketine `onSubmit` event handler’ını ekleyin.

```jsx
<form onSubmit={handleSubmit} className="feedback-form">
```

---

## ✅ Adım 9: Çıktıyı Kontrol Etme

1. Şimdi uygulamayı yeniden çalıştırmanız ve detayları doldurmanız gerekir. Ardından  **Submit Feedback** ’e tıklayın. Doldurulan detaylarla birlikte bir confirm kutusu görünecektir. Uygulama tarayıcıda zaten çalışıyorsa sayfayı yenileyin.
2. **OK** ’e tıklarsanız, teşekkür notu içeren başka bir alert kutusu görüntülenecektir.
3. Confirm kutusunda  **Cancel** ’a tıklarsanız, doldurulmuş detaylarla birlikte form yeniden görünecektir.

Tebrikler! Bir feedback form uygulaması oluşturdunuz!

4. **FeedbackForm.jsx** için tüm kod çözümünü görmek için buraya tıklayın.

```jsx
import React, { useState } from 'react';
 import './FeedbackForm.css'; // Import CSS for styling
 const FeedbackForm = () => {
 const [formData, setFormData] = useState({
 name: '',
 email: '',
 feedback: ''
 });
 const handleChange = (event) => {
 const { name, value } = event.target;
 setFormData({
 ...formData,
 [name]: value
 });
 };
 const handleSubmit = (event) => {
 event.preventDefault();
 const confirmationMessage = `
 Name: ${formData.name}
 Email: ${formData.email}
 Feedback: ${formData.feedback}
 `;
 const isConfirmed = window.confirm(`Please confirm your details:\n\n${confirmationMessage}`);
 if (isConfirmed) {
 console.log('Submitting feedback:', formData);
 setFormData({
 name: '',
 email: '',
 feedback: ''
 });
 alert('Thank you for your valuable feedback!');
 }
 };
 return (
 <>
 <nav>
 Tell Us What You Think
 </nav>
 <form onSubmit={handleSubmit} className="feedback-form">
 <h2>We'd Love to Hear From You!</h2>
 <p>Please share your feedback with us.</p>
 <input
 type="text"
 name="name"
 placeholder="Your Name"
 value={formData.name}
 onChange={handleChange}
 />
 <input
 type="email"
 name="email"
 placeholder="Your Email"
 value={formData.email}
 onChange={handleChange}
 />
 <textarea
 name="feedback"
 placeholder="Your Feedback"
 value={formData.feedback}
 onChange={handleChange}
 ></textarea>
 <button type="submit">Submit Feedback</button>
 </form>
 </>
 );
 };
 export default FeedbackForm;
```

---

## 🧩 Practice Exercise

1. Bu alıştırmada, kullanıcıların ayrıca rating verebilmesi için radio button’lar kullanarak bir rating sistemi oluşturacaksınız.
2. Önce, *formData useState hook* içinde **rating** adlı bir değişken oluşturmanız ve bunu boş string olarak initialize etmeniz gerekir.
   **İpucu:** Bu değişkeni `formData` içinde key value pair olarak ekleyin.
   Çözüm için buraya tıklayın.

```js
const [formData, setFormData] = useState({
 name: '',
 email: '',
 feedback: '',
 rating: '' // New state for rating
 });
```

3. Bunun için type’ı radio button olan bir input kutusu kullanmanız gerekir. 1’den 5’e kadar değerleri temsil eden beş radio button ile bir rating sistemi oluşturmak için, her radio button bir rating değerini 1’den 5’e temsil etmelidir. Her radio button kendi değerini göstermelidir: ilk radio button “1”, ikinci “2” ve bu şekilde beşinci radio button “5” değerini göstermelidir. Type’ı radio button olan input kutusunun, *handleChange* fonksiyonu kullanarak yapılan yeni seçimi yansıtacak şekilde *formData* state’ini güncellemek için `onChange` event handler’ına sahip olduğundan emin olun.
   **İpucu:** `type='radio'` olan input box field kullanın. Event handler fonksiyonunu `onChange={handleChange}` ile çağırın.
   Çözüm için buraya tıklayın.

```jsx
<div style={{display:'flex',gap:'10px',flexDirection:'column'}}>
 <span>Rate Us:</span>
<p><input
 type="radio"
name="rating"
value="1"
onChange={handleChange}
 /> 1</p>
 <p> <input
 type="radio"
name="rating"
value="2"
onChange={handleChange}
 /> 2</p>
 <p> <input
 type="radio"
name="rating"
value="3"
onChange={handleChange}
 /> 3</p>
 <p> <input
 type="radio"
name="rating"
value="4"
onChange={handleChange}
 /> 4</p>
<p><input
 type="radio"
name="rating"
value="5"
onChange={handleChange}
 /> 5</p>
 </div>
```

4. Tüm bilgiyi `...formData` spread operator’ü ile aldığınız için **handleChange** fonksiyonu değişmeden kalacaktır.
5. Şimdi rating detaylarını **handleSubmit** fonksiyonuna dahil etmeniz gerekir. Bunun için, `formData` değişkeninden radio button için kullanıcı tarafından seçilen değeri almanız ve diğer detaylarla birlikte görüntülemek üzere `confirmationMessage` içine dahil etmeniz gerekir.
   **İpucu:** Radio button field için kullanıcı input’unu erişmek ve göstermek için `formData.rating` değerini bir değişkene koyun.
   Çözüm için buraya tıklayın.

```js
const handleSubmit = (event) => {
 event.preventDefault();
 const confirmationMessage = `
 Name: ${formData.name}
 Email: ${formData.email}
 Feedback: ${formData.feedback}
 Rating: ${formData.rating}
 `;
 const isConfirmed = window.confirm(`Please confirm your details:\n\n${confirmationMessage}`);
 if (isConfirmed) {
 console.log('Submitting feedback:', formData);
 setFormData({
 name: '',
 email: '',
 feedback: '',
 rating: '' // Reset rating after submission
 });
 alert('Thank you for your valuable feedback!');
 }
};
```

6. Şimdi uygulamayı yeniden çalıştırarak çıktıyı kontrol edin. Çıktı, verilen ekran görüntüsüne göre görünecektir.
7. Tüm formu tekrar doldurun ve alert mesajını kontrol edin. Rating’i de diğer detaylarla birlikte gösterecektir.
   Tüm kod çözümü için buraya tıklayın.

```jsx
import React, { useState } from 'react';
import './FeedbackForm.css'; // Import CSS for styling
const FeedbackForm = () => {
 const [formData, setFormData] = useState({
 name: '',
 email: '',
 feedback: '',
 rating: '' // New state for rating
 });
 const handleChange = (event) => {
 const { name, value } = event.target;
 setFormData({
 ...formData,
 [name]: value
 });
 };
 const handleSubmit = (event) => {
 event.preventDefault();
 const confirmationMessage = `
 Name: ${formData.name}
 Email: ${formData.email}
 Feedback: ${formData.feedback}
 Rating: ${formData.rating}
 `;
 const isConfirmed = window.confirm(`Please confirm your details:\n\n${confirmationMessage}`);
 if (isConfirmed) {
 console.log('Submitting feedback:', formData);
 setFormData({
 name: '',
 email: '',
 feedback: '',
 rating: '' // Reset rating after submission
 });
 alert('Thank you for your valuable feedback!');
 }
 };
 return (
 <>
 <nav>
 Tell Us What You Think
 </nav>
 <form onSubmit={handleSubmit} className="feedback-form">
 <h2>We'd Love to Hear From You!</h2>
 <p>Please share your feedback with us.</p>
 <input
 type="text"
 name="name"
 placeholder="Your Name"
 value={formData.name}
 onChange={handleChange}
 />
 <input
 type="email"
 name="email"
 placeholder="Your Email"
 value={formData.email}
 onChange={handleChange}
 />
 <textarea
 name="feedback"
 placeholder="Your Feedback"
 value={formData.feedback}
 onChange={handleChange}
 ></textarea>
 <div style={{display:'flex',gap:'10px',flexDirection:'column'}}>
 <span>Rate Us:</span>
 <p><input
 type="radio"
 name="rating"
 value="1"
 
 onChange={handleChange}
 /> 1</p>
 <p> <input
 type="radio"
 name="rating"
 value="2"
 
 onChange={handleChange}
 /> 2</p>
 <p> <input
 type="radio"
 name="rating"
 value="3"
 onChange={handleChange}
 /> 3</p>
 <p> <input
 type="radio"
 name="rating"
 value="4"
 onChange={handleChange}
 /> 4</p>
 <p><input
 type="radio"
 name="rating"
 value="5"
 onChange={handleChange}
 /> 5</p>
 </div>
 <button type="submit">Submit Feedback</button>
 </form>
 </>
 );
};
export default FeedbackForm;
```

---

## 🧾 Sonuç

Verilen **FeedbackForm** component’inde kullanıcı geri bildirimi toplamak için bir form uyguladınız. Component, kullanıcının name, email ve feedback bilgileri dahil olmak üzere form data state’ini yönetmek için React’in *useState* hook’unu kullanır.

**handleChange** fonksiyonu, kullanıcı form alanlarına bilgi girerken form data state’ini günceller. Form gönderimi sırasında, **handleSubmit** fonksiyonu default form gönderim davranışını engeller, kullanıcının detaylarıyla birlikte bir confirmation dialog gösterir, form alanlarını temizler ve onay sonrası bir teşekkür mesajı görüntüler.

Form, kullanıcının adı ve e-postası için input alanları ve geri bildirim sağlamak için bir text area içerir.

---

## ✍️ Yazar(lar)

Richa Arora

---

## ©️ Telif

© IBM Corporation. Tüm hakları saklıdır.
