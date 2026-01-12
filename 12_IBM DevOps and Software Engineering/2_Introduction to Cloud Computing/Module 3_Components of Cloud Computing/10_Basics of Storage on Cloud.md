# 💾 Bulutta Depolamanın Temelleri

Bulut depolama, veri dosyalarını bulutta kaydettiğiniz yerdir. Bazı depolama türlerinin depolamaya erişilebilmesi için önce bir *hesaplama düğümüne* (compute node) eklenmesi gerekirken, diğer depolama türlerine doğrudan genel İnternet üzerinden veya adanmış bir özel ağ bağlantısı üzerinden erişilebilir. Bulut sağlayıcıları, ihtiyaç duyduğunuzda verilerinize erişebilmenizi sağlamak için bulut depolamayı ve ilişkili altyapıyı barındırır, güvenliğini sağlar, yönetir ve bakımını yapar.

Bulut depolama hizmetleri, kapasitenizi ihtiyacınıza göre ölçeklendirmenize olanak tanır; böylece genellikle “ *gigabayt başına* ” esasına göre yalnızca tahsis ettiğiniz kadar ödersiniz. Depolamanın maliyeti türe göre değişir; ancak genel olarak, depolamanın okuma/yazma hızı ne kadar yüksekse gigabayt başına maliyeti de o kadar yüksektir.

Bulut depolama dört ana türde mevcuttur:  **Doğrudan Bağlı (Direct Attached)** ,  **Dosya Depolama (File Storage)** , **Blok Depolama (Block Storage)** ve  **Nesne Depolama (Object Storage)** .

---

## 🧩 Doğrudan Bağlı Depolama

Doğrudan bağlı depolama, bazen *“Yerel Depolama”* ( *Local Storage* ) olarak adlandırılır; bulut tabanlı bir sunucuya doğrudan sunulan ve fiilen ya ana sunucu kasası içinde ya da aynı raf (rack) içinde bulunan depolamadır.

Bu depolama hızlıdır ve normalde yalnızca bir sunucunun işletim sistemini depolamak için kullanılır; ancak başka kullanım senaryoları da olabilir. Doğrudan bağlı depolamanın, işletim sistemini depolamanın dışında diğer kullanımlar için çok iyi olmamasının iki ana nedeni şunlardır: Genellikle *“Geçici”* ( *Ephemeral* ) olması — yani yalnızca bağlı olduğu hesaplama kaynağı var olduğu sürece sürmesi — diğer düğümlerle paylaşılamaması ve RAID tekniklerini kullanabilseniz de diğer depolama türlerine kıyasla arızalara karşı o kadar dayanıklı olmamasıdır.

---

## 📁 Dosya Depolama

Dosya depolama, genellikle hesaplama düğümlerine *“NFS Depolama”* ( *NFS Storage* ) olarak sunulur.  *NFS* , *Network File System* anlamına gelir ve depolamanın standart bir ethernet ağı üzerinden hesaplama düğümlerine bağlandığı anlamına gelir.

NFS ile bağlanan depolama yaygındır; ancak veriler ethernet ağı üzerinden taşındığı için, genellikle doğrudan bağlı depolama veya blok depolamadan daha yavaştır. Ayrıca, doğrudan bağlı depolama veya blok depolamaya kıyasla daha düşük maliyetli olma eğilimindedir. Dosya depolamanın bir avantajı, aynı anda birden fazla sunucuya bağlanabilmesi veya birden fazla sunucuda kullanılabilmesidir.

Dosya tabanlı depolama, basit ve doğrudan bir veri depolama yaklaşımıdır ve masaüstü kullanıcılarının aşina olduğu hiyerarşik bir klasör yapısı içinde verileri düzenlemek için iyi çalışır.

---

## 🧱 Blok Depolama

Blok depolama, hesaplama düğümlerine yüksek hızlı fiber bağlantılar kullanılarak sunulur; bu da okuma ve yazma hızlarının genellikle dosya depolamaya göre çok daha hızlı ve güvenilir olduğu anlamına gelir. Bu durum, blok depolamayı veritabanları ve disk hızının önemli olduğu diğer uygulamalar için uygun hale getirir.

Blok depolamayı genellikle *“birimler”* ( *volumes* ) halinde tahsis edersiniz; ardından bu birimler bir hesaplama düğümüne bağlanabilir ve düğüm bunu fiilen başka bir sabit disk gibi görür. Birimler normalde aynı anda yalnızca bir hesaplama düğümüne bağlanabilir.

---

## ⚙️ IOPS

Hem dosya hem de blok depolamada *“IOPS”* terimini de duyabilirsiniz.  *IOPS* , *Input/Output Operations Per Second* ( *Saniye Başına Giriş/Çıkış İşlemleri* ) anlamına gelir ve depolamanın hızıyla veya başka bir ifadeyle verinin depolamadan ne kadar hızlı okunup yazılabildiğiyle ilgilidir. Bunu sonraki bir videoda biraz daha ayrıntılı ele alacağız.

---

## 🧷 Kalıcılık

*Kalıcılık* ( *Persistence* ), dosya veya blok depolama tahsis edilirken kullanılan bir terimdir ve bağlı olduğu hesaplama düğümü sonlandırıldığında depolamaya ne olacağıyla ilgilidir.

Depolama *“kalıcı”* ( *persist* ) olarak ayarlanırsa, hesaplama düğümüyle birlikte silinmez; bu da depolamanın ve verilerinin korunacağı ve başka bir hesaplama düğümüne bağlanmak üzere kullanılabilir olacağı anlamına gelir; ancak depolama için ödeme yapmaya devam edersiniz.

Bazı durumlarda depolamayı, bağlı olduğu hesaplama düğümüyle birlikte otomatik olarak silinecek şekilde ayarlayabilirsiniz — bu durumda bildiğimiz gibi *Geçici Depolama* ( *Ephemeral Storage* ) haline gelir. Burada, depolama için ödeme yapmayı da durdurursunuz; ancak veriler başka bir yerde yedeklenmediyse tüm verileri kaybedersiniz.

---

## 📸 Anlık Görüntüler

Bulutta verileri yedeklemenin birkaç yolu vardır; ancak hem dosya hem de blok depolamayı yedeklemenin bir yolu, belirli bir andaki depolamanın görüntüsü olan bir *Anlık Görüntü* ( *Snapshot* ) almaktır.

Anlık görüntüler genellikle hızlı oluşturulur (aslında herhangi bir veri yazmazlar; daha doğrusu meta veri oluştururlar), kesinti süresi gerektirmez ve sonraki anlık görüntüler yalnızca verideki değişiklikleri kaydeder. Depolamayı belirli bir anlık görüntüdeki haline döndürmek için harikadırlar; ancak dikkat edin, tek tek dosyaları kurtarmak için kullanılamazlar.

---

## 🧺 Nesne Depolama

Dördüncü depolama türü *Nesne Depolama*dır ( *Object Storage* ). Bu, farklı bir depolama türüdür; çünkü bir hesaplama düğümüne bağlı değildir, bunun yerine bir *API* aracılığıyla erişilir.

Tüm depolama türleri içinde, nesne depolama açık ara en ucuz olanıdır ve okuma/yazma hızları açısından da en yavaştır; ancak son kullanıcı için boyutu sınırsızdır. Dosya ve blok depolamada belirli bir kapasite tahsis eder ve zamanla dolduğunu görürken, nesne depolamada dosyalar eklemeye devam edebilirsiniz ve hiç dolmaz; yalnızca kullandığınız kadar ödersiniz.

Bu durum, nesne depolamayı; büyük/küçük tüm *yapılandırılmamış veri* türleri için harika bir depo haline getirir. Bunlara belgeler, video, loglar, yedekler, IoT verileri, uygulama ikilileri (binaries) ve sanal makine imajları dahildir.

---

## 🎥 Devam Eden Videolar

Takip eden videolarda, farklı depolama türleri hakkında daha ayrıntılı bilgiler yer alacaktır.
