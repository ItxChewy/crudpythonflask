from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv, find_dotenv
import os
from sqlalchemy import types

load_dotenv(find_dotenv())
usuario = os.environ.get("MYSQLDB_USUARIO")
password = os.environ.get("MYSQLDB_PASSWORD")
host = os.environ.get("MYSQLDB_HOST")
bd = os.environ.get("MYSQLDB_BD")

db = SQLAlchemy()
ma = Marshmallow()

def initialize_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{usuario}:{password}@{host}/{bd}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'hardsecretkey'  

    db.init_app(app)
    ma.init_app(app)

class User(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    image_filename = db.Column(db.String(255))  
    image_blob = db.Column(types.LargeBinary)
    numeric_column = db.Column(db.Float) 
    date_column = db.Column(db.Date)  

    def __init__(self, username, name, password, image_filename=None,image_blob=None, numeric_column=None, date_column=None):
        self.username = username
        self.name = name
        self.password = password
        self.image_filename = image_filename
        self.image_blob = image_blob
        self.numeric_column = numeric_column
        self.date_column = date_column

    def __repr__(self):
        return f'<User {self.username}>'
