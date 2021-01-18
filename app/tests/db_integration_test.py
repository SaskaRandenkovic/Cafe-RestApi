from app import DB as db , create_app
from app.tests import DataBaseUnittest
from app.caffe.models import *

class DataBaseIntegrationTest(DataBaseUnittest):

    url = "http://127.0.0.1:5000"

    def create_caffe(self):
        caffe = Caffe.create("Oktopod","Cair","Mihajlo","23232442","3232553")
        return caffe
    def create_category(self):
        category = Category.create("Pica",{"dimenzije":"int"} , {})
        return category

    def create_product(self):
        caffe = Caffe.create("Oktopod","Cair","Mihajlo","23232442","3232553")
        category = Category.create("Pica",{"dimenzije":"int"} , {})
        product = Product.create("Italijanska",3,340,category.id , caffe.id,{"dimenzije": 30},{})

        return product

        

