from flask import render_template, request, redirect,url_for
from flask import Flask

app_age = Flask(__name__)

# category

@app_age.route("/")
def home_page():
    return render_template("homepage_age.html")

@app_age.route("/result", methods = ["POST"])
def age_form():
    print("Yes")
    username = request.form["username"]
    age = int(request.form["age"])

    if age < 18:
        message = f"Hello {username}, your age is {age} and you come into minor category"
    else:
        message = f"Hello {username}, your age is {age} and you come into adult category"

    return redirect(url_for("results", message=message))


@app_age.route("/result")
def results(request):

    message = request.args.get("message", "No message provided")
    return message

if __name__ == "__main__":
    app_age.run(debug=True)



