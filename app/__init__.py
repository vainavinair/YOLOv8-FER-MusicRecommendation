from flask import Flask
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)


    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.recommedations import bp as recommedations_bp
    app.register_blueprint(recommedations_bp, url_prefix='/recommedations')
    

    return app