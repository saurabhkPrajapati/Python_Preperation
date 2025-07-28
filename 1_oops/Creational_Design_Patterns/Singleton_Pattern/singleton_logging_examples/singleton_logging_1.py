import logging


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, name, log_file=None):
        if not hasattr(self, 'logger'):
            self.name = name
            self.logger = logging.getLogger(name)
            self.logger.setLevel(logging.DEBUG)

            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

            # Create console handler
            ch = logging.StreamHandler()
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)

            # If log_file is provided, create file handler
            if log_file:
                fh = logging.FileHandler(log_file)
                fh.setFormatter(formatter)
                self.logger.addHandler(fh)
                self.logger.addHandler(fh)

    def get_logger(self):
        return self.logger

    def get_logger_name(self):
        return self.name


# Example usage
s1 = Singleton("Logger_1", "logs.txt")
s2 = Singleton("Logger_2", "logs.txt")

print(s1.get_logger_name())
print(s2.get_logger_name())

logger1 = s1.get_logger()
logger2 = s2.get_logger()

logger1.debug("Debug message from logger1")
logger2.debug("Debug message from logger2")
