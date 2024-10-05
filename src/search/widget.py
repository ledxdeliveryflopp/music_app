from PySide6 import QtWidgets

from src.ui.search.search_widget_ui import SearchWidgetUi


class SearchWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = SearchWidgetUi()
        self.ui.setupUi(self)
