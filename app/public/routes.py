from flask import render_template,request, flash, redirect, url_for, session
from flask_login import login_required, current_user
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
@login_required
def addPost():
    form = PostForm()
    if form.validate_on_submit():
        # Verificar el identificador único para evitar envíos duplicados
        form_id = request.form['form_id']
        if form_id != str(int(time.time())):
            poster = current_user.id
            post = Posts(title=form.title.data, content=form.content.data,poster_id=poster,slug=form.slug.data)
            form.title.data = ''
            form.content.data = ''
            form.slug.data = ''
            #Add post data to database:
            db.session.add(post)
            db.session.commit()
            flash("Blog Post Submitted Successfully!")
            response = redirect(url_for('public.post', id=post.id)) 
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
@login_required
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
    if current_user.id == post.poster_id:
        form.title.data=post.title
        # form.author.data=post.author
        form.slug.data=post.slug
        form.content.data=post.content
        # return redirect(url_for('public.post', id=id, form=form))
        return render_template('public/editPost.html', form=form)
    else:
        flash("You Aren't Authorized to Edit This Post...")
        return redirect(url_for('public.post', id=id))
@public_bp.route("/deletePost<int:id>")
@login_required
def deletePost(id):
    postDelete=Posts.query.get_or_404(id)
    ide=current_user.id
    if ide== postDelete.poster.id:       
        try:
            db.session.delete(postDelete)
            db.session.commit()
            flash("¡Post fue eliminado...!")
            return redirect(url_for('public.index'))
        
        except:
                flash("Whoops! There was a problem deleting post")      
                #Grab all the posts from the databases:
                posts = Posts.query.order_by(Posts.date_posted)
                return render_template("public/posts.html", posts= posts)
    else:
        flash("You Aren't Authorized to Delete This Post")
        return redirect(url_for('public.post', id=id))
#https://www.youtube.com/shorts/1bX0xVcoX5w
    
