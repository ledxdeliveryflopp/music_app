from PySide6 import QtWidgets

from src.selection.widget_ui import SelectionWidgetUi


class SelectionWidget(QtWidgets.QWidget):
    """Виджет рекомендация и тд(в данный момент заглушка)"""

    def __init__(self):
        super().__init__()
        self.ui = SelectionWidgetUi()
        self.ui.setupUi(self)
        # self.resize(1920, 1080)
        # path = "static/main_resized.gif"
        # self.movie = QMovie(path)
        # self.ui.gif_label.setMovie(self.movie)
        # self.movie.start()
