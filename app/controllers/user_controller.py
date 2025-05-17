from sqlalchemy import text
from app import db
from flask import request, render_template, redirect, url_for, session
from sqlalchemy import text
from flask_login import login_user
from app import db
from app.models.user import User  # Modelo compatible con Flask-Login


def get_users():
    query = text("SELECT username, email, image_filename FROM users")
    result = db.session.execute(query)
    # Convertir cada fila a dict
    users = [dict(row) for row in result.mappings().all()]
    return users

def handle_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        query = text("SELECT id, username, email, password FROM users WHERE email = :email AND password = :password")
        result = db.session.execute(query, {'email': email, 'password': password}).mappings().first()

        if result:
            # Crear una instancia de User (UserMixin)
            user = User()
            user.id = result['id']
            user.username = result['username']
            user.email = result['email']

            login_user(user)
            session['user_id'] = user.id
            return redirect(url_for('post.new_post'))  # Redirige donde quieras
        else:
            return render_template('login.html', error="Credenciales inválidas")

    return render_template('login.html')


