from app import DB as db
from sqlalchemy.dialects.postgresql import *
from sqlalchemy import Column, Integer, Float, DateTime, func, desc, asc
from .category import Category

class Product(db.Model):
    """ Product model """

    __tablename__ = "product"

    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String)
    count = db.Column(db.Integer)
    price = db.Column(db.Integer)
    category_id = db.Column(db.Integer , db.ForeignKey('category.id'), nullable=False)
    caffe_id = db.Column(db.Integer, db.ForeignKey('caffe.id'), nullable =False)
    atributes = db.Column (db.JSON)
    additional_data = db.Column(db.JSON)

    def __init__(self, name , count, price, category_id , caffe_id , atributes, additional_data):
        self.name =  name
        self.count = count
        self.price = price
        self.category_id = category_id
        self.caffe_id = caffe_id
        self.atributes = atributes
        self.additional_data = additional_data

    @classmethod
    def create(cls, name, count, price, category_id , caffe_id , atributes, additional_data):

        product = cls (name = name, count = count, price = price , category_id = category_id , caffe_id = caffe_id , 
        atributes = atributes , additional_data = additional_data)

        db.session.add(product)
        db.session.commit()

        return product

    @classmethod
    def delete(cls, id):
        product = Product.query.filter_by(id = id).first()

        if product is None:
            return False
        db.session.delete(product)
        db.session.commit()

        return True

    @classmethod

    def update(cls , id, name, count, price, category_id , caffe_id , atributes, additional_data):

        product = Product.query.filter_by(id = id).first()

        if  name is not None and name != "":
            product.name = name

        if count is not None and count > -1:
            product.count = count
        if price is not None and price > -1:
            product.price = price
        if category_id is not None and category_id > 0:
            product.category_id = category_id
        if caffe_id is not None and caffe_id > 0:
            product.caffe_id = caffe_id
        if atributes is not None and atributes != {}:
            product.atributes = atributes
        if additional_data is not None :
            product.additional_data = additional_data
        db.session.commit()

        return product

    def to_json(self):

        json = dict()

        json["id"] = self.id
        json["name"] = self.name
        json["count"] = self.count
        json["price"] = self.price
        json["category_id"] = self.category_id
        json["caffe_id"] = self.caffe_id
        json["atributes"] = self.atributes
        json["additional_data"] = self.additional_data

        return json


        


