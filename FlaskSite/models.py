from FlaskSite import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False, default='Anonymous')
    email = db.Column(db.String(999), unique=True, nullable=False, default='anon@anon.com')
    image_file = db.Column(db.String(20), nullable=False, default='anonymous.png')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"Username: {self.username}, Email: {self.email}, Profile: {self.image_file}"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=True)
    date_posted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    content = db.Column(db.String(2000), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"title: {self.title}, Date: {self.date_posted}"