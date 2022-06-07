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
        test2 = Product(title="productb")
        db.create_all()
        db.session.add(test1)
        db.session.add(test2)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

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
        self.assert200(response)
