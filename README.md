# PizzaAPI
An API for ordering Pizza

# Project Installation & Run:

## Installation:

* Activate Virtual Enviorment

> `source venv/Scripts/activat`

* Install all the requirements

> `pip install -r requirements.txt`

## Run project:

* Migrate your project first

> `python manage.py makemigrations`

> `python manage.py migrate`

* Run

> `python manage.py runserver`

# API :

## USER

* Get all the pizza **[get Request]**

> http://localhost:8000/api/v1pizza/

* Get user by ID **[get Request]**

> http://localhost:8000/api/v1/pizza/**id**

* Create User **[post Request]**

> http://localhost:8000/api/v1/pizza/


## Admin:

* Credentials

> USERNAME: admin

> PASSWORD: admin
