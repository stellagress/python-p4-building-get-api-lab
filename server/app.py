#!/usr/bin/env python3
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from sqlalchemy import desc 

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():

    bakeries_all = []
    for bake in Bakery.query.all():
        bake_dict = {
            "id" : bake.id,
            "name" : bake.name,
            "created_at" : bake.created_at

        }
        bakeries_all.append(bake_dict)

        response = make_response(
            jsonify(bakeries_all),
            200,
            # {"Content-Type" : "application/json"}
        )
    return response



@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bake = Bakery.query.filter(Bakery.id == id).first()
    
    bake_dict = {
        "id" : bake.id,
        "name" : bake.name,
        "created_at" : bake.created_at
    }
 

    response = make_response(
        bake_dict,
        200
    )
    return response




@app.route('/baked_goods/by_price')
def baked_goods_by_price():

    order_by_price = []
    for product in BakedGood.query.order_by(BakedGood.price).all():
        price_dict = {
            "id" : product.id,
            "name" : product.name,
            "price" : product.price,
            "created_at" : product.created_at

        }
        order_by_price.append(price_dict)

    response = make_response(
        order_by_price,
        200
    )
    return response



# @app.route('/baked_goods/most_expensive')
# def most_expensive_baked_good():
    
#     order_by_price = []
#     for product in BakedGood.query.order_by(desc(BakedGood.price)).all():
#         price_dict = {
#             "id" : product.id,
#             "name" : product.name,
#             "price" : product.price,
#             "created_at" : product.created_at

#         }
#         order_by_price.append(price_dict)

#     response = make_response(
#         order_by_price,
#         200
#     )
#     return response

from sqlalchemy import desc  # Import the 'desc' function

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    most_expensive = BakedGood.query.order_by(desc(BakedGood.price)).first()  

    if most_expensive:
        price_dict = {
            "id": most_expensive.id,
            "name": most_expensive.name,
            "price": most_expensive.price,
            "created_at": most_expensive.created_at
        }
  
    response = make_response(
        price_dict,
        200
    )
    return response








if __name__ == '__main__':
    app.run(port=5555, debug=True)
