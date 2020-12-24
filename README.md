# E-commerce website using Django:
It is a basic ecommerce applicaion in which following operations can be performed:

    - visit the store: http://127.0.0.1:8000/store/
    - check and update the cart: http://127.0.0.1:8000/cart/
    - see the checkout page: http://127.0.0.1:8000/checkout/
    - user signup via email/user name: http://127.0.0.1:8000/accounts/signup/
    - login: http://127.0.0.1:8000/accounts/
    - logout: http://127.0.0.1:8000/accounts/logout/
    - forget password: http://127.0.0.1:8000/accounts/reset_password/ 
    - update password: http://127.0.0.1:8000/accounts/change_password/
    - user profile edit: http://127.0.0.1:8000/accounts/update_user/

# Technology stack:
1. Python3
2. Django REST Framework
3. sqlite3 Database
4. Google Chrome

# Project Structure:
```
.
├── db.sqlite3
├── ecom
│   ├── __init__.py
│   ├── settings.py settings file for the project.
│   ├── urls.py base urls for apps of the projects
│   └── wsgi.py
├── manage.py
├── README.md: documentation file
├── requirements.txt requirements needs to be install
├── static
│   ├── css
│   │   └── main.css css file for the store app templates
│   ├── images
│   └── js
│       └── cart.js javascript file for the store app
└── store
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── __init__.py
    ├── migrations: database migrations
    ├── models.py database models for store app
    ├── templates
    │   └── store
    │       ├── base.html
    │       ├── cart.html
    │       ├── change_password.html
    │       ├── checkout.html
    │       ├── login.html
    │       ├── main.html
    │       ├── password_reset_complete.html
    │       ├── password_reset_confirm.html
    │       ├── password_reset_done.html
    │       ├── password_reset_form.html
    │       ├── profile.html
    │       ├── signup.html
    │       ├── store.html
    │       └── update_user.html
    ├── tests.py
    ├── urls.py url endpoints of store app
    └── views.py
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
