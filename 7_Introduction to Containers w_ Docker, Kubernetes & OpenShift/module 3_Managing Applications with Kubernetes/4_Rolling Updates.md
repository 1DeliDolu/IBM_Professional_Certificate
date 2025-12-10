# 🔄 Rolling Updates

Rolling Updates’e hoş geldiniz. Bu videoyu izledikten sonra şunları yapabileceksiniz:

* Bir  *rolling update* ’in ne olduğunu ve nasıl çalıştığını açıklamak
* Bir *rolling update* uygulanmadan önceki ön adımları listelemek
* Bir  *rolling update* ’in geri alınışını ( *rollback* ) nasıl göstereceğinizi açıklamak

---

## ⚙️ Rolling update nedir ve nasıl çalışır?

Rolling updates, planlanmış bir zamanlamaya göre gerçekleşen otomatik güncellemelerdir.

Uygulama değişikliklerini pod’lar arasında otomatik ve kontrollü bir şekilde yayarlar, deployment gibi pod şablonlarıyla birlikte çalışırlar ve gerektiğinde geri alma ( *rollback* ) olanağı sunarlar.

---

## ✅ Rolling update için uygulamayı hazırlama

Uygulamanızı rolling updates için hazırlamak üzere, deployment’lara *liveness probe* ve *readiness probe* ekleyin.

Bu sayede deployment’lar uygun şekilde “hazır” olarak işaretlenir.

Sonraki adımda, YAML dosyasına bir rolling update stratejisi ekleyin. Bu örnekte, 10 pod’luk bir deployment oluşturuyorsunuz.

---

## 🔧 Rolling update strateji ayarları

Stratejiniz, pod’ların en az %50’sinin her zaman kullanılabilir olmasını sağlamaktır.

`max surge` değerinin 2 olması, daha önce tanımladığınız 10 pod’a en fazla 2 pod daha eklenebileceği anlamına gelir.

Kesmeyen ( *zero-downtime* ) bir sistem için `max unavailable` değerini 0 olarak ayarlayın.

`max surge` değerini %100 olarak ayarlamak, pod sayısını iki katına çıkarır ve rollout tamamlandıktan sonra orijinal seti kapatmadan önce tam bir replikasını oluşturur.

Ve bazen, rollout aşamasında bir sonraki pod’a geçmeden önce birkaç saniye beklemek için `*miniReadySeconds*` özelliğini kullanmak da faydalıdır.

---

## 🧪 Örnek: Uygulama güncellemesini rolling update ile dağıtma

Replica set’inizde 3 pod bulunan bir deployment’ınız var.

Uygulamanızda şu mesaj gösteriliyor: `Hello World!`

Müşteriniz yeni bir talepte bulundu ve farklı bir mesaj içeren yeni bir uygulama imajınız var.

Orijinal metin yerine, kullanıcılara `Hello World v2` mesajını göstermeniz gerekiyor. Ancak uygulamanızda herhangi bir kesinti yaşanmasına izin veremezsiniz.

---

## 📦 Docker imajını oluşturma ve Docker Hub’a yükleme

Önce bu yeni imajı oluşturmanız ( *build* ), etiketlemeniz ( *tag* ) ve Docker Hub’a yüklemeniz gerekir.

Yeni yazılımınız dockerize edilmiştir ve şu ad ve etiketle Docker Hub’a güncellenmiştir:

`hello-kubernetes-upcar-hello-kubernetes-colon-2.0`

Bunlar, Kubernetes ile doğrudan ilgili olmayan basit Docker komutlarıdır.

---

## 🚀 Yeni imajı deployment’a uygulama

Şimdi bu yeni imajı deployment’ınıza uygulayın.

İlk komuttan gelen 3 pod’a sahipsiniz.

İkinci komut, Docker Hub’daki güncellenmiş etiketli imaja `image` bayrağını ayarlar.

Çıktı, imajın güncellendiğini söylüyor. Ancak bunun gerçekten olup olmadığını doğrulayalım.

Rollout’un durumunu `rollout status` komutunu kullanarak görebilirsiniz.

```bash
rollout status
```

API, `deployment hello-kubernetes successfully rolled out` mesajını gösterir. Bu harika.

Şimdi URL’ye geri dönerseniz, yeni `Hello World v2` mesajını görürsünüz.

---

## ↩️ Rollback (geri alma) işlemini gerçekleştirme

Bazen bir deployment’ta hatalar olabilir veya müşteri fikrini değiştirebilir.

Kubernetes’te rollback’leri uygulamak kolaydır.

Rollout üzerinde bir `undo` komutu kullanın.

```bash
undo
```

Rollout pod’larının sonlandırıldığını doğrulamak için `get pods` komutunu kullanın.

```bash
get pods
```

Ayrıca bu rollback işleminin bir parçası olarak oluşturulan 3 yeni pod da göreceksiniz.

Siteyi tekrar ziyaret ederseniz, orijinal mesajı görürsünüz.

Ve işte bu şekilde, uygulamanıza yapılan değişiklikleri geri alırsınız.

---

## 🔁 Rolling update stratejileri: all-at-once ve one-at-a-time

Şimdi rolling updates’in *all-at-once* ve *one-at-a-time* yöntemleriyle nasıl çalıştığına bakalım.

---

## 💣 All-at-once rollout (hepsi bir kerede güncelleme)

Bir  *all-at-once rollout* ’ta, v2 nesneleri aktif hâle gelmeden önce tüm v1 nesnelerinin kaldırılması gerekir.

Burada, kullanıcıların erişebildiği 3 pod ile çalışan bir uygulamanın sürüm 1’ini görüyorsunuz.

Sürüm 2 dağıtıldığında yeni pod’lar oluşturulur.

Sürüm 1 pod’ları silinmek üzere işaretlenir ve kaldırılır.

Kullanıcı erişimi engellenir.

Sürüm 1 pod’ları kaldırıldıktan sonra sürüm 2 pod’ları aktif hâle gelir ve kullanıcı erişimi yeniden sağlanır.

Deployment ile pod güncellemeleri arasındaki zaman farkına dikkat edin.

---

## ⏪ All-at-once rollback (hepsi bir kerede geri alma)

Bir  *all-at-once rollback* ’te, v1 nesneleri aktif hâle gelmeden önce tüm v2 nesnelerinin kaldırılması gerekir.

Bir  *all-at-once rollback* ’in nasıl göründüğüne bakalım.

Burada, kullanıcıların erişebildiği 3 pod ile çalışan bir uygulamanın sürüm 2’sini görüyorsunuz.

Uygulamanın sürüm 1’i dağıtıldığında yeni pod’lar oluşturulur.

Sürüm 2 pod’ları silinmek üzere işaretlenir ve kaldırılır.

Ve kullanıcı erişimi engellenir.

Sürüm 2 pod’ları kaldırıldıktan sonra sürüm 1 pod’ları aktif hâle gelir ve kullanıcı erişimi yeniden sağlanır.

---

## 🌊 One-at-a-time rollout (teker teker güncelleme)

Bir  *one-at-a-time rollout* ’ta güncelleme kademeli olarak yapılır, böylece kullanıcı erişimi kesintiye uğramaz.

Burada, kullanıcıların erişebildiği 3 çalışan pod ile bir uygulamanın sürüm 1’ini görüyorsunuz.

Sürüm 2 dağıtıldığında yeni bir pod oluşturulur.

İlk sürüm 1 pod’u silinmek üzere işaretlenir ve kaldırılır.

Ve v2 pod’u aktif hâle gelir.

Ardından ikinci bir v2 pod’u oluşturulur.

İkinci sürüm 1 pod’u silinmek üzere işaretlenir ve kaldırılır.

İkinci v2 pod’u aktif hâle gelir.

Üçüncü bir v2 pod’u oluşturulur.

Ve üçüncü sürüm 1 pod’u silinmek üzere işaretlenir ve kaldırılır.

Ve şimdi üçüncü v2 pod’u aktif hâle gelir.

Kademeli bir güncellemede kullanıcı erişimi kesintiye uğramaz.

---

## 🔄 One-at-a-time rollback (teker teker geri alma)

Bir  *one-at-a-time rollback* ’te, geri alma işlemi kademeli olarak yapılır, böylece kullanıcı erişimi kesintiye uğramaz.

Bir  *one-at-a-time rollback* ’in nasıl göründüğüne bakalım.

Burada, kullanıcıların erişebildiği 3 çalışan pod ile bir uygulamanın sürüm 2’sini görüyorsunuz.

Uygulamanın sürüm 1’i dağıtıldığında yeni bir pod oluşturulur.

İlk sürüm 2 pod’u silinmek üzere işaretlenir ve kaldırılır.

Ve v1 pod’u aktif hâle gelir.

Şimdi ikinci bir v1 pod’u oluşturulur.

İkinci sürüm 2 pod’u silinmek üzere işaretlenir ve kaldırılır.

Ve ikinci v1 pod’u aktif hâle gelir.

Ardından üçüncü bir v1 pod’u oluşturulur.

Ve üçüncü sürüm 2 pod’u silinmek üzere işaretlenir ve kaldırılır.

Ve üçüncü v1 pod’u aktif hâle gelir.

---

## ✅ Özet

Bu videoda şunları öğrendiniz:

* Rolling updates, uygulama değişikliklerini kontrollü ve otomatik bir şekilde yayar.
* Rolling updates, uygulamalara fark edilir bir kesinti olmadan değişiklik yayımlar.
* Rolling updates, uygulamanın geri dönmesi gerektiğinde değişiklikleri geri alabilir.
* Rolling updates ve rollbacks, *all-at-once* ve *one-at-a-time* stratejileri kullanılarak gerçekleştirilebilir.
