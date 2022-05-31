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
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)

@app.route('/')
def index():
    product_list = Product.query.all()
    print(product_list)
    return render_template('index.html', product_list=product_list)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    genre = request.form.get("genre")
    price = request.form.get("price")
    quantity = request.form.get("quantity")
    new_product = Product(title=title, genre=genre, price=price, quantity=quantity)
    db.session.add(new_product)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:product_id>")
def delete(product_id):
    product = Product.query.filter_by(id=product_id).first()
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)