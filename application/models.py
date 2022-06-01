from application import db

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
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))

class Payment(db.Model):
    account_number = db.Column(db.Integer, primary_key=True)
    sort_code = db.Column(db.Integer)
    exp_date = db.Column(db.Date)
    cvv = db.Column(db.Integer)
    cust_id = db.Column(db.Integer, db.ForeignKey("customer.id"))