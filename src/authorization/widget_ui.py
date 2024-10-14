# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'authorization.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

from src.registration.widget import RegistrationWidget


class Ui_authorization_widget(object):
    def setupUi(self, authorization_widget):
        if not authorization_widget.objectName():
            authorization_widget.setObjectName(u"authorization_widget")
        authorization_widget.resize(506, 359)
        self.registration_widget = RegistrationWidget(authorization_widget=authorization_widget)
        self.formLayout_2 = QFormLayout(authorization_widget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.password_input = QLineEdit(authorization_widget)
        self.password_input.setObjectName(u"password_input")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.password_input)

        self.email_input = QLineEdit(authorization_widget)
        self.email_input.setObjectName(u"email_input")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.email_input)

        self.error_label = QLabel(authorization_widget)
        self.error_label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_label.sizePolicy().hasHeightForWidth())
        self.error_label.setSizePolicy(sizePolicy)
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.error_label)

        self.send_button = QPushButton(authorization_widget)
        self.send_button.setObjectName(u"send_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.send_button.sizePolicy().hasHeightForWidth())
        self.send_button.setSizePolicy(sizePolicy1)
        self.send_button.setBaseSize(QSize(0, 0))
        self.send_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.send_button.setAutoDefault(False)
        self.send_button.setFlat(False)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.send_button)

        self.registration_button = QPushButton(authorization_widget)
        self.registration_button.setObjectName(u"registration_button")
        sizePolicy1.setHeightForWidth(self.registration_button.sizePolicy().hasHeightForWidth())
        self.registration_button.setSizePolicy(sizePolicy1)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.registration_button)


        self.send_button.setDefault(False)


        QMetaObject.connectSlotsByName(authorization_widget)
    # setupUi



