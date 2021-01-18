from app import DB as db
from sqlalchemy.dialects.postgresql import *
from sqlalchemy import Column, Integer, Float, DateTime, func, desc, asc
from .product import Product
import traceback2 as traceback


class Caffe(db.Model):
    """
        Ovo je model kafica. 
    """
    __tablename__ = 'caffe'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    owner = db.Column(db.String)
    PIB = db.Column(db.String)
    bank_account = db.Column(db.String)
    products = db.relationship(
        Product,
        primaryjoin="Product.caffe_id==Caffe.id",
        cascade="all, delete-orphan")



    def __init__(self, name , location , owner ,PIB ,bank_account):
        self.name = name 
        self.location = location
        self.owner = owner
        self.PIB = PIB
        self.bank_account = bank_account

    @classmethod
    def create(cls, name, location, owner, PIB, bank_account):
        caffe = cls (name = name,
                    location = location, 
                    owner = owner,
                    PIB = PIB,
                    bank_account = bank_account)
        db.session.add(caffe)
        db.session.commit()
        return caffe

    @classmethod
    def delete(cls,id):
        try:
            caffe = Caffe.query.filter_by(id = id).first()
            db.session.delete(caffe)
            db.session.commit()
            return True
        except:
            traceback.print_exc()
            return False

    @classmethod
    def update(cls, id, name, location, owner, PIB, bank_account):
        try:
            caffe = Caffe.query.filter_by(id = id).first()

            if name is not None and name != '':
                caffe.name = name
            if location is not None and location != '':
                caffe.location = location
            if owner is not None and owner != '':
                caffe.owner = owner
            if PIB is not None and PIB != '':
                caffe.PIB = PIB
            if bank_account is not None and bank_account != '':
                caffe.bank_account = bank_account
            db.session.commit()
            return caffe

        except:
            traceback.print_exc()
            return False

    def to_json(self):
        try:
            json = dict()
            json["id"] = self.id
            json["name"] =  self.name
            json["location"] = self.location
            json["owner"] = self.owner
            json["PIB"] = self.PIB
            json["bank_account"] = self.bank_account
            products = []
            for product in self.products:
                products.append(product.to_json())
            json["products"] = products 
            return json
        except:
            traceback.print_exc()
            return {}

