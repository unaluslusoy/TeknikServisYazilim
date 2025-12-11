# -*- coding: utf-8 -*-
"""
Stat Card - İstatistik Kartı Widget
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from ui.styles.brand import BrandColors, BrandFonts, BrandSizes


class StatCard(QWidget):
    """İstatistik kartı widget"""

    def __init__(self, title, value, icon="📊", color=None, parent=None):
        super().__init__(parent)
        self.title = title
        self.value = value
        self.icon = icon
        self.color = color or BrandColors.PRIMARY
        self.init_ui()

    def init_ui(self):
        """UI bileşenlerini başlat"""
        self.setMinimumHeight(120)
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {BrandColors.BG_CARD};
                border-radius: {BrandSizes.RADIUS_LARGE}px;
                border: 1px solid {BrandColors.BORDER_LIGHT};
            }}
            QWidget:hover {{
                border: 2px solid {self.color};
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }}
        """)

        # Ana layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 15, 20, 15)
        main_layout.setSpacing(10)
        self.setLayout(main_layout)

        # Üst kısım - İkon ve başlık
        top_layout = QHBoxLayout()

        # İkon
        icon_label = QLabel(self.icon)
        icon_label.setFont(QFont(BrandFonts.FAMILY, 28))
        icon_label.setFixedSize(50, 50)
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_label.setStyleSheet(f"""
            QLabel {{
                background-color: {self.color};
                border-radius: 25px;
                color: white;
            }}
        """)
        top_layout.addWidget(icon_label)

        top_layout.addStretch()

        # Trend göstergesi (opsiyonel)
        trend_label = QLabel("↗ +12%")
        trend_label.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_SMALL))
        trend_label.setStyleSheet(f"color: {BrandColors.SECONDARY}; background: transparent;")
        top_layout.addWidget(trend_label)

        main_layout.addLayout(top_layout)

        # Değer
        self.value_label = QLabel(str(self.value))
        self.value_label.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_TITLE, QFont.Weight.Bold))
        self.value_label.setStyleSheet(f"color: {BrandColors.TEXT_PRIMARY}; background: transparent;")
        main_layout.addWidget(self.value_label)

        # Başlık
        title_label = QLabel(self.title)
        title_label.setFont(QFont(BrandFonts.FAMILY, BrandFonts.SIZE_NORMAL))
        title_label.setStyleSheet(f"color: {BrandColors.TEXT_SECONDARY}; background: transparent;")
        main_layout.addWidget(title_label)

    def set_value(self, value):
        """Değeri güncelle"""
        self.value = value
        self.value_label.setText(str(value))

