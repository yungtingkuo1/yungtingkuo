from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from database import load_database
from database import save_database


app= Flask(__name__)

# http://127.0.0.1:5000/
@app.route("/")
def main_page():
    return render_template("_1html.html")

#http://127.0.0.1:5000/purchaseform
@app.route("/purchaseform")
def purchase():
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