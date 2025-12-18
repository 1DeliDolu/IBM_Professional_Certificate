# 🧰 Platform ve Araçlar

‘Platform ve Araçlar’a hoş geldiniz. Bu videoyu izledikten sonra şunları yapabileceksiniz: CI/CD için farklı araçlar kullanmanın sorun olmadığını anlamak ve CI/CD için bazı yaygın araçları belirlemek.

![1766088098087](image/6_PlatformandTools/1766088098087.png)

Aynı şirket içinde bile pipeline’larınızın kullanabileceği pek çok araç vardır. Tek bir organizasyon içindeki farklı iş birimi uygulamaları (*line of business applications* veya  *LOBs* ), farklı ekipler tarafından çalıştırılıyor olabilir ve farklı araçlar kullanmaları önemli değildir.

Dolayısıyla kaynak kodu yönetim sistemleri, build sistemleri, continuous integration sistemleri, repository’leri vb. farklı araçlar üzerinde çalışıyor olabilir. Jenkins olabilir, Travis olabilir, Nexus ve JFrog Artifactory olabilir; ancak kullanılan spesifik araç önemli değildir. Önemli olan, bu süreçleri manuel yapmak yerine otomatikleştirmek için bir araç kullanmalarıdır.

![1766088138226](image/6_PlatformandTools/1766088138226.png)

---

## 🧩 CI/CD Araç Ekosistemi

Aslında CI/CD için seçebileceğiniz sayısız araç vardır. Örneğin, pipeline araçları diyagramındaki ‘Build’ sütununda yalnızca ‘CI’ kutusuna bakarsanız Team City, Jenkins, Travis CI, Bamboo, Codeship, Snap ve Go gibi araçları (birkaçını saymak gerekirse) görebilirsiniz.

![1766088186938](image/6_PlatformandTools/1766088186938.png)

Ve en üsttekilerin çoğunun birbirine benzer göründüğünü, benzer çalışma şekilleri ve benzer kavramlara sahip olduğunu fark edeceksiniz. Bu yüzden bir aracı denersiniz ve sevmezseniz, kullanmayı sevdiğiniz bir araç bulana kadar yenilerini denemeye devam edebilirsiniz.

---

## 🔧 CI/CD İçin Yaygın Araçlara Kısa Bakış

### 🛠️ Jenkins

Jenkins, merkezi build’in gerçekleşeceği bir sunucuya kurulan CI/CD yazılımıdır. CI/CD araçlarının en eski, en popüler ve en karmaşık olanlarından biridir.

### 🔄 CircleCI

Circle CI, DevOps uygulamalarını hayata geçirmek için kullanılabilen bir CI/CD platformudur. Continuous Delivery için deployment’lar gerçekleştirir ve  *workflow* ’ları bir `circle.yaml` dosyası içinde tanımlarsınız.

### 🧪 Travis CI

Travis CI, GitHub ve Bitbucket üzerinde barındırılan yazılım projelerini build etmek ve test etmek için geliştiricilere yardımcı olan, barındırılan ( *hosted* ) bir CI servisidir. Travis CI, açık kaynak projelere ücretsiz hizmet sunan ilk CI servisiydi.

Continuous Delivery için deployment’lar da gerçekleştirir ve bir  *workflow* ’u bir `.travis.yaml` dosyası içinde tanımlarsınız.

### ⚙️ GitHub Actions

GitHub Actions, GitHub  *workflow* ’larınızı build, test ve deploy süreçlerini otomatikleştirmenizi sağlayan bir CI/CD platformudur. Diğer araçların aksine yalnızca GitHub ile çalışır.

![1766088249749](image/6_PlatformandTools/1766088249749.png)

---

## ✅ Özet

Bu videoda, aynı organizasyon içindeki farklı iş birimi uygulamalarında birçok ekibin farklı araçlar kullanabileceğini öğrendiniz. CI/CD için farklı araçlar kullanmak sorun değildir; önemli olan süreçlerin manuel yapılmak yerine otomatikleştiriliyor olmasıdır. Ayrıca CI/CD için çok sayıda araç vardır ve kullanmayı sevdiğiniz bir araç bulana kadar yenilerini deneyebilirsiniz.

![1766088301474](image/6_PlatformandTools/1766088301474.png)
