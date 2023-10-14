import time
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField


class PostForm(FlaskForm):
    form_id = HiddenField('Form ID', default=int(time.time()))
    title = StringField('Titulo', validators=[DataRequired()], render_kw={"autofocus":True})
    slug = StringField("Slug", validators=[DataRequired()])
    content = CKEditorField('Content', validators=[DataRequired()])
    submit = SubmitField("Submit")