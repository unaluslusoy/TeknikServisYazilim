# -*- coding: utf-8 -*-
"""
Modern Ana Pencere - Responsive Dashboard (Emoji yok, Duzeltilmis)
"""

import os
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QScrollArea, QFrame, QMessageBox, QPushButton
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
        self.setWindowTitle("Teknik Servis Yonetim Sistemi v1.0.0")
        self.setMinimumSize(1200, 700)

        icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                "resources", "icons", "icon.jpeg")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        self.setStyleSheet(GLOBAL_STYLE)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        central_widget.setLayout(main_layout)

        # Sidebar
        self.sidebar = Sidebar()
        self.sidebar.menu_clicked.connect(self.on_menu_change)
        main_layout.addWidget(self.sidebar)

        # Right container
        right_container = QWidget()
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)
        right_container.setLayout(right_layout)

        # Header
        self.header_bar = HeaderBar()
        self.header_bar.logout_clicked.connect(self.handle_logout)
        right_layout.addWidget(self.header_bar)

        # Content scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setStyleSheet(f"""
            QScrollArea {{ border: none; background-color: {BrandColors.BG_MAIN}; }}
            QScrollBar:vertical {{ width: 8px; background: #E0E0E0; }}
            QScrollBar::handle:vertical {{ background: #BDBDBD; border-radius: 4px; }}
        """)

        self.content_widget = QWidget()
        self.content_widget.setStyleSheet(f"background-color: {BrandColors.BG_MAIN};")
        self.content_layout = QVBoxLayout()
        self.content_layout.setContentsMargins(30, 25, 30, 25)
        self.content_layout.setSpacing(20)
        self.content_widget.setLayout(self.content_layout)

        scroll.setWidget(self.content_widget)
        right_layout.addWidget(scroll)

        main_layout.addWidget(right_container)

        self.show_dashboard()

    def clear_content(self):
        while self.content_layout.count():
            child = self.content_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def on_menu_change(self, menu_key):
        self.current_page = menu_key

        page_titles = {
            "dashboard": "Dashboard",
            "customers": "Musteri Yonetimi",
            "devices": "Cihaz Yonetimi",
            "services": "Servis Yonetimi",
            "inventory": "Stok Yonetimi",
            "accounts": "Cari Hesap",
            "cash": "Kasa Yonetimi",
            "reports": "Raporlar",
            "notifications": "Bildirimler",
            "settings": "Ayarlar",
        }
        self.header_bar.set_page_title(page_titles.get(menu_key, menu_key))

        if menu_key == "dashboard":
            self.show_dashboard()
        elif menu_key == "customers":
            self.show_customers()
        elif menu_key == "services":
            self.show_services()
        elif menu_key == "inventory":
            self.show_inventory()
        elif menu_key == "accounts":
            self.show_accounts()
        elif menu_key == "cash":
            self.show_cash()
        elif menu_key == "reports":
            self.show_reports()
        else:
            self.show_coming_soon(page_titles.get(menu_key, menu_key))

    def show_dashboard(self):
        self.clear_content()

        # Welcome
        welcome_label = QLabel("Hos Geldiniz!")
        welcome_label.setFont(QFont(BrandFonts.FAMILY, 24, QFont.Weight.Bold))
        welcome_label.setStyleSheet(f"color: {BrandColors.TEXT_PRIMARY}; background: transparent;")
        self.content_layout.addWidget(welcome_label)

        subtitle = QLabel("Bugunun ozeti ve hizli erisim")
        subtitle.setFont(QFont(BrandFonts.FAMILY, 12))
        subtitle.setStyleSheet(f"color: {BrandColors.TEXT_SECONDARY}; background: transparent;")
        self.content_layout.addWidget(subtitle)

        self.content_layout.addSpacing(15)

        # Stat cards - Grid
        stats_container = QWidget()
        stats_container.setStyleSheet("background: transparent;")
        stats_grid = QHBoxLayout()
        stats_grid.setSpacing(20)
        stats_container.setLayout(stats_grid)

        stats = [
            ("Bugunku Servisler", "24", "S", BrandColors.PRIMARY),
            ("Bekleyen Isler", "12", "B", BrandColors.WARNING),
            ("Tamamlanan", "156", "T", BrandColors.SECONDARY),
            ("Toplam Ciro", "45,280 TL", "$", BrandColors.INFO),
        ]

        for title, value, icon, color in stats:
            card = StatCard(title, value, icon, color)
            stats_grid.addWidget(card)

        self.content_layout.addWidget(stats_container)

        self.content_layout.addSpacing(10)

        # Quick actions title
        quick_title = QLabel("Hizli Islemler")
        quick_title.setFont(QFont(BrandFonts.FAMILY, 16, QFont.Weight.Bold))
        quick_title.setStyleSheet(f"color: {BrandColors.TEXT_PRIMARY}; background: transparent;")
        self.content_layout.addWidget(quick_title)

        # Quick action buttons
        actions_container = QWidget()
        actions_container.setStyleSheet("background: transparent;")
        actions_layout = QGridLayout()
        actions_layout.setSpacing(15)
        actions_container.setLayout(actions_layout)

        actions = [
            ("Yeni Servis", BrandColors.PRIMARY, 0, 0),
            ("Yeni Musteri", BrandColors.SECONDARY, 0, 1),
            ("Stok Girisi", BrandColors.WARNING, 1, 0),
            ("Tahsilat", BrandColors.INFO, 1, 1),
        ]

        for text, color, row, col in actions:
            btn = QPushButton(text)
            btn.setFont(QFont(BrandFonts.FAMILY, 13, QFont.Weight.Bold))
            btn.setMinimumHeight(60)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    color: white;
                    border: none;
                    border-radius: 12px;
                }}
                QPushButton:hover {{
                    background-color: {BrandColors.PRIMARY_DARK};
                }}
            """)
            btn.clicked.connect(lambda c, t=text: self.show_info("Hizli Islem", f"{t} modulu aciliyor..."))
            actions_layout.addWidget(btn, row, col)

        self.content_layout.addWidget(actions_container)

        self.content_layout.addSpacing(10)

        # Recent activities
        activity_title = QLabel("Son Aktiviteler")
        activity_title.setFont(QFont(BrandFonts.FAMILY, 16, QFont.Weight.Bold))
        activity_title.setStyleSheet(f"color: {BrandColors.TEXT_PRIMARY}; background: transparent;")
        self.content_layout.addWidget(activity_title)

        activity_frame = QFrame()
        activity_frame.setStyleSheet(f"""
            QFrame {{
                background-color: {BrandColors.BG_CARD};
                border: 1px solid {BrandColors.BORDER_LIGHT};
                border-radius: 12px;
            }}
        """)
        activity_layout = QVBoxLayout()
        activity_layout.setContentsMargins(0, 0, 0, 0)
        activity_layout.setSpacing(0)
        activity_frame.setLayout(activity_layout)

        activities = [
            ("Servis #1234 - iPhone 13 ekran degisimi tamamlandi", BrandColors.PRIMARY),
            ("Yeni musteri kaydi - Ahmet Yilmaz", BrandColors.SECONDARY),
            ("Tahsilat yapildi - 1.250 TL", BrandColors.INFO),
            ("Stok girisi - 10 adet ekran", BrandColors.WARNING),
            ("Musteriye bildirim gonderildi", BrandColors.DARK_GRAY),
        ]

        for i, (text, color) in enumerate(activities):
            item = QWidget()
            item_layout = QHBoxLayout()
            item_layout.setContentsMargins(20, 15, 20, 15)
            item.setLayout(item_layout)

            # Color indicator
            indicator = QFrame()
            indicator.setFixedSize(8, 8)
            indicator.setStyleSheet(f"background-color: {color}; border-radius: 4px;")
            item_layout.addWidget(indicator)
            item_layout.addSpacing(12)

            label = QLabel(text)
            label.setFont(QFont(BrandFonts.FAMILY, 11))
            label.setStyleSheet(f"color: {BrandColors.TEXT_PRIMARY}; background: transparent;")
            item_layout.addWidget(label)
            item_layout.addStretch()

            if i < len(activities) - 1:
                item.setStyleSheet(f"border-bottom: 1px solid {BrandColors.BORDER_LIGHT};")

            activity_layout.addWidget(item)

        self.content_layout.addWidget(activity_frame)
        self.content_layout.addStretch()

    def show_customers(self):
        self.clear_content()
        self._create_module_page("Musteri Yonetimi", "Musteri listesi ve yonetim islemleri")

    def show_services(self):
        self.clear_content()
        self._create_module_page("Servis Yonetimi", "Servis kayit ve takip islemleri")

    def show_inventory(self):
        self.clear_content()
        self._create_module_page("Stok Yonetimi", "Stok ve parca yonetimi")

    def show_accounts(self):
        self.clear_content()
        self._create_module_page("Cari Hesap", "Musteri alacak ve borc takibi")

    def show_cash(self):
        self.clear_content()
        self._create_module_page("Kasa Yonetimi", "Gunluk kasa islemleri")

    def show_reports(self):
        self.clear_content()
        self._create_module_page("Raporlar", "Detayli raporlar ve analizler")

    def _create_module_page(self, title, description):
        """Modul sayfasi olustur"""
        title_label = QLabel(title)
        title_label.setFont(QFont(BrandFonts.FAMILY, 24, QFont.Weight.Bold))
        title_label.setStyleSheet(f"color: {BrandColors.TEXT_PRIMARY}; background: transparent;")
        self.content_layout.addWidget(title_label)

        desc_label = QLabel(description)
        desc_label.setFont(QFont(BrandFonts.FAMILY, 12))
        desc_label.setStyleSheet(f"color: {BrandColors.TEXT_SECONDARY}; background: transparent;")
        self.content_layout.addWidget(desc_label)

        self.content_layout.addSpacing(20)

        # Placeholder card
        card = QFrame()
        card.setMinimumHeight(400)
        card.setStyleSheet(f"""
            QFrame {{
                background-color: {BrandColors.BG_CARD};
                border: 2px dashed {BrandColors.BORDER_MEDIUM};
                border-radius: 12px;
            }}
        """)
        card_layout = QVBoxLayout()
        card_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card.setLayout(card_layout)

        icon_label = QLabel("[ ]")
        icon_label.setFont(QFont(BrandFonts.FAMILY, 48))
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_label.setStyleSheet(f"color: {BrandColors.BORDER_MEDIUM}; background: transparent;")
        card_layout.addWidget(icon_label)

        msg_label = QLabel(f"{title} modulu hazirlaniyor...")
        msg_label.setFont(QFont(BrandFonts.FAMILY, 14))
        msg_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        msg_label.setStyleSheet(f"color: {BrandColors.TEXT_SECONDARY}; background: transparent;")
        card_layout.addWidget(msg_label)

        self.content_layout.addWidget(card)
        self.content_layout.addStretch()

    def show_coming_soon(self, page_name):
        self.clear_content()
        self._create_module_page(page_name, "Bu modul gelistirme asamasindadir")

    def handle_logout(self):
        reply = QMessageBox.question(
            self, "Cikis",
            "Cikis yapmak istediginize emin misiniz?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.close()

    def show_info(self, title, message):
        QMessageBox.information(self, title, message, QMessageBox.StandardButton.Ok)

