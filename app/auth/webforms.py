from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length, Email
from flask_wtf.file import FileField



class UserForm(FlaskForm):
    name=StringField("Name", validators=[DataRequired()])
    username=StringField("Username", validators=[DataRequired()])
    email=StringField("Email", validators=[DataRequired(), Email()])
    about_me=TextAreaField("About me")
    password_hash= PasswordField("Password",validators=[DataRequired(), EqualTo('password_hash2', message='Password must match!')])
    password_hash2= PasswordField("Confirm password",validators=[DataRequired()])
    submit=SubmitField("Submit") 