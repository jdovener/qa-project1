from flask import Flask, render_template, request, redirect, url_for
from application import app, db
from application.models import Product, Customer, Order, Payment
from datetime import date

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
    return redirect(url_for("products"))

@app.route("/update/<int:product_id>", methods=["PUT"])
def update(product_id):
    product = Product.query.filter_by(id=product_id).first()
    product.quantity = not product.quantity
    db.session.commit()
    return redirect(url_for("products"))

@app.route("/delete/<int:product_id>", methods=["PUT"])
def delete(product_id):
    product = Product.query.filter_by(id=product_id).first()
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for("products"))

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
    cust_id = int(request.form.get("cust_id"))
    product_id = int(request.form.get("product_id"))
    new_order = Order(date_ordered=date_ordered, total=total, order_status=False, cust_id=cust_id, product_id=product_id)
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
    cust_id = int(request.form.get("cust_id"))
    new_payment = Payment(account_number=account_number, sort_code=sort_code, exp_date=exp_date, cvv=cvv, cust_id=cust_id)
    db.session.add(new_payment)
    db.session.commit()
    return redirect(url_for("payments"))

@app.route("/delete_payment/<int:account_number>")
def delete_payment(account_number):
    payment = Payment.query.filter_by(account_number=account_number).first()
    db.session.delete(payment)
    db.session.commit()
    return redirect(url_for("payments"))