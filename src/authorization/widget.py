import json
import sys

import httpx
from PySide6 import QtWidgets
from loguru import logger

from src.authorization.widget_ui import Ui_authorization_widget


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

    @logger.catch
    def set_signals(self) -> None:
        """Установка сигналов"""
        self.ui.send_button.clicked.connect(self.authorization_request)

    @logger.catch
    def set_input_settings(self) -> None:
        """Установка настроек для полей ввода"""
        self.ui.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    @logger.catch
    def create_token_in_config(self, token: str) -> None:
        """Создание токена в конфиге"""
        try:
            with open(f"config/token.json", "w") as file:
                data = {"token": token}
                json_data = json.dumps(data)
                file.write(json_data)
            logger.info(f"token written")
        except Exception as exception:
            logger.error(f"{self.create_token_in_config.__name__} error - {exception}")

    @logger.catch
    def authorization_request(self) -> None:
        """Запрос на эндопинт авторизации"""
        data = {"email": f"{self.ui.email_input.text()}",
                "password": f"{self.ui.password_input.text()}"}
        response = httpx.post("http://127.0.0.1:7000/authorization/login/", json=data)
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
    def closeEvent(self, event):
        if self.status is True:
            self.main_widget.setEnabled(True)
            self.close()
        else:
            sys.exit()
