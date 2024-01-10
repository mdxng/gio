from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5

app = Flask(__name__)  

app.config.from_mapping(
    BOOTSTRAP_BOOTSWATCH_THEME = 'lux'  
)

bootstrap = Bootstrap5(app)


# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle the form submission (login logic) here
        return redirect(url_for('home'))
    else:
        # Handle GET request (render the login form)
        return render_template('login.html')

#register page

@app.route('/register/')
def register():
    return render_template('register.html')
    

   # home page 
# Change the route for the home page to '/home'
@app.route('/home')
def home():
    return render_template('home.html')

# Set the root URL to redirect to the home page
@app.route('/')
def index():
    return redirect(url_for('home'))



# settings page

@app.route('/settings/')
def settings():
    return render_template('settings.html')

#event page

@app.route('/event/')
def event():
    return render_template('event.html')

if __name__ == '__main__':
    app.run(debug=True)
