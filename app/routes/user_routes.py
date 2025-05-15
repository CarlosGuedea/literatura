from flask import Blueprint, request, jsonify, render_template
from app.controllers.user_controller import get_users, create_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def list_users():
    users = get_users()
    return render_template('users.html', users=users)