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
├── ecom
│   ├── celery.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── README.md
├── requirements.txt
├── snapshots
├── static
│   ├── css
│   │   └── main.css
│   ├── images
│   └── js
│       └── cart.js
└── store
    ├── admin.py
    ├── apps.py
    ├── filters.py
    ├── forms.py
    ├── models.py
    ├── tasks.py
    ├── templates
    │   └── store
    │       ├── base.html
    │       ├── cart.html
    │       ├── category.html
    │       ├── change_password.html
    │       ├── checkout.html
    │       ├── email_template.html
    │       ├── login.html
    │       ├── main.html
    │       ├── order_detail.html
    │       ├── order_history.html
    │       ├── password_reset_complete.html
    │       ├── password_reset_confirm.html
    │       ├── password_reset_done.html
    │       ├── password_reset_form.html
    │       ├── profile.html
    │       ├── search.html
    │       ├── signup.html
    │       ├── store.html
    │       ├── success.html
    │       ├── update_user.html
    │       └── wrongpassword.html
    ├── tests.py
    ├── urls.py
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
