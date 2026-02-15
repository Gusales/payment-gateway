import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config.env import env
from app.utils.logger import Logger

Base = declarative_base()

class Database:
    def __init__(self):
        self.__logger = Logger(self.__class__.__name__)

        self.__db_url = f"{env.DB_DIALECT}://{env.DB_USER}:{env.DB_PASSWORD}@{env.DB_HOST}:{env.DB_PORT}/{env.DB_NAME}"

        self.__logger.debug(f"Trying to connect with database using this url: {self.__db_url}")

        self.__engine = create_engine(
            self.__db_url,
        )
        self.__session_local = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.__engine
        )

    def get_connection(self):
        conn = self.__session_local()
        try:
            yield conn
        except Exception as e:
            self.__logger.error(f"An error has ocourred: {str(e)}")
        finally:
            conn.close()
    
    def get_connection_url(self):
        return self.__db_url
