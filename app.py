from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    genre = db.Column(db.String(100))
    price = db.Column(db.Float)
    quantity = db.Column(db.Boolean)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(30))
    l_name = db.Column(db.String(30))
    email = db.Column(db.String(50))
    address = db.Column(db.String(100))
    postcode = db.Column(db.String(100))
    phone = db.Column(db.String(20))

# Homepage routes

@app.route('/')
def index():
    product_list = Product.query.all()
    print(product_list)
    return render_template('index.html', product_list=product_list)

# Products ADD PAGE ROUTE

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    genre = request.form.get("genre")
    price = request.form.get("price")
    quantity = request.form.get("quantity")
    new_product = Product(title=title, genre=genre, price=price, quantity=True)
    db.session.add(new_product)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/update/<int:product_id>")
def update(product_id):
    product = Product.query.filter_by(id=product_id).first()
    product.quantity = not product.quantity
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:product_id>")
def delete(product_id):
    product = Product.query.filter_by(id=product_id).first()
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for("index"))

# Customers routes

@app.route('/customers')
def customers():
    cust_list = Customer.query.all()
    print(cust_list)
    return render_template('customers.html', cust_list=cust_list)

@app.route("/add_cust", methods=["POST"])
def add_cust():
    f_name = request.form.get("f_name")
    l_name = request.form.get("l_name")
    email = request.form.get("email")
    address = request.form.get("address")
    postcode = request.form.get("postcode")
    phone = request.form.get("phone")
    new_customer = Customer(f_name=f_name, l_name=l_name, email=email, address=address, postcode=postcode, phone=phone)
    db.session.add(new_customer)
    db.session.commit()
    return redirect(url_for("customers"))

@app.route("/update_cust/<int:customer_id>")
def update_cust(customer_id):
    customer = Customer.query.filter_by(id=customer_id).first()
    db.session.commit()
    return redirect(url_for("customers"))

@app.route("/delete_cust/<int:customer_id>")
def delete_cust(customer_id):
    customer = Customer.query.filter_by(id=customer_id).first()
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for("customers"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)