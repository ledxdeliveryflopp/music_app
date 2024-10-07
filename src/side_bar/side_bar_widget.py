import httpx
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget
from loguru import logger

from src.side_bar.widget_ui import UiSideBarWidget
from src.upload.widget import UploadMusicWidget


class SideBarWidget(QtWidgets.QWidget):
    """Виджет бокового меню"""

    def __init__(self):
        super().__init__()
        self.ui = UiSideBarWidget()
        self.ui.setupUi(self)
        self.upload_widget: QWidget = UploadMusicWidget()
        self.translate_ui()
        self.set_signals()

    @logger.catch
    def translate_ui(self) -> None:
        """Установка текста на кнопки и тд"""
        self.ui.search_button.setText(self.tr("search"))
        self.ui.upload_music_button.setText(self.tr("upload music"))
        self.ui.playlist_button.setText(self.tr("playlists"))
        self.ui.main_window_button.setText(self.tr("main"))

    @logger.catch
    def set_signals(self) -> None:
        """Установка сигналов"""
        self.ui.upload_music_button.clicked.connect(self.open_upload_music_widget)

    @logger.catch
    def open_upload_music_widget(self) -> None:
        """Открытие виджета загрузки музыки"""
        print("test")
        self.upload_widget.show()
