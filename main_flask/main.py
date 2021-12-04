from dataclasses import dataclass

import requests
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from dotenv import load_dotenv
from os import getenv

from producer import publish

load_dotenv()
db_user = getenv('USER_POSTGRES')
db_pass = getenv('PASS_POSTGRES')

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql://{db_user}:{db_pass}@db/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
CORS(app)

db = SQLAlchemy(app)

@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)  # id come from django app
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # id come from django app
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name= 'user_product_unique')
    # TODO: Fix constrain because it is not applied on db

@app.route('/api/products')
def index():
    return jsonify(Product.query.all())


@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://host.docker.internal:9000/user')
    if req.status_code == 200:
        json = req.json()
        try:
            productUser = ProductUser(user_id=json['id'], product_id=id)
            db.session.add(productUser)
            db.session.commit()
            publish('product_liked', id)
        except:
            abort(400, 'You already liked this product')

        return jsonify({'message': 'success'})
    
    return abort(400, 'Something went wrong')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
