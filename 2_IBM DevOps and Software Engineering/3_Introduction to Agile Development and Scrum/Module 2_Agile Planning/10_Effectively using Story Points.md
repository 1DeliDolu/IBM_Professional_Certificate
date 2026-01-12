# 📌 Story Point’leri Etkili Kullanmak

Bu videoyu izledikten sonra,  *story point* ’leri tanımlayabilecek, *story point* atarken dikkate alınacak unsurları açıklayabilecek ve  *story point* ’leri göreli bir ölçekte tahmin edebileceksiniz.

Peki *story point* nedir?  *Story point* ’ler, bir  *user story* ’yi teslim etmek ve uygulamak için gereken zorluk derecesini tahmin etmekte kullanılan bir metriktir. Buradaki kilit nokta, bunun soyut bir ölçü olmasıdır. İnsanların takıldığı yer de burasıdır; soyutlukla baş etmekte zorlanırlar. Ancak bunu anlamanız çok ama çok önemlidir; aksi halde bazı  *anti-pattern* ’lere düşersiniz.

---

## 🧩 Tahmine Neler Dahildir?

Bu tahminin içinde birkaç bileşen vardır:

İlki  *effort* ’tur. Yani, bunu yapmak ne kadar zor?

Sonra *complexity* gelir. Yani, iş çok mu karmaşık, yoksa çok mu kolay? Bazen kolay bir iş için bile çok fazla *effort* gerekebilir; sadece sıkıcı ve zahmetlidir, oturup yapmak zorundasınızdır. Bu durumda iş çok karmaşık olmayabilir.

Bir de *uncertainty* vardır. Bunu daha önce yaptınız mı? Eğer daha önce yapmadıysanız,  *story point* ’leri biraz daha yüksek verebilirsiniz çünkü belirsizlik artar; ne kadar karmaşık olduğunu gerçekten bilmiyorsunuzdur. Yani bu, bildiklerinizle bilmedikleriniz arasındaki bir denge meselesidir.

---

## ⏱️ Neden “Süre” Üzerinden Tahmin Yapmıyoruz?

Geleneksel olarak insanlar “duvar saati zamanı” ( *wall clock time* ) tahmin etmekte çok kötüdür. Hatırlayın, tarihler “vuuuşş” diye geçip gider; bir şeye söz veririz ve sonra kaçırırız. Sonra da şunu öğreniriz: 30 dakika süren tek şey 30 dakikadır; geri kalan her şey daha uzun sürer.

Bu yüzden insanların “bu bir saat sürer”, “bu bir hafta sürer” diye tahmin yapması çok zordur. Bu nedenle bunu yapmayız. Eğer bu şekilde doğru tahmin edemiyorsak, o şekilde tahmin etmeyelim.

---

## 👕 Tişört Bedenleri Mantığı ve Fibonacci

Bunun yerine tişört bedenleri kullanırız;  *story point* ’ler tişört bedenleridir. Bu iş *medium* mu, *small* mı, *large* mı, *extra large* mı? Amacımız bunun ne kadar büyük olduğunu göreli olarak ifade etmektir; böylece mevcut sprint içindeki diğer işlerle karşılaştırabiliriz.

Ancak **S/M/L** gibi harfleri toplayıp sayı elde edemeyiz. Bir yandan da  *velocity* ’yi (bir sprintte tamamlayabildiğimiz *story point* sayısı) takip etmek için sayılara ihtiyacımız vardır. Bu yüzden çoğu araçta *Fibonacci sequence* kullanırız.

Ben hiçbir zaman dizideki tüm sayıları kullanmam. Önerim şudur:

* *medium* = **5**
* *small* = **3**
* *large* = **8**
* *extra large* = **13**

Bunun ötesine genelde pek geçmem. Dizinin tamamını kullanabilirsiniz, sorun yok; ama fazla granüler olmayın. Unutmayın, insanlar bu tür tahminlerde zaten çok iyi değildir. Bu yüzden soyut tutmak isteriz.

---

## 🧷 “Soyut” Nasıl Somutlanır?

Soyut yapmak için takımın “*medium* ne demek?” konusunda anlaşması gerekir. Çünkü  *story point* ’ler göreli olduğu için herkesin “tamam, bu medium” dediği bir referans gerekir.

Bu yüzden “medium = 5” deriz ve **5’lik story nasıl bir story’dir** diye ortak bir anlayış oluştururuz. Sonra diğer story’leri buna göre değerlendiririz:

* Bu bundan daha mı küçük?
* Daha mı büyük?
* Aynı boyutta mı?

---

## 🏙️ Binalarla Öğrenme Örneği

 *Story point* ’leri böyle öğrendim. Eğer size “Bu binalar ne kadar yüksek?” diye sorulsa, kat saymaya çalışırsınız. Her kat yaklaşık 20–25 feet dersiniz; böyle kabaca hesap yaparsınız.

Ama size şunu söylesem:

“Şu bina  **5** . Hemen solundaki bina kaç?”

Siz de dersiniz ki:

“Eğer bu 5 ise, soldaki muhtemelen  **3** .”

Sonra:

“Sağdaki biraz daha uzunsa, o **8** olabilir.”

Ve:

“En büyük olanı da **13** olabilir.”

Bu sadece göreli boyutlar demektir. Yani “bu medium ise, diğeri daha mı büyük?” diye bakarsınız. Takımın yaptığı şeye göre hepsi bir şeye göre göreli olur.

---

## 📏 Bir Story’nin Boyutu Nasıl Olmalı?

Story’ler küçük olmalıdır; göreli olarak küçük, idealde birkaç günde yapılabilecek işler olmalıdır. Çok büyük yapmamalısınız; uzayıp gitmesini istemezsiniz.

Bu yüzden story’leri küçük tutmalı ve birkaç gün içinde bitirebileceğiniz şeyleri tahmin etmelisiniz.

Büyük story’ler daha küçük olanlara bölünmelidir. Eğer bir story için “Bu  **21** ” diyorsanız ve “Bu aşırı ekstra büyük, sprint’e sığmaz” diye karar veriyorsanız, o zaman bu story daha küçük story’lere bölünmelidir.

Belki bir kısmı bu sprint’te, bir kısmı gelecek sprint’te yapılır. Ve belki de birden fazla sprint süreceğini takip etmek için bir *epic* oluştururuz.

---

## 🚫 Anti-Pattern: Story Point’leri “Süre”ye Çevirmek

Şimdi bazı  *anti-pattern* ’lerden bahsedelim; bunları anlamanız çok önemlidir.

İlk  *anti-pattern* , story’leri *wall clock time* üzerinden değerlendirmektir. Bunu sürekli görüyorum ve bu, organizasyonel  *anti-pattern* ’lerimize de bağlanıyor.

Şöyle oluyor: Bir *Scrum master* var; baştan *Scrum master* olarak başlamamış. Önceden  *project manager* ’mış.  *Gantt chart* ’larını seviyor. Peki *Gantt chart* nedir?  *Wall clock time* ’dır; takvimdeki tarihlerdir. Bu yüzden yalnızca takvim tarihleriyle düşünebilir.

Ve ben, eski *project manager* olan  *Scrum master* ’ların takıma şunu söylediğini gördüm:

> “ **1 = 1 gün** ,  **3 = 3 gün** ,  **5 = 5 gün** …”
> “…ya da 5 saat, 12 saat, her neyse.”

Bu yapılabilecek  **en yanlış şeydir** . Bu *wall clock time* ile ilgili değildir; sadece göreli büyüklüktür. *Medium* bazen 2–3 gün sürebilir, bazen 4 gün sürebilir. *Small* bir gün ya da bir günden az sürebilir.

Sadece bunun üzerinde bir tür “bulanıklık” ( *fuzziness* ) konusunda anlaşmanız gerekir. Ama **asla** ve **asla** takıma  *Fibonacci sequence* ’teki  *story point* ’lerin gün, hafta vb. olduğunu söylemeyin. Bu bir  *anti-pattern* ’dir.

İnsanlar *wall clock time* tahmin etmekte çok kötüdür. Bunu yapmayın.

---

## ✅ Video Özeti

Bu videoda şunları öğrendiniz:

* *Story point* ’ler, belirli bir  *user story* ’yi uygulamanın zorluğunu tahmin etmek için kullanılan bir metriktir.
* *Story point* ’ler, tişört bedenleri gibi göreli bir ölçektir.
* “Ortalama” ( *average / medium* ) ne demek, bunun üzerinde anlaşmanız gerekir.
* *Story point* ’leri asla *wall clock time* ile eşitlememelisiniz.
