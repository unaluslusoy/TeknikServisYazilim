"""
Login Dialog - Giriş Ekranı
"""

import os
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QFrame, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QIcon


class LoginDialog(QDialog):
    """Kullanıcı giriş ekranı"""

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """UI bileşenlerini başlat"""
        self.setWindowTitle("Teknik Servis - Giriş")
        self.setFixedSize(450, 600)
        self.setModal(True)

        # Window icon
        icon_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                "resources", "icons", "icon.jpeg")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        # Ana layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 30, 40, 30)
        main_layout.setSpacing(15)
        self.setLayout(main_layout)

        # Logo
        logo_label = QLabel()
        logo_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                "resources", "images", "logo.jpeg")
        if os.path.exists(logo_path):
            pixmap = QPixmap(logo_path)
            scaled_pixmap = pixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio,
                                         Qt.TransformationMode.SmoothTransformation)
            logo_label.setPixmap(scaled_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(logo_label)

        # Başlık
        title_label = QLabel("Teknik Servis\nYönetim Sistemi")
        title_label.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #2B579A; margin-bottom: 10px;")
        main_layout.addWidget(title_label)

        # Alt başlık
        subtitle_label = QLabel("Hoş Geldiniz")
        subtitle_label.setFont(QFont("Segoe UI", 12))
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle_label.setStyleSheet("color: #666; margin-bottom: 20px;")
        main_layout.addWidget(subtitle_label)

        # Form container
        form_frame = QFrame()
        form_frame.setStyleSheet("""
            QFrame {
                background-color: #F8F9FA;
                border-radius: 10px;
                padding: 20px;
            }
        """)
        form_layout = QVBoxLayout()
        form_frame.setLayout(form_layout)

        # Kullanıcı adı
        username_label = QLabel("Kullanıcı Adı")
        username_label.setFont(QFont("Segoe UI", 10, QFont.Weight.Medium))
        username_label.setStyleSheet("color: #333; margin-bottom: 5px;")
        form_layout.addWidget(username_label)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Kullanıcı adınızı girin")
        self.username_input.setFont(QFont("Segoe UI", 11))
        self.username_input.setMinimumHeight(45)
        self.username_input.setStyleSheet("""
            QLineEdit {
                padding: 10px 15px;
                border: 2px solid #E0E0E0;
                border-radius: 8px;
                background-color: white;
                color: #333;
            }
            QLineEdit:focus {
                border: 2px solid #2B579A;
            }
        """)
        form_layout.addWidget(self.username_input)

        form_layout.addSpacing(15)

        # Şifre
        password_label = QLabel("Şifre")
        password_label.setFont(QFont("Segoe UI", 10, QFont.Weight.Medium))
        password_label.setStyleSheet("color: #333; margin-bottom: 5px;")
        form_layout.addWidget(password_label)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Şifrenizi girin")
        self.password_input.setFont(QFont("Segoe UI", 11))
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setMinimumHeight(45)
        self.password_input.setStyleSheet("""
            QLineEdit {
                padding: 10px 15px;
                border: 2px solid #E0E0E0;
                border-radius: 8px;
                background-color: white;
                color: #333;
            }
            QLineEdit:focus {
                border: 2px solid #2B579A;
            }
        """)
        # Enter tuşu ile giriş
        self.password_input.returnPressed.connect(self.handle_login)
        form_layout.addWidget(self.password_input)

        main_layout.addWidget(form_frame)

        # Giriş butonu
        login_btn = QPushButton("🔐 Giriş Yap")
        login_btn.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        login_btn.setMinimumHeight(50)
        login_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        login_btn.setStyleSheet("""
            QPushButton {
                background-color: #2B579A;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 12px;
            }
            QPushButton:hover {
                background-color: #1e3f6f;
            }
            QPushButton:pressed {
                background-color: #153056;
            }
        """)
        login_btn.clicked.connect(self.handle_login)
        main_layout.addWidget(login_btn)

        # Demo bilgisi
        demo_label = QLabel("Demo: admin / admin")
        demo_label.setFont(QFont("Segoe UI", 9))
        demo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        demo_label.setStyleSheet("""
 istiyorum kullanışlı            QLabel {
                color: #E65100; 
                background-color: #FFF3E0;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #FFE0B2;
            }
        """)
        main_layout.addWidget(demo_label)

        # Versiyon
        version_label = QLabel("v1.0.0")
        version_label.setFont(QFont("Segoe UI", 8))
        version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        version_label.setStyleSheet("color: #999;")
        main_layout.addWidget(version_label)

        # Arka plan rengi
        self.setStyleSheet("QDialog { background-color: white; }")

        # Focus'u kullanıcı adına ver
        self.username_input.setFocus()

    def handle_login(self):
        """Giriş işlemini yönet"""
        username = self.username_input.text().strip()
        password = self.password_input.text()

        # Boş alan kontrolü
        if not username or not password:
            QMessageBox.warning(
                self,
                "Uyarı",
                "Lütfen kullanıcı adı ve şifre girin!",
                QMessageBox.StandardButton.Ok
            )
            return

        # Demo giriş kontrolü
        if username == "admin" and password == "admin":
            self.accept()  # Dialog'u başarıyla kapat
        else:
            QMessageBox.critical(
                self,
                "Hata",
                "Kullanıcı adı veya şifre hatalı!\n\nDemo: admin / admin",
                QMessageBox.StandardButton.Ok
            )
            self.password_input.clear()
            self.password_input.setFocus()

