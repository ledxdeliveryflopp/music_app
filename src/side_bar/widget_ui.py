# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'side_bar.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class UiSideBarWidget(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(180, 551)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(205)
        sizePolicy.setVerticalStretch(55)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.layout = QVBoxLayout()
        self.layout.setObjectName(u"layout")
        self.search_button = QPushButton(Form)
        self.search_button.setObjectName(u"search_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.search_button.sizePolicy().hasHeightForWidth())
        self.search_button.setSizePolicy(sizePolicy1)

        self.layout.addWidget(self.search_button)


        self.verticalLayout_2.addLayout(self.layout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.main_window_button = QPushButton(Form)
        self.main_window_button.setObjectName(u"main_window_button")
        sizePolicy1.setHeightForWidth(self.main_window_button.sizePolicy().hasHeightForWidth())
        self.main_window_button.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.main_window_button)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stream_button = QPushButton(Form)
        self.stream_button.setObjectName(u"stream_button")
        sizePolicy1.setHeightForWidth(self.stream_button.sizePolicy().hasHeightForWidth())
        self.stream_button.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.stream_button)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.playlist_button = QPushButton(Form)
        self.playlist_button.setObjectName(u"playlist_button")
        sizePolicy1.setHeightForWidth(self.playlist_button.sizePolicy().hasHeightForWidth())
        self.playlist_button.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.playlist_button)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.username_label = QLabel(Form)
        self.username_label.setObjectName(u"username_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.username_label.sizePolicy().hasHeightForWidth())
        self.username_label.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.username_label)


        self.verticalLayout_2.addLayout(self.verticalLayout_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.search_button.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.main_window_button.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.stream_button.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.playlist_button.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.username_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

