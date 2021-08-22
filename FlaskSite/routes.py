from flask import render_template, flash, url_for, redirect
import FlaskSite
from FlaskSite import app, db, bcrypt
from FlaskSite.forms import JoinForm, LoginForm
from FlaskSite.models import User, Post
from flask_login import login_user


topics = [
    {
        "name":"questions",
        "slug":"q"
    },

    {
        "name":"reality",
        "slug":"r"
    },

    {
        "name":"magic",
        "slug":"m"
    },
]

@app.route('/')
def main():
    return render_template('index.html', topics = topics)

@app.route('/<slug>/<topic>')
def topic(topic, slug):
    return render_template('topicview.html', name=topic, slug=slug, title=f"{slug}/{topic}")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/join', methods=['GET', 'POST'])
def register():
    form = JoinForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Thanks for Joining! Proceed by logging in.",'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Join Us", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main'))
        else:
            flash("Login Unsuccessful, please check email and password", "danger")
    return render_template('login.html', title="Login", form=form)

@app.route('/faq')
def faq():
    return render_template('faq.html', title="FAQ & Rules")