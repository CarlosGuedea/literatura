from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config
from bs4 import BeautifulSoup

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.secret_key = 'clave_secreta'

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    # Registrar filtro personalizado
    @app.template_filter('preview')
    def preview_filter(html, num_words=10):
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()
        words = text.split()
        return ' '.join(words[:num_words]) + '...'

    # Importar modelos (incluye el user_loader)
    from app.models import user

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
