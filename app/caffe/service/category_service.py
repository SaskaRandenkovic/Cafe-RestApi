from app.caffe.models.category import Category
from flask import Response , json , request
import traceback2 as traceback
from app.utils import BadDataApiException , InternalErrorApiException

class CategoryService():

    def create_category(self , request):

        try:
            data = request.json

            if type(data.get("name")) != str and data.get("name") is not None:
                raise BadDataApiException("name is not str !")
            else:
                name = data.get("name")
            if type(data.get("atributes")) != dict and data.get("atributes") is not None:
                raise BadDataApiException("atributes is not dictionry !")
            else:
                atributes = data.get("atributes")

            if type(data.get("additional_data")) != dict and data.get("additional_data") is not None:
                raise BadDataApiException("additional_data not dictionry !")
            else:
                additional_data = data.get("additional_data")

            category = Category.create(name, atributes , additional_data)
            
            return Response(response = json.dumps(category.to_json()) , status= 200 , mimetype= 'application/json')

        except BadDataApiException:
            raise
        except:
            traceback.print_exc()
            raise InternalErrorApiException("Server error")


    def delete_category(self , id):
        try:
            if int (id) == 0:
                raise BadDataApiException("Id is 0")
            category = Category.query.filter_by(id = int(id)).first()

            if category is None:
                raise BadDataApiException("Category with id " +id + " does not exist !")

            data = Category.delete(int(id))

            return Response(response = "Category is deleted", status = 200 , mimetype = 'application/json')
        except BadDataApiException:
            raise
        except:
            traceback.print_exc()
            raise InternalErrorApiException("Server error")

    def update_category(self, id, request):
        try:
            if int (id) == 0:
                raise BadDataApiException("Id is 0")

            category = Category.query.filter_by(id = id).first()

            if category is None:
                raise BadDataApiException("Category with id " + id + " does not exist !")
            
            data = request.json

            if type(data.get("name")) !=str and data.get("name") is not None:
                raise BadDataApiException("name is not str !")
            name = data.get("name")

            if type(data.get("atributes")) != dict and data.get("atributes") is not None:
                raise BadDataApiException("atributes is not dict !") 
            atributes = data.get("atributes")

            if type(data.get("additional_data")) != dict and data.get("additional_data") is not None:
                raise BadDataApiException("additional_data is not dict !")
            additional_data = data.get("additional_data")

            update_category = Category.update(id, name, atributes, additional_data)
            json_data = update_category.to_json()

            return Response(response = json.dumps(json_data) , status = 200 , mimetype = 'application/json')

        except BadDataApiException:
            raise
        except:
            traceback.print_exc()
            raise InternalErrorApiException("Server error")
