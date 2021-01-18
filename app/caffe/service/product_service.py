from app.caffe.models.category import Category 
from app.caffe.models.caffe import Caffe
from app.caffe.models.product import Product
from flask import Response , json , request
import traceback2 as traceback
from app.utils import BadDataApiException , InternalErrorApiException


class ProductService():

    def create_product(self , request):

        try:
            data = request.json

            if type(data.get("name")) != str:
                raise BadDataApiException("Name is not str !")
            else:
                name = data.get("name")

            if type(data.get("count")) != int:
                 raise BadDataApiException("Count is not int !")
            else:
                count = data.get("count")

            if type(data.get("price")) != int:
                 raise BadDataApiException("Price is not int !")
            else:
                price = data.get("price")

            if type(data.get("category_id")) != int:
                 raise BadDataApiException("category_id is not int !")
            else:
                category_id = data.get("category_id")

                category = Category.query.filter_by(id = category_id).first()
                if category is  None:
                     raise BadDataApiException("Category with category_id dont exist !")

                atributes = {}
                if type(data.get("atributes")) is not dict:
                     raise BadDataApiException("Atributes is not dict ")

                for key in category.atributes:
                    if data.get("atributes").get(key) is not None and type(data.get("atributes").get(key)) == eval(category.atributes.get(key)):
                        atributes[key] = data.get("atributes").get(key)
                    else:
                         raise BadDataApiException("Atribut with key = " + key + " dose not exist or type is not ok ! ")

            if type(data.get("caffe_id")) != int:
                 raise BadDataApiException("caffe_id is not int !")
            else:
                caffe_id = data.get("caffe_id")
                caffe = Caffe.query.filter_by(id = caffe_id).first()
                if caffe is  None:
                     raise BadDataApiException("Caffe with caffe_id dont exist !")
                
            if type(data.get("additional_data")) is not dict:
                 raise BadDataApiException("Additional data is not dictionary !")

            else:
                additional_data = data.get("additional_data")

            product = Product.create(name,count,price,category_id,caffe_id,atributes,additional_data)

            return Response (response = json.dumps(product.to_json()) , status = 200 ,mimetype='application/json')

        except BadDataApiException:
            raise
        except:
            traceback.print_exc()
            raise InternalErrorApiException("Server error")

    def update_product(self , id, request):
        try:

            if int(id) == 0:
                raise BadDataApiException("Id is 0")

            product = Category.query.filter_by(id = id).first()

            if product is None:
                raise BadDataApiException("Product with id " +id + " does not exist !")    
            data = request.json

            if type(data.get("name")) !=str and data.get("name") is not None:
                raise BadDataApiException("name is not str !")
            name = data.get("name")

            if type(data.get("count")) !=int and data.get("count") is not None:
                raise BadDataApiException("count is not int !")
            count = data.get("count")

            if type(data.get("price")) !=int and data.get("price") is not None:
                raise BadDataApiException("price is not int !")
            price = data.get("price")

            if type(data.get("category_id")) !=int and data.get("category_id") is not None:
                raise BadDataApiException("category_id is not int !")
            category_id = data.get("category_id")

            if type(data.get("caffe_id")) !=int and data.get("caffe_id") is not None:
                raise BadDataApiException("caffe_id is not int !")
            caffe_id = data.get("caffe_id")

            if type(data.get("atributes")) !=int and data.get("atributes") is not None:
                raise BadDataApiException("atributes is not str !")
            atributes = data.get("atributes")

            if type(data.get("additional_data")) !=int and data.get("additional_data") is not None:
                raise BadDataApiException("additional_data is not str !")
            additional_data = data.get("additional_data")

            update_product = Product.update(id, name, count, price, category_id , caffe_id , atributes, additional_data)

            update_data = update_product.to_json()

            return Response(response = json.dumps(update_data) , status = 200 , mimetype = 'applicatoin/json')

        except BadDataApiException:
            raise
        except:
            traceback.print_exc()
            raise InternalErrorApiException("Server error")
            

    
    def delete_product(self , id):
        try:
            if int (id) == 0:
                raise BadDataApiException("Id is 0")
                
            product = Product.query.filter_by(id = int(id)).first()

            if product is None:
                raise BadDataApiException("Product with id " +id + " does not exist !")

            data = Product.delete(int(id))

            return Response(response = "Product is deleted", status = 200 , mimetype = 'application/json')
        except BadDataApiException:
            raise
        except:
            traceback.print_exc()
            raise InternalErrorApiException("Server error")



            


