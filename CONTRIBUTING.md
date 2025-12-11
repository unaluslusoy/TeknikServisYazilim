# Katkıda Bulunma Rehberi

Teknik Servis Yönetim Sistemi projesine katkıda bulunmak istediğiniz için teşekkür ederiz! 🎉

## 🚀 Başlangıç

### Gereksinimler

- Python 3.11 veya üzeri
- Git
- PyQt6 (veya PySide6)

### Proje Kurulumu

1. Repository'yi fork edin
2. Bilgisayarınıza klonlayın:
   ```bash
   git clone https://github.com/YOUR_USERNAME/TeknikServisYazilim.git
   cd TeknikServisYazilim
   ```

3. Sanal ortam oluşturun:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

4. Bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

## 📝 Kod Standartları

### Python Kod Stili

- **PEP 8** standartlarına uyun
- Maksimum satır uzunluğu: 100 karakter
- Docstring'leri kullanın (Google style)
- Type hints kullanın

**Örnek:**

```python
def create_customer(
    name: str, 
    phone: str, 
    customer_type: str = 'bireysel'
) -> Customer:
    """
    Yeni müşteri oluşturur.
    
    Args:
        name: Müşteri adı
        phone: Telefon numarası
        customer_type: Müşteri tipi ('bireysel' veya 'kurumsal')
    
    Returns:
        Oluşturulan Customer nesnesi
    
    Raises:
        ValueError: Geçersiz telefon numarası durumunda
    """
    pass
```

### Commit Mesajları

Conventional Commits formatını kullanın:

```
<tip>(<kapsam>): <kısa açıklama>

[isteğe bağlı detaylı açıklama]

[isteğe bağlı footer]
```

**Tipler:**
- `feat`: Yeni özellik
- `fix`: Hata düzeltme
- `docs`: Dokümantasyon değişikliği
- `style`: Kod formatı (kod davranışını değiştirmeyen)
- `refactor`: Kod yeniden yapılandırma
- `test`: Test ekleme/düzeltme
- `chore`: Bakım işleri

**Örnekler:**

```
feat(customer): Müşteri arama özelliği eklendi

fix(service): Servis durum güncelleme hatası düzeltildi

docs(readme): Kurulum talimatları güncellendi

refactor(database): SQLAlchemy modelleri yeniden yapılandırıldı
```

### Branch İsimlendirme

```
<tip>/<kısa-açıklama>

Örnekler:
- feature/customer-search
- fix/database-connection
- docs/api-documentation
- refactor/service-layer
```

## 🔄 Geliştirme İş Akışı

1. **Yeni branch oluşturun:**
   ```bash
   git checkout -b feature/amazing-feature
   ```

2. **Değişikliklerinizi yapın ve test edin**

3. **Commit edin:**
   ```bash
   git add .
   git commit -m "feat(module): Açıklama"
   ```

4. **Push edin:**
   ```bash
   git push origin feature/amazing-feature
   ```

5. **Pull Request oluşturun**

## 🧪 Test

Yeni özellikler için test yazın:

```python
# tests/test_customer_service.py
import unittest
from services.customer_service import CustomerService

class TestCustomerService(unittest.TestCase):
    def test_create_customer(self):
        # Test kodları
        pass
```

Testleri çalıştırın:
```bash
python -m pytest tests/
```

## 📋 Pull Request Süreci

1. **PR açmadan önce:**
   - Kodunuzun çalıştığından emin olun
   - Testleri çalıştırın
   - Dokümantasyonu güncelleyin
   - main branch ile merge edin

2. **PR Başlığı:**
   ```
   [Tip] Kısa açıklama
   
   Örnek: [Feature] Müşteri arama özelliği
   ```

3. **PR Açıklaması Template:**
   ```markdown
   ## Değişiklik Türü
   - [ ] Yeni özellik
   - [ ] Hata düzeltme
   - [ ] Kod iyileştirme
   - [ ] Dokümantasyon
   
   ## Açıklama
   Bu PR'da neler yapıldı?
   
   ## İlgili Issue
   Closes #123
   
   ## Test
   Nasıl test edildi?
   
   ## Ekran Görüntüleri (varsa)
   ```

## 📁 Proje Yapısı

```
teknik_servis/
├── database/           # Veritabanı modelleri ve migration
├── ui/                 # PyQt6 arayüz bileşenleri
├── services/           # İş mantığı katmanı
├── utils/              # Yardımcı fonksiyonlar
├── resources/          # Statik dosyalar
├── tests/              # Test dosyaları
└── docs/               # Dokümantasyon
```

## 🎨 UI Geliştirme

- PyQt6 Designer kullanabilirsiniz (.ui dosyaları)
- QSS (Qt Style Sheets) ile stil verin
- Responsive tasarım yapın
- Açık ve koyu tema desteği ekleyin

## 🐛 Hata Bildirimi

Issue oluştururken şu bilgileri ekleyin:

```markdown
**Hata Açıklaması:**
Net ve öz açıklama

**Nasıl Tekrarlanır:**
1. '...' sayfasına git
2. '...' butonuna tıkla
3. Hatayı gör

**Beklenen Davranış:**
Ne olması gerekiyordu?

**Ekran Görüntüleri:**
Varsa ekleyin

**Ortam:**
- OS: [örn. Windows 11]
- Python: [örn. 3.11.5]
- PyQt6: [örn. 6.5.0]
```

## 💡 Yeni Özellik Önerisi

```markdown
**Özellik Açıklaması:**
Ne istiyorsunuz?

**Motivasyon:**
Neden gerekli?

**Alternatifler:**
Başka çözümler düşündünüz mü?

**Ek Bilgiler:**
Başka eklemek istedikleriniz
```

## 📞 İletişim

- **GitHub Issues:** Hata bildirimi ve özellik önerileri için
- **GitHub Discussions:** Genel sorular ve tartışmalar için

## 📜 Lisans

Katkılarınız MIT lisansı altında dağıtılacaktır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 🙏 Teşekkürler

Katkılarınız için teşekkür ederiz! Her türlü katkı değerlidir:

- 🐛 Hata raporları
- 💡 Yeni özellik önerileri
- 📝 Dokümantasyon iyileştirmeleri
- 🧪 Test yazımı
- 💻 Kod katkıları
- 🎨 UI/UX iyileştirmeleri

---

**Mutlu kodlamalar! 🚀**

