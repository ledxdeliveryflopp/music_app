from PySide6 import QtWidgets

from src.ui.main.main_widget_ui import MainWidgetUi


class MainWidget(QtWidgets.QWidget):
    """Виджет музыки"""

    def __init__(self):
        super().__init__()
        self.ui = MainWidgetUi()
        self.ui.setupUi(self)