from _3flask import load_data, save_data
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY-DATABASE-URI"] = "sqlite:///products.sqlite3"
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

inventory_data = load_data({})
balance_data = load_data(0)
history_data = load_data([])

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    all_products = db.session.query(Product).all()
    return render_template("index.html",products = all_products)

@app.route("/add_product/", method=["GET","POST"])
def add_product():
    if request.method == "POST":
        pn = request.form.get('product_name')
        pq = request.form.get('product_quantity')

        new_product = Product(
            name=pn,
            quantity=pq,
        )

        db.session.add(new_product)
        db.session.commit()

        return redirect(url_for("index"))
    return render_template("add_product.html")

@app.route("/edit_product/<idx>/", methods=["GET","POST"])
def edit_product(idx):
    product = db.session.query(Product).filter(Product.id == idx).first()
    if request.method == "POST":
        product.name = request.form.get("product_name")
        product.quantity = request.form.get("product_quantity")

        db.session.add(product)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit_product.html", product=product)


@app.route("/balancechangeform", methods=["GET", "POST"])
def balance():
    if request.method == "POST":
        balance_data = load_data(0)
        history_data = load_data([])

        amount = float(request.form.get("amount"))
        if balance_data + amount < 0:
            print("Not allowed to take a loan.")
            return redirect(url_for("balance"))

        balance_data += amount
        history_data.append(f"Changing the account balance by: {amount}")

        save_data(balance_data)
        save_data(history_data)

        return redirect(url_for("balance"))
    return render_template("balancechangeform.html")


@app.route("/history")
@app.route("/history/<int:start>/<int:stop>/")
def history(start=None, stop=None):
    history_data = load_data([])
    return render_template("history.html", history=history_data[start:stop])
