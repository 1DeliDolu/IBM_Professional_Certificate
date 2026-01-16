## 🧾 Git ve GitHub’a Başlarken: Özet

### 🧠 1. Git ve GitHub Temelleri

#### 🚀 1.1 Git ve GitHub ile başlarken

Dağıtık bir sürüm kontrol sistemi (DVCS), kodun nerede saklandığından bağımsız olarak koddaki değişiklikleri takip eder. Bu, birden fazla kullanıcının aynı kod tabanı veya depo ( *repository* ) üzerinde çalışmasına olanak tanır; gerekirse kullanıcılar kod tabanını kendi bilgisayarlarında kopyalayabilirken, dağıtık sürüm kontrol yazılımı çeşitli kod tabanı kopyaları arasındaki senkronizasyonun yönetilmesine yardımcı olur.

Depolar ( *repositories* ), aşağıdakileri yapan depolama yapılarıdır:

* Kodu saklar
* Sorunları ve değişiklikleri takip eder
* Başkalarıyla iş birliği yapmanızı sağlar

GitHub, Git depoları için en popüler web barındırmalı hizmetlerden biridir. GitLab, Bitbucket ve Beanstalk; barındırılan sürüm kontrol sistemlerine örnektir.

---

## 🛠️ Git Komutlarını Kullanma ve GitHub Projelerini Yönetme

### 🌿 2.1 Branch’ler ve Git komutları ile GitHub iş akışları

Branch’ler, koddaki değişiklikleri izole etmek için kullanılır. Değişiklikler tamamlandığında, tekrar ana branch’e birleştirilebilir ( *merged* ).

Depolar, yerelde çalışmayı mümkün kılmak için klonlanabilir ( *cloned* ), ardından değişiklikler tekrar orijinale senkronize edilebilir.

Depolar, yeni bir proje için temel olarak kullanılmak üzere veya geliştiricinin bağımsız çalışabilmesi için çatallanabilir ( *forked* ).

Değişikliklerinizin gözden geçirilmesi ve birleştirilmesi için bir *pull request (PR)* gönderilebilir.

Büyük projelerde farklı rollerde çalışan kişiler bulunur:

* Geliştirici ( *Developer* ): Kod oluşturur
* Entegratör ( *Integrator* ): Geliştiriciler tarafından yapılan değişiklikleri yönetir
* Depo Yöneticisi ( *Repository Administrator* ): Depoya erişimi yapılandırır ve sürdürür
