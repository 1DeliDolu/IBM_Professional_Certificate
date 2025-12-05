# 🌦️ Historical Weather Forecast Comparison - Final Project

## 📋 Proje Açıklaması

Bu proje, Casablanca şehri için günlük hava durumu verilerini toplar ve tarihsel tahmin doğruluğunu ölçer.

## 📁 Dosyalar

- `rx_poc.sh` - Ana bash script dosyası (hava durumu verilerini çeker ve kaydeder)
- `rx_poc.log` - Hava durumu verileri log dosyası
- `weather_report` - Ham hava durumu verisi (script tarafından otomatik oluşturulur)
- `README.md` - Bu dosya

## 🚀 Kullanım

### 1. Script'i çalıştırılabilir yap

```bash
chmod u+x rx_poc.sh
```

### 2. Script'i çalıştır

```bash
./rx_poc.sh
```

Script şunları yapacak:

- wttr.in'den Casablanca için hava durumu verilerini indirir
- Anlık sıcaklığı çıkarır
- Yarın öğlen için tahmin edilen sıcaklığı çıkarır
- Tarihi (yıl, ay, gün) alır
- Tüm verileri `rx_poc.log` dosyasına ekler

### 3. Log dosyasını görüntüle

```bash
cat rx_poc.log
```

veya

```bash
column -t -s $'\t' rx_poc.log
```

## 📊 Log Dosyası Formatı

Log dosyası aşağıdaki sütunları içerir (sekme ile ayrılmış):

- `year` - Yıl
- `month` - Ay
- `day` - Gün
- `obs_temp` - Gözlemlenen sıcaklık (°C)
- `fc_temp` - Tahmin edilen sıcaklık (°C)

## ⏰ Otomatik Çalıştırma (Cron)

Script'i günlük olarak otomatik çalıştırmak için crontab'a ekleyin:

```bash
crontab -e
```

Aşağıdaki satırı ekleyin (her gün saat 12:00'de çalışır):

```bash
0 12 * * * cd /path/to/final_project && ./rx_poc.sh
```

## 📈 Analiz

Birkaç gün veri topladıktan sonra, tahmin doğruluğunu analiz edebilirsiniz:

```bash
# Log dosyasını görüntüle
cat rx_poc.log

# Satır sayısını kontrol et (başlık dahil)
wc -l rx_poc.log

# En son 10 kaydı göster
tail -10 rx_poc.log
```

## 🛠️ Gereksinimler

- Bash shell
- curl
- İnternet bağlantısı (wttr.in API'sine erişim için)

## 📝 Notlar

- Script, Casablanca için Morocco/Casablanca saat dilimini kullanır (UTC+1)
- Veriler wttr.in hava durumu servisinden alınır
- Her çalıştırmada log dosyasına yeni bir satır eklenir

## 🎯 Öğrenme Hedefleri

Bu projede şunları öğrendiniz:

- Bash scripting temelleri
- curl ile web scraping
- grep, cut, head, tail ile metin işleme
- Tarih ve saat yönetimi
- Log dosyası oluşturma ve yönetimi
- Cron ile zamanlanmış görevler

## 👨‍💻 Geliştirici

IBM Back-End Development Professional Certificate - Final Project
