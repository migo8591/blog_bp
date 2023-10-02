from .extensions import db
from datetime import datetime

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    #author = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default= datetime.utcnow)
    slug = db.Column(db.String(255))
    # Foreing key to link Users(refer to primary of the user)
    # poster_id= db.Column(db.Integer, db.ForeignKey('users.id'))