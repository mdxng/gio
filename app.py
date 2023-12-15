from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
import forms

app = Flask(__name__)  

app.config.from_mapping(
    SECRET_KEY = 'secret_key_just_for_dev_environment',
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
    return 'This is the login page'

# settings page

@app.route('/settings/')
def settings():
    return render_template('settings.html')

#event page

@app.route('/event/', methods=['GET', 'POST'])
def event():
    form = forms.CreateEventForm()
    todo_form = forms.ToDoForm()
    comment_form = forms.CommentForm()
    if request.method == 'GET':
        return render_template('event.html', event=event, form=form, todo_form=todo_form, comment_form=comment_form)
    else:
        if form.validate():
            flash('Event created', 'success')
        if todo_form.validate():
            flash('To Do added', 'success')
        if comment_form.validate(): 
            flash('Comment added', 'success')
        else:
            flash('Error','warning')
        return redirect(url_for('event'))
        




