from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# class definitions

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
    orders = db.relationship("Order", backref="customer")
    payments = db.relationship("Payment", backref="customer")

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_ordered = db.Column(db.Date)
    total = db.Column(db.Float)
    order_status = db.Column(db.Boolean)
    cust_id = db.Column(db.Integer, db.ForeignKey("customer.id"))

class Payment(db.Model):
    account_number = db.Column(db.Integer, primary_key=True)
    sort_code = db.Column(db.Integer)
    exp_date = db.Column(db.Date)
    cvv = db.Column(db.Integer)
    cust_id = db.Column(db.Integer, db.ForeignKey("customer.id"))

# Homepage route

@app.route('/')
def index():
    return render_template('index.html')

# Products routes

@app.route('/products')
def products():
    product_list = Product.query.all()
    print(product_list)
    return render_template('products.html', product_list=product_list)

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

@app.route("/delete_cust/<int:customer_id>")
def delete_cust(customer_id):
    customer = Customer.query.filter_by(id=customer_id).first()
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for("customers"))

# Orders routes

@app.route('/orders')
def orders():
    order_list = Order.query.all()
    print(order_list)
    return render_template('orders.html', order_list=order_list)

@app.route("/add_order", methods=["POST"])
def add_order():
    date_ordered = date(*map(int, request.form.get("date_ordered").split("-")))
    total = float(request.form.get("total"))
    order_status = request.form.get("order_status")
    new_order = Order(date_ordered=date_ordered, total=total, order_status=False)
    db.session.add(new_order)
    db.session.commit()
    return redirect(url_for("orders"))

@app.route("/update_order/<int:order_id>")
def update_order(order_id):
    order = Order.query.filter_by(id=order_id).first()
    order.order_status = not order.order_status
    db.session.commit()
    return redirect(url_for("orders"))

@app.route("/delete_order/<int:order_id>")
def delete_order(order_id):
    order = Order.query.filter_by(id=order_id).first()
    db.session.delete(order)
    db.session.commit()
    return redirect(url_for("orders"))

# Payment details routes

@app.route('/payment_details')
def payments():
    payment_list = Payment.query.all()
    print(payment_list)
    return render_template('payment_details.html', payment_list=payment_list)

@app.route("/add_payment", methods=["POST"])
def add_payment():
    account_number = request.form.get("account_number")
    sort_code = request.form.get("sort_code")
    exp_date = date(*map(int, request.form.get("exp_date").split("-")))
    cvv = request.form.get("cvv")
    new_payment = Payment(account_number=account_number, sort_code=sort_code, exp_date=exp_date, cvv=cvv)
    db.session.add(new_payment)
    db.session.commit()
    return redirect(url_for("payments"))

@app.route("/delete_payment/<int:account_number>")
def delete_payment(account_number):
    payment = Payment.query.filter_by(account_number=account_number).first()
    db.session.delete(payment)
    db.session.commit()
    return redirect(url_for("payments"))

# run app code

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)