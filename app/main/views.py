from . import main_blueprint
from flask import render_template, abort, redirect, url_for, flash, request
from flask_login import login_required, current_user
from ..requests import get_quotes
from ..models import Follower, User, Comments, Blogs
from .. import db
from .forms import UpdateProfile, CreatePost
import secrets
import os
from PIL import Image

@main_blueprint.route('/')
def home():
    return render_template('index.html')

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join('app/static/images', picture_filename)
    form_picture.save(picture_path)
    
    output_size = (200, 200)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_filename

@main_blueprint.route('/quotes')
def quotes():
    quotes = get_quotes()
    return render_template('quotes.html', quotes = quotes)


@main_blueprint.route('/profile',methods = ['POST','GET'])
@login_required
def profile():
    form = UpdateProfile()
    if form.validate_on_submit():
        if form.profile_picture.data:
            picture_file = save_picture(form.profile_picture.data)
            current_user.profile_pic_path = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.bio = form.bio.data
        db.session.commit()
        flash('Succesfully updated your profile')
        return redirect(url_for('main_blueprint.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.bio.data = current_user.bio
    profile_pic_path = url_for('static', filename='assets/'+'current_user.profile_pic_path') 
    return render_template('profile/profile.html',  form = form, profile_pic_path=profile_pic_path)

@main_blueprint.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/updateprofile.html',form =form)



@main_blueprint.route('/new_post', methods=['POST','GET'])
@login_required
def new_blog():
    followers = Follower.query.all()
    form = CreatePost()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        user_id =  current_user._get_current_object().id
        blog = Blogs(title=title,content=content,user_id=user_id)
        blog.save()
        # for subscriber in subscribers:
        #     mail_message("New Blog Post","email/new_blog",subscriber.email,blog=blog)
        flash('You Posted a new Blog')
        return redirect(url_for('main.index'))
    return render_template('newblog.html', form = form)


@main_blueprint.route('/blog/<id>')
def blog(id):
    comments = Comments.query.filter_by(blog_id=id).all()
    blog = Blogs.query.get(id)
    return render_template('blog.html',blog=blog,comments=comments)