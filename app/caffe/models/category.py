from app import DB as db
from sqlalchemy.dialects.postgresql import *
from sqlalchemy import Column, Integer, Float, DateTime, func, desc, asc

class Category(db.Model):
    """ Model koji predstavlja kategoriju proiyvoda """

    __tablename__ = "category"

    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String)
    atributes = db.Column(db.JSON)
    additional_data = db.Column(db.JSON)

    def __init__ (self, name, atributes , additional_data):
       self.name = name
       self.atributes = atributes
       self.additional_data = additional_data


    @classmethod
    def create(cls, name, atributes , additional_data):
        category = cls(name = name , atributes = atributes , additional_data = additional_data)
        db.session.add(category)
        db.session.commit()
        return category

    @classmethod
    def delete(cls,id):
        category = Category.query.filter_by(id = id).first()
        db.session.delete(category)
        db.session.commit()
        return True

    @classmethod
    def update(cls,id,name, atributes, additional_data):
        category = Category.query.filter_by(id = id).first()
        if name is not None and name != "":
            category.name = name
        if atributes is not None:
            category.atributes = atributes 
        if additional_data is not None:
            category.additional_data = additional_data
        
        db.session.commit()
        return category

    def to_json(self):

        json = dict()

        json["name"] = self.name
        json["atributes"] = self.atributes
        json["additional_data"] = self.additional_data

        return json
    








