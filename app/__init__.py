from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.secret_key = 'clave_secreta'

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'user.login' # ajusta al nombre correcto de tu blueprint y ruta

    # Importar modelos (incluye el user_loader)
    from app.models import user  # <- IMPORTANTE: esto registra el user_loader

    # Registrar Blueprints
    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp)
    from app.routes.post_routes import post_bp
    app.register_blueprint(post_bp)
    from app.routes.comment_routes import comment_bp
    app.register_blueprint(comment_bp)
    from app.routes.raiz_routes import raiz_bp
    app.register_blueprint(raiz_bp)

    return app
