# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DaysEPBIk.ui'
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
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

from View.ExtendedClasses import closeBtn
import Resources.resources

class Ui_Day(object):
    def setupUi(self, Day):
        if not Day.objectName():
            Day.setObjectName(u"Day")
        Day.resize(480, 640)
        icon = QIcon()
        icon.addFile(u":/res/img/Logo1x1.png", QSize(), QIcon.Normal, QIcon.Off)
        Day.setWindowIcon(icon)
        Day.setWindowOpacity(0.996000000000000)
        self.Reminders = QListWidget(Day)
        self.Reminders.setObjectName(u"Reminders")
        self.Reminders.setGeometry(QRect(20, 160, 441, 411))
        self.horizontalLayoutWidget_2 = QWidget(Day)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 0, 481, 41))
        self.TopBar = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.TopBar.setSpacing(0)
        self.TopBar.setObjectName(u"TopBar")
        self.TopBar.setContentsMargins(12, 0, 12, 0)
        self.dayTitle = QLabel(self.horizontalLayoutWidget_2)
        self.dayTitle.setObjectName(u"dayTitle")
        self.dayTitle.setMinimumSize(QSize(72, 36))
        self.dayTitle.setMaximumSize(QSize(255, 36))
        self.dayTitle.setTabletTracking(False)
        self.dayTitle.setAutoFillBackground(False)
        self.dayTitle.setStyleSheet(u"")
        self.dayTitle.setFrameShadow(QFrame.Plain)
        self.dayTitle.setScaledContents(True)
        self.dayTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.TopBar.addWidget(self.dayTitle, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.closeBtn = closeBtn(self.horizontalLayoutWidget_2)
        self.closeBtn.setObjectName(u"closeBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy)
        self.closeBtn.setMinimumSize(QSize(24, 24))
        self.closeBtn.setMaximumSize(QSize(24, 24))
        font = QFont()
        font.setPointSize(16)
        self.closeBtn.setFont(font)
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeBtn.setTabletTracking(True)
        self.closeBtn.setStyleSheet(u"")
        self.closeBtn.setScaledContents(True)
        self.closeBtn.setAlignment(Qt.AlignCenter)

        self.TopBar.addWidget(self.closeBtn, 0, Qt.AlignRight)

        self.addReminder = QPushButton(Day)
        self.addReminder.setObjectName(u"addReminder")
        self.addReminder.setGeometry(QRect(20, 590, 441, 24))
        self.yearLabel = QLabel(Day)
        self.yearLabel.setObjectName(u"yearLabel")
        self.yearLabel.setGeometry(QRect(20, 50, 161, 21))
        self.yearLabel.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.dayLabel = QLabel(Day)
        self.dayLabel.setObjectName(u"dayLabel")
        self.dayLabel.setGeometry(QRect(20, 75, 271, 71))
        self.otherInfo = QLabel(Day)
        self.otherInfo.setObjectName(u"otherInfo")
        self.otherInfo.setGeometry(QRect(300, 50, 151, 101))
        self.otherInfo.setWordWrap(True)

        self.retranslateUi(Day)
        self.addReminder.clicked.connect(Day.addReminder)

        QMetaObject.connectSlotsByName(Day)
    # setupUi

    def retranslateUi(self, Day):
        self.dayTitle.setText(QCoreApplication.translate("Day", u"{Day}", None))
        self.closeBtn.setText(QCoreApplication.translate("Day", u"\u00d7", None))
        self.addReminder.setText(QCoreApplication.translate("Day", u"+", None))
        self.yearLabel.setText(QCoreApplication.translate("Day", u"TextLabel", None))
        self.dayLabel.setText(QCoreApplication.translate("Day", u"TextLabel", None))
        self.otherInfo.setText(QCoreApplication.translate("Day", u"TextLabel", None))
        pass
    # retranslateUi

