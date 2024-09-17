from flask import render_template, request, redirect, url_for
from flask import Flask

# 1. Initialize flask app
survey_app = Flask(__name__)

@survey_app.route('/')
def Home_page_function():
    return render_template('survey_home_page.html')

@survey_app.route('/survey_page')
def before_survey_page_function():
    return render_template("survey_page.html")

@survey_app.route("/result_page", methods = ['POST'])
def after_survey_page_function():
    # print(list(request.form.items()))
    name = request.form.get('name')
    age = request.form.get('age')
    email = request.form.get('email')
    city = request.form.get('city')

    # return f"Received data: Name: {name}, Age: {age}, Email: {email}, City: {city}", 200
    return render_template('result_page.html', name = name, age= age, email = email, city = city)
if __name__ == "__main__":
    # 2. Start app.
    survey_app.run(debug = True)