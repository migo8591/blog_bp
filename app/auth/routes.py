from flask import render_template, flash, redirect, url_for, session, request
from .webforms import UserForm, LoginForm
from ..model import Users
from ..extensions import db, bcrypt
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth_bp
from flask import jsonify


@auth_bp.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                flash("Login Successfull!!")
                return redirect(url_for('auth.dashboard'))
            else:
                flash("Wrong Password - Try Again!")
        else:
            flash("That User Doesn't Exist! Try Again...")        
    our_users = Users.query.order_by(Users.date_added)
    return render_template("auth/login.html",form =form, usuarios=our_users) 
@auth_bp.route("/sign", methods=['GET','POST'])
def sign():
    formulario= UserForm()
    if formulario.validate_on_submit():
        user=Users.query.filter_by(email=formulario.email.data).first()
        if user is None:
            hashed_pw=bcrypt.generate_password_hash(formulario.password_hash.data).decode('utf-8')
            user=Users(username=formulario.username.data,name=formulario.name.data, email=formulario.email.data, about_me=formulario.aboutme.data, password_hash=hashed_pw)
            db.session.add(user)
            db.session.commit()
        formulario.name.data=''    
        formulario.username.data=''    
        formulario.email.data='' 
        formulario.password_hash.data='' 
        flash("Usuario ha sido creado")
        return redirect(url_for('auth.login'))
    return render_template("auth/sign.html", form=formulario)

@auth_bp.route("/dashboard")
@login_required
def dashboard():
    # login_successful = session.pop('login_successful', False)
    login_successful = session.pop('login_successful', True)
    return render_template("auth/dashboard.html", login_successful=login_successful)

@auth_bp.route("/logout")
def logout():
    logout_user()
    flash("Closed Session...!")
    return redirect(url_for('auth.login'))

@auth_bp.route("/update/<int:id>", methods=['GET', 'POST'])
def update_user(id):
    usuario_to_update=Users.query.get_or_404(id)
    formulario = UserForm()
    if request.method == "POST":
        usuario_to_update.username = request.form['username']
        usuario_to_update.name = request.form['name']
        usuario_to_update.about_me = request.form['aboutme']
        # usuario_to_update.password = request.form['about_me'
        try:
            db.session.commit()
            flash("User update successfully")
            return redirect(url_for("auth.dashboard"))
        except:
            flash("Error! Looks like there was a problem...Try again!")
            return render_template("auth.update.html", form=formulario, user_to_update=usuario_to_update)
    else:
        return render_template("auth/update_user.html", form=formulario, user_to_update=usuario_to_update)
