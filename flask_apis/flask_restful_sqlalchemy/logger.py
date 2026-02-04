import logging
import os
import uuid
import threading
from flask import Flask, request
from flask_restful import Api, Resource

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

def singleton(cls):
    """Thread-Safe Singleton Decorator"""
    instances = {}
    lock = threading.Lock()

    def get_instance(*args, **kwargs):
        with lock:  # Ensures only one instance per class
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
            return instances[cls]

    return get_instance

@singleton
class LoggerSingleton:
    """Singleton Logger with Separate Log Files for Each Request"""

    def __init__(self):
        self.configure_console_logger()

    def configure_console_logger(self):
        """Configure a global console logger"""
        self.console_logger = logging.getLogger("ConsoleLogger")
        self.console_logger.setLevel(logging.INFO)

        # Prevent duplicate handlers
        if not self.console_logger.hasHandlers():
            console_handler = logging.StreamHandler()
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            console_handler.setFormatter(formatter)
            self.console_logger.addHandler(console_handler)

    def get_request_logger(self, name):
        """Create a new logger for each request (file-based logging)"""
        request_id = str(uuid.uuid4())[:8]  # Generate a short unique ID
        # log_filename = f"logs/request_{request_id}.log"
        log_filename = f"logs/{name}" # get filename from dynamically when client interacts

        request_logger = logging.getLogger(f"RequestLogger-{request_id}")
        request_logger.setLevel(logging.INFO)

        # Prevent duplicate handlers for this logger
        if not request_logger.hasHandlers():
            file_handler = logging.FileHandler(log_filename)
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(formatter)
            request_logger.addHandler(file_handler)

        return request_logger

# Get Singleton Logger Instance
logger_singleton = LoggerSingleton()


# for testing purposes
if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)

    class HelloWorld(Resource):
        def get(self):
            client_ip = request.remote_addr  # Get client IP
            
            # Log to console
            logger_singleton.console_logger.info(f"Request received from {client_ip}")

            # Log to a separate file per request
            request_logger = logger_singleton.get_request_logger("test")
            request_logger.info(f"Request received from {client_ip}")

            return {"message": "Hello, World!"}

    api.add_resource(HelloWorld, "/")

    if __name__ == "__main__":
        app.run(debug=True)
