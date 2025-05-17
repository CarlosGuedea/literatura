from flask import Blueprint, request, jsonify, render_template
from app.controllers.user_controller import get_users

raiz_bp = Blueprint('raiz', __name__)

@raiz_bp.route('/', methods=['GET'])
def list_raiz():
    users = get_users()
    return render_template('raiz.html', users=users)