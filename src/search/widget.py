from functools import partial

import httpx
import requests
from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import QModelIndex, QSize
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QAbstractItemView
from loguru import logger

from src.search.widget_ui import Ui_Search_widget
from src.settings.thread_manager import ThreadManager


class SearchWidget(QtWidgets.QWidget, ThreadManager):
    """Виджет поиска музыки"""

    def __init__(self, music_widget):
        super().__init__()
        self.model = None
        self.music_widget = music_widget
        self.ui = Ui_Search_widget()
        self.ui.setupUi(self)
        self.init_item_model()
        self.set_signals()

    @logger.catch
    def init_item_model(self) -> None:
        """Инициализация  модели для списка"""
        self.model = QtGui.QStandardItemModel()
        self.ui.listView.setIconSize(QSize(50, 50))
        self.ui.listView.setModel(self.model)

    @logger.catch
    def set_signals(self) -> None:
        """Установка сигналов"""
        self.ui.search_input.textChanged.connect(self.set_music_list_in_thread)
        self.ui.listView.setSpacing(5)
        self.ui.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.listView.pressed.connect(self.play_music_in_music_widget)

    @logger.catch
    def play_music_in_music_widget(self, index: QModelIndex) -> None:
        music_data = self.ui.listView.model().itemFromIndex(index)
        music_id = music_data.data()
        self.music_widget.play_music(music_id)

    @logger.catch
    def set_music_list_in_thread(self, query: str) -> None:
        """Запуск функции добавления музыки в список в отдельном потоке"""
        self.thread_manager.start(partial(self.set_music_to_list, query))

    @logger.catch
    def search_music(self, query: str) -> list | None:
        """Поиск музыки по автору и названию"""
        if len(self.ui.search_input.text()) < 4:
            return None
        try:
            request = httpx.get(f"http://127.0.0.1:7000/music/find_music/?author_username="
                                f"{query}&music_title={query}")
            request_data = request.json()
            return request_data
        except Exception as exception:
            logger.error(f"search_music error - {exception}")
            return None

    @logger.catch
    def set_cover_to_music_in_list(self, cover_url: str) -> QIcon:
        """Установить обложки для мызыки в списке"""
        cover_data = requests.get(cover_url)
        pixmap = QPixmap()
        pixmap.loadFromData(cover_data.content)
        icon = QtGui.QIcon(pixmap)
        return icon

    @logger.catch
    def set_music_to_list(self, query) -> None:
        """Добавить музыку в список"""
        data = self.search_music(query)
        row_count = self.model.rowCount()
        logger.info(f"row count - {row_count}")
        self.model.removeRows(0, row_count)
        print(data)
        try:
            for music_info in data:
                music_id = music_info.get("id")
                cover_url = music_info.get("cover_url")
                title = music_info.get("title")
                authors_list = music_info.get("authors")
                authors = ", ".join(authors_list)
                title_author = f"{title}\n{authors}"
                item = QtGui.QStandardItem(title_author)
                item.setData(music_id)
                icon = self.set_cover_to_music_in_list(cover_url)
                item.setIcon(icon)
                self.model.appendRow(item)

        except Exception as exc:
            logger.info(f"{self.set_music_to_list.__name__} exception - {exc}")
