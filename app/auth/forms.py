from click import confirm
from flask_wtf import FlaskForm
from requests import options
from wtforms import StringField, EmailField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo


class SignupForm(FlaskForm):
    username = StringField("Enter username", validators=[DataRequired()])
    email = EmailField("Enter Email", validators=[DataRequired()])
    role = SelectField('Would you like to signup as a writer?', choices=['Yes', 'No'], validators=[DataRequired()])
    password = PasswordField('Enter password', validators=[DataRequired(), EqualTo('confirm_password', 
         message='Passwords must match')])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired()] )
    submit = SubmitField("Signup")