from flask import render_template, request, redirect, url_for
from flask import Flask
# 1. Initialize flask app
appLogin = Flask(__name__)

# 2. Route for login page
@appLogin.route('/')
def login():
    return render_template('login.html')

# 3. Route to handle the login form submission
@appLogin.route('/login', methods = ['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']

    # 4. Simple username and password authentication
    if username =='admin' and password == 'password':
        # return f"welcome, {username}!"
        return redirect(url_for('show_dashboard'))
    else:
        return "Invalid credentials. Please try again"
    return "<h1>Welcome to the homepage!</h1>" # The textual file that will be returned to the web UI or browser.

@appLogin.route('/dashboard')
def show_dashboard():
    return render_template("dashboard.html")

if __name__ == '__main__':
    appLogin.run(debug = True)  # default port = 5000, debug = True provides opportunity to debug the application on the go.
