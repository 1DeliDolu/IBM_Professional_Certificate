## 🧩 JSX’e Giriş

JSX’e Giriş’e hoş geldiniz. Bu videoyu izledikten sonra, JSX’in amacını açıklayabilecek, JSX sözdizimini tanımlayabilecek, JSX’in neden derlenmesi gerektiğini açıklayabilecek ve JSX’in faydalarını özetleyebileceksiniz.

![1768053928353](image/7_IntroductiontoJSX/1768053928353.png)

---

## 🧠 JSX’in Amacı

Özünde JSX, JavaScript’i HTML ile birleştirir.

JSX, kullanıcı arayüzleri oluşturmayı daha kavramsal hale getirir.

HTML’e benzer şekilde okunur; aynı zamanda JavaScript ifadelerini de destekler.

JSX,  **JavaScript Syntax Extension** ’ın kısaltmasıdır ve **JavaScript XML** olarak da adlandırılır.

![1768053944482](image/7_IntroductiontoJSX/1768053944482.png)

---

## 🧾 JSX Sözdizimi

JSX sözdizimi, kullanıcıya ekranda nasıl görüneceklerini belirtmek için köşeli parantezler içinde (angle brackets) yer alan öğeler kullanarak XML ya da HTML gibi görünür.

![1768053970374](image/7_IntroductiontoJSX/1768053970374.png)

Şimdi bazı örnek JSX kodlarına bakalım.

Kod, “This is a sample JSX code snippet” başlığını görüntüleyen bir yapıyı gösterir.

Kod parçası HTML’e benzer, ancak HTML de olmayan JavaScript benzeri bir değişkene dikkat edin.

Bu ne HTML’dir ne de JavaScript’tir.

Bu JSX’tir.

React elementleri oluşturmak için JSX sözdizimini kullanırsınız.

React daha sonra bu elementleri **document object model** ya da  **DOM** ’a render eder.

![1768054005385](image/7_IntroductiontoJSX/1768054005385.png)

---

## 🛠️ JSX Neden Derlenmelidir

Tarayıcılar JSX’i anlamaz; bu nedenle JSX kodunuzu derlemek ve onu standart JavaScript nesnelerine dönüştürmek için **Babel** kullanmanız gerekir.

JavaScript motoru daha sonra bu nesneleri ayrıştırır.

Neyse ki, derlemeyi yönetmek için `create react app` komutunu kullanabilirsiniz.

![1768054030557](image/7_IntroductiontoJSX/1768054030557.png)

---

## ✅ JSX Kullanmanın Faydaları

JSX kullanmanın bazı faydalarını tartışalım.

Başlangıç olarak, JavaScript ya da diğer programlama dillerini bilmeyen kişiler bunu daha kolay anlayabilir ve üzerinde değişiklik yapabilir.

HTML gibi markup dilleri kullanan kişiler, JSX’i yalnızca JavaScript kullanmaktan daha tanıdık bulacaktır.

JSX’inizi dönüştürmek için bir compiler kullandığınızda, aksi halde fark etmesi zor olabilecek hataları daha erken bulursunuz.

JSX, inline stilleri kullanmasıyla kodu basit ve zarif tutmaya yardımcı olur.

JSX, JavaScript’ten daha iyi performans gösterir çünkü JavaScript’e çeviri sırasında optimizasyon yapar.

Son olarak, JSX çıktı sanitasyonu ile ilgili sorunları otomatik olarak ele alır; örneğin ifadeleri string’e dönüştürür ve render edilmeden önce saldırganların çalıştırılabilir bir script gömmesini engeller.

![1768054070180](image/7_IntroductiontoJSX/1768054070180.png)

---

## ⚛️ JSX ile React Bileşeni Örneği

Şimdi JSX kullanan bir React bileşeninin koduna bakın.

Bunu normal bir JavaScript fonksiyon çağrısıyla karşılaştırın.

Bu kod, “items number 1 and 2” öğelerini görüntüleyen iki maddelik bir listeyle birlikte bir `div` elementi oluşturur.

`app` fonksiyonu, düz HTML’e son derece benzeyen ve aynı XML tabanlı sözdizimini kullanan kod içerir.

![1768054112462](image/7_IntroductiontoJSX/1768054112462.png)

Bu örnek, önceki kodun JavaScript fonksiyon çağrılarıyla yazılmış halini gösterir.

Bu kodun okunmasının daha zor olduğunu, mantığını anlamanın güçleştiğini, ayrıca çirkin ve bakımının zor olduğunu görebilirsiniz.

JSX, HTML’in güzelliğini JavaScript’in gücüyle birleştirir.

![1768054126050](image/7_IntroductiontoJSX/1768054126050.png)

---

## ✅ Özet

Bu videoda, JSX’in HTML’e benzer şekilde okunduğunu öğrendiniz.

JSX, JavaScript ifadeleriyle birleştirilmiş HTML öğeleri kullanır.

JSX, HTML benzeri metni standart JavaScript nesnelerine dönüştürmek için compiler’lara dayanır.

JSX kullanmanın faydaları arasında kolay okunabilir kod, hata tespiti, daha iyi performans ve ek güvenlik yer alır.

![1768054154706](image/7_IntroductiontoJSX/1768054154706.png)
