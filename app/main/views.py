from . import main_blueprint
from flask import render_template, abort
from flask_login import login_required, current_user
from ..requests import get_quotes
from ..models import User
from .. import db

@main_blueprint.route('/')
def home():
    return render_template('index.html')

@main_blueprint.route('/quotes')
def quotes():
    quotes = get_quotes()
    return render_template('quotes.html', quotes = quotes)


@main_blueprint.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user=user)


