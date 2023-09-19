from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import json


app= Flask(__name__)

def load_data():
    with open ("product.json","r") as f:
        data = json.load(f)
    return data

def save_data(data):
    with open ("product.json","r") as f:
        json.dump(data.f)

# http://127.0.0.1:5000/
@app.route("/")
def main_page():
    return render_template("_1html.html")

#http://127.0.0.1:5000/purchaseform
@app.route("/purchaseform")
def purchase():
    if request.method == "POST":  
    # load data from file
    data = load_data()
    # get data from form
    purchase_data = data.get(purchase)
    # request.form.get("<name>")
    product_name = request.form.get("product-input")
    product_price = request.form.get("product-price")
    product_quantity = request.form.get("product-qantity")
    # update stock
    new_product = (
        name = product_name,
        price = product_price,
        quantity = product_quantity,
    )
    # save stock
    save_data(data)
    return redirect("/purchaseform")
return render_template("purchaseform.html")

#http://127.0.0.1:5000/saleform
@app.route("/saleform")
def sale():
    return render_template("saleform.html")

#http://127.0.0.1:5000/balancechangeform
@app.route("/balancechangeform")
def balance():
    return render_template("balancechangeform.html")


@app.route("/history", methods=["GET","POST"])
def history():
    if request.method == "POST":
        purchase = request.form.get("purchase.html")
        sale = request.form.get("sale.html")
        balance = request.form.get("balance.html")

        data = load_database()

        save_database(data)
        return redirect("/history")

    return render_template("history.html")

if __name__ == "__main__":
    app.run()