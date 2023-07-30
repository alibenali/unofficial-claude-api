from flask import Blueprint

# Import your route modules here
from . import books, chats

def register_routes(app):
    app.register_blueprint(books.books_bp)

    app.register_blueprint(chats.chats_bp)