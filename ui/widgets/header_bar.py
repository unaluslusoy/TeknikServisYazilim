# -*- coding: utf-8 -*-
"""
Modern Header Bar - Üst Bar
"""

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
from ui.styles.brand import BrandColors, BrandFonts, BrandSizes


class HeaderBar(QWidget):
    """Modern header bar widget"""

    logout_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        """UI bileşenlerini başlat"""
        self.setFixedHeight(BrandSizes.HEADER_HEIGHT)
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {BrandColors.WHITE};
                border-bottom: 1px solid {BrandColors.BORDER_LIGHT};
            }}
        """)

        # Ana layout
        layout = QHBoxLayout()
        layout.setContentsMargins(20, 10, 20, 10)
        layout.setSpacing(15)
        self.setLayout(layout)

        # Sayfa başlığı
        self.page_title = QLabel("Dashboard")
        self.page_title.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_LARGE, QFont.Weight.Bold))
        self.page_title.setStyleSheet(f"color: {BrandColors.TEXT_PRIMARY}; border: none;")
        layout.addWidget(self.page_title)

        layout.addStretch()

        # Arama kutusu
        search_box = QLineEdit()
        search_box.setPlaceholderText("🔍 Ara...")
        search_box.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_NORMAL))
        search_box.setFixedWidth(300)
        search_box.setMinimumHeight(40)
        search_box.setStyleSheet(f"""
            QLineEdit {{
                background-color: {BrandColors.LIGHT_GRAY};
                border: 1px solid {BrandColors.BORDER_LIGHT};
                border-radius: {BrandSizes.RADIUS_LARGE}px;
                padding: 8px 15px;
                color: {BrandColors.TEXT_PRIMARY};
            }}
            QLineEdit:focus {{
                border: 2px solid {BrandColors.PRIMARY};
                background-color: {BrandColors.WHITE};
            }}
        """)
        layout.addWidget(search_box)

        # Bildirim butonu
        notif_btn = QPushButton("🔔")
        notif_btn.setFont(QFont(BrandFonts.FAMILY, 16))
        notif_btn.setFixedSize(40, 40)
        notif_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        notif_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {BrandColors.LIGHT_GRAY};
                border: none;
                border-radius: 20px;
                color: {BrandColors.TEXT_PRIMARY};
            }}
            QPushButton:hover {{
                background-color: {BrandColors.GRAY};
            }}
        """)
        layout.addWidget(notif_btn)

        # Kullanıcı bilgisi
        user_btn = QPushButton("👤 Admin")
        user_btn.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_NORMAL))
        user_btn.setMinimumHeight(40)
        user_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        user_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {BrandColors.PRIMARY};
                color: {BrandColors.TEXT_LIGHT};
                border: none;
                border-radius: {BrandSizes.RADIUS_LARGE}px;
                padding: 8px 20px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {BrandColors.PRIMARY_DARK};
            }}
        """)
        layout.addWidget(user_btn)

        # Çıkış butonu
        logout_btn = QPushButton("🚪")
        logout_btn.setFont(QFont(BrandFonts.FAMILY, 14))
        logout_btn.setFixedSize(40, 40)
        logout_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        logout_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {BrandColors.DANGER};
                color: {BrandColors.TEXT_LIGHT};
                border: none;
                border-radius: 20px;
            }}
            QPushButton:hover {{
                background-color: #c82333;
            }}
        """)
        logout_btn.clicked.connect(self.logout_clicked.emit)
        layout.addWidget(logout_btn)

    def set_page_title(self, title):
        """Sayfa başlığını değiştir"""
        self.page_title.setText(title)

