from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from dotenv import load_dotenv
from os import getenv

load_dotenv()
db_user = getenv('USER_POSTGRES')
db_pass = getenv('PASS_POSTGRES')

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql://{db_user}:{db_pass}@db/main'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
CORS(app)

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)  # id come from django app
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # id come from django app
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name= 'user_product_unique')

@app.route('/')
def index():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
