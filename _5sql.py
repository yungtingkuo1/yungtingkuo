from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY-DATABASE-URI"] = "sqlite:///products.sqlite3"
db = SQLAlchemy(app)

class Product(db.Model):
    name = db.Column(db.String(120), unique = True, nullable = False)
    quantity = db.Column(db.Float, nullable = False)
    balance = db.Column(db.Float, nullable = False)
    history = db.Column(db.String(40))

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
        pb = request.form.get('product_balance')
        ph = request.form.get('pruduct_history')

        new_product = Product(
            name=pn,
            quantity=pq,
            balance=pb,
            history=ph
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
        product.balance = float(request.form.get("product_balance"))
        product.history = request.form.get("product_history")
        db.session.add(product)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit_product.html", product=product)