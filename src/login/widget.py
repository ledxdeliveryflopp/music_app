import httpx
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QMainWindow
from loguru import logger

from src.music.widget import MusicWidget
from src.registration.widget import RegistrationWidget
from src.settings.settings import settings


class LoginWidget(QtWidgets.QWidget):
    """Виджет логина"""

    def __init__(self, main_window: QMainWindow):
        super().__init__()

        self.main_window: QMainWindow = main_window
        self.layout = QtWidgets.QFormLayout(self)

        self.email_row = QtWidgets.QLineEdit()
        self.password_row = QtWidgets.QLineEdit()

        self.password_row.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.confirm_button = QtWidgets.QPushButton(self.tr("Send"))
        self.confirm_button.clicked.connect(self.login)

        self.register_button = QtWidgets.QPushButton(self.tr("Register"))
        self.register_button.clicked.connect(self.open_register_widget)

        # self.register_button = QtWidgets.QPushButton(self.tr("Next"))
        # self.register_button.clicked.connect(self.close)

        self.info_text = QtWidgets.QLabel(alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        self.layout.addRow(self.tr("email"), self.email_row)
        self.layout.addRow(self.tr("passowrd"), self.password_row)
        self.layout.addWidget(self.confirm_button)
        self.layout.addWidget(self.register_button)

        self.register_widget = RegistrationWidget()
        self.music_widget = MusicWidget()

        self.setLayout(self.layout)

    def login(self) -> None:
        """Логин"""
        data = {"email": f"{self.email_row.text()}",
                "password": f"{self.password_row.text()}"}
        logger.debug(f"login json - {data}")
        request = httpx.post(f"{settings.api_settings.api_url_login}/login/", json=data)
        logger.debug(f"request login data - {request.json()}")
        if request.status_code == 200:
            self.info_text.setText(self.tr("Success"))
            self.layout.removeRow(self.email_row)
            self.layout.removeRow(self.password_row)
            self.layout.addWidget(self.info_text)
            self.open_music_widget()
        else:
            logger.debug(f"login error - {request.json()}")

    def open_music_widget(self) -> None:
        """Открыть виджет проигрывателя"""
        self.main_window.setCentralWidget(self.music_widget)
        self.close()

    def open_register_widget(self) -> None:
        """Открыть виджет регистрации"""
        self.main_window.setCentralWidget(self.register_widget)
        self.close()

    def closeEvent(self, event) -> None:
        self.deleteLater()
        # self.widget.setCentralWidget(self.register)
