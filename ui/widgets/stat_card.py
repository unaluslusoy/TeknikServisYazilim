# -*- coding: utf-8 -*-
"""
Stat Card - Istatistik Karti Widget (Emoji yok, duzeltilmis)
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from ui.styles.brand import BrandColors, BrandFonts, BrandSizes


class StatCard(QFrame):
    """Istatistik karti widget"""

    def __init__(self, title, value, icon_char="*", color=None, parent=None):
        super().__init__(parent)
        self.title = title
        self.value = value
        self.icon_char = icon_char
        self.color = color or BrandColors.PRIMARY
        self.init_ui()

    def init_ui(self):
        """UI bilesenleri"""
        self.setMinimumHeight(140)
        self.setStyleSheet(f"""
            QFrame {{
                background-color: {BrandColors.BG_CARD};
                border-radius: {BrandSizes.RADIUS_LARGE}px;
                border: 1px solid {BrandColors.BORDER_LIGHT};
            }}
        """)

        # Ana layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 18, 20, 18)
        main_layout.setSpacing(12)
        self.setLayout(main_layout)

        # Üst kisim - Ikon ve trend
        top_layout = QHBoxLayout()
        top_layout.setSpacing(0)

        # Ikon container
        icon_container = QFrame()
        icon_container.setFixedSize(48, 48)
        icon_container.setStyleSheet(f"""
            QFrame {{
                background-color: {self.color};
                border-radius: 24px;
            }}
        """)
        icon_layout = QVBoxLayout()
        icon_layout.setContentsMargins(0, 0, 0, 0)
        icon_container.setLayout(icon_layout)

        icon_label = QLabel(self.icon_char)
        icon_label.setFont(QFont(BrandFonts.FAMILY, 18, QFont.Weight.Bold))
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_label.setStyleSheet("color: white; background: transparent;")
        icon_layout.addWidget(icon_label)

        top_layout.addWidget(icon_container)
        top_layout.addStretch()

        # Trend
        trend_frame = QFrame()
        trend_frame.setStyleSheet(f"""
            QFrame {{
                background-color: rgba(40, 167, 69, 0.1);
                border-radius: 12px;
                padding: 4px 8px;
            }}
        """)
        trend_layout = QHBoxLayout()
        trend_layout.setContentsMargins(8, 4, 8, 4)
        trend_frame.setLayout(trend_layout)

        trend_label = QLabel("+12%")
        trend_label.setFont(QFont(BrandFonts.FAMILY, 10, QFont.Weight.Bold))
        trend_label.setStyleSheet(f"color: {BrandColors.SECONDARY}; background: transparent;")
        trend_layout.addWidget(trend_label)

        top_layout.addWidget(trend_frame)
        main_layout.addLayout(top_layout)

        # Deger
        self.value_label = QLabel(str(self.value))
        self.value_label.setFont(QFont(BrandFonts.FAMILY, 28, QFont.Weight.Bold))
        self.value_label.setStyleSheet(f"color: {BrandColors.TEXT_PRIMARY}; background: transparent;")
        main_layout.addWidget(self.value_label)

        # Baslik
        title_label = QLabel(self.title)
        title_label.setFont(QFont(BrandFonts.FAMILY, 11))
        title_label.setStyleSheet(f"color: {BrandColors.TEXT_SECONDARY}; background: transparent;")
        main_layout.addWidget(title_label)

    def set_value(self, value):
        """Degeri guncelle"""
        self.value = value
        self.value_label.setText(str(value))

