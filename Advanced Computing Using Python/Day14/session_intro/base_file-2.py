from flask import render_template, request, redirect, url_for, session
from flask import Flask

# 1. Initialize flask app
product_track_app = Flask(__name__)
product_track_app.secret_key = 'secret'

@product_track_app.route('/')
def Home_screen_func():
    return render_template("home_screen.html")

@product_track_app.route("/order_details",  methods = ['POST'])
def order_details_func():
    quantity = request.form['quantity']
    product = request.form['product']

    session['name'] = (quantity, product)

    return render_template("shipping_details_screen.html",product = product, quantity = quantity)

@product_track_app.route("/order_summary", methods = ["POST"])
def order_display_func():
    product, quantity = session.get('name')
    name = request.form.get('name')
    address = request.form.get('address')
    contact_number = request.form.get('contact_number')

    return render_template("order_summary.html",
                           product = product,
                           quantity = quantity,
                           name = name,
                           address = address,
                           contact_number = contact_number)

@product_track_app.route("/order_confirmation")
def order_confirm_func():

    return render_template("order_confirmation.html")


if __name__ == "__main__":
    product_track_app.run(debug = True)

