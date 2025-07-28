import logging


class Singleton(object):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


def singleton_logger(cls):
    cls._logger = None

    def get_logger(self):
        if not self._logger:
            self._logger = logging.getLogger(cls.__name__)
            self._logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            ch = logging.StreamHandler()
            ch.setFormatter(formatter)
            self._logger.addHandler(ch)
        return self._logger

    cls.get_logger = get_logger
    return Singleton(cls)


@singleton_logger
class Logger:
    def __init__(self, name):
        self.name = name


# Example usage:
logger1 = Logger("Logger1")
logger2 = Logger("Logger2")

logger1.get_logger().debug("Debug message from logger1")
logger2.get_logger().debug("Debug message from logger2")

print(logger1 is logger2)  # Output: True
