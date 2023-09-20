from _9import1 import load_file, save_file
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
import json


app = Flask(__name__)

INVENTORY_FILE = "inventory.txt"
HISTORY_FILE = "history.txt"
BALANCE_FILE = "balance.txt"


# http://127.0.0.1:5000/
@app.route("/")
def main_page():
    inventory_data = load_file(INVENTORY_FILE, {})
    balance_data = load_file(BALANCE_FILE, 0)

    return render_template("_1html.html", inventory=inventory_data, balance=balance_data)


# http://127.0.0.1:5000/purchaseform
@app.route("/purchaseform", methods=["GET", "POST"])
def purchase():
    if request.method == "POST":
        # load data from file
        inventory_data = load_file(INVENTORY_FILE, {})
        balance_data = load_file(BALANCE_FILE, 0)
        history_data = load_file(HISTORY_FILE, [])

        # request.form.get("<name>")
        product_name = request.form.get("name")
        product_price = float(request.form.get("price"))
        product_quantity = float(request.form.get("quantity"))

        if balance_data < product_price * product_quantity:
            print("Not enough funds.")
            return redirect(url_for("purchase"))

        if product_name not in inventory_data:
            inventory_data[product_name] = 0
        inventory_data[product_name] += product_quantity

        balance_data -= product_price * product_quantity

        history_data.append(
            f"Buying {product_quantity} pcs. of {product_name} for {product_price} a pcs."
        )

        save_file(INVENTORY_FILE, inventory_data)
        save_file(BALANCE_FILE, balance_data)
        save_file(HISTORY_FILE, history_data)

        return redirect(url_for("purchase"))
    return render_template("purchaseform.html")


# http://127.0.0.1:5000/saleform
@app.route("/saleform", methods=["GET", "POST"])
def sale():
    if request.method == "POST":
        # load data from file
        inventory_data = load_file(INVENTORY_FILE, {})
        balance_data = load_file(BALANCE_FILE, 0)
        history_data = load_file(HISTORY_FILE, [])

        product_name = request.form.get("name")
        product_price = float(request.form.get("price"))
        product_quantity = float(request.form.get("quantity"))

        if inventory_data.get(product_name, 0) < product_quantity:
            print("Not enough items.")
            return redirect(url_for("sale"))

        inventory_data[product_name] -= product_quantity

        balance_data += product_price * product_quantity

        history_data.append(
            f"Selling {product_quantity} pcs. of {product_name} for {product_price} a pcs."
        )

        save_file(INVENTORY_FILE, inventory_data)
        save_file(BALANCE_FILE, balance_data)
        save_file(HISTORY_FILE, history_data)

        return redirect(url_for("sale"))
    return render_template("saleform.html")


# http://127.0.0.1:5000/balancechangeform
@app.route("/balancechangeform", methods=["GET", "POST"])
def balance():
    if request.method == "POST":
        balance_data = load_file(BALANCE_FILE, 0)
        history_data = load_file(HISTORY_FILE, [])

        amount = float(request.form.get("amount"))
        if balance_data + amount < 0:
            print("Not allowed to take a loan.")
            return redirect(url_for("balance"))

        balance_data += amount
        history_data.append(f"Changing the account balance by: {amount}")

        save_file(BALANCE_FILE, balance_data)
        save_file(HISTORY_FILE, history_data)

        return redirect(url_for("balance"))
    return render_template("balancechangeform.html")


@app.route("/history")
@app.route("/history/<int:start>/<int:stop>/")
def history(start=None, stop=None):
    history_data = load_file(HISTORY_FILE, [])
    return render_template("history.html", history=history_data[start:stop])


if __name__ == "__main__":
    app.run(debug=True)
