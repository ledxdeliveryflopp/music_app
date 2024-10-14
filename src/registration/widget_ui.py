# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registration.ui'
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

class Ui_registration_widget(object):
    def setupUi(self, registration_widget):
        if not registration_widget.objectName():
            registration_widget.setObjectName(u"registration_widget")
        registration_widget.resize(504, 359)
        registration_widget.setMinimumSize(QSize(0, 0))
        self.formLayout_2 = QFormLayout(registration_widget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.username_input = QLineEdit(registration_widget)
        self.username_input.setObjectName(u"username_input")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.username_input)

        self.email_input = QLineEdit(registration_widget)
        self.email_input.setObjectName(u"email_input")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.email_input)

        self.password_input = QLineEdit(registration_widget)
        self.password_input.setObjectName(u"password_input")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.password_input)

        self.send_button = QPushButton(registration_widget)
        self.send_button.setObjectName(u"send_button")

        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_button.sizePolicy().hasHeightForWidth())
        self.send_button.setSizePolicy(sizePolicy)
        self.send_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.send_button)

        self.error_label = QLabel(registration_widget)
        self.error_label.setObjectName(u"error_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.error_label.sizePolicy().hasHeightForWidth())
        self.error_label.setSizePolicy(sizePolicy1)
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.error_label)


        self.retranslateUi(registration_widget)

        QMetaObject.connectSlotsByName(registration_widget)
    # setupUi

    def retranslateUi(self, registration_widget):
        registration_widget.setWindowTitle(QCoreApplication.translate("registration_widget", u"Form", None))
        self.send_button.setText(QCoreApplication.translate("registration_widget", u"PushButton", None))
        self.error_label.setText(QCoreApplication.translate("registration_widget", u"TextLabel", None))
    # retranslateUi

