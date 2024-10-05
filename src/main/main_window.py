import os

from PySide6 import QtWidgets
from loguru import logger

from src.main.main_widget import MainWidget


class MainWindow(QtWidgets.QMainWindow):
    """Основное окно"""

    def __init__(self):
        super().__init__()
        self.main_widget = MainWidget()
        self.window().resize(1104, 791)
        self.setCentralWidget(self.main_widget)

    def closeEvent(self, event):
        try:
            self.main_widget.ui.music_widget.media_player.setSource("")
            os.remove("decoded.mp3")
            os.remove("encoded.mp3")
        except Exception as exc:
            logger.info(f"close main exception: {exc}")
