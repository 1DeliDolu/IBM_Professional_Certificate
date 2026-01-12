# 🏗️ Nitelikli Yazılım Geliştirme

Building Quality Software’a hoş geldiniz. Bu videoyu izledikten sonra: yaygın software engineering processes’ı listeleyebilecek ve yüksek kaliteli software geliştirmek için gerekli common software engineering processes’ı açıklayabileceksiniz.

Bu videoda, software engineering projelerinde yaygın olan çok sayıda process’ten altısını ele alacağız:  **requirements gathering, design, coding for quality, testing, releases ve documenting** .

 **Software requirements specification (SRS)** , software’in uyması gereken requirements set’inin toplanması ve dokümante edilmesi sürecini kapsar.

SRS, software’in implement etmesi gereken business needs ve user flows’u tanımlayan bir dizi use case içerebilir.

Software requirements genel olarak dört geniş kategoriye ayrılabilir:

* **functional** ,
* **external and User Interface (UI)** ,
* **system features** ,
* **non-functional** .

Bu kategoriler başka bir videoda daha detaylı tartışılacaktır.

---

## 🧩 Design

Software design, requirements’ı code kullanılarak implement edilebilir bir yapıya dönüştürme sürecidir.

Software design process, requirements’ı developers’ın code yazmak için kullanabileceği bir dile çevirir.

Başka bir deyişle, requirements’ı bir software solution’a dönüştürür.

Technical lead, requirements’ı net tanımlanmış behaviors, boundaries ve interactions’a sahip ilgili components set’lerine böler. Bu components, system architecture’ı tanımlar.

System design; system functions, performance, security ve platform characteristics hakkında yönlendirme içerir.

Design ayrıca şu konuları da iletir:

* Business rules ve application logic,
* Application programming interface design (apps’in birbirleriyle veya database ile nasıl konuştuğu),
* User interfaces,
* Database design.

---

## ✅ Coding for Quality

Code quality, code’un sahip olduğu maintainability, readability, testability ve security gibi özellikleri ifade eder.

Quality code, software’in amaçlanan requirements’ını defects olmadan karşılamalıdır. Buna ek olarak:

* clean ve consistent olmalı,
* okunması ve maintenance’ı kolay olmalı,
* iyi dokümante edilmiş olmalı,
* efficient olmalıdır.

 **Coding for quality** , development sırasında belirli coding practices set’ini takip etmeyi gerektirir. Bunlara şunlar dahildir:

* Common coding standards, conventions, patterns ve styles’ı takip etmek,
* Programmatic ve stylistic errors’ı tespit etmek için *linters* olarak bilinen automated tools kullanmak,
* Başkalarının code’u anlamasını ve değiştirmesini kolaylaştırmak için code içine comments eklemek.

---

## 🧪 Testing

Software testing, software’in belirlenmiş requirements ile eşleştiğini ve bugs içermediğini doğrulama sürecidir.

Amacı, stated requirements ile karşılaştırıldığında errors, gaps veya missing requirements’ı tespit etmektir.

Doğru şekilde test edilmiş software; reliability, security, performance ve efficiency sağlar.

Software testing çoğu zaman automated veya manual olarak yapılabilir.

Testing levels şunları içerir:

* **unit** ,
* **integration** ,
* **system** ,
* **user acceptance** .

Unit testing genellikle developer tarafından yapılır ve system’in geri kalanından izole edilebilen en küçük code component’ini test eder.

Components, daha büyük product’a integrate edildikten sonra **integration testing** yapılır.

Daha büyük product completed kabul edildikten sonra **system testing** gerçekleşebilir.

 **User acceptance testing (UAT)** , bazen **beta testing** olarak da adlandırılır ve software’in intended end user tarafından test edilmesi anlamına gelir.

Testing types, genel olarak üç kategoriye ayrılabilir:

* **functional** ,
* **non-functional** ,
* **regression** .

Testing levels ve types, gelecek bir videoda daha ayrıntılı olarak açıklanacaktır.

---

## 📦 Releases

Software’in en yeni versiyonu dağıtıldığında, buna **release** denir.

Farklı releases, farklı audiences için tasarlanır. Genellikle  **alpha** , **beta** ve **GA** release vardır.

 **GA** , *general availability* anlamına gelir.

* **Alpha release** , system’in ilk çalışan versiyonudur ve seçilmiş bir stakeholder grubuna dağıtılır.
* Muhtemelen errors içerir ve tüm feature set’i içermeyebilir, ancak istenen functionality’nin çoğunu barındırır.
* Bu stage sırasında hâlâ design changes oluşabilir.
* **Beta release** , **limited release** olarak da adlandırılır ve developing organization dışındaki stakeholders’a verilir.
* Beta release’in amaçlarından biri, software’i gerçek koşullar altında denemek, functionality’yi test etmek ve outstanding bugs veya errors’ı tespit etmektir.
* Beta release, tüm functional requirements’ı karşılamalıdır.

Beta release sonrası agreed-upon changes yapılıp test edildikten sonra, stable version release edilir.

 **GA release** ’in audience’ı  **tüm users** ’tır.

---

## 📚 Documenting

Software documentation, hem non-technical end-users’a hem de technical users’a sağlanmalıdır.

 **System documentation** , technical user’a yöneliktir. Technical users, diğer engineers, developers veya architects olabilir.

System documentation, software’in nasıl çalıştığını veya nasıl kullanılacağını açıklar ve şunlardan oluşur:

* README files,
* Inline comments,
* Architecture ve design documents,
* Verification information,
* Maintenance guides.

**User documentation** ise non-technical end-users’a ürünün kullanımında yardımcı olmak için sağlanır.

Genellikle şu biçimlerde sunulur:

* User guides,
* Instructional videos ve manuals,
* Online help,
* Inline help.

Documentation hakkında daha fazla detay başka bir videoda ele alınacaktır.

---

## 🧷 Özet

Bu videoda şunları öğrendiniz:

* **Requirement gathering** , software’in uyması gereken requirements set’inin toplanması ve dokümante edilmesidir.
* **Designing** , requirements’ı developers’ın kullanabileceği bir structure’a dönüştürür.
* **Coding for quality** , development sırasında belirli coding practices set’ini takip etmeyi gerektirir.
* **Testing** , software’in belirlenmiş requirements ile eşleştiğini ve bugs içermediğini doğrulama sürecidir.
* Üç tür release vardır:  **alpha** , **beta** ve  **general availability (GA)** .
* Son olarak,  **documenting** , software’i technical ve non-technical users’a açıklayan text veya video gerektirir.
