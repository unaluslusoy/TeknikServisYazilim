# GitHub Repository Kurulum Talimatları

Bu belge, GitHub'da repository oluşturulduktan sonra projeyi push etmek için gerekli adımları içerir.

## Adım 1: GitHub'da Repository Oluşturun

1. https://github.com/unaluslusoy adresine gidin
2. "New repository" butonuna tıklayın
3. Repository adı: `TeknikServisYazilim`
4. Açıklama: "Teknik Servis Yönetim Sistemi - Python & PyQt6"
5. **ÖNEMLİ:** README, .gitignore veya license eklemeyin (zaten projede var)
6. "Create repository" butonuna tıklayın

## Adım 2: Yerel Projeyi GitHub'a Push Edin

Repository oluşturduktan sonra, terminal'de şu komutları çalıştırın:

```powershell
# Mevcut remote'u kontrol edin
git remote -v

# Eğer remote yoksa ekleyin
git remote add origin https://github.com/unaluslusoy/TeknikServisYazilim.git

# Eğer remote varsa güncelleyin
git remote set-url origin https://github.com/unaluslusoy/TeknikServisYazilim.git

# Push edin
git push -u origin main
```

## Adım 3: GitHub Ayarları

### Repository Açıklaması
- **About** bölümünü düzenleyin
- Açıklama: "Telefon, tablet, bilgisayar ve elektronik cihaz servisleri için kapsamlı yönetim sistemi"
- Topics ekleyin: `python`, `pyqt6`, `sqlite`, `desktop-app`, `technical-service`, `management-system`

### Branch Koruması (Opsiyonel)
Settings > Branches > Add rule:
- Branch name pattern: `main`
- ✅ Require pull request reviews before merging
- ✅ Require status checks to pass before merging

### GitHub Pages (Dokümantasyon için)
Settings > Pages:
- Source: Deploy from a branch
- Branch: `main` / `/docs`

## Adım 4: İlk Release Oluşturun

1. Releases > Create a new release
2. Tag version: `v1.0.0`
3. Release title: `v1.0.0 - İlk Planlama Sürümü`
4. Description: CHANGELOG.md'den kopyalayın
5. Publish release

## Troubleshooting

### Hata: "repository not found"
- GitHub'da repository'nin oluşturulduğundan emin olun
- Repository adının doğru olduğunu kontrol edin
- GitHub kullanıcı adınızı kontrol edin

### Hata: "authentication failed"
Eğer 2FA (iki faktörlü doğrulama) kullanıyorsanız:
1. GitHub > Settings > Developer settings > Personal access tokens
2. "Generate new token (classic)" oluşturun
3. Scope: `repo` seçin
4. Token'ı kopyalayın
5. Push yaparken şifre yerine token'ı kullanın

Veya SSH kullanın:
```powershell
# SSH key oluşturun
ssh-keygen -t ed25519 -C "unaluslusoy@gmail.com"

# SSH key'i GitHub'a ekleyin
# GitHub > Settings > SSH and GPG keys > New SSH key

# Remote URL'i SSH'a çevirin
git remote set-url origin git@github.com:unaluslusoy/TeknikServisYazilim.git
```

## Sonraki Adımlar

✅ Repository oluşturuldu  
✅ İlk commit push edildi  
⏳ README'yi kontrol edin  
⏳ Issues oluşturun (geliştirme görevleri için)  
⏳ Projects board kurun  
⏳ Wiki sayfalarını doldurun  

---

**Not:** Bu dosyayı push ettikten sonra silebilirsiniz.

