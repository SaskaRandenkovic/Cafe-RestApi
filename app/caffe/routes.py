"""Routes for app."""

import traceback2 as traceback
from app.caffe import caffe as caffe_bp
from app.caffe import CAFFE_SERVICE as caffe_service , CATEGORY_SERVICE as category_service
from app.caffe import PRODUCT_SERVICE as product_service
from flask import request, Response, json
from app.utils import handle_api_exception


@caffe_bp.route('/api/get/caffe/<id_caffe>', methods=["GET"])
@handle_api_exception
def get_caffe_by_id(id_caffe):
    return caffe_service.get_by_id(id_caffe)

@caffe_bp.route('/api/create/caffe', methods=["POST"])
@handle_api_exception
def create_caffe_route():
    return caffe_service.create_caffe(request)

@caffe_bp.route('/api/delete/caffe/<id_caffe>' , methods = ["DELETE"])
@handle_api_exception
def delete_caffe_route(id_caffe):
    return caffe_service.delete_caffe(id_caffe)

@caffe_bp.route('/api/update/caffe/<id_caffe>' , methods = ["PUT"])
@handle_api_exception
def update_caffe_route(id_caffe):
    return caffe_service.update_caffe(id_caffe,request)

@caffe_bp.route('/api/create/category' , methods = ["POST"])
@handle_api_exception
def create_category_route():
    return category_service.create_category(request)

@caffe_bp.route('/api/delete/category/<id_category>' , methods = ["DELETE"])
@handle_api_exception
def delete_category_route(id_category):
    return category_service.delete_category(id_category)

@caffe_bp.route('/api/update/category/<id_category>' , methods = ["PUT"])
@handle_api_exception
def update_category_route(id_category):
    return category_service.update_category(id_category, request)

@caffe_bp.route('/api/create/product' , methods = ["POST"])
@handle_api_exception
def create_product_route():
    return product_service.create_product(request)

@caffe_bp.route('/api/update/product/<id_product>' , methods = ["PUT"])
@handle_api_exception
def update_product_route(id_product):
    return product_service.update_product(id_product, request)

@caffe_bp.route('/api/delete/product/<id_product>' , methods = ["DELETE"])
@handle_api_exception
def delete_product_route(id_product):
    return product_service.delete_product(id_product)
