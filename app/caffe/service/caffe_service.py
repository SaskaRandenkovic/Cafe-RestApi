from app.caffe.models import Caffe
from app import DB as db
import traceback2 as traceback
from flask import request , Response, json
from app.utils import BadDataApiException , InternalErrorApiException
class CaffeService():

    def get_by_id(self,id):
        try:
            caffe = Caffe.query.filter_by(id=id).first()
            if caffe is None:
                raise BadDataApiException("Caffe with ID = " + str(id) + " dosn't exist.")
            data = caffe.to_json()
            print(data)
            return Response(response = json.dumps(data) , status = 200, mimetype='application/json')
        except:
            traceback.print_exc()
            raise InternalErrorApiException("Server error")


    def create_caffe(self, request):
        try:
            data_dict = request.json
            if type(data_dict.get("name")) != str:
                raise BadDataApiException("Name is not Str")
            else:
                name = data_dict.get("name")
            if type(data_dict.get("location"))!= str:
                raise BadDataApiException("Location is not Str")
            else:
                location = data_dict.get("location")
            if type(data_dict.get("owner")) != str:
                raise BadDataApiException("Owner is not Str")
            else:
                owner = data_dict.get("owner")
            if type(data_dict.get("PIB")) != str:
                raise BadDataApiException("Pib is not Str")
            else:
                PIB = data_dict.get("PIB")
            if type(data_dict.get("bank_account")) != str:
                raise BadDataApiException("Bank account is not Str")
            else:
                bank_account = data_dict.get("bank_account")

            caffe = Caffe.create(name , location , owner ,PIB ,bank_account)
            data = caffe.to_json()
            return Response(response = json.dumps(data) , status = 200, mimetype='application/json')

        except BadDataApiException as BD:
            raise
        except:
            traceback.print_exc()
            raise InternalErrorApiException("Server error")
            

    def delete_caffe(self ,id):
        try:

            if int (id) == 0:
                raise BadDataApiException("Id is 0")

            caffe = Caffe.query.filter_by(id=int(id)).first()

            if caffe is None:
                raise BadDataApiException("Caffe with id" + id + " dose not exist !")
            
            Caffe.delete(int (id))
            return Response (response = "Delete caffe", status= 200 , mimetype= 'application/json' )
        except BadDataApiException:
            raise
        except:
            traceback.print_exc()
            raise InternalErrorApiException("Server error")

    def update_caffe(self, id , request):
        try:
            if int (id) == 0:
                raise BadDataApiException("Id is 0")

            caffe = Caffe.query.filter_by(id=id).first()

            if caffe is None:
                raise BadDataApiException("Caffe with id " + id + " dose not exist !")
            
            data_dict = request.json

            if type(data_dict.get("name") ) != str and data_dict.get("name")  is not None:
                raise BadDataApiException("name is not str !")
            else:
                name = data_dict.get("name")

            if type(data_dict.get("location") ) != str and data_dict.get("owner") is not None:
                raise BadDataApiException("location is not str !")
            else:
                location = data_dict.get("location")
            
            if type(data_dict.get("owner") ) != str and data_dict.get("owner") is not None :
                raise BadDataApiException("owner is not str !")
            else:
                owner = data_dict.get("owner")
            
            if type(data_dict.get("PIB") ) != str and data_dict.get("PIB") is not None :
                raise BadDataApiException("PIB is not str !")
            else:
                PIB = data_dict.get("PIB")
            
            if type(data_dict.get("bank_account") ) != str and data_dict.get("bank_account")  is not None :
                raise BadDataApiException("bank_account is not str !")
            else:
                bank_account = data_dict.get("bank_account")
           
            caffe = Caffe.update(id ,name, location, owner, PIB, bank_account)
            data = caffe.to_json()

            return Response(response = json.dumps(data), status = 200 , mimetype = 'application/json')

        except BadDataApiException:
            raise
        except:
            traceback.print_exc()
            raise InternalErrorApiException("Server error")
         