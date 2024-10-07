# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'upload_music.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_upload_music_widget(object):
    def setupUi(self, upload_music_widget):
        if not upload_music_widget.objectName():
            upload_music_widget.setObjectName(u"upload_music_widget")
        upload_music_widget.resize(581, 563)
        self.gridLayout_2 = QGridLayout(upload_music_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_author_button = QPushButton(upload_music_widget)
        self.add_author_button.setObjectName(u"add_author_button")

        self.verticalLayout.addWidget(self.add_author_button)

        self.author_input = QLineEdit(upload_music_widget)
        self.author_input.setObjectName(u"author_input")

        self.verticalLayout.addWidget(self.author_input)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.line_2 = QFrame(upload_music_widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.upload_music_file_button = QPushButton(upload_music_widget)
        self.upload_music_file_button.setObjectName(u"upload_music_file_button")

        self.verticalLayout.addWidget(self.upload_music_file_button)

        self.music_file_label = QLabel(upload_music_widget)
        self.music_file_label.setObjectName(u"music_file_label")
        self.music_file_label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.music_file_label)

        self.line = QFrame(upload_music_widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.upload_cover_file_button = QPushButton(upload_music_widget)
        self.upload_cover_file_button.setObjectName(u"upload_cover_file_button")

        self.verticalLayout.addWidget(self.upload_cover_file_button)

        self.cover_file_label = QLabel(upload_music_widget)
        self.cover_file_label.setObjectName(u"cover_file_label")
        self.cover_file_label.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.cover_file_label)


        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)

        self.pushButton = QPushButton(upload_music_widget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        QMetaObject.connectSlotsByName(upload_music_widget)
    # setupUi