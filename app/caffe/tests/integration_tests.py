from app import DB as db 
from app.tests import DataBaseIntegrationTest 
from app.tests import *
from json import dumps, loads


class IntegrationCaffeTest(DataBaseIntegrationTest):

    def test_get_by_id(self):
        with self.client:
            caffe= self.create_caffe()
            response = self.client.get(self.url + "/api/get/caffe/" + str(caffe.id))
            if response.status_code == 200:
                data = loads(response.data)
            else:
                data = response.data.decode("UTF-8")
            assert response.status_code == 200

    def test_create_caffe_route(self):
        with self.client:
            json = { "name":"Oktopod", "location": "Nis, Cair", "PIB": "959505947459", "owner": "Radoje Mitic", "bank_account": "28883-3332-43434"}
            response = self.client.post(self.url + "/api/create/caffe", json = json)
            if response.status_code == 200:
                data = loads(response.data)
            else:
                data = response.data.decode("UTF-8")
            assert response.status_code == 200
            assert data.get("name") == "Oktopod"
            assert data.get("location") == "Nis, Cair"
            assert data.get("PIB") == "959505947459"
            assert data.get("owner") == "Radoje Mitic"
            assert data.get("bank_account") == "28883-3332-43434"

            ''' Name is not string'''

            json = { "name":4, "location": "Nis, Cair", "PIB": "959505947459", "owner": "Neki lopov", "bank_account": "28883-3332-43434"}
            response = self.client.post(self.url + "/api/create/caffe", json = json)
            if response.status_code == 200:
                data = loads(response.data)
            else:
                data = response.data.decode("UTF-8")
            assert response.status_code == 400
            assert data == "Name is not Str"

            ''' Location is not string'''
            
            json = { "name":"Oktopod", "location": 67, "PIB": "959505947459", "owner": "Neki lopov", "bank_account": "28883-3332-43434"}
            response = self.client.post(self.url + "/api/create/caffe", json = json)
            if response.status_code == 200:
                data = loads(response.data)
            else:
                data = response.data.decode("UTF-8")
            assert response.status_code == 400
            assert data == "Location is not Str"

            ''' PIB is not string'''
            
            json = { "name":"Oktopod", "location": "nis , Bulevar", "PIB": 959505947459, "owner": "Neki lopov", "bank_account": "28883-3332-43434"}
            response = self.client.post(self.url + "/api/create/caffe", json = json)
            if response.status_code == 200:
                data = loads(response.data)
            else:
                data = response.data.decode("UTF-8")
            assert response.status_code == 400
            assert data == "Pib is not Str"

            ''' Owner is not string'''
            
            json = { "name":"Oktopod", "location": "nis , Bulevar", "PIB":"959505947459", "owner": True, "bank_account": "28883-3332-43434"}
            response = self.client.post(self.url + "/api/create/caffe", json = json)
            if response.status_code == 200:
                data = loads(response.data)
            else:
                data = response.data.decode("UTF-8")
            assert response.status_code == 400
            assert data == "Owner is not Str"

            ''' Bank account is not string'''
            
            json = { "name":"Oktopod", "location": "nis , Bulevar", "PIB": "959505947459", "owner": "Neki lopov", "bank_account":8}
            response = self.client.post(self.url + "/api/create/caffe", json = json)
            if response.status_code == 200:
                data = loads(response.data)
            else:
                data = response.data.decode("UTF-8")
            assert response.status_code == 400
            assert data == "Bank account is not Str"


    def test_delete_caffe_route(self):
        with self.client:
            caffe = self.create_caffe()
            response = self.client.delete(self.url + "/api/delete/caffe/" + str(caffe.id) )
            data = response.data.decode("UTF-8")
            assert response.status_code == 200

            '''Bad id '''

            caffe = self.create_caffe()
            id = 76
            response = self.client.delete(self.url + "/api/delete/caffe/" + str(id) )
            data = response.data.decode("UTF-8")
            assert response.status_code == 400
            assert data == "Caffe with id" + str(id) + " dose not exist !"

    def test_update_caffe_route(self):
         with self.client:
            caffe = self.create_caffe()
            json = {"name": "Pleasure", "PIB": "64739262893","bank_account": "4444444444"}
            response = self.client.put(self.url + "/api/update/caffe/" + str(caffe.id) , json =json)
            if response.status_code ==200:
                data = loads(response.data)
            else:
                data = response.data.decode("UTF-8")
            assert response.status_code == 200
            assert data["name"] == "Pleasure"
            assert data["PIB"] == "64739262893"
            assert data["bank_account"] == "4444444444"

            '''Name is not str'''

            caffe = self.create_caffe()
            json = {"name": 4, "PIB": "64739262893","bank_account": "4444444444"}
            response = self.client.put(self.url + "/api/update/caffe/" + str(caffe.id) , json =json)
            if response.status_code ==200:
                data = loads(response.data)
            else:
                data = response.data.decode("UTF-8")
            assert response.status_code == 400
            assert data == "name is not str !"

            '''PIB is not str'''

            caffe = self.create_caffe()
            json = {"name": "Pleasure", "PIB": 64739262893,"bank_account": "4444444444"}
            response = self.client.put(self.url + "/api/update/caffe/" + str(caffe.id) , json =json)
            if response.status_code ==200:
                data = loads(response.data)
            else:
                data = response.data.decode("UTF-8")
            assert response.status_code == 400
            assert data == "PIB is not str !"

            '''Bank account is not str'''

            caffe = self.create_caffe()
            json = {"name": "Pleasure", "PIB": "64739262893","bank_account": 4444444444}
            response = self.client.put(self.url + "/api/update/caffe/" + str(caffe.id) , json =json)
            if response.status_code ==200:
                data = loads(response.data)
            else:
                data = response.data.decode("UTF-8")
            assert response.status_code == 400
            assert data == "bank_account is not str !"
            



class IntegrationCategoryTest(DataBaseIntegrationTest):

    def test_create_category_route(self):
        with self.client:
            json = {"name":"Torte", "atributes": {"velicina": "int" , "okrugla" : "bool"}, "additional_data":{}}
            response = self.client.post(self.url + "/api/create/category" , json =json)

            if response.status_code == 200:
                data = loads(response.data)
            else:
                data = response.data.decode("UTF-8")
            assert response.status_code == 200
            assert data.get("name") == "Torte"
            assert data.get("atributes") == {"velicina": "int" , "okrugla" : "bool"}
            assert data["additional_data"] == {}

            ''' Name is not string'''

            json = {"name":4, "atributes": {"velicina": "int" , "okrugla" : "bool"}, "additional_data":{}}
            response = self.client.post(self.url + "/api/create/category" , json =json)

            if response.status_code == 200:
                data = loads(response.data)
            else:
                data = response.data.decode("UTF-8")
                return
            assert response.status_code == 400
            assert data == "name is not str !"

            ''' Atributes is not dict'''
            
            json = {"name":"Pleasure", "atributes": True, "additional_data":{}}
            response = self.client.post(self.url + "/api/create/category" , json =json)

            if response.status_code == 200:
                data = loads(response.data)
            else:
                data = response.data.decode("UTF-8")
                return
            assert response.status_code == 400
            assert data == "atributes is not dictionry !"

            ''' Additional data is not dict'''
            
            json = {"name":"Pleasure", "atributes": {"velicina": "int" , "okrugla" : "bool"}, "additional_data":False}
            response = self.client.post(self.url + "/api/create/category" , json =json)

            if response.status_code == 200:
                data = loads(response.data)
            else:
                data = response.data.decode("UTF-8")
                return
            assert response.status_code == 400
            assert data == "additional_data not dictionry !"
    
    def test_delete_category_route(self):
        with self.client:
            category = self.create_category()
            response = self.client.delete(self.url + "/api/delete/category/" + str(category.id))

            data = response.data.decode("UTF-8")
            assert response.status_code == 200

            '''Bed id '''

            id = 100001
            category = self.create_category()
            response = self.client.delete(self.url + "/api/delete/category/" + str(id))

            data = response.data.decode("UTF-8")
            assert response.status_code == 400
            assert data =="Category with id " + str(id) + " does not exist !"

    def test_update_category_route(self):
        with self.client:
            category = self.create_category()
            json = {"name":"Tikva", "atributes":{"dimenzije":24}}
            response = self.client.put(self.url + "/api/update/category/" + str(category.id) , json =json)
            if response.status_code == 200:
                data= loads(response.data)
            else:
                data = response.data.decode("UTF-8")
            
            assert response.status_code == 200
            assert data.get("name") == "Tikva"
            assert data.get("atributes") == {"dimenzije":24}

            '''Name is not string '''

            category = self.create_category()
            json = {"name":4, "atributes":{"dimenzije":24}}
            response = self.client.put(self.url + "/api/update/category/" + str(category.id) , json =json)
            if response.status_code == 200:
                data= loads(response.data)
            else:
                data = response.data.decode("UTF-8")
            
            assert response.status_code == 400
            assert data == "name is not str !"

            '''Atributes is not string '''

            category = self.create_category()
            json = {"name":"Tikva", "atributes":False}
            response = self.client.put(self.url + "/api/update/category/" + str(category.id) , json =json)
            if response.status_code == 200:
                data= loads(response.data)
            else:
                data = response.data.decode("UTF-8")
            assert response.status_code == 400
            assert data == "atributes is not dict !"
            

class IntegrationProductTest(DataBaseIntegrationTest):

    def test_create_product_route(self):
        caffe = self.create_caffe()
        category = self.create_category()
        json = {"name" : "Nugat" , "count" : 34, "price":543, "category_id" : category.id , "caffe_id" : caffe.id , "atributes":{"dimenzije":100}, "additional_data" : {} }
        response = self.client.post(self.url + "/api/create/product" , json =json)

        if response.status_code == 200:
            data = loads(response.data)
        else:
            data = response.data.decode("UTF-8")
        
        assert response.status_code == 200
        assert data.get("name") == "Nugat"
        assert data.get("count") == 34
        assert data.get("price") == 543
        assert data.get("category_id") == category.id
        assert data.get("caffe_id") == caffe.id
        assert data.get("atributes") == {"dimenzije":100}

        '''Name is not str'''

        caffe = self.create_caffe()
        category = self.create_category()
        json = {"name" : 4 , "count" : 34, "price":543, "category_id" : category.id , "caffe_id" : caffe.id , "atributes":{"dimenzije":100}, "additional_data" : {} }
        response = self.client.post(self.url + "/api/create/product" , json =json)

        if response.status_code == 200:
            data = loads(response.data)
        else:
            data = response.data.decode("UTF-8")
        
        assert response.status_code == 400
        assert data == "Name is not str !"

        '''Price is not int'''

        caffe = self.create_caffe()
        category = self.create_category()
        json = {"name" : "Nugat" , "count" : 34, "price":"543", "category_id" : category.id , "caffe_id" : caffe.id , "atributes":{"dimenzije":100}, "additional_data" : {} }
        response = self.client.post(self.url + "/api/create/product" , json =json)

        if response.status_code == 200:
            data = loads(response.data)
        else:
            data = response.data.decode("UTF-8")
        
        assert response.status_code == 400
        assert data == "Price is not int !"

        '''Count is not int'''

        caffe = self.create_caffe()
        category = self.create_category()
        json = {"name" : "Nugat" , "count" : "34", "price":543, "category_id" : category.id , "caffe_id" : caffe.id , "atributes":{"dimenzije":100}, "additional_data" : {} }
        response = self.client.post(self.url + "/api/create/product" , json =json)

        if response.status_code == 200:
            data = loads(response.data)
        else:
            data = response.data.decode("UTF-8")
        
        assert response.status_code == 400
        assert data == "Count is not int !"

        '''Atributes is not dict'''

        caffe = self.create_caffe()
        category = self.create_category()
        json = {"name" : "Nugat" , "count" : 34, "price":543, "category_id" : category.id , "caffe_id" : caffe.id , "atributes": 1, "additional_data" : {} }
        response = self.client.post(self.url + "/api/create/product" , json =json)

        if response.status_code == 200:
            data = loads(response.data)
        else:
            data = response.data.decode("UTF-8")
        
        assert response.status_code == 400
        assert data == "Atributes is not dict "

        ''' Bed category key '''

        id = 1111111
        caffe = self.create_caffe()
        category = self.create_category()
        json = {"name" : "Nugat" , "count" : 34, "price":543, "category_id" : id , "caffe_id" : caffe.id , "atributes":{"dimenzije":100}, "additional_data" : {} }
        response = self.client.post(self.url + "/api/create/product" , json =json)

        if response.status_code == 200:
            data = loads(response.data)
        else:
            data = response.data.decode("UTF-8")
        
        assert response.status_code == 400
        assert data == "Category with category_id dont exist !"

        ''' Bed category key '''

        id = 1111111
        caffe = self.create_caffe()
        category = self.create_category()
        json = {"name" : "Nugat" , "count" : 34, "price":543, "category_id" : category.id , "caffe_id" : id , "atributes":{"dimenzije":100}, "additional_data" : {} }
        response = self.client.post(self.url + "/api/create/product" , json =json)

        if response.status_code == 200:
            data = loads(response.data)
        else:
            data = response.data.decode("UTF-8")
        
        assert response.status_code == 400
        assert data == "Caffe with caffe_id dont exist !"

    def test_delete_product_route(self):
        with self.client:
            product = self.create_product()
            response = self.client.delete(self.url + "/api/delete/product/" + str(product.id))

            data = response.data.decode("UTF-8")
            assert response.status_code == 200

            '''Bad id '''
            id = 234
            product = self.create_product()
            response = self.client.delete(self.url + "/api/delete/product/" + str(id))

            data = response.data.decode("UTF-8")
            assert response.status_code == 400
            assert data == "Product with id " + str(id) + " does not exist !"

    def test_update_product_route(self):
        with self.client:
            product = self.create_product()
            json = {"name" : "Twist" , "count" : 1, "price":1433}

            response = self.client.put(self.url + "/api/update/product/" + str(product.id) , json=json)
            if response.status_code == 200:
                data = loads(response.data)
            else:
                data = response.data.decode("UTF-8")

            assert response.status_code == 200
            assert data.get("name") == "Twist"
            assert data.get("count") == 1
            assert data.get("price") == 1433

            '''Bad name'''

            product = self.create_product()
            json = {"name" : 4 , "count" : 1, "price":1433}

            response = self.client.put(self.url + "/api/update/product/" + str(product.id) , json=json)
            if response.status_code == 200:
                data = loads(response.data)
            else:
                data = response.data.decode("UTF-8")

            assert response.status_code == 400
            assert data == "name is not str !"

            '''Bad count'''

            product = self.create_product()
            json = {"name" : "Twist" , "count" : "", "price":1433}

            response = self.client.put(self.url + "/api/update/product/" + str(product.id) , json=json)
            if response.status_code == 200:
                data = loads(response.data)
            else:
                data = response.data.decode("UTF-8")

            assert response.status_code == 400
            assert data == "count is not int !"

            '''Bad price'''

            product = self.create_product()
            json = {"name" : "Twist" , "count" : 67, "price":"1433"}

            response = self.client.put(self.url + "/api/update/product/" + str(product.id) , json=json)
            if response.status_code == 200:
                data = loads(response.data)
            else:
                data = response.data.decode("UTF-8")

            assert response.status_code == 400
            assert data == "price is not int !"









          




    

