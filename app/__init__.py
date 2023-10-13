from flask import Flask 
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from .extensions import db, bcrypt
from flask_migrate import Migrate
from app.public import public_bp
from app.auth import auth_bp
from .model import Users
app = Flask(__name__)
bcrypt.init_app(app)
app.register_blueprint(public_bp)
app.register_blueprint(auth_bp)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:rebHaraya314@localhost/blog_matematica"
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