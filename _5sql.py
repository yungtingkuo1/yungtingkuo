from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.sqlite3"
db = SQLAlchemy(app)

class Balance(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    balance = db.Column(db.Integer, nullable = False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), unique = True, nullable = False)
    quantity = db.Column(db.Float, nullable = False)

class History(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    entry = db.Column(db.String(255), nullable = False)


with app.app_context():
    db.create_all()


# http://127.0.0.1:5000/
@app.route("/")
def main_page():
    products = db.session.query(Product).all()
    balance = db.session.query(Balance).first()

    if not balance:
        balance = Balance(balance=0)
        db.session.add(balance)
        db.session.commit()

    return render_template("_1html.html", products=products, balance=balance)


# http://127.0.0.1:5000/purchaseform
@app.route("/purchaseform", methods=["GET", "POST"])
def purchase():
    if request.method == "POST":
        # load data from file
      
        # request.form.get("<name>")
        product_name = request.form.get("name")
        product_price = float(request.form.get("price"))
        product_quantity = float(request.form.get("quantity"))

        balance_data = db.session.query(Balance).first()
        db_product = db.session.query(Product).filter(Product.name == product_name).first()

        if balance_data.balance < product_price * product_quantity:
            print("Not enough funds.")
            return redirect(url_for("purchase"))

        if not db_product:
            db_product = Product(name = product_name , quantity = 0)
        db_product.quantity += product_quantity

        balance_data.balance -= product_price * product_quantity

        history = History(
            entry=f"Buying {product_quantity} pcs. of {product_name} for {product_price} a pcs."
        )

        db.session.add(balance_data)
        db.session.add(db_product)
        db.session.add(history)
        db.session.commit()

        return redirect(url_for("purchase"))
    return render_template("purchaseform.html")


# http://127.0.0.1:5000/saleform
@app.route("/saleform", methods=["GET", "POST"])
def sale():
    if request.method == "POST":

        product_name = request.form.get("name")
        product_price = float(request.form.get("price"))
        product_quantity = float(request.form.get("quantity"))

        balance_data = db.session.query(Balance).first()
        db_product = db.session.query(Product).filter(Product.name == product_name).first()

        if db_product.quantity < product_quantity:
            print("Not enough items.")
            return redirect(url_for("sale"))

        db_product.quantity -= product_quantity

        balance_data.balance += product_price * product_quantity

        history = History(
            entry=f"Selling {product_quantity} pcs. of {product_name} for {product_price} a pcs."
        )

        db.session.add(balance_data)
        db.session.add(db_product)
        db.session.add(history)
        db.session.commit()

        return redirect(url_for("sale"))
    return render_template("saleform.html")


# http://127.0.0.1:5000/balancechangeform
@app.route("/balancechangeform", methods=["GET", "POST"])
def balance():
    if request.method == "POST":

        balance_data = db.session.query(Balance).first()

        amount = float(request.form.get("amount"))
        if balance_data.balance + amount < 0:
            print("Not allowed to take a loan.")
            return redirect(url_for("balance"))

        balance_data.balance += amount
        history = History(entry=f"Changing the account balance by: {amount}")

        db.session.add(balance_data)
        db.session.add(history)
        db.session.commit()

        return redirect(url_for("balance"))
    return render_template("balancechangeform.html")


@app.route("/history")
@app.route("/history/<int:start>/<int:stop>/")
def history(start=None, stop=None):
    history_data = db.session.query(History).all()
    return render_template("history.html", history=history_data[start:stop])


if __name__ == "__main__":
    app.run(debug=True)
