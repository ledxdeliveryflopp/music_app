from PySide6 import QtWidgets

from src.search.widget_ui import SearchWidgetUi


class SearchWidget(QtWidgets.QWidget):
    """Виджет поиска музыки"""

    def __init__(self):
        super().__init__()
        self.ui = SearchWidgetUi()
        self.ui.setupUi(self)
