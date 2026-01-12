# 📦 Behave ile Test Verisi Yükleme

Bu videoyu izledikten sonra, Behave kullanırken test verisinin nasıl yükleneceğini açıklayabileceksiniz. Test case’ler çoğu zaman test verisine ihtiyaç duyar. Neyse ki, Behave için test verisini doğrudan özellik ( *feature* ) dosyanızda **Background** bölümünü kullanarak belirtmenin basit bir yolu vardır.

**Background** içinde, başlangıçta sahip olmak istediğiniz verinin ilk durumunu ( *initial state* ) belirtebilirsiniz. Tek sorun, verinin kendiliğinden yüklenmemesidir; onu manuel olarak yüklemeniz gerekir. “Bunu nasıl yaparım?” diye sorabilirsiniz.

Şanslısınız ki Behave veriyi *context* içinde **table** adlı bir değişkene koyar. Bu, *context.table* üzerinde dolaşıp ( *iterate* ) veriyi çıkarabileceğiniz anlamına gelir.

---

## 🧱 Background Tablosu ile Veri Tanımlama

Bunu nasıl yaptığınıza bakalım. Bir örnek özellik üzerinden başlayacağız: kategoriye göre evcil hayvan arama ( *search for pets by category* ) özelliği.

Bu özelliğin, “ **Given the following pets** ” diyen bir **Background** bölümü olduğunu ve dikey çizgilerle ( *vertical bars* ) sınırlandırılmış bir evcil hayvan tablosu içerdiğini fark edin.

Bu tablonun ilk satırı sütun adlarını içerir:

* **name**
* **category**
* **available**

Behave bunları *context.table* içine yüklediğinde, tablodaki her satır **name** anahtarı, **category** anahtarı ve **available** anahtarı olan bir Python sözlüğü ( *dictionary* ) olur. Dolayısıyla veriyi sütun adlarını kullanarak tablodan çekebilirsiniz. Tablonun geri kalanı *context.table* içine yüklenen veridir.

Her satır, o satıra ait veriyi içeren bir sözlük olacaktır.

---

## 🧩 Steps Dosyasında Veriyi Yüklemek için Kod

Veriyi yüklemek için adımlar ( *steps* ) dosyanızda gerekli koda bakalım.

Önce, “ **the following pets** ” string’i ile **given**  *decorator* ’ına başlarsınız. Bu satır, özellik dosyasındaki “ **Given the following pets** ” ifadesiyle eşleşir.

Ardından bu adımı uygulamak için bir fonksiyon tanımlar,  *context* ’i parametre olarak geçirir ve uygun bir *docstring* eklersiniz.

Şimdi, bir **for** döngüsü kullanarak *context.table* üzerinde dolaşmak istersiniz. Bu döngü size tablodaki her satırı, **row** adlı bir sözlük olarak geri verir.

---

## 🧾 payload Sözlüğünü Oluşturma

Sonraki adımda **payload** adlı bir değişken oluşturursunuz. *payload* da bir Python sözlüğüdür ve onu tablodaki sütunlarla doldurmaya başlarsınız.

Önce **name** adlı bir anahtar oluşturursunuz. Değer olarak, mevcut satırdaki ( *current row* ) **name** anahtarına sahip veriyi atarsınız.

Aynı yaklaşımı **category** için de kullanırsınız. **category** adlı bir anahtar oluşturur ve mevcut satırda **category** anahtarına sahip veriyi atarsınız. Oldukça basittir.

---

## 🔁 available Alanını Boolean’a Çevirme

**available** biraz farklıdır çünkü bir Boolean’dır: evcil hayvan müsaitse “ **True** ”, değilse “ **False** ”.

Bu yüzden tablo verisini string’den Boolean’a dönüştürmeniz gerekir. **available** adlı bir anahtar oluşturursunuz. Ardından mevcut satırdan **available** anahtarına sahip veriyi atarsınız, fakat burada durmazsınız.

Bu veriyi; büyük T ile  **True** , tamamen küçük harfli **true** ve **1** sayısını içerecek şekilde değerlendirirsiniz. Başka bir deyişle, bu string’lerden herhangi biri Boolean **True** olarak değerlendirilir ve *available* değerini **True** yapar.

Artık *payload* sözlüğünüzde  **name** , **category** ve **available** verisi vardır ve bununla bir pet oluşturmanız gerekir.

---

## 🌐 REST API ile Pet Oluşturma

Test ettiğiniz sunucudan uzak ( *remote* ) olduğunuz için sunucunun REST API’sine bir HTTP isteği yapmanız gerekir.

Bunu yapmak için, servisinizin REST API’sine bir **post** isteği göndererek bir pet oluşturursunuz. İlk argüman, *context* içindeki base URL ile başlayan ve sonuna **/pets** eklenen bir string’dir.

**/pets** kullanırsınız çünkü RESTful bir API’de pet oluşturma endpoint’i budur.

İkinci argüman olarak **json=payload** belirtirsiniz; bu da *payload* adlı Python sözlüğünü REST API’ye JSON string’i olarak gönderir.

Bu post isteğinin yanıtını ( *response* ) *context* içine kaydettiğinize dikkat edin; böylece gerekirse diğer adımlar onu inceleyebilir.

Son olarak, yanıttaki status code’un **201** olduğunu doğrularsınız; bu, REST API için başarılı bir oluşturma ( *successful creation* ) status code’udur.

![1765977018323](image/14_LoadingTestDatawithBehave/1765977018323.png)

---

## 🧠 Özet

Tüm bu kod, Background bölümündeki bir tabloyu kullanarak veritabanlarını test verisiyle doldurmanın sadece bir örneğidir.

Bu videoda şunları öğrendiniz:

* Background içinde, testte kullanmak istediğiniz veriyi belirtmek için bir tablo kullanabilirsiniz.
* Behave bu tablo verisini **context.table** adlı bir değişkene koyar.
* Veriyi çıkarmak ve yüklemek için, bir **for** döngüsü kullanarak *context.table* üzerinde dolaşabilirsiniz.
