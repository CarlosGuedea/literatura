from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session, make_response
from app.controllers.user_controller import get_users, handle_login
from flask_login import login_required, logout_user


user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def list_users():
    users = get_users()
    return render_template('users.html', users=users)

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    return handle_login()

@user_bp.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()


    resp = make_response(redirect(url_for('user.login')))
    resp.set_cookie('session', '', expires=0)  # Elimina la cookie
    return resp