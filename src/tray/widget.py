import os
import sys

from PySide6 import QtWidgets
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QMenu, QApplication, QMainWindow
from loguru import logger


class TrayWidget(QtWidgets.QSystemTrayIcon):
    """Виджет треи"""

    def __init__(self, app: QApplication, main_window: QMainWindow, media_player):
        super().__init__()
        self.app: QApplication = app
        self.main_window: QMainWindow = main_window
        self.media_player = media_player
        self.quit_action: QAction = None
        self.open_action: QAction = None
        self.menu: QMenu = None
        self.icon: QIcon = None
        self.init_menu()
        self.init_tray()
        self.set_signals()

    @logger.catch
    def init_tray(self) -> None:
        """Инициализация треи"""
        self.icon = QIcon("static/images/tray/icon.png")
        self.setIcon(self.icon)
        self.setVisible(True)
        self.setContextMenu(self.menu)
        self.setToolTip("music app")

    @logger.catch
    def init_menu(self) -> None:
        """Инициализация меню треи"""
        self.menu = QMenu()
        self.open_action = QAction(self.tr("Open app"))
        self.quit_action = QAction(self.tr("Close app"))
        self.menu.addAction(self.open_action)
        self.menu.addAction(self.quit_action)

    @logger.catch
    def set_signals(self) -> None:
        """Установка сигналов"""
        self.activated.connect(self.open_app_by_double_click)
        self.quit_action.triggered.connect(self.close_app)
        self.open_action.triggered.connect(self.open_app_by_button)

    @logger.catch
    def open_app_by_double_click(self, reason) -> None:
        """Открыть приложение по двойному нажатию"""
        if reason == self.ActivationReason.DoubleClick:
            self.main_window.show()
            logger.info(f"app reopen by 2x click")

    @logger.catch
    def open_app_by_button(self) -> None:
        """Открыть приложение по кнопке"""
        self.main_window.show()
        logger.info(f"app reopen by button")

    @logger.catch
    def close_app(self) -> None:
        """Закрыть приложение"""
        try:
            self.media_player.stop()
            self.media_player.setSource("")
            os.remove("decoded.mp3")
        except Exception as exc:
            logger.info(f"close main exception: {exc}")
        logger.info(f"app closed")
        sys.exit(self.app.exec())
