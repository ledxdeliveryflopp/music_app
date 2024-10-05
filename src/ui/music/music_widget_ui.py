# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'music.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)

class MusicWidgetUi(object):
    def setupUi(self, music_play_widget):
        if not music_play_widget.objectName():
            music_play_widget.setObjectName(u"music_play_widget")
        music_play_widget.resize(690, 373)
        self.gridLayout_2 = QGridLayout(music_play_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.main_layout = QGridLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.time_play_layout = QVBoxLayout()
        self.time_play_layout.setObjectName(u"time_play_layout")
        self.valume_play_layout = QHBoxLayout()
        self.valume_play_layout.setObjectName(u"valume_play_layout")
        self.empty_layout = QVBoxLayout()
        self.empty_layout.setObjectName(u"empty_layout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.empty_layout.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(170, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.empty_layout.addLayout(self.horizontalLayout_4)


        self.valume_play_layout.addLayout(self.empty_layout)

        self.play_button_layout = QVBoxLayout()
        self.play_button_layout.setObjectName(u"play_button_layout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.play_button_layout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(60, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.play_button = QPushButton(music_play_widget)
        self.stop_button = QPushButton(music_play_widget)
        self.resume_button = QPushButton(music_play_widget)
        self.play_button.setObjectName(u"play_button")

        self.horizontalLayout_5.addWidget(self.play_button)
        self.horizontalLayout_5.addWidget(self.stop_button)
        self.horizontalLayout_5.addWidget(self.resume_button)

        self.horizontalSpacer_8 = QSpacerItem(60, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.play_button_layout.addLayout(self.horizontalLayout_5)


        self.valume_play_layout.addLayout(self.play_button_layout)

        self.valume_layout = QVBoxLayout()
        self.valume_layout.setObjectName(u"valume_layout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.valume_layout.addItem(self.verticalSpacer_3)

        self.valume_slider_layout = QHBoxLayout()
        self.valume_slider_layout.setObjectName(u"valume_slider_layout")
        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.valume_slider_layout.addItem(self.horizontalSpacer_2)

        self.valume_slider = QSlider(music_play_widget)
        self.valume_slider.setObjectName(u"valume_slider")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valume_slider.sizePolicy().hasHeightForWidth())
        self.valume_slider.setSizePolicy(sizePolicy)
        self.valume_slider.setOrientation(Qt.Orientation.Horizontal)

        self.valume_slider_layout.addWidget(self.valume_slider)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.valume_slider_layout.addItem(self.horizontalSpacer_5)


        self.valume_layout.addLayout(self.valume_slider_layout)


        self.valume_play_layout.addLayout(self.valume_layout)


        self.time_play_layout.addLayout(self.valume_play_layout)

        self.valume_time_layout_spacer_top = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.time_play_layout.addItem(self.valume_time_layout_spacer_top)

        self.time_duration_layout = QHBoxLayout()
        self.time_duration_layout.setObjectName(u"time_duration_layout")
        self.image_label = QLabel(music_play_widget)
        self.image_label.setObjectName(u"image_label")

        self.time_duration_layout.addWidget(self.image_label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.music_title = QLabel(music_play_widget)
        self.music_title.setObjectName(u"music_title")

        self.verticalLayout.addWidget(self.music_title)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.music_authors = QLabel(music_play_widget)
        self.music_authors.setObjectName(u"music_authors")

        self.verticalLayout.addWidget(self.music_authors)


        self.time_duration_layout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.time_duration_layout.addItem(self.horizontalSpacer)

        self.current_music_time = QLabel(music_play_widget)
        self.current_music_time.setObjectName(u"current_music_time")

        self.time_duration_layout.addWidget(self.current_music_time)

        self.current_music_time_spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.time_duration_layout.addItem(self.current_music_time_spacer)

        self.time_slider = QSlider(music_play_widget)
        self.time_slider.setObjectName(u"time_slider")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.time_slider.sizePolicy().hasHeightForWidth())
        self.time_slider.setSizePolicy(sizePolicy1)
        self.time_slider.setOrientation(Qt.Orientation.Horizontal)

        self.time_duration_layout.addWidget(self.time_slider)

        self.music_duration_spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.time_duration_layout.addItem(self.music_duration_spacer)

        self.music_duration = QLabel(music_play_widget)
        self.music_duration.setObjectName(u"music_duration")

        self.time_duration_layout.addWidget(self.music_duration)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.time_duration_layout.addItem(self.horizontalSpacer_3)


        self.time_play_layout.addLayout(self.time_duration_layout)

        self.time_layout_spacer_buttom = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.time_play_layout.addItem(self.time_layout_spacer_buttom)


        self.main_layout.addLayout(self.time_play_layout, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.main_layout, 1, 0, 1, 1)


        self.retranslateUi(music_play_widget)

        QMetaObject.connectSlotsByName(music_play_widget)
    # setupUi

    def retranslateUi(self, music_play_widget):
        music_play_widget.setWindowTitle(QCoreApplication.translate("music_play_widget", u"Form", None))
        self.play_button.setText(QCoreApplication.translate("music_play_widget", u"PushButton", None))
        self.image_label.setText(QCoreApplication.translate("music_play_widget", u"TextLabel", None))
        self.music_title.setText(QCoreApplication.translate("music_play_widget", u"TextLabel", None))
        self.music_authors.setText(QCoreApplication.translate("music_play_widget", u"TextLabel", None))
        self.current_music_time.setText(QCoreApplication.translate("music_play_widget", u"TextLabel", None))
        self.music_duration.setText(QCoreApplication.translate("music_play_widget", u"TextLabel", None))
    # retranslateUi

