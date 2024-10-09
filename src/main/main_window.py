from PySide6 import QtWidgets

from src.main.main_widget import MainWidget


class MainWindow(QtWidgets.QMainWindow):
    """Основное окно"""

    def __init__(self):
        super().__init__()
        self.main_widget = MainWidget()
        self.setup_size()
        self.setCentralWidget(self.main_widget)

    def setup_size(self):
        """Установить размер окна"""
        self.window().resize(1000, 360)
        self.setMaximumSize(1000, 360)
        self.setMinimumSize(1000, 360)
