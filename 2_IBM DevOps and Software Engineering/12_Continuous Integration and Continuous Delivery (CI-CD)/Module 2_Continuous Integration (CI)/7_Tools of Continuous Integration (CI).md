# 🧰 Sürekli Entegrasyon (CI) Araçları

Sürekli Entegrasyon Araçları’na hoş geldiniz. Bu videoyu izledikten sonra Jenkins aracının nasıl çalıştığını, CircleCI aracının nasıl çalıştığını ve Travis CI aracının nasıl çalıştığını açıklayabileceksiniz.

![1766092488894](image/7_ToolsofContinuousIntegration(CI)/1766092488894.png)

## 🧱 Jenkins

Jenkins, üç aracın en eskisi, hem Sürekli Entegrasyon’u hem de Sürekli Teslim’i uygular. Eskiden bu alandaki en iyilerden biriydi. Onu bu kadar popüler yapan şeylerden biri açık kaynak olması ve kendi Jenkins sunucularınızı çalıştırabilmenizdi.

Jenkins’in Docker, Jira ve Maven gibi diğer araçlarla entegre olmak için geniş bir eklenti ekosistemi vardır; ancak bunun dezavantajı yönetilecek çok sayıda eklentinin olmasıdır. Tüm eklentilerin güncel ve güvenli olduğundan, ayrıca diğer tüm eklentilerle uyumlu olduğundan emin olmak için çok zaman harcamanız gerekir.

CI hattını bir Jenkinsfile içinde *Groovy* diliyle tanımlar. Bu da kullanıcıların onu kullanabilmek için bir miktar Groovy bilmesini gerektirir. Jenkinsfile, geliştiricilerin CI/CD hatlarını kod gibi ele almasını sağlar; aşağıdaki kısa örnekte gördüğünüz gibi, kodu çekmek ve test etmek için iki aşamalı basit bir hattı tanımlar.

![1766092566885](image/7_ToolsofContinuousIntegration(CI)/1766092566885.png)

Jenkins’i iş akışınıza dahil etmek için önce Jenkins web sitesinde projenizi kurmanız gerekir. Bu bir dezavantajdır. Göreceğiniz üzere, diğer araçlar yalnızca deponuza bir dosya ekleyerek bir hattı belirtmenize izin verir; bu da onları çok daha tekrarlanabilir yapar.

Bazı yapılandırmalar için bir web sitesi kullanmanızı istemesi, otomatikleştirilemeyen ve yeniden üretilemeyen manuel adımlar anlamına gelir.

Jenkins’i kullanmanın iki yolu vardır. Biz Jenkins Pipeline iş akışını ele alacağız. Deponuzu Jenkins Pipeline için hazırlamak adına, CI talimatlarını belirtmek üzere bir Jenkinsfile oluşturmanız ve bunu proje deponuzun kök dizinine koymanız gerekir. Bu talimatlar Jenkins’e hattı nasıl çalıştıracağını ve kodunuzu nasıl derleyip test edeceğini söyler.

Jenkins kodunuzu bir sanal makinede veya bir Docker konteyneri içinde derleyebilir. Ayrıca bir derlemeyi hangi eylemlerin tetikleyeceğini de belirtebilirsiniz.

![1766092638369](image/7_ToolsofContinuousIntegration(CI)/1766092638369.png)

Ne yazık ki bunu Jenkinsfile içinde yapamazsınız; bunu Jenkins sunucusunda kullanıcı arayüzünü kullanarak yapılandırmalısınız. Master dalına push yaptığınızda, bir pull request oluşturduğunuzda veya başka birçok olay gerçekleştiğinde bir derlemeyi çalıştıracak şekilde ayarlayabilirsiniz.

Şimdi gerçekçi bir Jenkinsfile örneğine bakalım. Bu örnek Jenkinsfile, bir Python projesi üzerinde birim testlerini çalıştırır. Dört aşaması vardır. Jenkins bir webhook tarafından bilgilendirildiğinde Jenkinsfile boyunca çalışır.

En üstte, kodu bir Docker ortamında çalışacak şekilde kurar. Hat önce kodu çeker. Bu hattaki bir sonraki adım, belirtilen Python paket bağımlılıklarını kurar. Sonra kodunuzdaki her Python modülünü *lint* eder. Bu, kodunuza girip en iyi kodlama uygulamalarını takip edip etmediğini kontrol ettiği anlamına gelir. Son olarak, kodunuz üzerinde birim testlerini çalıştırır.

Süreç basittir ve diğer CI araçlarında da benzer şekilde çalışır.

![1766092668270](image/7_ToolsofContinuousIntegration(CI)/1766092668270.png)

## 🔁 CircleCI

CircleCI bir servis olarak sunulur ve hem CI hem de CD uygular. Bir servis olduğu için Jenkins’te olduğu gibi bunu kendi sunucunuzda çalıştıramazsınız ve açık kaynak değildir.

Geliştiricilerin CI/CD hatlarını kod gibi ele almasını sağlar; tüm bu araçlarda göreceğiniz ortak bir temadır. Jenkins’teki Jenkinsfile’a benzer şekilde CircleCI, CI sürecini belirtmek için bir YAML dosyası kullanır; kodu çekip, Python paket bağımlılıklarını kuran ve bazı birim testlerini çalıştıran bu kısa örnekte görüldüğü gibi.

![1766092717266](image/7_ToolsofContinuousIntegration(CI)/1766092717266.png)

YAML kullanmanın avantajı, hem insanlar hem de makineler tarafından kolayca okunabilmesidir ve sistemleri ve servisleri yapılandırmak için çok popüler bir formattır.

CircleCI’yi iş akışınıza dahil etmek için önce CircleCI web sitesinde projenizi kurmanız gerekir. Ne yazık ki bu manuel bir adımdır.

Deponuzu CircleCI için ayarlamak üzere, CI talimatlarını belirtmek amacıyla bir yapılandırma dosyası oluşturmanız gerekir. Bu talimatlar CircleCI’ye kodunuzun ne zaman ve nasıl derlenmesini istediğinizi söyler. Kodunuzu bir sanal makinede veya bir Docker konteyneri içinde derleyebilir.

Ayrıca bir derlemeyi hangi eylemlerin tetikleyeceğini belirtebilirsiniz. Bir örüntü oluştuğunu görebilirsiniz; bu dersteki tüm araçlar hem yerel hem de Docker derlemelerini destekler ve hattın talimatlarını Jenkins’teki Jenkinsfile gibi kod olarak belirtir.

![1766092768329](image/7_ToolsofContinuousIntegration(CI)/1766092768329.png)

Şimdi bir örnek `circle.yaml` dosyasına bakalım. CircleCI yerleşik olarak Closure, Java, JavaScript, Python, PHP ve bazı diğer dilleri destekler. Ayrıca MySQL, MongoDB ve Postgres gibi veritabanlarını da destekler.

Docker’ı desteklediğinden, Docker içinde derleyebildiğiniz her şeyi CircleCI ile de derleyebilirsiniz. YAML dosyasının bu bölümü CircleCI’den bir Docker Python imajı almasını ister ve veritabanı URL’i için bir ortam değişkeni ayarlar.

Sonraki bölüm PostgreSQL’i ve Postgres’i yapılandırmak için çeşitli ortam değişkenlerini ayarlar. Ortam kurulduktan sonra kodunuzu çeker, paketleri kurar ve testleri çalıştırır.

Açıkça görebilirsiniz ki Jenkins ve CircleCI’nin çalışma biçiminde bir örüntü vardır.

![1766092810092](image/7_ToolsofContinuousIntegration(CI)/1766092810092.png)

## ✅ Travis CI

Travis CI diğer iki araç gibidir; hem CI hem de CD uygular. CircleCI gibi Travis CI de barındırılan bir servistir; bu da onu kendi sunucularınızda çalıştıramayacağınız anlamına gelir. Yalnızca bir servis olarak mevcuttur.

Yine de, kurumsal bir lisans alıp şirketiniz içinde dahili olarak çalıştırabilirsiniz. Ayrıca CircleCI ve Jenkins gibi, projenizi önce onların yönetim arayüzünde kurmanız gerekir; bu manuel bir adımdır.

Geliştiricilerin CI/CD hatlarını kod gibi ele almasını sağlar. CircleCI’dan farklı olarak, yerleşik biçimde çok daha fazla dili ve veritabanını destekler; ayrıca Docker’ı da desteklediği için Travis CI ile gerçekten her şeyi çalıştırabilirsiniz.

CircleCI’da olduğu gibi, CI sürecini belirtmek için bir YAML dosyası kullanırsınız; Python 3.9 ortamı isteyen, bağımlılıkları kuran, birim testlerini çalıştıran ve kod kapsamını yükleyen bu örnekte olduğu gibi. Küçük bir dosya için oldukça fazla işlev.

Travis CI’yi iş akışınıza dahil etmek için önce Travis CI web sitesinde projenizi kurmanız gerekir. Bu manuel bir adımdır; ancak Jenkins ve CircleCI’dan farklı olarak Travis, bunu tüm depolarınız için etkinleştirmenize izin verir; böylece tüm depolarınız için yalnızca bir kez yapılması yeterlidir.

Sonra, deponuzu Travis CI için ayarlamak üzere `.travis.yml` adlı bir dosya oluşturup deponuzun kök dizinine koymanız gerekir. Bu talimatlar Travis’e kodunuzun ne zaman ve nasıl derlenmesini istediğinizi söyler. Kodunuzu bir sanal makinede veya bir Docker konteyneri içinde derleyebilirsiniz.

![1766092888135](image/7_ToolsofContinuousIntegration(CI)/1766092888135.png)

Diğer araçlar gibi bir derlemeyi hangi eylemlerin tetikleyeceğini belirtebilirsiniz; ancak diğer araçlardan farklı olarak bu `.travis.yml` dosyasında yapılmaz. Tıpkı Jenkins’te olduğu gibi yalnızca Travis CI yönetim arayüzünden manuel olarak yapılabilir; bu da bir dezavantajdır.

Gördüğünüz gibi, bu araçların her biri aynı hedefe ulaşmak için bir yol sunar: kodunuzun Sürekli Entegrasyon’unu etkinleştirmek.

![1766092978409](image/7_ToolsofContinuousIntegration(CI)/1766092978409.png)

Şimdi bir örnek Travis YAML dosyasına bakalım. Diğer iki araç gibi `.travis.yml` dosyası derlemeyi çalıştırmak için talimatları tanımlar. Bu dosyanın en üstü, kodu derlemek için kullanılacak dili belirtir.

Ardından bir PostgreSQL veritabanı ister, veritabanı URL’i için bir ortam değişkeni ayarlar ve testleri bununla çalıştırmak için bir test veritabanı sağlar. Bundan sonra gerekli Python bağımlılık paketlerini kurar. Ortam hazırlandıktan sonra bu betik kodu test eder.

Son olarak test sonuçlarını toplar ve Codecov.io’ya yükler. Bu çok basit bir örnektir, ancak Travis CI ile Sürekli Entegrasyon’u otomatikleştirmenin çok da zor olmadığını gösterir.

![1766093007938](image/7_ToolsofContinuousIntegration(CI)/1766093007938.png)

## ⚙️ GitHub Actions

Bu genel bakışta bahsetmediğimiz bir araç daha var: GitHub Actions.

GitHub Actions, her GitHub deposunda bulunan bir CI/CD aracıdır. GitHub’a bir servis olarak entegredir. CI hattınızı tamamen kod gibi ele almanıza izin verir ve YAML dosyaları ile kontrol edilir.

GitHub Actions sonraki videolarda daha ayrıntılı ele alınacaktır ve bu kursta kullanacağınız araç olacaktır.

![1766093057541](image/7_ToolsofContinuousIntegration(CI)/1766093057541.png)

## 🧾 Özet

Bu videoda, farklı artıları ve eksileri olan birçok otomatik CI aracı olduğunu öğrendiniz ve bunların çoğunun benzer özelliklere sahip olduğunu gördünüz.

Bu araçların her biri, otomasyonu ve tekrarlanabilirliği mümkün kılarak kod olarak yazılabilen CI hatları sağlar ve CircleCI ile Travis CI gibi araçlar servis olarak sunulur; böylece onları yönetme konusunda endişelenmenize gerek kalmaz.

![1766093085218](image/7_ToolsofContinuousIntegration(CI)/1766093085218.png)
