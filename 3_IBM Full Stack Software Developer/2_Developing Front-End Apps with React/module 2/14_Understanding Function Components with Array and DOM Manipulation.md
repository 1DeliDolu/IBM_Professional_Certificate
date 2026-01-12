## 📚 Module 2 Glossary: Understanding Function Components with Array and DOM Manipulation

Hoş geldiniz! Bu alfabetik sözlük, bu kurs boyunca karşılaşacağınız terimlerin birçoğunu içerir. Bu kapsamlı sözlük ayrıca kurs videolarında kullanılmayan, sektörde kabul görmüş ek terimleri de içerir. Bu terimler, sektörde çalışırken, kullanıcı gruplarına katılırken ve diğer sertifika programlarına katılırken tanımanız gereken önemli kavramlardır.

---

## 🧾 Terim — Tanım

**Abstraction principle** — UI özelliklerini kapsülleyen yeniden kullanılabilir bileşenler oluşturmak için bir yol sağlayan ilke.

**Array** — JavaScript’te birden fazla değeri tek bir değişkende saklamak için kullanılan veri yapısı.

**Array destructuring** — Bir diziden değerleri çıkarıp bunları tek tek değişkenlere atamanızı sağlayan özellik.

**Array literal** — JavaScript’te diziler oluşturmak için kullanılan sözdizimi. Virgülle ayrılmış eleman listesini köşeli parantez içine alarak dizi tanımlamanıza olanak tanır.

**Attributes** — Elementler hakkında ek bilgi sağlar. Özellikleri, stilleri veya davranışı belirtebilir.

**Component composition** — Daha karmaşık işlevsellik oluşturmak için birden fazla küçük bileşenin bir araya getirilmesi.

**Document object model (DOM)** — Bir HTML yapısını ağaç benzeri bir yapı olarak temsil etmek için kullanılan, web sayfaları ve belgeler için bir arayüz.

**Elements** — HTML belgelerinin yapı taşlarıdır.

**forEach()** — Bir dizinin her elemanı üzerinde dolaşan ve bir callback fonksiyon çalıştıran metot.

**Hierarchy principle** — Bileşenleri parent ve child bileşenler ile bir hiyerarşi içinde düzenlemenizi sağlayan ilke.

**Higher-order component** — Bir bileşenin uygulamasını değiştirmeden, state management veya logic gibi özellikler eklemenizi sağlayan fonksiyon.

**Hook** — Bileşen hiyerarşisini değiştirmeden veya gereksiz nesting eklemeden, kod mantığını bileşenler arasında yeniden kullanmanızı sağlayan fonksiyon.

**Initialization** — React’in functional component’in fonksiyon gövdesini çalıştırdığı; bileşenin başlangıç yapısını ve davranışını kurduğu adım.

**map()** — Bir dizinin her elemanı üzerinde dolaşıp React elemanlarından oluşan yeni bir dizi döndürmek için yaygın kullanılan metot.

**Mounting phase** — React’in functional component’i başlattığı ve DOM üzerinde render edilmeye hazırladığı lifecycle aşaması.

**Props Default** — `defaultProps` kullanarak props için varsayılan değer tanımlanmasıdır. Bir prop sağlanmadığında bileşenin varsayılan değer ile render edilmesini sağlar; böylece bileşen davranışının öngörülebilirliğini ve sağlamlığını artırır.

**Properties (props)** — React’te parent component’ten child component’e veri aktarmak için temel bir kavramdır. React uygulamasının farklı parçaları arasında iletişimi ve özelleştirmeyi sağlar.

**Rendering Array** — Dizinin içeriğine göre elemanları dinamik olarak üretme ve görüntüleme işlemidir. Bu genellikle JavaScript’in `map()` fonksiyonu kullanılarak yapılır; her öğe için React elemanları oluşturulur.

**Reuse principle** — Kod parçalarını yeniden kullanmayı sağlayan; organizasyonu ve bakımı kolaylaştıran ilke.

**Side effects** — Boş dependency array ile `useEffect` hook’u kullanarak yapılan data fetching, subscriptions veya DOM manipülasyonu gibi adımları kapsar.

**State** — Bir bileşenin belirli bir zamandaki durumudur ve nesnenin davranışını etkileyen bilgiyi tutar; bu bilgiye göre render edilmesini sağlar.

**State management** — Verinin zaman içinde ele alınması ve güncellenmesini içerir; bileşenlerin kullanıcı aksiyonlarına veya diğer event’lere yanıt olarak görünümünü ve davranışını dinamik biçimde değiştirmesini sağlar.

**State initialization** — React’in `useState` hook’unu kullanarak bileşen içinde state değişkenlerini bildirdiği ve başlangıç değerlerini atadığı adım.

**Updating phase** — React’in bileşenin state veya props değişikliklerine yanıt vererek bileşenin fonksiyon gövdesini yeniden çağırdığı lifecycle aşaması.

**Unmounting phase** — React’in bir bileşeni DOM’dan kaldırırken cleanup işlemlerini yürüttüğü lifecycle aşaması.

**useState hook** — Functional component’lerin state yönetmesini sağlayan yerleşik ( *built-in* ) React Hook’udur. State değişkenlerini bildirmeyi ve güncellemeyi sağlar. State değiştiğinde React otomatik olarak bileşeni yeniden render eder ve güncellenmiş state’i yansıtır.

**Virtual DOM** — Bellekte uygulanmış gerçek DOM’un bir soyutlamasıdır ve React’in *reconciliation* süreci ile gerçek DOM ile senkron tutulur.
