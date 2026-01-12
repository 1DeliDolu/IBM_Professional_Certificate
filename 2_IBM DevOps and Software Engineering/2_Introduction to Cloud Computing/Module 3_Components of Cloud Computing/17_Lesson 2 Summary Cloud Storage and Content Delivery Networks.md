# 📘 Ders 2 Özeti: Bulut Depolama ve İçerik Dağıtım Ağları

Bu derste şunları öğrendiniz:

## 🗄️ Bulut Depolama Türleri

Bulut depolama dört ana türde sunulur:  *Direct Attached* ,  *File* , *Block* ve  *Object Storage* . Bu depolama türleri; nasıl erişilebildikleri, sundukları kapasite, maliyetleri, depolamak için en uygun oldukları veri türleri ve okuma-yazma hızları açısından farklılık gösterir.

## 💽 Direct Attached Storage

 *Direct Attached (veya Local) Storage* , bulut tabanlı bir sunucuya doğrudan sunulan ve fiilen ya ana sunucu kasası içinde ya da aynı rack içinde bulunan depolamadır.

## 📁 File Storage

*File Storage* genellikle işlem (compute) düğümlerine bir *Network File System (NFS)* olarak sunulur; bu da depolamanın standart bir ethernet ağı üzerinden işlem düğümlerine bağlandığı anlamına gelir.

## 🧱 Block Storage

 *Block Storage* , işlem düğümlerine yüksek hızlı fiber bağlantılar kullanılarak sunulur; genellikle  *volume* ’lar halinde sağlanır ve bir işlem düğümüne mount edilir.

## 🪣 Object Storage

*Object Storage* bir API üzerinden erişilir ve altta yatan bir işlem düğümüne ihtiyaç duymaz.

## ♾️ Object Storage Kapasite ve Hız

*Object Storage* sonsuz kapasite sunar; çünkü sürekli dosya ekleyebilirsiniz ve yalnızca kullandığınız kadar ödersiniz. Diğer depolama türleriyle kıyaslandığında, nesne depolama okuma ve yazma hızları açısından en yavaştır.

## 🌐 CDN

Bir  *Content Delivery Network (CDN)* , coğrafi konumlarına göre kullanıcılara web sitesi veya medya içeriğinin geçici olarak saklanmış ya da önbelleğe alınmış kopyalarını sunarak internet içerik teslimatını hızlandıran, dağıtık bir sunucu ağıdır.
