# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search.ui'
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
from PySide6.QtWidgets import (QApplication, QListView, QSizePolicy, QTextEdit,
                               QVBoxLayout, QWidget, QLineEdit)

class Ui_Search_widget(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(601, 222)
        Form.setMinimumSize(QSize(601, 222))
        Form.setMaximumSize(QSize(601, 222))
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.search_input = QLineEdit(Form)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_input.sizePolicy().hasHeightForWidth())
        # self.textEdit.setSizePolicy(sizePolicy)
        # self.textEdit.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout.addWidget(self.search_input)

        self.listView = QListView(Form)
        self.listView.setObjectName(u"listView")

        self.verticalLayout.addWidget(self.listView)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        QMetaObject.connectSlotsByName(Form)


