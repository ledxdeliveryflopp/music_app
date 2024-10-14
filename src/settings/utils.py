import os
import urllib.request

import httpx
from loguru import logger

from src.settings.settings import settings


@logger.catch
def set_up_static_dirs() -> None:
    """Создание статических директорий"""
    try:
        os.makedirs("config", exist_ok=True)
        os.makedirs("static", exist_ok=True)
        os.makedirs("static/images", exist_ok=True)
        path = os.path.exists("static/images/tray")
        icon_path = os.path.exists("static/images/tray/icon.png")
        print(icon_path)
        if path is False or icon_path is False:
            os.makedirs("static/images/tray", exist_ok=True)
            response = httpx.get(f"{settings.api_settings.api_url}app/tray_icon/").json()
            static_icon_url = response.get("icon")
            urllib.request.urlretrieve(static_icon_url, "static/images/tray/icon.png")
    except Exception as exception:
        logger.info(f"{set_up_static_dirs.__name__} - {exception}")
