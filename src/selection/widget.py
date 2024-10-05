from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QMovie

from src.ui.selection.selection_widget_ui import SelectionWidgetUi


class SelectionWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = SelectionWidgetUi()
        self.ui.setupUi(self)
        # self.resize(1920, 1080)
        # path = "static/main_resized.gif"
        # self.movie = QMovie(path)
        # self.ui.gif_label.setMovie(self.movie)
        # self.movie.start()
