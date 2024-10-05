

from PySide6 import QtWidgets

from src.ui.side_bar.side_bar_widget_ui import UiSideBarWidget


class SideBarWidget(QtWidgets.QWidget):
    """Виджет музыки"""

    def __init__(self):
        super().__init__()
        self.ui = UiSideBarWidget()
        self.ui.setupUi(self)


# 800 600