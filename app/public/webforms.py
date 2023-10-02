import time
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    form_id = HiddenField('Form ID', default=int(time.time()))
    title = StringField('Titulo', validators=[DataRequired()])
    slug = StringField("Slug", validators=[DataRequired()])
    content = TextAreaField("Contenido")
    submit = SubmitField("Submit")