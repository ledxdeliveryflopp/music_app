# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QSizePolicy,
    QVBoxLayout, QWidget)

from src.music.widget import MusicWidget
from src.selection.widget import SelectionWidget
from src.side_bar.side_bar_widget import SideBarWidget


class MainWidgetUi(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1104, 791)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.music_play_layout = QVBoxLayout()
        self.music_play_layout.setObjectName(u"music_play_layout")
        self.music_widget = MusicWidget()
        self.music_widget.setObjectName(u"music_widget")

        self.music_play_layout.addWidget(self.music_widget)


        self.gridLayout_2.addLayout(self.music_play_layout, 2, 0, 1, 2)

        self.side_bar_layout = QHBoxLayout()
        self.side_bar_layout.setObjectName(u"side_bar_layout")
        self.side_bar_widget = SideBarWidget()
        self.side_bar_widget.setObjectName(u"side_bar_widget")

        self.side_bar_layout.addWidget(self.side_bar_widget)


        self.gridLayout_2.addLayout(self.side_bar_layout, 1, 0, 1, 1)

        self.selection_widget = SelectionWidget()
        self.selection_widget.setObjectName(u"selection_widget")
        self.main_window_layout = QVBoxLayout(self.selection_widget)
        self.main_window_layout.setObjectName(u"main_window_layout")
        # self.main_window_layout.setContentsMargins(800, -1, -1, 600)

        self.gridLayout_2.addWidget(self.selection_widget, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

