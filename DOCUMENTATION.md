# TEKNİK SERVİS YÖNETİM SİSTEMİ - Teknik Dokümantasyon

**Versiyon:** 1.0  
**Tarih:** Aralık 2024

## İçindekiler

1. [Veritabanı Tasarımı](#1-veritabanı-tasarımı)
2. [Uygulama Modülleri](#2-uygulama-modülleri)
3. [Kullanıcı Arayüzü](#3-kullanıcı-arayüzü)
4. [Teknik Mimari](#4-teknik-mimari)
5. [API ve Entegrasyonlar](#5-api-ve-entegrasyonlar)
6. [Güvenlik](#6-güvenlik)
7. [Yedekleme ve Bakım](#7-yedekleme-ve-bakım)

---

## 1. Veritabanı Tasarımı

### 1.1 Customers (Müşteriler)

```sql
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_type VARCHAR(10) NOT NULL CHECK(customer_type IN ('bireysel', 'kurumsal')),
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL UNIQUE,
    phone2 VARCHAR(20),
    email VARCHAR(100),
    tc_no VARCHAR(11),
    tax_no VARCHAR(11),
    tax_office VARCHAR(50),
    address TEXT,
    city VARCHAR(50),
    district VARCHAR(50),
    notes TEXT,
    balance DECIMAL(12,2) DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME,
    is_active BOOLEAN DEFAULT 1
);
```

**İndeksler:**
- `idx_customers_phone` on `phone`
- `idx_customers_name` on `name`
- `idx_customers_tc_no` on `tc_no`

### 1.2 Devices (Cihazlar)

```sql
CREATE TABLE devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    device_type VARCHAR(50) NOT NULL,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(100),
    serial_no VARCHAR(100),
    imei VARCHAR(20),
    imei2 VARCHAR(20),
    color VARCHAR(30),
    password VARCHAR(50),
    accessories TEXT,
    physical_condition TEXT,
    warranty_end DATE,
    photo_path VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```

**İndeksler:**
- `idx_devices_customer` on `customer_id`
- `idx_devices_imei` on `imei`

### 1.3 Service Orders (Servis Emirleri)

```sql
CREATE TABLE service_orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_no VARCHAR(20) UNIQUE NOT NULL,
    customer_id INTEGER NOT NULL,
    device_id INTEGER NOT NULL,
    technician_id INTEGER,
    status VARCHAR(30) NOT NULL DEFAULT 'pending',
    priority VARCHAR(10) DEFAULT 'medium',
    complaint TEXT NOT NULL,
    diagnosis TEXT,
    work_done TEXT,
    estimated_cost DECIMAL(12,2),
    final_cost DECIMAL(12,2),
    labor_cost DECIMAL(12,2),
    discount DECIMAL(12,2) DEFAULT 0,
    warranty_days INTEGER DEFAULT 0,
    received_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    estimated_delivery DATETIME,
    completed_at DATETIME,
    delivered_at DATETIME,
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (device_id) REFERENCES devices(id),
    FOREIGN KEY (technician_id) REFERENCES technicians(id)
);
```

**Status Değerleri:**
- `pending` - Beklemede
- `diagnosing` - Teşhis Aşamasında
- `waiting_approval` - Onay Bekleniyor
- `waiting_part` - Parça Bekleniyor
- `in_progress` - İşlemde
- `testing` - Test Ediliyor
- `completed` - Tamamlandı
- `delivered` - Teslim Edildi
- `cancelled` - İptal Edildi
- `unrepairable` - Tamir Edilemez

### 1.4 Technicians (Teknisyenler)

```sql
CREATE TABLE technicians (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100),
    specialization VARCHAR(100),
    commission_rate DECIMAL(5,2) DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### 1.5 Users (Kullanıcılar)

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    role VARCHAR(20) NOT NULL CHECK(role IN ('admin', 'user', 'viewer', 'technician')),
    technician_id INTEGER,
    last_login DATETIME,
    is_active BOOLEAN DEFAULT 1,
    FOREIGN KEY (technician_id) REFERENCES technicians(id)
);
```

### 1.6 Inventory (Stok/Parçalar)

```sql
CREATE TABLE inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku VARCHAR(50) UNIQUE,
    barcode VARCHAR(50),
    name VARCHAR(200) NOT NULL,
    category_id INTEGER,
    brand VARCHAR(50),
    compatible_models TEXT,
    purchase_price DECIMAL(12,2),
    sale_price DECIMAL(12,2),
    quantity INTEGER DEFAULT 0,
    min_quantity INTEGER DEFAULT 0,
    location VARCHAR(50),
    supplier_id INTEGER,
    is_active BOOLEAN DEFAULT 1,
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);
```

### 1.7 Service Parts (Servis Parça Kullanımı)

```sql
CREATE TABLE service_parts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_order_id INTEGER NOT NULL,
    inventory_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(12,2) NOT NULL,
    total_price DECIMAL(12,2) NOT NULL,
    warranty_included BOOLEAN DEFAULT 0,
    FOREIGN KEY (service_order_id) REFERENCES service_orders(id),
    FOREIGN KEY (inventory_id) REFERENCES inventory(id)
);
```

### 1.8 Account Transactions (Cari Hesap Hareketleri)

```sql
CREATE TABLE account_transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    service_order_id INTEGER,
    transaction_type VARCHAR(20) NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    payment_method VARCHAR(20),
    description TEXT,
    balance_after DECIMAL(12,2),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_by INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (service_order_id) REFERENCES service_orders(id),
    FOREIGN KEY (created_by) REFERENCES users(id)
);
```

**Transaction Types:**
- `service_charge` - Servis Ücreti (+ Borç)
- `payment_cash` - Nakit Tahsilat (- Alacak)
- `payment_card` - Kredi Kartı Tahsilat (- Alacak)
- `payment_transfer` - Havale/EFT Tahsilat (- Alacak)
- `refund` - İade (+ Borç)
- `discount` - İndirim (- Alacak)
- `opening_balance` - Açılış Bakiyesi (+/-)
- `adjustment` - Düzeltme (+/-)

### 1.9 Suppliers (Tedarikçiler)

```sql
CREATE TABLE suppliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100),
    address TEXT,
    tax_no VARCHAR(11),
    balance DECIMAL(12,2) DEFAULT 0,
    notes TEXT
);
```

### 1.10 Categories (Kategoriler)

```sql
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    parent_id INTEGER,
    description TEXT,
    FOREIGN KEY (parent_id) REFERENCES categories(id)
);
```

### 1.11 Stock Movements (Stok Hareketleri)

```sql
CREATE TABLE stock_movements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    inventory_id INTEGER NOT NULL,
    movement_type VARCHAR(20) NOT NULL,
    quantity INTEGER NOT NULL,
    reference_type VARCHAR(50),
    reference_id INTEGER,
    unit_cost DECIMAL(12,2),
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_by INTEGER,
    FOREIGN KEY (inventory_id) REFERENCES inventory(id),
    FOREIGN KEY (created_by) REFERENCES users(id)
);
```

### 1.12 Cash Register (Kasa Hareketleri)

```sql
CREATE TABLE cash_register (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_type VARCHAR(20) NOT NULL CHECK(transaction_type IN ('income', 'expense')),
    amount DECIMAL(12,2) NOT NULL,
    payment_method VARCHAR(20),
    category VARCHAR(50),
    description TEXT,
    reference_type VARCHAR(50),
    reference_id INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_by INTEGER,
    FOREIGN KEY (created_by) REFERENCES users(id)
);
```

### 1.13 Settings (Sistem Ayarları)

```sql
CREATE TABLE settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key VARCHAR(100) UNIQUE NOT NULL,
    value TEXT,
    description VARCHAR(255)
);
```

### 1.14 Notification Logs (Bildirim Kayıtları)

```sql
CREATE TABLE notification_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    service_order_id INTEGER,
    notification_type VARCHAR(20) NOT NULL CHECK(notification_type IN ('sms', 'email', 'whatsapp')),
    recipient VARCHAR(100),
    subject VARCHAR(255),
    message TEXT,
    status VARCHAR(20) DEFAULT 'pending',
    error_message TEXT,
    sent_at DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (service_order_id) REFERENCES service_orders(id)
);
```

### 1.15 Email Settings (E-Posta Ayarları)

```sql
CREATE TABLE email_settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    smtp_server VARCHAR(100) NOT NULL,
    smtp_port INTEGER DEFAULT 587,
    smtp_username VARCHAR(100) NOT NULL,
    smtp_password VARCHAR(255) NOT NULL,
    use_tls BOOLEAN DEFAULT 1,
    use_ssl BOOLEAN DEFAULT 0,
    sender_name VARCHAR(100),
    sender_email VARCHAR(100) NOT NULL,
    reply_to VARCHAR(100),
    signature_html TEXT,
    is_active BOOLEAN DEFAULT 1
);
```

### 1.16 Email Templates (E-Posta Şablonları)

```sql
CREATE TABLE email_templates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    template_code VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    subject VARCHAR(255) NOT NULL,
    body_html TEXT NOT NULL,
    body_text TEXT,
    trigger_event VARCHAR(50),
    is_auto_send BOOLEAN DEFAULT 0,
    is_active BOOLEAN DEFAULT 1
);
```

### 1.17 Veritabanı İlişki Diyagramı

```
customers (1) ──< (N) devices
customers (1) ──< (N) service_orders
customers (1) ──< (N) account_transactions
customers (1) ──< (N) notification_logs

devices (1) ──< (N) service_orders

technicians (1) ──< (N) service_orders

service_orders (1) ──< (N) service_parts
service_orders (1) ──< (N) notification_logs

inventory (1) ──< (N) service_parts
inventory (1) ──< (N) stock_movements

categories (1) ──< (N) inventory
suppliers (1) ──< (N) inventory

users (1) ──< (N) cash_register
users (1) ──< (N) account_transactions

email_templates (1) ──< (N) notification_logs
```

---

## 2. Uygulama Modülleri

### 2.1 Ana Sayfa (Dashboard)

**Dosya:** `ui/dashboard.py`

**Bileşenler:**
- Güncel istatistik widget'ları
- Grafik gösterimler (Chart.js veya PyQt Charts)
- Hızlı erişim butonları
- Bildirim merkezi

**Gösterilecek Metrikler:**
```python
dashboard_metrics = {
    'today_services': {
        'new': 0,
        'completed': 0,
        'delivered': 0
    },
    'pending_services': {
        'awaiting_approval': 0,
        'waiting_part': 0
    },
    'today_collections': {
        'cash': 0.0,
        'card': 0.0,
        'transfer': 0.0,
        'total': 0.0
    },
    'cash_balance': 0.0,
    'critical_stock_count': 0,
    'overdue_receivables': 0.0
}
```

### 2.2 Müşteri Yönetimi

**Dosya:** `ui/customers/customer_list.py`, `ui/customers/customer_detail.py`

**Ana Özellikler:**
- Müşteri listesi (tablo görünümü)
- Hızlı arama ve filtreleme
- Müşteri detay ekranı (tab'lı yapı)
- Cari hesap takibi

**Müşteri Detay Tab'ları:**
1. Bilgiler - Temel müşteri bilgileri
2. Cihazlar - Kayıtlı cihazlar listesi
3. Servisler - Geçmiş ve aktif servisler
4. Cari Hesap - Alacak/borç hareketleri
5. İletişim - SMS/E-posta geçmişi

### 2.3 Servis Yönetimi

**Dosya:** `ui/services/service_wizard.py`, `ui/services/service_list.py`

**Yeni Servis Wizard Adımları:**

**Adım 1 - Müşteri Seçimi:**
```python
class CustomerSelectionStep(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Müşteri Seçimi")
        # Telefon ile hızlı arama
        # Mevcut müşteri seçimi veya yeni kayıt
```

**Adım 2 - Cihaz Bilgileri:**
```python
class DeviceInfoStep(QWizardPage):
    device_types = ['Telefon', 'Tablet', 'Laptop', 'PC', 'Diğer']
    # Cihaz tipi, marka, model
    # IMEI/Seri no
    # Fiziksel durum checklist
    # Fotoğraf yükleme
```

**Adım 3 - Arıza ve Detaylar:**
```python
class ComplaintStep(QWizardPage):
    priorities = ['Düşük', 'Normal', 'Yüksek', 'Acil']
    # Arıza açıklaması
    # Öncelik seviyesi
    # Tahmini maliyet
    # Teknisyen atama
```

**Adım 4 - Onay ve Fiş:**
```python
class ConfirmationStep(QWizardPage):
    # Özet bilgi
    # Dijital imza alanı
    # Fiş yazdırma seçenekleri
```

**Servis Görünüm Modları:**
- Kanban (Sürükle-bırak)
- Tablo
- Takvim

### 2.4 Stok/Parça Yönetimi

**Dosya:** `ui/inventory/inventory_list.py`

**Özellikler:**
- Barkod ile hızlı arama
- Kategori bazlı filtreleme
- Stok giriş/çıkış formları
- Minimum stok uyarıları
- Barkod etiketi yazdırma

### 2.5 Cari Hesap Yönetimi

**Dosya:** `ui/finance/account_management.py`

**Modüller:**
- Müşteri cari hesap
- Tedarikçi cari hesap
- Tahsilat/ödeme kayıt formları
- Ekstre yazdırma

### 2.6 Kasa Yönetimi

**Dosya:** `ui/finance/cash_register.py`

**İşlevler:**
- Günlük açılış/kapanış
- Gelir kaydı
- Gider kaydı
- Z raporu
- Ödeme yöntemi bazlı toplam

### 2.7 Raporlama

**Dosya:** `ui/reports/report_generator.py`

**Rapor Tipleri:**

1. **Servis Raporları**
   - Günlük servis özeti
   - Durum dağılımı
   - Teknisyen performansı

2. **Finansal Raporlar**
   - Gelir-gider analizi
   - Kar-zarar raporu
   - Tahsilat raporu

3. **Stok Raporları**
   - Kritik stok listesi
   - Stok hareket raporu
   - En çok kullanılan parçalar

### 2.8 Sistem Ayarları

**Dosya:** `ui/settings/settings_panel.py`

**Ayar Kategorileri:**
- Firma bilgileri
- Yazıcı ayarları
- E-posta ayarları
- SMS entegrasyonu
- Kullanıcı yönetimi
- Yedekleme ayarları

---

## 3. Kullanıcı Arayüzü

### 3.1 Ana Pencere Yapısı

```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Teknik Servis Yönetim Sistemi")
        self.setMinimumSize(1280, 720)
        
        # Sol menü
        self.sidebar = SidebarMenu()
        
        # Üst çubuk
        self.toolbar = TopToolbar()
        
        # İçerik alanı (tab widget)
        self.content_area = QTabWidget()
        
        # Alt durum çubuğu
        self.statusbar = QStatusBar()
```

### 3.2 Tema Sistemi

**Dosya:** `ui/styles/theme.qss`

**Açık Tema:**
```css
QMainWindow {
    background-color: #F5F5F5;
}

QWidget {
    font-family: 'Segoe UI', Arial;
    font-size: 10pt;
}

QPushButton {
    background-color: #2B579A;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
}

QPushButton:hover {
    background-color: #1e3f6f;
}
```

### 3.3 Özel Widget'lar

**Dosya:** `ui/widgets/custom_widgets.py`

```python
class MetricCard(QWidget):
    """Dashboard metrik kartı"""
    def __init__(self, title, value, icon=None):
        super().__init__()
        # Kart tasarımı

class StatusBadge(QLabel):
    """Durum rozeti"""
    status_colors = {
        'pending': '#FFC107',
        'in_progress': '#2196F3',
        'completed': '#4CAF50',
        'cancelled': '#F44336'
    }

class SearchBar(QLineEdit):
    """Gelişmiş arama çubuğu"""
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Ara... (Ctrl+F)")
```

---

## 4. Teknik Mimari

### 4.1 Katmanlı Mimari

```
┌─────────────────────────────────────┐
│        Presentation Layer           │
│          (UI - PyQt6)               │
├─────────────────────────────────────┤
│       Business Logic Layer          │
│     (Services - Python Classes)     │
├─────────────────────────────────────┤
│       Data Access Layer             │
│      (ORM - SQLAlchemy)             │
├─────────────────────────────────────┤
│          Database Layer             │
│           (SQLite)                  │
└─────────────────────────────────────┘
```

### 4.2 Servis Katmanı

**Dosya:** `services/customer_service.py`

```python
class CustomerService:
    def __init__(self, db_session):
        self.db = db_session
    
    def create_customer(self, customer_data):
        """Yeni müşteri oluştur"""
        pass
    
    def get_customer_by_phone(self, phone):
        """Telefon ile müşteri bul"""
        pass
    
    def update_balance(self, customer_id, amount):
        """Bakiye güncelle"""
        pass
```

**Dosya:** `services/service_order_service.py`

```python
class ServiceOrderService:
    def create_order(self, order_data):
        """Yeni servis kaydı"""
        # Auto-generate order_no
        # Validate data
        # Save to database
        # Send notification
        pass
    
    def update_status(self, order_id, new_status):
        """Durum güncelle"""
        # Update status
        # Log change
        # Trigger notification
        pass
    
    def calculate_total_cost(self, order_id):
        """Toplam maliyet hesapla"""
        # Labor cost + Parts cost - Discount
        pass
```

### 4.3 Veritabanı Bağlantısı

**Dosya:** `database/connection.py`

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DatabaseManager:
    def __init__(self, db_path='data/servis.db'):
        self.engine = create_engine(f'sqlite:///{db_path}')
        self.Session = sessionmaker(bind=self.engine)
    
    def get_session(self):
        return self.Session()
    
    def create_tables(self):
        Base.metadata.create_all(self.engine)
```

### 4.4 Model Tanımları

**Dosya:** `database/models.py`

```python
from sqlalchemy import Column, Integer, String, DateTime, Decimal, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    customer_type = Column(String(10), nullable=False)
    name = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False, unique=True)
    # ... diğer alanlar
    
    # İlişkiler
    devices = relationship("Device", back_populates="customer")
    service_orders = relationship("ServiceOrder", back_populates="customer")
    transactions = relationship("AccountTransaction", back_populates="customer")

class ServiceOrder(Base):
    __tablename__ = 'service_orders'
    
    id = Column(Integer, primary_key=True)
    order_no = Column(String(20), unique=True, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    # ... diğer alanlar
    
    # İlişkiler
    customer = relationship("Customer", back_populates="service_orders")
    device = relationship("Device")
    technician = relationship("Technician")
    parts = relationship("ServicePart", back_populates="service_order")
```

---

## 5. API ve Entegrasyonlar

### 5.1 E-posta Gönderimi

**Dosya:** `utils/email_sender.py`

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Template

class EmailSender:
    def __init__(self, smtp_config):
        self.smtp_server = smtp_config['server']
        self.smtp_port = smtp_config['port']
        self.username = smtp_config['username']
        self.password = smtp_config['password']
        self.use_tls = smtp_config.get('use_tls', True)
    
    def send_email(self, to_email, subject, html_body, text_body=None):
        """E-posta gönder"""
        msg = MIMEMultipart('alternative')
        msg['From'] = self.username
        msg['To'] = to_email
        msg['Subject'] = subject
        
        if text_body:
            part1 = MIMEText(text_body, 'plain')
            msg.attach(part1)
        
        part2 = MIMEText(html_body, 'html')
        msg.attach(part2)
        
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                if self.use_tls:
                    server.starttls()
                server.login(self.username, self.password)
                server.send_message(msg)
                return True
        except Exception as e:
            print(f"E-posta gönderim hatası: {e}")
            return False
    
    def send_template_email(self, to_email, template_code, variables):
        """Şablon ile e-posta gönder"""
        # Template'i veritabanından al
        # Variables ile render et
        # Gönder
        pass
```

**Örnek Kullanım:**
```python
email_sender = EmailSender(smtp_config)

# Servis teslim alındı bildirimi
variables = {
    'MUSTERI_ADI': 'Ahmet Yılmaz',
    'SERVIS_NO': 'SRV-2024-001234',
    'CIHAZ_BILGI': 'iPhone 13 Pro',
    'ARIZA': 'Ekran kırık',
    'TAHMINI_TESLIM': '17.12.2024',
    'TAKIP_LINK': 'https://servis.example.com/track/SRV-2024-001234'
}

email_sender.send_template_email(
    to_email='musteri@example.com',
    template_code='service_received',
    variables=variables
)
```

### 5.2 SMS Entegrasyonu

**Dosya:** `utils/sms.py`

```python
import requests

class SMSSender:
    def __init__(self, api_config):
        self.api_url = api_config['url']
        self.api_key = api_config['key']
        self.sender_name = api_config['sender']
    
    def send_sms(self, phone, message):
        """SMS gönder"""
        payload = {
            'api_key': self.api_key,
            'sender': self.sender_name,
            'phone': phone,
            'message': message
        }
        
        try:
            response = requests.post(self.api_url, json=payload)
            return response.json()
        except Exception as e:
            print(f"SMS gönderim hatası: {e}")
            return None
    
    def send_template_sms(self, phone, template_name, variables):
        """Şablon ile SMS gönder"""
        template = self.get_template(template_name)
        message = template.format(**variables)
        return self.send_sms(phone, message)
```

### 5.3 Yazıcı Entegrasyonu

**Dosya:** `utils/printer.py`

```python
from escpos.printer import Win32Raw
from reportlab.pdfgen import canvas

class ThermalPrinter:
    def __init__(self, printer_name):
        self.printer = Win32Raw(printer_name)
    
    def print_service_receipt(self, service_data):
        """Servis fişi yazdır"""
        self.printer.set(align='center')
        # Logo
        if service_data['logo_path']:
            self.printer.image(service_data['logo_path'])
        
        # Firma bilgileri
        self.printer.text(f"{service_data['firma_adi']}\n")
        self.printer.text(f"Tel: {service_data['telefon']}\n")
        self.printer.text("=" * 32 + "\n")
        
        # Servis bilgileri
        self.printer.set(align='left')
        self.printer.text(f"Servis No: {service_data['servis_no']}\n")
        self.printer.text(f"Tarih: {service_data['tarih']}\n")
        self.printer.text("-" * 32 + "\n")
        
        # Müşteri
        self.printer.text(f"Müşteri: {service_data['musteri_adi']}\n")
        self.printer.text(f"Tel: {service_data['musteri_tel']}\n")
        
        # Cihaz
        self.printer.text(f"Cihaz: {service_data['cihaz']}\n")
        self.printer.text(f"IMEI: {service_data['imei']}\n")
        
        # QR Kod
        self.printer.qr(service_data['takip_url'])
        
        # Kesme
        self.printer.cut()

class A4Printer:
    def print_detailed_receipt(self, service_data, filename):
        """Detaylı servis fişi (A4)"""
        c = canvas.Canvas(filename)
        # PDF oluşturma
        c.save()
```

### 5.4 Yedekleme Sistemi

**Dosya:** `utils/backup.py`

```python
import shutil
import os
from datetime import datetime

class BackupManager:
    def __init__(self, db_path, backup_dir):
        self.db_path = db_path
        self.backup_dir = backup_dir
    
    def create_backup(self):
        """Yedek oluştur"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = f"backup_{timestamp}.db"
        backup_path = os.path.join(self.backup_dir, backup_file)
        
        shutil.copy2(self.db_path, backup_path)
        return backup_path
    
    def restore_backup(self, backup_file):
        """Yedekten geri yükle"""
        backup_path = os.path.join(self.backup_dir, backup_file)
        shutil.copy2(backup_path, self.db_path)
    
    def auto_backup_schedule(self, interval_hours=24):
        """Otomatik yedekleme planla"""
        # Zamanlanmış görev oluştur
        pass
```

---

## 6. Güvenlik

### 6.1 Şifre Hashleme

**Dosya:** `utils/security.py`

```python
import bcrypt

class SecurityManager:
    @staticmethod
    def hash_password(password):
        """Şifreyi hashle"""
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')
    
    @staticmethod
    def verify_password(password, hashed_password):
        """Şifre doğrula"""
        return bcrypt.checkpw(
            password.encode('utf-8'),
            hashed_password.encode('utf-8')
        )
```

### 6.2 Oturum Yönetimi

```python
class SessionManager:
    def __init__(self):
        self.current_user = None
        self.login_time = None
        self.session_timeout = 1800  # 30 dakika
    
    def login(self, username, password):
        """Kullanıcı girişi"""
        # Şifre doğrula
        # Oturum başlat
        # Son giriş zamanını kaydet
        pass
    
    def logout(self):
        """Çıkış yap"""
        self.current_user = None
        self.login_time = None
    
    def check_session_timeout(self):
        """Oturum zaman aşımı kontrolü"""
        # Timeout kontrolü
        pass
```

### 6.3 Yetkilendirme

```python
class PermissionManager:
    permissions = {
        'admin': ['*'],  # Tüm yetkiler
        'user': ['read', 'write_service', 'write_customer'],
        'technician': ['read_assigned', 'write_assigned'],
        'viewer': ['read']
    }
    
    @staticmethod
    def has_permission(user_role, action):
        """Yetki kontrolü"""
        if user_role == 'admin':
            return True
        return action in PermissionManager.permissions.get(user_role, [])
```

---

## 7. Yedekleme ve Bakım

### 7.1 Veritabanı Bakımı

```python
class DatabaseMaintenance:
    def vacuum_database(self):
        """Veritabanını optimize et"""
        # SQLite VACUUM komutu
        pass
    
    def reindex_database(self):
        """İndeksleri yeniden oluştur"""
        pass
    
    def analyze_database(self):
        """İstatistikleri güncelle"""
        pass
```

### 7.2 Log Yönetimi

**Dosya:** `utils/logger.py`

```python
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file, level=logging.INFO):
    """Logger yapılandır"""
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    handler = RotatingFileHandler(
        log_file,
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    handler.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    
    return logger
```

---

## 8. Test Stratejisi

### 8.1 Birim Testleri

**Dosya:** `tests/test_services.py`

```python
import unittest
from services.customer_service import CustomerService

class TestCustomerService(unittest.TestCase):
    def setUp(self):
        # Test veritabanı oluştur
        pass
    
    def test_create_customer(self):
        # Yeni müşteri oluşturma testi
        pass
    
    def test_update_balance(self):
        # Bakiye güncelleme testi
        pass
    
    def tearDown(self):
        # Temizlik
        pass
```

### 8.2 Entegrasyon Testleri

```python
class TestServiceOrderFlow(unittest.TestCase):
    def test_complete_service_flow(self):
        # Müşteri oluştur
        # Cihaz ekle
        # Servis kaydı oluştur
        # Durum güncelle
        # Ödeme al
        # Teslim et
        pass
```

---

## Sonuç

Bu teknik dokümantasyon, Teknik Servis Yönetim Sistemi'nin detaylı yapısını açıklamaktadır. Sistem, modüler bir mimari ile geliştirilecek ve her katman bağımsız olarak test edilebilir olacaktır.

**Güncel Durum:** Planlama aşaması tamamlandı, geliştirme başlayabilir.

**Sonraki Adımlar:**
1. Veritabanı migration script'lerini oluştur
2. Temel model sınıflarını kodla
3. Servis katmanını implement et
4. UI bileşenlerini geliştir
5. Entegrasyon testlerini yaz

---

**Doküman Sonu**  
*Hazırlayan: GitHub Copilot | Tarih: Aralık 2024*

