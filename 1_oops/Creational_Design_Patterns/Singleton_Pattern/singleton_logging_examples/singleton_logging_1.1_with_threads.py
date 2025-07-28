import logging
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed


class Singleton(object):
    _instance = None
    _lock = threading.Lock()  # Add a lock for thread safety

    def __new__(cls, *args, **kwargs):
        with cls._lock:
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

    def get_logger(self):
        return self.logger

    def get_logger_name(self):
        return self.name


# Example usage
def use_singleton(logger_name):
    s = Singleton(logger_name, "logs.txt")
    logger = s.get_logger()
    print(s.get_logger_name(), end='\n')
    logger.debug(f"Debug message from {logger_name}")


with ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(use_singleton, ["Logger_1", "Logger_2"])

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(use_singleton, logger_name) for logger_name in ["Logger_1", "Logger_2"]]

    # Collect results as they complete
    # for future in as_completed(futures):
    #     result = future.result()
