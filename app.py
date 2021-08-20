from flask import *

app = Flask(__name__)

topics = [
    {
        "name":"q/questions",
    },

    {
        "name":"r/reality",
    },

    {
        "name":"m/magic",
    },
]

@app.route('/')
def main():
    return render_template('index.html', topics = topics)

@app.route('/home/<name>')
def home(name):
    return "<h1>Welcome Back " + name + "</h1>"

@app.route('/<bio>/<name>')
def bio(bio, name):
    return render_template('bio.html', bio = bio, name = name)

if __name__ == "__main__":
    app.run(debug=True)
