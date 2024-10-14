import sys

from loguru import logger
from PySide6 import QtWidgets

from src.main.main_window import MainWindow
from src.settings.config import ini_settings

from src.settings.utils import set_up_static_dirs
from src.tray.widget import TrayWidget


@logger.catch
def start_app() -> None:
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    app.setStyle('Windows')
    window = MainWindow()
    tray = TrayWidget(app, window, window.main_widget.ui.music_play_widget.media_player)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    logger.add("application.log", rotation="100 MB",
               format="{time:DD-MM-YYYY at HH:mm:ss} | {level} | {message}")
    logger.info(f"application started")
    set_up_static_dirs()
    ini_settings.set_base_ini_config()
    start_app()

