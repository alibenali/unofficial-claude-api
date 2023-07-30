from flask import Blueprint

# Import your route modules here
from . import chats

def register_routes(app):
    app.register_blueprint(chats.chats_bp)