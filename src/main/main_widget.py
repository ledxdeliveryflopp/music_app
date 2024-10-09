from PySide6 import QtWidgets

from src.main.widget_ui import Ui_MainWindow


class MainWidget(QtWidgets.QWidget):
    """Класс главного виджета"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
