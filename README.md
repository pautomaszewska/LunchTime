# LunchTime

### Info
App created for lunch ordering. The user can compose lunch from one of three main dishes (meat, vegetarian or vegan), one of two appetizers (soup or salad) and a beverage.

Demo: https://time-for-lunch.herokuapp.com/
To use as admin:
```
login: pt
password: 1234
```

 ![user_main](./images/user_main.png)
 ![user_makeorder](./images/user_makeorder.png)
 ![user_orders](./images/user_orders.png)
 ![admin_main](./images/admin_main.png)
 ![admin_ranking](./images/admin_ranking.png)

### Technologies
* Python 3.6 
* Django 2.1 
* PostgreSQL / SQLite
* jQuery
* Bootstrap 4

### Functions
Admin can:
* add main dishes, appetizers and beverages
* view main dishes, appetizers and beverages
* set lunch for a particular date
* view lunches in calendar
* edit lunch
* view today's orders
* confirm when the lunch is ready
* view order history
* view lunch ranking
* view user details
* randomly set lunches for the next three months

User can:
* order lunch
* collect bonus points
* exchange points for discounts
* view order history
* review lunch

### Installation
* clone repository
```
git clone https://github.com/pautomaszewska/LunchTime
```
* create virtual environment and install requirements
```
virtualenv -p pytho3 env
source env/bin/activate
pip install -r requirements.txt
```
* run migrations for 'buy_lunch' app
```
python manage.py makemigrations buy_lunch
python manage.py migrate
python manage.py runserver
```
* to set menu for the next three months, run:
```
python manage.py set_lunches
```

