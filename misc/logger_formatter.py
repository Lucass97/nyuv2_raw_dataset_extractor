import logging


class CustomFormatter(logging.Formatter):
    """
    Custom log formatter that adds colors to log levels.

    Usage:
        formatter = CustomFormatter()
        handler.setFormatter(formatter)

    Colors:
        - DEBUG: White
        - INFO: Green
        - WARNING: Yellow
        - ERROR: Red
        - CRITICAL: Magenta
    """

    LEVEL_COLORS = {
        'DEBUG': '\033[37m',
        'INFO': '\033[32m',
        'WARNING': '\033[33m',
        'ERROR': '\033[31m',
        'CRITICAL': '\033[35m'
    }
    RESET_COLOR = '\033[0m'

    def format(self, record) -> str:
        """
        Formats the log record with colorized log level.

        :param record: The log record to format.
        :return: The formatted log record as a string.
        """
        levelname = record.levelname
        if levelname in self.LEVEL_COLORS:
            levelname_color = f"{self.LEVEL_COLORS[levelname]}{levelname}{self.RESET_COLOR}"
            record.levelname = levelname_color
        return super(CustomFormatter, self).format(record)