
from flask import render_template, request
from flask import Flask
import pandas as pd
import tabulate

# TEMP = "C:\Users\DAI.STUDENTSDC\Desktop\DAI 2024\Day14\pandas_and_flask\INDO.csv"



csv_describer_app = Flask(__name__)

@csv_describer_app.route('/')
def csv_home_screen():

    return render_template("home_page.html")

@csv_describer_app.route('/csv_data', methods = ["POST"])
def csv_data_generator():

    filepath = request.form.get('filepath')
    try:
        df = pd.read_csv(filepath)

        out = df.describe()

        temp = []
        indices = ['index'] + out.columns.to_list()
        for index, row in out.iterrows():
            temp.append([index] + row.to_list())

        ret_table = tabulate.tabulate(temp, headers= indices, tablefmt = 'html')
        ret_table2 = ret_table.replace('\n', '<br>')
        out_text = "<br><br><a href = \'/\'><button>Go back</button></a>"
        return ret_table2 + out_text, 200

    except Exception as error:
        print(error)
        return f"An Error occurred: {error}", 200


if __name__ == "__main__":
    csv_describer_app.run(debug = True)
