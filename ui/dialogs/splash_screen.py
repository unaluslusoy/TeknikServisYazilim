# -*- coding: utf-8 -*-
"""
Splash Screen - Ilk Acilis Ekrani
"""

from PyQt6.QtWidgets import QSplashScreen
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import os


class SplashScreen(QSplashScreen):
    """Ilk acilis splash ekrani"""

    def __init__(self):
        # Logoyu yukle
        logo_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                "resources", "images", "logo.jpeg")

        if os.path.exists(logo_path):
            pixmap = QPixmap(logo_path)
            pixmap = pixmap.scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio,
                                  Qt.TransformationMode.SmoothTransformation)
        else:
            # Logo yoksa bos pixmap
            pixmap = QPixmap(400, 400)
            pixmap.fill(Qt.GlobalColor.white)

        super().__init__(pixmap, Qt.WindowType.WindowStaysOnTopHint)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Mesajlari goster
        self.show_message("Teknik Servis Yonetim Sistemi")

    def show_message(self, message):
        """Mesaj goster"""
        self.showMessage(
            message,
            Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter,
            Qt.GlobalColor.white
        )

