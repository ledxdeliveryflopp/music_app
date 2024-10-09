from PySide6 import QtWidgets


from src.side_bar.widget_ui import Ui_Side_bar_widget


class SideBarWidget(QtWidgets.QWidget):
    """Виджет бокового меню"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_Side_bar_widget()
        self.ui.setupUi(self)
