# E-commerce web apllication using Django:
Ecommerce project made with Django and basic HTML & CSS. I have used both class-based and functional views throughout the project, Celery for handling emails and Django-Filter for category filtering. API's for admin side are included in the app named api. For payment integration, I have used Paypal's API.
# Features:

Admin side:

1. Add new products.
2. Edit details of the existing products.
3. Delete existing products.
4. View all orders.
5. Change order status.
6. Filter orders based on their status.
7. View the order details.

User side:


1. Registration and authentication.
2. Add and remove products to cart.
3. Update the quantity of cart.
4. Payment can be done with paypal.
5. Products can be filtered by category.
6. Search filter.
7. Confirmation email after order successfully placed.
8. View complete order history.
9. View order details.
10. Update profile details.

# Technology stack:
1. Python 3.6.5
2. Django REST Framework 2.1
3. sqlite3 Database
4. Google Chrome

# Project Structure:
```
.
├── api: API's for the ecommerce project
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py: serializers for the models
│   ├── tests.py
│   ├── urls.py: urls for api app
│   └── views.py: These views are called by API endpoints
├── ecom Ecommerce project base folder
│   ├── celery.py: contains the default code needed for celery
│   ├── __init__.py
│   ├── settings.py: settings file for the project
│   ├── urls.py: base urls for apps of the project
│   └── wsgi.py
├── manage.py
├── README.md: documentation file
├── requirements.txt: requirements needs to be install
├── snapshots: contains the screenshots of project
├── static
│   ├── css
│   │   └── main.css: CSS file for the Ecommerce project
│   ├── images
│   └── js
│       └── cart.js: JS file for updating cart items
└── store
    ├── admin.py
    ├── apps.py
    ├── filters.py: contains the Django filters
    ├── forms.py: contains the Django forms rendered by views
    ├── __init__.py
    ├── models.py: database models for store app
    ├── tasks.py: contain tasks for celery
    ├── templates: HTML templates for Ecommerce website project
    │   └── store
    │       ├── adminpages: HTML pages for admin interface
    │       │   ├── adminaddproduct.html
    │       │   ├── adminallproduct.html
    │       │   ├── adminbase.html
    │       │   ├── admincategory.html
    │       │   ├── adminhome.html
    │       │   ├── adminlogin.html
    │       │   ├── adminmain.html
    │       │   ├── adminorderdetail.html
    │       │   ├── adminorderlist.html
    │       │   ├── adminprofile.html
    │       │   ├── adminstore.html
    │       │   ├── adminwrongpassword.html
    │       │   ├── deleteproduct.html
    │       │   └── editproduct.html
    │       ├── base.html
    │       ├── cart.html
    │       ├── category.html
    │       ├── change_password.html
    │       ├── checkout.html
    │       ├── email_template.html
    │       ├── home.html
    │       ├── login.html
    │       ├── main.html
    │       ├── order_detail.html
    │       ├── order_history.html
    │       ├── password_reset_complete.html
    │       ├── password_reset_confirm.html
    │       ├── password_reset_done.html
    │       ├── password_reset_form.html
    │       ├── profile.html
    │       ├── search.html
    │       ├── signup.html
    │       ├── store.html
    │       ├── success.html
    │       ├── update_user.html
    │       └── wrongpassword.html
    ├── tests.py
    ├── urls.py: url endpoints of store app
    └── views.py: These views are called by store app endpoints
```

# Running Locally:
First, clone the repository to your local machine:
git clone https://github.com/saiyadfaizan/ecomm.git

# Create super user:
python manage.py createsuperuser 
Note: It will prompt to enter username, email and password one by one. Please remember the username and password,
it will be used to login admin area.

# Steps to run the project:
1. Install the requirements: pip install -r requirements/dev.txt
2. Create the .env file to the root directory of the project. You can refer this example file- .env.example
2. Check for the database migrations: python manage.py makemigrations
3. Apply the database migrations: python manage.py migrate
4. Run the developement server: python manage.py runserver
5. Open chrome and the site will be available at: 127.0.0.1:8000/

# Future scope of the project:
1. Integrating new payment gateways.
2. Adding new search and category filters.
3. Implementing and using sessions.
4. Adding suggestions wrt previous purchases.
