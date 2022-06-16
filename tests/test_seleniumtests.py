from selenium import webdriver
from flask_testing import LiveServerTestCase
from application import app, db
from application.models import Product, Customer, Order, Payment

class TestBase(LiveServerTestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
        return app

    def setUp(self):
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless') # must be headless

        self.driver = webdriver.Chrome(options=chrome_options, executable_path='/snap/bin/chromium.chromedriver') 

        db.create_all() # create schema before we try to get the page
        db.session.commit()
        self.driver.get(f'http://localhost:5000/')

    def tearDown(self):
        self.driver.quit()
        db.drop_all()

# Nav Bar buttons tests

class TestNavBarButtons(TestBase):
    def test_navbar_buttons(self):
        self.driver.get(f'http://localhost:5000/')

        self.driver.find_element_by_xpath('/html/body/nav/div/a[1]').click() # Home button test
        assert self.driver.current_url == 'http://localhost:5000/'

        self.driver.find_element_by_xpath('/html/body/nav/div/a[2]').click() # Products button test
        assert self.driver.current_url == 'http://localhost:5000/products'

        self.driver.find_element_by_xpath('/html/body/nav/div/a[3]').click() # Customers button test
        assert self.driver.current_url == 'http://localhost:5000/customers'

        self.driver.find_element_by_xpath('/html/body/nav/div/a[4]').click() # Orders button test
        assert self.driver.current_url == 'http://localhost:5000/orders'

        self.driver.find_element_by_xpath('/html/body/nav/div/a[5]').click() # Payment Details button test
        assert self.driver.current_url == 'http://localhost:5000/payment_details'
        
# Products page tests

class TestProductsPage(TestBase):
    def test_products_page(self):
        self.driver.get(f'http://localhost:5000/products') # go to products route

        element1 = self.driver.find_element_by_xpath('/html/body/div[3]/form/div/input[1]') # Set up an object for the text input box
        element2 = self.driver.find_element_by_xpath('/html/body/div[3]/form/div/input[2]') # Set up an object for the text input box          
        element3 = self.driver.find_element_by_xpath('/html/body/div[3]/form/div/input[3]') # Set up an object for the text input box          
        element1.send_keys('pancakes') # enter text into input box
        element2.send_keys('pancakes') # enter text into input box
        element3.send_keys('10') # enter text into input box

        self.driver.find_element_by_xpath('/html/body/div[3]/form/div/button').click() # Click submit button
        assert self.driver.current_url == 'http://localhost:5000/products'

        self.driver.find_element_by_xpath('/html/body/div[4]/a[1]').click() # Update button test
        assert self.driver.current_url == 'http://localhost:5000/products'

        self.driver.find_element_by_xpath('/html/body/div[4]/a[2]').click() # Delete button test
        assert self.driver.current_url == 'http://localhost:5000/products'

# Customers page tests

class TestCustomersPage(TestBase):
    def test_customers_page(self):
        self.driver.get(f'http://localhost:5000/customers') # go to customers route

        element1 = self.driver.find_element_by_xpath('/html/body/div[3]/form/div/input[1]') # Set up an object for the text input box
        element2 = self.driver.find_element_by_xpath('/html/body/div[3]/form/div/input[2]') # Set up an object for the text input box          
        element3 = self.driver.find_element_by_xpath('/html/body/div[3]/form/div/input[3]') # Set up an object for the text input box          
        element4 = self.driver.find_element_by_xpath('/html/body/div[3]/form/div/input[4]') # Set up an object for the text input box          
        element5 = self.driver.find_element_by_xpath('/html/body/div[3]/form/div/input[5]') # Set up an object for the text input box          
        element6 = self.driver.find_element_by_xpath('/html/body/div[3]/form/div/input[6]') # Set up an object for the text input box          
        element1.send_keys('pancakes') # enter text into input box
        element2.send_keys('pancakes') # enter text into input box
        element3.send_keys('pancakes') # enter text into input box
        element4.send_keys('pancakes') # enter text into input box
        element5.send_keys('AA18AA') # enter text into input box
        element6.send_keys('07123456789') # enter number into input box

        self.driver.find_element_by_xpath('/html/body/div[3]/form/div/button').click() # Click submit button
        assert self.driver.current_url == 'http://localhost:5000/customers'

        self.driver.find_element_by_xpath('/html/body/div[4]/a[1]').click() # Delete button test
        assert self.driver.current_url == 'http://localhost:5000/customers'

# Orders page tests

class TestOrdersPage(TestBase):
    def test_orders_page(self):
        self.driver.get(f'http://localhost:5000/orders') # go to orders route

        element1 = self.driver.find_element_by_xpath('/html/body/div[3]/form/div/input[1]') # Set up an object for the text input box
        element2 = self.driver.find_element_by_xpath('/html/body/div[3]/form/div/input[2]') # Set up an object for the text input box          
        element3 = self.driver.find_element_by_xpath('/html/body/div[3]/form/div/input[3]') # Set up an object for the text input box          
        element4 = self.driver.find_element_by_xpath('/html/body/div[3]/form/div/input[4]') # Set up an object for the text input box                  
        element1.send_keys('01-01-2022') # enter text into input box
        element2.send_keys('10') # enter text into input box
        element3.send_keys('1') # enter text into input box
        element4.send_keys('1') # enter text into input box

        self.driver.find_element_by_xpath('/html/body/div[3]/form/div/button').click() # Click submit button
        assert self.driver.current_url == 'http://localhost:5000/orders'

        self.driver.find_element_by_xpath('/html/body/div[4]/a[1]').click() # Update button test
        assert self.driver.current_url == 'http://localhost:5000/orders'

        self.driver.find_element_by_xpath('/html/body/div[4]/a[2]').click() # Delete button test
        assert self.driver.current_url == 'http://localhost:5000/orders'

# Payment details page tests

class TestPaymentDetailsPage(TestBase):
    def test_paymentdetails_page(self):
        self.driver.get(f'http://localhost:5000/payment_details') # go to payment details route

        element1 = self.driver.find_element_by_xpath('/html/body/div[3]/form/div/input[1]') # Set up an object for the text input box
        element2 = self.driver.find_element_by_xpath('/html/body/div[3]/form/div/input[2]') # Set up an object for the text input box          
        element3 = self.driver.find_element_by_xpath('/html/body/div[3]/form/div/input[3]') # Set up an object for the text input box          
        element4 = self.driver.find_element_by_xpath('/html/body/div[3]/form/div/input[4]') # Set up an object for the text input box                  
        element5 = self.driver.find_element_by_xpath('/html/body/div[3]/form/div/input[5]') # Set up an object for the text input box                  
        element1.send_keys('00000001') # enter text into input box
        element2.send_keys('123456') # enter text into input box
        element3.send_keys('01-01-2022') # enter text into input box
        element4.send_keys('111') # enter text into input box
        element5.send_keys('1') # enter text into input box

        self.driver.find_element_by_xpath('/html/body/div[3]/form/div/button').click() # Click submit button
        assert self.driver.current_url == 'http://localhost:5000/payment_details'

        self.driver.find_element_by_xpath('/html/body/div[4]/a').click() # Delete button test
        assert self.driver.current_url == 'http://localhost:5000/payment_details'