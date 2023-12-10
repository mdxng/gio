from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

#home 

@app.route('/')
def index():
    return render_template('home.html')

#register page

@app.route('/register/')
def register():
    return 'This is the register page'

# login page

@app.route('/login/')
def login():
    return 'This is the login page'

# settings page

@app.route('/settings/<int:id>')
def usersettings(id):
    return 'This is the settings page'
