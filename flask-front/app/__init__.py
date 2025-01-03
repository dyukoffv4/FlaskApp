from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import *

app = Flask(__name__)
app.secret_key = '0123'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASS}@{HOST_IP}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from .routes import *
