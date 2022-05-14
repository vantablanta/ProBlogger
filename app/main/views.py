from . import main_blueprint
from flask import render_template
from flask_paginate import Pagination, get_page_args
from ..requests import get_quotes

@main_blueprint.route('/')
def home():
    return render_template('index.html')

@main_blueprint.route('/quotes')
def quotes():
    quotes = get_quotes()
    return render_template('quotes.html', quotes = quotes)

