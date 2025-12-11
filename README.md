# TEKNİK SERVİS YÖNETİM SİSTEMİ

![Version](https://img.shields.io/badge/version-1.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

## 📋 Proje Özeti

Telefon, tablet, bilgisayar ve elektronik cihaz tamir/bakım hizmeti veren işletmeler için tasarlanmış kapsamlı bir masaüstü yönetim sistemi. Sistem; müşteri yönetimi, cihaz takibi, servis kayıtları, stok yönetimi, cari hesap takibi ve finansal raporlama modüllerini içermektedir.

## 🚀 Özellikler

### Temel Modüller

- ✅ **Müşteri Yönetimi** - Bireysel ve kurumsal müşteri takibi
- ✅ **Servis Yönetimi** - Kapsamlı servis kayıt ve takip sistemi
- ✅ **Cihaz Yönetimi** - IMEI/Seri no ile cihaz takibi
- ✅ **Stok Yönetimi** - Parça ve malzeme takibi
- ✅ **Cari Hesap** - Alacak/borç yönetimi
- ✅ **Kasa Yönetimi** - Gelir/gider takibi
- ✅ **Raporlama** - Detaylı finansal ve operasyonel raporlar
- ✅ **E-posta Entegrasyonu** - SMTP desteği ve HTML şablonlar
- ✅ **SMS/WhatsApp** - Müşteri bilgilendirme
- ✅ **Yazıcı Desteği** - Termal ve A4 yazıcı entegrasyonu

### Gelişmiş Özellikler

- 🔐 Çoklu kullanıcı ve rol bazlı yetkilendirme
- 📊 Gerçek zamanlı dashboard ve istatistikler
- 🏷️ Barkod/QR kod desteği
- 📧 Otomatik e-posta bildirimleri
- 💾 Otomatik yedekleme sistemi
- 🌓 Açık/koyu tema desteği
- ⌨️ Klavye kısayolları
- 📱 Online servis takip sistemi

## 🛠️ Teknoloji Stack

| Katman | Teknoloji | Açıklama |
|--------|-----------|----------|
| **Programlama Dili** | Python 3.11+ | Ana geliştirme dili |
| **GUI Framework** | PyQt6 / PySide6 | Modern masaüstü arayüz |
| **Veritabanı** | SQLite | Gömülü veritabanı |
| **ORM** | SQLAlchemy | Veritabanı soyutlama |
| **Raporlama** | ReportLab | PDF oluşturma |
| **Barkod/QR** | python-barcode, qrcode | Etiketleme |
| **Yazıcı** | ESC/POS, win32print | Termal ve A4 yazıcı |
| **E-posta** | SMTP, Jinja2 | E-posta gönderimi |

## 📦 Kurulum

### Gereksinimler

- Python 3.11 veya üzeri
- pip (Python paket yöneticisi)
- Windows 10/11 (diğer platformlar için test edilmemiştir)

### Adımlar

1. **Projeyi klonlayın:**
```bash
git clone https://github.com/unaluslusoy/TeknikServisYazilim.git
cd TeknikServisYazilim
```

2. **Sanal ortam oluşturun (önerilir):**
```bash
python -m venv venv
venv\Scripts\activate
```

3. **Bağımlılıkları yükleyin:**
```bash
pip install -r requirements.txt
```

4. **Veritabanını başlatın:**
```bash
python database/migrations/init_db.py
```

5. **Uygulamayı çalıştırın:**
```bash
python main.py
```

## 📊 Veritabanı Yapısı

### Ana Tablolar

#### 🧑 Customers (Müşteriler)
- Bireysel ve kurumsal müşteri bilgileri
- TC/Vergi no ile kayıt
- Cari bakiye takibi
- İletişim geçmişi

#### 📱 Devices (Cihazlar)
- Cihaz tipi, marka, model
- IMEI/Seri numarası
- Fiziksel durum kaydı
- Aksesuar takibi

#### 🔧 Service Orders (Servis Emirleri)
- Kapsamlı servis takibi
- 10 farklı durum seçeneği
- Öncelik seviyesi
- Maliyet hesaplama

#### 📦 Inventory (Stok)
- Parça ve malzeme yönetimi
- Minimum stok uyarısı
- Tedarikçi entegrasyonu
- Barkod desteği

#### 💰 Account Transactions (Cari Hesap)
- Alacak/borç hareketleri
- Ödeme yöntemleri
- Bakiye takibi
- Ekstre oluşturma

### Servis Durumları

| Kod | Türkçe | Açıklama |
|-----|--------|----------|
| `pending` | Beklemede | Yeni kayıt, henüz işlem başlamadı |
| `diagnosing` | Teşhis Aşamasında | Arıza tespiti yapılıyor |
| `waiting_approval` | Onay Bekleniyor | Müşteri onayı bekleniyor |
| `waiting_part` | Parça Bekleniyor | Yedek parça tedarik ediliyor |
| `in_progress` | İşlemde | Onarım devam ediyor |
| `testing` | Test Ediliyor | Onarım sonrası test |
| `completed` | Tamamlandı | Teslime hazır |
| `delivered` | Teslim Edildi | Müşteriye teslim edildi |
| `cancelled` | İptal Edildi | Servis iptal edildi |
| `unrepairable` | Tamir Edilemez | Onarım mümkün değil |

## 📁 Proje Yapısı

```
teknik_servis/
├── main.py                    # Ana uygulama başlatıcı
├── config.py                  # Yapılandırma ayarları
├── requirements.txt           # Python bağımlılıkları
├── database/
│   ├── connection.py          # Veritabanı bağlantısı
│   ├── models.py              # SQLAlchemy modelleri
│   └── migrations/            # Veritabanı migrasyonları
├── ui/
│   ├── main_window.py         # Ana pencere
│   ├── dashboard.py           # Dashboard widget
│   ├── customers/             # Müşteri ekranları
│   ├── services/              # Servis ekranları
│   ├── inventory/             # Stok ekranları
│   ├── finance/               # Finansal ekranlar
│   ├── reports/               # Rapor ekranları
│   └── settings/              # Ayar ekranları
├── services/                  # İş mantığı katmanı
├── utils/                     # Yardımcı fonksiyonlar
│   ├── printer.py             # Yazıcı işlemleri
│   ├── sms.py                 # SMS gönderimi
│   ├── email_sender.py        # E-posta gönderimi
│   ├── backup.py              # Yedekleme
│   └── pdf_generator.py       # PDF oluşturma
├── resources/                 # Statik dosyalar
│   ├── icons/                 # İkon dosyaları
│   ├── images/                # Görseller
│   └── templates/             # Şablonlar
└── data/                      # Veritabanı dosyası
    └── servis.db
```

## 🎨 Kullanıcı Arayüzü

### Ana Sayfa (Dashboard)

Dashboard, güncel iş durumu ve önemli metrikleri görsel olarak sunar:

- 📈 Günlük servis istatistikleri
- 💵 Tahsilat raporları
- 🏦 Kasa durumu
- ⚠️ Kritik stok uyarıları
- 📊 7 günlük trend grafikleri
- 👷 Teknisyen bazlı iş yükü

### Tema Desteği

| Öğe | Açık Tema | Koyu Tema |
|-----|-----------|-----------|
| Ana Arka Plan | #F5F5F5 | #1E1E1E |
| Kart Arka Plan | #FFFFFF | #2D2D2D |
| Ana Renk | #2B579A | #4A90D9 |
| Başarı | #28A745 | #34C759 |
| Uyarı | #FFC107 | #FFD60A |
| Hata | #DC3545 | #FF453A |

### Klavye Kısayolları

| Kısayol | İşlev |
|---------|-------|
| `Ctrl+N` | Yeni servis kaydı |
| `Ctrl+F` | Hızlı arama |
| `Ctrl+P` | Yazdır |
| `Ctrl+S` | Kaydet |
| `F1` | Yardım |
| `F2` | Düzenle |
| `F5` | Yenile |
| `F12` | Hızlı tahsilat |
| `Esc` | İptal / Kapat |

## 📧 E-posta Entegrasyonu

Sistem, SMTP protokolü üzerinden e-posta gönderim desteği sunar.

### Özellikler

- ✉️ HTML ve düz metin şablonları
- 🔄 Otomatik durum bildirim e-postaları
- 📝 Özelleştirilebilir şablonlar
- 🔐 SSL/TLS güvenlik desteği
- 📊 E-posta gönderim logları
- 🎯 Toplu e-posta kampanyaları

### E-posta Şablonları

| Şablon Kodu | Tetikleyici | Konu |
|-------------|-------------|------|
| `service_received` | Yeni servis kaydı | Cihazınız Teslim Alındı |
| `awaiting_approval` | Onay bekleniyor | Onayınız Bekleniyor |
| `in_progress` | İşlemde | Cihazınız İşleme Alındı |
| `completed` | Tamamlandı | Cihazınız Hazır! |
| `delivered` | Teslim edildi | Teşekkür Ederiz |
| `warranty_expiring` | Garanti dolmak üzere | Garanti Süreniz Dolmak Üzere |

### Kullanılabilir Değişkenler

```
{MUSTERI_ADI}       - Müşteri ad soyad
{SERVIS_NO}         - Servis takip numarası
{CIHAZ_BILGI}       - Cihaz marka ve model
{ARIZA}             - Arıza açıklaması
{DURUM}             - Servis durumu
{TUTAR}             - Toplam tutar
{TAHMINI_TESLIM}    - Tahmini teslim tarihi
{FIRMA_ADI}         - Firma adı
{TAKIP_LINK}        - Online takip linki
```

## 📱 SMS/WhatsApp Entegrasyonu

Müşteri bilgilendirme için SMS ve WhatsApp desteği:

### SMS Şablonları

**Teslim Alındı:**
```
Sayın {MUSTERI}, {CIHAZ} cihazınız servisimize teslim alınmıştır. 
Takip No: {SERVIS_NO}. Bilgi: {TELEFON}
```

**Tamamlandı:**
```
Sayın {MUSTERI}, {CIHAZ} cihazınızın tamiri tamamlanmıştır. 
Teslim için servisimize bekleriz. {FIRMA}
```

## 🖨️ Yazıcı Desteği

### Desteklenen Yazıcı Tipleri

- **Termal Yazıcı (80mm)**: ESC/POS protokolü ile fiş yazdırma
- **A4 Yazıcı**: Detaylı servis fişi ve raporlar

### Fiş İçeriği

- Firma logosu ve bilgileri
- Servis numarası ve QR kod
- Müşteri ve cihaz detayları
- Şikayet ve tahmini teslim
- Takip linki

## 🔐 Güvenlik

### Kimlik Doğrulama

- Bcrypt ile şifre hashleme
- Oturum zaman aşımı (15-30 dakika)
- Başarısız giriş limiti
- Şifre karmaşıklık kuralları

### Yetkilendirme Rolleri

| Rol | Okuma | Yazma | Silme |
|-----|-------|-------|-------|
| Admin | ✅ Tümü | ✅ Tümü | ✅ Tümü |
| Kullanıcı | ✅ Tümü | ⚠️ Sınırlı | ❌ Hayır |
| Teknisyen | ⚠️ Atanan | ⚠️ Atanan | ❌ Hayır |
| İzleyici | ⚠️ Sınırlı | ❌ Hayır | ❌ Hayır |

### Veri Güvenliği

- SQLite veritabanı şifreleme (SQLCipher - opsiyonel)
- Hassas veri maskeleme
- SQL injection koruması
- İşlem logları (audit trail)
- Otomatik yedekleme

## 📈 Raporlama

### Servis Raporları

- Günlük/haftalık/aylık servis sayıları
- Durum bazlı dağılım
- Cihaz tipi bazlı analiz
- Arıza tipi istatistikleri
- Ortalama tamir süresi
- Teknisyen performans raporu

### Finansal Raporlar

- Gelir/gider raporu
- Kar/zarar analizi
- Tahsilat raporu
- Alacak yaşlandırma
- En çok satan parçalar
- Kasa Z raporu

### Müşteri Raporları

- Yeni müşteri sayısı
- En çok servis getiren müşteriler
- Müşteri segmentasyonu

## 🔄 Geliştirme Planı

### Faz 1: Temel Altyapı (2 hafta) ✅
- Veritabanı tasarımı
- Kimlik doğrulama
- Ana pencere yapısı

### Faz 2: Müşteri ve Cihaz Modülü (2 hafta) 🔄
- Müşteri CRUD işlemleri
- Cihaz yönetimi

### Faz 3: Servis Yönetimi (3 hafta) 📋
- Servis kaydı wizard
- Durum takibi
- Fiş yazdırma

### Faz 4: Stok/Parça Yönetimi (2 hafta) 📋
- Stok kayıtları
- Minimum stok uyarıları

### Faz 5: Cari Hesap ve Kasa (2 hafta) 📋
- Alacak/borç takibi
- Tahsilat işlemleri

### Faz 6: Yazıcı Entegrasyonu (1 hafta) 📋
- Termal yazıcı desteği
- A4 şablon tasarımı

### Faz 7: Raporlama (2 hafta) 📋
- PDF rapor oluşturma
- Excel export

### Faz 8: SMS/Bildirim (1 hafta) 📋
- SMS API entegrasyonu
- Otomatik bildirimler

### Faz 9: Dashboard ve İstatistikler (1 hafta) 📋
- Grafik ve metrikler
- Gerçek zamanlı güncellemeler

### Faz 10: Test ve Hata Düzeltme (2 hafta) 📋
- Birim testleri
- Kullanıcı kabul testleri

**Toplam Tahmini Süre:** 18-20 Hafta

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen şu adımları izleyin:

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 📞 İletişim

**Proje Sahibi:** Ünal Uslusoy

**GitHub:** [@unaluslusoy](https://github.com/unaluslusoy)

**Proje Linki:** [https://github.com/unaluslusoy/TeknikServisYazilim](https://github.com/unaluslusoy/TeknikServisYazilim)

## 🙏 Teşekkürler

Bu proje aşağıdaki açık kaynak projeleri kullanmaktadır:

- [PyQt6](https://www.riverbankcomputing.com/software/pyqt/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [ReportLab](https://www.reportlab.com/)
- [python-barcode](https://github.com/WhyNotHugo/python-barcode)
- [qrcode](https://github.com/lincolnloop/python-qrcode)

---

**Versiyon:** 1.0 | **Son Güncelleme:** Aralık 2024

⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın!

