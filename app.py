from flask import Flask
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
#flask configuratios
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restuarant.db'
#create the 
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return 'Hello, World!'