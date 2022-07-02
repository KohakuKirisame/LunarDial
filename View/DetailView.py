# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DetailTukklv.ui'
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
    QPushButton, QSizePolicy, QWidget)

from View.ExtendedClasses import closeBtn
import Resources.resources

class Ui_Detail(object):
    def setupUi(self, Detail):
        if not Detail.objectName():
            Detail.setObjectName(u"Detail")
        Detail.resize(480, 320)
        Detail.setMinimumSize(QSize(480, 320))
        Detail.setMaximumSize(QSize(480, 320))
        icon = QIcon()
        icon.addFile(u":/res/img/Logo1x1.png", QSize(), QIcon.Normal, QIcon.Off)
        Detail.setWindowIcon(icon)
        Detail.setWindowOpacity(0.992000000000000)
        self.horizontalLayoutWidget_2 = QWidget(Detail)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 0, 481, 41))
        self.TopBar = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.TopBar.setSpacing(0)
        self.TopBar.setObjectName(u"TopBar")
        self.TopBar.setContentsMargins(12, 0, 12, 0)
        self.reminderDetail = QLabel(self.horizontalLayoutWidget_2)
        self.reminderDetail.setObjectName(u"reminderDetail")
        self.reminderDetail.setMinimumSize(QSize(72, 36))
        self.reminderDetail.setMaximumSize(QSize(255, 36))
        self.reminderDetail.setTabletTracking(False)
        self.reminderDetail.setAutoFillBackground(False)
        self.reminderDetail.setStyleSheet(u"")
        self.reminderDetail.setFrameShadow(QFrame.Plain)
        self.reminderDetail.setScaledContents(True)
        self.reminderDetail.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.TopBar.addWidget(self.reminderDetail, 0, Qt.AlignLeft|Qt.AlignVCenter)

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

        self.pushButton = QPushButton(Detail)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 280, 461, 24))
        self.Time = QLabel(Detail)
        self.Time.setObjectName(u"Time")
        self.Time.setGeometry(QRect(20, 80, 51, 21))
        self.Title = QLabel(Detail)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(20, 50, 51, 21))
        self.Title2 = QLabel(Detail)
        self.Title2.setObjectName(u"Title2")
        self.Title2.setGeometry(QRect(90, 50, 281, 21))
        self.Time2 = QLabel(Detail)
        self.Time2.setObjectName(u"Time2")
        self.Time2.setGeometry(QRect(90, 80, 281, 21))
        self.Content = QLabel(Detail)
        self.Content.setObjectName(u"Content")
        self.Content.setGeometry(QRect(20, 140, 51, 21))
        self.Remind2 = QLabel(Detail)
        self.Remind2.setObjectName(u"Remind2")
        self.Remind2.setGeometry(QRect(90, 110, 281, 21))
        self.Content2 = QLabel(Detail)
        self.Content2.setObjectName(u"Content2")
        self.Content2.setGeometry(QRect(90, 140, 281, 111))
        self.Content2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.Reimind = QLabel(Detail)
        self.Reimind.setObjectName(u"Reimind")
        self.Reimind.setGeometry(QRect(20, 110, 61, 21))

        self.retranslateUi(Detail)
        self.pushButton.clicked.connect(Detail.closeDetail)

        QMetaObject.connectSlotsByName(Detail)
    # setupUi

    def retranslateUi(self, Detail):
        self.reminderDetail.setText(QCoreApplication.translate("Detail", u"{reminderTitle}", None))
        self.closeBtn.setText(QCoreApplication.translate("Detail", u"\u00d7", None))
        self.pushButton.setText(QCoreApplication.translate("Detail", u"\u5173\u95ed", None))
        self.Time.setText(QCoreApplication.translate("Detail", u"\u65f6\u95f4", None))
        self.Title.setText(QCoreApplication.translate("Detail", u"\u6807\u9898", None))
        self.Title2.setText(QCoreApplication.translate("Detail", u"{title}", None))
        self.Time2.setText(QCoreApplication.translate("Detail", u"{time}", None))
        self.Content.setText(QCoreApplication.translate("Detail", u"\u5185\u5bb9", None))
        self.Remind2.setText(QCoreApplication.translate("Detail", u"{remindtime}", None))
        self.Content2.setText(QCoreApplication.translate("Detail", u"{content}", None))
        self.Reimind.setText(QCoreApplication.translate("Detail", u"\u63d0\u9192\u65f6\u95f4", None))
        pass
    # retranslateUi

