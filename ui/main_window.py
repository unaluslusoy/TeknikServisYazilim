"""
Ana Pencere - Dashboard
"""

import os
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTextEdit, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon, QPixmap


class MainWindow(QMainWindow):
    """Ana uygulama penceresi"""

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """UI bileşenlerini başlat"""
        self.setWindowTitle("Teknik Servis Yönetim Sistemi v1.0.0")
        self.setGeometry(100, 100, 1100, 800)

        # Window icon ayarla
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                "resources", "icons", "icon.jpeg")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        # Merkezi widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setStyleSheet("background-color: #FAFAFA;")

        # Ana layout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Header
        header_widget = QWidget()
        header_layout = QVBoxLayout()
        header_widget.setLayout(header_layout)
        header_widget.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #2B579A, stop:1 #1e3f6f);
            }
        """)

        # Logo
        logo_label = QLabel()
        logo_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                "resources", "images", "logo.jpeg")
        if os.path.exists(logo_path):
            pixmap = QPixmap(logo_path)
            scaled_pixmap = pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio,
                                         Qt.TransformationMode.SmoothTransformation)
            logo_label.setPixmap(scaled_pixmap)
            logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            logo_label.setStyleSheet("padding: 15px 10px 8px 10px; background: transparent;")
            header_layout.addWidget(logo_label)

        # Başlık
        title_label = QLabel("Teknik Servis Yönetim Sistemi")
        title_label.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: white; padding: 5px; background: transparent;")
        header_layout.addWidget(title_label)

        # Versiyon
        version_label = QLabel("v1.0.0")
        version_label.setFont(QFont("Segoe UI", 10))
        version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        version_label.setStyleSheet("color: #E0E0E0; padding-bottom: 15px; background: transparent;")
        header_layout.addWidget(version_label)

        main_layout.addWidget(header_widget)

        # Hoş geldiniz
        welcome_label = QLabel("🎉 Hoş Geldiniz!")
        welcome_label.setFont(QFont("Segoe UI", 18, QFont.Weight.Medium))
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setStyleSheet("""
            color: #2B579A; 
            padding: 25px;
            background-color: #E3F2FD;
            margin: 20px 30px 15px 30px;
            border-radius: 10px;
            border: 2px solid #2B579A;
        """)
        main_layout.addWidget(welcome_label)

        # Sistem özeti
        info_box = QTextEdit()
        info_box.setReadOnly(True)
        info_box.setMaximumHeight(220)
        info_box.setStyleSheet("""
            QTextEdit {
                background-color: white;
                border: 2px solid #2B579A;
                border-radius: 10px;
                padding: 20px;
                margin: 10px 30px 15px 30px;
                font-family: 'Segoe UI';
                font-size: 11pt;
            }
        """)
        info_text = """
        <div style='background-color: white;'>
        <h2 style='color: #2B579A; border-bottom: 3px solid #2B579A; padding-bottom: 10px; margin-top: 0;'>
            📊 Sistem Özeti
        </h2>
        
        <p style='font-size: 11pt; margin: 15px 0; color: #555; line-height: 1.6;'>
            <b style='color: #2B579A;'>Teknik Servis Yönetim Sistemi</b>, telefon, tablet, bilgisayar ve 
            elektronik cihaz servisleri için geliştirilmiş kapsamlı bir yönetim platformudur.
        </p>
        
        <h3 style='color: #2196F3; margin-top: 18px; border-left: 4px solid #2196F3; padding-left: 12px; font-size: 12pt;'>
            🎯 Ana Modüller
        </h3>
        <table style='width: 100%; color: #333; line-height: 1.8; margin-top: 8px;'>
            <tr>
                <td style='width: 50%; padding: 5px;'>🧑 Müşteri Yönetimi</td>
                <td style='width: 50%; padding: 5px;'>📱 Cihaz Takibi</td>
            </tr>
            <tr>
                <td style='padding: 5px;'>🔧 Servis Yönetimi</td>
                <td style='padding: 5px;'>📦 Stok/Parça Yönetimi</td>
            </tr>
            <tr>
                <td style='padding: 5px;'>💰 Cari Hesap</td>
                <td style='padding: 5px;'>🏦 Kasa Yönetimi</td>
            </tr>
            <tr>
                <td style='padding: 5px;'>📊 Raporlama</td>
                <td style='padding: 5px;'>📧 E-posta & SMS</td>
            </tr>
        </table>
        </div>
        """
        info_box.setHtml(info_text)
        main_layout.addWidget(info_box)

        # Hızlı erişim başlığı
        quick_label = QLabel("⚡ Hızlı Erişim")
        quick_label.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        quick_label.setStyleSheet("color: #2B579A; margin: 10px 30px 10px 30px;")
        main_layout.addWidget(quick_label)

        # Butonlar
        button_container = QWidget()
        button_grid = QVBoxLayout()
        button_grid.setSpacing(10)
        button_grid.setContentsMargins(30, 0, 30, 15)
        button_container.setLayout(button_grid)

        # İlk satır
        row1 = QHBoxLayout()
        row1.setSpacing(15)

        new_service_btn = self.create_button("🔧 Yeni Servis", "#2B579A", "#1e3f6f")
        new_service_btn.clicked.connect(lambda: self.show_info("Yeni Servis Kaydı", "Yeni servis kaydı modülü geliştiriliyor..."))
        row1.addWidget(new_service_btn)

        new_customer_btn = self.create_button("🧑 Yeni Müşteri", "#28A745", "#218838")
        new_customer_btn.clicked.connect(lambda: self.show_info("Yeni Müşteri", "Yeni müşteri kaydı modülü geliştiriliyor..."))
        row1.addWidget(new_customer_btn)

        button_grid.addLayout(row1)

        # İkinci satır
        row2 = QHBoxLayout()
        row2.setSpacing(15)

        reports_btn = self.create_button("📊 Raporlar", "#F57C00", "#E65100")
        reports_btn.clicked.connect(lambda: self.show_info("Raporlar", "Raporlama modülü geliştiriliyor..."))
        row2.addWidget(reports_btn)

        settings_btn = self.create_button("⚙️ Ayarlar", "#9C27B0", "#7B1FA2")
        settings_btn.clicked.connect(lambda: self.show_info("Ayarlar", "Ayarlar modülü geliştiriliyor..."))
        row2.addWidget(settings_btn)

        button_grid.addLayout(row2)
        main_layout.addWidget(button_container)

        # Footer
        footer_label = QLabel("© 2024 Teknik Servis Yönetim Sistemi | Python 3.13+ | PyQt6 6.10.1")
        footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer_label.setFont(QFont("Segoe UI", 9))
        footer_label.setStyleSheet("""
            color: #777; 
            padding: 15px; 
            background-color: #F0F0F0;
            border-top: 2px solid #D0D0D0;
        """)
        main_layout.addWidget(footer_label)

    def create_button(self, text, bg_color, hover_color):
        """Buton oluştur"""
        btn = QPushButton(text)
        btn.setMinimumHeight(55)
        btn.setFont(QFont("Segoe UI", 11, QFont.Weight.Medium))
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {bg_color};
                color: white;
                border: none;
                border-radius: 10px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {hover_color};
            }}
        """)
        return btn

    def show_info(self, title, message):
        """Bilgi mesajı göster"""
        QMessageBox.information(self, title, message, QMessageBox.StandardButton.Ok)

