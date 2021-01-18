from flask import Blueprint

utils = Blueprint('utils', __name__, template_folder="templates")

from .exceptions import ApiException , BadDataApiException , InternalErrorApiException
from .decorators import handle_api_exception