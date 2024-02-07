from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from blinker import Namespace
from db import db, User

app = Flask(__name__)  

# Configure Flask-Bootstrap5
app.config.from_mapping(
    SECRET_KEY = 'secret_key_just_for_dev_environment',
    BOOTSTRAP_BOOTSWATCH_THEME = 'lux'  
)
bootstrap = Bootstrap5(app)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Define signals
signals = Namespace()
session_started_signal = signals.signal('session-started')
session_teardown_signal = signals.signal('session-teardown')

# Connect functions to signals
@session_started_signal.connect
def session_started(sender, app):
    print("Session started")

@session_teardown_signal.connect
def session_teardown(sender, app, exception=None):
    print("Session ended")

@app.before_request
def before_request():
    print(f"Current user: {request.remote_user}")
    print(f"Current page: {request.path}")


@app.after_request
def after_request(response):
    return response


# home page
@app.route('/')
def index():
    user_id = session.get('user_id')
    return render_template('home.html')

# register page
@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            print("Passwords do not match")
            return 'Passwords do not match'

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            print("Username already exists")
            return 'Username already exists'

        # Create new user
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        print("Registration successful")
        return redirect(url_for('login'))
    
    return render_template('register.html')

# login page
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            print("Login successful")
            return redirect(url_for('index'))
        else:
            print("Invalid username or password")
            return 'Invalid username or password'

    return render_template('login.html')

# settings page
@app.route('/settings/')
def settings():
   
    user_id = session.get('user_id')
    if user_id:
        user = User.query.get(user_id)
        return render_template('settings.html', user=user)  
    else:
        return 'You are not logged in'

# event page
@app.route('/event/')
def event():
    return render_template('event.html')

# Logout route
@app.route('/logout/')
def logout():
   
    session.clear()
 
    return redirect(url_for('login'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
