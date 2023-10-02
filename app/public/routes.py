from flask import render_template, flash, redirect, url_for
from ..extensions import db
from .webforms import PostForm
from app.model import Posts
# from . import db
from . import public_bp

@public_bp.route("/")
def index():
    return render_template("public/index.html")

@public_bp.route("/addPost", methods=['GET', 'POST'])
def addPost():
    form = PostForm()
    if form.validate_on_submit():
        post = Posts(title=form.title.data, content=form.content.data,slug=form.slug.data)
        form.title.data = ''
        form.content.data = ''
        form.slug.data = ''
        #Add post data to database:
        db.session.add(post)
        db.session.commit()
        flash("Blog Post Submitted Successfully!")
        return redirect(url_for('public.index'))              
    return render_template("public/addPost.html", form=form)