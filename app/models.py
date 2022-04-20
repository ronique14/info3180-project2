from . import db
from werkzeug.security import generate_password_hash
import datetime

class UserProfile(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    biography = db.Column(db.String(80))
    photo = db.Column(db.String(255))
    date_joined = db.Column(db.DateTime)

    def __init__(self,username, password,name,email,location,biography,photo):
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:rta246')
        self.name = name
        self.email = email
        self.location = location
        self.biography = biography
        self.photo = photo
        self.date_joined = datetime.datetime.now()


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)

class Car(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    make = db.Column(db.String(80))
    model = db.Column(db.String(255))
    colour = db.Column(db.String(80))
    year = db.Column(db.String(80))
    transmission = db.Column(db.String(80))
    car_type = db.Column(db.String(80))
    price = db.Column(db.Float)
    photo = db.Column(db.String(255))
    user_id = db.Column(db.Integer)
    
    def __init__(self,description, make,model,colour,year,transmission,car_type,price,photo,user_id):
        self.description = description
        self.make = make
        self.model = model
        self.colour = colour
        self.year = year
        self.transmission = transmission 
        self.car_type = car_type
        self.price = price
        self.photo = photo
        self.user_id = user_id


class Favourite(db.Model):
    __tablename__ = 'favourites'

    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
   

     
    def __init__(self,car_id,user_id):
         self.car_id = car_id
         self.user_id = user_id