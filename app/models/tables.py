from app import db

class Beds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.String, nullable=False)
    product_size = db.Column(db.String, nullable=False)
    amount_stock = db.Column(db.Integer, default=0)
    price = db.Column(db.Float, nullable=True)

    def __init__(self, product_type, product_size, amount_stock, price):
        self.product_type = product_type
        self.product_size = product_size
        self.amount_stock = amount_stock
        self.price = price

    def __repr__(self):
        return '<Beds %r %r %r %r>' % self.product_type, self.product_size, self.amount_stock, self.price

class Couches(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.String, nullable=False)
    product_size = db.Column(db.String, nullable=False)
    amount_stock = db.Column(db.Integer, default=0)
    price = db.Column(db.Float, nullable=True)

    def __init__(self, product_type, product_size, amount_stock, price):
        self.product_type = product_type
        self.product_size = product_size
        self.amount_stock = amount_stock
        self.price = price

    def __repr__(self):
        return '<Couches %r %r %r %r>' % self.product_type, self.product_size, self.amount_stock, self.price


class Wardrobe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.String, nullable=False)
    product_size = db.Column(db.String, nullable=False)
    amount_stock = db.Column(db.Integer, default=0)
    price = db.Column(db.Float, nullable=True)

    def __init__(self, product_type, product_size, amount_stock, price):
        self.product_type = product_type
        self.product_size = product_size
        self.amount_stock = amount_stock
        self.price = price

    def __repr__(self):
        return '<Wardrobe %r %r %r %r>' % self.product_type, self.product_size, self.amount_stock, self.price