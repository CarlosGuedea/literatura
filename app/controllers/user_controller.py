from sqlalchemy import text
from app import db

def get_users():
    query = text("SELECT username, email, image_filename FROM users")
    result = db.session.execute(query)
    # Convertir cada fila a dict
    users = [dict(row) for row in result.mappings().all()]
    return users

def create_user(username, email, password):
    query = text("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)")
    db.session.execute(query, {
        'username': username,
        'email': email,
        'password': password
    })
    db.session.commit()
