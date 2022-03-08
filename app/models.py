from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Post(db.Model):
    _tablename_ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    category = db.Column(db.String)
    content = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment = db.relationship('Comment', backref='post', lazy='dynamic')
    upvote = db.relationship('Upvote',backref='post',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='post',lazy='dynamic')

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    def _repr_(self):
        return f'Post {self.title}'


