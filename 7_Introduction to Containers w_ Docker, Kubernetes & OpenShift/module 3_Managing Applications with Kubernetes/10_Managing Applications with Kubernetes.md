# 📌 Özet ve Öne Çıkanlar: Kubernetes ile Uygulamaları Yönetme

Tebrikler! Bu modülü tamamladınız. Bu noktada şunları biliyorsunuz:

* Bir  *ReplicaSet* , pod oluşturarak veya silerek ölçeklendirmeyi mümkün kılar.
* *ReplicaSet* her zaman mevcut durumu istenen durumla eşleştirmeye çalışır.
* Otomatik ölçekleme ( *autoscaling* ), gerektikçe küme veya düğüm düzeyinde ve pod düzeyinde ölçeklendirme yapılmasını sağlar.
* Otomatik ölçekleyici türleri arasında yatay pod ( *HPA* ), dikey pod ( *VPA* ) ve küme ( *CA* ) bulunur.
* Rolling update’ler uygulama değişikliklerini kontrollü ve otomatik bir şekilde devreye alır.
* Rolling update ve geri alma ( *rollback* ), *all-at-once* ve *one-at-a-time* stratejileri kullanılarak gerçekleştirilebilir.
* *ConfigMap* ’ler, uygulamanıza değişkenler sağlamak için kullanılır.
* *Secret* ’ler, uygulamanıza hassas bilgiler sağlamak için kullanılır.
* Harici bir  *Service* ’i deployment’ınıza bağlamak ( *binding* ), bu Service’i kod içinde kullanmak için gereken kimlik bilgilerini otomatik olarak sağlar.
* Binding, arka uç ( *back-end* )  *Service* ’ler için yapılandırma ve kimlik bilgilerini yönetirken hassas verileri korur.
