# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutSnZKhe.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)

from View.ExtendedClasses import closeBtn
import Resources.resources

class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.resize(480, 320)
        About.setMinimumSize(QSize(480, 320))
        About.setMaximumSize(QSize(480, 320))
        icon = QIcon()
        icon.addFile(u":/res/img/Logo1x1.png", QSize(), QIcon.Normal, QIcon.Off)
        About.setWindowIcon(icon)
        About.setWindowOpacity(0.950000000000000)
        self.horizontalLayoutWidget = QWidget(About)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 40, 481, 100))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(180, 96))
        self.label.setPixmap(QPixmap(u":/res/img/Logo_dark.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.line = QFrame(About)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-10, 144, 501, 21))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.App = QLabel(About)
        self.App.setObjectName(u"App")
        self.App.setGeometry(QRect(60, 170, 51, 21))
        self.App2 = QLabel(About)
        self.App2.setObjectName(u"App2")
        self.App2.setGeometry(QRect(140, 170, 281, 21))
        font = QFont()
        font.setFamilies([u"\u534e\u6587\u6977\u4f53"])
        font.setPointSize(12)
        self.App2.setFont(font)
        self.Lib2 = QLabel(About)
        self.Lib2.setObjectName(u"Lib2")
        self.Lib2.setGeometry(QRect(140, 200, 281, 41))
        self.Lib2.setFont(font)
        self.Lib = QLabel(About)
        self.Lib.setObjectName(u"Lib")
        self.Lib.setGeometry(QRect(60, 200, 61, 21))
        self.Cr = QLabel(About)
        self.Cr.setObjectName(u"Cr")
        self.Cr.setGeometry(QRect(10, 300, 461, 16))
        self.Cr.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget_2 = QWidget(About)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 0, 481, 41))
        self.TopBar = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.TopBar.setSpacing(0)
        self.TopBar.setObjectName(u"TopBar")
        self.TopBar.setContentsMargins(12, 0, 0, 0)
        self.Logo = QLabel(self.horizontalLayoutWidget_2)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setMinimumSize(QSize(72, 36))
        self.Logo.setMaximumSize(QSize(72, 36))
        font1 = QFont()
        font1.setFamilies([u"GLT-GonunneObsolete"])
        font1.setPointSize(18)
        self.Logo.setFont(font1)
        self.Logo.setTabletTracking(False)
        self.Logo.setAutoFillBackground(False)
        self.Logo.setStyleSheet(u"")
        self.Logo.setFrameShadow(QFrame.Plain)
        self.Logo.setScaledContents(True)
        self.Logo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.TopBar.addWidget(self.Logo, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.closeBtn = closeBtn(self.horizontalLayoutWidget_2)
        self.closeBtn.setObjectName(u"closeBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy1)
        self.closeBtn.setMinimumSize(QSize(24, 24))
        self.closeBtn.setMaximumSize(QSize(24, 24))
        font2 = QFont()
        font2.setPointSize(16)
        self.closeBtn.setFont(font2)
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeBtn.setTabletTracking(True)
        self.closeBtn.setStyleSheet(u"")
        self.closeBtn.setScaledContents(True)
        self.closeBtn.setAlignment(Qt.AlignCenter)

        self.TopBar.addWidget(self.closeBtn, 0, Qt.AlignRight)

        self.Cr_2 = QLabel(About)
        self.Cr_2.setObjectName(u"Cr_2")
        self.Cr_2.setGeometry(QRect(10, 250, 461, 31))
        self.Cr_2.setAlignment(Qt.AlignCenter)
        self.Cr_2.setOpenExternalLinks(True)

        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"\u5173\u4e8e", None))
        self.label.setText("")
        self.App.setText(QCoreApplication.translate("About", u"App", None))
        self.App2.setText(QCoreApplication.translate("About", u"\u6708\u6642\u8a08 ~Lunar Dial~ \u65e5\u5386 (Beta)", None))
        self.Lib2.setText(QCoreApplication.translate("About", u"PySide 6, PySqlite 3, Qt-Material, \n"
"Lunar-Pyhton, Time, PyInstaller", None))
        self.Lib.setText(QCoreApplication.translate("About", u"Libraries", None))
        self.Cr.setText(QCoreApplication.translate("About", u"\u00a92022 KohakuCao All Rights Reserved (For BUAA ComThinking Course)", None))
        self.Logo.setText(QCoreApplication.translate("About", u"\u6708\u6642\u8a08", None))
        self.closeBtn.setText(QCoreApplication.translate("About", u"\u00d7", None))
        self.Cr_2.setText(QCoreApplication.translate("About", u"\u80cc\u666f\u56fe\u81ea<a href=\"https://www.pixiv.net/artworks/72443860\">https://www.pixiv.net/artworks/72443860</a><br />\n"
"\u8f6f\u4ef6\u540d\u201c\u6708\u6642\u8a08\u201d\u6e90\u81ea\u4e1c\u65b9Project\uff0c\u5176\u8457\u4f5c\u6743\u5f52ZUN\u4e0e\u4e0a\u6d77\u30a2\u30ea\u30b9\u5e7b\u6a02\u56e3\u6240\u6709", None))
    # retranslateUi

