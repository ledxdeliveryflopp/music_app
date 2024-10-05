import sys
from loguru import logger
from PySide6 import QtWidgets

from src.main.main_window import MainWindow


def start_app() -> None:
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.setStyle('Windows')
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    logger.add("application.log", rotation="100 MB",
               format="{time:DD-MM-YYYY at HH:mm:ss} | {level} | {message}")
    logger.info(f"application started")
    start_app()


