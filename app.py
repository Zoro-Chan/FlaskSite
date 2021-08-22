from FlaskSite import app
from random import randint

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=randint(2000, 9000))
