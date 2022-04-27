"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

# from crypt import methods
# from lib2to3.pytree import _Results
from app import app,db,login_manager
from flask import render_template, request, jsonify, send_file,redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
import os
from app.forms import CreateUserForm,LoginForm,CarsForm,SearchForm
from app.models import UserProfile, Car, Favourite
from datetime import date
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash

###
# Routing for your application.
###
@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


@app.route('/api/register', methods=["GET", "POST"])
def register():
    """Accepts user information and saves it to the database."""
    form = CreateUserForm()
     
        
    if form.validate_on_submit() and request.method == "POST" :
        username=form.username.data
        password=form.password.data
        name=form.name.data                          
        email=form.email.data
        location=form.location.data 
        biography=form.biography.data
        photo=form.photo.data 
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    
            
        NewProfile = UserProfile(username=username,password=password,name=name,email=email,
                                    location=location, biography=biography,photo=filename)

        db.session.add(NewProfile)
        db.session.commit()

        flash('Profile created and successfully saved', 'success')
        #login_user(NewProfile)
        #return redirect(url_for('profile'))        

    #return render_template('register.html',form=form)

@app.route('/api/auth/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    
    # change this to actually validate the entire form submission
    # and not just one field
    if form.validate_on_submit() and request.method == "POST":
        # Get the username and password values from the form.
        username = form.username.data
        password = form.password.data
        
        user = UserProfile.query.filter_by(username=username).first()
        if user is not None and check_password_hash(user.password, password):

            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('secure_page'))
        else:
            flash('Username or Password is incorrect.', 'danger')


        # remember to flash a message to the user
        #return redirect(url_for("home"))  # they should be redirected to a secure-page route instead
    #flash_errors(form)
    #return render_template("login.html", form=form)

@app.route('/api/cars', methods=["GET"])
def cars():
    myform = CarsForm()
    if request.method == "GET" and myform.validate_on_submit():
        Cars = Car.query.all()
        return render_template('cars.html',Cars)

@app.route('/api/cars/new', methods=["POST"])
def newcar():
    myform = CarsForm()
    if request.method == "POST" and myform.validate_on_submit():
        model = myform.model.data
        make = myform.make.data
        description = myform.description.data
        price = myform.price.data
        colour = myform.colour.data
        car_type = myform.car_type.data
        transmission = myform.transmission.data
        year = myform.year.data
        photo = myform.photo.data
        car_form = Car(model,make,description,price,colour,car_type,transmission,year,photo)
        db.session.add(car_form)
        db.session.commit()
        return '{\
                "message":"Car Successfully Added"\
                }'
    return '{\
        "errors": "%s"\
    }'% form_errors(myform)

@app.route('/api/car/<car_id>', methods=["GET"])
def car_detail(car_id):

    car_dets = Car.query.get(car_id)
    if car_dets is not None:
        model = car_dets.model
        make = car_dets.make
        description = car_dets.description
        price = car_dets.price
        colour = car_dets.colour
        car_type = car_dets.car_type
        transmission = car_dets.transmission
        year = car_dets.year
        photo = car_dets.photo
        return render_template('car.html',model=model,make=make,description=description,price=price,colour=colour,car_type=car_type,transmission=transmission,year=year,photo=photo)

# @app.route('/api/cars/<car_id>/favourite', methods=["GET"])
# def add_favourite(id):
#     if request.method == "POST":

@app.route('/api/search', methods=['POST'])
def search():
    form = SearchForm()
    car = Car.query
    if form.validate_on_submit():
        car.searched = form.searched.data
        car = car.filter(Car.make.like('%' + car.searched + '%'))
        car = car.order_by(Car.car_type).all()
        return render_template("search.html",form=form,searched = car.searched)

@app.route('/api/users/<user_id>', methods=['POST'])
def user_detail(user_id):
    user_dets = Car.query.get(user_id)
    if user_dets is not None:
        username = user_dets.username
        password = user_dets.password
        name = user_dets.name
        email = user_dets.email
        location = user_dets.location
        biography = user_dets.biography
        photo = user_dets.photo
        date_joined = user_dets.date_joined
        return render_template("profile",username=username,password=password,name=name,email=email,location=location,biography=biography,photo=photo,date_joined=date_joined)

@app.route('/api/auth/logout')
@login_required
def logout():
 logout_user()
 flash('You have been logged out.', 'success')
 return redirect(url_for('home'))

###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify(error="Page Not Found"), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")