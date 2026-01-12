# 🧾 Özet ve Öne Çıkanlar: Gözlemlenebilirlik (Observability)

Tebrikler! Bu dersi tamamladınız. Bu noktada şunları biliyorsunuz:

---

## 🔍 Gözlemlenebilirlik Tanımı

Gözlemlenebilirlik ( *observability* ), mühendislik ve bilgisayar bilimlerinde, bir sistemin *dış çıktıları* kullanılarak *iç durumunu* anlama yeteneğini tanımlamak için kullanılan bir terimdir.

---

## 🎯 Gözlemlenebilirliğin Faydaları

Gözlemlenebilirlik; BT ekiplerine, kuruluşlara, uygulama geliştiricilerine ve kullanıcılara aşağıdakiler gibi güçlü faydalar sunar:

* Uygulama performansı izleme ( *application performance monitoring* )
* Altyapı ve bulut izleme ( *infrastructure and cloud monitoring* )
* Kullanıcı deneyimi ( *user experience* )

---

## 🧱 Gözlemlenebilirliğin 3 Sütunu

Gözlemlenebilirliğin üç sütunu şunlardır:  *loglar (logs)* , *metrikler (metrics)* ve  *izler (traces)* .

---

## 🗒️ Loglar

Loglar, tekil olaylar veya işlemler hakkında ayrıntılı bilgileri yakalayarak ne olduğuna dair kronolojik bir kayıt sunar.

---

## 📈 Metrikler

Metrikler, belirli bir sistem bileşeninin sağlığını gösteren, eşlik eden özniteliklere sahip sayısal ölçümlerdir.

---

## 🧵 İzler

İzler ( *traces* ), bir işlem gibi bir iş öğesini takip etmek için oluşturulan bilgi yollarının veya iş akışlarının kayıtlarıdır.

---

## ☁️ Cloud Native Gözlemlenebilirlik

Cloud native gözlemlenebilirlik, dinamik ve dağıtık ortamlarda çalışan cloud-native uygulamaların davranışını izleme ve anlama pratiğidir.

---

## 🧩 Cloud Enterprise Gözlemlenebilirliğin Sütunları

Cloud enterprise gözlemlenebilirliğin sütunları şunlardır:

* Otomasyon ( *automation* )
* Bağlam ( *context* )
* Akıllı aksiyon ( *intelligent action* )

---

## 🛠️ Cloud Native Gözlemlenebilirlik Araçları

Cloud native gözlemlenebilirlik araçları ve çözümleri kuruluşlar için kritiktir ve bulut ortamları genelinde telemetri verilerini büyük ölçekte ilişkilendirebilir.

Popüler cloud native gözlemlenebilirlik araçları:

* Prometheus
* Jaeger
* FluentD
* Thanos
* Datadog
* New Relic
* AWS CloudWatch
* Google Cloud Monitoring
* Instana
* Mezmo

---

## 🎛️ Loglamada Örnekleme (Sampling)

Loglamada örnekleme ( *sampling* ), analiz veya depolama amacıyla log olaylarının yalnızca bir alt kümesini toplama pratiğidir. Her bir olayı veya veri parçasını loglamak yerine, kayıt için rastgele veya başka bir kritere göre bir alt küme seçilir.

---

## ✅ Örneklemenin Avantajları

Örneklemenin avantajları:

* Azaltılmış ek yük ( *reduced overhead* )
* Geliştirilmiş performans ( *enhanced performance* )
* Maliyet etkinliği ( *cost-effectiveness* )
* İyileştirilmiş doğruluk ( *improved accuracy* )
* Daha iyi ölçeklenebilirlik ( *better scalability* )

---

## ⚠️ Örneklemenin Dezavantajları

Örneklemenin dezavantajları:

* Ayrıntıların kaçırılması ( *missing details* )
* Hatalı/verimsiz veri ( *inaccurate data* )
* Sınırlı çözünürlük ( *limited resolution* )
* Aykırı değerlerin maskelenmesi ( *masked outliers* )
* Karmaşık performans sorunlarını teşhis etmede zorluklar ( *challenges in diagnosing complex performance issues* )

---

## 🧠 IBM Instana Observability

IBM Instana Observability (genellikle *Instana* olarak bilinir), mikroservis ve cloud-native uygulamaları yönetmenin zorluklarını aşmak için özel olarak tasarlanmış, tamamen otomatik bir uygulama performans yönetimi ( *APM* ) çözümüdür.

---

## 🔬 Instana’nın İzleme ve Analiz Kapsamı

Instana; uygulamalarınızı, servislerinizi, altyapınızı, web tarayıcılarını, mobil uygulamaları ve daha fazlasını 200’den fazla alan-özgü teknoloji için izler ve analiz eder.

---

## 🗺️ Bağımlılık Haritalama ve Etki Bildirimi

Instana, tüm yığın genelinde bağımlılık haritalamayı otomatikleştirir ve müşterilerin performans veya kararlılık sorunlarından etkilendiği durumlarda bilgilendirme yapar.
