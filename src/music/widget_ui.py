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

class Ui_Music_widget(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(950, 148)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(950, 148))
        Form.setMaximumSize(QSize(950, 148))
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.slider_layout = QVBoxLayout()
        self.slider_layout.setObjectName(u"slider_layout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.play_button = QPushButton(Form)
        self.stop_button = QPushButton(Form)
        self.resume_button = QPushButton(Form)
        self.play_button.setObjectName(u"play_button")

        self.verticalLayout.addWidget(self.play_button)
        self.verticalLayout.addWidget(self.stop_button)
        self.verticalLayout.addWidget(self.resume_button)


        self.slider_layout.addLayout(self.verticalLayout)

        self.music_duration_slider = QSlider(Form)
        self.music_duration_slider.setObjectName(u"music_duration_slider")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.music_duration_slider.sizePolicy().hasHeightForWidth())
        self.music_duration_slider.setSizePolicy(sizePolicy1)
        self.music_duration_slider.setOrientation(Qt.Orientation.Horizontal)

        self.slider_layout.addWidget(self.music_duration_slider)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.slider_layout.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.slider_layout, 0, 2, 1, 1)

        self.text_current_duration_layout = QVBoxLayout()
        self.text_current_duration_layout.setObjectName(u"text_current_duration_layout")
        self.loop_button = QPushButton(Form)
        self.loop_button.setObjectName(u"loop_button")

        self.text_current_duration_layout.addWidget(self.loop_button)

        self.current_duration = QLabel(Form)
        self.current_duration.setObjectName(u"current_duration")

        self.text_current_duration_layout.addWidget(self.current_duration)


        self.gridLayout.addLayout(self.text_current_duration_layout, 0, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.volume_slider_layout = QVBoxLayout()
        self.volume_slider_layout.setObjectName(u"volume_slider_layout")
        self.valume_slider = QSlider(Form)
        self.valume_slider.setObjectName(u"valume_slider")
        sizePolicy.setHeightForWidth(self.valume_slider.sizePolicy().hasHeightForWidth())
        self.valume_slider.setSizePolicy(sizePolicy)
        self.valume_slider.setOrientation(Qt.Orientation.Horizontal)

        self.volume_slider_layout.addWidget(self.valume_slider)


        self.verticalLayout_3.addLayout(self.volume_slider_layout)

        self.duration_layout = QHBoxLayout()
        self.duration_layout.setObjectName(u"duration_layout")
        self.music_duration = QLabel(Form)
        self.music_duration.setObjectName(u"music_duration")

        self.duration_layout.addWidget(self.music_duration)


        self.verticalLayout_3.addLayout(self.duration_layout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 3, 1, 1)

        self.music_data_layout = QGridLayout()
        self.music_data_layout.setObjectName(u"music_data_layout")
        self.music_title = QLabel(Form)
        self.music_title.setObjectName(u"music_title")

        self.music_data_layout.addWidget(self.music_title, 0, 1, 1, 1)

        self.authors_label = QLabel(Form)
        self.authors_label.setObjectName(u"authors_label")

        self.music_data_layout.addWidget(self.authors_label, 1, 1, 1, 1)

        self.music_cover = QLabel(Form)
        self.music_cover.setObjectName(u"music_cover")
        self.music_cover.setMaximumSize(QSize(50, 50))

        self.music_data_layout.addWidget(self.music_cover, 0, 0, 2, 1)


        self.gridLayout.addLayout(self.music_data_layout, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.play_button.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.loop_button.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.current_duration.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.music_duration.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.music_title.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.authors_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.music_cover.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

