from flask import Flask, render_template, redirect, request, url_for, session
from functools import wraps

from models.client import Client
from models.sale import Sale
from models.car import Car
from models.dealer import Dealer

from database.clients import insert_client, update_client, select_clients
from database.dealers import select_dealers
from database.sales import select_sales, insert_sale, remove_sale
from database.cars import select_cars
from database.login import dealer_login

import sys

app = Flask(__name__)
app.secret_key = 'yellow'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def home():
    if 'logged_in' in session:
        return redirect(url_for('clients'))
    return redirect(url_for('login'))

# Routes to serve html
@app.route('/clients', methods=['GET'])
@login_required
def clients():
    clients = select_clients()
    return render_template('clients.html', clients=clients)

@app.route('/login', methods=['GET'])
def login():
    if 'logged_in' in session:
        return redirect(url_for('clients'))
    return render_template('login.html')

@app.route('/sales')
@login_required
def sales():
    sales = select_sales()
    return render_template('sales.html', sales=sales)

@app.route('/cars')
@login_required
def cars():
    cars = select_cars()
    return render_template('cars.html', cars=cars)

@app.route('/dealers')
@login_required
def dealers():
    dealers = select_dealers()
    return render_template('dealers.html', dealers=dealers)

# Ler forms e chamar funções da base de dados
@app.route('/clients', methods=['POST'])
def register_client():
    # Add new client to database
    form_id = request.form.get('form_id')

    if form_id == 'form1':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        success = insert_client(name=str(name), email=str(email), phone=str(phone))
        if not success:
            print("Failed to insert", sys.stderr)
    elif form_id == 'form2':
        name = request.form.get('name2')
        email = request.form.get('email2')
        phone = request.form.get('phone2')
        success = update_client(name=str(name), email=str(email), phone=str(phone))
        if not success:
            print("Failed to insert", sys.stderr)
    return redirect(url_for('clients'))

@app.route('/sales', methods=['POST'])
def register_sale():
    form_id = request.form.get('form_id')

    if form_id == 'form1':
        name = request.form.get('name')
        car = request.form.get('car')
        dealer = request.form.get('dealer')
        price = request.form.get('price')

        success = insert_sale(name, car, dealer, price)

        if not success:
            print("Failed to insert", sys.stderr)
    elif form_id == 'form2':
        id = int(request.form.get('id'))

        success = remove_sale(id)

        if not success:
            print("Failed to remove", sys.stderr)

    return redirect(url_for('sales'))

@app.route('/login', methods=['POST'])
def login_handler():
    name = request.form.get('name')
    password = request.form.get('password')

    accepted = dealer_login(name=name, password=password)
    if accepted:
        session['logged_in'] = True
        return redirect(url_for('clients'))
    return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
