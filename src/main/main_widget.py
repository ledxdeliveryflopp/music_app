import httpx
from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import QModelIndex
from PySide6.QtWidgets import QVBoxLayout, QAbstractItemView
from loguru import logger

from src.search.widget import SearchWidget
from src.ui.main.main_widget_ui import MainWidgetUi


class MainWidget(QtWidgets.QWidget):
    """Виджет музыки"""

    def __init__(self):
        super().__init__()
        self.ui = MainWidgetUi()
        self.ui.setupUi(self)
        self.ui.side_bar_widget.ui.search_button.clicked.connect(self.open_search_widget)

        self.search_widget = SearchWidget()
        self.search_widget.ui.search_input.textChanged.connect(self.set_music_to_list)

        self.model = QtGui.QStandardItemModel()
        self.search_widget.ui.listView.setModel(self.model)
        self.search_widget.ui.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.search_widget.ui.listView.pressed.connect(self.play_music_in_music_widget)

    @logger.catch
    def play_music_in_music_widget(self, index: QModelIndex):
        music_index = self.search_widget.ui.listView.model().itemFromIndex(index)
        logger.info(f"play_music_in_music_widget index - {music_index.text()}")
        self.ui.music_widget.play_music(music_index.text())

    @logger.catch
    def open_search_widget(self) -> None:
        self.ui.selection_widget.hide()
        self.ui.main_window_layout = QVBoxLayout(self.search_widget)
        self.ui.gridLayout_2.addWidget(self.search_widget, 1, 1, 1, 1)

    @logger.catch
    def search_music(self, query: str) -> None:
        """Поиск музыки по автору и названию"""
        try:
            request = httpx.get(f"http://127.0.0.1:7000/music/find_music/?author_username="
                                f"{query}&music_title={query}")
            request_data = request.json()
            return request_data
        except Exception as exception:
            logger.error(f"search_music error - {exception}")
            return None

    @logger.catch
    def delete_duplicate(self, title: str) -> None:
        """Удаление дубликатов"""
        item = self.model.findItems(title)
        if len(item) > 1:
            row = item[1].row()
            self.model.removeRow(row)

    @logger.catch
    def set_music_to_list(self, query) -> None:
        """Добавить музыку в список"""
        data = self.search_music(query)
        try:
            for music_info in data:
                cover = music_info.get("cover_url")
                title = music_info.get("title")
                item = QtGui.QStandardItem(title)
                self.model.appendRow(item)
                self.delete_duplicate(title)
        except TypeError:
            logger.info(f"TypeError set music list exception")
            if self.search_widget.ui.search_input.text() == "":
                row_count = self.model.rowCount()
                self.model.removeRows(0, row_count)
            else:
                pass
