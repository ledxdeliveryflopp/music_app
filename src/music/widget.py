import base64
import os
import urllib.request
from functools import partial

import httpx
from PySide6 import QtWidgets
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

from loguru import logger

from src.settings.thread_manager import ThreadManager
from src.ui.music.music_widget_uii import MusicWidgetUi


class MusicWidget(QtWidgets.QWidget, ThreadManager):
    """Виджет музыки"""

    def __init__(self):
        super().__init__()
        self.duration = None

        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)

        self.ui = MusicWidgetUi()
        self.ui.setupUi(self)

        self.translate_ui()
        self.connect_sliders_etc()

    @logger.catch
    def translate_ui(self) -> None:
        """Установка текста на кнопки и тд"""
        self.ui.play_button.setText(self.tr("Play music"))
        self.ui.stop_button.setText(self.tr("Pause music"))
        self.ui.resume_button.setText(self.tr("Resume music"))
        self.ui.music_title.setText("Music title")
        self.ui.music_authors.setText("Music authors")
        self.ui.music_duration.setText("00:00")
        self.ui.current_music_time.setText("00:00")
        # self.ui.music_duration.hide()
        # self.ui.current_music_time.hide()
        self.ui.stop_button.hide()
        self.ui.resume_button.hide()

    @logger.catch
    def connect_sliders_etc(self) -> None:
        """Привязка слайдеров/текста и тд к функциям и сигналам"""
        # self.ui.time_slider.sliderPressed.connect(self.show_duration_labels)
        self.ui.valume_slider.setValue(50)
        self.ui.valume_slider.valueChanged.connect(self.change_volume)
        self.ui.time_slider.sliderMoved.connect(self.change_time_position)
        self.ui.play_button.clicked.connect(self.play_music)
        self.ui.stop_button.clicked.connect(self.stop_music)
        self.ui.resume_button.clicked.connect(self.resume_music)

    # @logger.catch
    # def show_duration_labels(self):
    #     """Отображение времени воспроизведения и длительности трека"""
    #     music_duration_status = self.ui.music_duration.isHidden()
    #     current_music_time_status = self.ui.current_music_time.isHidden()
    #     if music_duration_status is True and current_music_time_status is True:
    #         self.ui.music_duration.show()
    #         self.ui.current_music_time.show()
    #     else:
    #         self.ui.music_duration.hide()
    #         self.ui.current_music_time.hide()

    @logger.catch
    def get_music_duration(self, time) -> float:
        """Длительность трека в миллисекундах"""
        duration = round(time * 1000)
        self.duration = duration
        return duration

    @logger.catch
    def set_time_slider_duration(self, time) -> None:
        """Установить длительность трека для слайдера"""
        logger.info(f"{self.set_time_slider_duration.__name__} - started in thread")
        duration = self.get_music_duration(time)
        self.ui.time_slider.setMaximum(duration)
        logger.info(f"{self.set_time_slider_duration.__name__} - stoped in thread")

    @logger.catch
    def change_volume(self, value) -> None:
        """Изменить громкость"""
        volume = value / 100
        self.audio_output.setVolume(volume)

    @logger.catch
    def set_volume(self) -> None:
        """Установка громкости на 50%"""
        volume = self.ui.valume_slider.value() / 100
        self.audio_output.setVolume(volume)

    @logger.catch
    def change_slider(self, position) -> None:
        """Изменение слайдера при проигровании музыки"""
        self.ui.time_slider.setValue(position)

    @logger.catch
    def change_time_position(self, position) -> None:
        """Изменить место воспроизвидения"""
        if self.ui.time_slider.value() != self.media_player.position():
            self.media_player.setPosition(self.ui.time_slider.value())
        else:
            pass

    @logger.catch
    def set_current_music_duration(self, position) -> None:
        """Установка текущего времени воспроизведения для текста"""
        time = position / 60000
        self.ui.current_music_time.setText(f"{'%.2f'%time}")

    @logger.catch
    def set_label_duration(self, time) -> None:
        """Установить длительность трека в Qlabel"""
        logger.info(f"{self.set_label_duration.__name__} - started in thread")
        duration = self.get_music_duration(time)
        seconds = duration / 60000
        duration = '{:.2f}'.format(seconds)
        self.ui.music_duration.setText(duration)
        logger.info(f"{self.set_label_duration.__name__} - started in thread")

    @logger.catch
    def make_response(self) -> dict | None:
        """Запрос к API"""
        try:
            response = httpx.get("http://127.0.0.1:7000/music/find_music/?music_id=16").json()
            data = response["file_url"]
            duration = response["duration"]
            title = response["title"]
            authors = response["authors"]
            return {"data": data, "duration": duration, "title": title, "authors": authors}
        except httpx.ConnectError as httpx_error:
            logger.error(f"{self.decode_music.__name__} - {httpx_error}")
            return None

    @logger.catch
    def set_title(self, title: str) -> None:
        """Установить название"""
        self.ui.music_title.setText(title)

    @logger.catch
    def set_authors(self, authors: list) -> None:
        string = ""
        authors_len = len(authors) - 1
        for username in authors:
            if authors.index(username) == authors_len or len(authors) == 0:
                string = string + f"{username}"
            else:
                string = string + f"{username}, "
        self.ui.music_authors.setText(string)

    @logger.catch
    def decode_music(self) -> float:
        """Декодирование музыки"""
        response = self.make_response()
        if not response:
            return None
        title = response.get("title")
        self.set_title(title)
        authors = response.get("authors")
        self.set_authors(authors)
        data = response.get("data")
        duration = response.get("duration")
        urllib.request.urlretrieve(data, "encoded.mp3")
        with open("decoded.mp3", "wb+") as file, open("encoded.mp3", "rb") as api_file:
            api_data = api_file.read()
            decoded_data = base64.b64decode(api_data)
            file.write(decoded_data)
        os.remove("encoded.mp3")
        return duration

    @logger.catch
    def play_music(self) -> None:
        """Запуск проигрывателя"""
        duration = self.decode_music()
        if not duration:
            return None
        self.media_player.setSource(QUrl.fromLocalFile("decoded.mp3"))
        self.thread_manager.start(partial(self.set_time_slider_duration, duration))
        self.thread_manager.start(partial(self.set_label_duration, duration))
        self.media_player.positionChanged.connect(self.change_slider)
        self.ui.time_slider.valueChanged.connect(self.change_time_position)
        self.media_player.positionChanged.connect(self.set_current_music_duration)
        self.ui.play_button.hide()
        self.ui.stop_button.show()
        self.set_volume()
        self.media_player.play()

    @logger.catch
    def stop_music(self) -> None:
        """Поставить музыку на паузу"""
        if self.media_player.isPlaying() is True:
            self.media_player.pause()
            if self.ui.resume_button.isHidden() is True:
                self.ui.stop_button.hide()
                self.ui.resume_button.show()
        else:
            logger.debug(f"music not playing")
            try:
                self.media_player.setSource("")
                os.remove("decoded.mp3")
            except Exception as exc:
                logger.info(f"stop_music delete exception: {exc}")

    @logger.catch
    def resume_music(self) -> None:
        """Продолжить воспреизведение музыки"""
        self.media_player.play()
        self.ui.resume_button.hide()
        self.ui.stop_button.show()
