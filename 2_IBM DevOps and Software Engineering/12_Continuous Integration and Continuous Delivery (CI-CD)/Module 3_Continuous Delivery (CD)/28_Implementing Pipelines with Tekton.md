# 🏁 Özet ve Öne Çıkanlar: Tekton ile Pipeline’ları Uygulama

Tebrikler! Bu dersi tamamladınız. Kursun bu noktasında şunları biliyorsunuz:

Tekton’un kavramsal yapı taşları  *events* ,  *triggers* ,  *pipelines* , *tasks* ve  *steps* ’tir.

Tekton’un fiziksel yapı taşları Kubernetes *custom resource definitions* (CRD’ler)dir.

Gerekli parametreleri geçirerek görevleri referans gösterip Tekton pipeline’ları oluşturabilirsiniz.

*EventListeners* harici olayları dinler, *TriggerBindings* bu olaylara yanıt verip bunlardan parametreleri bağlar ve *TriggerTemplates* parametreleri pipeline’a ileten  *PipelineRun* ’lar oluşturur.

Tekton Catalog veya Tekton Hub, CI/CD pipeline’larınız için yeniden kullanılabilir görevler içerir.

*PipelineRun* workspace’i bir *PersistentVolumeClaim* ile eşlemelidir.

Görevler içinde mevcut shell script’lerini kullanabilir ve yapılandırma bilgilerini görevlere geçirmek için environment variable’lar tanımlayabilirsiniz.

CI/CD pipeline’larınız için build görevlerini bulmak üzere Tekton Hub veya Tekton CLI kullanabilirsiniz.

Paralel görevlerden sonra bir görevi çalıştırmak için, paralel görevleri `runAfter` alanında belirtmeniz gerekir.

Uygulamaları bir ortama komutlar veya YAML manifestleri kullanarak dağıtabilirsiniz.
