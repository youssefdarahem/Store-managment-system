from flask import render_template, url_for
from stm import app
from stm.models import getProducts

# TODO import models when created


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/products', methods=['GET'])
def product():
    products = getProducts()
    return render_template('products.html', products=products)
