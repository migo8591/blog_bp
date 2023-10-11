from flask import render_template, flash
from .webforms import UserForm
from ..model import Users
from ..extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

from . import auth_bp

@auth_bp.route("/login")
def login():
    our_users = Users.query.order_by(Users.date_added)
    return render_template("auth/login.html", usuarios=our_users) 
@auth_bp.route("/sign", methods=['GET','POST'])
def sign():
    formulario= UserForm()
    if formulario.validate_on_submit():
        user=Users.query.filter_by(email=formulario.email.data).first()
        if user is None:
            hashed_pw=generate_password_hash(formulario.password_hash.data, "sha256" )
            user=Users(username=formulario.username.data,name=formulario.name.data, email=formulario.email.data, about_me=formulario.about_me.data, password_hash=hashed_pw)
            db.session.add(user)
            db.session.commit()
        formulario.name.data=''    
        formulario.username.data=''    
        formulario.email.data='' 
        formulario.password_hash.data='' 
        flash("Usuario ha sido creado")
        return render_template("auth/login.html")
    return render_template("auth/sign.html", form=formulario)