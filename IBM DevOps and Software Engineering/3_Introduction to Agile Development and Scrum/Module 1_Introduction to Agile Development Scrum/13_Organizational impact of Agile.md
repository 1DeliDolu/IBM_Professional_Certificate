# 🏢 Organizational impact of Agile

Bu videoyu izledikten sonra, doğru organizasyonun başarıya nasıl katkıda bulunduğunu açıklayabilecek, takımların nasıl hizalanması gerektiğini anlatabilecek, özerkliğin neden önemli olduğunu açıklayabilecek ve Agile’ın etkili olabilmesi için tüm organizasyonun neden Agile’ı benimsemesi gerektiğini tartışabileceksiniz.

Başarı için organizasyonun ne kadar kritik olduğunu yeterince vurgulayamam. Birçok şirket bunu anlamıyor. Mevcut takımlarıyla yola çıkıyorlar ve bu takımları Agile yapacaklarını düşünüyorlar. Ancak fark etmedikleri şey şu: Agile olmanın tüm avantajlarından yararlanmak için mevcut takımlarınızın yeniden organize edilmesi gerekebilir.

---

## 🧩 Conway’s Law ve organizasyon yapısının tasarıma etkisi

1968’de Melvin Conway, bugün *Conway’s Law* olarak bilinen bir ifade ortaya koydu: Geniş anlamda bir sistemi tasarlayan herhangi bir organizasyon, yapısı organizasyonun iletişim yapısının bir kopyası olan bir tasarım üretecektir.

Bu şu anlama gelir: Eğer dört takımdan bir derleyici ( *compiler* ) yapmalarını isterseniz, dört geçişli ( *four pass* ) bir derleyici elde edersiniz. Dört takıma yaptırdınız; dört geçişli bir derleyici çıkmasına şaşırmamalısınız.

Benzer şekilde, bir *UI* takımı, bir uygulama ( *app* ) takımı ve bir veritabanı ( *database* ) takımınız varsa, üç katmanlı ( *three tier* ) bir mimari inşa ederler. Üç takıma yaptırdınız; üç katmanlı bir mimari çıkmasına şaşırmamalısınız.

---

## 🔗 Takımlar nasıl organize edilmeli?

Peki bu takımlar nasıl organize edilmeli? Hizalı ( *aligned* ) olmalılar. Gevşek bağlı ( *loosely coupled* ) olmalarını istersiniz. Takımlar arasında çok fazla bağımlılık ( *dependency* ) istemezsiniz; ancak tek bir uygulama inşa ettikleri için takımların sıkı biçimde hizalı ( *tightly aligned* ) olmasını istersiniz.

Sonrasında, her takımın kendi misyonu olmalıdır ve bu misyon iş hedefleriyle hizalı olmalıdır.

Eğer bir e-ticaret ( *e-commerce* ) uygulaması geliştiriyor olsaydım ve 50 geliştiricim olsaydı, monolitler ( *monoliths* ) inşa ettiğim zamanlarda yaptığım gibi hepsini tek büyük bir takıma koymazdım. Yapacağım şey onları daha küçük takımlara bölmek olurdu: bir sipariş ( *order* ) takımı, bir hesaplar ( *accounts* ) takımı, bir *shopkart* takımı, bir öneri ( *recommendation* ) takımı gibi; ve her biri o iş alanının sahipliğini ( *ownership* ) alırdı.

---

## 🛠️ Uçtan uca sorumluluk ve uzun vadeli misyon

Ardından takımın uçtan uca ( *end-to-end* ) sorumluluğu olmalıdır. İnşa etmelerini, çalıştırmalarını ve üretimde ( *production* ) hata ayıklamalarını istersiniz. Takım, inşa ettikleri şeyin uçtan uca sorumluluğunu taşımalıdır.

Ve son olarak, uzun vadeli bir misyona ihtiyaçları vardır. İnsanları projelere alıp çıkarma işi iyi çalışmaz; çünkü insanlar sahiplik duygusu hissetmez. Bu yüzden uzun vadeli misyon, iş başarısı için kritiktir.

---

## 🚀 Özerklik neden kritik?

Özerklik ( *autonomy* ) kritik derecede önemlidir. Motive edicidir ve motive olmuş insanlar daha iyi şeyler inşa eder; bu bir gerçektir.

Hızlıdır. Kararlar yukarıdan aşağıya gelmeyi beklemek yerine yerel olarak, takım seviyesinde alınır. İnsanları asıl yavaşlatan şey budur. Bu devri teslimleri ( *handoffs* ) ve beklemeleri azaltarak takımların tıkanmasını önlersiniz; kendi kararlarını verirler ve kendi hızlarında ilerlerler.

---

## 🧱 “Wall of confusion” ve Dev–Ops çatışması

Bu grafik,  *wall of confusion* , Andrew Clay Schafer tarafından ünlü hale getirildi; ancak tamamen geliştirme ( *development* ) ve operasyon ( *operations* ) tarafında kullandığımız birbirine zıt metriklerle ilgilidir.

Geliştirme değişim ister; üretime yeni değişiklikleri çıkarmakla ölçülür. Operasyon ise istikrarla ölçülür: sistemi nasıl stabil tutarsınız, hiçbir şeyi değiştirmeyin.

Bunlar birbirine taban tabana zıt bakış açılarıdır. Eğer organizasyonunuz bu bakış açılarını barındırıyorsa, ne kadar Agile olursanız olun, düşündüğünüz faydaları elde edemezsiniz.

---

## 🕰️ Organizasyon Agile olmazsa darboğaz kaçınılmazdır

Bu grafiği ben çizmedim ama bunun aynısı olan bir projede yer aldım. Agile çalışıyorduk. Ocak’ta başladık ve sprintlerle çalışıyorduk; sonunda Şubat ortasında deploy etmek istediğimiz bir şeyimiz vardı.

Operasyon takımına gittik ve şöyle dediler: “Bir ticket açın.” Tamam dedik, ticket açarız; bir hafta kadar içinde deploy edilir diye düşündük.

Ama ticket gittikçe ileri tarihe atıldı, ileri tarihe atıldı, ileri tarihe atıldı. Bekledik, daha fazla fonksiyon geliştirdik ama yine de deploy edilmedi. En sonunda uygulama Eylül’de deploy edildi ve ben Aralık’ta projeden ayrıldım. Artık dayanamadım.

Buradaki ders şu: Tüm organizasyon Agile olmazsa, geliştirme takımınızın Agile olması hiçbir şeyi değiştirmez. Operasyon takımınız Agile değilse, işte *DevOps* tam da bununla ilgilidir.

Agile olmanın tüm avantajlarından yararlanmak istiyorsanız, DevOps’u benimsemeyi gerçekten düşünmelisiniz. Aksi halde, ops takımı Agile geliştirme takımını yakalayana kadar sadece bekler ve beklersiniz.

---

## 🤝 Agile ve DevOps hizalanması

Agile ve DevOps’un hizalanmasına bakalım. Agile’ın hedeflerinden biri yazılımı daha hızlı teslim etmektir. DevOps’un hedefi de pazara çıkış süresini ( *time to market* ) hızlandırmaktır; mükemmel biçimde hizalıdır.

Agile’da değişime duyarlı olmak isteriz. DevOps’ta ise iş değeri üretmek için BT organizasyonunu iş ile sıkı biçimde hizalamaya çalışırız.

Agile’da daha yüksek kalite elde etmeye odaklanırız; DevOps’ta BT’nin verimliliğini artırmaya çalışırız. Bu iki hedef de hizalıdır.

Bu yüzden çoğu zaman, Agile olmanın tam faydasını elde etmek istiyorsanız, ops takımının da geliştirme takımı kadar Agile olabilmesi için DevOps’u bir pratik olarak benimsemeyi de düşünmelisiniz.

---

## ✅ Video özeti

Bu videoda, nasıl organize olduğunuzun inşa ettiğiniz sistemleri etkileyebileceğini öğrendiniz. Takımlara özerklik vermek, daha hızlı çalışabilen ve daha iyi sistemler inşa eden motive takımlara yol açar. Organizasyon genelinde Agile’ı benimsememek operasyonel darboğazlara yol açabilir ve Agile ile DevOps’un hedefleri birbiriyle yakından hizalıdır.
