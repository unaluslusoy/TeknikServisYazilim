# -*- coding: utf-8 -*-
"""
Modern Sidebar - Sol Menu (Emoji yok)
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QScrollArea
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont, QPixmap
import os
from ui.styles.brand import BrandColors, BrandFonts, BrandSizes


class SidebarButton(QPushButton):
    """Sidebar menu butonu"""

    def __init__(self, icon_text, text, parent=None):
        super().__init__(parent)
        self.icon_text = icon_text
        self.button_text = text
        self.is_active = False

        self.setText(f"  {icon_text}   {text}")
        self.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_NORMAL))
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setMinimumHeight(48)

        self.update_style()

    def set_active(self, active):
        self.is_active = active
        self.update_style()

    def update_style(self):
        if self.is_active:
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: {BrandColors.PRIMARY};
                    color: {BrandColors.TEXT_LIGHT};
                    border: none;
                    border-radius: {BrandSizes.RADIUS_MEDIUM}px;
                    padding: 12px 16px;
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
                    padding: 12px 16px;
                    text-align: left;
                }}
                QPushButton:hover {{
                    background-color: rgba(255, 255, 255, 0.1);
                }}
            """)


class Sidebar(QWidget):
    """Modern sidebar widget"""

    menu_clicked = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_button = None
        self.init_ui()

    def init_ui(self):
        self.setFixedWidth(BrandSizes.SIDEBAR_WIDTH)
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {BrandColors.BG_SIDEBAR};
            }}
        """)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(15, 20, 15, 20)
        main_layout.setSpacing(5)
        self.setLayout(main_layout)

        # Logo container
        logo_container = QWidget()
        logo_layout = QVBoxLayout()
        logo_layout.setSpacing(8)
        logo_layout.setContentsMargins(0, 0, 0, 0)
        logo_container.setLayout(logo_layout)

        # Logo image
        logo_label = QLabel()
        logo_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                "resources", "images", "logo.jpeg")
        if os.path.exists(logo_path):
            pixmap = QPixmap(logo_path)
            scaled = pixmap.scaled(70, 70, Qt.AspectRatioMode.KeepAspectRatio,
                                  Qt.TransformationMode.SmoothTransformation)
            logo_label.setPixmap(scaled)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo_label.setStyleSheet("background: transparent;")
        logo_layout.addWidget(logo_label)

        title_label = QLabel("Teknik Servis")
        title_label.setFont(QFont(BrandFonts.FAMILY, 16, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet(f"color: {BrandColors.TEXT_LIGHT}; background: transparent;")
        logo_layout.addWidget(title_label)

        subtitle_label = QLabel("Yonetim Sistemi")
        subtitle_label.setFont(QFont(BrandFonts.FAMILY, 10))
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle_label.setStyleSheet(f"color: {BrandColors.DARK_GRAY}; background: transparent;")
        logo_layout.addWidget(subtitle_label)

        main_layout.addWidget(logo_container)
        main_layout.addSpacing(20)

        # Separator
        sep = QFrame()
        sep.setFrameShape(QFrame.Shape.HLine)
        sep.setFixedHeight(1)
        sep.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);")
        main_layout.addWidget(sep)
        main_layout.addSpacing(15)

        # Menu scroll
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll.setStyleSheet("""
            QScrollArea { border: none; background: transparent; }
            QScrollBar:vertical { width: 6px; background: transparent; }
            QScrollBar::handle:vertical { background: rgba(255,255,255,0.3); border-radius: 3px; }
        """)

        menu_widget = QWidget()
        menu_widget.setStyleSheet("background: transparent;")
        menu_layout = QVBoxLayout()
        menu_layout.setSpacing(4)
        menu_layout.setContentsMargins(0, 0, 0, 0)
        menu_widget.setLayout(menu_layout)

        # Menu items - ICON KARAKTERLERI (emoji degil)
        self.menu_items = [
            ("H", "Dashboard", "dashboard"),
            ("M", "Musteriler", "customers"),
            ("C", "Cihazlar", "devices"),
            ("S", "Servisler", "services"),
            ("P", "Stok Yonetimi", "inventory"),
            ("$", "Cari Hesap", "accounts"),
            ("K", "Kasa", "cash"),
            ("R", "Raporlar", "reports"),
            ("B", "Bildirimler", "notifications"),
            ("A", "Ayarlar", "settings"),
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

        # Bottom separator
        main_layout.addSpacing(10)
        sep2 = QFrame()
        sep2.setFrameShape(QFrame.Shape.HLine)
        sep2.setFixedHeight(1)
        sep2.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);")
        main_layout.addWidget(sep2)

        # User info
        user_widget = QWidget()
        user_layout = QVBoxLayout()
        user_layout.setContentsMargins(10, 10, 10, 5)
        user_widget.setLayout(user_layout)
        user_widget.setStyleSheet(f"""
            QWidget {{
                background-color: rgba(255, 255, 255, 0.05);
                border-radius: 8px;
            }}
        """)

        user_label = QLabel("Admin")
        user_label.setFont(QFont(BrandFonts.FAMILY, 11, QFont.Weight.Bold))
        user_label.setStyleSheet(f"color: {BrandColors.TEXT_LIGHT}; background: transparent;")
        user_layout.addWidget(user_label)

        role_label = QLabel("Yonetici")
        role_label.setFont(QFont(BrandFonts.FAMILY, 9))
        role_label.setStyleSheet(f"color: {BrandColors.DARK_GRAY}; background: transparent;")
        user_layout.addWidget(role_label)

        main_layout.addWidget(user_widget)

        self.set_active_menu("dashboard")

    def on_menu_click(self, key):
        self.set_active_menu(key)
        self.menu_clicked.emit(key)

    def set_active_menu(self, key):
        for btn in self.buttons.values():
            btn.set_active(False)
        if key in self.buttons:
            self.buttons[key].set_active(True)
            self.current_button = key

