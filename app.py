from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5

app = Flask(__name__)  

app.config.from_mapping(
    BOOTSTRAP_BOOTSWATCH_THEME = 'lux'  
)

bootstrap = Bootstrap5(app)

# home page

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
    return render_template('login.html')

# settings page

@app.route('/settings/')
def settings():
    return render_template('settings.html')

#event page

@app.route('/event/')
def event():
    return render_template('event.html')
