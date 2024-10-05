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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QListView,
    QSizePolicy, QVBoxLayout, QWidget)

class SearchWidgetUi(object):
    def setupUi(self, search_widget):
        if not search_widget.objectName():
            search_widget.setObjectName(u"search_widget")
        search_widget.resize(685, 492)
        self.gridLayout_2 = QGridLayout(search_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listView = QListView(search_widget)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_2.addWidget(self.listView)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.search_input = QLineEdit(search_widget)
        self.search_input.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.search_input, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(search_widget)

        QMetaObject.connectSlotsByName(search_widget)
    # setupUi

    def retranslateUi(self, search_widget):
        search_widget.setWindowTitle(QCoreApplication.translate("search_widget", u"Form", None))
    # retranslateUi

