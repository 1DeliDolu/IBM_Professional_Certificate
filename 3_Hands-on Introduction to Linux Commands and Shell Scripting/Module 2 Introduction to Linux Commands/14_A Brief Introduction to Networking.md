# 🌐 Ağlara Kısa Bir Giriş

Burada bilgisayar ağlarıyla ilgili bazı temel kavramları tanıtıyoruz.

Bu, isteğe bağlı ama önerilen bir okumadır ve daha sonra ağlar ve bilgi amaçlı komutlar hakkında öğrenecekleriniz için bağlam oluşturmanıza yardımcı olmak üzere tasarlanmıştır.

---

## 🎯 Öğrenme Hedefleri

Bu okumayı tamamladıktan sonra şunları yapabileceksiniz:

* Bilgisayar ağlarını, ağ kaynaklarını ve ağ düğümlerini tanımlamak
* Ana makineleri ( *hosts* ), istemcileri ( *clients* ) ve sunucuları ( *servers* ) açıklamak
* Paketleri ( *packets* ) ve pingleri ( *pings* ) tanımlamak
* URL’leri ve IP adreslerini açıklamak

---

## 🖧 Bilgisayar Ağları

Bir  **bilgisayar ağı** , birbirleriyle iletişim kurabilen ve ağ düğümleri tarafından sağlanan kaynakları paylaşabilen bilgisayarların oluşturduğu bir kümedir.

Bilgisayar ağlarına örnek olarak  **Yerel Alan Ağları (LAN)** , **Geniş Alan Ağları (WAN)** ve tüm **İnternet** verilebilir. İnternet ya da Dünya Çapında Ağ (World Wide Web), temelde bilgisayar ağlarının devasa bir ağıdır.

Bir  **ağ kaynağı (network resource)** , ağ tarafından tanımlanabilen herhangi bir nesnedir; örneğin bir dosya veya belge.

Bir nesne, ağa kendisini tanımlamak ve erişmek için kullanabileceği benzersiz bir ad ve adres atanabiliyorsa, **tanımlanabilir (identifiable)** kabul edilir.

Bir  **ağ düğümü (network node)** , bir ağa katılan herhangi bir aygıttır.

Bir ağ, mutlaka bilgisayar olmayan ama ağ altyapısının bir parçası olan herhangi bir aygıtı içerebilir. Ağ düğümlerine örnek olarak  **modemler** ,  **ağ anahtarları (switches)** , **hub’lar** ve **Wi-Fi erişim noktaları (hotspots)** verilebilir.

---

## 🖥️ Ana Makineler, İstemciler ve Sunucular

Bir  **ana makine (host)** , bilgisayar ağında özel bir tür düğümdür; ağ üzerinde bir **sunucu (server)** ya da **istemci (client)** olarak çalışabilen bir bilgisayardır.

Bir  **sunucu** , bir istemci ana makinesinden bağlantı kabul edebilen ve istemcinin yaptığı belirli kaynak isteklerini yerine getirebilen bir ana bilgisayardır.

Birçok ana makine her iki rolü de yerine getirebilir; hem istemci hem de sunucu olarak davranabilir.

---

## 📦 Paketler ve Pingler

Bir  **ağ paketi (network packet)** , ağ üzerinden iletilebilen biçimlendirilmiş bir veri parçasıdır.

Günümüz bilgisayar ağları, genellikle bu tür bilgi paketlerine dayanan iletişim protokolleri kullanır. Her paket iki tür veriden oluşur:

1. **Kontrol bilgisi (control information)**
2. **Yük (payload)**

Kontrol bilgisi; kaynağın ve hedefin ağ adresleri gibi, yükün nasıl ve nereye iletileceğine dair verilerden oluşur. Yük ( *payload* ) ise gönderilen asıl mesajdır.

`ping` komutu, bir ana makineye özel **“echo request”** paketleri göndererek ve ana makineden bir yanıt bekleyerek çalışır.

`ping`, ağ özelliklerine sahip çoğu işletim sisteminde bulunan bir yardımcı programdır. Linux, diğer ağ ana makinelerine olan bağlantıyı test etmek ve sorun gidermek için kullanılan `ping` komutunun kendine özgü bir uygulamasına sahiptir.

---

## 🔗 URL’ler ve IP Adresleri

 **IP** , “Internet Protocol”ün kısaltmasıdır ve internet veya yerel bir ağ üzerinden iletilen verinin biçimini tanımlar.

Bir  **IP adresi** , ağ üzerindeki herhangi bir ana makineyi benzersiz şekilde tanımlamak için kullanılan bir koddur.

Bir IP adresi, bir ana makineye bağlantı kurmak ve örneğin `ping` komutunu kullanarak onunla paket alışverişinde bulunmak için kullanılabilir.

Yüklerine ek olarak, **IP paketleri** – Internet Protokolü’ne uyan bir ağ paketi türü – kaynak ve hedef ana makinelerin IP adreslerini de içerir.

Bir  **URL** , daha yaygın adıyla bir web adresi, *Uniform Resource Locator* ifadesinin kısaltmasıdır.

Bir URL, bir web kaynağını benzersiz şekilde tanımlar ve bu kaynağa erişim sağlar. Tipik olarak bir URL’nin işaret ettiği kaynak bir web sayfasıdır; ancak dosya transferi, e-posta gönderme ve veritabanı erişimi gibi görevler için de kullanılabilir.

Örneğin, URL hakkındaki Wikipedia sayfasının URL’si:

`https://en.wikipedia.org/wiki/URL`

Tipik bir URL’de olduğu gibi bu URL’nin biçimi de bir **protokolü** (`https`), bir **ana makine adını (hostname)** (`en.wikipedia.org`) ve bir **dosya adını** (`/wiki/URL`) belirtir.

---

## ✅ Özet

Bu okumada şunları öğrendiniz:

* Bir  **bilgisayar ağı** , birbirleriyle iletişim kurabilen ve kaynakları paylaşabilen bilgisayarların bir kümesidir. Bir  **ağ kaynağı** , ağ tarafından tanımlanabilen herhangi bir nesnedir; örneğin bir dosya veya belge. Bir  **ağ düğümü** , ağa katılan herhangi bir aygıttır.
* Bir  **ana makine (host)** , ağ üzerinde bir sunucu ya da istemci olarak çalışabilen bir bilgisayardır. Bir  **sunucu (server)** , bir istemci ana makinesinden bağlantı kabul edebilen ve istemcinin belirli kaynak isteklerini yerine getirebilen bir ana bilgisayardır.
* Bir  **ağ paketi** , ağ üzerinden iletilebilen biçimlendirilmiş bir veri parçasıdır. `ping` komutu, bir ana makineye özel **“echo request”** paketleri göndererek ve ana makineden yanıt bekleyerek çalışır.
* Bir  **IP adresi** , ağ üzerindeki herhangi bir ana makineyi benzersiz biçimde tanımlamak için kullanılan bir koddur. Bir  **URL** , bir web kaynağını tanımlar ve bu kaynağa erişim sağlar.
