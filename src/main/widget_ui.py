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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLayout, QMainWindow,
    QMenuBar, QSizePolicy, QVBoxLayout, QWidget)

from src.music.widget import MusicWidget
from src.search.widget import SearchWidget
from src.side_bar.widget import SideBarWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(968, 465)
        MainWindow.setMaximumSize(QSize(1000, 492))
        # MainWindow.setMaximumSize(QSize(950, 148))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QSize(950, 148))
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.music_play_layout = QVBoxLayout()
        self.music_play_layout.setSpacing(6)
        self.music_play_layout.setObjectName(u"music_play_layout")
        self.music_play_layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.music_play_layout.setContentsMargins(-1, 0, -1, -1)
        self.music_play_widget = MusicWidget()
        self.music_play_widget.setObjectName(u"music_play_wdiget")

        self.music_play_layout.addWidget(self.music_play_widget)


        self.gridLayout.addLayout(self.music_play_layout, 1, 0, 1, 2)

        self.side_bar_layout = QVBoxLayout()
        self.side_bar_layout.setObjectName(u"side_bar_layout")
        self.side_bar_widget = SideBarWidget()
        self.side_bar_widget.setObjectName(u"side_bar_widget")

        self.side_bar_layout.addWidget(self.side_bar_widget)


        self.gridLayout.addLayout(self.side_bar_layout, 0, 0, 1, 1)
        self.dynamic_widget_layout = QVBoxLayout()
        self.dynamic_widget_layout.setObjectName(u"dynamic_widget_layout")
        self.search_widget = SearchWidget(self.music_play_widget)

        self.dynamic_widget_layout.addWidget(self.search_widget)


        self.gridLayout.addLayout(self.dynamic_widget_layout, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 968, 22))

        QMetaObject.connectSlotsByName(MainWindow)


