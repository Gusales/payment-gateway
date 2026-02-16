from app.config.env import Environment, env
from app.utils.logger import Logger

import logging

class TestLogger:
    
    def test_should_be_logger_message(self, caplog):
        caplog.set_level(logging.INFO)
        logger = Logger("TestLogger")
        message = "Hello World"

        logger.log(message)

        assert f"[TestLogger]: {message}" in caplog.text
    
    def test_should_be_logger_error_messages(self, caplog):
        caplog.set_level(logging.ERROR)
        logger = Logger("TestLogger")
        message = "Error Message"

        print(caplog.text)

        logger.error(message)

        assert f"Error at: [TestLogger]: {message}" in caplog.text

    def test_should_be_logger_debug_message_with_env_TEST(self, caplog, monkeypatch):
        monkeypatch.setattr(env, "environment", Environment.TEST)
        caplog.set_level(logging.DEBUG)
        logger = Logger("TestLogger")
    
        message = "Debug Message"

        logger.debug(message)

        assert "DEBUG" in caplog.text
        assert f"[TestLogger]: {message}" in caplog.text

    
    def test_should_be_logger_debug_message_with_env_not_TEST(self, caplog, monkeypatch):
        monkeypatch.setattr(env, "environment", Environment.PROD)
        caplog.set_level(logging.DEBUG)
        logger = Logger("TestLogger")
    
        message = "Debug Message"

        logger.debug(message)

        assert "" in caplog.text
