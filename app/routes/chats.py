from flask import Blueprint, jsonify, request
from claude_rest.chats import claudeREST


chats_bp = Blueprint('chats/', __name__, url_prefix='/api/chats')

@chats_bp.route('/new_chat')
def new_chat(methods=['POST']):
    name = request.json['name']
    claude = claudeREST()
    chat = claude.create_chat(name)
    return jsonify(chat)

@chats_bp.route('/', methods=['GET'])
def get_chats():
    claude = claudeREST()
    chats = claude.get_chats()
    return jsonify(chats)

@chats_bp.route('/<chat_uuid>', methods=['GET'])
def get_chat(chat_uuid):
    claude = claudeREST()
    chat = claude.get_chat(chat_uuid)
    return jsonify(chat)

@chats_bp.route('/send_message')
def append_message(methods=['POST']):
    message = request.json['message']
    chat_uuid = request.json['chat_uuid']
    claude = claudeREST()
    res_status = claude.append_message(message, chat_uuid)
    if res_status == 200:
        return jsonify({'success':True})
    else:
        return jsonify({'error':res_status})