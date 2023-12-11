from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

#home  

bootstrap = Bootstrap5(app)

@app.route('/')
def index():
    return render_template('home.html')

#register page

@app.route('/register/')
def register():
    return render_template('register.html')

# login page

@app.route('/login/')
def login():
    return 'This is the login page'

# settings page

@app.route('/settings/<int:id>')
def usersettings(id):
    return render_template('settings.html')
