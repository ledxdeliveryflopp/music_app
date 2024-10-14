import configparser
import os
from dataclasses import dataclass
from datetime import datetime

from loguru import logger


@dataclass
class IniConfig:
    """Класс ini настроек приложения"""
    config = configparser.ConfigParser()

    def set_base_ini_config(self) -> None:
        """Создание базового конфига"""
        path = os.path.exists("config/config.ini")
        if path is False:
            self.config["AUTH"] = {"token": "", "expire": ""}
            self.config["LANG"] = {"code": "en_EN"}
            with open("config/config.ini", "w") as file:
                self.config.write(file)
            logger.info(f"base ini created")

    def change_auth_section(self, token: bytes, expire: datetime) -> None:
        """Изменение секции auth"""
        path = os.path.exists("config/config.ini")
        self.config["AUTH"] = {"token": token, "expire": expire}
        self.config["LANG"] = {"code": "en_EN"}
        if path is False:
            self.set_base_ini_config()
            with open("config/config.ini", "w") as file:
                self.config.write(file)
            logger.info(f"base ini created, token updated")
        else:
            with open("config/config.ini", "w") as file:
                self.config.write(file)
            logger.info(f"token updated")

    def check_auth_token_section(self) -> bool:
        """Проверка наличия токена в ini"""
        self.config.read("config/config.ini")
        if "AUTH" in self.config:
            token_data = self.config["AUTH"]["token"]
            if token_data:
                return True
            else:
                return False
        else:
            return False

    def get_auth_token_section(self) -> str:
        """Получить токен из ini"""
        self.config.read("config/config.ini")
        token = self.config["AUTH"]["token"]
        return token


def init_ini_settings() -> IniConfig:
    return IniConfig()


ini_settings = init_ini_settings()
