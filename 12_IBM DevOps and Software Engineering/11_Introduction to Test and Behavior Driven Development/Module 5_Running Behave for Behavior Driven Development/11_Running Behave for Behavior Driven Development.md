# 🧪 Modül 5 Özeti: Davranış Odaklı Geliştirme için Behave Çalıştırma

Tebrikler! Bu modülü tamamladınız. Kursun bu noktasında şunları biliyorsunuz:

Behave, eksik olan tüm Python adımlarını raporlar ve bunlar için kullanabileceğiniz kod parçacıkları önerir.

Bu kod ile adım dosyanızı oluşturmak için bir başlangıç noktanız olur.

---

## 🔁 Python Adımlarını Uygulama İş Akışı

Python adımlarını uygulama iş akışı aşağıdaki gibidir:

* Bir adımı uygula
* Behave’i çalıştır ve adımın geçtiğinden emin ol
* Başarısız olan bir sonraki adımı uygula
* Behave’i çalıştır ve bu adımın geçtiğinden emin ol
* Tüm adımlar geçene kadar bu süreci tekrarla

---

## 🧳 Context Kullanımı

 *Context* , her adım tanımına geçirilen bir değişkendir.

Adımlar arasında bilgi aktarmak için, bilgiyi bir adımın *context* değişkeninde saklayıp başka bir adımda bu değişkeni kullanırsınız.

---

## 🧩 Değişken Yerine Koyma

Değişken yerine koyma, gereken adım sayısını azaltır ve yeniden kullanımı en üst düzeye çıkarır.

Değişkenleri yerine koymak için şu süreci izlersiniz:

* Decorator dizesindeki verileri, süslü parantezler `{}` içine alınmış değişkenlerle değiştir.
* Bu değişkenlerle aynı isimlere sahip adım uygulama parametreleri ekle.
* Feature dosyasından gelen stringler yerine bu değişken adlarını kullan.
