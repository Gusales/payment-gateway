import logging

from app.config.env import env, Environment

class Logger:
    def __init__(self, context):
        self.__ctx = context

        logging.basicConfig(
            format="{levelname} | {asctime}: {message}",
            datefmt="%Y-%m-%d %H:%M",
            style="{"
        )

        self.__logger = logging.getLogger(__name__)
        self.__logger.setLevel(logging.INFO)

    def log(self, message):
        log_message = f"[{self.__ctx}]: {message}"

        self.__logger.info(log_message)

    def error(self, message):
        log_message = f"[{self.__ctx}]: {message}"

        self.__logger.error(log_message)

    def debug(self, message):
        if env.environment == Environment.DEV or env.environment == Environment.LOCAL:
            log_message = f"[{self.__ctx}]: {message}"
            self.__logger.info(log_message)