# 📊 Modül 4 Özeti: Python'da Verilerle Çalışmak

🎉 Tebrikler! Bu modülü tamamladınız. Bu noktada şunları biliyorsunuz:

---

## 📁 Dosyalarla Çalışma ve `open()` Fonksiyonu

Python, `open()` fonksiyonunu kullanır ve dosyaları okumanıza ve yazmanıza olanak tanır; dosyanın içeriğine okuma için erişim sağlar. Ayrıca, yazma için dosyanın üzerine yazmaya izin verir ve dosya kipini belirtir (örneğin, okuma için `r`, yazma için `w`, ekleme için `a`).

Bir dosyayı okumak için Python, `open` fonksiyonunu `r` ile birlikte kullanır.

Python, bir dosya özniteliğini okumak ve işlemek için `open` ile birlikte `with` fonksiyonunu kullanır, yani açmadan kapamaya kadar olan süreçte.

Python’da bir dosyayı düzenlemek veya üzerine yazmak için `open` metodunu kullanırsınız.

Bir dosyaya yazmak için Python, `open` fonksiyonunu `w` ile birlikte kullanır.

Python’da `a`, programın dosyaya ekleme ( *append* ) işlemi yaptığını belirtir.

Python’da `"\n"`, kodun yeni bir satırdan başlaması gerektiğini ifade eder.

Python, özniteliklerden satırları yazdırmak için çeşitli yöntemler kullanır.

---

## 🐼 Pandas ve DataFrame'lerle Çalışma

Pandas, veri manipülasyonu ve analizi için güçlü bir Python kütüphanesidir; veri çerçeveleri ( *data frames* ) ve seriler ( *series* ) gibi yapılandırılmış verilerle çalışmak için veri yapıları ve fonksiyonlar sağlar.

Dosyayı (panda) içe aktarmak için `import` komutunu, ardından dosya adını kullanırsınız.

Python’da bir dosya için daha kısa bir ad sağlamak amacıyla `as` komutunu kullanırsınız.

Pandas’ta, okunacak dosyaları belirtmek için bir veri çerçevesi ( *data frame* , `df`) kullanırsınız.

 *DataFrame* ’ler satırlardan ve sütunlardan oluşur.

Belirli bir  *DataFrame* ’in sütununu veya sütunlarını kullanarak yeni  *DataFrame* ’ler oluşturabilirsiniz.

Bir *DataFrame* içindeki verilerle çalışabilir ve sonuçları farklı formatlarda kaydedebiliriz.

Python’da, bir  *DataFrame* ’in sütunundaki benzersiz elemanları belirlemek için `Unique` metodunu kullanırsınız.

*DataFrames* içinde seçili sütuna Boolean bir değer atamak için, eşitsizlik ( *inequality* ) operatörünü `df` ile birlikte kullanırsınız.

Yeni bir  *DataFrame* ’i, daha önceki bir  *DataFrame* ’den değerler içerebilecek farklı bir *DataFrame* olarak kaydedersiniz.

---

## 🔢 NumPy Temelleri ve Vektör İşlemleri

NumPy, sayısal ve matris işlemleri için bir Python kütüphanesidir; verilerle verimli bir şekilde çalışmak üzere çok boyutlu dizi nesneleri ve çeşitli matematiksel fonksiyonlar sunar.

NumPy, Pandas için bir temeldir.

Bir NumPy dizisi veya  *ND array* , genellikle sabit boyutlu ve aynı türden elemanlar içeren bir listeye benzer.

Tek boyutlu bir NumPy dizisi, tek eksenli, geleneksel bir listeye benzeyen doğrusal bir eleman dizisidir; ancak sayısal hesaplamalar ve dizi işlemleri için optimize edilmiştir.

NumPy içinde elemanlara bir indeks kullanarak erişebilirsiniz.

Dizi elemanlarının veri tipini elde etmek için `dtype` özniteliğini kullanırsınız.

Dizinin boyutunu ve boyut sayısını ( *dimension* ) sırasıyla elde etmek için `size` ve `ndim` kullanırsınız.

NumPy’da indeksleme ve dilimleme ( *slicing* ) yöntemlerini kullanabilirsiniz.

Vektör toplamları, Python’da yaygın olarak kullanılan işlemlerdir.

Vektör toplamını doğru parçalar veya oklarla temsil etmek faydalıdır.

NumPy kodları çok daha hızlı çalışır; bu da çok miktarda veriyle çalışırken yararlıdır.

Vektör çıkarmayı, toplama işaretini eksi işaretiyle değiştirerek gerçekleştirirsiniz.

Python’da bir diziyi bir skaler ile çarpmak, dizinin her bir elemanını skaler değerle çarpmayı içerir; bu da her elemanın skalerle ölçeklendiği yeni bir dizi ortaya çıkarır.

 *Hadamard product* , aynı şekle sahip iki dizinin eleman bazında çarpımına karşılık gelir; sonuçta, her elemanı giriş dizilerindeki karşılık gelen elemanların çarpımı olan yeni bir dizi elde edilir.

Python’da *dot product* (nokta çarpımı), iki dizinin eleman bazlı çarpımlarının toplamıdır ve genellikle vektör ve matris işlemlerinde, karşılık gelen elemanları çarpıp toplayarak skaler bir sonuç bulmak için kullanılır.

NumPy ile çalışırken, NumPy dizilerinde saklanan sayısal verilerden grafikler ve görselleştirmeler oluşturmak için Matplotlib gibi kütüphaneleri kullanmak yaygındır.

---

## 🧮 İki Boyutlu NumPy Dizileri ve Dizinin Özellikleri

İki boyutlu bir NumPy dizisi, satırlar ve sütunlardan oluşan, sayısal hesaplamalar için verileri matris veya tablo şeklinde temsil etmeye uygun ızgara benzeri bir yapıdır.

NumPy’da `shape`, bir dizinin boyutlarına (satır ve sütun sayısı) karşılık gelir ve dizinin büyüklüğünü ve yapısını ifade eder.

Bir dizinin boyutunu ( *size* ) elde etmek için `size` özniteliğini kullanırsınız.

Bir dizideki çeşitli elemanlara erişmek için dikdörtgen benzeri köşeli öznitelikleri (köşeli parantezleri) kullanırsınız.

NumPy’da elemanları çarpmak için bir skaler kullanırsınız.
