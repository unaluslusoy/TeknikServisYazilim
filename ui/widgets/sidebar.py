# -*- coding: utf-8 -*-
"""
Modern Sidebar - Sol Menü
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QScrollArea
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont, QIcon
from ui.styles.brand import BrandColors, BrandFonts, BrandSizes


class SidebarButton(QPushButton):
    """Sidebar menü butonu"""

    def __init__(self, icon_text, text, parent=None):
        super().__init__(parent)
        self.icon_text = icon_text
        self.button_text = text
        self.is_active = False

        self.setText(f"{icon_text}  {text}")
        self.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_NORMAL))
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setMinimumHeight(45)

        self.update_style()

    def set_active(self, active):
        """Aktif durumu ayarla"""
        self.is_active = active
        self.update_style()

    def update_style(self):
        """Stil güncelle"""
        if self.is_active:
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: {BrandColors.PRIMARY};
                    color: {BrandColors.TEXT_LIGHT};
                    border: none;
                    border-radius: {BrandSizes.RADIUS_MEDIUM}px;
                    padding: 12px 15px;
                    text-align: left;
                    font-weight: bold;
                }}
            """)
        else:
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: transparent;
                    color: {BrandColors.TEXT_LIGHT};
                    border: none;
                    border-radius: {BrandSizes.RADIUS_MEDIUM}px;
                    padding: 12px 15px;
                    text-align: left;
                }}
                QPushButton:hover {{
                    background-color: rgba(255, 255, 255, 0.1);
                }}
            """)


class Sidebar(QWidget):
    """Modern sidebar widget"""

    menu_clicked = pyqtSignal(str)  # Menü tıklama sinyali

    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_button = None
        self.init_ui()

    def init_ui(self):
        """UI bileşenlerini başlat"""
        self.setFixedWidth(BrandSizes.SIDEBAR_WIDTH)
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {BrandColors.BG_SIDEBAR};
            }}
        """)

        # Ana layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(15, 20, 15, 20)
        main_layout.setSpacing(5)
        self.setLayout(main_layout)

        # Logo ve başlık
        header_widget = QWidget()
        header_layout = QVBoxLayout()
        header_layout.setSpacing(5)
        header_widget.setLayout(header_layout)

        logo_label = QLabel("⚙️")
        logo_label.setFont(QFont(BrandFonts.FAMILY, 32))
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo_label.setStyleSheet(f"color: {BrandColors.PRIMARY_LIGHT};")
        header_layout.addWidget(logo_label)

        title_label = QLabel("Teknik Servis")
        title_label.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_LARGE, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet(f"color: {BrandColors.TEXT_LIGHT};")
        header_layout.addWidget(title_label)

        subtitle_label = QLabel("Yönetim Sistemi")
        subtitle_label.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_SMALL))
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle_label.setStyleSheet(f"color: {BrandColors.DARK_GRAY};")
        header_layout.addWidget(subtitle_label)

        main_layout.addWidget(header_widget)
        main_layout.addSpacing(20)

        # Ayırıcı çizgi
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setStyleSheet(f"background-color: rgba(255, 255, 255, 0.1);")
        main_layout.addWidget(separator)
        main_layout.addSpacing(10)

        # Menü scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        menu_widget = QWidget()
        menu_layout = QVBoxLayout()
        menu_layout.setSpacing(5)
        menu_layout.setContentsMargins(0, 0, 0, 0)
        menu_widget.setLayout(menu_layout)

        # Menü öğeleri
        self.menu_items = [
            ("📊", "Dashboard", "dashboard"),
            ("🧑", "Müşteriler", "customers"),
            ("📱", "Cihazlar", "devices"),
            ("🔧", "Servisler", "services"),
            ("📦", "Stok Yönetimi", "inventory"),
            ("💰", "Cari Hesap", "accounts"),
            ("🏦", "Kasa", "cash"),
            ("📊", "Raporlar", "reports"),
            ("📧", "Bildirimler", "notifications"),
            ("⚙️", "Ayarlar", "settings"),
        ]

        self.buttons = {}
        for icon, text, key in self.menu_items:
            btn = SidebarButton(icon, text)
            btn.clicked.connect(lambda checked, k=key: self.on_menu_click(k))
            menu_layout.addWidget(btn)
            self.buttons[key] = btn

        menu_layout.addStretch()
        scroll.setWidget(menu_widget)
        main_layout.addWidget(scroll)

        # Alt bilgi
        main_layout.addSpacing(10)
        separator2 = QFrame()
        separator2.setFrameShape(QFrame.Shape.HLine)
        separator2.setStyleSheet(f"background-color: rgba(255, 255, 255, 0.1);")
        main_layout.addWidget(separator2)

        user_label = QLabel("👤 Admin")
        user_label.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_NORMAL))
        user_label.setStyleSheet(f"color: {BrandColors.TEXT_LIGHT}; padding: 10px;")
        main_layout.addWidget(user_label)

        # Dashboard'ı varsayılan olarak aktif yap
        self.set_active_menu("dashboard")

    def on_menu_click(self, key):
        """Menü tıklama olayı"""
        self.set_active_menu(key)
        self.menu_clicked.emit(key)

    def set_active_menu(self, key):
        """Aktif menüyü ayarla"""
        # Tüm butonları pasif yap
        for btn in self.buttons.values():
            btn.set_active(False)

        # Seçilen butonu aktif yap
        if key in self.buttons:
            self.buttons[key].set_active(True)
            self.current_button = key

