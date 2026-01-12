# 📋 Gereksinimler

Requirements’a hoş geldiniz. Bu videoyu izledikten sonra şunları yapabileceksiniz: Requirement gathering sürecinin adımlarını açıklamak, User Requirement Specification (URS) document’in amacını açıklamak, Software Requirement Specification (SRS) document’in amacını açıklamak ve System Requirement Specification (SysRS) document’in amacını açıklamak.

Requirement gathering, çözülecek bir problemi tanımlama ve bu problemi nasıl çözeceğimizi dokümante etme sürecinden oluşan altı adımlı bir süreçtir. Bu adımlar şunlardır:

* Stakeholders’ı belirlemek,
* Goals ve objectives belirlemek,
* Stakeholders’dan requirements’ı eliciting etmek,
* Requirements’ı documenting,
* Requirements’ı analiz edip doğrulamak (confirming),
* Ve requirements’ı prioritizing.

Genel olarak stakeholders, software product’ın geliştirilmesini talep eden organization için çalışır. Organization içindeki kilit personel; decision-makers, end-users, system administrators, engineering, marketing, sales ve customer support personnel olabilir.

Üründen etkilenen her gruptan bir temsilciye sahip olmak faydalıdır.

Product’ın goals’ları açıkça tanımlanmalıdır. Goals, geniş kapsamlı, uzun vadede ulaşılabilir outcomes’tır. Goals, customer outcomes ve business goals’u içerebilir.

Sonraki adımda objectives belirlenmelidir. Objectives, goals’tan daha spesifik, stated goals’a ulaşmayı sağlayan actionable ve measurable actions’tır.

Sonraki üç adım — eliciting, documenting ve requirement confirmation — genellikle iterative olarak tamamlanır.

 **Elicitation** , surveys, questionnaires ve interviews yoluyla gerçekleştirilebilir. Requirements ortaya çıktıkça, bunlar documented edilmeli ve goals ve objectives ile uyumlu olup olmadıkları kontrol edilmelidir.

Documented requirements, stakeholders ve project team tarafından kolayca anlaşılabilir olmalıdır. Requirements’ı confirm etmek için; consistency, clarity ve completeness açısından analiz edilmeleri gerekir. Analizden sonra requirements, stakeholders ile paylaşılmalı ve onların onayına sunulmalıdır.

Confirmation’dan sonra requirements, prioritized edilmelidir. “Must-have”, “highly desired” ve “nice to have” gibi etiketler yardımcı olur. Mümkünse, her kategori içindeki requirements’ı da sıralayın.

Requirement gathering sürecinden genellikle üç doküman ortaya çıkabilir:

* Software Requirements Specification (SRS),
* User Requirements Specification (URS),
* System Requirements Specification (SysRS).

Bunlar arasında en yaygın olanı  **software requirements specification** ’dır.

 **Software requirements specification (SRS)** , software’in yerine getirmesi gereken functionalities’i yakalayan ve ayrıca performance için benchmarks veya service levels belirleyen bir document’tir.

Bir SRS’in bölümleri şunları içerebilir:

* SRS’in intended use’unu, audience ve scope’unu içeren bir purpose statement,
* Constraints, assumptions ve dependencies,
* Ve dört kategoriye ayrılabilen requirements:
  * Functional requirements
  * External Interface requirements
  * System Features
  * Non-functional requirements

Product’ın purpose’ı, SRS’e kimin erişeceğini ve onu nasıl kullanması gerektiğini açıklar. Scope ise software’in benefits’ini, goals ve objectives’ını açıklar.

SRS’in ikinci kısmı, constraints, assumptions ve dependencies’i detaylandırmalıdır.

* **Constraints** , product’ın, design phase’deki seçenekleri sınırlayabilecek belirli koşullar altında nasıl çalışmak zorunda olduğunu açıklar; örneğin belirli standards’a uyum veya hardware limitations.
* **Assumptions** , software’in çalışması için gereken operating system veya hardware gibi unsurları içerebilir.
* Diğer software products’a olan dependencies de not edilmelidir.

Requirements dört kategoriye ayrılabilir:

* **Functional requirements** , software’in functionalities’ini kapsayan requirements’tır.
* **External requirements** , software’in users gibi external entities ve diğer hardware veya software ile etkileşimi bağlamındaki davranışını ele alan requirements’tır.
* **System features** , functional requirements’ın bir subset’idir. Bunlar, system’in çalışması için gerekli features’tır.
* Ayrıca performance, safety, security ve quality standards gibi konuları belirten **non-functional requirements** da vardır.

 **User requirements** , business need’i ve end-users’ın software system’den beklentilerini açıklar. User requirements, üç soruya cevap veren “user stories” veya “use cases” şeklinde yazılır:

1. User kimdir?
2. Hangi function’ın yerine getirilmesi gerekir?
3. User bu functionality’yi neden istemektedir?

User acceptance testing, bu requirements’ın karşılanıp karşılanmadığını belirler. Çoğu zaman user requirements ve software requirements, tek bir SRS document içinde birleştirilir.

SRS, software system’e dair expectations’ı detaylandırır.

**System Requirement Specification (SysRS)** document, SRS’ten ayırt etmek için, tüm bir system’in requirements’ını açıkça ortaya koyar. System requirement specification çoğu zaman software requirement specification ile birbirinin yerine kullanılır; ancak SysRS, kapsam olarak SRS’ten daha geniştir.

Birçok software projesi SysRS yerine SRS geliştirir.

SysRS; system capabilities, interfaces ve user characteristics içerir. Ayrıca policy requirements, regulation requirements, personnel requirements, performance requirements, security requirements ve system acceptance criteria’yı da içerebilir. SysRS, software requirements’a ek olarak system için gereken hardware’e dair expectations’ı da açıklar.

Bu videoda şunları öğrendiniz:

* Requirement gathering process; stakeholders’ı belirlemeyi, goals ve objectives oluşturmayı ve requirements’ı eliciting, documenting, confirming ve ardından prioritizing etmeyi içerir.
* SRS, functional, external, system ve non-functional requirements’ı dokümante eder.
* URS, user stories’i dokümante eder.
* Ve son olarak SysRS; system capabilities ve acceptance criteria’yı, ayrıca policy, regulation, personnel, performance, security ve hardware requirements’ı dokümante eder.
