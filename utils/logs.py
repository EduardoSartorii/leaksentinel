import logging
import os

class LoggingSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_logger()
        return cls._instance

    def _initialize_logger(self):
        log_level = os.getenv("LOG_LEVEL", "INFO").upper()
        log_format = ('%(asctime)s - %(levelname)s - %(name)s - '
                      '%(module)s - %(funcName)s - line: %(lineno)d - %(message)s')

        logging.basicConfig(level=log_level, format=log_format)
        self.logger = logging.getLogger(__name__)

    def get_logger(self):
        return self.logger

logger_instance = LoggingSingleton().get_logger()    
