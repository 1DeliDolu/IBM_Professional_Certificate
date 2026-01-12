## 🧪 Lab: Function Component Event Planner Landing Page

*cognitiveclass.ai logo*

Tahmini gereken süre: **40 dakika**

---

## 🎯 Ne Öğreneceksiniz?

Bu lab’de, kişisel ve kurumsal etkinlikler planlayan bir organizasyon için bir landing page oluşturacaksınız. Açıklama bölümü, etkinlik kategorileri, özellikler, referanslar ( *testimonials* ), iletişim formu ve footer gibi çeşitli bölümlerden oluşan **EventPlanner** bileşenini oluşturacaksınız.

Her bölüm, Event Planner uygulamasının çeşitli yönlerini açıklar; örneğin, planlanabilecek etkinlik türleri, uygulamanın ana özellikleri, müşteri yorumları ve hizmet sağlayıcıyla nasıl iletişime geçileceği.

React bileşenini **JSX** sözdizimini kullanarak yapılandıracak ve `<div>`, `<header>` ve `<h1>` gibi temel HTML öğelerini kullanacaksınız. Ek olarak, temiz ve düzenli bir kod yapısını korumanın önemine ve ölçeklenebilir React uygulamaları oluştururken bileşen yeniden kullanılabilirliği ( *reusability* ) ve modülerliğin ( *modularity* ) rolüne dair içgörü kazanacaksınız.

---

## 🧭 Learning objectives

Bu lab’i tamamladıktan sonra şunları yapabileceksiniz:

* Kolay bakım ve sorun yönetimi sağlamak için Event Planner landing page düzenini organize edecek şekilde React bileşenlerinden oluşan yapılandırılmış bir hiyerarşi oluşturmak
* JSX kodu kullanarak header’lar, paragraflar, listeler ve butonlar gibi kullanıcı arayüzü öğelerini yazmak
* Veri kaynaklarından dinamik olarak alınan referanslar ( *testimonials* ), etkinlik kategorileri ve özellikleri dinamik içerik render etme ile göstermek
* Kullanılabilirlik ve arama motoru optimizasyonu (SEO) faydaları sağlamak için semantik HTML işaretlemesi ( *semantic HTML markup* ) kullanmak

---

## ✅ Prerequisites

* HTML hakkında temel bilgi
* JavaScript hakkında orta düzey bilgi
* React function component hakkında temel bilgi

---

## 🛠️ Setting up the environment

Lab’in üst menüsünden, verilen ekran görüntüsünde **1** numara ile gösterilen pencerenin sağ üstündeki **Terminal** sekmesine tıklayın ve ardından **2** numara ile gösterildiği gibi **New Terminal** seçeneğine tıklayın.

---

## 📥 Boiler Template’i Klonlama

Terminale aşağıdaki komutu yazın ve  **Enter** ’a basarak bu React uygulaması için boiler template’i klonlayın:

```bash
git clone https://github.com/ibm-developer-skills-network/event_planner.git
```

Yukarıdaki komut, **Project** klasörü altında **event_planner** adlı bir klasör oluşturacaktır ve yapı, verilen ekran görüntüsünde gösterildiği gibi olacaktır.

---

## 📂 event_planner Klasörüne Girme

Terminalde **event_planner** klasörüne girmek için aşağıdaki komutu kullanarak klasöre gidin:

```bash
cd event_planner
```

---

## 📦 Gerekli Paketleri Kurma

Klonladığınız kodun doğru çalıştığından emin olmak için aşağıdaki adımları izlemelisiniz:

Uygulamayı çalıştırmak için gerekli tüm paketleri yüklemek üzere terminalde aşağıdaki komutu yazın ve  **Enter** ’a basın:

```bash
npm install
```

---

## ▶️ Uygulamayı Çalıştırma

Ardından uygulamayı çalıştırmak için aşağıdaki komutu yürütün; bu işlem size **4173** port numarasını sağlayacaktır:

```bash
npm run preview
```

---

## 🌐 React Uygulamasını Görüntüleme

React uygulamanızı görüntülemek için sol panelde **Skills Network** ikonuna tıklayın ( **1** numaraya bakın ). Bu işlem  **SKILLS NETWORK TOOLBOX** ’ı açacaktır.

Sonrasında  **Launch Application** ’a tıklayın ( **2** numaraya bakın ). **Application Port** alanına **4173** port numarasını girin ( **3** numaraya bakın ) ve tıklayın.

Çıktı, verilen ekran görüntüsünde gösterildiği gibi görüntülenecektir.

---


## 🧱 Create Basic Template

`src` klasörü içinde bulunan **Components** klasörüne gidin. `event_planner` uygulama klasörü, **EventPlanner.jsx** adlı class component’i ve **EventPlanner.css** adlı bir CSS dosyası içerir.

`src` klasörü içinde bulunan **EventPlanner.jsx** bileşenine gidin. Bu bileşenin *return* kısmında, `event-planner-container` sınıf adına sahip bir üst `<div>` bulunur ve bu `<div>` içinde `<h1>` etiketini içeren bir `<header>` etiketi yer alır.

`<header>` etiketinden sonra **beş** adet `<section>` etiketi oluşturmanız gerekir.

* Birinci `section` etiketi: `className="description"`
* İkinci `section` etiketi: `className="events_categories"`
* Üçüncü `section` etiketi: `className="features"`
* Dördüncü `section` etiketi: `className="testimonials"`
* Beşinci `section` etiketi: `className="contact"`

```jsx
<div className="event-planner-container">
    {/* Page Header */}
    <header>
        <h1>Welcome to Event Planner</h1>
    </header>
    {/* Section for describing the purpose or overview of the app */}
    <section className="description">
        {/* Description content goes here */}
    </section>
    {/* Section to list or categorize different types of events */}
    <section className="events_categories">
        {/* Event categories content goes here */}
    </section>
    {/* Section to highlight app features or functionalities */}
    <section className="features">
        {/* Features content goes here */}
    </section>
    {/* Section to showcase user reviews or testimonials */}
    <section className="testimonials">
        {/* Testimonials content goes here */}
    </section>
    {/* Section to provide contact information or a contact form */}
    <section className="contact">
        {/* Contact content goes here */}
    </section>
</div>
```

---



## 📝 Define Description and Event Categories

`className="description"` olan `section` etiketinin içine bir `<p>` etiketi ve bir `button` etiketi ekleyin. `<p>` etiketinin içine etkinlik planlama temasına uygun bir metin ekleyin. `button` etiketine `get-started-button` sınıf adını atayın.

```jsx
<section className="description">
    {/* Brief introduction or marketing message */}
    <p>
        Plan and organize your events effortlessly with Event Planner. From
        birthdays to corporate meetings, we've got you covered.
    </p>
    {/* Primary call-to-action button */}
    <button className="get-started-button">Get Started</button>
</section>
```

Ardından React uygulamasını yeniden çalıştırmanız ve çıktıyı görmeniz gerekir. Çıktı, verilen ekran görüntüsündeki gibi olmalıdır.

> Not: Sayfa tarayıcıda zaten açıksa, yenilemeniz ( *refresh* ) gerekecektir.

---

## 🗂️ Event Categories Oluşturma

Sonraki adımda, `className="events_categories"` olan `section` etiketi içinde birden fazla etkinlik kategorisi oluşturmanız gerekir. Bunun için bu `section` içine bir `<ul>` etiketi oluşturun. `<ul>` etiketinin içinde etkinlik başlığı için bir `<h2>` etiketi ve o etkinliğin farklı kategorileri için birden fazla `<li>` etiketi olmalıdır.

```jsx
<ul>
    <h2>Social Events:</h2>
    <li>Birthday parties</li>
    <li>Anniversary celebrations</li>
    <li>Wedding receptions</li>
    <li>Baby showers</li>
    <li>Graduation parties</li>
    <li>Family reunions</li>
</ul>
```

Yukarıdaki gibi, farklı etkinlik başlıkları ve alt kategoriler için birden fazla `<ul>` etiketi de ekleyebilirsiniz.

```jsx
<section className="events_categories">
    {/* Social event types */}
    <ul>
        <h2>Social Events:</h2>
        <li>Birthday parties</li>
        <li>Anniversary celebrations</li>
        <li>Wedding receptions</li>
        <li>Baby showers</li>
        <li>Graduation parties</li>
        <li>Family reunions</li>
    </ul>
    {/* Entertainment-based event types */}
    <ul>
        <h2>Entertainment Events:</h2>
        <li>Concerts</li>
        <li>Music festivals</li>
        <li>Film screenings</li>
        <li>Comedy shows</li>
        <li>Art exhibitions</li>
        <li>Cultural events</li>
    </ul>
    {/* Community-focused event types */}
    <ul>
        <h2>Community Events:</h2>
        <li>Fundraising events</li>
        <li>Charity galas</li>
        <li>Volunteer drives</li>
        <li>Neighborhood block parties</li>
        <li>Community festivals</li>
        <li>Cultural celebrations</li>
    </ul>
</section>
```

Uygulamayı tekrar çalıştırın ve çıktıyı kontrol edin; verilen ekran görüntüsünde gösterildiği gibi görüntülenecektir.

> Not: Sayfa tarayıcıda zaten açıksa, yenilemeniz ( *refresh* ) gerekecektir.

---



## ✨ Create Features Section

Şimdi, bu event planner organizasyonunun etkinlik planlama için sunduğu farklı özellikleri görüntülemeniz gerekiyor.

`className="features"` olan `section` etiketi içinde, başlık için bir `<h1>` etiketi ve etkinlik planlama için sunulan çeşitli özellikleri göstermek üzere birden fazla `<li>` içeren bir `<ul>` etiketi oluşturun.

```jsx
<section className="features">
    {/* Section heading */}
    <h2>Features</h2>
    {/* List of key platform features */}
    <ul>
        <li>Easy event creation and management</li>
        <li>Customizable event templates</li>
        <li>Guest list management</li>
        <li>Real-time collaboration</li>
        <li>Reminders and notifications</li>
    </ul>
</section>
```

Yukarıdaki kod, event categories bölümünden sonra verilen ekran görüntüsündeki gibi çıktıyı gösterecektir.

En güncel güncellemeleri görmek için uygulamayı yeniden çalıştırmalısınız; sayfa tarayıcıda zaten açıksa, yenilemeniz ( *refresh* ) gerekecektir.

---



## 💬 Create Testimonials Section

Birden fazla kullanıcı tarafından verilen referansları ( *testimonials* ) oluşturmak için, `className="testimonials"` olan `section` etiketi içinde bir `<h1>` etiketi ve bir `<div>` etiketi oluşturmanız gerekir.

Ardından `<h2>` etiketi içinde bu bölümün ana başlığını vermeniz gerekir ve `<div>` etiketi içinde kullanıcının verdiği yorumu kullanıcı adıyla birlikte yazabilirsiniz.

```jsx
<section className="testimonials">
    <h2>Testimonials</h2>
    <div className="testimonial">
        <p>"Event Planner made organizing my wedding a breeze. Highly recommended!"</p>
        <p className="author">- Emily Johnson</p>
    </div>
</section>
```

Yukarıdaki gibi birden fazla testimonial da oluşturabilirsiniz.

```jsx
<section className="testimonials">
    {/* Section heading */}
    <h2>Testimonials</h2>
    {/* Individual testimonial block */}
    <div className="testimonial">
        <p>"Event Planner made organizing my wedding a breeze. Highly recommended!"</p>
        <p className="author">- Emily Johnson</p>
    </div>
    {/* Another testimonial block */}
    <div className="testimonial">
        <p>"I use Event Planner for all my corporate events. It saves me so much time and effort!"</p>
        <p className="author">- John Smith</p>
    </div>
</section>
```

Çıktı, Features bölümünden sonra verilen ekran görüntüsünde gösterildiği gibi görüntülenecektir.

---


## 📩 Create Contact Section

Şimdi, web sayfasını ziyaret eden herhangi bir kişinin organizasyon çalışanlarına kolayca ulaşabilmesi için bir contact bölümü oluşturun.

Bunun için, `className="contact"` olan `section` etiketi içinde bir `<h2>` etiketi ve bir `<form>` etiketi oluşturabilirsiniz. Formun içinde birden fazla input kutusu ve bir `<button>` etiketi bulunmalıdır.

```jsx
<section className="contact">
    {/* Section heading */}
    <h2>Contact Us</h2>
    {/* Contact form */}
    <form>
        {/* Name input field */}
        <input type="text" placeholder="Name" />
        {/* Email input field */}
        <input type="email" placeholder="Email" />
        {/* Message textarea */}
        <textarea placeholder="Message"></textarea>
        {/* Submit button */}
        <button className="submit-button">Send</button>
    </form>
</section>
```

Ardından terminalde uygulamayı tekrar çalıştırın ve çıktıyı kontrol edin. Çıktı, ekran görüntüsünde gösterildiği gibi görüntülenecektir.

---

## 🧩 EventPlanner.jsx Bileşeninin Tüm Kodu

Aşağıda **EventPlanner.jsx** bileşeninin tüm kodu yer almaktadır:

```jsx
import React from 'react';
import './EventPlanner.css'; // Import CSS file for styling

const EventPlanner = () => {
    return (
        <div className="event-planner-container">
            <header>
                <h1>Welcome to Event Planner</h1>
            </header>
            <section className="description">
                <p>
                    Plan and organize your events effortlessly with Event Planner. From
                    birthdays to corporate meetings, we've got you covered.
                </p>
                <button className="get-started-button">Get Started</button>
            </section>
            <section className="events_categories">
                <ul>
                    <h2>Social Events:</h2>
                    <li>Birthday parties</li>
                    <li>Anniversary celebrations</li>
                    <li>Wedding receptions</li>
                    <li>Baby showers</li>
                    <li>Graduation parties</li>
                    <li>Family reunions</li>
                </ul>
                <ul>
                    <h2> Entertainment Events:</h2>
                    <li>Concerts</li>
                    <li>Music festivals</li>
                    <li>Film screenings</li>
                    <li>Comedy shows</li>
                    <li>Art exhibitions</li>
                    <li>Cultural events</li>
                </ul>
                <ul>
                    <h2>Community Events:</h2>
                    <li>Fundraising events</li>
                    <li>Charity galas</li>
                    <li>Volunteer drives</li>
                    <li>Neighborhood block parties</li>
                    <li>Community festivals</li>
                    <li>Cultural celebrations</li>
                </ul>
            </section>
            <section className="features">
                <h2>Features</h2>
                <ul>
                    <li>Easy event creation and management</li>
                    <li>Customizable event templates</li>
                    <li>Guest list management</li>
                    <li>Real-time collaboration</li>
                    <li>Reminders and notifications</li>
                </ul>
            </section>
            <section className="testimonials">
                <h2>Testimonials</h2>
                <div className="testimonial">
                    <p>"Event Planner made organizing my wedding a breeze. Highly recommended!"</p>
                    <p className="author">- Emily Johnson</p>
                </div>
                <div className="testimonial">
                    <p>"I use Event Planner for all my corporate events. It saves me so much time and effort!"</p>
                    <p className="author">- John Smith</p>
                </div>
            </section>
            <section className="contact">
                <h2>Contact Us</h2>
                <form>
                    <input type="text" placeholder="Name" />
                    <input type="email" placeholder="Email" />
                    <textarea placeholder="Message"></textarea>
                    <button className="submit-button">Send</button>
                </form>
            </section>
        </div>
    );
};

export default EventPlanner;
```

---



## 🧪 Practice Exercise

Bu pratik alıştırmada, **EventPlanner.jsx** bileşenine dahil edilecek bir **footer component** oluşturacaksınız. Bunun yardımıyla, bileşenlerin bileşimi ( *composition* ) kavramını da anlamış olacaksınız.

---

## 📄 Footer.jsx Dosyasını Oluşturma

Bunun için **Components** klasörünü seçtikten sonra sağ tıklayın ve **New File** seçeneğini seçin. Bu yeni dosyanın adını **Footer.jsx** olarak verin. Bu işlem, Components klasörü içinde yeni bir bileşen oluşturacaktır.

---

## 🧩 Footer.jsx İçinde Function Component Temel Yapısını Oluşturma

**Footer.jsx** bileşeni içinde, önce function component için temel yerleşimi oluşturun.

İpucu: Bu yerleşimi oluşturmak için function component boiler plate kullanın.

```jsx
import React from 'react';
const Footer = () => {
        return (
    <>
    </>
)}

export default Footer
```

---

## 🦶 footer Etiketi Ekleyin

Bir `<footer>` etiketi oluşturun ve organizasyon hakkında görüntülemek istediğiniz herhangi bir bilgiyi ekleyebilirsiniz.

İpucu: `footer` etiketini kullanın ve `<p>`, `<div>` veya `<section>` gibi birden fazla etiket dahil edebilirsiniz.

```jsx
<footer>
<p>© Event Planner Organization. All rights reserved.</p>
</footer>
```

---

## 🧱 Footer Bileşenini EventPlanner.jsx İçine Dahil Etme

**EventPlanner.jsx** bileşeni içinde, `className="event-planner-container"` olan `div` etiketinin **en sonuna** Footer.jsx bileşenini ekleyin.

İpucu: Footer bileşenini parent EventPlanner bileşeninin en üst kısmında `import` anahtar sözcüğü ile child olarak dahil edin.

```jsx
import Footer from './Footer';
```

Footer bileşenini aşağıdaki gibi ekleyin:

```jsx
<Footer/>
```

---

## ✅ Çıktıyı Kontrol Etme

Uygulamayı tekrar çalıştırarak çıktıyı kontrol edin. Footer çıktısı, verilen ekran görüntüsüne göre görüntülenecektir.

> Not: En güncel değişiklikleri görmek için terminalde `npm run preview` komutunu tekrar çalıştırmanız gerekir.

---

## 🧩 EventPlanner.jsx Bileşeninin Tüm Kodu

```jsx
import React from 'react';
import './EventPlanner.css'; // Import CSS file for styling

import Footer from './Footer';
const EventPlanner = () => {
return (
    <div className="event-planner-container">
        <header>
            <h1>Welcome to Event Planner</h1>
        </header>
        <section className="description">
            <p>
                Plan and organize your events effortlessly with Event Planner. From
                birthdays to corporate meetings, we've got you covered.
            </p>
            <button className="get-started-button">Get Started</button>
         </section>
         <section className="events_categories">
            <ul>
                <h2>Social Events:</h2>
                <li>Birthday parties</li>
                <li>Anniversary celebrations</li>
                <li>Wedding receptions</li>
                <li>Baby showers</li>
                <li>Graduation parties</li>
                <li>Family reunions</li>
            </ul>
            <ul>
                <h2> Entertainment Events:</h2>
                <li>Concerts</li>
                <li>Music festivals</li>
                <li>Film screenings</li>
                <li>Comedy shows</li>
                <li>Art exhibitions</li>
                <li>Cultural events</li>
            </ul>
            <ul>
                <h2>Community Events:</h2>
                <li>Fundraising events</li>
                <li>Charity galas</li>
                <li>Volunteer drives</li>
                <li>Neighborhood block parties</li>
                <li>Community festivals</li>
                <li>Cultural celebrations</li>
            </ul>
        </section>
        <section className="features">
            <h2>Features</h2>
            <ul>
                <li>Easy event creation and management</li>
                <li>Customizable event templates</li>
                <li>Guest list management</li>
                <li>Real-time collaboration</li>
                <li>Reminders and notifications</li>
            </ul>
        </section>
        <section className="testimonials">
            <h2>Testimonials</h2>
            <div className="testimonial">
                <p>"Event Planner made organizing my wedding a breeze. Highly recommended!"</p>
                <p className="author">- Emily Johnson</p>
            </div>
            <div className="testimonial">
                <p>"I use Event Planner for all my corporate events. It saves me so much time and effort!"</p>
                <p className="author">- John Smith</p>
            </div>
        </section>
        <section className="contact">
            <h2>Contact Us</h2>
            <form>
                <input type="text" placeholder="Name" />
                <input type="email" placeholder="Email" />
                <textarea placeholder="Message"></textarea>
                <button className="submit-button">Send</button>
            </form>
        </section>
        <Footer/>
    </div>
   );
};

 export default EventPlanner;
```

---

## 🧩 Footer.jsx Bileşeninin Tüm Kodu

```jsx
import React from 'react';
const Footer = () => {
    return (
        <>
            <footer>
                <p>© Event Planner Organization. All rights reserved.</p>
            </footer>
        </>
    )}

export default Footer
```

---



## 🎉 Conclusion

Tebrikler! Üçüncü React uygulamanızı oluşturdunuz!

Bu lab’de, **EventPlanner** adlı bir bileşen oluşturarak React bileşenlerinden oluşan yapılandırılmış bir hiyerarşi oluşturmayı öğrendiniz.

Ek olarak, bir bileşene iletişim formu ekleyerek React’te form oluşturmayı öğrendiniz. Bu, `textarea` ve `input` alanları gibi form öğelerini bir **Send** düğmesiyle nasıl birleştireceğinizi gösterir.

Bu bileşende, etkinlik planlama uygulaması ve özellikleri hakkında bilgi vermek için başlıklar, paragraflar ve liste öğeleri gibi statik içerikler kullandınız.
