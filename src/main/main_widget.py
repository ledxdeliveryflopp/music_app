import json
import os

from PySide6 import QtWidgets
from loguru import logger

from src.main.widget_ui import Ui_MainWindow


class MainWidget(QtWidgets.QWidget):
    """Класс главного виджета"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.check_authorization()

    @logger.catch
    def check_token_in_config(self) -> bool:
        path = os.path.exists("config/token.json")
        if path is True:
            with open(f"config/token.json", "r") as file:
                data = json.load(file)
                token = data.get("token")
            if token:
                logger.info(f"token inited")
                return True
            else:
                logger.info(f"token dont exist")
                return False
        else:
            return False

    @logger.catch
    def check_authorization(self) -> None:
        """Проверка авторизации"""
        token_in_config = self.check_token_in_config()
        if token_in_config is True:
            pass
        else:
            self.open_authorization_widget()

    @logger.catch
    def open_authorization_widget(self) -> None:
        """Открыть виджет авторизаии"""
        self.setEnabled(False)
        self.ui.authorization_widget.show()
