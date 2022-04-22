"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app,db,login_manager
from flask import render_template, request, jsonify, send_file,redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
import os
from app.forms import CreateUserForm,LoginForm
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
    if request.method == "POST":
        form.FormSubmitted = True
        
        if form.validate_on_submit():            
                
                NewProfile = UserProfile(form.username.data, form.password.data, form.name.data, 
                                         form.email.data, form.location.data, form.biography.data,
                                          form.photo.data)

                db.session.add(NewProfile)
                db.session.commit()

                flash('Profile created and successfully saved', 'success')
                login_user(NewProfile)
                return redirect(url_for('profile'))        

    return render_template('register.html',form=form)

@app.route('/api/auth/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        # change this to actually validate the entire form submission
        # and not just one field
        if form.validate_on_submit():
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
            return redirect(url_for("home"))  # they should be redirected to a secure-page route instead
    flash_errors(form)
    return render_template("login.html", form=form)

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