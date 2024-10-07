import httpx
import requests
from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog
from loguru import logger

from src.upload.widget_ui import Ui_upload_music_widget


class UploadMusicWidget(QtWidgets.QWidget):
    """Виджет загрузки музыки"""

    def __init__(self):
        super().__init__()
        self.music_id: int = None
        self.token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2VtYWlsIjoiZ2VvQGdtYWlsLmNvbSIsInVzZXJfaWQiOjYsInJhbmRvbV9zdHIiOlsieSIsIj8iLCJSIiwiNiIsInIiLCI1IiwiSyIsIjciXX0.VWNFKCAjQYCu7y_JJrjb3eUZmE1_NWoGJh6tVrkPAYM"
        self.ui = Ui_upload_music_widget()
        self.ui.setupUi(self)
        self.translate_ui()
        self.set_signals()

    @logger.catch
    def translate_ui(self) -> None:
        """Установка текста на кнопки и тд"""
        self.ui.add_author_button.setText(self.tr("add authors"))
        self.ui.upload_cover_file_button.setText(self.tr("Upload cover file"))
        self.ui.upload_music_file_button.setText(self.tr("Upload mp3 file"))
        self.ui.pushButton.setText(self.tr("Upload music"))

    @logger.catch
    def set_signals(self) -> None:
        """Установка сигналов"""
        self.ui.pushButton.clicked.connect(self.upload_music)
        self.ui.upload_music_file_button.clicked.connect(self.set_music_file)
        self.ui.upload_cover_file_button.clicked.connect(self.set_cover_file)

    @logger.catch
    def set_main_music_info(self) -> int:
        """Создание объекта музыки и установка авторов"""
        author = self.ui.author_input.text()
        authors = [author]
        return authors

    @logger.catch
    def set_music_file(self) -> None:
        """Выбор файла музыки"""
        music_file = QFileDialog.getOpenFileName(self, self.tr("search file"),
                                                 filter="mp3(*.mp3)")[0]
        try:
            self.ui.music_file_label.setText(music_file)
            self.ui.pushButton.setEnabled(True)
            logger.info(f"upload_music_file = {music_file}")
            return music_file
        except Exception as exc:
            logger.error(f"{exc}")

    @logger.catch
    def set_cover_file(self) -> None:
        """Выбор файла обложки"""
        cover_file = QFileDialog.getOpenFileName(self, self.tr("search file"),
                                                 filter="png(*.png)")[0]
        try:
            self.ui.pushButton.setEnabled(True)
            logger.info(f"upload_cover_file = {cover_file}")
            self.ui.cover_file_label.setText(cover_file)
        except Exception as exc:
            logger.error(f"{exc}")

    @logger.catch
    def check_fill_files(self):
        music_file = self.ui.music_file_label.text()
        cover_file = self.ui.cover_file_label.text()
        if not music_file or not cover_file:
            self.ui.pushButton.setEnabled(False)
            return False
        else:
            return True

    @logger.catch
    def upload_music(self):
        check = self.check_fill_files()
        if check is False:
            pass
        else:
            try:
                main_data = self.set_main_music_info()
                music_file = self.ui.music_file_label.text()
                cover_file = self.ui.cover_file_label.text()
                data = {"authors": main_data}
                request_main = httpx.post("http://127.0.0.1:7000/music/upload/", json=data,
                                          headers={f"Authorization": self.token})
                request_main_data = request_main.json()
                music_id = request_main_data.get("id")
                music_file_data = {'music_file': open(f'{music_file}', 'rb')}
                cover_file_data = {'cover_file': open(f'{cover_file}', 'rb')}
                response_music = httpx.patch(f"http://127.0.0.1:7000/music/upload_music_file/?music_id="
                                             f"{music_id}", files=music_file_data)
                response_cover = httpx.patch(f"http://127.0.0.1:7000/music/upload_cover_file/?music_id="
                                             f"{music_id}", files=cover_file_data)
            except Exception as exception:
                logger.info(f"upload_music error - {exception}")
