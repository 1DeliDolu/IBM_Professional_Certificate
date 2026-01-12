# 📏 Ölçümleri Etkili Kullanma

Bu videoyu izledikten sonra, *gösteriş metrikleri* ile *uygulanabilir metrikler* arasındaki farkı açıklayabileceksiniz. En iyi dört uygulanabilir metriği tanımlayabilecek ve metriklerin ekibin performansını iyileştirmek için nasıl kullanılabileceğini açıklayabileceksiniz.

Metriklere sahip olmak kritik derecede önemlidir, çünkü ölçemediğiniz şeyi iyileştiremezsiniz. Nasıl gittiğinizi ölçebilmeniz gerekir; sadece içgüdüye dayanamazsınız. Yüksek performanslı ekipler, nasıl gittiklerini ölçer; bu ölçümlere tepki verir ve bunların doğru yönde ilerlediğinden emin olur. Bu yüzden temel seviyeleri belirler, hedefler koyar ve sonra bu hedeflere göre ölçüm yaparlar. Bu, ekibinizin sağlığı için son derece, son derece önemlidir.

---

## ⚠️ Gösteriş Metriklerine Dikkat

Gösteriş metriklerine karşı dikkatli olun. Web sitemize 10.000 hit geldi. Hadi pizza partisi yapalım. 10.000 hit ne demek? Gerçekte ne anlama geliyor? Birisi sinirli şekilde 10.000 kez mi tıkladı? 10.000 kişi birer kez tıklayıp gitti mi?

Bilmiyorsunuz, hiçbir fikriniz yok. Onları web sitesine neyin getirdiğini bilmiyorsunuz ve sonraki adımda hangi aksiyonu alacağınızı da bilmiyorsunuz. Nasıl daha fazla tıklama alırım? Bilmiyorum; bir web sitesine gelen tıklamalar ya da hit’ler sadece bir  *gösteriş metriğidir* .

---

## 🎯 Uygulanabilir Metriklere Odaklanma

*Uygulanabilir metrikler* üzerinde çalışmak istersiniz. Diyelim ki bir *A/B split-testing* yapıyorsunuz, değil mi? İki farklı sürümünüz var; müşterilerin hangisini seveceğini bilmiyorsunuz.

Bu yüzden trafiği şekillendirirsiniz: %50’yi bir müşteri grubuna, %50’yi diğerine yönlendirirsiniz. Sonra ölçersiniz, değil mi? Yeni özelliği gören müşteriler, istediğimiz gibi mi tepki verdi? Onlardan beklediğimiz davranışı aldık mı? Eğer aldıysak, o davranışı daha fazla yapalım. Eğer almadıysak, o davranışı daha fazla yapmayalım, değil mi? Daha az yapalım.

---

## 📌 Temel Seviye Belirleme ve Hedef Koyma

Bir temel seviye almanız kritik önem taşır; bu temel seviye her neyse. Diyelim ki şu anda bir deploy’a çıkmak için altı ekip ve 10 saat gerekiyor.

Ve bunu azaltmak istiyorsunuz; ya da bir release yapmak şu kadar paraya mal oluyor, her neyse. Temel seviye nasıl tanımlanmışsa, iyileştirmek istediğiniz bir şeyi seçersiniz; sonra bugün nasıl olduğuna göre ölçersiniz, o temel seviyeyi belirlersiniz ve ardından kendinize bir hedef koyarsınız. Belki 10 saatten iki saate düşürmek istersiniz ve bunu nasıl yapabilirim diye düşünürsünüz, değil mi?

Sonra ölçersiniz: Yaklaşıyor muyuz? İlk seferde başaramayacaksınız, değil mi? Bu, bir dizi sprint boyunca olacak: Daha mı hızlanıyoruz? Daha mı iyi oluyoruz? Daha mı az maliyetli hale geliyor? Prod’da daha çok bug mu buluyoruz? Pardon, testte daha çok bug buluyoruz, değil mi? Prod’da daha çok bug bulmak istemezsiniz. Testte, prod’a göre daha fazla bug yakalıyor muyuz?

Değil mi? Bu da bize daha az para harcatır ve *break fix* maliyetini düşürür. Her neyse; bir hedef belirlemek ve ona göre ölçmek istersiniz.

---

## 📊 En İyi Dört Uygulanabilir Metrik

İnsanların kullandığı en iyi dört uygulanabilir metrik şunlardır:

* *Ortalama lead time* (mean lead time), değil mi? Bir fikirden, müşteriye bir şey teslim etmeye kadar ne kadar sürüyor?
* *Release frequency* (yayınlama sıklığı): Ne kadar sık release yapabiliyorsunuz? İhtiyacınızdan daha hızlı olmak zorunda değil. Haftada bir release yeterliyse, sorun yok. Ama müşteriye yeni bir şey sunmanız gerektiğinde release yapabiliyor musunuz?
* *Change failure rate* (değişiklik başarısızlık oranı), değil mi? Bozan şeyler mi release ediyorsunuz? Bu da kritik derecede önemli.
* *Mean time to recovery* (ortalama toparlanma süresi). Eskiden *mean time to failure* idi, değil mi? “Asla hata yapmayalım, asla düşmesin.” Olacak; düşecek. Soru şu: düştüğünde ne kadar hızlı toparlanabiliyorsunuz?

Eğer yeterince hızlıysa ve müşteri bunu fark etmiyorsa, bu her şeyin en iyisidir. Bu nedenle, *mean time to recovery* bugün insanların uygulanabilir bir metrik olarak ölçtüğü şeydir.

---

## 🧭 Örnek Metrikler

Bazı örnek metriklere bakalım, değil mi?

* Yeni özellikler için pazara çıkış süresini azaltmak, değil mi? Yeni bir özelliği dışarı çıkarmam ne kadar sürüyor? Günler mi? Haftalar mı? Aylar mı?
* Ürünün genel erişilebilirliğini artırmak, değil mi? Belki daha yüksek erişilebilirlik istiyorsunuz.
* Release deploy etmek için gereken süreyi azaltmak. Bu, yaygın bir metriktir, değil mi? Release’leri daha hızlı çıkarabilmek istersiniz.
* Prod’a çıkmadan önce testte yakalanan defect yüzdesini artırmak; çünkü bu uzun vadede size para kazandırır.
* Performans ve kullanıcı geri bildirimini ekibe zamanında sağlamak, değil mi? Hızlı geri bildirim döngülerim var mı? Müşteriden ekibime geri bildirim alabiliyor muyum? Belki bunu daha hızlı yapmak istiyorum; çok uzun sürmesini istemiyorum.

Bu metrikler her neyse, içlerinden birini seçip onun üzerinde iyileştirme yapmak istersiniz.

---

## ✅ Öğrenilenler

Bu videoda, yüksek performanslı ekiplerin metrikleri sürekli iyileştirme için kullandığını öğrendiniz. Kullandığınız metriklerin uygulanabilir olduğundan emin olmak önemlidir. Değişimi ölçmeye başlamadan önce bir temel seviye almak önemlidir.

Ve en iyi dört uygulanabilir metrik, ekibinizin genel performansını iyileştirmek için kullanılabilir.
