import logging

from misc.decorators import Singleton
from misc.logger_formatter import CustomFormatter


@Singleton
class CustomLogger(logging.Logger):
    """
    Custom logger class that provides a logger with a custom formatter.
    """

    def __init__(self, name, level=logging.DEBUG):
        """
        Initializes the CustomLogger.

        :param name: The name of the logger.
        :param level: The logging level (default is DEBUG).
        """
        super().__init__(name)
        self.setLevel(level)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        formatter = CustomFormatter("%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")

        console_handler.setFormatter(formatter)
        self.addHandler(console_handler)

    def set_level(self, level):
        """
        Sets the logging level for the logger.

        :param level: The new logging level to be set.
        """
        self.setLevel(level)
        for handler in self.handlers:
            handler.setLevel(level)
