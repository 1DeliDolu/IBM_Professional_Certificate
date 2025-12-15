# 🕰️ Bulut Bilişimin Tarihi ve Evrimi

Bulut bilişimin Tarihi ve Evrimine hoş geldiniz. Bulut bilişim, zaman içinde teknolojinin bir evrimidir. Bulut bilişim kavramı, yüksek hacimli işlem gücüne sahip büyük ölçekli ana bilgisayarların (mainframe) kullanılabilir hâle geldiği 1950’lere dayanır.

Zaman paylaşımı (veya kaynak havuzlama) uygulaması, ana bilgisayarların işlem gücünü verimli kullanmak için gelişti. Tek amacı ana bilgisayarlara erişimi kolaylaştırmak olan “dumb terminal”lar kullanılarak, birden fazla kullanıcı herhangi bir terminalden aynı veri depolama katmanına ve CPU gücüne erişebiliyordu.

1970’lerde, Virtual Machine (VM) adlı bir işletim sisteminin yayımlanmasıyla, ana bilgisayarların tek bir fiziksel düğüm üzerinde birden fazla sanal sistem veya sanal makine (virtual machine) çalıştırması mümkün oldu. Sanal makine işletim sistemi, 1950’lerde ana bilgisayara paylaşımlı erişim uygulamasından evrildi.

Birden fazla ayrı hesaplama ortamının aynı fiziksel donanım üzerinde var olmasına izin vererek. Her sanal makine, kaynaklar paylaşılıyor olsa bile kendi belleğine, CPU’suna ve sabit disklerine sahipmiş gibi davranan konuk işletim sistemlerini barındırıyordu. Böylece sanallaştırma, iletişim ve bilişimdeki en önemli evrimlerin bazılarında teknolojik bir itici güç ve büyük bir katalizör hâline geldi.

Daha 20 yıl önce fiziksel donanım oldukça pahalıydı. İnternet daha erişilebilir hâle gelirken ve donanım maliyetlerini daha uygulanabilir kılma ihtiyacı doğarken, sunucular; sanal makine işletim sisteminin sağladığı aynı işlevsellik kullanılarak paylaşımlı barındırma ortamlarına, sanal özel sunuculara ve sanal adanmış sunuculara sanallaştırıldı.

Örneğin, bir şirket uygulamalarını çalıştırmak için ‘x’ sayıda fiziksel sisteme ihtiyaç duyuyorsa, tek bir fiziksel düğümü birden fazla sanal sisteme bölebilirdi. Hypervisor, birden fazla işletim sisteminin aynı fiziksel bilişim kaynaklarını paylaşarak yan yana çalışmasını sağlayan küçük bir yazılım katmanıdır.

Bir hypervisor ayrıca Sanal Makineleri mantıksal olarak ayırır; alttaki işlem gücü, bellek ve depolamanın her bir dilimini tahsis ederek sanal makinelerin birbirini etkilemesini engeller. Dolayısıyla örneğin bir işletim sistemi bir çökme veya güvenlik ihlali yaşarsa, diğerleri çalışmaya devam edebilir.

Teknolojiler ve hypervisor’lar geliştikçe ve kaynakları güvenilir biçimde paylaşabilir ve sunabilir hâle geldikçe, bazı şirketler bulutun faydalarını kullanıcılara erişilebilir kılmaya karar verdi. Bu kullanıcıların, kendi bulut bilişim altyapılarını oluşturmak için çok sayıda fiziksel sunucusu yoktu.

Sunucular zaten çevrimiçi olduğu için yeni bir örneği (instance) ayağa kaldırmak anlıktı. Kullanıcılar artık daha büyük bir kullanılabilir kaynak havuzundan bulut kaynakları sipariş edebiliyor ve bunlar için kullanım başına ödeme yapabiliyordu; bu, *pay-as-you-go* olarak da bilinir. Bu *pay-as-you-go* veya hizmet tipi bilişim (utility computing) modeli, bulut bilişimin başlatılmasının arkasındaki temel itici güçlerden biri hâline geldi.

Kullanım başına ödeme modeli, şirketlerin ve hatta bireysel geliştiricilerin bilişim kaynakları için tıpkı elektrik birimleri gibi, kullandıkları zaman ve kullandıkları ölçüde ödeme yapmalarına olanak tanıdı. Bu, onların CapEx modelinden, nakit akışına daha uygun bir OpEx modeline geçmesini sağladı.

Bu model; az donanıma sahip olan ya da hiç donanımı olmayan şirketlere ve hatta çok donanımı olanlara bile cazip geldi; çünkü artık donanıma büyük sermaye harcamaları yapmak yerine, ihtiyaç duyduklarında ve ihtiyaç duydukları kadar işlem (compute) kaynağı için ödeme yapabiliyorlardı. Ayrıca kullanım zirvelerinde iş yüklerini ölçekleyip, kullanım azaldığında ölçeği küçültebilmelerini sağladı. Ve bu da modern bulut bilişimin doğuşuna yol açtı.
