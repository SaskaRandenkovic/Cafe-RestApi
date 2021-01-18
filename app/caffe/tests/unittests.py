from app.tests import DataBaseUnittest
from app import DB as db
from app.caffe.models import Caffe, Category ,Product

class UnitCaffeTest(DataBaseUnittest):

    def test_create(self):
        caffe = Caffe.create("Oktopod","Cair","Mihajlo","23232442","3232553")
        assert caffe in db.session

    def test_delete(self):
        caffe = Caffe.create("Oktopod","Cair","Mihajlo","23232442","3232553")
        Caffe.delete(caffe.id)
        assert caffe not in db.session

    def test_update(self):
        caffe = Caffe.create("Oktopod","Cair","Mihajlo","23232442","3232553")
        caffe_update = Caffe.update(caffe.id,None,"Park", None,None,None)
        assert caffe_update in db.session

class UnitCategoryTest(DataBaseUnittest):

    def test_create(self):
        category = Category.create("Pica",{"dimenzije":"int"} , {})
        assert category in db.session
        assert category.name == "Pica"

    def test_delete(self):
        category = Category.create("Pica",{"dimenzije":"int"} , {})
        Category.delete(category.id)
        assert category not in db.session

    def test_update(self):
        category = Category.create("Pica",{"dimenzije":"int"} , {})
        category_update = Category.update(category.id ,"Pljeskavica",None, None)
        assert category_update in db.session
        assert category_update.name == "Pljeskavica"

class UnitProductTest(DataBaseUnittest):

    def test_create(self):
        caffe = Caffe.create("Oktopod","Cair","Mihajlo","23232442","3232553")
        category = Category.create("Pica",{"dimenzije":"int"} , {})
        product = Product.create("Italijanska",3,340,category.id , caffe.id,{"dimenzije": 30},{})
        assert product in db.session
        assert product.atributes == {"dimenzije": 30}

    def test_delete(self):
        caffe = Caffe.create("Oktopod","Cair","Mihajlo","23232442","3232553")
        category = Category.create("Pica",{"dimenzije":"int"} , {})
        product = Product.create("Italijanska",3,340,category.id , caffe.id,{"dimenzije": 30},{})
        Product.delete(product.id)
        assert product not in db.session

    def test_update(self):
        caffe = Caffe.create("Oktopod","Cair","Mihajlo","23232442","3232553")
        category = Category.create("Pica",{"dimenzije":"int"} , {})
        product = Product.create("Italijanska",3,340,category.id , caffe.id,{"dimenzije": 30},{})
        product_update = Product.update(product.id,"Caprizzosa", 10 , 444,None,None,None,None)

        assert product_update in db.session
        assert product_update.name == "Caprizzosa"
        assert product_update.count == 10
        assert product_update.price == 444
        assert product_update.category_id == product.category_id




