from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    # Register blueprints
    from .routes import register_routes
    register_routes(app)

    return app
