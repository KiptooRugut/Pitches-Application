from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from ..models import Comment, User, Post, Upvote, Downvote
from flask_login import login_required, current_user
from .. import db, photos
from .forms import UpdateProfile, PostForm, CommentForm
from flask_wtf.csrf import CSRFProtect, CSRFError

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''
    post_form = PostForm()
    all_posts = Post.query.order_by(Post.date_posted).all()
    return render_template('index.html', posts = all_posts)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user=user)


