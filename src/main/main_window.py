from PySide6 import QtWidgets

from src.main.main_widget import MainWidget


class MainWindow(QtWidgets.QMainWindow):
    """Основное окно"""

    def __init__(self):
        super().__init__()
        self.main_widget = MainWidget()
        self.window().resize(1104, 791)
        self.setCentralWidget(self.main_widget)

