import httpx
from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import QModelIndex
from PySide6.QtWidgets import QVBoxLayout, QAbstractItemView
from loguru import logger

from src.main.widget_ui import MainWidgetUi
from src.search.widget import SearchWidget


class MainWidget(QtWidgets.QWidget):
    """Виджет музыки"""

    def __init__(self):
        super().__init__()
        self.model = None
        self.search_widget = None
        self.ui = MainWidgetUi()
        self.ui.setupUi(self)
        self.init_search_widget()
        self.set_signals()
       
    @logger.catch
    def init_search_widget(self) -> None:
        """инициализация виджета поиска"""
        self.search_widget = SearchWidget(music_widget=self.ui.music_widget)
        logger.info(f"{self.init_search_widget.__name__} - inited")
    
    @logger.catch
    def set_signals(self) -> None:
        """Установка сигналов"""
        self.ui.side_bar_widget.ui.search_button.clicked.connect(self.open_search_widget)
        logger.info(f"{self.set_signals.__name__} - inited")

    @logger.catch
    def open_search_widget(self) -> None:
        self.ui.selection_widget.hide()
        self.ui.main_window_layout = QVBoxLayout(self.search_widget)
        self.ui.gridLayout_2.addWidget(self.search_widget, 1, 1, 1, 1)
