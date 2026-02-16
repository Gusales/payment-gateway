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

    def log(self, message):
        self.__logger.setLevel(logging.INFO)
        log_message = f"[{self.__ctx}]: {message}"

        self.__logger.info(log_message)

    def error(self, message):
        self.__logger.setLevel(logging.ERROR)
        log_message = f"Error at: [{self.__ctx}]: {message}"

        self.__logger.error(log_message)

    def debug(self, message):
        if env.environment == Environment.DEV or env.environment == Environment.LOCAL or env.environment == Environment.TEST or env.environment == Environment.TEST_E2E:
            self.__logger.setLevel(logging.DEBUG)
            log_message = f"[{self.__ctx}]: {message}"
            self.__logger.debug(log_message)