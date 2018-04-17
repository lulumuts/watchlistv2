from flask import Flask

#import 3rd party apps
from flask_bootstrap import Bootstrap

# setting up configuration
from .config import config_options


#Initializing flask extensions
bootstrap = Bootstrap()

def create_app(config_name):
    # Init app
    app = Flask(__name__)

   # Creating the app configurations
    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Configure request
    from .request import configure_request
    configure_request(app)

    return app
