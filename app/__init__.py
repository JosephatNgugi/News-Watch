from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

# Initializing the application
def create_app(config_name):
    app = Flask(__name__)
    
    # Creating the app configs
    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)
    
    # Register the Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # setting Config
    from .requests import configure_request
    configure_request(app)
    
    return app