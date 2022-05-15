from crypt import methods
from . import auth_blueprint
from flask import render_template
from .forms import SignupForm



@auth_blueprint.route('/signup', methods=['POST','GET'])
def signup():
    form = SignupForm()
    return render_template('auth/signup.html', form = form)
