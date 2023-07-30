from flask import Blueprint, jsonify

other_resource_data = [
    {'name': 'Resource 1'},
    {'name': 'Resource 2'},
    # ...
]

other_resource_bp = Blueprint('other_resource', __name__, url_prefix='/api/other')

@other_resource_bp.route('/', methods=['GET'])
def get_all_resources():
    return jsonify(other_resource_data)

# Add other routes for this resource as needed
