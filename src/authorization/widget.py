import sys
from datetime import datetime

import httpx
from PySide6 import QtWidgets
from loguru import logger

from src.authorization.widget_ui import Ui_authorization_widget
from src.settings.config import ini_settings
from src.settings.settings import settings


class AuthorizationWidget(QtWidgets.QWidget):
    """Виджет авторизации"""

    def __init__(self, main_widget: QtWidgets.QWidget) -> None:
        super().__init__()
        self.main_widget = main_widget
        self.ui = Ui_authorization_widget()
        self.ui.setupUi(self)
        self.translate_ui()
        self.set_signals()
        self.set_input_settings()
        self.status: bool = None

    @logger.catch
    def translate_ui(self) -> None:
        """Установка текста"""
        self.ui.error_label.setText("")
        self.ui.send_button.setText(self.tr("send"))
        self.ui.registration_button.setText(self.tr("Register"))

    @logger.catch
    def set_signals(self) -> None:
        """Установка сигналов"""
        self.ui.send_button.clicked.connect(self.authorization_request)
        self.ui.registration_button.clicked.connect(self.open_registration_widget)

    @logger.catch
    def set_input_settings(self) -> None:
        """Установка настроек для полей ввода"""
        self.ui.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    @logger.catch
    def create_token_in_config(self, token: str, expire: datetime) -> None:
        """Создание токена в конфиге"""
        try:
            ini_settings.change_auth_section(token, expire)
        except Exception as exception:
            logger.error(f"{self.create_token_in_config.__name__} error - {exception}")

    @logger.catch
    def authorization_request(self) -> None:
        """Запрос на эндопинт авторизации"""
        data = {"email": f"{self.ui.email_input.text()}",
                "password": f"{self.ui.password_input.text()}"}
        response = httpx.post(f"{settings.api_settings.api_url}authorization/login/", json=data)
        response_json = response.json()
        if response.status_code == 200:
            token = response_json.get("token")
            self.status = True
            self.create_token_in_config(token)
            self.close()
        else:
            logger.error(f"{self.authorization_request.__name__} json error - {response_json}")
            self.ui.error_label.setText("error")

    @logger.catch
    def open_registration_widget(self) -> None:
        self.setEnabled(False)
        self.ui.registration_widget.show()

    @logger.catch
    def closeEvent(self, event):
        if self.status is True:
            self.main_widget.setEnabled(True)
            self.close()
        else:
            sys.exit()
