from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Titulo', validators=[DataRequired()])
    slug = StringField("Slug", validators=[DataRequired()])
    content = TextAreaField("Contenido")
    submit = SubmitField("Submit")