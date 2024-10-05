

from PySide6 import QtWidgets

from src.side_bar.widget_ui import UiSideBarWidget


class SideBarWidget(QtWidgets.QWidget):
    """Виджет бокового меню"""

    def __init__(self):
        super().__init__()
        self.ui = UiSideBarWidget()
        self.ui.setupUi(self)
        self.ui.search_button.setText(self.tr("search"))
