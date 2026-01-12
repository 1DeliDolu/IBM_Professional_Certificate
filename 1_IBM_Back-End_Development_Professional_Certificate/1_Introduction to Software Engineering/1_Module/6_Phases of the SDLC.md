
# 🔁 SDLC Aşamaları

Phases of the Software Development Life Cycle’a hoş geldiniz. Bu videoyu izledikten sonra SDLC’de yer alan phases’ların isimlerini söyleyebilecek, her phase’i açıklayabilecek ve her phase ile ilişkili bazı tasks’i tanımlayabileceksiniz.

Genel olarak SDLC sürecinde altı phase bulunur:  **planning, design, development, testing, deployment ve maintenance** .

Her phase  **discrete** ’tir; yani önceki phase’deki tasks, bir sonraki phase’deki tasks ile örtüşmez.

Orijinal SDLC, phases’ların linear olarak ilerlediği geleneksel **waterfall method** şeklinde tasarlanmıştı; ancak daha sonra değişen requirements’ı karşılayabilmek için **iteration** eklenerek uyarlanmıştır. Waterfall ve diğer software development yaklaşımları başka bir videoda ele alınacaktır. Ayrıca, bazı organizations her stage için farklı isimler kullanabilir.

Örneğin, “planning” bazı yerlerde “requirements” ya da “strategy” veya “analysis” olarak adlandırılabilir. Yine bazı organizations daha fazla veya daha az stage’e sahip olabilir.

---

## 🧠 Planning Phase

SDLC’nin ilk stage’i olan  **planning phase** ’de, requirements toplanır, analiz edilir, dokümante edilir ve önceliklendirilir.

Bir software solution planlanırken şu faktörler mutlaka dikkate alınmalıdır:

* Solution’ın users’ı
* Solution’ın genel amacı
* Data inputs ve outputs
* Legal ve regulatory compliance
* Risk identification
* Quality assurance requirements
* Human ve financial resources’ın allocation’ı
* Project scheduling

Planning process’in bir parçası olarak, labor ve material costs tahmin edilir ve time constraints ile karşılaştırılır. Ayrıca project teams belirlenir ve her team member’ın roles’u önerilir.

Eğer stakeholders, requirements’ı tanımlamakta zorlanıyorsa, çoğu zaman development team, bu requirements’ı netleştirmek için planning stage sırasında **prototypes** üretebilir.

Bir  **prototype** , stakeholder feedback almak ve requirements’ı belirlemek için kullanılan, end product’ın küçük ölçekli bir kopyasıdır. Prototype, temel design ideas’ı test etmek için kullanılır.

Her ne kadar **prototyping** genellikle planning stage’de gerçekleşse de, proje geliştikçe requirements yeniden gözden geçirilmeye veya netleştirilmeye ihtiyaç duyduğu her anda, SDLC’nin farklı phases’larında da prototyping yapılabilir.

Requirements toplandıktan sonra, bunlar **software requirements specification** ya da kısaca **SRS** document adı verilen bir dokümanda birleştirilir.

SRS, tüm stakeholders tarafından net bir şekilde anlaşılmalı ve onaylanmalıdır. Developers da bu stage’e dahil edilir; böylece bu requirements hakkında net bir anlayışa sahip olurlar.

Requirements ve SRS daha detaylı olarak ilerideki bir videoda ele alınacaktır.

---

## 🧱 Design Phase

 **Design phase** ’de, SRS’den elde edilen requirements, **software architecture** geliştirmek için kullanılır.

Bu aşamada birden fazla team member, architecture’ı design etmek için birlikte çalışır. Architecture, stakeholders ve team tarafından gözden geçirilir. Ve bu phase sırasında **prototypes** da design edilebilir.

Bir prototype, demonstration purposes için kullanılan system’in ya da system’in bazı parts’larının preliminary mock-up’ıdır.

Bu phase’de oluşturulan doküman **design document** olarak adlandırılır ve bir sonraki phase olan **development phase** sırasında developers tarafından kullanılır.

**Development phase** — bazen **“building” phase** veya **“implementation” phase** olarak da adlandırılır —, design document tamamlandıktan sonra developers’ın coding process’e başladığı aşamadır.

Project planners, design document’ı kullanarak coding tasks’i belirler ve assign eder.

Bu phase genellikle programming tools, farklı programming languages ve software stacks kullanımını gerektirir. Organizations’ın ayrıca uyulması gereken standards veya guidelines’ları da olabilir.

---

## 🧪 Testing Phase

Coding tamamlandıktan sonra süreçte sıradaki aşama  **testing phase** ’dir.

Bazı büyük projelerde, yalnızca testing’den sorumlu dedicated testing teams bulunur.

Code’un, stable ve secure olduğundan ve SRS’de belirtilen requirements’ı karşıladığından emin olmak için thoroughly tested edilmesi gerekir.

Testing  **manual** , **automated** veya ikisinin **hybrid** bir kombinasyonu olabilir.

Product bugs raporlanır, track edilir ve fix edilir; ardından software stable olana kadar code tekrar tekrar retest edilir.

Yaygın testing levels arasında **unit testing, integration testing, system testing ve acceptance testing** bulunur.

Bu testing levels’ın her biri başka bir videoda daha ayrıntılı olarak açıklanacaktır.

---

## 🚀 Deployment Phase

 **Deployment phase** , application’ın  **production environment** ’a release edildiği ve users için kullanılabilir hâle getirildiği aşamadır.

Bu süreç de stages hâlinde gerçekleşebilir:

Önce application, **user acceptance testing (UAT)** platformuna release edilir ve customer, functionality’yi onayladıktan sonra production’a release edilir.

Bu approach; software’in bir **website** üzerinden, bir **mobile device app store** üzerinden veya bir **corporate network** üzerindeki **software distribution server** aracılığıyla kullanılabilir hâle getirilmesi için kullanılabilir.

---

## 🔧 Maintenance Phase

Son olarak,  **maintenance phase** , code production environment’a deploy edildikten sonra gerçekleşir.

Bu phase, başka bugs olup olmadığını bulmaya, **user interface** (kısaca  **UI** ) issues’larını belirlemeye ve SRS’de listelenmemiş olabilecek diğer requirements’ı tespit etmeye yardımcı olur.

Ayrıca bu aşamada code enhancements da belirlenebilir.

Eğer bu phase’de, testing sırasında gözden kaçmış bugs keşfedilirse, bu errors, high-priority issues için hemen fix edilmek zorunda olabilir veya future software release’in bir parçası olarak requirements’a dahil edilebilir ve process baştan başlayabilir.

---

## 📌 Özet

Bu videoda şunları öğrendiniz:

* SDLC, altı phase’e ayrılabilir.
* **Planning** , requirement gathering ve SRS’in geliştirilmesini içerir.
* **Design phase** sırasında architecture geliştirilir ve **design document** oluşturulur.
* **Development phase** ’de coding yapılır ve ardından  **testing phase** ’de code ile ilgili issues bulunur ve mümkünse fix edilir.
* **Deployment** , code’un production environment’a release edildiği aşamadır.
* Son olarak  **maintenance stage** ’de stakeholders’tan feedback toplanır, diğer UI issues tespit edilebilir ve code enhancements önerilir.

  Ve gerekirse bu bilgiler, yeni bir software development cycle’a geri beslenebilir.
