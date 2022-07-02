# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditoErSvf.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QWidget)

from View.ExtendedClasses import closeBtn
import Resources.resources

class Ui_Edit(object):
    def setupUi(self, Edit):
        if not Edit.objectName():
            Edit.setObjectName(u"Edit")
        Edit.resize(480, 320)
        Edit.setMinimumSize(QSize(480, 320))
        Edit.setMaximumSize(QSize(480, 320))
        icon = QIcon()
        icon.addFile(u":/res/img/Logo1x1.png", QSize(), QIcon.Normal, QIcon.Off)
        Edit.setWindowIcon(icon)
        self.horizontalLayoutWidget_2 = QWidget(Edit)
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

        self.Title = QLabel(Edit)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(20, 50, 61, 21))
        self.Time = QLabel(Edit)
        self.Time.setObjectName(u"Time")
        self.Time.setGeometry(QRect(20, 80, 61, 21))
        self.saveBtn = QPushButton(Edit)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setGeometry(QRect(260, 280, 211, 24))
        self.Content = QLabel(Edit)
        self.Content.setObjectName(u"Content")
        self.Content.setGeometry(QRect(20, 140, 61, 21))
        self.Reimind = QLabel(Edit)
        self.Reimind.setObjectName(u"Reimind")
        self.Reimind.setGeometry(QRect(20, 110, 71, 21))
        self.cancelBtn = QPushButton(Edit)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setGeometry(QRect(40, 280, 211, 24))
        self.delBtn = QPushButton(Edit)
        self.delBtn.setObjectName(u"delBtn")
        self.delBtn.setGeometry(QRect(10, 280, 24, 24))
        self.titleEdit = QLineEdit(Edit)
        self.titleEdit.setObjectName(u"titleEdit")
        self.titleEdit.setGeometry(QRect(90, 50, 341, 20))
        self.titleEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.titleEdit.setMaxLength(127)
        self.timeEdit = QDateTimeEdit(Edit)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(90, 80, 251, 22))
        self.timeEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.timeEdit.setMaximumDateTime(QDateTime(QDate(2199, 12, 31), QTime(23, 59, 59)))
        self.timeEdit.setMinimumDateTime(QDateTime(QDate(1970, 1, 1), QTime(8, 0, 0)))
        self.timeEdit.setCalendarPopup(True)
        self.remindEdit = QDateTimeEdit(Edit)
        self.remindEdit.setObjectName(u"remindEdit")
        self.remindEdit.setGeometry(QRect(90, 110, 251, 22))
        self.remindEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.remindEdit.setMaximumDateTime(QDateTime(QDate(2199, 12, 31), QTime(23, 59, 59)))
        self.remindEdit.setMinimumDateTime(QDateTime(QDate(1970, 1, 1), QTime(8, 0, 0)))
        self.remindEdit.setCalendarPopup(True)
        self.contentEdit = QPlainTextEdit(Edit)
        self.contentEdit.setObjectName(u"contentEdit")
        self.contentEdit.setGeometry(QRect(90, 140, 341, 111))
        self.contentEdit.setContextMenuPolicy(Qt.NoContextMenu)

        self.retranslateUi(Edit)
        self.cancelBtn.clicked.connect(Edit.close)
        self.saveBtn.clicked.connect(Edit.saveReminder)
        self.delBtn.clicked.connect(Edit.delReminder)

        QMetaObject.connectSlotsByName(Edit)
    # setupUi

    def retranslateUi(self, Edit):
        Edit.setWindowTitle(QCoreApplication.translate("Edit", u"Form", None))
        self.reminderDetail.setText(QCoreApplication.translate("Edit", u"{reminderTitle}", None))
        self.closeBtn.setText(QCoreApplication.translate("Edit", u"\u00d7", None))
        self.Title.setText(QCoreApplication.translate("Edit", u"\u6807\u9898", None))
        self.Time.setText(QCoreApplication.translate("Edit", u"\u65f6\u95f4", None))
        self.saveBtn.setText(QCoreApplication.translate("Edit", u"\u4fdd\u5b58", None))
        self.Content.setText(QCoreApplication.translate("Edit", u"\u5185\u5bb9", None))
        self.Reimind.setText(QCoreApplication.translate("Edit", u"\u63d0\u9192\u65f6\u95f4", None))
        self.cancelBtn.setText(QCoreApplication.translate("Edit", u"\u53d6\u6d88", None))
        self.delBtn.setText(QCoreApplication.translate("Edit", u"\u00d7", None))
        self.titleEdit.setPlaceholderText(QCoreApplication.translate("Edit", u"\u4e0d\u8d85\u8fc740\u5b57", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("Edit", u"yyyy-MM-dd HH:mm:ss", None))
        self.remindEdit.setDisplayFormat(QCoreApplication.translate("Edit", u"yyyy-MM-dd HH:mm:ss", None))
        self.contentEdit.setPlaceholderText(QCoreApplication.translate("Edit", u"\u4e0d\u8d85\u8fc7200\u5b57", None))
    # retranslateUi

