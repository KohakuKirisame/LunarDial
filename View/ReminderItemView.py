# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReminderItemAIpicY.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ReminderItem(object):
    def setupUi(self, ReminderItem):
        if not ReminderItem.objectName():
            ReminderItem.setObjectName(u"ReminderItem")
        ReminderItem.resize(320, 64)
        ReminderItem.setMinimumSize(QSize(310, 64))
        ReminderItem.setMaximumSize(QSize(430, 64))
        self.horizontalLayout = QHBoxLayout(ReminderItem)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 2, 8, 2)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(ReminderItem)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setMinimumSize(QSize(0, 32))
        self.titleLabel.setMaximumSize(QSize(16777215, 24))

        self.verticalLayout.addWidget(self.titleLabel)

        self.timeLabel = QLabel(ReminderItem)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setMinimumSize(QSize(0, 18))
        self.timeLabel.setMaximumSize(QSize(16777215, 18))

        self.verticalLayout.addWidget(self.timeLabel)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.editBtn = QPushButton(ReminderItem)
        self.editBtn.setObjectName(u"editBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editBtn.sizePolicy().hasHeightForWidth())
        self.editBtn.setSizePolicy(sizePolicy)
        self.editBtn.setMinimumSize(QSize(64, 32))
        self.editBtn.setMaximumSize(QSize(72, 32))

        self.horizontalLayout.addWidget(self.editBtn)


        self.retranslateUi(ReminderItem)
        self.editBtn.clicked.connect(ReminderItem.toEdit)

        QMetaObject.connectSlotsByName(ReminderItem)
    # setupUi

    def retranslateUi(self, ReminderItem):
        self.titleLabel.setText(QCoreApplication.translate("ReminderItem", u"{title}", None))
        self.timeLabel.setText(QCoreApplication.translate("ReminderItem", u"{tile}", None))
        self.editBtn.setText(QCoreApplication.translate("ReminderItem", u"\u7f16\u8f91", None))
        pass
    # retranslateUi

