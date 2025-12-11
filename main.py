"""
Teknik Servis Yönetim Sistemi
Ana Uygulama Başlatıcı

Versiyon: 1.0.0
Tarih: 11 Aralık 2024
"""

import sys
import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer
from ui.dialogs.splash_screen import SplashScreen
from ui.dialogs.login_dialog import LoginDialog
from ui.main_window import MainWindow


def main():
    """Ana uygulama fonksiyonu"""
    app = QApplication(sys.argv)

    # Uygulama bilgileri
    app.setApplicationName("Teknik Servis Yönetim Sistemi")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("Teknik Servis")

    # Splash screen göster
    splash = SplashScreen()
    splash.show()
    app.processEvents()

    # Ana pencereyi oluştur (arka planda)
    main_window = MainWindow()

    # Splash screen'i 2.5 saniye sonra kapat
    def close_splash():
        splash.close()
        # Login dialog göster
        login_dialog = LoginDialog()
        if login_dialog.exec():
            # Giriş başarılı, ana pencereyi göster
            main_window.show()
        else:
            # Giriş iptal edildi, uygulamayı kapat
            app.quit()

    QTimer.singleShot(2500, close_splash)

    # Uygulama döngüsünü başlat
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

