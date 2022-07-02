# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomezcyCYf.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLCDNumber, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

from View.ExtendedClasses import (bgImage, closeBtn, dayLabel, weatherView)
import Resources.resources

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(540, 960)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Home.sizePolicy().hasHeightForWidth())
        Home.setSizePolicy(sizePolicy)
        Home.setMinimumSize(QSize(540, 960))
        Home.setMaximumSize(QSize(540, 960))
        icon = QIcon()
        icon.addFile(u":/res/img/Logo1x1.png", QSize(), QIcon.Normal, QIcon.Off)
        Home.setWindowIcon(icon)
        Home.setWindowOpacity(0.995000000000000)
        self.centralwidget = QWidget(Home)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(490, 60, 31, 31))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 541, 41))
        self.TopBar = QHBoxLayout(self.horizontalLayoutWidget)
        self.TopBar.setSpacing(0)
        self.TopBar.setObjectName(u"TopBar")
        self.TopBar.setContentsMargins(12, 0, 12, 0)
        self.Logo = QLabel(self.horizontalLayoutWidget)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setMinimumSize(QSize(72, 36))
        self.Logo.setMaximumSize(QSize(72, 36))
        font = QFont()
        font.setFamilies([u"GLT-GonunneObsolete"])
        font.setPointSize(18)
        self.Logo.setFont(font)
        self.Logo.setAutoFillBackground(False)
        self.Logo.setStyleSheet(u"")
        self.Logo.setFrameShadow(QFrame.Plain)
        self.Logo.setScaledContents(True)
        self.Logo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.TopBar.addWidget(self.Logo, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.closeBtn = closeBtn(self.horizontalLayoutWidget)
        self.closeBtn.setObjectName(u"closeBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy1)
        self.closeBtn.setMinimumSize(QSize(24, 24))
        self.closeBtn.setMaximumSize(QSize(24, 24))
        font1 = QFont()
        font1.setPointSize(16)
        self.closeBtn.setFont(font1)
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeBtn.setTabletTracking(True)
        self.closeBtn.setStyleSheet(u"")
        self.closeBtn.setScaledContents(True)
        self.closeBtn.setAlignment(Qt.AlignCenter)

        self.TopBar.addWidget(self.closeBtn, 0, Qt.AlignRight)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 60, 371, 91))
        self.Time = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.Time.setObjectName(u"Time")
        self.Time.setContentsMargins(0, 0, 0, 0)
        self.nowTimeH = QLCDNumber(self.horizontalLayoutWidget_2)
        self.nowTimeH.setObjectName(u"nowTimeH")
        self.nowTimeH.setFrameShape(QFrame.Box)
        self.nowTimeH.setSmallDecimalPoint(False)
        self.nowTimeH.setDigitCount(2)
        self.nowTimeH.setMode(QLCDNumber.Dec)
        self.nowTimeH.setProperty("value", 12.000000000000000)

        self.Time.addWidget(self.nowTimeH)

        self.timeSep1 = QLabel(self.horizontalLayoutWidget_2)
        self.timeSep1.setObjectName(u"timeSep1")
        self.timeSep1.setMaximumSize(QSize(20, 16777215))
        font2 = QFont()
        font2.setPointSize(48)
        self.timeSep1.setFont(font2)
        self.timeSep1.setAlignment(Qt.AlignCenter)

        self.Time.addWidget(self.timeSep1)

        self.nowTimeM = QLCDNumber(self.horizontalLayoutWidget_2)
        self.nowTimeM.setObjectName(u"nowTimeM")
        self.nowTimeM.setFrameShape(QFrame.Box)
        self.nowTimeM.setSmallDecimalPoint(False)
        self.nowTimeM.setDigitCount(2)
        self.nowTimeM.setProperty("value", 12.000000000000000)

        self.Time.addWidget(self.nowTimeM)

        self.timeSep2 = QLabel(self.horizontalLayoutWidget_2)
        self.timeSep2.setObjectName(u"timeSep2")
        self.timeSep2.setMinimumSize(QSize(2, 0))
        self.timeSep2.setMaximumSize(QSize(20, 16777215))
        self.timeSep2.setFont(font2)
        self.timeSep2.setAlignment(Qt.AlignCenter)

        self.Time.addWidget(self.timeSep2)

        self.nowTimeS = QLCDNumber(self.horizontalLayoutWidget_2)
        self.nowTimeS.setObjectName(u"nowTimeS")
        self.nowTimeS.setFrameShape(QFrame.Box)
        self.nowTimeS.setSmallDecimalPoint(False)
        self.nowTimeS.setDigitCount(2)
        self.nowTimeS.setMode(QLCDNumber.Dec)
        self.nowTimeS.setProperty("value", 12.000000000000000)

        self.Time.addWidget(self.nowTimeS)

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 200, 501, 481))
        self.mainCalendar = QGridLayout(self.gridLayoutWidget)
        self.mainCalendar.setSpacing(0)
        self.mainCalendar.setObjectName(u"mainCalendar")
        self.mainCalendar.setContentsMargins(0, 0, 0, 0)
        self.c11 = dayLabel(self.gridLayoutWidget)
        self.c11.setObjectName(u"c11")
        self.c11.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c11, 1, 0, 1, 1)

        self.c33 = dayLabel(self.gridLayoutWidget)
        self.c33.setObjectName(u"c33")
        self.c33.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c33, 3, 2, 1, 1)

        self.c44 = dayLabel(self.gridLayoutWidget)
        self.c44.setObjectName(u"c44")
        self.c44.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c44, 4, 3, 1, 1)

        self.c13 = dayLabel(self.gridLayoutWidget)
        self.c13.setObjectName(u"c13")
        self.c13.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c13, 1, 2, 1, 1)

        self.c23 = dayLabel(self.gridLayoutWidget)
        self.c23.setObjectName(u"c23")
        self.c23.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c23, 2, 2, 1, 1)

        self.c24 = dayLabel(self.gridLayoutWidget)
        self.c24.setObjectName(u"c24")
        self.c24.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c24, 2, 3, 1, 1)

        self.c06 = QLabel(self.gridLayoutWidget)
        self.c06.setObjectName(u"c06")
        self.c06.setMaximumSize(QSize(16777215, 64))
        self.c06.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c06, 0, 5, 1, 1)

        self.c32 = dayLabel(self.gridLayoutWidget)
        self.c32.setObjectName(u"c32")
        self.c32.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c32, 3, 1, 1, 1)

        self.c35 = dayLabel(self.gridLayoutWidget)
        self.c35.setObjectName(u"c35")
        self.c35.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c35, 3, 4, 1, 1)

        self.c22 = dayLabel(self.gridLayoutWidget)
        self.c22.setObjectName(u"c22")
        self.c22.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c22, 2, 1, 1, 1)

        self.c42 = dayLabel(self.gridLayoutWidget)
        self.c42.setObjectName(u"c42")
        self.c42.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c42, 4, 1, 1, 1)

        self.c31 = dayLabel(self.gridLayoutWidget)
        self.c31.setObjectName(u"c31")
        self.c31.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c31, 3, 0, 1, 1)

        self.c52 = dayLabel(self.gridLayoutWidget)
        self.c52.setObjectName(u"c52")
        self.c52.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c52, 5, 1, 1, 1)

        self.c16 = dayLabel(self.gridLayoutWidget)
        self.c16.setObjectName(u"c16")
        self.c16.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c16, 1, 5, 1, 1)

        self.c26 = dayLabel(self.gridLayoutWidget)
        self.c26.setObjectName(u"c26")
        self.c26.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c26, 2, 5, 1, 1)

        self.c34 = dayLabel(self.gridLayoutWidget)
        self.c34.setObjectName(u"c34")
        self.c34.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c34, 3, 3, 1, 1)

        self.c21 = dayLabel(self.gridLayoutWidget)
        self.c21.setObjectName(u"c21")
        self.c21.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c21, 2, 0, 1, 1)

        self.c53 = dayLabel(self.gridLayoutWidget)
        self.c53.setObjectName(u"c53")
        self.c53.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c53, 5, 2, 1, 1)

        self.c43 = dayLabel(self.gridLayoutWidget)
        self.c43.setObjectName(u"c43")
        self.c43.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c43, 4, 2, 1, 1)

        self.c27 = dayLabel(self.gridLayoutWidget)
        self.c27.setObjectName(u"c27")
        self.c27.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c27, 2, 6, 1, 1)

        self.c57 = dayLabel(self.gridLayoutWidget)
        self.c57.setObjectName(u"c57")
        self.c57.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c57, 5, 6, 1, 1)

        self.c51 = dayLabel(self.gridLayoutWidget)
        self.c51.setObjectName(u"c51")
        self.c51.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c51, 5, 0, 1, 1)

        self.c54 = dayLabel(self.gridLayoutWidget)
        self.c54.setObjectName(u"c54")
        self.c54.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c54, 5, 3, 1, 1)

        self.c47 = dayLabel(self.gridLayoutWidget)
        self.c47.setObjectName(u"c47")
        self.c47.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c47, 4, 6, 1, 1)

        self.c02 = QLabel(self.gridLayoutWidget)
        self.c02.setObjectName(u"c02")
        self.c02.setMaximumSize(QSize(16777215, 64))
        self.c02.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c02, 0, 1, 1, 1)

        self.c37 = dayLabel(self.gridLayoutWidget)
        self.c37.setObjectName(u"c37")
        self.c37.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c37, 3, 6, 1, 1)

        self.c55 = dayLabel(self.gridLayoutWidget)
        self.c55.setObjectName(u"c55")
        self.c55.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c55, 5, 4, 1, 1)

        self.c45 = dayLabel(self.gridLayoutWidget)
        self.c45.setObjectName(u"c45")
        self.c45.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c45, 4, 4, 1, 1)

        self.c01 = QLabel(self.gridLayoutWidget)
        self.c01.setObjectName(u"c01")
        self.c01.setMaximumSize(QSize(16777215, 64))
        self.c01.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c01, 0, 0, 1, 1)

        self.c03 = QLabel(self.gridLayoutWidget)
        self.c03.setObjectName(u"c03")
        self.c03.setMaximumSize(QSize(16777215, 64))
        self.c03.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c03, 0, 2, 1, 1)

        self.c12 = dayLabel(self.gridLayoutWidget)
        self.c12.setObjectName(u"c12")
        self.c12.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c12, 1, 1, 1, 1)

        self.c25 = dayLabel(self.gridLayoutWidget)
        self.c25.setObjectName(u"c25")
        self.c25.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c25, 2, 4, 1, 1)

        self.c56 = dayLabel(self.gridLayoutWidget)
        self.c56.setObjectName(u"c56")
        self.c56.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c56, 5, 5, 1, 1)

        self.c14 = dayLabel(self.gridLayoutWidget)
        self.c14.setObjectName(u"c14")
        self.c14.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c14, 1, 3, 1, 1)

        self.c07 = QLabel(self.gridLayoutWidget)
        self.c07.setObjectName(u"c07")
        self.c07.setMaximumSize(QSize(16777215, 64))
        self.c07.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c07, 0, 6, 1, 1)

        self.c36 = dayLabel(self.gridLayoutWidget)
        self.c36.setObjectName(u"c36")
        self.c36.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c36, 3, 5, 1, 1)

        self.c04 = QLabel(self.gridLayoutWidget)
        self.c04.setObjectName(u"c04")
        self.c04.setMaximumSize(QSize(16777215, 64))
        self.c04.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c04, 0, 3, 1, 1)

        self.c41 = dayLabel(self.gridLayoutWidget)
        self.c41.setObjectName(u"c41")
        self.c41.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c41, 4, 0, 1, 1)

        self.c46 = dayLabel(self.gridLayoutWidget)
        self.c46.setObjectName(u"c46")
        self.c46.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c46, 4, 5, 1, 1)

        self.c15 = dayLabel(self.gridLayoutWidget)
        self.c15.setObjectName(u"c15")
        self.c15.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c15, 1, 4, 1, 1)

        self.c17 = dayLabel(self.gridLayoutWidget)
        self.c17.setObjectName(u"c17")
        self.c17.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c17, 1, 6, 1, 1)

        self.c05 = QLabel(self.gridLayoutWidget)
        self.c05.setObjectName(u"c05")
        self.c05.setMaximumSize(QSize(16777215, 64))
        self.c05.setAlignment(Qt.AlignCenter)

        self.mainCalendar.addWidget(self.c05, 0, 4, 1, 1)

        self.lastYear = QPushButton(self.centralwidget)
        self.lastYear.setObjectName(u"lastYear")
        self.lastYear.setGeometry(QRect(20, 170, 51, 24))
        self.lastMonth = QPushButton(self.centralwidget)
        self.lastMonth.setObjectName(u"lastMonth")
        self.lastMonth.setGeometry(QRect(80, 170, 31, 24))
        self.nextMonth = QPushButton(self.centralwidget)
        self.nextMonth.setObjectName(u"nextMonth")
        self.nextMonth.setGeometry(QRect(430, 170, 31, 24))
        self.nextYear = QPushButton(self.centralwidget)
        self.nextYear.setObjectName(u"nextYear")
        self.nextYear.setGeometry(QRect(470, 170, 51, 24))
        self.Reminders = QListWidget(self.centralwidget)
        self.Reminders.setObjectName(u"Reminders")
        self.Reminders.setGeometry(QRect(20, 690, 321, 221))
        self.addReminder = QPushButton(self.centralwidget)
        self.addReminder.setObjectName(u"addReminder")
        self.addReminder.setGeometry(QRect(20, 920, 321, 24))
        self.weather = weatherView(self.centralwidget)
        self.weather.setObjectName(u"weather")
        self.weather.setGeometry(QRect(350, 690, 181, 251))
        self.weather.setMaximumSize(QSize(181, 251))
        self.weather.setContextMenuPolicy(Qt.NoContextMenu)
        self.weather.setUrl(QUrl(u"qrc:/res/web/weather.html"))
        self.weather.setZoomFactor(0.850000000000000)
        self.todayDate = QLabel(self.centralwidget)
        self.todayDate.setObjectName(u"todayDate")
        self.todayDate.setGeometry(QRect(400, 110, 121, 41))
        self.backToday = QPushButton(self.centralwidget)
        self.backToday.setObjectName(u"backToday")
        self.backToday.setGeometry(QRect(220, 170, 111, 24))
        self.calYear = QLabel(self.centralwidget)
        self.calYear.setObjectName(u"calYear")
        self.calYear.setGeometry(QRect(120, 170, 91, 21))
        self.calYear.setAlignment(Qt.AlignCenter)
        self.calMonth = QLabel(self.centralwidget)
        self.calMonth.setObjectName(u"calMonth")
        self.calMonth.setGeometry(QRect(340, 170, 81, 21))
        self.calMonth.setAlignment(Qt.AlignCenter)
        self.bgImg = bgImage(self.centralwidget)
        self.bgImg.setObjectName(u"bgImg")
        self.bgImg.setGeometry(QRect(0, 40, 541, 921))
        self.bgImg.setPixmap(QPixmap(u":/res/img/bg.png"))
        self.bgImg.setScaledContents(True)
        Home.setCentralWidget(self.centralwidget)
        self.bgImg.raise_()
        self.pushButton.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.gridLayoutWidget.raise_()
        self.lastYear.raise_()
        self.lastMonth.raise_()
        self.nextMonth.raise_()
        self.nextYear.raise_()
        self.Reminders.raise_()
        self.addReminder.raise_()
        self.weather.raise_()
        self.todayDate.raise_()
        self.backToday.raise_()
        self.calYear.raise_()
        self.calMonth.raise_()

        self.retranslateUi(Home)
        self.pushButton.clicked.connect(Home.toAbout)
        self.addReminder.clicked.connect(Home.toAddReminder)
        self.backToday.clicked.connect(Home.backToToday)
        self.nextMonth.clicked.connect(Home.nextMonth)
        self.nextYear.clicked.connect(Home.nextYear)
        self.lastMonth.clicked.connect(Home.lastMonth)
        self.lastYear.clicked.connect(Home.lastYear)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"\u6708\u6642\u8a08 ~Lunar Dial~", None))
        self.pushButton.setText(QCoreApplication.translate("Home", u"i", None))
        self.Logo.setText(QCoreApplication.translate("Home", u"\u6708\u6642\u8a08", None))
        self.closeBtn.setText(QCoreApplication.translate("Home", u"\u00d7", None))
        self.timeSep1.setText(QCoreApplication.translate("Home", u":", None))
        self.timeSep2.setText(QCoreApplication.translate("Home", u":", None))
        self.c11.setText(QCoreApplication.translate("Home", u"00", None))
        self.c33.setText(QCoreApplication.translate("Home", u"14", None))
        self.c44.setText(QCoreApplication.translate("Home", u"22", None))
        self.c13.setText(QCoreApplication.translate("Home", u"00", None))
        self.c23.setText(QCoreApplication.translate("Home", u"7", None))
        self.c24.setText(QCoreApplication.translate("Home", u"8", None))
        self.c06.setText(QCoreApplication.translate("Home", u"\u5468\u516d\n"
"\u571f\u66dc\u65e5", None))
        self.c32.setText(QCoreApplication.translate("Home", u"13", None))
        self.c35.setText(QCoreApplication.translate("Home", u"16", None))
        self.c22.setText(QCoreApplication.translate("Home", u"6", None))
        self.c42.setText(QCoreApplication.translate("Home", u"20", None))
        self.c31.setText(QCoreApplication.translate("Home", u"12", None))
        self.c52.setText(QCoreApplication.translate("Home", u"27", None))
        self.c16.setText(QCoreApplication.translate("Home", u"3", None))
        self.c26.setText(QCoreApplication.translate("Home", u"10", None))
        self.c34.setText(QCoreApplication.translate("Home", u"15", None))
        self.c21.setText(QCoreApplication.translate("Home", u"5", None))
        self.c53.setText(QCoreApplication.translate("Home", u"28", None))
        self.c43.setText(QCoreApplication.translate("Home", u"21", None))
        self.c27.setText(QCoreApplication.translate("Home", u"11", None))
        self.c57.setText(QCoreApplication.translate("Home", u"00", None))
        self.c51.setText(QCoreApplication.translate("Home", u"26", None))
        self.c54.setText(QCoreApplication.translate("Home", u"29", None))
        self.c47.setText(QCoreApplication.translate("Home", u"25", None))
        self.c02.setText(QCoreApplication.translate("Home", u"\u5468\u4e8c\n"
"\u706b\u66dc\u65e5", None))
        self.c37.setText(QCoreApplication.translate("Home", u"18", None))
        self.c55.setText(QCoreApplication.translate("Home", u"30", None))
        self.c45.setText(QCoreApplication.translate("Home", u"23", None))
        self.c01.setText(QCoreApplication.translate("Home", u"\u5468\u4e00\n"
"\u6708\u66dc\u65e5", None))
        self.c03.setText(QCoreApplication.translate("Home", u"\u5468\u4e09\n"
"\u6c34\u66dc\u65e5", None))
        self.c12.setText(QCoreApplication.translate("Home", u"00", None))
        self.c25.setText(QCoreApplication.translate("Home", u"9", None))
        self.c56.setText(QCoreApplication.translate("Home", u"00", None))
        self.c14.setText(QCoreApplication.translate("Home", u"1", None))
        self.c07.setText(QCoreApplication.translate("Home", u"\u5468\u65e5\n"
"\u65e5\u66dc\u65e5", None))
        self.c36.setText(QCoreApplication.translate("Home", u"17", None))
        self.c04.setText(QCoreApplication.translate("Home", u"\u5468\u56db\n"
"\u6728\u66dc\u65e5", None))
        self.c41.setText(QCoreApplication.translate("Home", u"19", None))
        self.c46.setText(QCoreApplication.translate("Home", u"24", None))
        self.c15.setText(QCoreApplication.translate("Home", u"2", None))
        self.c17.setText(QCoreApplication.translate("Home", u"4", None))
        self.c05.setText(QCoreApplication.translate("Home", u"\u5468\u4e94\n"
"\u91d1\u66dc\u65e5", None))
        self.lastYear.setText(QCoreApplication.translate("Home", u"<<", None))
        self.lastMonth.setText(QCoreApplication.translate("Home", u"<", None))
        self.nextMonth.setText(QCoreApplication.translate("Home", u">", None))
        self.nextYear.setText(QCoreApplication.translate("Home", u">>", None))
        self.addReminder.setText(QCoreApplication.translate("Home", u"+", None))
        self.todayDate.setText(QCoreApplication.translate("Home", u"TextLabel", None))
        self.backToday.setText(QCoreApplication.translate("Home", u"\u56de\u5230\u4eca\u65e5", None))
        self.calYear.setText(QCoreApplication.translate("Home", u"TextLabel", None))
        self.calMonth.setText(QCoreApplication.translate("Home", u"TextLabel", None))
    # retranslateUi

