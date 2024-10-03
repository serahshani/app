from sqlalchemy import MetaData
from Flask_SQLAlchemy import SQLAlchemy

metadata = MetaData()
#create the extension
db = SQLAlchemy(metadata=metadata)
    """
    -> must have the tablename property
    ->
    """
class Menu(db.Model):
    __tablename__ = 'menus'
    #define columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    