from flask import flash, redirect, render_template, request, url_for
from stm import app, db
from stm.forms import ProductsEditForm, ProductsForm
from stm.models import Product, getProducts


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/products', methods=['GET', 'POST'])
def product():
    products = getProducts()
    form = ProductsForm()
    if request.method == 'POST':
        product = Product(name=form.productName.data, price=form.price.data,
                          quantity=form.quantity.data)
        db.session.add(product)
        db.session.commit()
        flash('Thanks for registering')
        print(url_for('product'))
        return redirect(url_for('product'))
    return render_template('products.html', products=products, form=form)


@app.route('/products/<int:product_id>/edit', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    form = ProductsEditForm()
    if request.method == 'POST':
        product.name = form.productName.data
        product.price = form.price.data
        product.quantity = form.quantity.data
        db.session.commit()
        return redirect(url_for('product'))
    elif request.method == 'GET':
        form.productName.data = product.name
        form.price.data = product.price
        form.quantity.data = product.quantity
    return render_template('edit.html', form=form)


@app.route('/products/<int:product_id>/delete', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('product'))
