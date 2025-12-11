"""
Teknik Servis Yönetim Sistemi
Ana Uygulama Başlatıcı

Versiyon: 1.0.0
Tarih: 11 Aralık 2024
"""

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QPushButton, QTextEdit
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon


class MainWindow(QMainWindow):
    """Ana uygulama penceresi"""

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """UI bileşenlerini başlat"""
        self.setWindowTitle("Teknik Servis Yönetim Sistemi v1.0.0")
        self.setGeometry(100, 100, 1024, 768)

        # Merkezi widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Ana layout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Başlık
        title_label = QLabel("🔧 Teknik Servis Yönetim Sistemi")
        title_font = QFont("Arial", 24, QFont.Weight.Bold)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #2B579A; padding: 20px;")
        main_layout.addWidget(title_label)

        # Hoş geldiniz mesajı
        welcome_label = QLabel("Hoş Geldiniz!")
        welcome_font = QFont("Arial", 14)
        welcome_label.setFont(welcome_font)
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setStyleSheet("color: #555; padding: 10px;")
        main_layout.addWidget(welcome_label)

        # Bilgi kutusu
        info_box = QTextEdit()
        info_box.setReadOnly(True)
        info_box.setMaximumHeight(400)
        info_text = """
        <h2 style='color: #2B579A;'>📋 Proje Durumu</h2>
        
        <p><b>Versiyon:</b> 1.0.0 - Planlama Fazı</p>
        <p><b>Durum:</b> ✅ Temel yapı oluşturuldu</p>
        
        <h3 style='color: #28A745;'>✅ Tamamlanan İşlemler:</h3>
        <ul>
            <li>Kapsamlı dokümantasyon (README, DOCUMENTATION)</li>
            <li>16 tablolu veritabanı tasarımı</li>
            <li>Proje klasör yapısı</li>
            <li>Git repository ve GitHub push</li>
            <li>PyQt6 ana pencere template</li>
        </ul>
        
        <h3 style='color: #FFC107;'>⏳ Devam Eden Çalışmalar:</h3>
        <ul>
            <li>Faz 1: Temel Altyapı (2 hafta)</li>
            <li>Veritabanı migration script'leri</li>
            <li>SQLAlchemy model implementasyonları</li>
            <li>Kullanıcı arayüzü geliştirme</li>
        </ul>
        
        <h3 style='color: #2196F3;'>📊 Planlanan Modüller:</h3>
        <ul>
            <li>🧑 Müşteri Yönetimi</li>
            <li>📱 Cihaz Takibi</li>
            <li>🔧 Servis Yönetimi</li>
            <li>📦 Stok/Parça Yönetimi</li>
            <li>💰 Cari Hesap Takibi</li>
            <li>🏦 Kasa Yönetimi</li>
            <li>📊 Raporlama Sistemi</li>
            <li>📧 E-posta Entegrasyonu</li>
            <li>📱 SMS/WhatsApp Bildirimleri</li>
            <li>🖨️ Yazıcı Desteği</li>
        </ul>
        
        <h3 style='color: #DC3545;'>⚠️ Not:</h3>
        <p>Bu, uygulamanın ilk prototip versiyonudur. Tam işlevsellik için geliştirme 
        aşamasının tamamlanması gerekmektedir.</p>
        
        <hr>
        <p><b>GitHub:</b> <a href='https://github.com/unaluslusoy/TeknikServisYazilim'>
        https://github.com/unaluslusoy/TeknikServisYazilim</a></p>
        <p><b>Tahmini Tamamlanma:</b> 18-20 hafta</p>
        """
        info_box.setHtml(info_text)
        main_layout.addWidget(info_box)

        # Buton paneli
        button_layout = QHBoxLayout()

        # Dokümantasyon butonu
        docs_btn = QPushButton("📚 Dokümantasyon")
        docs_btn.setStyleSheet("""
            QPushButton {
                background-color: #2B579A;
                color: white;
                padding: 10px 20px;
                font-size: 14px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #1e3f6f;
            }
        """)
        docs_btn.clicked.connect(self.open_documentation)
        button_layout.addWidget(docs_btn)

        # GitHub butonu
        github_btn = QPushButton("🔗 GitHub Repository")
        github_btn.setStyleSheet("""
            QPushButton {
                background-color: #28A745;
                color: white;
                padding: 10px 20px;
                font-size: 14px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #1e7e34;
            }
        """)
        github_btn.clicked.connect(self.open_github)
        button_layout.addWidget(github_btn)

        # Çıkış butonu
        exit_btn = QPushButton("❌ Çıkış")
        exit_btn.setStyleSheet("""
            QPushButton {
                background-color: #DC3545;
                color: white;
                padding: 10px 20px;
                font-size: 14px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
        """)
        exit_btn.clicked.connect(self.close)
        button_layout.addWidget(exit_btn)

        main_layout.addLayout(button_layout)

        # Alt bilgi
        footer_label = QLabel("© 2024 Teknik Servis Yönetim Sistemi | Python 3.11+ | PyQt6")
        footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer_label.setStyleSheet("color: #888; padding: 10px; font-size: 10px;")
        main_layout.addWidget(footer_label)

        # Pencere stilini ayarla
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QTextEdit {
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 10px;
            }
        """)

    def open_documentation(self):
        """Dokümantasyonu aç"""
        import webbrowser
        import os
        doc_path = os.path.join(os.path.dirname(__file__), "README.md")
        if os.path.exists(doc_path):
            webbrowser.open(doc_path)
        else:
            print("Dokümantasyon dosyası bulunamadı!")

    def open_github(self):
        """GitHub repository'yi aç"""
        import webbrowser
        webbrowser.open("https://github.com/unaluslusoy/TeknikServisYazilim")


def main():
    """Ana uygulama fonksiyonu"""
    app = QApplication(sys.argv)

    # Uygulama bilgileri
    app.setApplicationName("Teknik Servis Yönetim Sistemi")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("Teknik Servis")

    # Ana pencereyi oluştur ve göster
    window = MainWindow()
    window.show()

    # Uygulama döngüsünü başlat
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
