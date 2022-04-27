from msilib.schema import Class
from app.models import *
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired, FileField
from wtforms import TextAreaField,StringField,SubmitField,validators,ValidationError,PasswordField,IntegerField
from wtforms.validators import DataRequired,Email

class CreateUserForm(FlaskForm):
    userName = StringField('Username', [validators.Length(min=1, max=80)])
    
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.Length(max=70),
        validators.EqualTo('confirm', message='Passwords must match')
    ])

    confirm = PasswordField('Repeat Password',[
        validators.DataRequired(),
        validators.Length(max=70),
        validators.EqualTo('password', message='Passwords must match')])

    name = StringField('Full Name', [validators.Length(min=1, max=80)])

    email = StringField('Email',[Email(message=('Not a valid email address.')), DataRequired()])

    location = StringField('Address', validators=[DataRequired()])

    biography = StringField('Biography', validators=[validators.Length(min=0, max=140)])
    
    photo = FileField('image',validators=[FileRequired(),FileAllowed(['jpg','jpeg','png','Images Only'])])
    

    FormSubmitted = False

    def validate_userName(form, field):
        user = UserProfile.query.filter_by(username=field.data).first()
        if user is not None: # Username already exist so we cannot proceed safely
            raise ValidationError('Username already exists.')
        

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired()])

class CarsForm(FlaskForm):
    model = StringField('Model', [validators.Length(min=1, max=80)])
    make = StringField('Make', [validators.Length(min=1, max=80)])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    colour = StringField('Colour', validators=[DataRequired()])
    car_type = StringField('Car type', validators=[DataRequired()])
    transmission = StringField('Transmission', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    photo = FileField('image',validators=[FileRequired(),FileAllowed(['jpg','jpeg','png','Images Only'])])

class SearchForm(FlaskForm):
    searched = StringField('Make', [DataRequired()])
    submit = SubmitField("Submit")
