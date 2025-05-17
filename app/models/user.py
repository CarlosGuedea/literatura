from app import db
from flask_login import UserMixin  # importa UserMixin

class User(db.Model, UserMixin):  # hereda de UserMixin
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


from app import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
