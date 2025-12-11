# -*- coding: utf-8 -*-
"""
Modern Ana Pencere - Responsive Dashboard
"""

import os
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QScrollArea, QFrame, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
from ui.styles.brand import BrandColors, BrandFonts, BrandSizes, GLOBAL_STYLE
from ui.widgets.sidebar import Sidebar
from ui.widgets.header_bar import HeaderBar
from ui.widgets.stat_card import StatCard


class MainWindow(QMainWindow):
    """Modern responsive ana pencere"""

    def __init__(self):
        super().__init__()
        self.current_page = "dashboard"
        self.init_ui()

    def init_ui(self):
        """UI bileşenlerini başlat"""
        self.setWindowTitle("Teknik Servis Yönetim Sistemi v1.0.0")
        self.setMinimumSize(1200, 700)

        # Window icon
        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                "resources", "icons", "icon.jpeg")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        # Global stil
        self.setStyleSheet(GLOBAL_STYLE)

        # Merkezi widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Ana layout (Horizontal: Sidebar + Content)
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        central_widget.setLayout(main_layout)

        # Sidebar
        self.sidebar = Sidebar()
        self.sidebar.menu_clicked.connect(self.on_menu_change)
        main_layout.addWidget(self.sidebar)

        # Sağ taraf (Header + Content)
        right_container = QWidget()
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)
        right_container.setLayout(right_layout)

        # Header bar
        self.header_bar = HeaderBar()
        self.header_bar.logout_clicked.connect(self.handle_logout)
        right_layout.addWidget(self.header_bar)

        # Content area (scroll)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setStyleSheet(f"QScrollArea {{ border: none; background-color: {BrandColors.BG_MAIN}; }}")

        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout()
        self.content_layout.setContentsMargins(25, 25, 25, 25)
        self.content_layout.setSpacing(20)
        self.content_widget.setLayout(self.content_layout)

        scroll.setWidget(self.content_widget)
        right_layout.addWidget(scroll)

        main_layout.addWidget(right_container)

        # Dashboard'ı yükle
        self.show_dashboard()

    def clear_content(self):
        """İçeriği temizle"""
        while self.content_layout.count():
            child = self.content_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def on_menu_change(self, menu_key):
        """Menü değiştiğinde"""
        self.current_page = menu_key

        # Sayfa başlığını güncelle
        page_titles = {
            "dashboard": "Dashboard",
            "customers": "Müşteri Yönetimi",
            "devices": "Cihaz Yönetimi",
            "services": "Servis Yönetimi",
            "inventory": "Stok Yönetimi",
            "accounts": "Cari Hesap",
            "cash": "Kasa Yönetimi",
            "reports": "Raporlar",
            "notifications": "Bildirimler",
            "settings": "Ayarlar",
        }
        self.header_bar.set_page_title(page_titles.get(menu_key, menu_key))

        # İçeriği yükle
        if menu_key == "dashboard":
            self.show_dashboard()
        elif menu_key == "customers":
            self.show_customers()
        elif menu_key == "services":
            self.show_services()
        else:
            self.show_coming_soon(page_titles.get(menu_key, menu_key))

    def show_dashboard(self):
        """Dashboard göster"""
        self.clear_content()

        # Hoş geldiniz mesajı
        welcome_label = QLabel("👋 Hoş Geldiniz!")
        welcome_label.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_XLARGE, QFont.Weight.Bold))
        welcome_label.setStyleSheet(f"color: {BrandColors.TEXT_PRIMARY}; background: transparent;")
        self.content_layout.addWidget(welcome_label)

        subtitle_label = QLabel("Bugünün özeti ve hızlı erişim")
        subtitle_label.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_NORMAL))
        subtitle_label.setStyleSheet(f"color: {BrandColors.TEXT_SECONDARY}; background: transparent;")
        self.content_layout.addWidget(subtitle_label)

        self.content_layout.addSpacing(10)

        # İstatistik kartları (Grid layout - Responsive)
        stats_grid = QGridLayout()
        stats_grid.setSpacing(15)

        # Stat kartları
        stats = [
            ("Bugünkü Servisler", "24", "🔧", BrandColors.PRIMARY),
            ("Bekleyen İşler", "12", "⏳", BrandColors.WARNING),
            ("Tamamlanan", "156", "✅", BrandColors.SECONDARY),
            ("Toplam Ciro", "₺45,280", "💰", BrandColors.INFO),
        ]

        for i, (title, value, icon, color) in enumerate(stats):
            card = StatCard(title, value, icon, color)
            stats_grid.addWidget(card, i // 4, i % 4)

        self.content_layout.addLayout(stats_grid)

        # Hızlı İşlemler
        self.content_layout.addSpacing(10)

        quick_label = QLabel("⚡ Hızlı İşlemler")
        quick_label.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_LARGE, QFont.Weight.Bold))
        quick_label.setStyleSheet(f"color: {BrandColors.TEXT_PRIMARY}; background: transparent;")
        self.content_layout.addWidget(quick_label)

        # Quick action butonları
        quick_grid = QGridLayout()
        quick_grid.setSpacing(15)

        quick_actions = [
            ("🔧 Yeni Servis", BrandColors.PRIMARY),
            ("🧑 Yeni Müşteri", BrandColors.SECONDARY),
            ("📦 Stok Girişi", BrandColors.WARNING),
            ("💰 Tahsilat", BrandColors.INFO),
        ]

        from PyQt6.QtWidgets import QPushButton
        for i, (text, color) in enumerate(quick_actions):
            btn = QPushButton(text)
            btn.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_MEDIUM, QFont.Weight.Bold))
            btn.setMinimumHeight(60)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    color: white;
                    border: none;
                    border-radius: {BrandSizes.RADIUS_LARGE}px;
                    padding: 15px;
                }}
                QPushButton:hover {{
                    background-color: {BrandColors.PRIMARY_DARK};
                }}
            """)
            btn.clicked.connect(lambda checked, t=text: self.show_info("Hızlı İşlem", f"{t} modülü geliştiriliyor..."))
            quick_grid.addWidget(btn, i // 2, i % 2)

        self.content_layout.addLayout(quick_grid)

        # Son aktiviteler
        self.content_layout.addSpacing(10)

        activity_label = QLabel("📋 Son Aktiviteler")
        activity_label.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_LARGE, QFont.Weight.Bold))
        activity_label.setStyleSheet(f"color: {BrandColors.TEXT_PRIMARY}; background: transparent;")
        self.content_layout.addWidget(activity_label)

        # Aktivite listesi
        activity_frame = QFrame()
        activity_frame.setStyleSheet(f"""
            QFrame {{
                background-color: {BrandColors.BG_CARD};
                border: 1px solid {BrandColors.BORDER_LIGHT};
                border-radius: {BrandSizes.RADIUS_LARGE}px;
                padding: 15px;
            }}
        """)
        activity_layout = QVBoxLayout()
        activity_frame.setLayout(activity_layout)

        activities = [
            "🔧 Servis #1234 - iPhone 13 ekran değişimi tamamlandı",
            "🧑 Yeni müşteri kaydı - Ahmet Yılmaz",
            "💰 Tahsilat yapıldı - ₺1,250",
            "📦 Stok girişi - 10 adet ekran",
            "📧 Müşteriye bildirim gönderildi",
        ]

        for activity in activities:
            activity_item = QLabel(activity)
            activity_item.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_NORMAL))
            activity_item.setStyleSheet(f"""
                QLabel {{
                    color: {BrandColors.TEXT_PRIMARY};
                    padding: 10px;
                    border-bottom: 1px solid {BrandColors.BORDER_LIGHT};
                    background: transparent;
                }}
            """)
            activity_layout.addWidget(activity_item)

        self.content_layout.addWidget(activity_frame)
        self.content_layout.addStretch()

    def show_customers(self):
        """Müşteri sayfası"""
        self.clear_content()

        title = QLabel("👥 Müşteri Yönetimi")
        title.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_XLARGE, QFont.Weight.Bold))
        title.setStyleSheet(f"color: {BrandColors.TEXT_PRIMARY}; background: transparent;")
        self.content_layout.addWidget(title)

        info = QLabel("Müşteri listesi ve yönetim modülü geliştiriliyor...")
        info.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_MEDIUM))
        info.setStyleSheet(f"color: {BrandColors.TEXT_SECONDARY}; background: transparent;")
        self.content_layout.addWidget(info)

        self.content_layout.addStretch()

    def show_services(self):
        """Servis sayfası"""
        self.clear_content()

        title = QLabel("🔧 Servis Yönetimi")
        title.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_XLARGE, QFont.Weight.Bold))
        title.setStyleSheet(f"color: {BrandColors.TEXT_PRIMARY}; background: transparent;")
        self.content_layout.addWidget(title)

        info = QLabel("Servis kayıt ve takip modülü geliştiriliyor...")
        info.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_MEDIUM))
        info.setStyleSheet(f"color: {BrandColors.TEXT_SECONDARY}; background: transparent;")
        self.content_layout.addWidget(info)

        self.content_layout.addStretch()

    def show_coming_soon(self, page_name):
        """Yakında gelecek sayfası"""
        self.clear_content()

        title = QLabel(f"🚧 {page_name}")
        title.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_XLARGE, QFont.Weight.Bold))
        title.setStyleSheet(f"color: {BrandColors.TEXT_PRIMARY}; background: transparent;")
        self.content_layout.addWidget(title)

        info = QLabel("Bu modül geliştirme aşamasındadır...")
        info.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_MEDIUM))
        info.setStyleSheet(f"color: {BrandColors.TEXT_SECONDARY}; background: transparent;")
        self.content_layout.addWidget(info)

        self.content_layout.addStretch()

    def handle_logout(self):
        """Çıkış yap"""
        reply = QMessageBox.question(
            self,
            "Çıkış",
            "Çıkış yapmak istediğinize emin misiniz?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.close()

    def show_info(self, title, message):
        """Bilgi mesajı göster"""
        QMessageBox.information(self, title, message, QMessageBox.StandardButton.Ok)

