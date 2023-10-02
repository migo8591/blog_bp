from flask import Flask 
from .extensions import db
from app.public import public_bp


app = Flask(__name__)
app.register_blueprint(public_bp)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:rebHaraya314@localhost/blog_matematica"
db.init_app(app)
with app.app_context():
    db.create_all()

def create_app(config):
    app.config.from_object(config)
    return app