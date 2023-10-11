from flask import render_template,request, flash, redirect, url_for, session
from ..extensions import db
from .webforms import PostForm
from app.model import Posts
# from . import db
from . import public_bp
import time

@public_bp.route("/")
def index():
    posts=Posts.query.order_by(Posts.date_posted)
    return render_template("public/index.html", publicaciones=posts)

@public_bp.route("/addPost", methods=['GET', 'POST'])
def addPost():
    form = PostForm()
    if form.validate_on_submit():
        # Verificar el identificador único para evitar envíos duplicados
        form_id = request.form['form_id']
        if form_id != str(int(time.time())):
            post = Posts(title=form.title.data, content=form.content.data,slug=form.slug.data)
            form.title.data = ''
            form.content.data = ''
            form.slug.data = ''
            #Add post data to database:
            db.session.add(post)
            db.session.commit()
            flash("Blog Post Submitted Successfully!")
            response = redirect(url_for('public.index')) 
            response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            response.headers['Pragma'] = 'no-cache'
            response.headers['Expires'] = '0'
            return response
    return render_template("public/addPost.html", form=form)
@public_bp.route("/post<int:id>")
def post(id):
    post=Posts.query.get_or_404(id)
    return render_template('public/post.html', post=post)
@public_bp.route("/editPost<int:id>", methods=['GET','POST'])
def editPost(id):
    form=PostForm()
    post=Posts.query.get_or_404(id)
    if form.validate_on_submit():
        post.title=form.title.data
        post.slug=form.slug.data
        post.content=form.content.data
        db.session.add(post)
        db.session.commit()
        flash("Post ha sido actualizado")
        return redirect(url_for('public.post', id=id))
    else:
        form.title.data=post.title
        form.slug.data=post.slug
        form.content.data=post.content
        return render_template('public/editPost.html',form=form)
@public_bp.route("/deletePost<int:id>")
def deletePost(id):
    postDelete=Posts.query.get_or_404(id)
    try:
        db.session.delete(postDelete)
        db.session.commit()
        return redirect(url_for('public.index'))
    except:
            flash("Whoops! There was a problem deleting post")      
            #Grab all the posts from the databases:
            posts = Posts.query.order_by(Posts.date_posted)
            return render_template("public/posts.html", posts= posts)
#https://www.youtube.com/shorts/1bX0xVcoX5w
    
