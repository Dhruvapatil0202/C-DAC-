
from flask import render_template, request
from flask import Flask
import pandas as pd
import numpy as np

csv_data_adder = Flask(__name__)
CSV_FILEPATH = r"C:\Users\DAI.STUDENTSDC\Desktop\DAI 2024\Submission\Dhruva\Advanced Computing in python\240840128026_Day14_python\temp_csv.csv"

@csv_data_adder.route("/")
def render_start_page():
    return render_template("data_addition_homepage.html")

@csv_data_adder.route("/add_data", methods = ["POST"])
def data_receiver_and_adder():
    name = request.form.get("name")
    age = request.form.get("age")
    contact_number = request.form.get("contact_number")

    df = pd.read_csv(CSV_FILEPATH)

    # df.loc[len(df)] = np.array(record) # Can be used, not preferred

    df = pd.concat([df, pd.DataFrame({'name': [name], 'age': [age], 'contact': [contact_number]})], axis = 0)
    df.to_csv(CSV_FILEPATH, index = False)

    html_text = """
    <h1>The record has been added Successfully</h1><br><br>
    <a href = '/'><button>Add More Records</button></a>
    """

    return html_text, 200

if __name__ == "__main__":
    csv_data_adder.run(debug = True)