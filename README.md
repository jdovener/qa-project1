# qa-project1 - 'QA Games Shop' App:  
This GitHub repository contains my deliverable files for the QA DevOps fundamental project.

## Contents:
* [Project Requirements](#Project-Requirements)  
* [Project Design](#Project-Design)
* [The App](#The-App)
* [Testing](#Testing) IMCOMPLETE
* [CI Pipeline](#CI-Pipeline) INCOMPLETE
* [Risk Assessment](#Risk-Assessment) INCOMPLETE
* [Updates](#Updates)
* [Known Issues](#Known-Issues)
* [Future Work](#Future-Work)

## Project Requirements:
* This project requirement to create an application of my choosing. The app must be created in Python and have full CRUD functionality. 
* A relational database must be used to store data persistently for the project, the database needs to have at least 2 tables which must have a relationship. 
* A Trello board must be used to lay out tasks to be completed throughout.
* The project must be displayed as a functioning front-end website using Flask.
* The code must be fully integrated into a Version Control System (I chose to use GitHub). This must utilise the Feature-Branch model and be built through a CI server and deployed to a cloud-based virtual machine.
* Clear documentation must be made.

## Project Design:
The app I have chosen to build is a video games shop product and customer information tracking system. This would allow employees of the shop to: 
Add products, customer details, payment details and order details to a database (create functionality).
View products, customer details, payment details and order details in a database (read functionality).
Update specific products to show if they are in stock or out of stock, update order details to show if they are pending or delivered (update functionality).
Delete records of products, customer details and payment details from the database (delete functionality).
The database for the MVP of this project is comprised of 4 tables: Products, Customers, Orders, Payment details. The database features 2 one-to-many relationships. The ERD for this MVP is shown below:

![ERD]()

The structure was updated to include an 'email' field and 'postcode' field in the Customer table. The 'total' field in the Orders table was changed to 'price' as only one item can be added to an order. A 'product_id' field (a foreign key from the Products table) was also added to the Orders table. The current ERD is shown below:

![Current ERD]()

In the future, the app would ideally have the ability to add more than one product to each order, this would result in a small change to the ERD. The 'price' field in the Orders table would be changed to a 'total' field. The future ERD is shown below:

![Future ERD]()

# The App:
Upon opening the app, the user is presented with the homepage:

![Homepage]()

The user is able to use the nav bar which provides links to alternate pages. The product page is shown below:

---

![Products]()

The Products page shows all products currently entered into the database. On this page the user can: 
Add products by populating the forms at the bottom of the page and pressing the 'Add' button. 
Update the status of a product to 'In Stock' or 'Out of stock' by pressing the 'Update' button beneath each entry. This is represented by either a green label or a red label beneath the product entry.
Delete product entries by pressing the 'Delete' button beneath each entry.

---

The Customers page is shown below:

![Customers]()

The Customers page shows all customers currently entered into the database. On this page the user can: 
Add customers by populating the forms at the bottom of the page and pressing the 'Add' button. 
Delete customer entries by pressing the 'Delete' button beneath each entry.

---

The Orders page is shown below:

![Orders]()

The Orders page shows all orders currently entered into the database. On this page the user can: 
Add orders by populating the forms at the bottom of the page and pressing the 'Add' button. 
Update the status of an order to 'Pending' or 'Delivered' by pressing the 'Update' button beneath each entry. This is represented by either a yellow label or a green label beneath the product entry.
Delete product entries by pressing the 'Delete' button beneath each entry.

The 'Customer ID' field is a foreign key from the Customers table in the database, this must be populated with an existing ID present in the Customer table or the app will not allow entry.
The 'Product ID' field is a foreign key from the Products table in the database, this must be populated with an existing ID present in the Product table or the app will not allow entry.

---

The Payment Details page is shown below:

![Payment Details]()

The Payment Details page shows all customer payment details currently entered into the database. On this page the user can: 
Add customer payment details by populating the forms at the bottom of the page and pressing the 'Add' button. 
Delete customer payment details entries by pressing the 'Delete' button beneath each entry.

The 'Customer ID' field is a foreign key from the Customers table in the database, this must be populated with an existing ID present in the Customer table or the app will not allow entry.

# Testing

INCOMPLETE

# CI Pipeline

INCOMPLETE

# Risk Assesment

INCOMPLETE

# Updates

* 31/05/2022
    * Added Homepage, user will now be initially taken to Homepage instead of Products page.
    * Added nav bar to all pages.

* 01/06/2022
    * Added basic styling with Semantic UI.
    * Refactored code for general readability improvements.
    * New file structure. Refactored code to seperate models, routes and init file.
    * Began using GCP SQL database as opposed to sqlite database.
    * Minor bug fix on payment page. Customer ID field is now displaying.

# Known Issues

* If an entry is submitted on the Payment Details page with a customer id that is not currently present in the customer table, an error is thrown and the app does not redirect the user back automatically.
* Similarly to above issue: If an entry is submitted on the Orders page with a customer/product id that is not currently present in the customer/product table, an error is thrown and the app does not redirect the user back automatically.

# Future Work

If I were to recreate this app, in addition to fixing the current known issues, I would like to implement the following changes:

* Add the ability to update records in all tables without having to delete the entire entry and re-enter the updated information.
* Add drop down menus to various input fields to increase efficiency for the user and reduce the chance of spelling mistakes.
* Improve stylisation of displayed database entries for easier readability
* Add a max character limit to various input fields (such as the account number input field on the payment details page) to reduce the chance of errors.
* Add the ability to create orders with multiple products on the Orders page. The input fields would also feature drop down menus for adding products/customer information.