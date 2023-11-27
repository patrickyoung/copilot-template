import connexion
from flask import after_this_request
from logs.logger_config import configure_logger
import config
from flask_jwt_extended import JWTManager


def create_app():
    connexion_app = connexion.FlaskApp(__name__, specification_dir=config.SPECIFICATION_DIR)
    connexion_app.add_api('health_api.yaml')

    # Confugure Logger
    configure_logger(connexion_app.app)
    
    # Configure JWT
    connexion_app.app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this to a proper secret key!
    JWTManager(connexion_app.app)
    
    @connexion_app.app.after_request
    def add_security_headers(response):
        response.headers['Content-Security-Policy'] = "default-src 'self'"
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        return response

    return connexion_app

if __name__ == '__main__':
    app = create_app()
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT)
