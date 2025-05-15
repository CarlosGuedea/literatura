from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp)
    from app.routes.post_routes import post_bp
    app.register_blueprint(post_bp)
    from app.routes.comment_routes import comment_bp
    app.register_blueprint(comment_bp)
    from app.routes.raiz_routes import raiz_bp
    app.register_blueprint(raiz_bp)

    return app
