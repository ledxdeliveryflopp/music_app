import httpx
from PySide6 import QtWidgets
from loguru import logger

from src.main.widget_ui import Ui_MainWindow
from src.settings.config import ini_settings
from src.settings.settings import settings


class MainWidget(QtWidgets.QWidget):
    """Класс главного виджета"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.check_authorization()

    @logger.catch
    def check_token_response(self, token: str) -> bool:
        """Запрос на эндопинт проверки токена"""
        try:
            response = httpx.post(f"{settings.api_settings.api_url}authorization/check_token/?token={token}")
            if response.status_code == 200:
                return True
        except Exception as e:
            logger.error(f"{self.check_token_response.__name__} error - {e}")
            return False

    @logger.catch
    def check_authorization(self) -> None:
        """Проверка авторизации"""
        token_in_config = ini_settings.check_auth_token_section()
        if token_in_config is True:
            token = ini_settings.get_auth_token_section()
            response = self.check_token_response(token)
            if response is True:
                pass
            else:
                self.open_authorization_widget()
        else:
            self.open_authorization_widget()

    @logger.catch
    def open_authorization_widget(self) -> None:
        """Открыть виджет авторизаии"""
        self.setEnabled(False)
        self.ui.authorization_widget.show()
