import httpx
from PySide6 import QtWidgets, QtCore
from loguru import logger

from src.settings.settings import settings


class RegistrationWidget(QtWidgets.QWidget):
    """Виджет регистрации"""

    def __init__(self) -> None:
        super().__init__()
        self.layout = QtWidgets.QFormLayout(self)
        self.username_input = QtWidgets.QLineEdit()
        self.email_input = QtWidgets.QLineEdit()
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.send_button = QtWidgets.QPushButton(self.tr("Send"))
        self.info = QtWidgets.QLabel(alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        self.send_button.clicked.connect(self.register)

        self.layout.addRow(self.tr("Username"), self.username_input)
        self.layout.addRow(self.tr("Email"), self.email_input)
        self.layout.addRow(self.tr("Password"), self.password_input)
        self.layout.addWidget(self.send_button)
        self.setLayout(self.layout)

    def register(self) -> None:
        """Регистрация"""
        data = {"username": f"{self.username_input.text()}",
                "email": f"{self.email_input.text()}",
                "password": f"{self.password_input.text()}"}
        logger.debug(f"json data - {data}")
        request = httpx.post(f"{settings.api_settings.api_url_registration}/", json=data)
        logger.debug(f"request data - {request.json()}")
        request_data = request.json()
        if request.status_code == 200:
            self.info.setText("Success")
            self.layout.addWidget(self.info)
        else:
            try:
                error_from_json = f"{request_data.get('detail')[0].get('msg')} in {request_data.get('detail')[0].get('loc')[1]}"
                self.info.setText(f"Error - {error_from_json}")
                self.layout.addWidget(self.info)
            except AttributeError:
                error_from_json = request_data
                self.info.setText(f"Error - {error_from_json}")
                self.layout.addWidget(self.info)

