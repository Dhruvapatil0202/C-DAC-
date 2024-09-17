
from flask import Flask
app = Flask(__name__)

@app.route('/')
def homePage():
    return "<h1>Welcome to the homepage!</h1>" # The textual file that will be returned to the web UI or browser.

if __name__ == '__main__':
    app.run(port = 5001, debug = True)  # default port = 5000, debug = True provides opportunity to debug the application on the go.
