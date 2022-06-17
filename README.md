# qa-project1 - 'QA Games Shop' App:  
This GitHub repository contains my deliverable files for the QA DevOps fundamental project.  

## Contents:
* [Project Requirements](#Project-Requirements)
* [Project Design](#Project-Design)
* [Risk Assessment](#Risk-Assessment)
* [The App](#The-App)
* [Testing](#Testing)
* [CI Pipeline](#CI-Pipeline)
* [Updates](#Updates)
* [Known Issues](#Known-Issues)
* [Future Work](#Future-Work)

## Project Requirements:
* This project required me to create an application of my choosing. The app must be created in Python and have full CRUD functionality. 
* A relational database must be used to store data persistently for the project, the database needs to have at least 2 tables which must have a relationship. 
* A Trello board must be used to lay out tasks to be completed throughout.
* The project must be displayed as a functioning front-end website using Flask.
* The code must be fully integrated into a Version Control System (I chose to use GitHub). This must utilise the Feature-Branch model and be built through a CI server and deployed to a cloud-based virtual machine.
* Clear documentation must be made.

## Project Design:
The app I have chosen to build is a video games shop product and customer information tracking system. This would allow employees of the shop to:  
* Add products, customer details, payment details and order details to a database (create functionality).  
* View products, customer details, payment details and order details in a database (read functionality).  
* Update specific products to show if they are in stock or out of stock, update order details to show if they are pending or delivered (update functionality).  
* Delete records of products, customer details and payment details from the database (delete functionality).  
  
The database for the minimum viable product (MVP) of this project is comprised of 4 tables: Products, Customers, Orders, Payment details. The database features 2 one-to-many relationships.  
The ERD for this MVP is shown below:

![ERD](https://github.com/jdovener/qa-project1/blob/dev/images/ERD.png)

The structure was updated to include an 'email' field and 'postcode' field in the Customer table. The 'total' field in the Orders table was changed to 'price' as only one item can be added to an order. A 'product_id' field (a foreign key from the Products table) was also added to the Orders table.  
The current ERD is shown below:

![Current ERD](https://github.com/jdovener/qa-project1/blob/dev/images/Current%20ERD.png)

In the future, the app would ideally have the ability to add more than one product to each order, this would result in a small change to the ERD. The 'price' field in the Orders table would be changed to a 'total' field.  
The future ERD is shown below:

![Future ERD](https://github.com/jdovener/qa-project1/blob/dev/images/Future%20ERD.png)

A Trello board was created to list and organise the objectives of the project. The inital Trello board is shown below:

![Trello Board](https://github.com/jdovener/qa-project1/blob/dev/images/Trello%20Board.png)

This was referred to and updated throughout the creation and documentation of the project in order to ensure no objectives were missed.  

The trello board was updated to include Use Cases and User Stories, a screen shot of these columns are shown below. The trello board can be accessed [HERE](https://trello.com/b/t1pViKWS/qa-project-1-trello) for in-depth viewing.

![Use User](https://github.com/jdovener/qa-project1/blob/dev/images/Use%20User.png)

# Risk Assessment

Prior to beginning the project, a risk assessment was carried out. This was used to identify potential hazards, consider their implications and propose control measures for preventing/solving them. The risk assessment is shown below:

![Risk Assessment](https://github.com/jdovener/qa-project1/blob/dev/images/Risk%20Assessment.png)

The outlined control measures were implemented during the creation of the project.  
The key included in the image explains the probability, impact and priority level of the potential hazards.

# The App:
Upon opening the app, the user is presented with the homepage:

![Homepage](https://github.com/jdovener/qa-project1/blob/dev/images/Homepage.png)

The user is able to use the nav bar which provides links to alternate pages. The product page is shown below:

---

![Products](https://github.com/jdovener/qa-project1/blob/dev/images/Products.png)

The Products page shows all products currently entered into the database. On this page the user can:  
* Add products by populating the forms at the bottom of the page and pressing the 'Add' button.  
* Update the status of a product to 'In Stock' or 'Out of stock' by pressing the 'Update' button beneath each entry. This is represented by either a green label or a red label beneath the product entry.  
* Delete product entries by pressing the 'Delete' button beneath each entry.

---

The Customers page is shown below:

![Customers](https://github.com/jdovener/qa-project1/blob/dev/images/Customers.png)

The Customers page shows all customer information currently entered into the database. On this page the user can:  
* Add customers by populating the forms at the bottom of the page and pressing the 'Add' button.  
* Delete customer entries by pressing the 'Delete' button beneath each entry.

---

The Orders page is shown below:

![Orders](https://github.com/jdovener/qa-project1/blob/dev/images/Orders.png)

The Orders page shows all orders currently entered into the database. On this page the user can:  
* Add orders by populating the forms at the bottom of the page and pressing the 'Add' button.  
    * The 'Customer ID' field is a foreign key from the Customers table in the database, this MUST be populated with an existing ID present in the Customer table or the app will not allow entry.  
    * The 'Product ID' field is a foreign key from the Products table in the database, this MUST be populated with an existing ID present in the Product table or the app will not allow entry.
* Update the status of an order to 'Pending' or 'Delivered' by pressing the 'Update' button beneath each entry. This is represented by either a yellow label or a green label beneath the product entry.  
* Delete product entries by pressing the 'Delete' button beneath each entry.  


---

The Payment Details page is shown below:

![Payment Details](https://github.com/jdovener/qa-project1/blob/dev/images/Payment%20Details.png)

The Payment Details page shows all customer payment details currently entered into the database. On this page the user can:  
* Add customer payment details by populating the forms at the bottom of the page and pressing the 'Add' button.  
    * The 'Customer ID' field is a foreign key from the Customers table in the database, this MUST be populated with an existing ID present in the Customer table or the app will not allow entry.
* Delete customer payment details entries by pressing the 'Delete' button beneath each entry.  


# Testing

Testing is an essential part of the development process. The project features both unit testing and integration testing, the documentation for which can be found below.

## Unit Testing

Unit testing is used to verify that individual aspects of the app function correctly (i.e functions/methods/routes etc). This is used to ensure that all create, read, update and delete fucntionality works as intended. 

Pytest was used to conduct the unit testing. Below is an image of a pytest test session showing 15 tests passing successfully. The coverage report shows 100% coverage across the code base, verifying that everything is working correctly.

![Pytest](https://github.com/jdovener/qa-project1/blob/dev/images/Pytest.png)

## Integration Testing

Integration testing is used to test the app in an 'as-live' environment. This method is able to simulate mouse clicks and keyboard input. I have written integration tests using selenium which tests that every button and input field on every page is functioning as intended.

The images below show pytest running the aformentioned tests. 20 tests pass successfully - The first 15 tests are unit tests, the remaining 5 tests are integration tests). 

![Integration1](https://github.com/jdovener/qa-project1/blob/dev/images/Integration1.png)
![Integration2](https://github.com/jdovener/qa-project1/blob/dev/images/Integration2.png)

I have omitted the terminal output explanations regarding the warnings as they are not relevant to this project. The warnings simply suggest that these tests may not be compatible with future versions of Ubuntu.

## Instructions on how to run tests

In order to run these tests manually, I open a terminal and navigate to the top layer of the project. I then run the following command:

```
python3 -m pytest --cov --cov-report term-missing
```

This command runs pytest on any files beginning with the word 'test'. It also makes the terminal produce a coverage report to show what percentage of the code has been covered. It is important to aim for 100% coverage to ensure everything works as intended. If areas of code have not been covered by the test, the 'term-missing' argument will provide the user with details of which file the missed code is in and which lines the missed code occupies.

However, the project is now set up to automatically via Jenkins every time a push is made to the GitHub repository.

# CI Pipeline

One of the project constraints required the project to implement a CI pipeline. The stages of this pipeline include: project tracking, version control, development environment and build server.  
  
For project tracking, trello was used to create a tracking board. Examples of this and access to the trello board can be found in the [Project Design](#Project-Design) section of this README document.

Git was used for the version control stage of the pipeline. The project repository was hosted on GitHub. Using Git allows for the project to be built incrementally and saves a history of all previous commits. These previous commits can be rolled back to in the event of errors to allow access to previous versions of the project.

A Python3 virtual environment (venv) was used as a development environment. This was hosted on a virtual machine (on Google Cloud Platform) running Ubuntu 20.04. A venv allows for seperation of concerns meaning pip installs can be performed without affecting any conflicting pip installs within the same machine.

Jenkins was used as a build server in order to automate the tests and the build. This is achieved by creating a freestyle project via Jenkins, the project uses gunicorn to run the app. A webhook is used to continuously integrate changes.  
  
The Jenkins freestyle project handles the following steps:
1. Kills the previous deployment to ensure a fresh build
2. Creates a venv and activates the venv
3. Installs project requirements into the venv
4. Holds a secret key to access the SQL database (instead of hardcoding a password into the application project)
5. Runs unit tests and integration tests
6. Runs the app
7. Uses a webhook to continuously integrate changes

An illustration of the full pipeline is shown below:

![Infrastructure](https://github.com/jdovener/qa-project1/blob/dev/images/Infrastructure.png)

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

* 02/06/2022
    * Improved readability of README.md compilation by adding line breaks.

* 15/06/2022
    * Added dependencies file and relevant information to README file.

* 16/06/2022
    * Updated .gitignore file to include more items to ignore.

# Known Issues

* If an entry is submitted on the Payment Details page with a customer id that is not currently present in the customers table, an error is thrown and the app does not redirect the user back automatically.
* Similarly to above issue: If an entry is submitted on the Orders page with a customer id/product id that is not currently present in the customers/products table, an error is thrown and the app does not redirect the user back automatically.

# Future Work

If I were to recreate this app, in addition to fixing the current known issues, I would like to implement the following changes:

* Use flask forms to create form fields instead of using <a> tags.
* Add the ability to update records in all tables without having to delete the entire entry and re-enter the updated information.
* Add drop down menus to various input fields.
    * This would prevent the user from attempting to enter an incorrect customer id/product id as a foreign key in the Payment Details/Orders submission forms. This would be done by querying the database for present entries in relevant other tables and using the results to populate the dropdown.
    * This would also increase efficiency for the user and reduce the chance of general spelling mistakes.
* Improve stylisation of displayed database entries for easier readability
* Add a max character limit to various input fields (such as the account number input field on the payment details page) to reduce the chance of errors.
* Add the ability to create orders with multiple products on the Orders page. The input fields would also feature drop down menus for adding products/customer information.