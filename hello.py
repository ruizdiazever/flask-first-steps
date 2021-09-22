from flask import Flask, url_for, request
from markupsafe import escape

app = Flask(__name__)



# First examples

@app.route('/')
def helloWorld():
    return 'Hello, World!'

@app.route("/escape/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/ever")
def ever():
    return f"Hello, my name is Ever. I'm 28 years old, father of Sofia, in my home 'Picucu!'."


# https://flask.palletsprojects.com/en/2.0.x/quickstart/#variable-rules

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


# https://flask.palletsprojects.com/en/2.0.x/quickstart/#unique-urls-redirection-behavior

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


# https://flask.palletsprojects.com/en/2.0.x/quickstart/#url-building

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


# https://flask.palletsprojects.com/en/2.0.x/quickstart/#http-methods

from flask import request

def do_the_login():
    return "Test login"
def show_the_login_form():
    return "Test form login"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == '__main__':
    app.run()