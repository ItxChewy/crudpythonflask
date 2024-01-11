from database import db
from sqlalchemy.sql import func

class User(db.Model):

    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    image_filename = db.Column(db.String(255))
    image_blob = db.Column(db.LargeBinary)
    numeric_column = db.Column(db.Float)
    date_column = db.Column(db.Date)

    def __init__(self, username, name, password, image_filename=None, image_blob=None, numeric_column=None, date_column=None):
        self.username = username
        self.name = name
        self.password = password
        self.image_filename = image_filename
        self.image_blob = image_blob
        self.numeric_column = numeric_column
        self.date_column = date_column

    def __repr__(self):
        return f'<User {self.username}>'


# Para crear las tablas, desde el entorno de ejecución de Python, ejecutar:
# from database import app, db
# from estudiante import Estudiante
# app.app_context().push()
# db.create_all()
