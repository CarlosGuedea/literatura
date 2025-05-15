from flask import Blueprint, request, jsonify
from app.controllers.post_controller import get_posts, create_post

post_bp = Blueprint('post', __name__)

@post_bp.route('/posts', methods=['GET'])
def list_posts():
    return jsonify(get_posts())

@post_bp.route('/posts', methods=['POST'])
def add_post():
    data = request.json
    create_post(data['user_id'], data['title'], data['content'])
    return jsonify({'message': 'Post created'}), 201