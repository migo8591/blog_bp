from flask import Flask 
from flask_login import LoginManager, current_user
from .extensions import db, bcrypt
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from app.public import public_bp
from app.auth import auth_bp
from app.admin import admin_bp
from .model import Users
from config import DATABASE_CONNECTION_URI
app = Flask(__name__)
ckeditor = CKEditor(app)
bcrypt.init_app(app)
app.register_blueprint(public_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp) 
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
db.init_app(app)
migrate = Migrate(app, db)
with app.app_context():
    db.create_all()
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


def create_app(config):
    app.config.from_object(config)
    return app
@app.context_processor
def inject_user():
    user = current_user  # Obtiene el usuario actual si está autenticado
    return dict(user=user)  # Pasamos el usuario al contexto global