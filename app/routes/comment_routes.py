from flask import Blueprint, request, jsonify
from app.controllers.comment_controller import get_comments, create_comment

comment_bp = Blueprint('comment', __name__)

@comment_bp.route('/comments', methods=['GET'])
def list_comments():
    return jsonify(get_comments())

@comment_bp.route('/comments', methods=['POST'])
def add_comment():
    data = request.json
    create_comment(data['post_id'], data.get('author_name'), data['comment'])
    return jsonify({'message': 'Comment created'}), 201
