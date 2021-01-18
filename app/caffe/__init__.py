from flask import Blueprint

caffe = Blueprint("caffe",__name__)

from app.caffe import models
from app.caffe.service import CAFFE_SERVICE , CATEGORY_SERVICE , PRODUCT_SERVICE
from app.caffe import routes