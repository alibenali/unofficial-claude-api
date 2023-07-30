from flask import Blueprint, jsonify, request

books = []
books_bp = Blueprint('books', __name__, url_prefix='/api/books')

@books_bp.route('/', methods=['GET'])
def get_all_books():
    return jsonify(books)

@books_bp.route('/', methods=['POST'])
def add_book():
    # ... (same as before)
    pass

@books_bp.route('/<int:index>', methods=['GET'])
def get_book(index):
    # ... (same as before)
    pass

@books_bp.route('/<int:index>', methods=['PUT'])
def update_book(index):
    # ... (same as before)
    pass

@books_bp.route('/<int:index>', methods=['DELETE'])
def delete_book(index):
    # ... (same as before)
    pass
