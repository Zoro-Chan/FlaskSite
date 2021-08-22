from models import User, Post
from flask import render_template
from FlaskSite import app
from FlaskSite.forms import JoinForm, LoginForm
from FlaskSite.models import User, Post


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

@app.route('/join')
def register():
    form = JoinForm()
    return render_template('register.html', title="Join Us", form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)