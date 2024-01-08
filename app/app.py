from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my app!</h1>'

@app.route('/<username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'