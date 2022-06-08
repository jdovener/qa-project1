from application import app, db
from flask import url_for
from flask_testing import TestCase
from application.models import Product, Customer, Order, Payment

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            SQLALCHEMY_TRACK_MODIFICATIONS = False,
            SECRET_KEY = 'test secret key',
            WTF_CSRF_ENABLED = False
        )
        return app

    def setUp(self):
        test1 = Product(title="producta")
        test2 = Customer(f_name="Earl")
        test3 = Order(total=10)
        test4 = Payment(account_number=11111111)
        db.create_all()
        db.session.add(test1)
        db.session.add(test2)
        db.session.add(test3)
        db.session.add(test4)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

# Index route test

class TestViewIndex(TestBase):
    def test_get_index(self):
        response = self.client.get(url_for('index'))
        self.assert200(response)

# Product routes tests

class TestViewProduct(TestBase):
    def test_get_product(self):
        response = self.client.get(url_for('products'))
        self.assert200(response)
        self.assertIn(b'producta', response.data)

class TestAddProduct(TestBase):
    def test_post_product(self):
        response = self.client.post(url_for('add'),
        data = dict(title="pancakes"),
        follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'pancakes', response.data)

class TestUpdateProduct(TestBase):
    def test_put_product(self):
        response = self.client.put(url_for('update', product_id=1),
        data = dict(title="pancakes"),
        follow_redirects = True
        )
        assert response.status_code == 405

class TestDeleteProduct(TestBase):
    def test_delete_product(self):
        response = self.client.delete(url_for('delete', product_id=1)
        )
        assert response.status_code == 302

# Customer routes tests

class TestViewCustomer(TestBase):
    def test_get_customer(self):
        response = self.client.get(url_for('customers'))
        self.assert200(response)
        self.assertIn(b'Earl', response.data)

class TestAddCustomer(TestBase):
    def test_post_pcustomer(self):
        response = self.client.post(url_for('add_cust'),
        data = dict(f_name="Earl"),
        follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Earl', response.data)

class TestDeleteCustomer(TestBase):
    def test_delete_customer(self):
        response = self.client.delete(url_for('delete_cust', customer_id=1)
        )
        assert response.status_code == 302

# Orders routes tests

class TestViewOrder(TestBase):
    def test_get_order(self):
        response = self.client.get(url_for('orders'))
        self.assert200(response)
        self.assertIn(b'10', response.data)

class TestAddOrder(TestBase):
    def test_post_order(self):
        response = self.client.post(url_for('add_order'),
        data = dict(total=10),
        follow_redirects = True
        )
        self.assert500(response)
        test_order = Order.query.filter_by(total=10).first()
        assert test_order.total == 10

# class TestUpdateOrder(TestBase):
#     def test_put_order(self):
#         response = self.client.put(url_for('update_order', order_id=1),
#         data = dict(total="pancakes"),
#         follow_redirects = True
#         )
#         self.assert200(response)

# class TestDeleteOrder(TestBase):
#     def test_delete_order(self):
#         response = self.client.delete(url_for('delete_order', order_id=1)
#         )
#         self.assert405(response)

# Payment details routes tests

# class TestViewPayment(TestBase):
#     def test_get_payment(self):
#         response = self.client.get(url_for('payment_details'))
#         self.assert200(response)
#         self.assertIn(b'11111111', response.data)

# class TestAddPayment(TestBase):
#     def test_post_payment(self):
#         response = self.client.post(url_for('add_payment'),
#         data = dict(account_number=11111111),
#         follow_redirects = True
#         )
#         self.assert500(response)
#         self.assertIn(b'11111111', response.data)

# class TestDeletePayment(TestBase):
#     def test_delete_payment(self):
#         response = self.client.delete(url_for('delete_payment', account_number=11111111)
#         )
#         self.assert405(response)