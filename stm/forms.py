from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class ProductsForm(FlaskForm):

    productName = StringField(
        'Product Name', [DataRequired()])
    price = IntegerField('Price', [DataRequired()])
    quantity = IntegerField('quantity', [DataRequired()])
    submit = SubmitField('Submit')


class ProductsEditForm(FlaskForm):

    productName = StringField(
        'Product Name', [DataRequired()])
    price = IntegerField('Price', [DataRequired()])
    quantity = IntegerField('quantity', [DataRequired()])
    submit = SubmitField('Save')
