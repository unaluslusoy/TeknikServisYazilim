# -*- coding: utf-8 -*-
"""
Login Dialog - Giriş Ekranı (Düzeltilmiş)
"""

import os
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QMessageBox, QSpacerItem, QSizePolicy
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
        self.setWindowTitle("Teknik Servis - Giris")
        self.setFixedSize(420, 580)
        self.setModal(True)

        # Window icon
        icon_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                "resources", "icons", "icon.jpeg")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        # Ana layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(50, 40, 50, 40)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        # Üst boşluk
        main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        # Logo
        logo_label = QLabel()
        logo_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                "resources", "images", "logo.jpeg")
        if os.path.exists(logo_path):
            pixmap = QPixmap(logo_path)
            scaled_pixmap = pixmap.scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio,
                                         Qt.TransformationMode.SmoothTransformation)
            logo_label.setPixmap(scaled_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(logo_label)

        main_layout.addSpacing(20)

        # Başlık
        title_label = QLabel("Teknik Servis\nYonetim Sistemi")
        title_label.setFont(QFont("Segoe UI", 22, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #2B579A;")
        main_layout.addWidget(title_label)

        main_layout.addSpacing(10)

        # Alt başlık
        subtitle_label = QLabel("Hos Geldiniz")
        subtitle_label.setFont(QFont("Segoe UI", 12))
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle_label.setStyleSheet("color: #6C757D;")
        main_layout.addWidget(subtitle_label)

        main_layout.addSpacing(30)

        # Kullanıcı adı input
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Kullanici adinizi girin")
        self.username_input.setFont(QFont("Segoe UI", 11))
        self.username_input.setMinimumHeight(48)
        self.username_input.setStyleSheet("""
            QLineEdit {
                padding: 12px 16px;
                border: 2px solid #E0E0E0;
                border-radius: 10px;
                background-color: #F8F9FA;
                color: #333;
            }
            QLineEdit:focus {
                border: 2px solid #2B579A;
                background-color: white;
            }
        """)
        main_layout.addWidget(self.username_input)

        main_layout.addSpacing(15)

        # Şifre input
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Sifrenizi girin")
        self.password_input.setFont(QFont("Segoe UI", 11))
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setMinimumHeight(48)
        self.password_input.setStyleSheet("""
            QLineEdit {
                padding: 12px 16px;
                border: 2px solid #E0E0E0;
                border-radius: 10px;
                background-color: #F8F9FA;
                color: #333;
            }
            QLineEdit:focus {
                border: 2px solid #2B579A;
                background-color: white;
            }
        """)
        self.password_input.returnPressed.connect(self.handle_login)
        main_layout.addWidget(self.password_input)

        main_layout.addSpacing(25)

        # Giriş butonu
        login_btn = QPushButton("Giris Yap")
        login_btn.setFont(QFont("Segoe UI", 13, QFont.Weight.Bold))
        login_btn.setMinimumHeight(52)
        login_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        login_btn.setStyleSheet("""
            QPushButton {
                background-color: #2B579A;
                color: white;
                border: none;
                border-radius: 10px;
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

        main_layout.addSpacing(20)

        # Demo bilgisi
        demo_label = QLabel("Demo: admin / admin")
        demo_label.setFont(QFont("Segoe UI", 10))
        demo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        demo_label.setStyleSheet("""
            color: #E65100; 
            background-color: #FFF3E0;
            padding: 12px;
            border-radius: 8px;
            border: 1px solid #FFE0B2;
        """)
        main_layout.addWidget(demo_label)

        # Esnek boşluk
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Versiyon
        version_label = QLabel("v1.0.0")
        version_label.setFont(QFont("Segoe UI", 9))
        version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        version_label.setStyleSheet("color: #999;")
        main_layout.addWidget(version_label)

        # Arka plan rengi
        self.setStyleSheet("QDialog { background-color: white; }")

        # Focus
        self.username_input.setFocus()

    def handle_login(self):
        """Giriş işlemi"""
        username = self.username_input.text().strip()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Uyari", "Lutfen kullanici adi ve sifre girin!")
            return

        if username == "admin" and password == "admin":
            self.accept()
        else:
            QMessageBox.critical(self, "Hata", "Kullanici adi veya sifre hatali!\n\nDemo: admin / admin")
            self.password_input.clear()
            self.password_input.setFocus()

