# -*- coding: utf-8 -*-
"""
Marka Kimliği ve Tema Ayarları
"""

class BrandColors:
    """Marka renk paleti"""

    # Ana Renkler
    PRIMARY = "#2B579A"          # Koyu Mavi (Ana marka rengi)
    PRIMARY_LIGHT = "#4A90D9"    # Açık Mavi
    PRIMARY_DARK = "#1e3f6f"     # Çok Koyu Mavi

    # İkincil Renkler
    SECONDARY = "#28A745"        # Yeşil (Başarı)
    WARNING = "#F57C00"          # Turuncu (Uyarı)
    DANGER = "#DC3545"           # Kırmızı (Hata)
    INFO = "#2196F3"             # Açık Mavi (Bilgi)

    # Nötr Renkler
    WHITE = "#FFFFFF"
    LIGHT_GRAY = "#F8F9FA"
    GRAY = "#E9ECEF"
    DARK_GRAY = "#6C757D"
    BLACK = "#212529"

    # Arka Plan Renkleri
    BG_MAIN = "#F5F7FA"
    BG_SIDEBAR = "#1E2832"       # Koyu sidebar
    BG_CARD = "#FFFFFF"

    # Metin Renkleri
    TEXT_PRIMARY = "#212529"
    TEXT_SECONDARY = "#6C757D"
    TEXT_LIGHT = "#FFFFFF"

    # Border Renkleri
    BORDER_LIGHT = "#DEE2E6"
    BORDER_MEDIUM = "#CED4DA"


class BrandFonts:
    """Marka font ayarları"""

    FAMILY = "Segoe UI"
    FAMILY_MONO = "Consolas"

    # Font Boyutları
    SIZE_SMALL = 9
    SIZE_NORMAL = 11
    SIZE_MEDIUM = 13
    SIZE_LARGE = 16
    SIZE_XLARGE = 20
    SIZE_TITLE = 24


class BrandSizes:
    """Marka boyut ayarları"""

    # Spacing
    PADDING_SMALL = 8
    PADDING_MEDIUM = 15
    PADDING_LARGE = 20

    # Border Radius
    RADIUS_SMALL = 4
    RADIUS_MEDIUM = 8
    RADIUS_LARGE = 12

    # Sidebar
    SIDEBAR_WIDTH = 250
    SIDEBAR_COLLAPSED_WIDTH = 60

    # Header
    HEADER_HEIGHT = 60

    # Button
    BUTTON_HEIGHT_SMALL = 32
    BUTTON_HEIGHT_MEDIUM = 40
    BUTTON_HEIGHT_LARGE = 48


# Global Stylesheet
GLOBAL_STYLE = f"""
    * {{
        font-family: {BrandFonts.FAMILY};
    }}
    
    QMainWindow {{
        background-color: {BrandColors.BG_MAIN};
    }}
    
    QWidget {{
        color: {BrandColors.TEXT_PRIMARY};
    }}
    
    /* Scrollbar */
    QScrollBar:vertical {{
        border: none;
        background: {BrandColors.LIGHT_GRAY};
        width: 10px;
        border-radius: 5px;
    }}
    
    QScrollBar::handle:vertical {{
        background: {BrandColors.DARK_GRAY};
        border-radius: 5px;
        min-height: 20px;
    }}
    
    QScrollBar::handle:vertical:hover {{
        background: {BrandColors.PRIMARY};
    }}
    
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
        height: 0px;
    }}
"""

