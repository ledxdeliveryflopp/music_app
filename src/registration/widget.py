import httpx
from PySide6 import QtWidgets
from loguru import logger

from src.registration.widget_ui import Ui_registration_widget
from src.settings.settings import settings


class RegistrationWidget(QtWidgets.QWidget):
    """Класс виджета регистрации"""

    def __init__(self, authorization_widget: QtWidgets):
        super().__init__()
        self.ui = Ui_registration_widget()
        self.ui.setupUi(self)
        self.authorization_widget = authorization_widget
        self.translate_ui()
        self.set_signals()

    @logger.catch
    def translate_ui(self) -> None:
        """Установка текста"""
        self.ui.send_button.setText(self.tr("Send"))

    @logger.catch
    def set_signals(self) -> None:
        """Установка сигналов"""
        self.ui.send_button.clicked.connect(self.register)

    @logger.catch
    def registration_request(self) -> bool | None:
        """Запрос на эндопинт регистрации"""
        data = {"username": f"{self.ui.username_input.text()}",
                "email": f"{self.ui.email_input.text()}",
                "password": f"{self.ui.password_input.text()}"}
        response = httpx.post(f"{settings.api_settings.api_url}registration/", json=data)
        response_json = response.json()
        if response.status_code == 200:
            return True
        else:
            logger.error(f"{self.registration_request.__name__} json error - {response_json}")
            self.ui.error_label.setText("registration error")

    @logger.catch
    def register(self) -> None:
        """Зарегестрироваться и войти"""
        registration = self.registration_request()
        if registration is True:
            self.close()
        else:
            logger.error(f"{self.register.__name__} error")

    @logger.catch
    def closeEvent(self, event):
        self.authorization_widget.setEnabled(True)
        self.close()
