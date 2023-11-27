import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

ENABLED_APIS=[
    "health_api.yaml"
]


# Flask configuration
SPECIFICATION_DIR = os.getenv("SPECIFICATION_DIR", './swagger/')
FLASK_DEBUG = os.getenv("FLASK_DEBUG")
FLASK_HOST = os.getenv("FLASK_HOST", "localhost")
FLASK_PORT = int(os.getenv("FLASK_PORT", 5000))  # Default to 5000 if not specified


# Logging configuration
LOG_FILE = os.getenv("LOG_FILE", "app.log")
LOG_ROTATION = os.getenv("LOG_ROTATION", "daily")
LOG_MAX_SIZE = os.getenv("LOG_MAX_SIZE", "10MB")


JWT_SECRET_KEY = "asdlfkua;iofjma.sdcjpa09sdf;via"