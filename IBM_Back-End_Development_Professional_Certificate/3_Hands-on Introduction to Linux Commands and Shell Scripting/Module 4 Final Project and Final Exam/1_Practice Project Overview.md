# 🌦️ Uygulama Projesi: Giriş

## 📌 Senaryo

Ekibin tarafından, günlük hava tahmini ve gözlemlenen hava durumu verilerini çekmek ve bunları analiz ekibi tarafından daha ileri analizlerde kullanılmak üzere canlı bir rapora yüklemek için otomatik bir *Extract, Transform, Load (ETL)* süreci oluşturma görevi sana verilmiştir. Daha büyük bir tahmin modelleme projesinin parçası olarak ekip, raporu; kaynak ve istasyon bazında sıcaklık tahminlerinin tarihsel doğruluğunu izlemek ve ölçmek için kullanmak istemektedir.

Bir *proof-of-concept (POC)* olarak, başlangıçta bunu yalnızca tek bir istasyon ve tek bir kaynak için yapman gerekmektedir. Her gün, öğlen (yerel saatle), Fas’ın Kazablanka şehri için hem gerçek sıcaklığı hem de ertesi gün öğlen için tahmin edilen sıcaklığı toplayacaksın.

Daha sonraki bir aşamada ekip, raporu; konum listelerini, farklı tahmin kaynaklarını, farklı güncelleme sıklıklarını ve rüzgâr hızı ve yönü, yağış ve görüş mesafesi gibi diğer hava durumu metriklerini içerecek şekilde genişletmeyi öngörmektedir.

---

## 🌐 Veri kaynağı

Bu uygulama projesi için, açık kaynaklı *wttr.in* projesi tarafından sağlanan hava durumu veri paketini kullanacaksın. Bu, hava tahmini bilgilerini basit ve metin tabanlı bir formatta sağlayan bir web servisidir. Daha fazla bilgi için, hizmet hakkında  *GitHub Repo* ’sunda okuyabilirsin.

Önce, *wttr.in* web sitesi üzerinden hava durumu verilerini kazımak ( *scrape* ) için `curl` komutunu kullanacaksın. Örneğin, Kazablanka için veri almak üzere şu komutu gir:

1

```bash
curl wttr.in/casablanca
```

Bu komut, aşağıdakileri *standart çıktıya* ( *stdout* ) yazar.

![1764943544944](image/2_HistoricalWeatherForecastComparisontoActuals/1764943544944.png)

---

## 🎯 Öğrenme Hedefleri

Bu uygulama projesini tamamladıktan sonra, yeni kabuk betikleme ( *shell scripting* ) becerilerini gerçek dünya senaryosunda aşağıdaki amaçlarla uygulayabileceksin:

* Ham hava durumu verilerini indirmek
* Ham verilerden ilgi duyulan verileri çıkarmak
* Verileri gerektiği şekilde dönüştürmek
* Verileri, sekmeli bir format kullanarak bir günlük ( *log* ) dosyasına yüklemek
* Tüm süreci her gün belirli bir saatte otomatik olarak çalışacak şekilde zamanlamak

---

## 🧭 Genel Bakış

### 📋 Hava durumu raporlama görevleri

Fas’ın Kazablanka şehri için, her gün öğlen (yerel saatle) aşağıdaki verileri çıkarman ve saklaman gerekmektedir:

* Gerçek sıcaklık (santigrat derece cinsinden)
* Ertesi gün öğlen için tahmin edilen sıcaklık (santigrat derece cinsinden)

Ortaya çıkan hava durumu raporunun nasıl görünmesi gerektiğine dair bir örnek aşağıda verilmiştir:

| yıl | ay | gün | obs_tmp | fc_temp |
| ---- | -- | ---- | ------- | ------- |
| 2023 | 1  | 1    | 10      | 11      |
| 2023 | 1  | 2    | 11      | 12      |
| 2023 | 1  | 3    | 12      | 10      |
| 2023 | 1  | 4    | 13      | 13      |
| 2023 | 1  | 5    | 10      | 9       |
| 2023 | 1  | 6    | 11      | 10      |
| …   | … | …   | …      | …      |

Tablo 1. Hava durumu raporu örneği

Tüm projeyi kendi başına tamamlamayı deneyebilir veya süreç boyunca sana rehberlik etmesi için aşağıdaki alıştırmaları takip edebilirsin. Her iki durumda da, alıştırmalara, ipuçlarına ve çözümlere göz atmayı unutma.

---

## 💡 İpucu

Sürecin her adımında, kodunun amaçladığın şeyi yaptığından emin olmak için onu test et. Daha karmaşık adımlarda, görevi daha küçük ve daha yönetilebilir adımlara böl; böylece her birini ayrı ayrı test edebilirsin. Kodu, içinde bulunduğun bağlamın en uygun olduğunu gösterdiği şekilde, komut satırında ya da betiğini çalıştırarak test edebilirsin. Bağlam, en iyi yaklaşımı gösterecektir.
