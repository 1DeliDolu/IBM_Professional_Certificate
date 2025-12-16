# 🧰 Kanban ve Agile Planlama Araçları

Bu videoyu izledikten sonra, bir Kanban panosunun ne olduğunu açıklayabilecek, her bir  *pipeline* ’ın ne için kullanıldığını anlatabilecek ve bir Kanban panosu üzerindeki iş akışını özetleyebileceksiniz.

Agile planlama araçlarının pek çoğu var. Ancak anlamanız gereken bir şey var: Bir araç sizi *Agile* yapmaz; Agile olmak için gerçekten Agile zihniyetine sahip olmanız gerekir. Araçlar Agile sürecinizi destekler, ama önce sürecin kendisine sahip olmanız gerekir.

Eğitim almamış birçok kişinin bir Kanban panosunu bir Gantt şeması gibi göstermeye çalıştığını gördüm. Bunlar iki farklı şeydir, proje yönetiminin iki farklı yoludur. Bu yüzden bunu anlamanız gerçekten önemlidir.

Agile planlama araçları çok ama çok fazladır. Çoğu aynı şeyi yapar, ancak bazıları diğerlerinden biraz daha karmaşıktır. Ben planlarımı tanımlamak için sadece  *epic* ’lere ve  *story* ’lere ihtiyaç duyarım. Bazıları görevler ve alt görevler (*tasks* ve  *subtasks* ) seviyesine iner. Ben bunu istemiyorum; bana göre bu mikro yönetimdir, değil mi? Sadece  *epic* ’ler ve  *story* ’ler yeterli. Bu yüzden ZenHub adlı bir aracı kullanmayı seviyorum. Ve bu kursta ZenHub kullanacağız.

---

## 🔌 ZenHub Nedir?

Peki ZenHub nedir? GitHub için bir eklentidir. Sevmemin nedenlerinden biri de budur.

Geliştiricilerim GitHub’da kalır ve bu ZenHub eklentisini kullanırlar. ZenHub’un yaptığı şey, GitHub’da kalmaya devam ederken projelerinizi yönetebilmeniz için proje yönetimi araçları ve bir Kanban panosu eklemenize izin vermesidir. Bu benim için oldukça önemlidir.

Bir diğer nokta da ZenHub’un özelleştirilebilir olmasıdır. Kanban panonuzda *pipeline* olarak adlandırılan bir sütun setiyle başlar, ancak bunları istediğiniz şekilde özelleştirebilirsiniz. İsterseniz karmaşık, isterseniz basit yapabilirsiniz. Ben basit tutmayı severim.

---

## 🎯 Neden Kullanıyoruz?

Peki neden kullanıyoruz? Ana sebeplerden biri, GitHub  *issue* ’larını kullanmasıdır. Başka bir şeye gidip düzenlemem gereken başka bir araç değildir.

Benim gördüğüm sorunlardan biri şudur: Çok fazla araç kullanıyorsanız ve bir geliştiricinin durumu güncellemek için başka bir yere gitmesi gerekiyorsa, o durum %100 ihtimalle her zaman güncelliğini yitirecektir. Çünkü güncelledikleri anda başka bir şeye geçecekler ve bu durum statüye yansımayacaktır.

Bu nedenle ZenHub’u seviyorum. Neler olup bittiğini anlamak için kolay bir yol sunar. Kanban panom GitHub’dadır. Ve biri bana “Proje nasıl gidiyor? Yönetim nerede olduğunuzu bilmek istiyor,” derse, ZenHub Kanban panosunu açabilirler; sprintte hâlâ duran, üzerinde çalışılmamış tüm  *issue* ’ları görebilirler. Şu anda üzerinde çalışılan tüm  *issue* ’ları ve kimin çalıştığını görebilirler. Ayrıca tamamladığımız tüm  *issue* ’ları da görebilirler.

Bir projede nerede olduğumuzun hızlı bir durum bilgisini almak için bu çok ama çok önemlidir.

Ve dediğim gibi, güncel, tek bir doğru versiyonu ( *one version of the truth* ) korur. Geliştiriciler gün boyunca GitHub’da  *story* ’ler üzerinde çalışır. GitHub’daki  *issue* ’lar (yani  *story* ’ler) açıp kapattıkları şeylerdir ve durum güncellemek için başka bir yere gitmeleri gerekmez. Durum kendi favori araçları GitHub’ın içinde tutulur.

Böylece geliştiriciler işi bitirmek için tek bir yere gidebilir ve birden fazla aracı güncellemek zorunda kalmaz.

---

## 🧱 Kanban Panosu Nedir?

Peki Kanban panosu nedir? Burada Kanban panolarından bahsediyoruz. Çok basitçe:

* Yapmanız gereken şeyler
* Yaptığınız şeyler
* Zaten tamamladığınız şeyler

Bundan daha karmaşık olmak zorunda değildir. İnsanlar bunu çok ama çok karmaşık hâle getirir. Ama bir bakıma “neyi yapmam lazım, şu an ne üzerinde çalışıyorum, neleri tamamladım” gibi düşünebilirsiniz.

İlerlemeyi göstermek için işleri Kanban panosu üzerinde hareket ettirirsiniz; bu da herhangi bir zamanda tam olarak nerede olduğunuzu görmenin çok görsel bir yoludur.

Şimdi, işte gerçek bir Kanban panosu. Gördüğünüz gibi bir *product backlog* var.

Ayrıca “on deck”, “doing” ve “done” var. Çok basit tutulmuş, ama bu gerçek bir Kanban panosu. Bir araç değil. Elektronik bir şey değil. Üzerinde bir sürü post-it olan fiziksel bir beyaz tahta.

Kanban’ın gerçek mantığında, yani bir panonun, tedarik zinciri gibi üretim zinciri gibi hareket eden not mantığında, yaptıkları budur. Bir post-it alırsınız, üzerine  *story* ’yi yazarsınız. Sonra bu post-it’i sütunlar boyunca beyaz tahta üzerinde hareket ettirirsiniz. Yani Kanban panosu olması gereken kadar basittir.

---

## 🧭 ZenHub’daki Varsayılan Pipeline’lar

ZenHub’daki varsayılan *pipeline* ya da sütunlardan bahsedelim.

---

## 📥 New Issues

İlk olarak *new issues* ile başlar.  *New issues* , gelen kutunuz ( *inbox* ) gibidir. Birisi bir *issue* açtığında, varsayılan olarak *new issues* sütununa düşer.

Ben orada çok uzun süre kalmasını sevmem. *Backlog refinement* yaparken ve Kanban panom üzerinde çalışırken genellikle önce *new issue triage* yaparım ve “bu az önce geldi, nereye gitmeli?” derim. Sonra başka bir  *pipeline* ’a taşırım ya da reddederim.

Ama *new issues* içinde tutmam; çünkü yeni bir tane geldiğinde “aa bu gerçekten yeni olmalı, çünkü ben az önce burayı temizledim” diyebilmek isterim. Tıpkı e-posta gelen kutusu gibi.

---

## 🧊 Icebox

Sonra *icebox* vardır. Bu ZenHub’a özgüdür ama ben seviyorum. *Icebox* soğuk depodur ( *cold storage* ).

Uzun vadede çalışacağınız şeyleri koyduğunuz yerdir. Eğer bir şeye bir süre dokunmayacaksam, unutmayayım diye  *icebox* ’a atarım.

Ama böylece aktif olarak çalıştığım diğer  *pipeline* ’larda bulunmaz ve ortalık fazla kalabalık olmaz.

---

## 📚 Product Backlog

 *Icebox* ’tan sonra *product backlog* gelir.  *Product backlog* , ürününüzde sonsuza kadar yapmak isteyeceğiniz ve henüz yapmadığınız her şeydir.

Yani yaptığınız şeyleri içermez. Henüz bir sprint’e koymadığınız, gelecekte bir zamanda üzerinde çalışmak istediğiniz her şeyi içerir.

Ve yine, *product backlog* çok kalabalık olmasın diye, uzun vadeli şeyleri  *icebox* ’a taşımayı severim.

---

## 🏁 Sprint Backlog

Sonra *sprint backlog* gelir.  *Sprint backlog* , önümüzdeki iki haftada yapacağımız şeydir.

Yani  *product backlog* ’dan bazı şeyleri alıp  *sprint backlog* ’a taşırım ve bir sprint planı yaparım.

Geliştiricilerin bu diğer  *pipeline* ’ların hiçbirini dert etmesine gerek yoktur; onlar sadece  *sprint backlog* ’a odaklanır, çünkü bir sonraki sprint’te yapacağımız iş budur.

---

## 🔧 In-Progress

Sonra bir şeyler üzerinde çalışmaya başladığımızda, onları  *in-progress* ’e taşırız.

Böylece *in progress* sütununda o kartları, o  *story* ’leri gördüğümde birinin onlar üzerinde çalıştığını bilirim; çünkü kendilerine atadıklarında küçük avatarları görünür.

Yani tam olarak kimin ne üzerinde çalıştığını ve şu anda nelerin işlendiğini görebilirim.

---

## 🔍 Review QA

İş tamamlandığında, bir geliştirici genellikle çalışmasını temel dala ( *base branch* ) geri çekmek için bir *pull request* oluşturur.

Bunlar  *review QA* ’a gider. Ayrıca GitHub ve ZenHub’u, *review QA* sütununda otomatik olarak *pull request* oluşturacak şekilde de ayarlayabilirsiniz.

Böylece geliştiriciler, orada bir şeyin belirdiğini gördüklerinde, gidip bakmaları gerektiğini, başka bir geliştiriciye yardım etmeleri gerektiğini, o  *story* ’yi gözden geçirmeleri ve kodun geri kalanına merge edilmek için gereken kriterleri karşıladığından emin olmaları gerektiğini bilirler.

---

## ✅ Done

Ve son olarak *done* sütunu vardır. Tamamen bitirdiğimizde, kodumuzu geri merge ettiğimizde,  *story* ’yi  *done* ’a taşırız.

*Done* demek, geliştiricinin işi bitirdiği anlamına gelir. Ürün sahibinin ( *product owner* ) kabul ettiği anlamına gelmez. Bu sprint review sırasında gerçekleşen bir şeydir.

Ama geliştiricinin o *story* ile işi bittiği anlamına gelir. Sonra geliştirici tekrar  *sprint backlog* ’a döner, bir  *story* ’yi  *in-progress* ’e çeker, kendine atar ve çalışmaya devam eder.

Dolayısıyla akış soldan sağa doğrudur. Yeni  *story* ’ler soldan gelir ve sonunda sağ taraftan *done increment* çıkar.

![1765879529890](image/3_KanbanandAgilePlanningTools/1765879529890.png)

---

## ✅ Video Özeti

Bu videoda, bir Kanban panosunun planlanan ve yapılması gereken öğeleri, devam eden işleri ve tamamlanan işleri takip etmenin bir yolu olduğunu öğrendiniz.

Bir Kanban panosu birden fazla  *pipeline* ’dan oluşur.

İş tamamlandıkça soldan sağa doğru hareket eder.
