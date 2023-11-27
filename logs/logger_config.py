import logging
from logging.handlers import RotatingFileHandler
import time
from flask import request, current_app

FILE_NAME="app.log"
MAX_BYTES=10000
BACKUP_COUNT=1

def configure_logger(app):
    @app.after_request
    def after_request(response):
        try:
            # Safely access request and response information
            remote_addr = request.remote_addr if request else 'Unknown'
            method = request.method if request else 'Unknown'
            scheme = request.scheme if request else 'Unknown'
            full_path = request.full_path if request else 'Unknown'
            status = response.status if response else 'Unknown'
            
            current_app.logger.info(f"IP: {remote_addr}, Method: {method}, Scheme: {scheme}, Path: {full_path}, Response: {status}")
            return response
        except Exception as e:
            current_app.logger.error("Logging error: %s", e)
        finally:
            # Ensure the response is returned regardless of logging outcome
            return response

    handler = RotatingFileHandler(FILE_NAME, maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    formatter.converter = time.gmtime
    handler.setFormatter(formatter)
    
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)