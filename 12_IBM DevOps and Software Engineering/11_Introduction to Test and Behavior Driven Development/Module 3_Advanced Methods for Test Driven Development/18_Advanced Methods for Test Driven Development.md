## 🧩 Module Summary: Test Güdümlü Geliştirme için İleri Yöntemler

Tebrikler! Bu modülü tamamladınız. Kursun bu noktasında şunları biliyorsunuz:

* Test kapsamı ( *test coverage* ) ne kadar yüksekse, geliştiriciler kodlarının beklendiği gibi çalıştığından o kadar emin olabilir.
* Eksik test kapsamı raporları, geliştiricilerin hâlâ test vakalarına ihtiyaç duyan kod satırlarını belirlemesine yardımcı olabilir.
* *Factory* ve *fake* yapıları, büyük miktarda test verisi oluşturmak ve sürdürmek için faydalıdır.
* *Factory* yapıları, gerçekçi test verileriyle *fake* üretir.
* *Fake* nesneler, test sırasında gerçek nesneler gibi davranır; bu nedenle geliştiriciler  *fake* ’leri gerçek veriyi test eder gibi test eder.
* *Mocking* , gerçek nesnelerin davranışını taklit eden nesneler oluşturma sürecidir.
* Geliştiriciler, testleri uzak bir bileşenden veya harici bir sistemden izole etmek istediklerinde *mock* kullanmalıdır.
* *Patching* , geliştiricilerin bir fonksiyon çağrısının davranışını değiştirdiği bir *mocking* tekniğidir.
* Python’un *mock* kütüphanesi iki *patching* tekniği sağlar:
  * Bir fonksiyonun dönüş değerini ( *return value* ) patch’lemek
  * Bir fonksiyonu başka bir fonksiyonla değiştirmek (*side effect* tekniği)
* *Mock object* ’ler, davranışlarını kontrol edebileceğiniz şekilde gerçek nesnelerin davranışını taklit eden nesnelerdir.
* Bir *Mock* veya *MagicMock* nesnesinin belirli bir nesneyi taklit etmesi için, `spec` parametresinde gerçek nesnenin adını belirtin.
* TDD, tek bir kod satırı yazmadan önce uygulamanın gereksinimlerine odaklanmanızı sağlar.
* TDD iş akışı, ileri-geri ilerleyen bir süreçtir.
