from flask import Flask, render_template, redirect, request, url_for, session, jsonify
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
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
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JWT_SECRET_KEY'] = 'yellow'

jwt = JWTManager(app)


@app.route('/clients', methods=['GET'])
@jwt_required()
def clients():
    clients = select_clients()
    return jsonify(clients), 200

@app.route('/sales')
@jwt_required()
def sales():
    sales = select_sales()
    return jsonify(sales), 200

@app.route('/cars')
@jwt_required()
def cars():
    cars = select_cars()
    return jsonify(cars), 200

@app.route('/dealers')
@jwt_required()
def dealers():
    dealers = select_dealers()
    return jsonify(dealers), 200

@app.route('/login', methods=['POST'])
def login():
    req_data = request.get_json()
    name = req_data['name']
    password = req_data['password']

    accepted = dealer_login(name=name, password=password)

    if accepted:
        access_token = create_access_token(identity=name)
        return jsonify(access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401
    
@app.route('/registerclient', methods=['POST'])
@jwt_required()
def register_client_route():
    req_data = request.get_json()
    name = req_data['name']
    email = req_data['email']
    phone = req_data['phone']
    success = insert_client(name=str(name), email=str(email), phone=str(phone))
    if not success:
        print("Failed to insert", sys.stderr)
        return "Failed to insert", 500

    return "Client Registered", 200

@app.route("/updateclient", methods=['PUT'])
@jwt_required()
def update_client_route():
    req_data = request.get_json()
    name = req_data['name']
    email = req_data['email']
    phone = req_data['phone']
    success = update_client(name=str(name), email=str(email), phone=str(phone))
    if not success:
        print("Failed to insert", sys.stderr)
        return "Failed to update", 500

    return "Client Updated", 200

@app.route('/registersale', methods=['POST'])
@jwt_required()
def register_sale_route():
    req_data = request.get_json()
    name = req_data['name']
    car = req_data['car']
    dealer = req_data['dealer']
    price = req_data['price']

    success = insert_sale(name, car, dealer, price)
    if not success:
        print("Failed to insert", sys.stderr)
        return "Failed to Register Sale", 500

    return "Sale Registered", 200

@app.route('/deletesale', methods=['DELETE'])
@jwt_required()
def delete_sale_route():
    req_data = request.get_json()

    id = req_data["id"]
    success = remove_sale(id)
    if not success:
        print("Failed to remove", sys.stderr)
        return "Failed to remove sale", 401

    return "Sale Removed", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
