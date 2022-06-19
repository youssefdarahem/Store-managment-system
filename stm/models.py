from stm import db


def getProducts():
    return Product.query.order_by(Product.id).all()


class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Product('{self.name}', '{self.price}', '{self.quantity}')"


class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20), unique=False, nullable=False)
    lname = db.Column(db.String(20), unique=False, nullable=False)
    address = db.Column(db.String(50), nullable=False)
    phone_num = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Customer('{self.fname}', '{self.lname}', '{self.address}', '{self.phone_num}')"


class Supplier(db.Model):
    __tablename__ = 'supplier'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    address = db.Column(db.String(50), nullable=False)
    phone_num = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Supplier('{self.name}', '{self.address}', '{self.phone_num}')"
